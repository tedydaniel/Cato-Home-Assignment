"""Action specialist that gates protected actions behind a human decision."""

from __future__ import annotations

import json
from collections.abc import Callable
from hashlib import sha256
from typing import Any, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from app.graph.state import SupportState
from app.repositories.approvals import create_or_get
from app.repositories.alerts import create_sev1
from app.repositories.tickets import create as create_ticket
from app.schemas.approvals import ApprovalRequest, ProtectedAction
from app.schemas.handoffs import ActionResult
from langgraph.types import interrupt


class ProposedProtectedAction(BaseModel):
    action_type: ProtectedAction | Literal["ticket_create"]
    reason: str = Field(min_length=1, max_length=2_000)
    payload: dict[str, Any] = Field(default_factory=dict)
    evidence_ids: list[str] = Field(default_factory=list)


ApprovalCreator = Callable[[ApprovalRequest], ApprovalRequest]
Sev1Creator = Callable[[str, UUID, str], str]
TicketCreator = Callable[[str, str, str, str], str]


def _idempotency_key(conversation_id: str, action: ProposedProtectedAction) -> str:
    stable_payload = json.dumps(action.payload, sort_keys=True, separators=(",", ":"))
    material = f"{conversation_id}:{action.action_type}:{stable_payload}"
    return sha256(material.encode("utf-8")).hexdigest()


def _proposal_from_state(state: SupportState) -> ProposedProtectedAction | None:
    raw = state.get("action_request")
    return ProposedProtectedAction.model_validate(raw) if raw else None


def _mfa_identity_is_verified(state: SupportState) -> bool:
    return state["customer_context"].get("identity_verified") is True


def build_node(*, create_approval: ApprovalCreator | None = None, create_sev1_alert: Sev1Creator | None = None, create_support_ticket: TicketCreator | None = None, pause_for_review: bool = False) -> Callable[[SupportState], dict[str, Any]]:
    """Create a durable approval work item; never execute the protected action."""
    save_approval = create_approval or create_or_get
    save_sev1 = create_sev1_alert or create_sev1
    save_ticket = create_support_ticket or create_ticket

    def action_node(state: SupportState) -> dict[str, Any]:
        if state.get("triage_result", {}).get("priority") == "P1":
            try:
                alert_id = save_sev1(state["customer_context"]["customer_id"], UUID(state["conversation_id"]), state["triage_result"].get("summary", "Sev-1 escalation"))
                return {"action_result": ActionResult(action="escalate_sev1", ticket_id=alert_id, summary="A Sev-1 escalation was sent to the human incident commander.").model_dump()}
            except Exception:
                return {"action_result": ActionResult(action="approval_unavailable", summary="The Sev-1 escalation could not be submitted.").model_dump()}
        proposal = _proposal_from_state(state)
        if proposal is None:
            return {"action_result": ActionResult(action="none", summary="No protected action was requested.").model_dump()}
        if proposal.action_type == "ticket_create":
            try:
                ticket_id = save_ticket(state["customer_context"]["customer_id"], state["customer_context"]["requester_email"], proposal.reason, state.get("triage_result", {}).get("priority") or "P3")
                return {"action_result": ActionResult(action="ticket_create", ticket_id=ticket_id, summary="A support ticket was created.").model_dump()}
            except Exception:
                return {"action_result": ActionResult(action="approval_unavailable", summary="The support ticket could not be created.").model_dump()}
        if proposal.action_type == "mfa_reset" and not _mfa_identity_is_verified(state):
            return {"action_result": ActionResult(
                action="none", summary="The MFA reset cannot proceed until identity is verified."
            ).model_dump()}
        try:
            request = ApprovalRequest(
                approval_id=uuid4(), conversation_id=UUID(state["conversation_id"]),
                customer_id=state["customer_context"]["customer_id"], action_type=proposal.action_type,
                reason=proposal.reason, proposed_payload=proposal.payload, evidence_ids=proposal.evidence_ids,
                idempotency_key=_idempotency_key(state["conversation_id"], proposal), status="pending",
            )
            saved = save_approval(request)
        except Exception:
            return {"action_result": ActionResult(
                action="approval_unavailable", summary="The approval request could not be submitted."
            ).model_dump()}
        if pause_for_review:
            decision = interrupt({"approval_id": str(saved.approval_id), "action_type": saved.action_type, "reason": saved.reason})
            if isinstance(decision, dict) and decision.get("decision") == "approved":
                return {"action_result": ActionResult(action="none", approval_id=str(saved.approval_id), summary="The approved action was recorded and the case resumed.").model_dump()}
            if isinstance(decision, dict) and decision.get("decision") == "rejected":
                return {"action_result": ActionResult(action="none", approval_id=str(saved.approval_id), summary="The reviewer declined the protected request.").model_dump()}
        return {"action_result": ActionResult(
            action="approval_request", approval_id=str(saved.approval_id),
            summary="The protected action is pending human approval."
        ).model_dump()}

    return action_node
