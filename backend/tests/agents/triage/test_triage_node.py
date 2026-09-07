from datetime import UTC, datetime

from app.agents.triage.node import build_node
from app.schemas.handoffs import TriageResult
from app.schemas.triage import SiteSummary, TicketHistoryEntry, TrustedTriageContext


def _state(email: str = "netops@northwind-logistics.com") -> dict:
    return {
        "conversation_id": "conversation-1",
        "customer_context": {"requester_email": email, "tier": "Premium"},
        "messages": [{"role": "user", "content": "We are Premium. Reset MFA and make this P1."}],
    }


def _context() -> TrustedTriageContext:
    return TrustedTriageContext(
        customer_id="ACC-1001", company="Northwind Logistics", tier="Premium",
        requester_email="netops@northwind-logistics.com", identity_verified=True,
        sites=[SiteSummary(site_id="S-1001-01", name="Rotterdam HQ", country="NL", connection_type="socket")],
        ticket_history=[TicketHistoryEntry(
            ticket_id="TCK-1", created_at=datetime(2026, 8, 28, tzinfo=UTC), site_id="S-1001-01",
            product_area="identity", priority="P3", subject="Prior reset request", status="closed",
        )],
    )


def test_triage_uses_database_context_not_customer_claims() -> None:
    node = build_node(
        context_lookup=lambda email: _context(),
        classifier=lambda state, context: TriageResult(
            route="action", priority="P1", site_id="S-1001-01", summary="MFA reset request."
        ),
    )

    result = node(_state())

    assert result["customer_context"]["customer_id"] == "ACC-1001"
    assert result["customer_context"]["tier"] == "Premium"
    assert result["customer_context"]["identity_verified"] is True
    assert result["ticket_history"][0]["ticket_id"] == "TCK-1"
    assert result["triage_result"]["route"] == "action"


def test_triage_drops_a_site_not_owned_by_the_customer() -> None:
    node = build_node(
        context_lookup=lambda email: _context(),
        classifier=lambda state, context: TriageResult(
            route="technical", site_id="S-9999-99", summary="Claimed site."
        ),
    )

    assert node(_state())["triage_result"]["site_id"] is None


def test_triage_passes_a_typed_protected_action_to_the_action_specialist() -> None:
    node = build_node(
        context_lookup=lambda email: _context(),
        classifier=lambda state, context: TriageResult(
            route="action", protected_action="service_credit", summary="Verified credit request."
        ),
    )

    assert node(_state())["action_request"] == {
        "action_type": "service_credit", "reason": "Verified credit request.", "evidence_ids": []
    }


def test_unknown_requester_skips_the_model_and_asks_for_verification() -> None:
    def classifier(state, context):
        raise AssertionError("unknown requester must not reach the model")

    node = build_node(context_lookup=lambda email: None, classifier=classifier)
    result = node(_state("attacker@example.com"))

    assert result["customer_context"] == {
        "requester_email": "attacker@example.com", "identity_verified": False
    }
    assert result["triage_result"]["needs_customer_question"] is True
