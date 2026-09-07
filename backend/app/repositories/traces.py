"""Durable, replayable graph-run audit records for the reviewer experience."""

from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

import psycopg
from psycopg.types.json import Jsonb

from app.config import get_settings


def _database_url() -> str:
    return get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)


def record_completed(conversation_id: UUID, state: dict[str, Any]) -> UUID:
    """Store a final graph snapshot and its evidence as replayable audit data."""

    run_id = uuid4()
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO agent_runs (run_id, conversation_id, graph_version, status, state, completed_at)
               VALUES (%s, %s, %s, 'completed', %s, now())""",
            (run_id, conversation_id, "support-graph-v1", Jsonb(state)),
        )
        tool_calls = [
            *state.get("diagnostic_tool_calls", []),
            *state.get("knowledge_tool_calls", []),
        ]
        # Preserve useful traces written before individual tool-call recording
        # was introduced, so historic demo conversations remain inspectable.
        if not tool_calls:
            tool_calls = [
                {"tool_name": "diagnostics", "input": {}, "output": state.get("diagnostic_evidence", {})},
                {"tool_name": "search_knowledge_base", "input": {}, "output": state.get("knowledge_evidence", {})},
            ]
        for tool_call in tool_calls:
            output = tool_call.get("output", {})
            if not output:
                continue
            cursor.execute(
                """INSERT INTO tool_calls (tool_call_id, run_id, tool_name, input, output, status, completed_at)
                   VALUES (%s, %s, %s, %s, %s, 'completed', now())""",
                (uuid4(), run_id, tool_call.get("tool_name", "unknown"), Jsonb(tool_call.get("input", {})), Jsonb(output)),
            )
    return run_id


def list_for_conversation(conversation_id: UUID) -> list[dict[str, Any]]:
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute(
            """SELECT run_id, status, state, started_at, completed_at FROM agent_runs
               WHERE conversation_id = %s ORDER BY started_at""",
            (conversation_id,),
        )
        return [
            {"run_id": str(row[0]), "status": row[1], "state": row[2], "started_at": row[3], "completed_at": row[4]}
            for row in cursor.fetchall()
        ]


def get(run_id: UUID) -> dict[str, Any] | None:
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute("SELECT run_id, conversation_id, status, state, started_at, completed_at FROM agent_runs WHERE run_id = %s", (run_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        cursor.execute("SELECT tool_name, input, output, status, started_at, completed_at FROM tool_calls WHERE run_id = %s ORDER BY started_at", (run_id,))
        tools = [
            {"tool_name": tool[0], "input": tool[1], "output": tool[2], "status": tool[3], "started_at": tool[4], "completed_at": tool[5]}
            for tool in cursor.fetchall()
        ]
    return {"run_id": str(row[0]), "conversation_id": str(row[1]), "status": row[2], "state": row[3], "started_at": row[4], "completed_at": row[5], "tool_calls": tools}
