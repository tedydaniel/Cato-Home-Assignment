---
title: "Configuring Sites with Cato Sockets"
slug: "configuring-sites-with-cato-sockets"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/configuring-sites-with-cato-sockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Sites with Cato Sockets

## Overview

Sites that use Cato Sockets to connect to the Cato Cloud support all the networking and QoS features to help you manage network traffic. The X1500 Socket is a tabletop appliance designed for branch offices and has four ports (two WAN ports and two LAN). The X1600 Socket is for mid-size sites with eight ports and also includes an LTE model. The X1700 Socket is a 1U appliance that is mounted in a server rack. It is designed for data centers and corporate headquarters. It has eight ports, and an expansion slot for additional copper or fiber optic ports. In addition, the X1700 Socket has two replaceable hard disk drives.

## Configuring Primary and Secondary Connections

Sockets support connections to multiple ISPs to provide redundancy and failover functionality. The WAN ports send traffic from the internal LAN network, to other WAN locations or the external Internet. The default active/passive configuration for a Socket is that the primary connection has the highest precedence and is the active connection. The other connection has a secondary precedence and is the passive connection. Some of the additional Socket configurations are:

- Active/Active - Both connections are set to primary precedence and send WAN traffic at the same time.
- 4G/LTE cellular connection - The X1600 LTE Sockets provide built-in cellular support, and for other Socket models you can connect cellular modems to the Socket that are used for WAN traffic. Since cellular connections are often quite expensive, the site is configured to only use this connection in an extreme situation.

When you are creating a site, the **Enable WAN2** option lets you configure the settings for the bandwidth secondary connection. Later, you can use the Site Configuration > Socket page to change or update the settings.

## Controlling the Bandwidth for a Site

You can use the Cato Management Application to control the maximum upstream and downstream bandwidth from the Cato Cloud to each site.

Configure the bandwidth setting according to the terms of the Cato site license. For example, if the site license is for 100Mbps, configure each link (upstream and downstream) as 100Mbps. If the Cato site license has a higher bandwidth value than the ISP link bandwidth, set each link’s bandwidth according to the ISP bandwidth.

You can set values as whole numbers or include up to one decimal.

You can configure the settings in Network > *<site>* > Site Configuration > Socket.

## Configuring the Native Range

The native range for a site is the IPv4 address (and CIDR) for the primary LAN network that is behind the Socket.

You can configure the native range settings in Network > *<site>* > Site Configuration > Networks. You can also use this section to configure additional network ranges for the site.

You can optionally tag the native range per LAN interface with a VLAN ID (802.Q). It is considered a best practice to only have tagged networks within your sites. You can either add the tag while creating a site or add it for existing sites.

![vlan-nativeRange-tag.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275594045597.png)
