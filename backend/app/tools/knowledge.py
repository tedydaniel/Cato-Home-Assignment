"""Knowledge-base retrieval tool for the specialised Knowledge agent."""

from __future__ import annotations

from typing import Any, Literal
import re

import psycopg
from langchain.tools import tool
from openai import OpenAI
from pydantic import BaseModel, Field

from app.config import get_settings
from scripts.ingest_kb import EMBEDDING_DIMENSIONS, EMBEDDING_MODEL, vector_literal


class SearchKnowledgeBaseInput(BaseModel):
    query: str = Field(min_length=3, max_length=1_000, description="Technical Cato support question to research.")
    limit: int = Field(default=3, ge=1, le=5, description="Maximum number of cited KB sections to return.")


class KnowledgeHit(BaseModel):
    article_title: str
    article_url: str
    section_title: str
    excerpt: str
    score: float


class KnowledgeEvidence(BaseModel):
    status: Literal["ok"] = "ok"
    tool_name: Literal["search_knowledge_base"] = "search_knowledge_base"
    source: Literal["cato_knowledge_base"] = "cato_knowledge_base"
    query: str
    hits: list[KnowledgeHit]


class KnowledgeSearchError(BaseModel):
    status: Literal["error"] = "error"
    tool_name: Literal["search_knowledge_base"] = "search_knowledge_base"
    code: Literal["unavailable", "no_results"]
    message: str


def _database_url() -> str:
    return get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)


def _embed_query(query: str) -> list[float]:
    api_key = get_settings().openai_api_key
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")
    response = OpenAI(api_key=api_key).embeddings.create(
        model=EMBEDDING_MODEL, dimensions=EMBEDDING_DIMENSIONS, input=query
    )
    return response.data[0].embedding


def _policy_query(query: str) -> str | None:
    text = query.lower()
    intents = ((("credit", "refund", "billing", "compensation"), "service credit refund SLA outage"), (("mfa", "identity", "reset", "admin lockout"), "MFA identity verification reset"), (("sev-1", "sev1", "entire account", "multi-site", "outage"), "Sev-1 escalation incident commander"), (("c2", "verdict", "malware", "whitelist"), "security verdict malware C2 override"), (("psk", "secret", "credential", "password"), "credential hygiene pre-shared key secret"))
    return next((policy for keywords, policy in intents if any(keyword in text for keyword in keywords)), None)


def _rerank(query: str, hits: list[KnowledgeHit], limit: int) -> list[KnowledgeHit]:
    terms = set(re.findall(r"[a-z0-9]{3,}", query.lower()))
    policy_intent = _policy_query(query)
    def score(hit: KnowledgeHit) -> float:
        text = f"{hit.article_title} {hit.section_title} {hit.excerpt}".lower()
        overlap = sum(term in text for term in terms) / max(1, len(terms))
        return hit.score + .02 * overlap + (.05 if policy_intent and hit.article_url.startswith("policy://") else 0)
    return sorted((hit.model_copy(update={"score": score(hit)}) for hit in hits), key=lambda hit: hit.score, reverse=True)[:limit]


def _unsupported_product_request(query: str) -> bool:
    """Requests for unpublished product plans are deliberately out of coverage."""
    text = query.lower()
    return any(phrase in text for phrase in (
        "roadmap", "future feature", "future release", "planned feature", "release date",
    ))


def _has_sufficient_confidence(query: str, hits: list[KnowledgeHit]) -> bool:
    """Use a conservative, explainable gate before grounding an answer.

    RRF scores are only comparable within this retrieval pipeline.  The initial
    0.020 threshold was selected from the saved scenario run: weaker results
    were predominantly broad product-update matches.  A policy intent is
    permitted because it is a governed, local source selected by intent.
    """
    if not hits or _unsupported_product_request(query):
        return False
    if _policy_query(query) and any(hit.article_url.startswith("policy://") for hit in hits):
        return True
    top = hits[0]
    query_terms = set(re.findall(r"[a-z0-9]{3,}", query.lower()))
    hit_terms = set(re.findall(r"[a-z0-9]{3,}", f"{top.article_title} {top.section_title} {top.excerpt}".lower()))
    lexical_overlap = len(query_terms & hit_terms) / max(1, len(query_terms))
    return top.score >= get_settings().knowledge_min_score and lexical_overlap >= 0.10


def retrieve_knowledge(query: str, limit: int) -> list[KnowledgeHit]:
    """Fuse semantic and lexical rankings from the locally pinned KB corpus."""
    query_vector = vector_literal(_embed_query(query))
    sql = """
        WITH semantic AS (
            SELECT chunk_id, row_number() OVER (ORDER BY embedding <=> %s::vector) AS rank
            FROM kb_chunks ORDER BY embedding <=> %s::vector LIMIT 20
        ), lexical AS (
            SELECT chunk_id, row_number() OVER (ORDER BY ts_rank_cd(
                to_tsvector('english', chunk_text), websearch_to_tsquery('english', %s)
            ) DESC) AS rank
            FROM kb_chunks
            WHERE to_tsvector('english', chunk_text) @@ websearch_to_tsquery('english', %s)
            ORDER BY ts_rank_cd(to_tsvector('english', chunk_text), websearch_to_tsquery('english', %s)) DESC LIMIT 20
        ), fused AS (
            SELECT chunk_id, SUM(1.0 / (60 + rank)) AS score FROM (
                SELECT * FROM semantic UNION ALL SELECT * FROM lexical
            ) ranked GROUP BY chunk_id
        )
        SELECT a.article_title, c.article_url, c.section_title,
               left(c.chunk_text, 1200), fused.score
        FROM fused JOIN kb_chunks c USING (chunk_id)
        JOIN kb_articles a ON a.article_url = c.article_url
        ORDER BY fused.score DESC LIMIT 40
    """
    with psycopg.connect(_database_url(), connect_timeout=5) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SET LOCAL statement_timeout = '5000ms'")
            cursor.execute(sql, (query_vector, query_vector, query, query, query))
            rows = cursor.fetchall()
        policy = _policy_query(query)
        if policy:
            with connection.cursor() as policy_cursor:
                policy_cursor.execute("""SELECT a.article_title, c.article_url, c.section_title, left(c.chunk_text, 1200), ts_rank_cd(to_tsvector('english', c.chunk_text), websearch_to_tsquery('english', %s)) FROM kb_chunks c JOIN kb_articles a ON a.article_url = c.article_url WHERE c.article_url LIKE 'policy://%%' ORDER BY ts_rank_cd(to_tsvector('english', c.chunk_text), websearch_to_tsquery('english', %s)) DESC LIMIT 8""", (policy, policy))
                rows.extend(policy_cursor.fetchall())
    hits = [
        KnowledgeHit(
            article_title=row[0], article_url=row[1], section_title=row[2], excerpt=row[3], score=float(row[4])
        )
        for row in rows
    ]
    unique = {(hit.article_url, hit.section_title): hit for hit in hits}
    ranked = _rerank(query, list(unique.values()), limit)
    return ranked if _has_sufficient_confidence(query, ranked) else []


@tool(args_schema=SearchKnowledgeBaseInput)
def search_knowledge_base(query: str, limit: int = 3) -> dict[str, Any]:
    """Find citable Cato KB sections for a technical support question.

    Use before stating product limits, defaults, or troubleshooting steps. The
    returned article URL and section title must be cited in the customer reply.
    """
    try:
        hits = retrieve_knowledge(query, limit)
    except (psycopg.Error, RuntimeError):
        return KnowledgeSearchError(
            code="unavailable", message="The local knowledge base is temporarily unavailable."
        ).model_dump()
    if not hits:
        return KnowledgeSearchError(
            code="no_results", message="No sufficiently relevant Cato KB section was found."
        ).model_dump()
    return KnowledgeEvidence(query=query, hits=hits).model_dump()
