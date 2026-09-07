from scripts.evaluate_retrieval import _matches


def test_retrieval_source_match_uses_article_slug() -> None:
    assert _matches("configuring-bgp-neighbors", "https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors.md")
    assert not _matches("configuring-bgp-neighbors", "https://knowledge.catonetworks.com/docs/ipsec.md")
