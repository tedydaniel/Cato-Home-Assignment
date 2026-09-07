"""Read-only trusted account and historical-ticket lookup for Triage."""

from __future__ import annotations

from typing import Any

import psycopg

from app.config import get_settings
from app.schemas.triage import SiteSummary, TicketHistoryEntry, TrustedTriageContext


def _database_url() -> str:
    return get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)


def get_triage_context(requester_email: str) -> TrustedTriageContext | None:
    """Resolve a requester from account data, never from a chat claim."""
    normalized_email = requester_email.strip().lower()
    if "@" not in normalized_email:
        return None
    domain = normalized_email.rsplit("@", maxsplit=1)[1]
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute(
            """SELECT customer_id, company, tier, registered_admin_contact
               FROM accounts WHERE email_domain = %s""",
            (domain,),
        )
        account = cursor.fetchone()
        if account is None:
            return None
        customer_id, company, tier, registered_admin_contact = account
        cursor.execute(
            "SELECT site_id, name, country, connection_type FROM sites WHERE customer_id = %s ORDER BY site_id",
            (customer_id,),
        )
        sites = [SiteSummary(site_id=row[0], name=row[1], country=row[2], connection_type=row[3]) for row in cursor.fetchall()]
        cursor.execute(
            """SELECT ticket_id, created_at, site_id, product_area, priority, subject, status
               FROM tickets WHERE customer_id = %s ORDER BY created_at DESC LIMIT 10""",
            (customer_id,),
        )
        history = [
            TicketHistoryEntry(
                ticket_id=row[0], created_at=row[1], site_id=row[2], product_area=row[3],
                priority=row[4], subject=row[5], status=row[6],
            )
            for row in cursor.fetchall()
        ]
    return TrustedTriageContext(
        customer_id=customer_id, company=company, tier=tier, requester_email=normalized_email,
        identity_verified=normalized_email == registered_admin_contact.lower(), sites=sites, ticket_history=history,
    )
