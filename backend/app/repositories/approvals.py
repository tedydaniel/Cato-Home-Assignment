"""PostgreSQL persistence for approval work items.

These functions deliberately do not execute customer-impacting actions. They
only create and transition the approval record that authorizes a later executor.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

import psycopg
from psycopg.types.json import Jsonb

from app.config import get_settings
from app.schemas.approvals import ApprovalDecision, ApprovalRequest


def _database_url() -> str:
    return get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)


def _record(row: tuple[Any, ...]) -> ApprovalRequest:
    return ApprovalRequest(
        approval_id=row[0], conversation_id=row[1], customer_id=row[2], action_type=row[3],
        reason=row[4], proposed_payload=row[5], evidence_ids=row[6], idempotency_key=row[7],
        status=row[8], created_at=row[9], decided_at=row[10], decided_by=row[11], reviewer_note=row[12],
    )


_RETURNING = """approval_id, conversation_id, customer_id, action_type, reason, proposed_payload,
evidence_ids, idempotency_key, status, created_at, decided_at, decided_by, reviewer_note"""


def create_or_get(request: ApprovalRequest) -> ApprovalRequest:
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO approval_requests (
                approval_id, conversation_id, customer_id, action_type, reason, proposed_payload,
                evidence_ids, idempotency_key, status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'pending')
            ON CONFLICT (idempotency_key) DO UPDATE SET idempotency_key = EXCLUDED.idempotency_key
            RETURNING {_RETURNING}""",
            (request.approval_id, request.conversation_id, request.customer_id, request.action_type,
             request.reason, Jsonb(request.proposed_payload), Jsonb(request.evidence_ids), request.idempotency_key),
        )
        row = cursor.fetchone()
        assert row is not None
        created = row[0] == request.approval_id
        cursor.execute(
            """INSERT INTO approval_events (event_id, approval_id, event_type, details)
               VALUES (%s, %s, %s, %s)""",
            (uuid4(), row[0], "created" if created else "retrieved", Jsonb({"idempotency_key": request.idempotency_key})),
        )
    return _record(row)


def list_requests(status: str | None = "pending") -> list[ApprovalRequest]:
    where, values = ("WHERE status = %s", (status,)) if status else ("", ())
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute(f"SELECT {_RETURNING} FROM approval_requests {where} ORDER BY created_at DESC", values)
        return [_record(row) for row in cursor.fetchall()]


def decide(approval_id: UUID, decision: ApprovalDecision) -> ApprovalRequest | None:
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        if decision.decision == "edit":
            cursor.execute(
                f"""UPDATE approval_requests SET proposed_payload = COALESCE(%s, proposed_payload), reviewer_note = %s
                    WHERE approval_id = %s AND status = 'pending' RETURNING {_RETURNING}""",
                (Jsonb(decision.edited_payload) if decision.edited_payload is not None else None, decision.note, approval_id),
            )
            row = cursor.fetchone()
            if row is None:
                return None
            cursor.execute(
                """INSERT INTO approval_events (event_id, approval_id, event_type, actor, details)
                   VALUES (%s, %s, 'edited', %s, %s)""",
                (uuid4(), approval_id, decision.reviewer, Jsonb({"note": decision.note, "edited_payload": decision.edited_payload})),
            )
            return _record(row)
        cursor.execute(
            f"""UPDATE approval_requests SET status = %s, decided_by = %s, reviewer_note = %s,
                decided_at = now() WHERE approval_id = %s AND status = 'pending'
                RETURNING {_RETURNING}""",
            (decision.decision, decision.reviewer, decision.note, approval_id),
        )
        row = cursor.fetchone()
        if row is None:
            return None
        cursor.execute(
            """INSERT INTO approval_events (event_id, approval_id, event_type, actor, details)
               VALUES (%s, %s, %s, %s, %s)""",
            (uuid4(), approval_id, decision.decision, decision.reviewer, Jsonb({"note": decision.note})),
        )
    return _record(row)


def mark_executed(approval_id: UUID, result: dict[str, Any]) -> ApprovalRequest | None:
    """Record the simulated side effect exactly once after a human approval."""
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE approval_requests SET status = 'executed', executed_at = now(), execution_result = %s
                WHERE approval_id = %s AND status = 'approved' RETURNING {_RETURNING}""",
            (Jsonb(result), approval_id),
        )
        row = cursor.fetchone()
        if row is None:
            return None
        cursor.execute(
            """INSERT INTO approval_events (event_id, approval_id, event_type, details)
               VALUES (%s, %s, 'executed', %s)""",
            (uuid4(), approval_id, Jsonb(result)),
        )
    return _record(row)
