---
title: "When is a Flow Assigned QoS Priority 255?"
slug: "when-is-a-flow-assigned-qos-priority-255"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/when-is-a-flow-assigned-qos-priority-255"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# When is a Flow Assigned QoS Priority 255?

## Question

When is a flow categorized with QoS priority 255, even though there is no network rule to assign this priority?

## Answer

QoS priority 255 is referred to as the **Default** priority in the **BW Management** window (**Network > BW Management**).

There are several reasons why a flow can be assigned the lowest QoS priority 255:

- Blocked/prompted flows will be categorized according to the configured network rule. If none exists, they will be categorized as P255.
- Traffic that is redirected from a block page is assigned QoS priority 255. For example, when someone tries to go to a compromised website that is blocked by IPS.
- At the destination site (WAN flows), the first packets, before the flow is identified, are assigned the lowest QoS priority 255.

The flow will get the highest priority when:

- Cato evaluates the network profile for each flow, and the QoS priority is assigned when the flow is identified with a specific application as follows:
  - At the source site, the first packets, before the flow is identified, are assigned the highest QoS priority.
  - Until the application behind the flow is recognized, it retains the highest QoS priority. This can be seen in the Analytics window until the application is identified.
