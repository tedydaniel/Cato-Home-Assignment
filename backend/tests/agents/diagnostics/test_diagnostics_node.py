from app.agents.diagnostics.node import build_node


def test_diagnostics_node_returns_tool_derived_evidence() -> None:
    node = build_node(lookup=lambda email, customer: {
        "status": "ok", "source": "telemetry:client_diagnostics",
        "facts": {"last_error": "UDP blocked"},
    })
    result = node({
        "conversation_id": "c-1", "messages": [],
        "customer_context": {"customer_id": "ACC-1", "requester_email": "person@example.com"},
    })

    assert result["diagnostic_evidence"]["status"] == "complete"
    assert result["diagnostic_evidence"]["findings"][0]["source"] == "telemetry:client_diagnostics"
    assert result["diagnostic_evidence"]["suggested_knowledge_queries"] == ["Cato Client troubleshooting UDP blocked"]
    assert result["diagnostic_tool_calls"][0]["tool_name"] == "get_client_diagnostics"


def test_diagnostics_node_does_not_run_without_trusted_scope() -> None:
    node = build_node(lookup=lambda email, customer: (_ for _ in ()).throw(AssertionError("must not run")))
    result = node({"conversation_id": "c-1", "messages": [], "customer_context": {}})

    assert result["diagnostic_evidence"]["status"] == "needs_scope"


def test_diagnostics_node_turns_site_bgp_evidence_into_a_kb_query() -> None:
    node = build_node(site_lookup=lambda site, customer: [{
        "status": "ok", "tool_name": "get_bgp_status", "source": "telemetry:bgp_status",
        "facts": {"neighbors": [{"peer_ip": "10.20.0.2", "state": "Established", "routes_count": 1024, "routes_limit": 1024, "last_error": "Hold Timer Expired"}]},
    }])
    result = node({
        "conversation_id": "c-1", "messages": [],
        "customer_context": {"customer_id": "ACC-1007", "requester_email": "admin@example.com"},
        "triage_result": {"site_id": "S-1007-01"},
    })

    assert result["diagnostic_evidence"]["findings"][0]["evidence_id"] == "tool:bgp:S-1007-01:10.20.0.2"
    assert result["diagnostic_evidence"]["suggested_knowledge_queries"] == ["Cato BGP route limit prefix exhaustion Hold Timer Expired"]
    assert result["diagnostic_tool_calls"][0]["input"] == {"site_id": "S-1007-01"}
