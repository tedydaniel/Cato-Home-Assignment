---
title: "Socket HA Status Troubleshooting"
slug: "socket-ha-status-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-ha-status-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket HA Status Troubleshooting

## Overview

High availability offers redundancy in the case of a critical outage in a socket device. A site must be able to successfully transition between socket devices in these instances to ensure business continuity is maintained. This playbook looks to guide troubleshooting this scenario.

## Symptoms

Unreadiness in socket HA status can manifest in several ways. An administrator may note the following symptoms:

- One of the HA pair member sockets is offline.
- HA status not ready due to 'Keepalive'.
- HA status not ready due to 'Compatible Version'.

## Possible Causes

- One of the HA pair has connectivity issues with Cato.
- Sockets lack LAN side connectivity to each other
- Firmware differences between sockets

## Troubleshooting the Issue

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

### Troubleshooting Socket HA Member Offline

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18463039098269.png)

Please follow our [Socket Connectivity Troubleshooting Playbook](/v1/docs/socket-site-tunnel-connectivity-troubleshooting).

### Troubleshooting HA Status Not Ready Due to 'Keepalive'

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18463338443677.png)

#### LAN Interface Status

VRRP messages, the mechanism for maintaining HA status between an HA pair, require a network path between the LAN interfaces of each member. Ensure that a LAN port is up and available for VRRP messages.

Check for any recent changes in the switch or LAN side configuration, like VLAN config or changes in the physical cabling. Ensure your configuration follows the best practices for Socket HA described in [What is Socket High Availability (HA)](/v1/docs/what-is-socket-ha).

#### VRRP Frame Transmission and Receipt

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18547121690781.png)

Run a packet capture on the LAN Interface of both sockets, following the procedure listed in H[ow to Take a Packet Capture on a Socket,](/v1/docs/how-to-capture-traffic-on-a-socket) and check if the master Socket is sending VRRP keepalive messages to the standby Socket.

For the socket HA status to be ready, both of the following conditions must be true:

- Primary socket must be sending VRRP messages
- Secondary socket must be receiving those VRRP messages

If the primary socket is sending these messages but the secondary is not receiving them, investigate your local network infrastructure to identify if something is preventing them from reaching the secondary socket.

### Troubleshooting HA Status Not Ready Due to 'Compatible Version'

If this occurred due to a firmware upgrade failure, please see the process for **Tunnel established after the upgrade failure** in the [Troubleshooting Socket Upgrade Failure Playbook.](https://support.catonetworks.com/hc/en-us/articles/16407852770333/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MTY0MDc4NTI3NzAzMzMsImV4cCI6MTcxNDEzMTQxN30.y2zsoArl91B6YO2RS_JloCBlPKVPlfCXAiJwCS_kNSA#h_01HFN8Z62Q8TZY3JRJYKS1PF9E)

Navigate to [Resolving Incompatible Versions](/v1/docs/socket-ha-status-troubleshooting#resolving-incompatible-versions).

## Resolving Discovered Issues

### Resolving Incompatible Versions

A momentary connectivity issue may have caused an upgrade failure and could succeed the second time. To attempt a new Socket upgrade, manually initiate the upgrade from Site Configuration > Socket > Actions > Upgrade.

Ensure that the target version will lead to both sockets in the HA pair having the same version. This tool can only upgrade and not downgrade the firmware version. 17 minutes after the manual firmware upgrade starts, CMA will show an "upgraded successfully" notification indicating that the Socket reported a successful upgrade after the grace period. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18466028900381.png)

If this upgrade also fails, utilise the [Troubleshooting Socket Upgrade Failure Playbook.](/v1/docs/socket-upgrade-failure-troubleshooting)

## Raising cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken throughout the use of this playbook. Including, for example:

- Confirmation of any manual upgrades that have taken place, including timestamps.
- Confirmation of transmission and receipt of VRRP messages.
