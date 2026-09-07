from uuid import UUID

import psycopg
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from app.db import database_is_ready
from app.config import get_settings
from app.repositories.approvals import decide, list_requests
from app.schemas.approvals import ApprovalDecision, ApprovalRequest
from app.schemas.conversations import ChatTurn, ConversationView, CreateConversation, SendMessage
from app.repositories import conversations
from app.repositories import traces
from app.repositories.alerts import list_open as list_open_alerts
from app.services.chat import send_message
from app.services.approval_execution import resume_review_decision

app = FastAPI(title="Cato AI Support Engineer API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in get_settings().cors_origins.split(",") if origin.strip()],
    allow_credentials=False,
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type"],
)

@app.get("/health/live", tags=["health"])
def liveness() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/health/ready", tags=["health"])
def readiness() -> dict[str, str]:
    if not database_is_ready():
        raise HTTPException(status_code=503, detail="database unavailable")
    return {"status": "ready"}

@app.get("/api")
def api_root() -> dict[str, str]:
    return {"service": "cato-support-engineer-api", "phase": "foundation"}


@app.get("/api/approvals", response_model=list[ApprovalRequest], tags=["approvals"])
def approvals(status: str | None = Query(default="pending")) -> list[ApprovalRequest]:
    """List approval work items for the internal Tasks & Alerts page."""
    try:
        return list_requests(status)
    except psycopg.Error as error:
        raise HTTPException(status_code=503, detail="approval store unavailable") from error


@app.get("/api/alerts", tags=["alerts"])
def alerts() -> list[dict]:
    return list_open_alerts()


@app.post("/api/approvals/{approval_id}/decision", response_model=ApprovalRequest, tags=["approvals"])
def decide_approval(approval_id: UUID, decision: ApprovalDecision) -> ApprovalRequest:
    """Atomically approve or reject a still-pending request.

    Authentication will supply the reviewer identity in production; the explicit
    reviewer field keeps the local assignment workflow demonstrable and auditable.
    """
    try:
        approval = decide(approval_id, decision)
    except psycopg.Error as error:
        raise HTTPException(status_code=503, detail="approval store unavailable") from error
    if approval is None:
        raise HTTPException(status_code=409, detail="approval is missing or no longer pending")
    if approval.status in {"approved", "rejected"}:
        approval = resume_review_decision(approval)
    return approval


@app.post("/api/conversations", response_model=ConversationView, status_code=201, tags=["chat"])
def create_conversation(request: CreateConversation) -> ConversationView:
    try:
        conversation = conversations.create(request.requester_email, request.title)
    except psycopg.Error as error:
        raise HTTPException(status_code=503, detail="conversation store unavailable") from error
    if conversation is None:
        raise HTTPException(status_code=404, detail="requester account not found")
    return conversation


@app.get("/api/conversations", response_model=list[ConversationView], tags=["chat"])
def list_conversations(requester_email: str = Query(min_length=3)) -> list[ConversationView]:
    try:
        return conversations.list_for_requester(requester_email)
    except psycopg.Error as error:
        raise HTTPException(status_code=503, detail="conversation store unavailable") from error


@app.get("/api/conversations/{conversation_id}", response_model=ConversationView, tags=["chat"])
def get_conversation(conversation_id: UUID) -> ConversationView:
    try:
        conversation = conversations.get(conversation_id)
    except psycopg.Error as error:
        raise HTTPException(status_code=503, detail="conversation store unavailable") from error
    if conversation is None:
        raise HTTPException(status_code=404, detail="conversation not found")
    return conversation


@app.get("/api/conversations/{conversation_id}/runs", tags=["debug"])
def conversation_runs(conversation_id: UUID) -> list[dict]:
    """List durable graph runs so a reviewer can select a particular reply."""
    return traces.list_for_conversation(conversation_id)


@app.get("/api/runs/{run_id}", tags=["debug"])
def graph_run(run_id: UUID) -> dict:
    """Return the stored graph state and tool evidence for one reply."""
    run = traces.get(run_id)
    if run is None:
        raise HTTPException(status_code=404, detail="graph run not found")
    return run


@app.delete("/api/conversations/{conversation_id}", status_code=204, tags=["chat"])
def delete_conversation(conversation_id: UUID) -> None:
    try:
        deleted = conversations.delete(conversation_id)
    except psycopg.Error as error:
        raise HTTPException(status_code=503, detail="conversation store unavailable") from error
    if not deleted:
        raise HTTPException(status_code=404, detail="conversation not found")


@app.post("/api/conversations/{conversation_id}/messages", response_model=ChatTurn, tags=["chat"])
def post_message(conversation_id: UUID, request: SendMessage) -> ChatTurn:
    try:
        turn = send_message(conversation_id, request.content)
    except psycopg.Error as error:
        raise HTTPException(status_code=503, detail="conversation store unavailable") from error
    if turn is None:
        raise HTTPException(status_code=404, detail="conversation not found")
    return turn
