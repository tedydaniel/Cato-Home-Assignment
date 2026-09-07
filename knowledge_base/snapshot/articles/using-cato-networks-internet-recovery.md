---
title: "Using Cato Networks' Internet Recovery"
slug: "using-cato-networks-internet-recovery"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/using-cato-networks-internet-recovery"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Cato Networks' Internet Recovery

## Overview of Recovering Internet Traffic

In the rare case that a site loses connectivity to the Cato Cloud, the Internet Recovery feature helps you easily restore traffic directly to and from the Internet. Internet Recovery is part of the Socket’s recovery features that prioritize connectivity and minimize disruption to traffic flows.

Internet Recovery is enabled by default and you can use the Cato Management Application to disable it for a specific site or for the entire account.

## How Does Internet Recovery Work?

This section describes when the Socket activates Internet Recovery to connect directly to the Internet and then resumes sending the traffic over the Cato Cloud.

### Activating Internet Recovery

If the tunnel between the Socket and the PoP (Cato Cloud) is disconnected, the Socket immediately moves to Internet Recovery mode. The tunnel is considered disconnected if there is 100% packet loss, or the Socket stops receiving responses to 3 consecutive keep alive messages.

First the Socket randomly selects a link and designates it for Internet Recovery. Then the Socket transfers the Internet traffic directly to the Internet (the local ISP). Because the traffic bypasses the Cato Cloud, the Cato security protections, such as firewall and IPS, are not applied.

**Note:** Internet Recovery doesn't modify WAN traffic between your sites. To recover WAN traffic if a site can't connect to the Cato Cloud, enable the WAN Recovery feature. For more information, see [Socket Site Resiliency with WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery).

If the Socket temporarily disconnects from the Cato Cloud, for example it identifies a better transport or PoP, Internet Recovery lets users continue to access the Internet.

For sites with Socket High-Availability (HA) and Internet recovery feature enabled, when there are connectivity issues with the Cato Cloud, first the Socket HA is activated. The primary Socket fails over to the secondary Socket. And, if there are still connectivity issues with the Cato Cloud, then the Internet recovery is activated on the secondary Socket.

### Restoring Traffic to the Cato Cloud

The Socket keeps trying to connect to the Cato Cloud and when the Socket receives responses to the keep alive messages, it identifies that the link with the Cato Cloud is restored. The Socket then immediately routes the traffic over the Cato Cloud.

In some cases, the tunnel can repeatedly disconnect in short intervals, then Cato uses a back-off algorithm to prevent flapping between trying to connect to Cato Cloud or to the local ISP (Internet Recovery).

The first time that the connection with the PoP is recovered, the Socket immediately creates a tunnel to the Cato Cloud. If there is another Socket disconnect within the next 1024 seconds (~17 min), the Socket waits 8 seconds before restoring connectivity to the Cato Cloud (when the connection recovers). In the next times the Socket disconnects, it waits for 16 seconds, 32 seconds and so on until the maximum of 1024 seconds. Once the Socket tunnel is connected to the Cato Cloud for more than 1024 seconds, then the Socket is considered stable. Then the back-off delay resets to waiting for 8 seconds.
