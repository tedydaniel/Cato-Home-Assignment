# Architecture

```text
Customer chat -> FastAPI -> Triage -> Diagnostics -> Knowledge -> Actions -> Response
                              |            |              |             |
                         account/ticket   telemetry      pgvector     approvals
                              \____________ durable PostgreSQL run trace ____________/
                                                        |
                                              reviewer Debug / Tasks UI
```

The parent LangGraph routes a typed shared case file through specialised agents. Triage owns trusted customer context, Diagnostics owns telemetry evidence, Knowledge owns KB citations, Actions owns protected-action proposals, and Response owns customer wording. Customer content is redacted and injection-checked before it enters the graph.

PostgreSQL persists conversations, approval records, LangGraph checkpoints, graph-run state, and derived tool/retrieval evidence. The graph has no Redis or worker dependency: this keeps the demo reproducible. A protected action creates its approval record, then pauses at a LangGraph interrupt; a reviewer decision resumes the exact checkpoint using the conversation ID.

Retrieval uses title-prefixed Markdown sections, OpenAI embeddings, PostgreSQL lexical search, and reciprocal-rank fusion. The KB snapshot is maintained under `knowledge_base/snapshot`; ingestion uses article hashes for incremental updates.

## Deployment view

```text
Browser (:3000) -> Next.js frontend
                      |
                      v
                 FastAPI backend (:8000) -> OpenAI / LangSmith
                      |
                      v
              PostgreSQL + pgvector (:5432)
              conversations, approvals, alerts, traces, KB index
```

Docker Compose runs the frontend, backend, and PostgreSQL. Migrations and seed loading are one-off jobs; KB ingestion is a deliberate command because it refreshes external content and consumes embedding API usage.

## Deliberate limitations

Approval execution is deliberately simulated; production would require an authenticated reviewer identity, authorization policy, and an audited integration with the affected Cato system. Retrieval has measured baseline metrics and policy-aware reranking, but needs a stronger reranker and confidence calibration before production use.
