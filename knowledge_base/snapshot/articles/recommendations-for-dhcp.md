---
title: "Recommendations for DHCP"
slug: "recommendations-for-dhcp"
tags: ["Best Practices", "Networking"]
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/recommendations-for-dhcp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recommendations for DHCP

## Overview

You can use the Cato DHCP service to assign IP addresses for your clients. The Cato PoPs are responsible for providing the IP addresses to the clients. Cato’s DHCP service works only for hosts that are connected to the Cato Cloud and only if you configure a DHCP range for the network.

Starting with Socket v21, the PoP saves the DHCP data, so hosts can retain their IP addresses after temporary disconnections. When the Socket reconnects to the PoP, the host receives the same IP address it had before the disconnection, helping prevent conflicts and reducing downtime. The Socket also stores the reserved host table locally to prevent reserved IP addresses from being assigned to non-reserved hosts while the tunnel is down.

For more about Cato DHCP, see [Configuring DHCP Settings](/v1/docs/configuring-dhcp-settings).

## Best Practice for DHCP

This section contains best practices and recommendations for configuring DHCP with Cato.

### Using Cato’s DHCP Servers for Global Coverage

We highly recommend that you use Cato’s DHCP service for your account. The advantage of working with Cato’s DHCP service is that it gives you global coverage, and you are not dependent on the WAN connectivity. It means that Cato’s DHCP server assigns an IP address to any host in your network regardless of its location, and you don’t have to maintain the connectivity from the hosts to an internal DHCP server. Cato PoP global coverage lets hosts communicate anywhere as long as they are connected to the Cato Cloud.

Cato also lets you configure a DHCP Relay and add your internal DHCP server for your account (**Network > DHCP > DHCP Relay Settings**). However, we recommend that you use Cato's DHCP server to improve the performance of your network. For example, if you have a site in New York and a site in Singapore, and your internal DHCP server is located in New York, any DHCP requests coming from the Singapore site go to the server in New York for resolving.
