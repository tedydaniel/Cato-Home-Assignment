---
title: "Why AI Security Policies May Not Be Enforced on Platforms Like Microsoft Copilot When Using Browser Extensions"
slug: "why-ai-security-policies-may-not-be-enforced-on-platforms-like-microsoft-copilot"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/why-ai-security-policies-may-not-be-enforced-on-platforms-like-microsoft-copilot"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Why AI Security Policies May Not Be Enforced on Platforms Like Microsoft Copilot When Using Browser Extensions

## Issue

In some cases, AI security policies are enforced on certain AI applications but not on others when the Browser Extension is connected. For example, policies may be applied to ChatGPT but not to Microsoft Copilot, even though both applications are enabled within the same policy. This article explores the reason behind this behavior.

**NOTE**: This case study focuses on the [Cato Browser Extension](/v1/docs/what-is-the-cato-browser-extension) in the context of AI security and should not be confused with the [AI Security Browser Plugin](/v1/docs/what-is-the-ai-security-browser-plugin).

## Root Cause

The Cato Browser Extension currently supports only [HTTPS traffic](/v1/docs/configuring-the-cato-browser-extension). Non-HTTPS traffic is not routed through Cato, and therefore AI security policies cannot be enforced.

## Troubleshooting

1. Verify that a policy is configured under User Interaction Policy for the relevant traffic. In the CMA, go to AI Security > User Interaction Policy. For browser extension use cases, ensure the policy is defined with a Network Rule as the interception type.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35648735234333(1).png)
2. Verify that the application is supported by Cato and is listed in the dropdown within the network interception rule. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35648646346269(1).png)
3. Finally, confirm that the AI application **uses HTTPS as the underlying protocol** for AI security policies to be enforced. [Capture HAR data](/v1/docs/how-to-collect-har-data) while sending a prompt, then review the entries to locate the request carrying the prompt. In the example below (Microsoft Copilot), the underlying protocol is **WSS://**; therefore, the traffic is sent directly to the internet, bypassing the Cato AI security engine. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35648683633309(1).png)
