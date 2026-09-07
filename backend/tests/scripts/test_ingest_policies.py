from app.config import get_settings
from scripts.ingest_policies import build_policy_records


def test_policy_documents_become_citable_section_chunks() -> None:
    articles, chunks = build_policy_records(get_settings().data_path)

    assert any(article["url"] == "policy://POL-CREDIT" for article in articles)
    assert any("SLA credits" in chunk["text"] for chunk in chunks["policy://POL-CREDIT"])
    assert all(chunk["article_url"].startswith("policy://") for values in chunks.values() for chunk in values)
