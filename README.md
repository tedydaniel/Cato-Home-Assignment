# Cato AI Support Engineer

A runnable multi-agent support chat for the Cato Networks home assignment. It uses a Next.js chat and reviewer UI, FastAPI, LangGraph, PostgreSQL/pgvector, Cato's public knowledge base, supplied synthetic telemetry, and PostgreSQL-backed human approval interrupts.

## Quick start

1. Copy `.env.example` to `.env`. Set `POSTGRES_PASSWORD`, the matching `POSTGRES_URL`, and `OPENAI_API_KEY`. For Docker, the database host inside `POSTGRES_URL` must be `postgres`, not `localhost`.
2. Optionally enable LangSmith by setting `LANGSMITH_TRACING=true`, `LANGSMITH_API_KEY`, and `LANGSMITH_PROJECT`.
3. Start the application:

   ```powershell
   docker compose up --build -d
   ```

4. Index the committed KB snapshot into pgvector:

   ```powershell
   docker compose --profile tools run --rm ingest
   ```

   This verifies every snapshot file against its manifest and creates embeddings. It does not crawl the internet.
5. Open <http://localhost:3000>. API documentation is available at <http://localhost:8000/docs>.

Use **New** to create a conversation with an email from `data/tickets/accounts.csv`. The **Debug** page shows the durable graph state and individual tool calls. **Tasks & alerts** is the reviewer queue for approvals and Sev-1 alerts.

`data/` is mounted read-only. Compose runs database migrations and safely upserts accounts, sites, and historical tickets before the backend starts.

## Included submission artifacts

| Path | Contents and purpose |
| --- | --- |
| [SPEC.md](SPEC.md) | Stack choice, agent contracts, orchestration, persistence, safety, and API plan. |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Logical and deployment architecture diagrams, components, and limitations. |
| [DEMO.md](DEMO.md) | Suggested live-demo flow: telemetry diagnosis, human approval, and adversarial input. |
| [RUNBOOK.md](RUNBOOK.md) | Operational commands and expected failure behavior. |
| [EVAL_REPORT.md](EVAL_REPORT.md) | Retrieval/scenario evaluation results and known limitations. |
| [answers.md](answers.md) | Answers to all 35 supplied KB questions, generated through the chat path. |
| [reports/](reports/) | Machine-readable retrieval and scenario evaluation output. |
| [demo_traces/](demo_traces/) | Saved traces for one diagnosis, one approval-gated request, and one adversarial conversation. |
| [knowledge_base/snapshot/](knowledge_base/snapshot/) | Pinned Cato KB Markdown snapshot and manifest with per-article SHA-256 hashes. |
| [data/](data/) | Supplied policies, accounts, tickets, telemetry, and evaluation scenarios. |
| [backend/](backend/) | FastAPI app, LangGraph agents, typed tools, migrations, ingestion, tests, and evaluation scripts. |
| [frontend/](frontend/) | Next.js customer chat, Debug view, and reviewer Tasks & alerts UI. |
| [compose.yaml](compose.yaml) | Local Docker Compose stack: frontend, backend, PostgreSQL, migration, seed, and optional ingestion job. |

## Retrieval design

The ingestion pipeline verifies the pinned manifest, splits Markdown at `##` sections, and prefixes every chunk with its article and section title. Long sections target 450 tokens, have a hard 600-token ceiling, and use 75-token overlap. Each chunk retains article URL, SHA-256, section title, token count, and chunk index, which makes citations specific and reproducible.

Queries combine semantic search (`text-embedding-3-small`) with PostgreSQL lexical search, then use reciprocal-rank fusion and a lightweight lexical/policy-aware rerank. A conservative coverage gate rejects weak evidence; requests for unpublished roadmap or future-feature information are explicitly out of coverage. See [EVAL_REPORT.md](EVAL_REPORT.md) for measured quality and limitations.

## Useful commands

Generate the required answer transcript and LangSmith-backed LLM cost totals:

```powershell
docker compose build backend
docker compose run --rm backend python -m scripts.generate_answers
```

Replay the scripted scenarios and measure retrieval:

```powershell
docker compose run --rm backend python -m scripts.evaluate_scenarios
docker compose run --rm backend python -m scripts.evaluate_retrieval
```

Run the test suite:

```powershell
docker compose run --rm backend pytest -q
```

Refresh the public KB only deliberately; this requires internet access and regenerates the snapshot:

```powershell
docker compose --profile tools run --rm ingest python -m scripts.ingest_kb --refresh-snapshot
```
