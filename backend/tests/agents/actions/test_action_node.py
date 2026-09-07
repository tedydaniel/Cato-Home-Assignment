from app.agents.actions import node as action_node_module
from app.agents.actions.node import build_node
from app.schemas.approvals import ApprovalRequest


def _state(action_request: dict, *, identity_verified: bool = True) -> dict:
    return {
        "conversation_id": "6f41632c-992f-46fd-8df1-d1c57e5505b5",
        "customer_context": {"customer_id": "ACC-1001", "requester_email": "netops@northwind-logistics.com", "identity_verified": identity_verified},
        "messages": [],
        "action_request": action_request,
    }


def test_protected_action_creates_a_pending_approval_request() -> None:
    created: list[ApprovalRequest] = []

    def save(request: ApprovalRequest) -> ApprovalRequest:
        created.append(request)
        return request

    node = build_node(create_approval=save)
    result = node(_state({
        "action_type": "service_credit", "reason": "Verified qualifying outage.",
        "payload": {"incident_ids": ["INC-42"]}, "evidence_ids": ["tool:incident:42"],
    }))

    assert result["action_result"]["action"] == "approval_request"
    assert result["action_result"]["approval_id"] == str(created[0].approval_id)
    assert created[0].status == "pending"
    assert created[0].customer_id == "ACC-1001"
    assert created[0].evidence_ids == ["tool:incident:42"]


def test_unverified_mfa_reset_never_creates_an_approval_request() -> None:
    node = build_node(create_approval=lambda request: (_ for _ in ()).throw(AssertionError("must not save")))

    result = node(_state(
        {"action_type": "mfa_reset", "reason": "Customer asked for a reset."}, identity_verified=False
    ))

    assert result["action_result"]["action"] == "none"
    assert "identity is verified" in result["action_result"]["summary"]


def test_p1_creates_a_durable_sev1_escalation() -> None:
    node = build_node(create_sev1_alert=lambda customer, conversation, summary: "alert-1")

    result = node({**_state({}), "triage_result": {"priority": "P1", "summary": "Entire account offline"}})

    assert result["action_result"]["action"] == "escalate_sev1"
    assert result["action_result"]["ticket_id"] == "alert-1"


def test_ticket_request_creates_a_simulated_ticket() -> None:
    node = build_node(create_support_ticket=lambda customer, email, subject, priority: "SIM-1")

    result = node(_state({"action_type": "ticket_create", "reason": "Please open a ticket."}))

    assert result["action_result"]["action"] == "ticket_create"
    assert result["action_result"]["ticket_id"] == "SIM-1"


def test_duplicate_proposal_uses_the_same_idempotency_key() -> None:
    captured: list[str] = []

    def save(request: ApprovalRequest) -> ApprovalRequest:
        captured.append(request.idempotency_key)
        return request

    node = build_node(create_approval=save)
    state = _state({"action_type": "c2_verdict_override", "reason": "Requested override."})

    node(state)
    node(state)

    assert len(captured) == 2
    assert captured[0] == captured[1]


def test_approved_interrupt_continues_without_creating_a_second_approval(monkeypatch) -> None:
    created: list[ApprovalRequest] = []
    monkeypatch.setattr(action_node_module, "interrupt", lambda payload: {"decision": "approved"})
    node = build_node(create_approval=lambda request: created.append(request) or request, pause_for_review=True)

    result = node(_state({"action_type": "service_credit", "reason": "Verified qualifying outage."}))

    assert len(created) == 1
    assert result["action_result"]["action"] == "none"
    assert "resumed" in result["action_result"]["summary"]
