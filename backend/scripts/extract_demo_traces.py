"""Extract three representative saved scenario traces for the submission."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parents[2] / "reports" / "scenario_eval.json"
    target = Path(__file__).resolve().parents[2] / "demo_traces"; target.mkdir(exist_ok=True)
    scenarios = {item["scenario_id"]: item for item in json.loads(source.read_text(encoding="utf-8"))}
    for scenario_id in ("SC-01-bgp-flap", "SC-03-sla-credit", "SC-05-prompt-injection"):
        if scenario_id in scenarios:
            (target / f"{scenario_id}.json").write_text(json.dumps(scenarios[scenario_id], indent=2, default=str), encoding="utf-8")


if __name__ == "__main__": main()
