---
title: "Monitoring Local Agents"
slug: "monitoring-local-agents"
updated: 2026-08-02T19:01:58Z
published: 2026-08-02T19:02:00Z
canonical: "knowledge.catonetworks.com/monitoring-local-agents"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Local Agents

## Overview
Local Agents helps admins understand which AI agents are installed on managed endpoints, who is running them, which MCP servers and tools they can access, and how those tools are classified. Use this visibility to identify unapproved agents, assess endpoint exposure, and evaluate whether agent usage aligns with organizational security requirements.

Use the Local Agents page to review discovered agents and tools from the Agents and Tools views. Local Agents focuses on what exists in your environment, including which agents are installed, who is running them, what MCP servers they are configured to use, and whether those tools meet your organization's security standards. If you need to investigate what agents are doing at runtime, use the Agent Sessions page to review prompts, responses, tool calls, policy decisions, and violations.
### Prerequisites
To monitor Local Agents, make sure [AI Scout](/v1/docs/understanding-scouts-and-agent-controls-1) is deployed to discover AI agents on endpoints. To inspect runtime sessions and enforce policies, deploy the relevant Managed Agents.
## Review Agents

The **Agents** tab is the default view on the  Local Agents page. Summary widgets at the top show total agents discovered, total users, and the most active applications in your environment.
![Local_agents_agents.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Local_agents_agents.png){height="" width=""}

Each agent instance in the list includes the following fields:

- **App** - The agent application, for example, Claude Code, Cursor, or GitHub Copilot
- **Users** - The user account associated with this agent instance. When the user is unidentified, AI Security uses the detected email addresses to identify agent activity from personal and shadow users.
- **Tools** - The tools available to this agent instance, including native tools and MCP-connected tools
- **Hostname** - The endpoint the agent is installed on
- **Interceptor** - The mechanism that discovered or monitors this agent instance. Agents discovered only by AI Scout are identified through endpoint scanning, but their runtime activity is not inspected. Agents with Claude Code Hooks as an interceptor are monitored by Agents Policy. Their sessions and tool calls are captured in Agent Sessions and are subject to runtime policy enforcement.
- **Last Seen** - The most recent time this agent instance was observed. An agent that appears without a user was discovered by AI Scout during a scan, but has not yet generated intercepted activity.

### Review Agent Details

Select an agent instance to drill down and open pages with configuration and activity data for that agent. These pages are scoped to the specific combination of agent application, user, and endpoint.

### Review the Agent Footprint

Review AI agent usage across managed endpoints to identify which agents are active in your environment, which users are running them, and which agent applications are used most frequently. The Agents view provides summary widgets for discovered agents, users running agents, and the most active agent applications.

The header shows key context at a glance, including total interactions over time, the associated user, the resource type, the hostname, the organization, and which interceptors are active for this instance.

Use this page as your starting point when assessing the potential impact of a compromised or misbehaving agent. An agent connected to many directories and several MCP servers can create higher exposure than one with limited, well-scoped access.

### Review MCP Servers

The **MCP** page lists all MCP servers configured for this agent instance.

Use this page to understand which external systems an agent is integrated with. You can identify unauthorized or unexpected MCP server connections and compare them with the **Tools** view to check whether those servers are sanctioned. For more information, see [Sanction and Unsanction Tools](/v1/docs/monitoring-local-agents#sanction-tools).

Each entry includes the following fields:

- **Server** - The address of the MCP server
- **Type** - The connection type, either STDIO for a local process or HTTP for a remote endpoint
- **Alias** - The friendly name assigned to this server in the agent's configuration file
- **Scope** - Whether the server was configured at the user level or scoped to a specific directory
- **Config Path** - The path to the configuration file where this MCP server is defined, useful for locating and auditing the source of the configuration

### Review Permissions

The **Permissions** page lists the filesystem scopes this agent instance has been granted access to.

Review this page when assessing the potential impact of a compromise or an indirect prompt injection attack. An agent with access to many directories and a linked code repository can create higher exposure than one scoped to a single working directory.

Each entry includes the following fields:

- **Scope** - The directory path that the agent can access
- **Repo** - Any code repository linked to this scope, for example, a GitHub repository
- **Tools** - The number of tools available to the agent within this scope
- **Permission** - The permission mode granted for this scope, where applicable

### Trace Agent Activity

Use the **Tracing** page to understand the activity history of a specific agent instance without first navigating through the broader Agent Sessions view. You can browse activity at two levels of granularity:

- **Sessions** - Lists all sessions generated by this agent instance. Select a session to open the full session detail in Agent Sessions, where you can review the Events timeline and Schema graph for each session. See [Monitoring Agent Sessions](/v1/docs/monitoring-agent-sessions) for details.
- **Events** - A flat, timestamped log of every individual event generated by this agent. Each event includes the following fields:
  - **Session ID** - The session this event belongs to
  - **Interaction** - The type of event, for example User Prompt, Agent Response, Tool Call, Permission Request, or Subagent Stop
  - **Tool** - The tool involved, if the event was a tool call or permission request
  - **Violations** - Any policy violations triggered by this event
  - **Interceptor** - The mechanism that captured this event
  - **Last Activity** - The timestamp of the event

## Review Tools

The **Tools** view shifts the perspective from individual agent instances to the tools and MCP servers discovered in your environment. Summary widgets at the top show:

- **MCP Servers** - The total number of distinct MCP servers discovered across your environment
- **Top MCP Servers** - The most actively used MCP servers by call volume
- **Tools Usage by Type** - A breakdown of tool call volume split between native tools and MCP-connected tools
- **Usage** - Total tool calls recorded across the selected time range

Below the summary, the tool inventory lists all tool groups, including native tool sets and MCP servers. You can switch between the **Tool Groups** view and the **Tools List** view, depending on how much detail you need. Each entry includes the following fields:

- **Tool Group** - The name of the tool group or MCP server, along with its type, either Native or MCP
- **Users** - The number of users who have this tool configured, out of the total users in your environment
- **Usage** - The number of tool calls made to this tool group in the selected time range
- **Status** - The sanctioned status of this tool group: sanctioned, unsanctioned, or unset
- **Applications** - The agent applications that use this tool group
- **Last Used** - The most recent time a tool call was made to this group
- **Last Seen** - The most recent time this tool group was observed in any agent configuration

### Sanctioned and Unsanctioned Tools

Control which tool groups and MCP servers are approved for use by assigning a sanctioned status to each item. Use the row action menu to mark an item as sanctioned, mark it as unsanctioned, or clear the status.

Sanctioned status helps you enforce agent security policies based on approved tool usage. When building policies, you can configure rules for unsanctioned tools or MCP servers, such as blocking tool calls to any MCP server that hasn't been explicitly approved. This helps you enforce least-privilege access for tool connectivity without adding every individual tool to the policy.

As part of an iterative process, review the **Tools** view and mark known, approved tools as sanctioned. Then create a policy that alerts or blocks tool calls involving unsanctioned tools. This helps admins identify new MCP servers added without IT approval.

For information on building policies that reference tool sanctioning status, see **Configuring AI Security Policies**. For information on investigating runtime activity associated with specific tools, see [Monitoring Agent Sessions](/v1/docs/monitoring-agent-sessions).
