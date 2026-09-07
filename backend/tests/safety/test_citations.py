from app.safety.citations import customer_safe_citations


def test_customer_safe_citations_excludes_internal_policy_urls() -> None:
    citations = [
        {"source": "policy://POL-CREDIT", "evidence_id": "policy:credit"},
        {"source": "https://knowledge.catonetworks.com/docs/example.md", "evidence_id": "kb:public"},
    ]

    assert customer_safe_citations(citations) == [citations[1]]
