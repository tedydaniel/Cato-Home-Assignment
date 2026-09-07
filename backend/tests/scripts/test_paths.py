from pathlib import Path

from scripts.paths import project_root


def test_project_root_uses_container_override(monkeypatch):
    monkeypatch.setenv("PROJECT_ROOT", "/app")

    assert project_root("/app/scripts/crawl_kb_snapshot.py") == Path("/app")


def test_project_root_derives_local_repository_root(monkeypatch, tmp_path):
    monkeypatch.delenv("PROJECT_ROOT", raising=False)
    script = tmp_path / "backend" / "scripts" / "ingest_kb.py"
    script.parent.mkdir(parents=True)
    script.touch()

    assert project_root(script) == tmp_path
