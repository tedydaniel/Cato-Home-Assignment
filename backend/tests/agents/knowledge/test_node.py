from app.agents.knowledge.node import KnowledgeSearchPlan, build_node


def _state() -> dict:
    return {
        "conversation_id": "conversation-1",
        "customer_context": {"customer_id": "ACC-1001"},
        "messages": [{"role": "user", "content": "Why is BGP flapping?"}],
        "triage_result": {"route": "technical"},
        "diagnostic_evidence": {"findings": [{"fact": "1024 routes out of 1024"}]},
    }


def test_knowledge_node_searches_and_returns_citable_handoff() -> None:
    searched: list[str] = []

    def search(query: str, limit: int) -> dict:
        searched.append(query)
        assert limit == 3
        return {
            "status": "ok",
            "hits": [{
                "article_title": "BGP Prefix Exhaustion",
                "article_url": "https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-prefix-exhaustion.md",
                "section_title": "Identify the issue",
                "excerpt": "The route count has reached the configured limit.",
            }],
        }

    node = build_node(
        query_planner=lambda state: KnowledgeSearchPlan(queries=["BGP prefix exhaustion"]),
        search=search,
    )
    result = node(_state())

    assert searched == ["BGP prefix exhaustion"]
    evidence = result["knowledge_evidence"]
    assert evidence["status"] == "complete"
    assert evidence["citations"][0]["source"].endswith("bgp-prefix-exhaustion.md")
    assert evidence["findings"][0]["fact"] == "The route count has reached the configured limit."
    assert result["knowledge_tool_calls"] == [{"tool_name": "search_knowledge_base", "input": {"query": "BGP prefix exhaustion", "limit": 3}, "output": result["knowledge_tool_calls"][0]["output"]}]


def test_knowledge_node_reports_no_coverage_when_all_searches_are_empty() -> None:
    node = build_node(
        query_planner=lambda state: KnowledgeSearchPlan(queries=["unpublished roadmap"]),
        search=lambda query, limit: {"status": "error", "code": "no_results"},
    )

    assert node(_state())["knowledge_evidence"]["status"] == "no_coverage"


def test_knowledge_node_hides_planner_or_tool_failures() -> None:
    def broken_planner(state):
        raise RuntimeError("provider details must not escape")

    node = build_node(query_planner=broken_planner)

    assert node(_state())["knowledge_evidence"]["status"] == "unavailable"
