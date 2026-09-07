# Evaluation report

## Retrieval

The scenario-opening retrieval baseline was Recall@5 **0.25** and MRR **0.188**. After policy-aware retrieval and lexical reranking, it improved to Recall@5 **0.583** and MRR **0.472**. These are useful but not production-ready scores; remaining failures are tracked through the scenario report.

## Scenario replay

Run `uv run python -m scripts.evaluate_scenarios` from `backend` to regenerate `reports/scenario_eval.json`. The evaluator replays all supplied conversations through the normal chat path. It reports required citation sources (including telemetry evidence), required tool use, action handling, and account guardrail results. It is deliberately honest: expected-source matching is strict, and a passing conversation still needs manual claim-by-claim groundedness review.

## Known limitations

- Retrieval has a conservative coverage gate (minimum hybrid score plus lexical overlap, with an explicit refusal for unpublished roadmap/future-feature requests). It needs further calibration against reviewer-held answer keys and a stronger reranker.
- Protected-action conversations use a PostgreSQL-backed LangGraph interrupt. Approval or rejection resumes the original checkpoint; edit intentionally leaves it pending for a later final decision.
- Model-token cost is available in LangSmith when configured, but is not aggregated into the local report.
