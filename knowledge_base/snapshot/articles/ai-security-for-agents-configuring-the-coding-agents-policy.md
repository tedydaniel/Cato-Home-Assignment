---
title: "Configuring the Coding Agents Policy"
slug: "ai-security-for-agents-configuring-the-coding-agents-policy"
updated: 2026-08-26T06:26:20Z
published: 2026-08-26T06:26:20Z
canonical: "knowledge.catonetworks.com/ai-security-for-agents-configuring-the-coding-agents-policy"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Coding Agents Policy

## Overview

As developers increasingly use local coding agents, security teams need visibility into both user prompts and the actions the agent performs with connected tools. Risk can occur after the initial prompt, including in tool calls, tool output, and MCP-based interactions. Coding Agents Policy helps you monitor and block risky activity in supported coding-agent workflows, so you can reduce the risk of sensitive data exposure and unsafe agent actions.

Coding Agents Policy is part of AI Security for Users and works with Scout and Hooks. Scout helps identify the local coding agents and tools running on endpoints, and Hooks surfaces supported coding-agent interactions for policy evaluation. Together, they extend AI Security controls to supported coding-agent activity in your environment.

Use the Coding Agents Policy to govern two parts of coding-agent behavior: the messages exchanged between the user and the agent, and the agent’s interactions with connected tools. For each rule, you define whether Cato monitors or blocks the activity. You can scope rules to specific interaction types and specific tools, which lets you apply stricter controls to higher-risk agent actions. Engine profiles let you apply the same AI Security inspection logic used in other AI Security policies.

### Before You Start

- Requires AI Security for End Users license
- Scout and Hooks are deployed on the supported AI agents
- Blocking is currently supported for Cursor, Claude Code, Claude Cowork, and Codex

## Sample Use Cases

### Block Unsanctioned AI Tools

Developers connect AI tools to a coding agent so the agent can use external tools and services. This creates a security risk when the agent can access resources that are not approved for your environment. You can use the Agent Policy to block activity for unsanctioned tools. To block unauthorized MCP servers, create a Tool Use rule with these settings:

- Applications - **Cursor**
- Type - **Tool Use**
- Tools - **Approval Status** = **Unsanctioned**
- Action - **Block**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/coding_agent_usecase.png)

This configuration blocks tool activity for any unsanctioned AI tools used by the selected coding agent.

### Block Tool Calls Triggered by Malicious MCP Instructions

Cursor MCP servers describe their tools to the coding agent with text. This creates a security risk when a malicious MCP server includes hidden instructions in the tool description, such as telling the agent to read credential files and pass them as input. The Coding Agents Policy blocks manipulated tool calls before the MCP server runs. Create a Tool Use rule with these settings:

- Applications - **Cursor**
- Tools - **MCPs**
- Detector in the Engine Profile - **Jailbreak and Prompt Injection** detector
- Action - **Block**

This configuration blocks the tool call before the MCP server runs when the agent is manipulated into unsafe tool use.

### Block Sensitive Data with Tools for Calls and Responses

Developers are configuring coding agents with Claude with access to the local file system. This is a security risk because the agent can send sensitive data in a tool call or receive as part of a response. For example, SSH keys, AWS credentials, or ENV file content. You can use the Coding Agents Policy to block sensitive data in tool calls before the tool reads or transmits the content. In addition, it blocks tool responses before the content reaches the agent context. To block sensitive data for tools, create a Tool Use rule with these settings:

- Applications - **Claude Code**
- Tools - **Any**
- Detector in the Engine Profile - **Secrets and Passwords** detector
- Action - **Block**

This configuration blocks tool calls that contain sensitive data before the content is read or transmitted, or before the content is returned to the agent.

## Configuring Coding Agents Policy

Coding Agents Policy supports two rule types.

- **User Message** rules apply to the prompt layer between the user and the agent.
- **Tool Use** rules govern agentic actions by inspecting tool calls from the agent and tool messages returned to the agent.

For a list of the detectors supported for each rule type, see [this article](/v1/docs/configuring-ai-security-engine-profiles#configuring-detectors).

Coding Agents Policy is not an ordered rulebase. Cato evaluates the relevant rules independently, so multiple rules can apply to the same coding agent or the same coding-agent interaction.

![coding_agents.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/coding_agents.png)

### Rule Components

Each rule includes these main components:

- **Type** - User Message or Tool Use rule
- **Source** - Where the activity originates
- **Applications** - Coding agents the rule applies to
- **Tools** - The AI tools for the rule (for Tool Use rules)
- **Engine Profile** - Which AI Security checks are applied to the activity
- **Action** - Matched activity is monitored or blocked
- **Enabled** - Defines whether the rule is active

## User Message Rules

User Message rules focus on the content exchanged between the user and the coding agent. Use this rule type to inspect prompts sent to the agent and responses returned by the agent.

**To create a User Message rule:**

1. From the navigation pane, select **AI Security > Agent Policy**.
2. Click **New** and select **User Message Rule**.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider. Green is enabled, and grey is disabled.
5. Select the **Users** or **User Groups** that are the activity **Source**.
6. In **Applications**, select the AI agents.
7. Select the **AI Security Engine Profile** that is applied to the rule.
8. In **Action**, select to **Monitor** or **Block** the user messages.
9. Click **Add** and then click **Save**.

## Tool Use Rules

Tool Use rules focus on the agent’s interactions with connected tools after the message exchange starts. This rule type adds more granular controls for tool-related activity, including:

- **Tools** - Select the tools that the rule applies to, based on tool activity identified in the Scout and Hooks workflow. **Note:** When you select multiple tools, there is an OR relationship between them.
- **Approval Status** - Cato’s sanctioned and unsanctioned app classification, so you can apply different controls to approved and unapproved tools.
- **MCPs** - Select specific MCP servers that the Tool Use rule applies to.
- **Raw Tool Names** - Match the Tool Use rule to the exact tool name reported by the agent or tool interaction.

**Note:** Claude Cowork is available as an EA feature.

**To create a Tool Use rule:**

1. From the navigation pane, select **AI Security > Agent Policy**.
2. Click **New** and select **Tool Message Rule**.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider. Green is enabled, and grey is disabled.
5. Select the **Users** or **User Groups** that are the activity **Source**.
6. In **Applications**, select the AI agents.
7. In **Tools**, you can apply the rule to a specific tool activity.
8. Select the **AI Security Engine Profile** that is applied to the rule.
9. In **Action**, select to **Monitor** or **Block** the user messages.
10. Click **Add** and then click **Save**.

## Monitoring Agent Policy Activity

After you publish the Coding Agents Policy rules, use Agent Sessions to review the sequence of supported interactions captured for a coding-agent session. This view helps you trace the violation to the specific step in the session, such as a user prompt, an agent response, a tool call, or a tool message, and see whether the rule monitored or blocked that activity. For example:

- Identify which step in the session triggered the policy violation.
- Trace the sequence of prompts, tool calls, tool messages, and agent responses in the session.
- Investigate which tool or MCP-related interaction introduced the risky activity.

## Agent Sessions

Unlike simple chatbot interactions, AI agents can execute chains of tool calls before producing a response. A single user request can trigger multiple actions, so you need session tracing to understand how the interaction progressed and which step triggered a policy action.

The Agent Sessions page provides session tracing for the complete recorded lifecycle of an AI agent interaction. A session captures the full sequence of events that occur when an agent processes a request, including:

- **User prompts** - What the user asked the agent
- **Model responses** - How the AI model responded
- **Tool calls** - Which tools the agent invoked and with what parameters
- **Tool responses** - What those tools returned
- **Final output** - How the agent used the tool results to formulate its answer

![AgentSessions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/AgentSessions.png)

**To open the Agent Sessions page:**

1. From the navigation pane, select **AI Security > Agent Sessions**.

## Supported Detectors

The following table lists the supported Engine Profiles for the Coding Agents Policy and which rule type it can be applied to.

| Engine Profile | User Message Rules | Tool Use Rules |
| --- | --- | --- |
| Name | Supported | Supported |
| Address | Supported | Supported |
| Email | Supported | Supported |
| Phone Number | Supported | Supported |
| Credit Card Number | Supported | Supported |
| IBAN | Supported | Supported |
| Bank Account Number | Supported | Supported |
| Swift Number | Supported | Supported |
| Crypto Address | Supported | Supported |
| Driver License ID Number | Supported | Supported |
| Vehicle ID | Supported | Supported |
| Passport Number | Supported | Supported |
| ID Number / SSN | Supported | Supported |
| Tax ID Number | Supported | Supported |
| VAT ID Number | Supported | Supported |
| Health ID Number | Supported | Supported |
| Medical Record Number | Supported | Supported |
| Health Plan Beneficiary Number | Supported | Supported |
| Secrets & Passwords | Supported | Supported |
| IP Address | Supported | Supported |
| MAC Address | Supported | Supported |
| URL | Supported | Supported |
| Custom Regex Pattern | Supported | Supported |
| Harmful or Unsafe Content | Supported | Not supported |
| Jailbreak and Prompt Injection | Not supported | Supported |
| Obfuscation Attack | Not supported | Supported |
| Topic-based detectors (e.g. Code Sharing, AI Usage Regulation) | Not supported | Not supported |
| Custom Topic and Intent | Not supported | Not supported |
| Language Detection | Not supported | Not supported |
