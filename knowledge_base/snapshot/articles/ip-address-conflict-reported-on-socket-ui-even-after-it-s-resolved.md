---
title: "IP Address Conflict Reported on Socket UI Even After It's Resolved"
slug: "ip-address-conflict-reported-on-socket-ui-even-after-it-s-resolved"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/ip-address-conflict-reported-on-socket-ui-even-after-it-s-resolved"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IP Address Conflict Reported on Socket UI Even After It's Resolved

## Issue

The Socket is able to detect IP conflicts with its configured interface IP addresses. An IP conflict exists when two devices on the same network are assigned the same IP address. For instance, if the Socket's WAN1 interface is assigned the 192.168.50.193 IP address, and another device on the WAN is also assigned with the same IP address, you'll see an error like the one below on the Monitor page of the Socket UI:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/14850578971293.png)

In order to correct the IP conflict, you can either change the Socket's interface IP address, or change the IP address of the conflicting device. The MAC address of the conflicting device is also shown in the error message above and you could check on your switch and/or router to identify it.

## Troubleshooting

- If possible, change the IP address on the conflicting device on the network. Once changed, no further steps are required.
- If the issue continues, an unfiltered packet capture can be taken on the interface of the Socket reporting the IP conflict. You may only be able to run the PCAP for a few seconds depending on how much traffic is passing through the interface. Refer to [How-to-Capture-Traffic-on-a-Socket](/v1/docs/how-to-capture-traffic-on-a-socket) for instructions on how to capture traffic on a socket. In the PCAP, look for ARPs for the Socket interface's IP address that are coming from a non-Cato MAC. This tells you that the IP conflict still exists.

## Solution

1. **Change the IP address of the conflicting device** As the IP address remains unchanged on the Socket, the IP conflict warning will continue to be displayed for a 24 hours period, starting from when the conflict was first detected. In this case, the warning can be safely ignored, and it will disappear after 24 hours.
2. **Change the IP address of the Socket** The warning message will disappear once the conflicting IP address on the socket is changed.
