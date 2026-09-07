---
title: "Enabling mDNS Between Subnets"
slug: "enabling-mdns-between-subnets"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/enabling-mdns-between-subnets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enabling mDNS Between Subnets

This article explains how to configure mDNS for your Cato account.

## Overview

mDNS is a protocol for name resolution without having to configure a DNS server. It enables hosts to communicate with each other in your network within the same VLAN seamlessly. mDNS uses multicast packets to allow discovery of the different hosts in the network. This lets you use a variety of mDNS-based services, such as an office printer or a monitor in a meeting room to share your screen.

![mDNS-sameSubnet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247948920605.png)

For example, if you have a host within VLAN 10 that it needs to discover the printers in the VLAN, the host sends out mDNS requests and receives responses from all endpoints providing these services in the VLAN (within the broadcast domain). Since the devices are in the same VLAN, the communication happens directly without involving the Socket.

![mDNS-differentSubnet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247996759581.png)

However, if you are part of VLAN 10 and your printer is part of VLAN 20, you do not have direct access to the printer since it's in a separate subnet. To enable your computer to communicate with the printer in VLAN 20, you must enable the Socket to function as an mDNS gateway. That lets you to send multicast requests from VLAN 10 and receive responses from devices offering services within VLAN 20.

> [!NOTE]
> Note:
> 
> Since multicast traffic is noisy, and considered not secure, Cato recommends that you only enable mDNS traffic for subnets that require it.

## Configuring mDNS for Between Subnets

For communication between the different subnets to work, you need to enable mDNS for the relevant VLANs in the site's network configuration

> [!NOTE]
> Note:
> 
> mDNS must be enabled on all VLAN segments that you need to communicate with each other.

### Enabling mDNS on your VLANs

![mDNS-VLAN.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247966209437.png)

**To enable mDNS on a VLAN:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the site menu, click **Networks**.
3. Click **New** or edit an existing IP range.
4. Under **Additional Settings**, select **mDNS Gateway**.
5. Click **Apply**.

### Allowing Unicast Traffic

After enabling mDNS for your various subnets, you must configure a rule to allow the traffic in the LAN Firewall. For more information, see [Configuring the Socket LAN Firewall Policy](/v1/docs/configuring-the-socket-lan-firewall-policy).
