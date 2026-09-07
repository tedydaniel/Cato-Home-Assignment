"""Triage specialist: establish trusted context then classify graph routing."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from langchain_openai import ChatOpenAI

from app.agents.triage.prompts import build_prompt
from app.config import get_settings
from app.graph.state import SupportState
from app.repositories.support_context import get_triage_context
from app.schemas.handoffs import TriageResult
from app.schemas.triage import TrustedTriageContext


ContextLookup = Callable[[str], TrustedTriageContext | None]
RouteClassifier = Callable[[SupportState, TrustedTriageContext], TriageResult]


def _last_customer_message(state: SupportState) -> str:
    for message in reversed(state["messages"]):
        if message.get("role") == "user" and message.get("content"):
            return message["content"]
    return ""


def _conversation_text(state: SupportState) -> str:
    return "\n".join(message.get("content", "") for message in state["messages"] if message.get("role") == "user").lower()


def _deterministic_route(state: SupportState) -> TriageResult | None:
    text = _conversation_text(state)
    protected = (("service_credit", ("credit", "refund", "compensation")), ("mfa_reset", ("mfa reset", "reset my mfa")), ("c2_verdict_override", ("c2", "verdict override", "whitelist")))
    for action, phrases in protected:
        if any(phrase in text for phrase in phrases):
            return TriageResult(route="action", protected_action=action, summary="A protected request requires policy evidence and human review.")
    if any(phrase in text for phrase in ("all sites down", "entire account", "multiple sites down", "complete loss of connectivity")) or ("site" in text and any(word in text for word in ("unreachable", "offline", "down")) and any(word in text for word in ("multiple", "several", "three", "regional", "germany"))):
        return TriageResult(route="technical", priority="P1", summary="Potential Sev-1 outage requires immediate human escalation.")
    return None


def _default_classifier(state: SupportState, context: TrustedTriageContext) -> TriageResult:
    settings = get_settings()
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")
    model = ChatOpenAI(
        model=settings.openai_model, api_key=settings.openai_api_key, temperature=0,
    ).with_structured_output(TriageResult)
    result = model.invoke(build_prompt(customer_message=_last_customer_message(state), context=context))
    if not isinstance(result, TriageResult):
        raise RuntimeError("Triage classifier returned an invalid result.")
    return result


def _safe_fallback(summary: str) -> TriageResult:
    return TriageResult(route="knowledge", needs_customer_question=True, summary=summary)


def build_node(
    *, context_lookup: ContextLookup | None = None, classifier: RouteClassifier | None = None,
) -> Callable[[SupportState], dict[str, Any]]:
    """Build Triage with injectable database and model boundaries for tests."""
    load_context = context_lookup or get_triage_context
    classify = classifier or _default_classifier

    def triage_node(state: SupportState) -> dict[str, Any]:
        requester_email = state["customer_context"].get("requester_email", "")
        try:
            context = load_context(requester_email)
        except Exception:
            context = None
        if context is None:
            return {
                "customer_context": {"requester_email": requester_email, "identity_verified": False},
                "ticket_history": [],
                "triage_result": _safe_fallback("Account identity could not be verified.").model_dump(),
            }
        try:
            result = _deterministic_route(state) or classify(state, context)
        except Exception:
            result = _safe_fallback("Triage classification is temporarily unavailable.")
        valid_site_ids = {site.site_id for site in context.sites}
        if result.site_id not in valid_site_ids:
            result = result.model_copy(update={"site_id": None})
        if result.site_id is None:
            matched = next((site.site_id for site in context.sites if site.name.lower() in _conversation_text(state)), None)
            result = result.model_copy(update={"site_id": matched})
        update = {
            "customer_context": {
                "customer_id": context.customer_id,
                "company": context.company,
                "tier": context.tier,
                "requester_email": context.requester_email,
                "identity_verified": context.identity_verified,
                "sites": [site.model_dump() for site in context.sites],
            },
            "ticket_history": [entry.model_dump(mode="json") for entry in context.ticket_history],
            "triage_result": result.model_dump(),
        }
        if result.route == "action" and (result.protected_action or result.requested_action):
            update["action_request"] = {
                "action_type": result.protected_action or result.requested_action,
                "reason": result.summary,
                "evidence_ids": [],
            }
        return update

    return triage_node
