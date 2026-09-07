"""Simulated support-ticket writes for the home-assignment workflow."""

from datetime import datetime, timezone
from uuid import uuid4

import psycopg

from app.config import get_settings


def create(customer_id: str, requester_email: str, subject: str, priority: str = "P3") -> str:
    ticket_id = f"SIM-{uuid4().hex[:10].upper()}"
    url = get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(url) as connection, connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO tickets (ticket_id, customer_id, requester_email, created_at, channel, product_area, priority, subject, body, status)
               VALUES (%s, %s, %s, %s, 'chat', 'general', %s, %s, %s, 'open')""",
            (ticket_id, customer_id, requester_email, datetime.now(timezone.utc), priority, subject, subject),
        )
    return ticket_id
