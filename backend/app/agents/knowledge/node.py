"""Knowledge specialist: plan searches, retrieve KB evidence, and hand it off."""

from __future__ import annotations

from collections.abc import Callable
from hashlib import sha256
from typing import Any

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from app.agents.knowledge.prompts import build_prompt
from app.config import get_settings
from app.graph.state import SupportState
from app.schemas.handoffs import EvidenceReference, KnowledgeResult
from app.tools.knowledge import search_knowledge_base


class KnowledgeSearchPlan(BaseModel):
    """The small, bounded piece of LLM judgement this specialist needs."""

    queries: list[str] = Field(min_length=1, max_length=3)


QueryPlanner = Callable[[SupportState], KnowledgeSearchPlan]
KnowledgeSearch = Callable[[str, int], dict[str, Any]]


def _last_customer_message(state: SupportState) -> str:
    messages = [message["content"] for message in state["messages"] if message.get("role") == "user" and message.get("content")]
    return "\n".join(messages[-6:]) or "Find the relevant Cato knowledge-base documentation for this case."


def _default_query_planner(state: SupportState) -> KnowledgeSearchPlan:
    settings = get_settings()
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    model = ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key,
        temperature=0,
    ).with_structured_output(KnowledgeSearchPlan)
    result = model.invoke(
        build_prompt(
            customer_message=_last_customer_message(state),
            triage=state.get("triage_result", {}),
            diagnostics=state.get("diagnostic_evidence", {}),
        )
    )
    if not isinstance(result, KnowledgeSearchPlan):
        raise RuntimeError("Knowledge search planner returned an invalid result.")
    return result


def _default_search(query: str, limit: int) -> dict[str, Any]:
    return search_knowledge_base.invoke({"query": query, "limit": limit})


def _evidence_id(article_url: str, section_title: str) -> str:
    slug = article_url.removesuffix(".md").rsplit("/", maxsplit=1)[-1]
    digest = sha256(section_title.encode("utf-8")).hexdigest()[:10]
    return f"kb:{slug}:{digest}"


def _result_from_searches(searches: list[dict[str, Any]]) -> KnowledgeResult:
    if not searches:
        return KnowledgeResult(status="unavailable")
    if all(result.get("status") == "error" for result in searches):
        error_codes = {result.get("code") for result in searches}
        return KnowledgeResult(status="no_coverage" if error_codes == {"no_results"} else "unavailable")

    findings: list[EvidenceReference] = []
    citations: list[EvidenceReference] = []
    retrievals: list[dict[str, object]] = []
    seen: set[str] = set()
    for result in searches:
        for hit in result.get("hits", []):
            evidence_id = _evidence_id(hit["article_url"], hit["section_title"])
            if evidence_id in seen:
                continue
            seen.add(evidence_id)
            retrievals.append({"source": hit["article_url"], "section": hit["section_title"], "score": hit.get("score"), "query": result.get("query")})
            citations.append(EvidenceReference(
                source=hit["article_url"], evidence_id=evidence_id,
                fact=f"{hit['article_title']} — {hit['section_title']}",
            ))
            findings.append(EvidenceReference(
                source=hit["article_url"], evidence_id=evidence_id, fact=hit["excerpt"]
            ))
    return KnowledgeResult(status="complete" if findings else "no_coverage", findings=findings, citations=citations, retrievals=retrievals)


def build_node(
    *, query_planner: QueryPlanner | None = None, search: KnowledgeSearch | None = None,
) -> Callable[[SupportState], dict[str, Any]]:
    """Build a node with injectable boundaries for fast, isolated tests."""
    plan_queries = query_planner or _default_query_planner
    run_search = search or _default_search

    def knowledge_node(state: SupportState) -> dict[str, Any]:
        try:
            plan = plan_queries(state)
            searches = [run_search(query, 3) for query in plan.queries]
            result = _result_from_searches(searches)
            tool_calls = [
                {"tool_name": "search_knowledge_base", "input": {"query": query, "limit": 3}, "output": search}
                for query, search in zip(plan.queries, searches, strict=True)
            ]
        except Exception:
            # Do not reveal infrastructure failures to the customer or the model.
            result = KnowledgeResult(status="unavailable")
            tool_calls = []
        return {"knowledge_evidence": result.model_dump(), "knowledge_tool_calls": tool_calls}

    return knowledge_node
