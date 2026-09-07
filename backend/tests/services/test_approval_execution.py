from uuid import UUID

from app.schemas.approvals import ApprovalRequest
from app.services import approval_execution


def test_approved_request_creates_a_durable_continuation_reply(monkeypatch) -> None:
    request = ApprovalRequest(
        approval_id=UUID("0c4b2289-9b9f-4874-9342-5e5e26557adc"), conversation_id=UUID("6f41632c-992f-46fd-8df1-d1c57e5505b5"),
        customer_id="ACC-1001", action_type="service_credit", reason="Outage", proposed_payload={}, evidence_ids=[], idempotency_key="key", status="approved",
    )
    recorded: dict = {}
    monkeypatch.setattr(approval_execution, "mark_executed", lambda approval_id, result: request.model_copy(update={"status": "executed"}))
    monkeypatch.setattr(approval_execution, "resume_support_graph", lambda conversation_id, decision: {"final_response": {"message": "completed", "citations": []}})
    monkeypatch.setattr(approval_execution, "record_completed", lambda conversation_id, state: UUID("4a76132c-992f-46fd-8df1-d1c57e5505b5"))
    monkeypatch.setattr(approval_execution.conversations, "append", lambda conversation_id, role, content, metadata: recorded.update({"role": role, "content": content, "metadata": metadata}))

    result = approval_execution.resume_review_decision(request)

    assert result.status == "executed"
    assert recorded["role"] == "agent"
    assert recorded["content"] == "completed"
    assert recorded["metadata"]["approval_id"] == str(request.approval_id)


def test_rejected_request_resumes_the_checkpoint_without_executing(monkeypatch) -> None:
    request = ApprovalRequest(
        approval_id=UUID("0c4b2289-9b9f-4874-9342-5e5e26557adc"), conversation_id=UUID("6f41632c-992f-46fd-8df1-d1c57e5505b5"),
        customer_id="ACC-1001", action_type="service_credit", reason="Outage", proposed_payload={}, evidence_ids=[], idempotency_key="key", status="rejected",
    )
    decisions: list[str] = []
    monkeypatch.setattr(approval_execution, "mark_executed", lambda *_: (_ for _ in ()).throw(AssertionError("must not execute")))
    monkeypatch.setattr(approval_execution, "resume_support_graph", lambda conversation_id, decision: decisions.append(decision) or {"final_response": {"message": "declined", "citations": []}})
    monkeypatch.setattr(approval_execution, "record_completed", lambda *_: UUID("4a76132c-992f-46fd-8df1-d1c57e5505b5"))
    monkeypatch.setattr(approval_execution.conversations, "append", lambda *_: None)

    result = approval_execution.resume_review_decision(request)

    assert result.status == "rejected"
    assert decisions == ["rejected"]
