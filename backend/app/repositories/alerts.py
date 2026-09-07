"""Durable simulated incident alerts used for Sev-1 escalation."""

from uuid import UUID, uuid4

import psycopg
from psycopg.types.json import Jsonb

from app.config import get_settings


def create_sev1(customer_id: str, conversation_id: UUID, summary: str) -> str:
    alert_id = uuid4()
    url = get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(url) as connection, connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO alerts (alert_id, customer_id, conversation_id, severity, kind, summary, details)
               VALUES (%s, %s, %s, 'P1', 'sev1_page', %s, %s)""",
            (alert_id, customer_id, conversation_id, summary, Jsonb({"simulated": True, "requires_human": True})),
        )
    return str(alert_id)


def list_open() -> list[dict[str, str]]:
    url = get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(url) as connection, connection.cursor() as cursor:
        cursor.execute("SELECT alert_id, customer_id, severity, kind, summary, status FROM alerts WHERE status = 'open' ORDER BY created_at DESC")
        return [{"alert_id": str(row[0]), "customer_id": row[1], "severity": row[2], "kind": row[3], "summary": row[4], "status": row[5]} for row in cursor.fetchall()]
