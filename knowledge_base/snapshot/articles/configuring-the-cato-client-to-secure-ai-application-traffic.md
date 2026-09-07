---
title: "Configuring the Cato Client to Secure AI Application Traffic (EA)"
slug: "configuring-the-cato-client-to-secure-ai-application-traffic"
updated: 2026-08-19T13:44:47Z
published: 2026-08-19T13:44:47Z
canonical: "knowledge.catonetworks.com/configuring-the-cato-client-to-secure-ai-application-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Cato Client to Secure AI Application Traffic (EA)

This article provides information about routing only AI application traffic through the Cato Cloud using the Cato Client.
{{snippet.EA note}}
## Overview

Cato lets you secure AI application traffic from managed endpoints without replacing your existing SASE, Internet security, or VPN solution. You can configure the Cato Client to route selected AI application traffic to the Cato Cloud for inspection and AI Security policy enforcement, while all other traffic continues through your existing security stack.

This deployment is useful when you want to enforce AI Security policies for browser-based and native AI applications, but you do not want to route all endpoint traffic through Cato. To support this use case, configure the Client with a Split Tunnel policy that routes only selected AI application traffic to Cato.

### How Cato Secures Selected AI Application Traffic

The Cato Client acts as the endpoint on-ramp to the Cato Cloud. After the Client connects, the Split Tunnel policy determines which traffic is routed to Cato and which traffic bypasses the Cato tunnel.

For this type of deployment, configure the Split Tunnel policy to route only selected traffic to Cato as destination inclusions. Cato then inspects the matching traffic and applies AI Security policy rules.

Traffic that does not match the selected AI applications is not routed to Cato and continues through the existing customer security stack.

### Prerequisites

Before you configure this deployment, make sure the account meets these requirements:

- AI Security is enabled for the account
- The relevant users are licensed to connect with the Cato Client 
- The Cato Client is deployed to the relevant endpoint devices
- The endpoint devices use a supported Client version:
  - Windows Client v6.4 or higher for application-based destinations 


## Deploying the Cato Client

[Deploy the Cato Client](/v1/docs/getting-started-with-the-cato-client) to the users and devices that need AI Security enforcement. These users do not need to route all endpoint traffic through Cato, but the Client must be installed and connected so selected AI application traffic can be forwarded to the Cato Cloud.

For the best user experience, deploy the Client using your standard endpoint management tool. For Windows devices joined to Microsoft Entra ID, you can use seamless authentication so the Client connection is established with minimal user interaction.

After the Client is deployed, make sure the users are included in the relevant [Client Connectivity Policy](/v1/docs/client-connectivity-policy) and can connect to the Cato Cloud.

## Configuring the Split Tunnel Policy

Configure the [Split Tunnel policy](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) to route only selected AI application traffic to Cato.

1. From the navigation menu, go to **Access > Split Tunnel**.
2. Create a new rule.
3. In **Select Connection Mode**, select **All Ports & Protocols (recommended)**.
4. In **Choose Routing Policy**, select **Route only selected to Cato**.
5. In **DNS Inclusions**, add the DNS destinations required to resolve the selected AI applications.
Add only the DNS traffic required for the selected AI applications. Do not select **Any** unless you want all DNS traffic from the Client to route to Cato.
6. In **Destination Inclusions**, add the AI applications that you want to route to Cato.
7. Save the rule.
8. Make sure the rule is enabled and applies to the relevant users or groups.

## Sample Configuration for Routing AI Application Traffic to Cato

This example routes selected AI application traffic to Cato while all other endpoint traffic continues through the existing security stack.

In this example:

- **Connection Mode**: **All Ports & Protocols (recommended)**
- **Routing Policy**: **Route only selected to Cato**
- **DNS Inclusions**: DNS destinations required to resolve the selected AI applications
- **Destination Inclusions**:
  - DeepSeek
  - Gemini
  - Claude

Use this sample configuration as a starting point. The exact DNS inclusions can vary based on the DNS architecture in your environment and the AI applications you route to Cato.

**Note:** Cato recommends that you add the full list of supported AI apps your organization uses to ensure that all AI user traffic is routed through Cato.

## Configuring AI Security Policy Rules for Client Traffic

After the Split Tunnel policy routes the selected AI traffic to Cato, configure your User Interaction Policy rules to inspect and control that traffic.

The policy applies only to the AI application traffic that reaches the Cato Cloud. Make sure the Split Tunnel policy includes the AI applications that you want the AI Security policy to inspect.

## Supported Traffic

This deployment can secure AI application traffic from:

- Browser-based AI applications
- Native AI applications
- Managed endpoint devices with the Cato Client installed and connected

Browser-only enforcement methods can help secure web-based AI usage, but they do not cover native AI applications. Use the Cato Client when you need to secure both browser-based and native AI application traffic.

## Recommended Applications
The following applications are recommended to configure:

* Claude
* ChatGPT
    * ChatGPT for Business
    * ChatGPT Personal 
* Perplexity
* Grok (X.ai)
* Gemini Advanced
* Microsoft Copilot
* Microsoft Copilot (enterprise)
:::(Info) (Note)
To fully cover Copilot for Enterprise, configure Microsoft Copilot in the policy together with one of the following:

* The **Microsoft Office365** application
* `substrate.office.com` domain

If users access Copilot as an add-on within other Office apps, and you don’t want to include **Microsoft Office365** in the policy, also add these domains:

* `augloop.office.com`
* `augloop.svc.cloud.microsoft`

:::

* Atlassian JIRA and Comfluence
* Le Chat (Mistral AI)
* DeepSeek
* Anthropic for Business

## Limitations and Considerations

### Existing SASE or VPN Solutions

This deployment is designed to work alongside an existing SASE, Internet security, or VPN solution. However, interoperability depends on the configuration of the other solution.

You may need to configure the existing solution so it does not block or override the Cato Client traffic for the selected AI applications.

### DNS Routing

Make sure **DNS Inclusions** match the DNS traffic required for the selected AI applications. Avoid selecting **Any** unless the deployment intentionally routes all DNS traffic to Cato.

### Client Version Support

Support for FQDN-based and application-based destination inclusions depends on the Client operating system and version. Confirm the minimum supported Client version before deploying this configuration in production.
