---
title: "Link Aggregation (LAG) Link Experiencing High Latency and Packet Loss"
slug: "link-aggregation-lag-link-experiencing-high-latency-and-packet-loss"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/link-aggregation-lag-link-experiencing-high-latency-and-packet-loss"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Link Aggregation (LAG) Link Experiencing High Latency and Packet Loss

## Issue

A Socket deployment using Link Aggregation (LAG) with an internal switch may experience high latency and packet loss if the link isn't configured correctly. This issue may be more visible with applications sensitive to latency variations.

## Environment

- Cato LAG implementation.
- Internal switch not supporting Static LAG or LAG isn't configured.

## Troubleshooting

In LAG implementations, Cato only supports Static LAG as explained in [Configuring Link Aggregation for a Socket](/v1/docs/configuring-link-aggregation-for-a-socket). LACP is currently not supported.

A LAG misconfiguration can be identified by running the following steps:

**Note:** [Network Analytics](/v1/docs/showing-the-site-network-analytics) will not show latency/packet loss caused by LAG misconfigurations.

1. Run a ping test from a device on the LAN to the Socket's LAN IP address. The Socket's IP address is the 'Local IP' of the Native range configured in the Socket's networks page. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15402000615069.png)
2. Optionally, the ping test can be run from the Socket's [WebUI](/v1/docs/using-the-socket-webui-tools) routing it via the LAN to the switch IP or a host behind the switch.
3. If the ping test shows intermittent high latency and/or packet loss, the LAG link may be misconfigured. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15402000640413.png)
4. Confirm that both the Cato Socket and the internal switch include the same number of LAG members and the correct ports. All LAG members must be in UP state.
5. Confirm that the switch has the LAG feature configured as static LAG. Active or passive LACP isn't supported when connecting to the Cato Socket.

## Solution

If the switch connected to the Cato Socket supports Link Aggregation, configure LAG in static mode.

If static LAG isn't supported by the switch (e.g. only LACP is supported), then remove LAG configurations from both the switch and the Socket. In this scenario, only one port can be configured for the LAN.
