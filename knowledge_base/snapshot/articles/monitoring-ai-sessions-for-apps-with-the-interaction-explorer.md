---
title: "Monitoring AI Sessions for Apps with the Interaction Explorer"
slug: "monitoring-ai-sessions-for-apps-with-the-interaction-explorer"
updated: 2026-08-03T16:06:07Z
published: 2026-08-03T16:06:07Z
canonical: "knowledge.catonetworks.com/monitoring-ai-sessions-for-apps-with-the-interaction-explorer"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring AI Sessions for Apps with the Interaction Explorer

The **Interaction Explorer** page provides a centralized view of AI interactions sent from your homegrown applications. You can use this page to review AI activity across multiple guards, monitor detections, and investigate individual interactions.

The page is available for accounts with an **AI Security for Applications** license.

## Overview

The Interaction Explorer helps administrators track AI usage from applications and agents protected by guards. Each row represents a session and includes the related guard, session ID, number of interactions, detections, and activity timestamps.

Use this page to:

- View AI interactions sent from homegrown applications
- Monitor detection data alongside interaction logs
- Review activity across multiple guards from a single location
- Open an interaction to view rule violations and the engine analysis report

## Interaction Table

The table shows the AI interaction sessions that match the selected time range and filters.

| Column | Description |
| --- | --- |
| Guard | The guard who inspected the AI interaction. |
| Session ID | The unique identifier for the AI interaction session. |
| Interactions | The number of AI interactions in the session. |
| Detections | The number of detections found in the session. |
| First Activity | The time the first interaction in the session occurred. |
| Last Activity | The time the most recent interaction in the session occurred. |

## Viewing interaction details

Click a session in the table to open the interaction details. The details show the relevant rule violations and the AI Security engine analysis report, helping you understand why a detection occurred and what content or behavior triggered it.
