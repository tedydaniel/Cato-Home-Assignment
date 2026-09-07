---
title: "Monitoring Agent Sessions"
slug: "monitoring-agent-sessions"
updated: 2026-07-21T16:25:16Z
published: 2026-07-21T16:25:16Z
canonical: "knowledge.catonetworks.com/monitoring-agent-sessions"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Agent Sessions

## Overview

Agent Sessions helps you investigate how supported AI agents behave at runtime across your organization. As agents interact with users, tools, and connected services, their activity can create risks such as data exposure, unsafe tool use, policy violations, and unexpected agent behavior.

Agent Sessions records this activity so you can review user prompts, agent responses, tool calls, policy decisions, and violations to investigate risky behavior and audit agent usage over time.

For a broader discussion of when to use Agent Sessions instead of the Local Agents page, see [Monitoring AI Agents Overview](/v1/docs/monitoring-ai-agents).

### Viewing Agent Sessions
You can review recorded sessions and individual events in the Agent Sessions page.
1. Navigate to **AI Security > Agent Sessions**. 

## Before You Start

To monitor Agent Sessions, deploy the relevant Hooks or interceptors for supported AI agents. Sessions are generated when agent activity is captured by an interceptor. For more information, see [Understanding Scouts and Agent Controls](/v1/docs/understanding-scouts-and-agent-controls).

## Review Agent Sessions

The Agent Sessions page is the top-level view of recorded agent activity. At the top of the page, two summary widgets show high-level activity across your environment:

![monitor-agent-sessions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/monitor-agent-sessions.png){height="" width=""}



- **Interactions by Application** - Distribution of total interactions broken down by agent application, so you can identify which agents are most active in your environment
- **Interactions Over Time** - Number of interactions over the selected time range, so you can identify spikes in activity that may warrant investigation

Below the summary widgets, the page displays two tabs:

- **Sessions** - Lists all recorded agent sessions. Each session row includes the following fields:
  - **Session ID** - The unique ID for the session. Select the **Session ID** to open the full Session Audit view
  - **No. of Interactions** - The total number of exchanges that took place during the session, including user prompts, agent responses, and tool calls
  - **No. of Tools Used** - The number of distinct tools the agent invoked during the session
  - **Violations** - Any policy violations triggered during the session, displayed as labeled tags. 
      Violations are surfaced inline so you can identify sessions that require attention without opening each one
  - **Application** - The agent application that generated the session, for example, Claude Code or Cursor
  - **User** - User name associated with the session
  - **Interceptor** - The mechanism that captured the session, for example, Claude Code Hooks
  - **Last Activity** - The timestamp of the most recent event in the session
- **Events** - A flat, chronological log of individual events across sessions. Use this tab to search or filter across interaction types, tools, or violations without navigating into individual sessions

## Investigate a Session

Select a session to open the Session Audit view, which shows detailed activity recorded during that session. The header displays key session metadata:

- **Application** - The agent that generated the session
- **User** - The user who triggered the session
- **Hostname** - The endpoint the agent was running on
- **Session ID** - The unique identifier for the session, which you can copy for use in investigations or incident records
- **Interceptor** - The mechanism that captured the session's traffic
- **Model** - The LLM model the agent used during the session
- **Tools Used** - The tools invoked during the session, each showing the number of calls made
- **Violations** - Any policy violations triggered during the session, displayed as labeled tags. These are shown upfront so you can triage immediately, for example, to distinguish between PII exposure, a secrets leak, and an indirect prompt injection attempt

The session detail view has two tabs: **Events** and **Schema**.

### Review Session Events

The **Events** tab shows the chronological timeline of the session. Each event is displayed as a labeled step, such as User Prompt, Agent Response, Tool Call, Tool Message, Permission Request, or Subagent Stop, with a relative timestamp showing how many seconds elapsed since the session started. MCP-sourced events are labeled with an MCP badge, so you can identify which parts of the session involved external tool integrations.

Events that triggered a violation are highlighted and marked with a Blocked badge, showing where in the session the policy engine intervened. This level of detail is useful when investigating indirect prompt injection attempts, where the malicious payload arrives through a tool message instead of a user prompt. It also helps you trace how sensitive data moved through a sequence of tool calls.

### Review the Session Schema

The **Schema** tab renders the session as a visual graph, showing the flow of activity from the user prompt through the agent to each tool it called. Each tool node displays the number of calls made to that tool during the session, and nodes representing blocked tool calls are marked with a red indicator. This view helps you understand the overall shape of a complex session, for example, which tools an agent called most frequently or where in the tool call graph a violation occurred.

For information on configuring the policies that generate violations in Agent Sessions, see [Configuring the Coding Agents Policy](/v1/docs/configuring-the-coding-agents-policy). For information on discovering and managing the local agents that generate these sessions, see [Monitoring Local Agents](/v1/docs/monitoring-local-agents).
