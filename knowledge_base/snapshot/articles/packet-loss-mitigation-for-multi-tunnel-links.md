---
title: "Packet Loss Mitigation for Multi-Tunnel Links"
slug: "packet-loss-mitigation-for-multi-tunnel-links"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/packet-loss-mitigation-for-multi-tunnel-links"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Packet Loss Mitigation for Multi-Tunnel Links

## Overview of Cato Packet Loss Mitigation

Cato Networks’ Packet Loss Mitigation feature improves the reliability of data delivery and the quality of IP transport on the last mile of your network. This feature uses the packet duplication technique to mitigate the impact of packet loss, in case of network issues like a congestion. The Packet Loss Mitigation works only for the Cato Cloud transport links. When Packet Loss Mitigation is enabled for a network rule, the Socket duplicates the packets and sends the duplicated traffic over the secondary link. This article explains the packet duplication technique and describes the difference for Packet Loss Mitigation between active/active and active/passive deployments.

### Enabling Packet Loss Mitigation for a Network Rule

The Packet Loss Mitigation increases the link throughput. Therefore, we recommend that you enable it for network rules that route traffic that is sensitive to packet loss such as voice and video. Use the Cato Management Application to enable Packet Loss Mitigation for the appropriate network rules. For more about optimizing traffic and enabling the packet loss mitigation, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

## Packet Loss Mitigation for Active/Active Links

When 2 active links are connected to the Cato Cloud, the Socket simultaneously sends duplicated TCP and UDP packets over the two active DTLS tunnels. The traffic (both original and duplicated traffic) is sent at the same time over both links with no delays. If for any reason, only one link is connected to the Cato Cloud, the Socket sends the packets as follows:

- TCP packet are sent without any packet duplication
- UDP packets are sent with packets duplication and a 5 ms delay.

## Packet Loss Mitigation for Active/Passive Links

For sites that are in active/passive mode, the Socket only duplicates UDP traffic over the active link with a 5 ms delay. TCP traffic isn't duplicated because TCP can handle packet loss. The Socket sends the TCP packets only over the active link and without any packet duplication.

## Considering the Links Bandwidth Configuration

When enabling the Packet Loss Mitigation for a network rule, the Socket duplicates packets that increase the throughput over the links. For links with different bandwidth configuration, the duplicated traffic can saturate the weaker link and drop packets. Therefore, the Socket limits the throughput to prevent packet loss. In this case, the Socket doesn’t optimize the total bandwidth of the links. Cato recommends that you don’t enable the Packet Loss Mitigation for network rules that consume a major part of the link bandwidth. For example, if you have 2 active WAN links: WAN1 is 200 Mbps link and WAN2 is 100 Mbps link. If you enable the Packet Loss Mitigation for all traffic, the Socket sends up to 100 Mbps traffic and not 300 Mbps to prevent reaching the 100 Mbps limit of the WAN2 link. When you calculate the bandwidth of a traffic type, to provide the best last mile connection - enable Packet Loss Mitigation when the duplication doesn’t exceed the link bandwidth limit.
