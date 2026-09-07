---
title: "Why Do Routes to IPsec Sites Still Exist in Socket Even Though IPsec Tunnels Are Down?"
slug: "why-do-routes-to-ipsec-sites-still-exist-in-socket-even-though-ipsec-tunnels-are"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/why-do-routes-to-ipsec-sites-still-exist-in-socket-even-though-ipsec-tunnels-are"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Why Do Routes to IPsec Sites Still Exist in Socket Even Though IPsec Tunnels Are Down?

## Question

Why Do Routes to IPsec Sites Still Exist in Socket Even Though IPsec Tunnels Are Down?

For example, an IPsec site was configured with a native range of 10.80.80.0/24

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20437774709917.png) This site is currently down.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20437789309853.png) In the CMA, under Monitoring > Routing Table, we do not see the 10.80.80.0/24 network

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20437789312285.png) However, in the Socket UI, it still shows the route:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20437774719517.png)

## Answer

Sockets may be tested for reachability, with their ranges normally present in the routing tables of other Sockets only if they are reachable. Otherwise, these ranges are grayed out on the monitoring page of the Socket's UI. These pingable ranges are of the type REMOTE_SITE, and reachability is tested by pings that the Sockets send to each other.

In contrast, IPsec sites cannot be "pinged"; therefore, Sockets consider these remote IPsec sites to be always connected, and their static ranges are always reachable. These are seen as REMOTE_RANGE. This is a known limitation, as the reachability of static REMOTE_RANGEs cannot be probed.

## Case Study

This will be an issue if the customer has the following design:

The IPsec site has a subnet of 10.10.10.0/24, and the Socket site has a BGP LAN subnet of the 10.10.0.0/16 network. The intention is that when the IPsec tunnel is down, traffic destined for 10.10.0.0/16 should be routed through the Socket site. However, this is not feasible. Since the Socket route table still has the 10.10.10.0/24 route through the IPsec site (even though the IPsec tunnel is down), the Socket will drop the packet.

**Workaround**:

1. Publish the range 10.10.10.0/24 dynamically via the BGP
2. OR, use a native range on the IPsec site that doesn't overlap with the network range of another site
