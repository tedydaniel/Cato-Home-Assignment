---
title: "What is AI Security for Agents"
slug: "what-is-ai-security-for-agents"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/what-is-ai-security-for-agents"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is AI Security for Agents

## Overview

AI Security for Agents lets you securely adopt AI agents in your organization without losing visibility or control over how they access data, use tools, and perform actions. You can protect agent workflows from prompt injection, unauthorized data access, sensitive data exposure, and other misuse that can lead to security or compliance risks.

Cato classifies AI agents into these categories:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35504464454557(1).png)

Local agents typically run on the user endpoint and are mostly provided by third parties. Managed agents are generally low-code or no-code agents provided by cloud platforms and SaaS providers. Custom agents are fully coded agents that you build and run on endpoints or in cloud environments.

AI Security for Agents gives you a unified way to monitor and govern these agent types across the environments you manage. This helps you confidently deploy AI agents while maintaining policy enforcement, reducing operational risk, and supporting your compliance requirements.

## Risks Presented by AI Agents

AI agents that operate autonomously and interact with tools, data, and external systems introduce unique security, compliance, and governance risks that go beyond traditional AI chatbot threats:

- **AI-specific attacks** - including: prompt injection, jailbreak attempts, and multi-turn attacks designed to manipulate agent behavior. Unlike chatbots, agents can also be attacked through their tool responses (indirect prompt injection), where a malicious payload in a tool's output can hijack the agent's actions.
- **Data exfiltration** - agents that have access to code repositories, internal APIs, CRM systems, or file systems. These agents may inadvertently or maliciously leak sensitive data such as source code, credentials, personal identifiers, or financial data through tool calls or model outputs.
- **Shadow agents** - there can be unmanaged or unauthorized AI agents installed by employees without IT approval, creating blind spots in security posture. This includes personal instances of coding assistants running without enterprise licenses or security controls.
- **MCP server risks** - malicious or misconfigured MCP servers can expose sensitive data, execute unauthorized commands, or introduce vulnerabilities into the agent's workflow.
- **Compliance violations** - failure to meet regulatory requirements for AI systems, such as the EU AI Act, or internal policies governing code generation, data handling, and automated decision-making.
- **Governance gaps** - lack of visibility into which agents are deployed, what tools they connect to, and what data they can access, making it impossible to enforce consistent security policies across the organization
