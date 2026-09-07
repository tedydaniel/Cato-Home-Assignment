---
title: "What is Custom AI Agents Security"
slug: "what-is-custom-ai-agents-security"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/what-is-custom-ai-agents-security"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Custom AI Agents Security

## Overview

Custom AI agents let you build AI-driven workflows in code and connect them directly to internal systems, databases, and third-party services. Organizations often build these agents by using frameworks such as LangChain, the OpenAI Agents SDK, or direct API calls to LLM providers. Because these agents are deeply integrated into business workflows and often have access to sensitive data and tools, they require runtime visibility and protection.

AI Security for Agents secures custom agents through direct integration with the Cato AI Firewall (AI-FW) at the SDK level. Developers can connect a custom agent to the AI-FW with minimal code changes, typically by redirecting the LLM base URL to the AI-FW proxy endpoint and adding an authentication header. The AI-FW then sits transparently in the request path, inspecting traffic between the agent and the LLM while proxying requests to the original provider. This lets you trace agent activity and enforce runtime protections without changing the agent’s core logic or adding a separate security layer.

## Use Cases

### Tracing Custom Agent Activity

Once a custom agent is connected to the AI-FW, all of its interactions are automatically traced and visible in the dashboard. Every invocation, including the full conversation history, tool calls with their parameters, tool responses, and the agent's final output, is recorded as a session. Security teams can browse, search, and investigate these sessions just as they would for managed or local agents.

Tracing for custom agents is especially valuable because these agents are often the hardest to get visibility into. The AI-FW integration provides this instrumentation with minimal developer effort, turning a previously opaque system into a fully observable one.

### Runtime Protection from AI Attacks

The AI-FW provides active runtime protection for custom agents using the same Guards and policy engine that protects the rest of the agent estate. Because the AI-FW is in the request path between the custom agent and the LLM provider, it can enforce policies in real time - blocking or alerting on violations before they reach the model, tool, or the user.

This is particularly critical for custom agents because they are often the most exposed to attack. A custom agent that queries external APIs, reads from databases, or processes user-uploaded documents is vulnerable to indirect prompt injection through any of these data sources. An attacker who can influence the content returned by a tool, even something as simple as a poisoned field in a database record or a malicious string in a document, can attempt to hijack the agent's behavior. The AI-FW inspects tool responses at the content level, detecting injection payloads before they reach the model and influence subsequent tool calls or outputs.

For organizations building production-grade custom agents, the AI-FW integration also provides protection against jailbreak attempts, sensitive data leakage (PII, credentials), and policy violations, all without requiring changes to the agent's core logic. The security team configures policies centrally in the dashboard, and those policies are enforced transparently across all connected custom agents.
