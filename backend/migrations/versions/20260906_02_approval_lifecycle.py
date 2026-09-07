"""Add idempotency and an immutable audit trail to approval requests.

Revision ID: 20260906_02
Revises: 20260905_01
Create Date: 2026-09-06
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20260906_02"
down_revision = "20260905_01"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("approval_requests", sa.Column("customer_id", sa.Text(), nullable=True))
    op.add_column("approval_requests", sa.Column("evidence_ids", postgresql.JSONB(), nullable=False, server_default="[]"))
    op.add_column("approval_requests", sa.Column("idempotency_key", sa.Text(), nullable=True))
    op.add_column("approval_requests", sa.Column("executed_at", sa.DateTime(timezone=True)))
    op.add_column("approval_requests", sa.Column("execution_result", postgresql.JSONB()))
    op.execute("""UPDATE approval_requests AS request SET customer_id = conversation.customer_id
                  FROM conversations AS conversation
                  WHERE request.conversation_id = conversation.conversation_id""")
    op.alter_column("approval_requests", "customer_id", nullable=False)
    op.execute("UPDATE approval_requests SET idempotency_key = approval_id::text WHERE idempotency_key IS NULL")
    op.alter_column("approval_requests", "idempotency_key", nullable=False)
    op.create_unique_constraint("approval_requests_idempotency_key_key", "approval_requests", ["idempotency_key"])
    op.create_table(
        "approval_events",
        sa.Column("event_id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("approval_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("approval_requests.approval_id", ondelete="CASCADE"), nullable=False),
        sa.Column("event_type", sa.Text(), nullable=False),
        sa.Column("actor", sa.Text()),
        sa.Column("details", postgresql.JSONB(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("approval_events_approval_created_idx", "approval_events", ["approval_id", "created_at"])


def downgrade() -> None:
    op.drop_table("approval_events")
    op.drop_constraint("approval_requests_idempotency_key_key", "approval_requests", type_="unique")
    op.drop_column("approval_requests", "execution_result")
    op.drop_column("approval_requests", "executed_at")
    op.drop_column("approval_requests", "idempotency_key")
    op.drop_column("approval_requests", "evidence_ids")
    op.drop_column("approval_requests", "customer_id")
