---
title: "What is Managed AI Agents Security"
slug: "what-is-managed-ai-agents-security"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/what-is-managed-ai-agents-security"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Managed AI Agents Security

## Overview

AI Security for Managed Agents lets you discover, trace, and protect AI agents that run on managed AI platforms such as AWS Bedrock, Azure AI Foundry, and Microsoft Copilot Studio. You gain visibility into which agents exist, what data sources and tools they can access, and how they behave at runtime.

Managed platforms provide the infrastructure for creating, deploying, and scaling AI agents - but they also introduce a distinct set of security and governance challenges. Organizations often lack a centralized visibility into which agents exist across these platforms, what data and tools they can access, and how they behave at runtime.

AI Security for Managed Agents helps you reduce the risk of unauthorized access, sensitive data exposure, and unsafe agent actions while supporting governance and compliance requirements.

## Use Cases

### Discovering Managed Agents

The first step in securing managed agents is knowing what exists. Cato connects to managed AI platforms via API and automatically discovers all agents deployed within the environment. For each agent, the system collects a comprehensive inventory that includes the agent's name, purpose, and configuration instructions, its connected tools and connectors, its knowledge bases and data sources, and the permissions and access controls assigned to it.

### Tracing Agentic AI Activities

Managed AI platforms generate tracing data as agents execute - recording the sequence of prompts, model responses, tool invocations, and results that make up each agent session. Cato queries this tracing data directly from the platform and streams it into the Agentic AI dashboard, providing real-time visibility into how managed agents are actually behaving in production.

Tracing captures the full lifecycle of an agent interaction: what the user asked, how the model responded, which tools the agent invoked (and with what parameters), what those tools returned, and how the agent used the tool results to formulate its final output. This level of detail is essential for understanding agentic behavior because, unlike a simple chatbot, an agent may execute a chain of multiple tool calls, each building on the previous result, before producing a response. A single user request can trigger a complex sequence of actions that would be invisible without tracing.

For security and compliance teams, tracing provides the evidence needed for incident investigation and audit. If a managed agent accesses data it shouldn't have, makes an unexpected tool call, or produces an output that violates policy, the tracing record shows exactly what happened - step by step. This is also invaluable for understanding the blast radius of an incident: tracing reveals not just what went wrong, but what data was touched and what actions were taken along the way.

### Protection via AI Firewall Integration

Discovery and tracing provide visibility, but organizations also need active protection for their managed agents. Cato achieves this by streaming the traced agent invocations into the AI Firewall (AI-FW), where they are evaluated against the same Guards and policies used across the rest of the agent security stack.

This integration means that every prompt, model response, tool call, and tool message flowing through a managed agent is inspected by the AI-FW engine. The engine applies detection models for prompt injection, jailbreak attempts, sensitive data exposure, and policy violations, the same four-point inspection that protects local and custom agents. When the AI-FW detects a threat, it can alert the security team, log the event for compliance purposes, or, depending on the integration and enforcement mode, block the violating interaction.
