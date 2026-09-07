---
title: "Working with the Cato Remote MCP Server"
slug: "working-with-the-cato-remote-mcp-server"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/working-with-the-cato-remote-mcp-server"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with the Cato Remote MCP Server

## Overview

Cato’s Remote MCP Server enables you to securely connect AI agents and automation platforms directly to your Cato environment — without building custom API integrations.

Instead of manually orchestrating API calls in scripts, you expose structured Cato tools to any compatible MCP client. This allows AI workflows to retrieve data, investigate incidents, and automate actions in a secure and controlled manner.

With the Remote MCP Server, you can:

- Connect AI agents to Cato using a standardized protocol
- Eliminate custom API orchestration logic
- Reduce integration complexity
- Maintain centralized governance and visibility

The Remote MCP Server is designed for organizations that want to operationalize AI across security and network workflows while maintaining strict control over data access and execution boundaries.

## Understanding the Building Blocks

### What is an LLM?

A Large Language Model (LLM) is an AI model trained on large volumes of text that can understand and generate natural language.

In enterprise environments, LLMs can: summarize incidents, generate investigation steps, query systems, and automate operational workflows.

However, an LLM does not inherently have access to your environment. It requires controlled interfaces to securely retrieve and act on data.

### What Is MCP?

Model Context Protocol (MCP) is a standardized protocol that enables LLMs to securely access external tools and structured data sources.

Rather than allowing an LLM to directly call APIs, MCP:

- Defines tools in a structured format
- Controls how tools are invoked
- Returns machine-readable responses
- Maintains strict execution boundaries

### What Is an MCP Client?

An MCP client is the software component that connects an LLM to one or more MCP servers. It can host or connect to an LLM, and also to multiple MCP servers. It discovers tools and uses the tools to securely execute calls.

The client does not implement Cato logic - it consumes tools exposed by the Cato MCP Server.

#### Examples of MCP Clients

Common MCP-compatible platforms include:

- **Cursor IDE** - AI-powered development environment with native MCP support
- **OpenAI Codex** (desktop, CLI, IDE integrations) – AI coding agent supporting MCP servers
- **Claude Desktop** - Desktop AI assistant that connects to MCP servers and uses structured tools

### What Is the Cato Remote MCP Server?

The Cato Remote MCP Server is a hosted MCP endpoint that exposes Cato tools over a secure remote connection.

Instead of deploying and maintaining a local MCP server, your MCP client connects directly to Cato’s hosted MCP endpoint. It exposes structured Cato tools, authenticates to your account, and returns the results to the MCP client.

This approach significantly simplifies integration and reduces operational overhead.

### Remote MCP vs. Local MCP

#### Local MCP Deployment

- You host the MCP server in your infrastructure
- You manage availability and scaling
- You maintain security controls
- You handle network exposure and maintenance

This model provides flexibility but increases operational complexity.

#### Cato Remote MCP Deployment

- Cato hosts and manages the MCP server
- No infrastructure deployment is required
- No local service maintenance is needed
- Secure connection to the Cato environment is provided

## Remote MCP vs. Ask AI

Cato’s embedded AI assistant, **Ask AI**, is integrated directly into the Cato Management Application (CMA). Cato controls the LLM, and Ask AI is optimized for in-console analysis and guidance.

A remote MCP lets you control the LLM and the orchestration layer, and your AI platform can correlate Cato data with other enterprise systems.

Remote MCP enables broader enterprise AI workflows beyond the CMA.

## Using the Cato Remote MCP Server

After you configure the Remote MCP Server in your MCP client, the client can immediately access Cato data according to the data lake [retention period](/v1/docs/guide-to-cato-data-lake) for your account. For example, if your account retains three months of data, the MCP client can query up to three months of historical data.

Access to data and available actions are strictly controlled by the permissions assigned to the API key you use for authentication. The MCP server enforces the same [role-based access model](/v1/docs/managing-admin-roles-using-rbac) as the Cato API, ensuring that AI agents and automation workflows only access data and perform actions permitted by that key.

### Prerequisites

- An MCP-compatible client (for example, Cursor IDE, or OpenAI Codex)
- Valid [API key for the Cato account](/v1/docs/generating-api-keys-for-the-cato-api)

### Connecting to the Cato Remote MCP Server

Once connected, the MCP client automatically discovers the tools that are exposed by the Cato MCP server. The server is dynamically updated with new tools, and no action is required for the MCP client.

These are the Cato API keys that you can use:

1. An **Admin API key** for personal or interactive use
2. A **Service API key** for automation and production workflows

**To connect an MCP client to the Cato remote MCP server:**

1. Make sure that your MCP client is already connected to your LLM
2. Configure your MCP client with the URL for the Cato API endpoint: `https://api.catonetworks.com/api/v1/rest/mcp`

The same URL is used for all CMA instances.
3. Add a custom authentication header:
  1. **Header Name:** x-api-key
  2. **Header Value:** <Cato API key>
4. Save and activate the MCP connection.

## Example Use Cases

### AI-Assisted Threat Investigation

An analyst asks: Investigate this IP and summarize related security events.

The MCP client:

1. Calls the Security Events tool
2. Retrieves relevant structured data
3. Returns results to the LLM
4. The LLM summarizes findings

### Automated XOps Incident Enrichment

When an XOps story is generated, the AI agent retrieves: Related flows, target reputation, and user history. The agent then responds with:

- A contextual report
- Suggested mitigation actions

### AI-Driven Network Troubleshooting

This example demonstrates how, using the Cato MCP server, the AI performs structured, cross-domain queries across networking and application metrics. This replaces manually navigating multiple dashboards in the CMA.

An administrator reports that users at the London site are experiencing slow access to Microsoft 365.

1. Using Remote MCP, the AI agent queries:
  1. Site Operations metrics
  2. WAN link health
  3. Packet loss and latency statistics
  4. Application performance metrics
2. It detects:
  1. Increased packet loss on the primary WAN link
  2. Degraded SLA for M365 traffic class
3. It correlates:
  1. Link quality degradation
  2. Bandwidth saturation during peak hours
4. It recommends:
  1. Failing over to the secondary link
  2. Adjusting QoS priority
  3. Investigating ISP performance

## Known Limitations

- MCP clients that support only local MCP connections (STDIO) can’t connect directly to the Cato Remote MCP endpoint. To use these clients, you must deploy a lightweight MCP proxy that bridges the local STDIO connection to the remote Cato MCP server.
