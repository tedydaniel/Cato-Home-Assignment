---
title: "DHCP Doesn't Work With Subnet Source Bypass"
slug: "cato-dhcp-dhcp-doesn-t-work-with-subnet-source-bypass"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/cato-dhcp-dhcp-doesn-t-work-with-subnet-source-bypass"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# DHCP Doesn't Work With Subnet Source Bypass

## Problem

When using Cato as a DHCP server for one of your networks, clients are unable to obtain an IP address when the entire network is added to the site's Local Bypass configuration.

For example, consider the configuration below.

VLAN 2 is configured with a DHCP Range of 172.17.4.10-172.17.4.50. The Gateway IP is 172.17.4.1

![360000269365-mceclip5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247990970653.png)

A Local Bypass entry exists for all of VLAN 2, 172.17.4.0/24.

![360000269325-mceclip2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247974219549.png)

With this configuration, all clients on VLAN 2 are not allocated an IP address through Cato DHCP.

The Socket uses the Gateway IP address as the source to relay DHCP requests to Cato for IP allocation (the Socket itself does not act as a DHCP server). These requests must be sent through the tunnel, but since the Socket's Gateway IP address falls within the bypass range, the DHCP requests get sent out the WAN interface instead.

## Solution

Configure the Source Bypass to exempt the Socket's Gateway IP address. In the example above, instead of entering the subnet using CIDR notation, 172.17.4.2-172.17.4.255 can be used, a range that does not include the Gateway IP, 172.17.4.1.

![360000274809-mceclip4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247950782493.png)
