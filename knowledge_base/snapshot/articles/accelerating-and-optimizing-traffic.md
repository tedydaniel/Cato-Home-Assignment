---
title: "Accelerating and Optimizing Traffic"
slug: "accelerating-and-optimizing-traffic"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/accelerating-and-optimizing-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Accelerating and Optimizing Traffic

This article discusses how the Cato Cloud accelerates and optimizes traffic. For more about configuring these settings, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

## Accelerating Traffic

CATO enables acceleration for TCP traffic. You can configure the default system settings for acceleration, and through network rules you can override the system acceleration default.

Each Cato PoP can act as a TCP proxy server, reducing latency. The proxy server effectively makes TCP clients and servers believe their destinations are closer than they really are, allowing them to set a larger TCP window. In addition, the Socket's advanced version of TCP congestion control lets endpoints connected to the Socket send and receive more data before waiting for acknowledgment. This increases the total throughput while reducing the time needed to remediate errors such as packet loss.

You can define and manage your acceleration settings from a centralized location with as much granularity as required as part of the network rules.

### How Does Cato Acceleration Work?

When TCP acceleration is enabled for a flow, Cato establishes a proxy between the client and the PoP (last mile), between the PoPs (middle mile), and eventually egresses the PoP to the destination.

### Why Does this Enhance Your Throughput?

As an example, consider a TCP flow between London and New York over the Internet in which a packet did not reach its destination (lost). If the proxy is disabled, when the destination receives the next packet, it understands a packet is lost and requests the client to retransmit that packet (as per TCP protocol). This will cost a full RTT between London and New York before flow transmission can continue.

With Cato, the RTT is significantly reduced due to multi-segmenting the traffic path to the last and middle mile. In the above example, instead of lost packet retransmission between London and New York, the lost packet is detected, for example, between London and Cato’s London PoP.

As Cato uses large Tier-1 links to carry traffic across the middle mile, packet loss is rare in this segment.

## Optimizing Traffic

Cato Socket's optimization mechanism mitigates packet loss through packet duplication. Because this increases the total throughput, optimization should be used only on critical flows that are sensitive to packet loss (such as voice and video traffic).

You can define and manage your optimization settings from a centralized location with as much granularity as required as part of the network rules.

### How Does Cato Optimization Work?

When you enable optimization, Cato performs one of the following optimization methods based on the site’s topology and existing connections:

- Packet duplication - used when more than one active link is available. With this technique, Cato sends duplicate packets over another active link while reassembling packets at the other end. Since a redundant packet is sent for any given packet, packet loss mitigation increases even if a packet is lost on one of the links.
- UDP retransmission - used when only a single active link is available. With this technique, Cato retransmits UDP packets (waiting 5 msec prior to retransmission). Since a redundant packet is sent for any given packet, packet loss mitigation increases even if a packet is lost.

> [!NOTE]
> Note:
> 
> As TCP performs retransmission as part of its protocol, UDP retransmission effectively mitigates packet loss for the other commonly-used protocols.

## Transaction Processing Latency

Transaction processing latency measures the time from when the Cato Single Pass Cloud Engine (SPACE) receives network data packets for a transaction until the complete transaction is received by the client or host. This latency can be up to 10 milliseconds for both decrypted and non-decrypted transactions of up to 1MB of data.
