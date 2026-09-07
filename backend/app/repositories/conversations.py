"""Minimal durable conversation persistence for the demo chat API."""

from __future__ import annotations

from uuid import UUID, uuid4

import psycopg
from psycopg.types.json import Jsonb

from app.config import get_settings
from app.schemas.conversations import ChatMessage, ConversationView


def _database_url() -> str:
    return get_settings().postgres_url.replace("postgresql+psycopg://", "postgresql://", 1)


def _messages(cursor: psycopg.Cursor, conversation_id: UUID) -> list[ChatMessage]:
    cursor.execute(
        """SELECT message_id, role, content, metadata, created_at FROM messages
           WHERE conversation_id = %s ORDER BY created_at, message_id""",
        (conversation_id,),
    )
    return [ChatMessage(message_id=row[0], role=row[1], content=row[2], citations=row[3].get("citations", []), run_id=row[3].get("run_id"), created_at=row[4]) for row in cursor.fetchall()]


def _conversation(cursor: psycopg.Cursor, conversation_id: UUID) -> ConversationView | None:
    cursor.execute(
        """SELECT conversation_id, customer_id, requester_email, title
           FROM conversations WHERE conversation_id = %s""",
        (conversation_id,),
    )
    row = cursor.fetchone()
    if row is None:
        return None
    return ConversationView(
        conversation_id=row[0], customer_id=row[1], requester_email=row[2], title=row[3],
        messages=_messages(cursor, conversation_id),
    )


def create(requester_email: str, title: str) -> ConversationView | None:
    normalized_email = requester_email.strip().lower()
    if "@" not in normalized_email:
        return None
    domain = normalized_email.rsplit("@", maxsplit=1)[1]
    conversation_id = uuid4()
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute("SELECT customer_id FROM accounts WHERE email_domain = %s", (domain,))
        account = cursor.fetchone()
        if account is None:
            return None
        cursor.execute(
            """INSERT INTO conversations (conversation_id, customer_id, requester_email, title)
               VALUES (%s, %s, %s, %s)""",
            (conversation_id, account[0], normalized_email, title),
        )
        return _conversation(cursor, conversation_id)


def get(conversation_id: UUID) -> ConversationView | None:
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        return _conversation(cursor, conversation_id)


def list_for_requester(requester_email: str) -> list[ConversationView]:
    normalized_email = requester_email.strip().lower()
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute(
            """SELECT conversation_id FROM conversations WHERE requester_email = %s
               ORDER BY updated_at DESC""",
            (normalized_email,),
        )
        return [conversation for row in cursor.fetchall() if (conversation := _conversation(cursor, row[0])) is not None]


def append(conversation_id: UUID, role: str, content: str, metadata: dict | None = None) -> ConversationView | None:
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        conversation = _conversation(cursor, conversation_id)
        if conversation is None:
            return None
        cursor.execute(
            "INSERT INTO messages (message_id, conversation_id, role, content, metadata) VALUES (%s, %s, %s, %s, %s)",
            (uuid4(), conversation_id, role, content, Jsonb(metadata or {})),
        )
        cursor.execute("UPDATE conversations SET updated_at = now() WHERE conversation_id = %s", (conversation_id,))
        return _conversation(cursor, conversation_id)


def delete(conversation_id: UUID) -> bool:
    with psycopg.connect(_database_url()) as connection, connection.cursor() as cursor:
        cursor.execute("DELETE FROM conversations WHERE conversation_id = %s RETURNING conversation_id", (conversation_id,))
        return cursor.fetchone() is not None
