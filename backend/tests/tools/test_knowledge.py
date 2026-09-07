from typing import Any

from app.tools import knowledge


def test_policy_intent_and_reranking_promote_governed_evidence() -> None:
    policy = knowledge.KnowledgeHit(article_title="SLA credits", article_url="policy://POL-CREDIT", section_title="Process", excerpt="Credits require approval", score=.01)
    generic = knowledge.KnowledgeHit(article_title="General", article_url="https://kb/general", section_title="Overview", excerpt="General support", score=.02)

    assert knowledge._policy_query("Please request a service credit") == "service credit refund SLA outage"
    assert knowledge._rerank("Please request a service credit", [generic, policy], 2)[0].article_url == "policy://POL-CREDIT"


def _invoke(query: str, limit: int = 3) -> dict[str, Any]:
    assert knowledge.search_knowledge_base.func is not None
    return knowledge.search_knowledge_base.func(query=query, limit=limit)


def test_search_tool_exposes_only_query_and_limit_to_the_model() -> None:
    assert set(knowledge.search_knowledge_base.args_schema.model_fields) == {"query", "limit"}


def test_search_returns_citable_knowledge_evidence(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        knowledge,
        "retrieve_knowledge",
        lambda query, limit: [
            knowledge.KnowledgeHit(
                article_title="BGP Prefix Exhaustion",
                article_url="https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-prefix-exhaustion.md",
                section_title="Identify the Issue",
                excerpt="routes_count is at the configured limit.",
                score=0.03,
            )
        ],
    )

    result = _invoke("Why is BGP flapping?")

    assert result["status"] == "ok"
    assert result["hits"][0]["section_title"] == "Identify the Issue"


def test_search_returns_no_results_when_retrieval_is_empty(monkeypatch: Any) -> None:
    monkeypatch.setattr(knowledge, "retrieve_knowledge", lambda query, limit: [])

    assert _invoke("Unknown roadmap date")["code"] == "no_results"


def test_coverage_gate_rejects_unpublished_roadmap_requests() -> None:
    hit = knowledge.KnowledgeHit(
        article_title="Product update", article_url="https://kb/product-update", section_title="New features",
        excerpt="A previously released feature.", score=0.9,
    )

    assert not knowledge._has_sufficient_confidence("Is this on the future product roadmap?", [hit])


def test_coverage_gate_accepts_a_high_scoring_lexically_supported_hit() -> None:
    hit = knowledge.KnowledgeHit(
        article_title="Configuring BGP neighbors", article_url="https://kb/bgp", section_title="Route limits",
        excerpt="BGP route limits can cause a session to flap.", score=0.03,
    )

    assert knowledge._has_sufficient_confidence("Why is the BGP session flapping at the route limit?", [hit])


def test_search_hides_database_or_embedding_failures(monkeypatch: Any) -> None:
    monkeypatch.setattr(knowledge, "retrieve_knowledge", lambda query, limit: (_ for _ in ()).throw(RuntimeError()))

    assert _invoke("What is DTLS MTU?")["code"] == "unavailable"
