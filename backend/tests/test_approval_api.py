from uuid import UUID

import pytest
from fastapi import HTTPException

from app import main
from app.schemas.approvals import ApprovalDecision, ApprovalRequest


def _approval(status: str = "pending") -> ApprovalRequest:
    return ApprovalRequest(
        approval_id=UUID("0c4b2289-9b9f-4874-9342-5e5e26557adc"),
        conversation_id=UUID("6f41632c-992f-46fd-8df1-d1c57e5505b5"),
        customer_id="ACC-1001", action_type="service_credit", reason="Verified outage.",
        proposed_payload={}, evidence_ids=[], idempotency_key="key", status=status,
    )


def test_pending_approval_endpoint_delegates_to_the_store(monkeypatch) -> None:
    monkeypatch.setattr(main, "list_requests", lambda status: [_approval()])

    result = main.approvals("pending")

    assert result[0].status == "pending"


def test_reviewer_decision_endpoint_returns_the_atomic_transition(monkeypatch) -> None:
    monkeypatch.setattr(main, "decide", lambda approval_id, decision: _approval("approved"))
    monkeypatch.setattr(main, "resume_review_decision", lambda approval: approval)

    result = main.decide_approval(
        UUID("0c4b2289-9b9f-4874-9342-5e5e26557adc"),
        ApprovalDecision(decision="approved", reviewer="reviewer@cato.example"),
    )

    assert result.status == "approved"


def test_reviewer_decision_rejects_a_request_that_is_no_longer_pending(monkeypatch) -> None:
    monkeypatch.setattr(main, "decide", lambda approval_id, decision: None)

    with pytest.raises(HTTPException) as error:
        main.decide_approval(
            UUID("0c4b2289-9b9f-4874-9342-5e5e26557adc"),
            ApprovalDecision(decision="rejected", reviewer="reviewer@cato.example"),
        )

    assert error.value.status_code == 409


def test_reviewer_can_edit_a_pending_request(monkeypatch) -> None:
    monkeypatch.setattr(main, "decide", lambda approval_id, decision: _approval("pending"))

    result = main.decide_approval(UUID("0c4b2289-9b9f-4874-9342-5e5e26557adc"), ApprovalDecision(decision="edit", reviewer="reviewer@cato.example", edited_payload={"memo": "revised"}))

    assert result.status == "pending"
