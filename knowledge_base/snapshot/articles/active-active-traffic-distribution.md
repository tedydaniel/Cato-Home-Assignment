---
title: "Active/Active Traffic Distribution"
slug: "active-active-traffic-distribution"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/active-active-traffic-distribution"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Active/Active Traffic Distribution

**How is traffic distributed across the WAN links of a Socket in Active/Active mode?**

Traffic will be distributed across the WAN links based on health metrics, link preference, and the propotional ratio of the configured bandwidths for each link. The distribution is flow-based rather than packet-based.

A flow is a conversation between a client and a server in which all the packets share the same 5-tuple:

1. Source IP address
2. Source port
3. Protocol
4. Destination IP address
5. Destination port

**Example Flow**

A user with IP address 192.168.1.20 connects to a mail server with IP address 10.10.10.2 to send an email. A flow is created with the following 5-tuple:

1. Source IP: 192.168.1.20
2. Source port: 34579
3. Protocol: TCP
4. Destination IP: 10.10.10.2
5. Destination port: 25

**How Distribution Works**

Each flow is distributed in the following order:

1. Every second, Cato evaluates the link quality of each active link by calculating a score based on health metrics that include packet loss, jitter, and latency. The following are the minimal link quality metrics, which are configurable under the Site's Advanced Configuration:

If there is no internet connectivity, the link will not be selected for traffic distribution. Also, if a link can't meet one of the above metrics, it receives a lower priority and is less likely to be used for new traffic flows.

Cato constantly checks that the link quality of the interface chosen is still healthy and meets [acceptable SLA](/v1/docs/understanding-acceptable-and-unacceptable-sla-for-sites) (based on the 1-second checkup results). If it is healthy, packets continue to flow through the link. If the link is not healthy and has unacceptable SLA, the Socket immediately chooses the best link for the traffic flows.
  - Packet loss - 3%
  - Jitter - 30 ms
  - Latency - 600 ms
2. If all active links satisfy link quality metrics, traffic distribution follows the preferred interface selected in the network rule.

![networkRuleInterface.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28022686322205.png)
3. If there's no preferred interface (automatic role) in the network rule, the Socket considers the active/active bandwidth configuration from the CMA.

In the example below, the WAN1 link is configured with a bandwidth of 100 Mbps down/up, and the WAN2 link is configured with 20 Mbps down/up.

![Active-Active_Socket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28022686389277.png)

In this configuration, the WAN1:WAN2 bandwidth ratio is 100:20 or 5:1 for both upstream and downstream traffic. Therefore, five flows will be sent to WAN1 for every one flow that is sent to WAN2.

The Socket and the PoP that it's connected to share the duties of flow distribution. The Socket itself only takes the upstream bandwidth into consideration because it only controls the traffic sent from the Socket to the PoP (upstream traffic). The PoP takes the downstream bandwidth of the Socket into consideration because it controls the traffic sent from the PoP to the Socket (downstream traffic).

**Failover**

If one of the WAN links goes down, packets belonging to flows that were assigned to that link will be sent to the WAN link that is still up. This ensures that any existing flows will not be discarded, although a slight, temporary disruption may be observed for connection-sensitive applications like video conferencing during the failover process.
