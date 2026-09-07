"""Response specialist that formats validated handoffs into a customer reply."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from app.agents.response.prompts import build_prompt
from app.config import get_settings
from app.graph.state import SupportState
from app.schemas.handoffs import EvidenceReference, ResponseResult


class ResponseDraft(BaseModel):
    message: str = Field(min_length=1, max_length=3_000)


DraftWriter = Callable[[SupportState], ResponseDraft]


def _fallback_message(state: SupportState) -> str:
    triage = state.get("triage_result", {})
    action = state.get("action_result", {})
    knowledge = state.get("knowledge_evidence", {})
    diagnostics = state.get("diagnostic_evidence", {})
    tool_findings = diagnostics.get("findings", [])
    citations = knowledge.get("citations", [])
    if action.get("action") == "approval_request":
        return "I submitted this request for human review. You can continue this conversation while it is pending."
    if triage.get("needs_customer_question"):
        return "I need a little more information to safely identify the account or scope the issue."
    if knowledge.get("status") == "no_coverage":
        return "I could not verify this in the available Cato knowledge base, so I will not guess."
    if knowledge.get("status") == "unavailable":
        return "The knowledge base is temporarily unavailable, so I cannot verify a technical answer yet."
    if tool_findings:
        return tool_findings[0]["fact"] + (" I found related documented guidance." if citations else "")
    if citations:
        return "I found relevant documented Cato guidance for your request."
    return "I have recorded your request and need additional scope before I can provide a verified answer."


def _default_draft_writer(state: SupportState) -> ResponseDraft:
    settings = get_settings()
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")
    evidence = {
        "triage": state.get("triage_result", {}),
        "diagnostics": state.get("diagnostic_evidence", {}),
        "knowledge": state.get("knowledge_evidence", {}),
        "action": state.get("action_result", {}),
    }
    result = ChatOpenAI(model=settings.openai_model, api_key=settings.openai_api_key, temperature=0).with_structured_output(ResponseDraft).invoke(build_prompt(evidence=evidence))
    if not isinstance(result, ResponseDraft):
        raise RuntimeError("Response writer returned an invalid result.")
    return result


def build_node(*, draft_writer: DraftWriter | None = None) -> Callable[[SupportState], dict[str, Any]]:
    """Build a conservative response node with no privileged tool access."""

    write_draft = draft_writer or _default_draft_writer

    def response_node(state: SupportState) -> dict[str, Any]:
        action = state.get("action_result", {})
        knowledge = state.get("knowledge_evidence", {})
        diagnostics = state.get("diagnostic_evidence", {})
        citations = [EvidenceReference.model_validate(citation) for citation in knowledge.get("citations", [])]
        tool_findings = diagnostics.get("findings", [])
        technical_evidence_exists = bool(tool_findings or knowledge.get("findings"))
        credential_redacted = any("[REDACTED]" in message.get("content", "") for message in state["messages"] if message.get("role") == "user")
        if action.get("action") == "approval_request":
            message = _fallback_message(state)
        elif credential_redacted:
            message = "I removed the credential from this conversation for safety. I cannot verify or repeat a secret; please rotate it if it was exposed and use an approved secure channel for replacement details."
        elif technical_evidence_exists and not citations:
            message = "I found diagnostic evidence, but I cannot provide technical guidance until I can verify it against the Cato knowledge base."
        else:
            try:
                message = write_draft(state).message
            except Exception:
                message = _fallback_message(state)

        result = ResponseResult(
            message=message,
            citation_evidence_ids=[citation.evidence_id for citation in citations],
            tool_evidence_ids=[finding["evidence_id"] for finding in tool_findings],
            citations=citations,
        )
        return {"final_response": result.model_dump()}

    return response_node
