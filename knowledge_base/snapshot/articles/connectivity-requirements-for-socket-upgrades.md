---
title: "Connectivity Requirements for Socket Upgrades"
slug: "connectivity-requirements-for-socket-upgrades"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/connectivity-requirements-for-socket-upgrades"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectivity Requirements for Socket Upgrades

The Socket upgrade process requires connectivity with specific Socket ports to the Cato Cloud to correctly update to new Socket versions. Otherwise, the new version doesn't install correctly and the Socket rolls back to an earlier version.

There are different connectivity requirements for an initial upgrade for factory reset or newly registered Sockets and for gradual upgrades (regular Socket upgrades during a maintenance window).

- HTTPS traffic from the Socket's WAN IP address must be excluded from SSL/TLS inspection performed by a device in the upstream direction (otherwise the upgrade process fails)

This means that you can't have a site configuration where a Socket is located behind another Socket
- For initial upgrades, connect the following ports to the Cato Cloud:
  - X1500 – WAN1 or Port 3 (WAN)
  - X1600 – Port 1
  - X1700 – Port 1

> [!NOTE]
> Important:
> 
> If you have an add-on card, make sure that you do the following before connecting the card:
> 
> 1. Ensure that you have connectivity to the Cato Cloud via Port 1 and only then, power off your Socket.
> 2. Connect the add-on card.
> 3. Power on your Socket.
- For gradual/scheduled Socket upgrades, connect the following ports to the Cato Cloud:
  - X1500 – Any WAN port (for Socket versions 14.0 and higher)
    - For Socket versions 13.x and lower, WAN1 or port 3 (WAN) must be connected
  - X1600 – Any WAN port
  - X1700 – Port 1 or Port 9 (available with the add-on card)
