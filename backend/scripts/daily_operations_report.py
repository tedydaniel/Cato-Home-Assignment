"""Generate daily support operations outputs in Markdown and CSV formats."""

from __future__ import annotations

import csv
from pathlib import Path

import psycopg

from app.config import get_settings


def main() -> None:
    output = Path(__file__).resolve().parents[2] / "reports"; output.mkdir(exist_ok=True)
    url = get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)
    try:
        connection = psycopg.connect(url)
    except psycopg.OperationalError:
        if "@postgres:" in url or "@postgres/" in url:
            url = url.replace("@postgres:", "@localhost:").replace("@postgres/", "@localhost/")
            connection = psycopg.connect(url)
        else:
            raise
    with connection, connection.cursor() as cursor:
        cursor.execute("SELECT priority, count(*) FROM tickets WHERE status = 'open' GROUP BY priority ORDER BY priority"); tickets = cursor.fetchall()
        cursor.execute("SELECT severity, summary, status FROM alerts WHERE status = 'open' ORDER BY created_at DESC"); alerts = cursor.fetchall()
        cursor.execute("SELECT action_type, customer_id, reason FROM approval_requests WHERE status = 'pending' ORDER BY created_at DESC"); approvals = cursor.fetchall()
    markdown = ["# Daily support operations report", "", "## Open tickets"] + [f"- {priority}: {count}" for priority, count in tickets]
    markdown += ["", "## Open escalations"] + [f"- {severity}: {summary} ({status})" for severity, summary, status in alerts]
    markdown += ["", "## Pending approvals"] + [f"- {action}: {customer} — {reason}" for action, customer, reason in approvals]
    (output / "daily_operations.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")
    with (output / "daily_operations.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle); writer.writerow(["kind", "priority_or_action", "detail", "status"])
        writer.writerows([("ticket", priority, count, "open") for priority, count in tickets])
        writer.writerows([("alert", severity, summary, status) for severity, summary, status in alerts])
        writer.writerows([("approval", action, f"{customer}: {reason}", "pending") for action, customer, reason in approvals])


if __name__ == "__main__":
    main()
