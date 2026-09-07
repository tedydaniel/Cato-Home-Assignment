---
title: "Monitoring AI Agents"
slug: "monitoring-ai-agents"
updated: 2026-08-10T10:06:08Z
published: 2026-08-10T10:06:08Z
canonical: "knowledge.catonetworks.com/monitoring-ai-agents"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring AI Agents

This article explains how to use the **Agents Overview** page to monitor local AI agent activity in your organization.

## Overview

Local AI agents are different from standard AI chat applications because they can use tools, memory, API calls, Model Context Protocol (MCP) servers, planning, and autonomous feedback loops to complete user tasks. This creates a broader risk surface because agents can act on behalf of users, interact with enterprise systems, and process untrusted content from connected tools or external sources.

Cato AI Security gives admins visibility and control over local AI agents used in the organization, including agent applications, tools, MCP servers, users, and policy violations. The **Agents Overview** page provides a high-level view of agent activity so you can identify Shadow AI agents, review risky tool and MCP usage, and investigate blocked or monitored interactions.

Use the page to understand which local agents are active in your organization, how users interact with them, and where AI Security policies detect violations such as indirect prompt injection, exposed secrets, or sensitive data. You can drill down from the widgets to the relevant inventory or session data for deeper investigation.

## Prerequisites

To use the **Agents Overview** page, you need:

- **AI Security for Users** license
- AI Scout deployed on the endpoints where local agents are used

AI Scout provides visibility into local agent activity on the endpoint, including agent applications, tools, MCP server calls, and policy violations.

## Show the Agents Overview Page

The **Agents Overview** page shows agent activity for the selected time range. ![agent_overview.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/agent_overview.png)

**To show the Agents Overview page:**

1. From the navigation menu, click **AI Security > Agents Overview**

## Understand the Agents Overview Page

The **Agents Overview** page includes widgets that summarize local agent activity, policy enforcement, users, applications, tools, MCP servers, and violations.

Use the time range filter to define the period shown on the page. The page updates the displayed data based on the selected time range.

| Widget | Description |
| --- | --- |
| Summary Flow | Shows a high-level summary of local agent activity, including interceptors, users, applications, total interactions, allowed interactions, and blocked interactions |
| Top Usage | Shows the most-used local agent applications or tools. Use **Applications** and **Tools** to change how usage is grouped |
| Violation Breakdown | Shows the distribution of AI Security policy violations detected for local agents |
| Top Users | Shows the users with the highest local agent activity |
| Top MCPs | Shows the MCP servers or tools with the highest usage, including agents and calls |

## Analyze the Summary Flow

The Summary Flow gives you a near real-time view of local agent activity and enforcement outcomes in the selected time range. It shows the relationship between agent-related components, total interactions, and the final policy outcome.

The widget includes:

- Interceptors used to inspect local agent activity
- Users that interacted with local agents
- Applications detected in local agent activity
- Total interactions inspected by Cato
- Allowed interactions
- Blocked interactions

Use this widget to quickly understand the scale of agent activity in your organization and whether AI Security policies are blocking risky interactions.

## Analyze Top Agent Usage

Use the **Top Usage** widget to identify which local agent applications or tools generate the most interactions.

You can group usage by:

- **Applications**
- **Tools**

When grouped by **Applications**, the widget helps you identify which local agent applications are most active in the organization. For example, this can help you understand whether users are working with coding agents such as Claude Code, Codex, or Cursor.

When grouped by **Tools**, the widget shows cross-application tool usage. This helps you understand which tools are being called most often, which applications use them, and how many users or calls are associated with the tool.

Click **View Agent Inventory** to open the **Local Agents** page and review discovered local agents, tools, and MCP servers.

## Review Policy Violations

Use the **Violation Breakdown** widget to understand which AI Security policy rules are detecting or blocking local agent activity. The widget shows the violation types, the number of violations, and their percentage of the total violations in the selected time range.

Violations can include detections such as:

- Indirect prompt injection
- Secrets or passwords
- PII
- Other AI Security policy violations configured for local agents

Click a violation type to open the **Agent Sessions** page filtered for the selected violation. This helps you focus the investigation on sessions that matched the specific policy violation.

Click **View Agent Sessions** to open the **Agent Sessions** page and investigate local agent sessions.

## Review Top Users

Use the **Top Users** widget to identify the users with the highest local agent activity. This helps you understand which users are driving agent usage and where additional investigation or policy review may be required.

For example, a user with unusually high activity can indicate heavy legitimate usage, automation, testing, or activity that requires security review. Drill down to the relevant sessions to better understand the context of the activity.

## Review Top MCP Servers and Tools

Use the **Top MCPs** widget to identify MCP servers and tools used by local agents in your organization. The widget helps admins find unsanctioned or risky MCP servers, review supply chain exposure, and understand which agent workflows rely on external tools.

For each MCP server or tool, the widget can show usage details such as:

- Name
- Status
- Agents
- Calls
- Activity trend

Use **Servers** and **Tools** to change the view based on the type of MCP-related activity you want to analyze.

## Drill Down from the Agents Overview Page

You can drill down from the **Agents Overview** page to investigate agent usage and security events:

- Click **View Agent Inventory** to open the **Local Agents** page
- Click **View Agent Sessions** to open the **Agent Sessions** page
- Click a violation in the **Violation Breakdown** widget to open the **Agent Sessions** page filtered for the selected violation type
