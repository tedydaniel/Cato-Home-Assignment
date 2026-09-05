"""Load supplied accounts, sites, and ticket history into PostgreSQL.

Telemetry remains on disk and is only reached through diagnostic tools. This is
safe to re-run: it upserts source records without deleting conversation data.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import psycopg

from app.config import get_settings


def database_url() -> str:
    return get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)


def load_accounts(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))
    expected = {"customer_id", "company", "tier", "email_domain", "registered_admin_contact"}
    if not rows or any(set(row) != expected for row in rows):
        raise ValueError("accounts.csv does not match the expected account schema.")
    return rows


def load_sites(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    sites = payload.get("sites")
    if not isinstance(sites, list) or not all(isinstance(site, dict) for site in sites):
        raise ValueError("sites.json must contain a sites list.")
    return sites


def load_tickets(path: Path) -> list[dict[str, Any]]:
    tickets = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    required = {"ticket_id", "customer_id", "requester_email", "created_at", "channel", "product_area", "priority", "subject", "body", "status"}
    if any(not required.issubset(ticket) for ticket in tickets):
        raise ValueError("tickets.jsonl does not match the expected ticket schema.")
    return tickets


def load_support_data(data_path: Path) -> tuple[int, int, int]:
    accounts = load_accounts(data_path / "tickets" / "accounts.csv")
    sites = load_sites(data_path / "telemetry" / "sites.json")
    tickets = load_tickets(data_path / "tickets" / "tickets.jsonl")
    with psycopg.connect(database_url()) as connection, connection.cursor() as cursor:
        for account in accounts:
            cursor.execute(
                """INSERT INTO accounts (customer_id, company, tier, email_domain, registered_admin_contact)
                   VALUES (%(customer_id)s, %(company)s, %(tier)s, %(email_domain)s, %(registered_admin_contact)s)
                   ON CONFLICT (customer_id) DO UPDATE SET company = EXCLUDED.company, tier = EXCLUDED.tier,
                   email_domain = EXCLUDED.email_domain, registered_admin_contact = EXCLUDED.registered_admin_contact""",
                account,
            )
        for site in sites:
            cursor.execute(
                """INSERT INTO sites (site_id, customer_id, name, country, connection_type, details)
                   VALUES (%s, %s, %s, %s, %s, %s::jsonb)
                   ON CONFLICT (site_id) DO UPDATE SET name = EXCLUDED.name, country = EXCLUDED.country,
                   connection_type = EXCLUDED.connection_type, details = EXCLUDED.details""",
                (site["site_id"], site["customer_id"], site["name"], site["country"], site["connection_type"], json.dumps(site)),
            )
        for ticket in tickets:
            cursor.execute(
                """INSERT INTO tickets (ticket_id, customer_id, requester_email, site_id, created_at, channel,
                   product_area, priority, subject, body, status)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                   ON CONFLICT (ticket_id) DO UPDATE SET status = EXCLUDED.status, subject = EXCLUDED.subject,
                   body = EXCLUDED.body, priority = EXCLUDED.priority""",
                (ticket["ticket_id"], ticket["customer_id"], ticket["requester_email"], ticket.get("site_id"),
                 datetime.fromisoformat(ticket["created_at"].replace("Z", "+00:00")), ticket["channel"],
                 ticket["product_area"], ticket["priority"], ticket["subject"], ticket["body"], ticket["status"]),
            )
    return len(accounts), len(sites), len(tickets)


def main() -> None:
    accounts, sites, tickets = load_support_data(get_settings().data_path)
    print(f"Loaded {accounts} accounts, {sites} sites, and {tickets} tickets.")


if __name__ == "__main__":
    main()
