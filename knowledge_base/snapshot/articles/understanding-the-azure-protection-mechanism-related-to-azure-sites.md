---
title: "Understanding the Azure Protection Mechanism Related to Azure Sites"
slug: "understanding-the-azure-protection-mechanism-related-to-azure-sites"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/understanding-the-azure-protection-mechanism-related-to-azure-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the Azure Protection Mechanism Related to Azure Sites

## Overview

Azure has a DDOS protection mechanism that limits traffic to a specific public IP (for example, a Cato PoP). This might impact the performance of a vSocket or an IPSec connection installed in the Azure cloud, and also cause severe packet loss.

Recently, Cato noticed a few customers have experienced significant packet loss due to Azure’s default infrastructure DDoS Protection. The problem arises when the DTLS (UDP/443) tunnel traffic exceeds the threshold of 200k packets-per-second (PPS) per destination IP, triggering Azure’s DDoS protection mechanisms. This triggers Azure to throttle the traffic to a limit of 1k packets-per-second. This limit is applied globally, meaning it aggregates traffic from all Azure sources to a single destination IP.

## Frequently Asked Questions (FAQs)

### What caused the packet loss issue?

The packet loss was caused by Azure’s default DDoS protection mechanisms, which drop packets when traffic exceeds 200,000 PPS to a single destination IP. This is to prevent potential outbound attacks.

### How would a customer detect if there’s a problem with Azure?

For Azure vSocket sites, if there is an extremely high packet loss, it might indicate that Azure activated their DDOS protection. To see the high packet loss, please check Network > Site Monitoring > Network Analytics, and look for packet loss as presented below:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22754765034909.png) If you see increased packet loss on the last-mile between the Azure site and the Cato Cloud, especially upstream, this might indicate that Azure DDoS protection was triggered. Open a support ticket with Azure to further investigate the issue.

An incident of high last-mile packet loss between the Azure site and the Cato Cloud, especially in the upstream direction, should be considered as a possible result of Azure DDoS mitigation and trigger opening a support ticket with Azure for further investigation.

### What temporary solutions have been implemented?

Azure has temporarily increased the PPS threshold for the affected IPs to 2 million PPS until April 2025.

### Is there a permanent solution to this issue?

Currently, there is no permanent solution. However, Cato is working closely with Azure to provide such a solution. Customers are encouraged to monitor their traffic and work with Azure support to find long-term strategies to mitigate the impact.

### What should customers do if they experience similar issues?

Customers should immediately report the issue to **Azure support** and provide detailed information about their traffic patterns and also share it with Cato. In addition, please open a Support ticket with Cato as well. Cato will work together with Azure to prevent future incidents.

**Recommended Traffic Settings**

- Customers should consider implementing traffic distribution strategies to avoid exceeding the Azure PPS threshold.
- For accounts that use the Cato Smart SLA setting (Network > Connection SLA), this means the vSocket will connect to a different IP address after 10 minutes of link quality issues.
  - For impacted Azure vSocket sites, set a custom SLA with lower unacceptable SLA values to reduce the downtime for impacted IP addresses. For more information, see [Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites)
