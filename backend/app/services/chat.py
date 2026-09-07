"""Run one durable customer turn through the composed support graph."""

from __future__ import annotations

from typing import Any
from uuid import UUID

from langgraph.types import Command

from app.graph.checkpoints import application_graph
from app.repositories import conversations
from app.repositories import traces
from app.schemas.conversations import ChatTurn, ConversationView
from app.safety.prompt_injection import detect_prompt_injection
from app.safety.redaction import redact_secrets


def run_support_graph(state: dict[str, Any], *, tags: list[str] | None = None) -> dict[str, Any]:
    with application_graph() as graph:
        return graph.invoke(
            state,
            config={"configurable": {"thread_id": state["conversation_id"]}, "tags": tags or []},
        )


def resume_support_graph(conversation_id: UUID, decision: str) -> dict[str, Any]:
    """Continue the paused graph associated with one durable conversation."""
    with application_graph() as graph:
        return graph.invoke(
            Command(resume={"decision": decision}),
            config={"configurable": {"thread_id": str(conversation_id)}},
        )


def send_message(conversation_id: UUID, content: str, *, trace_tags: list[str] | None = None) -> ChatTurn | None:
    safe_content = redact_secrets(content)
    injection = detect_prompt_injection(safe_content)
    metadata = {"guardrail": {"prompt_injection_detected": injection.detected, "signals": list(injection.signals)}}
    conversation = conversations.append(conversation_id, "customer", safe_content, metadata)
    if conversation is None:
        return None
    if injection.detected:
        response = {
            "message": "I can help with Cato support questions, but I cannot process requests to override system controls or reveal internal instructions. Please describe the technical issue or account request directly.",
            "citation_evidence_ids": [], "tool_evidence_ids": [], "citations": [],
        }
        updated = conversations.append(conversation_id, "agent", response["message"], {"citations": [], "guardrail": metadata["guardrail"]})
        assert updated is not None
        state = {"conversation_id": str(conversation_id), "guardrail": metadata["guardrail"], "final_response": response}
        return ChatTurn(conversation=updated, response=response, state=state)
    graph_input = {
        "conversation_id": str(conversation.conversation_id),
        "customer_context": {"requester_email": conversation.requester_email},
        "messages": [{"role": "user" if message.role == "customer" else "assistant", "content": message.content}
                     for message in conversation.messages],
    }
    state = run_support_graph(graph_input, tags=trace_tags) if trace_tags else run_support_graph(graph_input)
    response = state.get("final_response")
    if response is None:
        # The action agent has persisted an approval request and interrupted the
        # graph.  The customer can keep talking; this particular run continues
        # only when a reviewer resumes its checkpoint.
        response = {
            "message": "I submitted this request for human review. You can continue this conversation while it is pending.",
            "citation_evidence_ids": [],
            "tool_evidence_ids": [],
            "citations": state.get("knowledge_evidence", {}).get("citations", []),
        }
        updated = conversations.append(
            conversation_id,
            "agent",
            response["message"],
            {"citations": response["citations"], "approval_pending": True},
        )
        assert updated is not None
        return ChatTurn(conversation=updated, response=response, state=state)
    run_id = traces.record_completed(conversation_id, state)
    updated = conversations.append(conversation_id, "agent", response["message"], {"citations": response.get("citations", []), "run_id": str(run_id)})
    assert updated is not None
    return ChatTurn(conversation=updated, response=response, state=state)
