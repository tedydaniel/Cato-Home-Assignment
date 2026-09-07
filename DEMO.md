# Live demo guide

## Startup

1. Start the stack with `docker compose up --build`.
2. Confirm `http://localhost:8000/health/ready` and open `http://localhost:3000`.
3. Use a requester email from a seeded account domain.

## Conversation 1 — telemetry-led diagnosis

Use the BGP-prefix scenario in `data/eval/scenarios.jsonl` (`SC-01-bgp-flap`). Show the reply citations, then click the agent reply to open its durable Debug trace. Highlight BGP evidence and the KB playbook citation.

## Conversation 2 — human approval

Use the credit scenario (`SC-03-sla-credit`). The action is held as a pending approval. Open Tasks & alerts, show the reviewer controls, approve it, and return to chat to show the durable continuation reply.

## Conversation 3 — adversarial input

Use the prompt-injection scenario (`SC-05-prompt-injection`) or paste a credential-shaped PSK. Explain that the system redacts secrets before persistence and refuses instruction overrides before graph execution.

## Evidence to show

- [answers.md](answers.md): all 35 questions through the real chat path.
- [scenario report](reports/scenario_eval.json): current end-to-end results.
- [evaluation report](EVAL_REPORT.md): retrieval metrics and known limitations.
- `demo_traces/`: saved BGP, approval, and injection examples.
