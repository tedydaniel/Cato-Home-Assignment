---
title: "Socket MTU and DTLS Tunnels"
slug: "socket-mtu-and-dtls-tunnels"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/socket-mtu-and-dtls-tunnels"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket MTU and DTLS Tunnels

## Overview

The Maximum Transmission Unit (MTU) defines the largest packet size that can be transmitted without fragmentation. The MTU setting helps determine packet flow efficiency between the Socket and the PoP. While Ethernet interfaces typically support an MTU of 1500 bytes, DTLS overhead reduces the effective MTU over the tunnel to 1383 bytes. This behavior affects how packets are handled based on fragmentation settings.

![mtu_diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29899340469405(1).png)

## Behavior for Do Not Fragment (DF) Setting (WAN Interfaces)

### DF Set

When the DF bit is set, the Socket handles oversized packets for WAN traffic by sending an ICMP Fragmentation Needed message back to the sender. This message includes the acceptable MTU size (e.g., 1383 bytes), prompting the client to fragment the packet accordingly.

### DF Not Set

If the DF bit is not set and the packet for WAN traffic exceeds the effective MTU, the Socket fragments the packet. The PoP then reassembles the fragments and forwards the complete packet to the destination. This behavior ensures continuity but may have implications for packet loss visibility in monitoring tools.

## Socket LAN Ports and Jumbo Frames

Cato doesn’t support jumbo frames on Socket LAN ports. When the Socket receives a packet larger than 1500 bytes on a LAN port, it checks the Do Not Fragment (DF) bit.

- If the DF bit is not set, the Socket accepts the packet and fragments it to comply with the 1500-byte limit
- If the DF bit is set, the Socket drops the packet and sends an ICMP Fragmentation Needed message back to the sender

## MTU Behavior with Multiple Active WAN Links

For Socket sites that are deployed with multiple active WAN links:

- Downstream (PoP to Socket): The PoP checks the maximum packet size that can pass through without fragmentation per WAN link. The lowest MTU discovered is applied across all downstream tunnels.

For example, if a site has two WAN links with discovered MTUs of 1450 bytes and 1383 bytes, the downstream MTU used will be 1383 bytes to ensure consistent delivery across all links.
- Upstream (Socket to PoP): The Socket calculates MTU per active link. The smallest MTU among active links becomes the effective MTU for the upstream tunnel.

**Note:** Passive WAN links do not influence the MTU used for active tunnels.

## Off-Cloud Traffic

Off-Cloud tunnels (site-to-site) use a separate MTU calculation, accounting for a 106-byte overhead. These tunnels periodically run their own MTU discovery independent of the Socket-to-PoP path.

## Configuring the MTU for a Specific Socket Site

Use the Socket WebUI to configure the MTU for a Socket site. The Socket must reconnect to the PoP for the changes to take effect, which can interrupt all traffic flows.

**To configure the MTU for a Socket site:**

1. Log in to the Socket WebUI for the site (see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui)).
2. Go to the **Network Settings** tab and enter the MTU for each WAN link.

![Socket_MTU.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29899340557085(1).png)
3. Click **Update**. The Socket reconnects to the PoP and the MTU is updated.

**Notes:**

- PMTUD packets can trigger apparent packet loss, particularly on passive links with minimal traffic.
- Starting in Socket version 23.0.19445, PMTUD packets are excluded from packet loss metrics.
- It's possible to set the MTU that is automatically applied to all Socket sites. When you use this automatic MTU configuration, you CANNOT configure the MTU for a specific site.

For more information about setting the MTU for all Socket sites, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
