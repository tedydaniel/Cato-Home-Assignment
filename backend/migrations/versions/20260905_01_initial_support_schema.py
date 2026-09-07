"""Create the initial support, workflow, and knowledge-base schema.

Revision ID: 20260905_01
Revises:
Create Date: 2026-09-05
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20260905_01"
down_revision = None
branch_labels = None
depends_on = None

EMBEDDING_DIMENSIONS = 1536


class Vector(sa.types.UserDefinedType):
    """Minimal pgvector type; avoids requiring a second ORM integration package."""

    cache_ok = True

    def __init__(self, dimensions: int) -> None:
        self.dimensions = dimensions

    def get_col_spec(self, **_: object) -> str:
        return f"vector({self.dimensions})"


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "accounts",
        sa.Column("customer_id", sa.Text(), primary_key=True),
        sa.Column("company", sa.Text(), nullable=False),
        sa.Column("tier", sa.Text(), nullable=False),
        sa.Column("email_domain", sa.Text(), nullable=False, unique=True),
        sa.Column("registered_admin_contact", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_table(
        "sites",
        sa.Column("site_id", sa.Text(), primary_key=True),
        sa.Column("customer_id", sa.Text(), sa.ForeignKey("accounts.customer_id"), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("country", sa.Text(), nullable=False),
        sa.Column("connection_type", sa.Text(), nullable=False),
        sa.Column("details", postgresql.JSONB(), nullable=False),
    )
    op.create_index("sites_customer_idx", "sites", ["customer_id"])
    op.create_table(
        "tickets",
        sa.Column("ticket_id", sa.Text(), primary_key=True),
        sa.Column("customer_id", sa.Text(), sa.ForeignKey("accounts.customer_id"), nullable=False),
        sa.Column("requester_email", sa.Text(), nullable=False),
        sa.Column("site_id", sa.Text(), sa.ForeignKey("sites.site_id")),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("channel", sa.Text(), nullable=False),
        sa.Column("product_area", sa.Text(), nullable=False),
        sa.Column("priority", sa.Text(), nullable=False),
        sa.Column("subject", sa.Text(), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("status", sa.Text(), nullable=False),
    )
    op.create_index("tickets_customer_created_idx", "tickets", ["customer_id", "created_at"])

    op.create_table(
        "conversations",
        sa.Column("conversation_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("customer_id", sa.Text(), sa.ForeignKey("accounts.customer_id"), nullable=False),
        sa.Column("requester_email", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("conversations_customer_updated_idx", "conversations", ["customer_id", "updated_at"])
    op.create_table(
        "messages",
        sa.Column("message_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("conversation_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("conversations.conversation_id", ondelete="CASCADE"), nullable=False),
        sa.Column("role", sa.Text(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("messages_conversation_created_idx", "messages", ["conversation_id", "created_at"])

    op.create_table(
        "agent_runs",
        sa.Column("run_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("conversation_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("conversations.conversation_id", ondelete="CASCADE"), nullable=False),
        sa.Column("graph_version", sa.Text(), nullable=False),
        sa.Column("status", sa.Text(), nullable=False),
        sa.Column("state", postgresql.JSONB(), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("completed_at", sa.DateTime(timezone=True)),
    )
    op.create_table(
        "tool_calls",
        sa.Column("tool_call_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("run_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("agent_runs.run_id", ondelete="CASCADE"), nullable=False),
        sa.Column("tool_name", sa.Text(), nullable=False),
        sa.Column("input", postgresql.JSONB(), nullable=False),
        sa.Column("output", postgresql.JSONB()),
        sa.Column("status", sa.Text(), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("completed_at", sa.DateTime(timezone=True)),
    )
    op.create_index("tool_calls_run_idx", "tool_calls", ["run_id", "started_at"])

    op.create_table(
        "approval_requests",
        sa.Column("approval_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("conversation_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("conversations.conversation_id", ondelete="CASCADE"), nullable=False),
        sa.Column("action_type", sa.Text(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("proposed_payload", postgresql.JSONB(), nullable=False),
        sa.Column("status", sa.Text(), nullable=False, server_default="pending"),
        sa.Column("reviewer_note", sa.Text()),
        sa.Column("decided_by", sa.Text()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("decided_at", sa.DateTime(timezone=True)),
    )
    op.create_index("approval_requests_status_idx", "approval_requests", ["status", "created_at"])
    op.create_table(
        "alerts",
        sa.Column("alert_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("customer_id", sa.Text(), sa.ForeignKey("accounts.customer_id"), nullable=False),
        sa.Column("conversation_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("conversations.conversation_id", ondelete="SET NULL")),
        sa.Column("severity", sa.Text(), nullable=False),
        sa.Column("kind", sa.Text(), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("status", sa.Text(), nullable=False, server_default="open"),
        sa.Column("details", postgresql.JSONB(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("resolved_at", sa.DateTime(timezone=True)),
    )
    op.create_index("alerts_status_created_idx", "alerts", ["status", "created_at"])

    op.create_table(
        "kb_snapshots",
        sa.Column("snapshot_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("source_url", sa.Text(), nullable=False),
        sa.Column("manifest_sha256", sa.Text(), nullable=False, unique=True),
        sa.Column("article_count", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_table(
        "kb_articles",
        sa.Column("article_url", sa.Text(), primary_key=True),
        sa.Column("article_title", sa.Text(), nullable=False),
        sa.Column("content_sha256", sa.Text(), nullable=False),
        sa.Column("snapshot_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_table(
        "kb_chunks",
        sa.Column("chunk_id", sa.Text(), primary_key=True),
        sa.Column("article_url", sa.Text(), sa.ForeignKey("kb_articles.article_url", ondelete="CASCADE"), nullable=False),
        sa.Column("article_sha256", sa.Text(), nullable=False),
        sa.Column("section_title", sa.Text(), nullable=False),
        sa.Column("chunk_index", sa.Integer(), nullable=False),
        sa.Column("token_count", sa.Integer(), nullable=False),
        sa.Column("chunk_text", sa.Text(), nullable=False),
        sa.Column("metadata", postgresql.JSONB(), nullable=False),
        sa.Column("embedding", Vector(EMBEDDING_DIMENSIONS), nullable=False),
    )
    op.create_index("kb_chunks_article_idx", "kb_chunks", ["article_url"])
    op.execute("CREATE INDEX kb_chunks_embedding_idx ON kb_chunks USING hnsw (embedding vector_cosine_ops)")


def downgrade() -> None:
    op.drop_table("kb_chunks")
    op.drop_table("kb_articles")
    op.drop_table("kb_snapshots")
    op.drop_table("alerts")
    op.drop_table("approval_requests")
    op.drop_table("tool_calls")
    op.drop_table("agent_runs")
    op.drop_table("messages")
    op.drop_table("conversations")
    op.drop_table("tickets")
    op.drop_table("sites")
    op.drop_table("accounts")
