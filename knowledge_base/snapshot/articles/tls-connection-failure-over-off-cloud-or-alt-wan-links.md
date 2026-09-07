---
title: "TLS Connection Failure Over Off-Cloud or Alt-WAN Links"
slug: "tls-connection-failure-over-off-cloud-or-alt-wan-links"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/tls-connection-failure-over-off-cloud-or-alt-wan-links"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TLS Connection Failure Over Off-Cloud or Alt-WAN Links

## Issue

A TLS connection may fail when going over an Off-Cloud or Alt-WAN link between two sites behind Cato Sockets.

## Environment

- TLS connection between two Cato sites.
- TLS Inspection is Enabled
- The network rule that the traffic hits is below a complex rule (more information below)

## Troubleshooting

- TCP Proxy will be enforced when a complex network rule exists above the simple Off-Cloud or Alt-WAN network rule as explained in [Working with Complex Network Rules](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices)
- Below is an example of a scenario where a simple off-cloud rule is placed below a complex rule. The rule is complex because it contains a defined Application.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12132709416349.png)
- In this scenario, the Socket can’t evaluate the network rule on the SYN packet and sends it to the PoP. The TCP proxy completes the TCP handshake on the client side (Site A) only, as shown in the diagram below.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23122317546013.png)
- The network profile is decided on the Site A Socket, and it switches to the off-cloud transport. Following this, the SSL handshake is initiated, and Socket A sends the Client Hello over the off-cloud.
- The Client Hello arrives at the server, but the server hasn’t even completed the TCP handshake with the client. As a result, the server sent a RESET to the client, terminating the connection.
- The above behavior can be seen from the server side by running a packet capture. [See How to Capture Traffic on a Socket](/v1/docs/how-to-capture-traffic-on-a-socket)

## Solution

As mentioned in [Working with Off-Cloud Traffic](/v1/docs/routing-traffic-to-an-off-cloud-link), the solution is to move the simple Off-Cloud or Alt-WAN rule above any complex rules. When doing this, the sockets are able to evaluate the network rule and route packets over Off Cloud or Alt-WAN immediately.

The PoP and the TCP proxy are eliminated from the path in both directions. Packets are sent directly between both Sockets.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12132766988445.png)

Alternatively, while not recommended, disabling TLS inspection at the account level can resolve the issue as it will disable TCP proxy enforcement.
