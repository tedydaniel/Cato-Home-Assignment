"""Diagnostics specialist for customer-scoped Cato Client telemetry."""

from __future__ import annotations

from collections.abc import Callable
from types import SimpleNamespace
from typing import Any

from app.graph.state import SupportState
from app.schemas.handoffs import DiagnosticsResult, EvidenceReference
from app.tools.diagnostics import get_client_diagnostics
from app.tools.site_diagnostics import get_bgp_status, get_events, get_ipsec_status, get_link_quality, get_site_status


DiagnosticsLookup = Callable[[str, str], dict[str, Any]]
SiteLookup = Callable[[str, str], list[dict[str, Any]]]


def _default_lookup(user_email: str, customer_id: str) -> dict[str, Any]:
    """Invoke the existing tool with graph-owned customer scope.

    The model never provides the customer ID; the node obtains it from trusted
    Triage context before invoking the telemetry tool.
    """
    assert get_client_diagnostics.func is not None
    runtime = SimpleNamespace(context={"customer_id": customer_id})
    return get_client_diagnostics.func(user_email=user_email, runtime=runtime)


def _default_site_lookup(site_id: str, customer_id: str) -> list[dict[str, Any]]:
    runtime = SimpleNamespace(context={"customer_id": customer_id})
    tools = (get_site_status, get_bgp_status, get_ipsec_status, get_link_quality, get_events)
    return [tool.func(site_id=site_id, runtime=runtime) for tool in tools if tool.func is not None]


def build_node(*, lookup: DiagnosticsLookup | None = None, site_lookup: SiteLookup | None = None) -> Callable[[SupportState], dict[str, Any]]:
    run_lookup = lookup or _default_lookup
    run_site_lookup = site_lookup or _default_site_lookup

    def diagnostics_node(state: SupportState) -> dict[str, Any]:
        context = state["customer_context"]
        customer_id = context.get("customer_id")
        requester_email = context.get("requester_email")
        site_id = state.get("triage_result", {}).get("site_id")
        if not customer_id:
            result = DiagnosticsResult(status="needs_scope")
            tool_calls: list[dict[str, Any]] = []
        elif site_id:
            try:
                evidence = run_site_lookup(site_id, customer_id)
            except Exception:
                evidence = []
            tool_calls = [
                {"tool_name": item.get("tool_name", "unknown"), "input": {"site_id": site_id}, "output": item}
                for item in evidence
            ]
            successful = [item for item in evidence if item.get("status") == "ok"]
            findings: list[EvidenceReference] = []
            queries: list[str] = []
            for item in successful:
                tool_name = item["tool_name"]
                facts = item["facts"]
                if tool_name == "get_bgp_status":
                    for neighbor in facts["neighbors"]:
                        findings.append(EvidenceReference(source=item["source"], evidence_id=f"tool:bgp:{site_id}:{neighbor['peer_ip']}", fact=f"BGP peer {neighbor['peer_ip']}: {neighbor['state']}, routes {neighbor['routes_count']}/{neighbor['routes_limit']}, last error {neighbor['last_error']}."))
                    queries.append("Cato BGP route limit prefix exhaustion Hold Timer Expired")
                elif tool_name == "get_ipsec_status":
                    findings.append(EvidenceReference(source=item["source"], evidence_id=f"tool:ipsec:{site_id}", fact=f"IPsec primary tunnel is {facts['primary']['status']}; last error {facts['primary']['last_error']}."))
                    queries.append(f"Cato IPsec troubleshooting {facts['primary']['last_error']}")
                elif tool_name == "get_link_quality":
                    for link in facts["links"]:
                        findings.append(EvidenceReference(source=item["source"], evidence_id=f"tool:link:{site_id}:{link['link']}", fact=f"{link['link']} maximum loss {link['max_packet_loss_pct']}%, latency {link['max_latency_ms']} ms, jitter {link['max_jitter_ms']} ms."))
            result = DiagnosticsResult(status="complete" if findings else "unavailable", findings=findings, suggested_knowledge_queries=queries[:3])
        elif not requester_email:
            result = DiagnosticsResult(status="needs_scope")
            tool_calls = []
        else:
            try:
                evidence = run_lookup(requester_email, customer_id)
            except Exception:
                evidence = {"status": "error", "code": "unavailable"}
            tool_calls = [{
                "tool_name": evidence.get("tool_name", "get_client_diagnostics"),
                "input": {"user_email": requester_email},
                "output": evidence,
            }]
            if evidence.get("status") != "ok":
                result = DiagnosticsResult(status="unavailable")
            else:
                facts = evidence["facts"]
                evidence_id = f"tool:client:{requester_email.lower()}"
                result = DiagnosticsResult(
                    status="complete",
                    findings=[EvidenceReference(
                        source=evidence["source"], evidence_id=evidence_id,
                        fact=f"Cato Client last error: {facts['last_error']}",
                    )],
                    suggested_knowledge_queries=[
                        f"Cato Client troubleshooting {facts['last_error']}"
                    ],
                )
        return {"diagnostic_evidence": result.model_dump(), "diagnostic_tool_calls": tool_calls}

    return diagnostics_node
