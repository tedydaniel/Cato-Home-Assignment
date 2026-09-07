---
title: "Working with Managed Agents"
slug: "working-with-managed-agents"
updated: 2026-07-29T07:56:14Z
published: 2026-07-29T07:56:14Z
canonical: "knowledge.catonetworks.com/working-with-managed-agents"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Managed Agents

## Overview

Managed agents are AI agents created in no-code agent-building platforms. Users in your organization can build, configure, and share these agents without writing code, and connect them to knowledge bases, data sources, and tools that act on your organization's data.

Cato provides visibility into managed agents in various agent platforms. You can use the **Managed Agents** page to understand which agents exist in your account, who owns them, which knowledge bases and tools they can access, and more.

For each managed agent, you can drill down to review the agent configuration such as system prompt, connected knowledge bases, provided tools, as well as the agent's activity. This helps you understand which agents were built by your organization, how they were defined, and assess agent behavior.

The following table describes the current support for the different platforms and agent types, and which features are supported for each:

| Platform | Supported Agent Types | Agent Configuration | Agent Sessions |
| --- | --- | --- | --- |
| Copilot Studio | All agents | ✓ | ✓ |
| Amazon Bedrock | Bedrock Agents Classic | ✓ | |
| Microsoft Foundry | Foundry (classic), Foundry prompt agents | ✓ | |
| ChatGPT | GPTs, Agents | ✓ | |
| Amazon Quick | All agents | ✓ | |

## Getting Started

To get started, connect Cato to managed agent platforms using integrations. These integrations can be configured on the **AI Security** > **Integrations** page. The following articles provide instructions on how to integrate with each of the supported platforms:

- [Copilot Studio](/v1/docs/configuring-copilot-studio)
- [Amazon Bedrock](/v1/docs/configuring-amazon-bedrock)
- [Microsoft Foundry](/v1/docs/configuring-microsoft-foundry)
- [ChatGPT](/v1/docs/chatgpt-integration-with-ai-security)
- [Amazon Quick](/v1/docs/configuring-amazon-quick)

## View Managed Agents

The **Managed Agents** page provides an inventory of the managed agents in your account.

From the navigation menu, select **AI Security** > **Managed Agents**.

You can search for a specific managed agent or filter the table by provider.

You can click on an agent to drill down into what the agent is designed to do, which resources it can access, and view its recent activity.
