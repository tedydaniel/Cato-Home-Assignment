---
title: "Cato Reserved BGP Communities"
slug: "cato-reserved-bgp-communities"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-reserved-bgp-communities"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Reserved BGP Communities

This article discusses how to use Cato reserved BGP communities.

## Overview

Cato provides a list of reserved BGP communities with hard-coded behavior for handling and processing incoming BGP prefixes from the neighboring routing devices. When Cato receives a BGP prefix marked with a reserved community, it will handle it according to the section below, [Cato's Reserved BGP Communities](/v1/docs/cato-reserved-bgp-communities#catos-reserved-bgp-communities).

This is the structure for Cato reserved communities: **Cato peer ASN:<reserved value>**. For example, a Socket site with a BGP neighbor that we want to apply the Socket isolated routing reserved community:

- Cato ASN is 65001
- LAN switch is defined with Cato Peer ASN is 65002
- To keep routes local on the Socket, add the following BGP community to the Cato Peer BGP process: **65001:32768**. This is based on the reserved value 32768 (see table below).

For example, for Cisco routers, the command would be `set community 65001:32768`, and you need to specify the Cato ASN.

For more about defining the Cato peer ASN, see [Configuring BGP Neighbors for a Cato Socket](/v1/docs/configuring-bgp-neighbors-for-a-cato-socket).

**IMPORTANT:** If you use a Cato reserved BGP community, make sure to configure BGP filtering on the BGP routers to prevent advertising the [Cato system range](/v1/docs/working-with-the-cato-system-range) to the Sockets. Otherwise, there can be significant connectivity issues with the impacted Sockets.

## Cato's Reserved BGP Communities

The following table describes the reserved BGP communities and their functionality.

| Name | BGP Community | Applies To | Description |
| --- | --- | --- | --- |
| Socket isolated routing | <Cato ASN>:32768 | Socket sites with Socket v15 or higher | - The Socket installs the received BGP prefixes tagged with the reserved community in the routing table - The Socket doesn't propagate these prefixes to the PoP - For routing decisions, the Socket prefers BGP routes tagged with the reserved community over routes received from the PoP in the Cato Cloud - Sample use case - route all the WAN traffic over the Alt WAN network, and only the Internet and SDP user traffic is sent over the Cato Cloud |
