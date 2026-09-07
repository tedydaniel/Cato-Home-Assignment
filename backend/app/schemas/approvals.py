"""Contracts for durable human approval requests and decisions."""

from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field


ProtectedAction = Literal["mfa_reset", "service_credit", "c2_verdict_override"]
ApprovalStatus = Literal["pending", "approved", "rejected", "executed", "expired"]


class ApprovalRequest(BaseModel):
    approval_id: UUID
    conversation_id: UUID
    customer_id: str
    action_type: ProtectedAction
    reason: str
    proposed_payload: dict[str, Any]
    evidence_ids: list[str] = Field(default_factory=list)
    idempotency_key: str
    status: ApprovalStatus
    created_at: datetime | None = None
    decided_at: datetime | None = None
    decided_by: str | None = None
    reviewer_note: str | None = None


class ApprovalDecision(BaseModel):
    decision: Literal["approved", "rejected", "edit"]
    reviewer: str = Field(min_length=1, max_length=200)
    note: str | None = Field(default=None, max_length=2_000)
    edited_payload: dict[str, Any] | None = None
