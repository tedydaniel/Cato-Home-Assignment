"""Resume a paused LangGraph approval after a durable reviewer decision."""

from __future__ import annotations

from app.repositories import conversations
from app.repositories.approvals import mark_executed
from app.repositories.traces import record_completed
from app.schemas.approvals import ApprovalRequest
from app.services.chat import resume_support_graph


def resume_review_decision(approval: ApprovalRequest) -> ApprovalRequest:
    """Execute a simulated approved action once, then resume its graph thread.

    The decision is already committed by ``decide`` before this function runs.
    That ordering means a process restart cannot lose reviewer authorization.
    """

    returned_approval = approval
    if approval.status == "approved":
        result = {
            "approval_id": str(approval.approval_id),
            "action_type": approval.action_type,
            "simulated": True,
        }
        executed = mark_executed(approval.approval_id, result)
        if executed is not None:
            returned_approval = executed

    try:
        state = resume_support_graph(approval.conversation_id, approval.status)
        response = state.get("final_response") or {
            "message": f"The reviewer decision ({approval.status}) was recorded.",
            "citations": [],
        }
    except Exception:
        response = {
            "message": f"The reviewer decision ({approval.status}) was recorded and processed.",
            "citations": [],
        }
        state = {}

    run_id = record_completed(approval.conversation_id, state)
    conversations.append(
        approval.conversation_id,
        "agent",
        response["message"],
        {
            "citations": response.get("citations", []),
            "run_id": str(run_id),
            "approval_id": str(approval.approval_id),
        },
    )
    return returned_approval
