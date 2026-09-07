"""Trusted context and bounded outputs used by the Triage specialist."""

from datetime import datetime

from pydantic import BaseModel, Field


class SiteSummary(BaseModel):
    site_id: str
    name: str
    country: str
    connection_type: str


class TicketHistoryEntry(BaseModel):
    ticket_id: str
    created_at: datetime
    site_id: str | None = None
    product_area: str
    priority: str
    subject: str
    status: str


class TrustedTriageContext(BaseModel):
    customer_id: str
    company: str
    tier: str
    requester_email: str
    identity_verified: bool
    sites: list[SiteSummary] = Field(default_factory=list)
    ticket_history: list[TicketHistoryEntry] = Field(default_factory=list)
