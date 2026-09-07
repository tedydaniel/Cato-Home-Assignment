from scripts.evaluate_scenarios import score


def test_scenario_score_requires_expected_public_citation() -> None:
    result = score({"action": "auto_resolve", "must_cite": ["bgp-article"], "must_use_tools": ["get_bgp_status"]}, {"citations": [{"source": "https://kb/bgp-article.md"}]}, {"action_result": {"action": "none"}, "diagnostic_tool_calls": [{"tool_name": "get_bgp_status", "output": {"source": "telemetry:bgp_status"}}]})

    assert result == {"citations": True, "tools": True, "action": True}
