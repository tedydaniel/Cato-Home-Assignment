---
title: "Socket High Availability Failover Fails Due To Meraki Switch GARP Limitation"
slug: "socket-high-availability-failover-fails-due-to-meraki-switch-garp-limitation"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/socket-high-availability-failover-fails-due-to-meraki-switch-garp-limitation"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket High Availability Failover Fails Due To Meraki Switch GARP Limitation

## Issue

In instances where a Socket HA pair performs an HA failover, the newly designated master Socket sends a gratuitous ARP broadcast and then starts to respond to ARP broadcast requests for the Site's LAN IP address. For more information see [Understanding Socket High Availability and Failover](/v1/docs/what-is-socket-ha).

However, in scenarios where a Meraki switch interconnects the two Sockets, the HA failover process may fail and the switch will wrongly forward all frames to the slave Socket, resulting in an outage.

## Environment

This issue pertains specifically to Socket HA pairs interconnected through a Meraki switch. The proposed solution is applicable to Socket version 13 and above.

## Troubleshooting

- In adherence to [RFC2338](https://www.ietf.org/rfc/rfc2338.html), the socket will send out a Gratuitous ARP REQUEST packet during HA failover. This behavior can be validated in a packet capture which will show the following flag: **opcode = 1** ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13934381194269.png)
- Meraki support has confirmed their system's behavior of disregarding GARP requests with opcode = 1, consequently failing to update the switch's CAM table.

## Solution

Starting with Socket version 13, a backend configuration can be [requested to Support](/v1/docs/submitting-a-support-ticket) to change the opcode flag in the gratuitous ARP packet, effectively mitigating the issue related to Meraki switches.

***Note:*** *This configuration should only be applied to sites with Meraki switches and not at the account level.*

The recommended backend configuration changes the opcode in the GARP packet to 2, denoting a REPLY, thereby ensuring successful updating of the switch's CAM table.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13934482796701.png)
