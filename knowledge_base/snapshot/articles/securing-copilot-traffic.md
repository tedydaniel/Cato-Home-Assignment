---
title: "Securing Copilot Traffic"
slug: "securing-copilot-traffic"
tags: ["AI Sec - Users"]
updated: 2026-09-01T07:21:57Z
published: 2026-09-01T07:21:57Z
canonical: "knowledge.catonetworks.com/securing-copilot-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Securing Copilot Traffic

## Overview

For organizations that need to secure only Microsoft Copilot with Cato AI Security, you can use the Split Tunnel policy to configure Cato Clients to only route Copilot traffic to Cato for inspection. If all your remote user traffic is routed to the Cato Cloud, the AI Security policies inspect Copilot, and you don't need a Split Tunnel rule for it.

Microsoft delivers Copilot over many domains, and several of them are shared with other Microsoft 365 services, so selecting the **Microsoft Copilot** app in a Split Tunnel rule doesn't route all Copilot traffic to Cato. This article describes which domains to add to a Split Tunnel rule so that the Copilot traffic you want to secure reaches the Cato Cloud, where the AI Security policies inspect it.

**Note:** The instructions for Copilot are accurate as of September 2026. See the Microsoft documentation for the up-to-date list of domains that are related to Copilot traffic.

For more information about the Split Tunnel policy, see [Routing with the Cato Client (Split Tunnel Policy)](https://knowledge.catonetworks.com/docs/routing-with-the-cato-client-split-tunnel-policy) and [Including and Excluding Traffic for the Split Tunnel Policy](https://knowledge.catonetworks.com/docs/including-and-excluding-traffic-for-the-split-tunnel-policy).

### Use Case

Company ABC secures the Internet traffic of its remote users with a third-party solution, and wants Cato AI Security to inspect AI usage for Microsoft Copilot Enterprise. The admin creates a Split Tunnel rule that routes only the Copilot Enterprise traffic to Cato for inspection by the AI Security policies. The rest of the traffic continues to the third-party solution.

### Prerequisites

- DNS Relay is enabled
- Windows Client v6.4 and higher installed on the device

## How Microsoft Copilot Traffic Is Identified

Microsoft doesn't give Copilot its own dedicated set of domains. Copilot is delivered over many domains, and several of them are shared backend services that also carry the traffic of other Microsoft 365 applications. A domain that serves several applications identifies all of them equally, so a shared domain can't indicate Copilot specifically.

For example, `substrate.office.com` carries Exchange traffic and Copilot Enterprise traffic over the same domain. Because that domain identifies Exchange as accurately as it identifies Copilot, it isn't part of the Microsoft Copilot app. Adding it to the app would classify Exchange traffic as Copilot.

The impact on the Split Tunnel policy is that a rule with only the Microsoft Copilot app as the destination routes Copilot Free and Personal traffic to Cato. Copilot Enterprise traffic and Copilot traffic inside Office applications bypass the tunnel and aren't fully inspected. To secure those deployments, add the shared domains to the rule alongside the app.

## Destinations for Each Copilot Deployment

Identify which Copilot deployments your organization uses, and add the destinations for those deployments to the rule. A deployment that your organization doesn't use doesn't need its domains.

Include the **Microsoft Copilot** app in the **Destination Inclusions** of the rule in every case. Cato maintains the domains behind the app and updates them when the application changes, which reduces the maintenance on your rulebase. The domains you add manually are only the shared ones that the app can't cover.

Add the domains under **DNS Inclusions** as well, because the traffic is routed correctly only when the domains are resolved through Cato. An application can't be selected in **DNS Inclusions**, so enter each domain individually.

### Copilot Free and Personal

Copilot Free and Personal is the consumer version of Copilot that employees reach with a personal Microsoft account. The **Microsoft Copilot** app covers all the domains that this version uses, so no additional domains are needed.

- **Destination Inclusions**
  - **Microsoft Copilot** app
- **DNS Inclusions**
  - No changes

### Copilot Enterprise

Copilot Enterprise is Microsoft 365 Copilot licensed to your organization and used through the Copilot web app. It uses substrate.office.com, which the **Microsoft Copilot** app doesn't cover, so add that domain to the rule.

- **Destination Inclusions**
  - **Microsoft Copilot** app
  - substrate.office.com
- **DNS Inclusions**
  - copilot.cloud.microsoft
  - copilot.cloud.microsoft.com
  - copilot.com
  - copilot.microsoft.com
  - copilotstudio.microsoft.com
  - copilotstudio.preview.microsoft.com
  - sydney.bing.com
  - substrate.office.com

### Copilot Embedded in Office Applications

Copilot embedded in Office applications is the set of Copilot features that users work with inside applications such as Word, PowerPoint, and Outlook.

These features use the Augmentation Loop domains (augloop.office.com, augloop.svc.cloud.microsoft) in addition to substrate.office.com.

- **Destination Inclusions**
  - **Microsoft Copilot** app
  - substrate.office.com
  - augloop.office.com
  - augloop.svc.cloud.microsoft
- **DNS Inclusions**
  - copilot.cloud.microsoft
  - copilot.cloud.microsoft.com
  - copilot.com
  - copilot.microsoft.com
  - copilotstudio.microsoft.com
  - copilotstudio.preview.microsoft.com
  - sydney.bing.com
  - substrate.office.com
  - augloop.office.com
  - augloop.svc.cloud.microsoft

## Configuring a Split Tunnel Rule for Copilot

Configure a rule that routes only the Copilot destinations to Cato. All other traffic from the users in the scope of the rule goes directly to the Internet, including traffic to Microsoft 365 services that Copilot doesn't use.

**To configure a Split Tunnel rule for Copilot:**

1. From the navigation menu, click **Access > Split Tunnel Policy**.
2. Click **New > New Rule** and enter a name and description for the rule.
3. Configure the settings for **Users/Groups**, **Source Network**, and **Countries** to define which users the rule applies to.
4. In the **Platforms** section, select **Windows**.
5. In the **Configuration** section, under **Select Connection Mode**, select **All Ports & Protocols**.
6. Under **Choose Routing Policy**, select **Route only selected to Cato**.
7. Enter the **Destination Inclusions** and **DNS Inclusions** based on your Copilot deployment (see above [Destinations for Each Copilot Deployment](/v1/docs/securing-copilot-traffic#destinations-for-each-copilot-deployment1)).
8. Click **Save**, and then publish the policy revision. Matching Copilot traffic is routed to the Cato Cloud the next time the Client connects.

## Sample Split Tunnel Rules for Copilot

The following table shows the configuration for each Copilot deployment. Each rule uses **All Ports & Protocols**, the **Route only selected to Cato** routing policy, and Windows as the platform. Use the row that matches your deployment, or combine the rows for the deployments that your organization uses.

| Rule name | DNS Inclusions | Destination Inclusions |
| --- | --- | --- |
| AI Security Copilot Free | Any | **Microsoft Copilot** |
| AI Sec Copilot - Office | `copilot.cloud.microsoft`, `copilot.cloud.microsoft.com`, `copilot.com`, `copilot.microsoft.com`, `copilotstudio.microsoft.com`, `copilotstudio.preview.microsoft.com`, `sydney.bing.com`, `substrate.office.com`, `augloop.office.com`, `augloop.svc.cloud.microsoft` | **Microsoft Copilot**, `substrate.office.com`, `augloop.office.com`, `augloop.svc.cloud.microsoft` |
| AI Sec Copilot Enterprise | `copilot.cloud.microsoft`, `copilot.cloud.microsoft.com`, `copilot.com`, `copilot.microsoft.com`, `copilotstudio.microsoft.com`, `copilotstudio.preview.microsoft.com`, `sydney.bing.com`, `substrate.office.com` | **Microsoft Copilot**, `substrate.office.com` |

![copilot_split_tunnel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/copilot_split_tunnel.png)

## Known Limitations

- Reassigning a shared domain from another Microsoft application to Microsoft Copilot isn't supported. The shared domains must be added to rules manually until Microsoft separates the Copilot services from the other Microsoft 365 services.
