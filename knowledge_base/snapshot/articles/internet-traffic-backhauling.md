---
title: "Configuring Internet Traffic Backhauling"
slug: "configuring-internet-traffic-backhauling"
updated: 2026-07-07T06:58:02Z
published: 2026-07-07T06:58:02Z
canonical: "knowledge.catonetworks.com/configuring-internet-traffic-backhauling"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Internet Traffic Backhauling

This article explains how to configure a site as a backhauling gateway and create network rules to route traffic to that site.

## Overview of Internet Traffic Backhauling

By default, Cato egresses Internet traffic from a PoP in the Cato Cloud. In some scenarios, customers want to backhaul the Internet traffic via a specific site to be processed an on-premise appliance or egressed with the site's local ISP public IP.

Cato's Internet traffic backhauling lets you designate these sites as gateways for the Internet traffic and use network rules to backhaul the relevant traffic to these sites.

After you define the backhauling gateway sites, create Internet network rules to backhaul the relevant traffic to the gateway sites. You can use the full functionality of network rules which provide granularity to route traffic according to your specific needs. For example, you can create a network rule that backhauls traffic for a specific application and for specific users to a gateway site.

Any type of site or SDP user can be defined in a network rule as the source of the backhaul Internet traffic.

For redundancy, you can also define additional backup sites as backhauling gateways. In this case, if the primary gateway site is unavailable, then the traffic is routed to the backup site according to the order of the gateway sites in the network rule.

If all the gateway sites are disconnected from the Cato Cloud, then the traffic is egressed from the Cato Cloud directly to the Internet.

> [!NOTE]
> Note:
> 
> Cato supports passive FTP for backhauling, active FTP is not supported.

### Internet Traffic Backhauling Options

These are the backhauling options that Cato supports:

- **Backhauling Internet traffic to a LAN device behind a Socket** - You can use this option if you need to inspect some of the Internet traffic using an on-premise appliance.
  - For more information, see [Backhauling Traffic to a LAN Device behind a Socket](/v1/docs/backhauling-traffic-to-a-lan-device-behind-a-socket)
- **Backhauling via a Socket's WAN IP address** - You can use this option if you need to egress some of the Internet applications via a public IP used by a Socket. For example, accessing a SaaS application that has already allowlisted this public IP.
  - Supported from Socket v16.0 and higher
  - For more information, see [Backhauling Traffic via a Socket's WAN Interface IP Address](/v1/docs/backhauling-traffic-via-a-socket-s-wan-interface-ip-address)
- **Hairpinning traffic to the same Socket site** - You can use this option if you need to send Internet traffic from the Socket site to the PoP (for the Cato Security services) and then back to the same site for further processing.
  - Supported from Socket v16.0 and higher
  - For more information, see [Hairpinning Traffic to the Same Site](/v1/docs/hairpinning-traffic-to-the-same-site)
- **Backhauling via IPsec sites** - You can use this option if you need to egress Internet traffic to a third-party cloud/proxy based security service (such as a Secure Web Gateway).
  - For more information, see [Backhauling Traffic via an IPsec Site](/v1/docs/backhauling-traffic-via-an-ipsec-site)

### Sample Backhauling Configurations

This is a sample backhauling configuration using a Socket site to backhaul traffic to a LAN device (firewall appliance, and using an IPsec site to backhaul traffic to a Secure Web Gateway.

![Backhauling_Socket_IPsec.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247907841949.png)

## Configuring Internet Backhauling for the Account

This section shows the overview of configuring your account to backhaul Internet traffic to a gateway site.

1. Define one or more backhauling gateway sites.
2. Create Internet network rules that backhaul Internet traffic to the gateway sites.

## Sample Networking Rules for Internet Backhauling

This section shows sample configurations of granular network rules for Internet backhauling (rules #8 - 10 within the Network Rules policy).

For more information about routing options, you can also [watch this video tutorial](https://academy.catonetworks.com/routing-options-in-the-cato-cloud).

![Backhauling_Network_Rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247914916893.png)

- Network rule #8 (Bloomberg-app-Backhaul) is an example of a network rule that backhauls specific Internet application traffic for an SDP user, as follows:
  - The **Source** of the Internet traffic is the SDP user **Sample Admin**
  - The matching traffic is for the **Bloomberg Professional** application (defined as the **App/Category** for the rule).
  - The traffic is assigned the **Bandwidth** priority **P20**.
  - The traffic is backhauled via the primary gateway site **BERLIN-DC2**. If the primary gateway site is unreachable, then the traffic is backhauled via the secondary gateway site **MILAN** (defined as the **Routing** for the rule).
- Network rule #9 (US-Backhaul) is an example of regional backhauling. This rule backhauls the HTTP(S) traffic from a group of sites to the gateway sites as follows:
  - The **Source** of the Internet traffic is the group **US** and the members of this group are sites located in the United States.
  - The matching traffic is all HTTP and HTTPS traffic (defined as the **App/Category** for the rule)
  - The traffic is assigned the **Bandwidth** priority **P30**.
  - The traffic is backhauled via the primary gateway site **NYC-DC1**. If the primary gateway site is unreachable, then the traffic is backhauled via the secondary gateway site **BOSTON-DC2** (defined as the **Routing** for the rule).
- Network rule #10 is similar to rule #9 above, and it backhauls traffic for a group of sites in the EMEA region.
- You can create network rules for any combination of source sites, SDP users, groups for the **Source** of the rule. In addition, you can use **Any** for the **App/Category** to backhaul all Internet traffic.
- For network rules that use the **Backhaul via** option, you can use a combination of Socket and IPsec backhauling gateway sites in a single rule.
