---
title: "Multiple CMA Events Are Generated For The Same Traffic Flow"
slug: "multiple-cma-events-are-generated-for-the-same-traffic-flow"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/multiple-cma-events-are-generated-for-the-same-traffic-flow"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multiple CMA Events Are Generated For The Same Traffic Flow

## Issue

Multiple CMA events, such as Internet/WAN Firewall, IPS, RPF, or Anti-Malware are generated for the same traffic flow. Having multiple events for the same traffic can be confusing when troubleshooting allowed or blocked actions over the Cato Cloud.

## Troubleshooting

This behavior may be observed across various types of CMA events. Below are some possible scenarios that can occur:

#### Same Event Actions

In this scenario, the traffic flow was blocked by the **Firewall** engine because it was categorized as "Botnet", which is a category blocked in an Internet Firewall rule. Simultaneously, the IPS engine also blocked the traffic since it matches the **IPS** signature "cid_heur_suspicious", which is also based on the website's category.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20054918774429.png)

#### Different Event Actions

In this scenario, the traffic flow is initially blocked by the **IPS** engine due to a geo-restriction policy. However, the TLS/HTTP connection is established with the client to get traffic information so the **Firewall** engine can make a decision, which in this case is to allow (Action: Monitor) the traffic flow. Traffic is ultimately blocked by the **IPS** engine and no packets reach the destination IP.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20054504192541.png)

## Explanation

As explained in [Understanding Packet Flow with Cato](/v1/docs/understanding-packet-flow-with-cato-space-architecture), the Cato Cloud includes multiple networking and security engines that operate **in parallel**. This means there is no prioritization for one engine to evaluate traffic over another.

Furthermore, the block/allow decisions are not performed immediately. The PoP waits until a specific request/response stage is reached (e.g., HTTP request), and each engine performs a definitive block or allow action. This is why we might observe multiple events generated in CMA with the same or different block/allow conclusions.

When different actions are seen in various events, the **block** action will take precedence over an **allow** action.
