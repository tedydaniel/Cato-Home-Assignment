"""Persistable contracts used when specialised agents hand work to each other."""

from typing import Literal

from pydantic import BaseModel, Field


class EvidenceReference(BaseModel):
    source: str
    evidence_id: str
    fact: str


class TriageResult(BaseModel):
    route: Literal["technical", "knowledge", "action"]
    priority: Literal["P1", "P2", "P3", "P4"] | None = None
    site_id: str | None = None
    needs_customer_question: bool = False
    summary: str


class DiagnosticsResult(BaseModel):
    status: Literal["complete", "unavailable", "needs_scope"]
    findings: list[EvidenceReference] = Field(default_factory=list)
    suggested_knowledge_queries: list[str] = Field(default_factory=list)


class KnowledgeResult(BaseModel):
    status: Literal["complete", "no_coverage", "unavailable"]
    findings: list[EvidenceReference] = Field(default_factory=list)
    citations: list[EvidenceReference] = Field(default_factory=list)


class ActionResult(BaseModel):
    action: Literal["none", "ticket_update", "ticket_create", "escalate_sev1", "approval_request"]
    ticket_id: str | None = None
    approval_id: str | None = None
    summary: str


class ResponseResult(BaseModel):
    message: str
    citation_evidence_ids: list[str] = Field(default_factory=list)
    tool_evidence_ids: list[str] = Field(default_factory=list)
