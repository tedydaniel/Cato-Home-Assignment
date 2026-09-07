"""HTTP contracts for the small end-to-end chat API."""

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class CreateConversation(BaseModel):
    requester_email: str = Field(min_length=3, max_length=320)
    title: str = Field(default="New support request", min_length=1, max_length=200)


class SendMessage(BaseModel):
    content: str = Field(min_length=1, max_length=10_000)


class ChatMessage(BaseModel):
    message_id: UUID
    role: str
    content: str
    created_at: datetime
    citations: list[dict[str, str]] = Field(default_factory=list)
    run_id: str | None = None


class ConversationView(BaseModel):
    conversation_id: UUID
    customer_id: str
    requester_email: str
    title: str
    messages: list[ChatMessage]


class ChatTurn(BaseModel):
    conversation: ConversationView
    response: dict[str, Any]
    state: dict[str, Any]
