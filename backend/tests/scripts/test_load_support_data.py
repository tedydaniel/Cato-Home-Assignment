from pathlib import Path

from scripts.load_support_data import load_accounts, load_sites, load_tickets


def test_support_source_files_match_expected_schema() -> None:
    data_path = Path(__file__).resolve().parents[3] / "data"
    accounts = load_accounts(data_path / "tickets" / "accounts.csv")
    sites = load_sites(data_path / "telemetry" / "sites.json")
    tickets = load_tickets(data_path / "tickets" / "tickets.jsonl")

    assert accounts
    assert sites
    assert tickets
    customer_ids = {account["customer_id"] for account in accounts}
    assert customer_ids.issuperset(ticket["customer_id"] for ticket in tickets)
    assert {site["customer_id"] for site in sites}.issubset(customer_ids)
