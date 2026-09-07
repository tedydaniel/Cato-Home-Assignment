---
title: "Working with AI Security Guards"
slug: "working-with-ai-security-guards"
updated: 2026-09-02T07:21:01Z
published: 2026-09-02T07:21:01Z
canonical: "knowledge.catonetworks.com/working-with-ai-security-guards"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with AI Security Guards

AI Security Guards help you protect and govern the AI-powered applications that you build, and enforce security controls in runtime. They let you enforce rules to inspect and control traffic between the AI applications that you build, your users, and supported AI models. You use guards to detect malicious prompts, unsafe content, and sensitive data exposure before they affect your application. Guards also give you visibility into how AI applications are used, so you can monitor violations and enforce organizational policies with a consistent control point.

A guard acts as the enforcement layer for AI Security. It evaluates prompts and, when relevant, model responses against the detections and actions that you configure in your policy. Based on the policy match, the guard can allow, block, or log the interaction.

## How Guards Work

Guards inspect AI traffic and compare it to the detections and actions that are defined in your policy. This lets you apply security and governance controls to AI interactions before the traffic reaches the model provider, and in some cases, before the response is returned to the user.

### Traffic Flow

AI Security supports different traffic flow models, depending on how your application integrates with the guard.

- Proxy Mode - In this mode, the guard sits inline between the application and the AI provider. Your application sends requests through the guard, which forwards traffic to the provider after evaluating the content against policy.

This mode lets you apply controls directly in the traffic path. The guard can inspect the request before it reaches the provider and, where supported, inspect the response before it is returned to the application. This gives you a direct enforcement point for real-time protection and visibility.

![image (19).png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36731069242269.png)
- API Mode - In API mode, your application interacts with the guard via an API-based integration rather than routing traffic through an inline proxy. The application sends the relevant content to the guard for evaluation as part of the application flow.

This mode gives you more flexibility for environments where an inline deployment is not the preferred architecture. The guard still evaluates the content against policy, but the enforcement flow depends on how your application is integrated with the guard.

![image (20).png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36731069244445.png)

### What does the Guard Detect and Enforce

You can use guards to detect and enforce policy for a range of AI-related risks, including:

- Prompt injection attempts
- Unsafe or restricted content
- Sensitive data exposure, such as personally identifiable information (PII) or protected health information (PHI)
- Topic or usage violations based on company policy
- Suspicious or non-compliant AI interactions

When a guard detects a match, it applies the action that is configured in the policy. For example, the guard can block a request, allow it, or log the event for monitoring and investigation.

## Use Case - Protecting an Internal AI Assistant

Your company uses an internal AI assistant to help employees search internal documentation and summarize content. To reduce the risk of sensitive data exposure, prompt injection, and policy violations, you apply an AI Security guard to the application traffic.

The guard inspects prompts and, where supported, responses against your AI Security policy. You can detect unsafe or non-compliant interactions and block or log them before the content reaches the AI provider or is returned to the user.

## Supported Providers

Proxy mode supports the following providers and API formats.

| Selected AI Service | Supported Platforms | Supported APIs |
| --- | --- | --- |
| Google AI Studio Gemini Enterprise Agent Platform (Vertex AI) | - Google AI Studio - Gemini Enterprise Agent Platform (Vertex AI) | - Gemini API: generateContent, streamGenerateContent - OpenAI-compatible API: chat completions |
| Anthropic’s Claude | - Claude Platform - Any Claude-compatible endpoint, such as: - Microsoft Foundry - Amazon Bedrock | - Claude API: messages, complete (legacy) - OpenAI-compatible API: chat completions |
| OpenAI Public API | - OpenAI Platform | - OpenAI API: responses, chat completions, embeddings |
| Azure OpenAI Service | - Azure OpenAI | - OpenAI API: chat completions |
| Amazon’s Bedrock | - Amazon Bedrock | - Bedrock API: Converse, ConverseStream |
| Custom Endpoint | - Any OpenAI-compatible endpoint, such as: - Microsoft Foundry - Amazon Bedrock - Gemini Enterprise Agent Platform (Vertex AI) | - OpenAI API: responses, completions, embeddings |

##
