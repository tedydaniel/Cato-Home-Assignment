from typing import Any, NotRequired, TypedDict


class SupportState(TypedDict):
    """Shared case file. Each specialist writes only its named handoff field."""

    conversation_id: str
    customer_context: dict[str, Any]
    messages: list[dict[str, str]]
    ticket_history: NotRequired[list[dict[str, Any]]]
    triage_result: NotRequired[dict[str, Any]]
    diagnostic_evidence: NotRequired[dict[str, Any]]
    diagnostic_tool_calls: NotRequired[list[dict[str, Any]]]
    knowledge_evidence: NotRequired[dict[str, Any]]
    knowledge_tool_calls: NotRequired[list[dict[str, Any]]]
    action_request: NotRequired[dict[str, Any]]
    action_result: NotRequired[dict[str, Any]]
    final_response: NotRequired[dict[str, Any]]
