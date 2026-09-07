---
title: "What is Local AI Agents Security"
slug: "what-is-local-ai-agents-security"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/what-is-local-ai-agents-security"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Local AI Agents Security

## Overview

AI Security for Local Agents lets you discover and secure AI agents that run on user endpoints, such as coding agents. You gain visibility into installed agents, their configurations, license types, connected MCP servers, and runtime activity. This helps you control shadow agents and reduce the risk of data leakage and indirect prompt injection.

## Discovering and Securing Shadow Coding Agents

An engineering organization allows certain teams to use managed coding assistants such as Cursor and Claude Code with an enterprise license. However, individual developers across the company have installed additional AI coding tools without IT approval or enterprise-grade security controls.

AI Security for Agents uses Cato AI Scout to scan endpoints across the organization, identifying all installed AI agents, their configurations, license types, and connected MCP servers. The security team gains a complete inventory of managed and unmanaged agents, enabling them to enforce a consistent security posture - ensuring that only approved, properly configured agents are in use.

## Preventing Data Leakage Through Agent Tool Calls

A development team uses AI coding agents that connect to internal and external systems through MCP servers and other types of tools. While these integrations boost productivity, they also create pathways for sensitive data to flow through the agent and potentially become exposed.

AI Security for Agents enforces runtime policies across all four inspection points: user prompts, model outputs, tool calls, and tool messages. When an agent attempts to send sensitive data, credentials, or PII through a tool call, or when a tool response contains sensitive information that should not be passed to the model, the policy engine detects and blocks/redacts the action in real time. This ensures that agent-assisted workflows remain productive without introducing data leakage risks.

## Protecting Local AI Agents from Indirect Prompt Injection

Local and coding agents are exposed to indirect prompt injection attacks, coming from tools. For example, "EchoLeak" and "CurXecute".

AI Security for Agents provides runtime protection that inspects not only the prompts and responses exchanged with the LLM, but also the content of tool calls and tool messages. When a tool response contains a malicious payload, such as an indirect prompt injection attempting to hijack the agent's behavior, the Cato AI Firewall detects and blocks it before the content reaches the agent. This ensures that external data sources cannot be weaponized to manipulate the agent's actions.
