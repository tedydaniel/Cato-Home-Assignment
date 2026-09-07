from pathlib import Path


def test_initial_migration_defines_core_support_and_kb_tables() -> None:
    migration = (
        Path(__file__).resolve().parents[1]
        / "migrations"
        / "versions"
        / "20260905_01_initial_support_schema.py"
    ).read_text(encoding="utf-8")
    for table in ("accounts", "tickets", "conversations", "messages", "tool_calls", "approval_requests", "alerts", "kb_articles", "kb_chunks"):
        assert f'"{table}"' in migration
    assert "CREATE EXTENSION IF NOT EXISTS vector" in migration


def test_approval_lifecycle_migration_adds_idempotency_and_audit_events() -> None:
    migration = (
        Path(__file__).resolve().parents[1]
        / "migrations"
        / "versions"
        / "20260906_02_approval_lifecycle.py"
    ).read_text(encoding="utf-8")

    assert '"idempotency_key"' in migration
    assert '"approval_events"' in migration


def test_message_metadata_migration_persists_citations() -> None:
    migration = (
        Path(__file__).resolve().parents[1]
        / "migrations"
        / "versions"
        / "20260906_03_message_metadata.py"
    ).read_text(encoding="utf-8")

    assert '"metadata"' in migration
