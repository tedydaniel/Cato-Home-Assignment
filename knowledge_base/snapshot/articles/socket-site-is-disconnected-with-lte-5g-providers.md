---
title: "Socket Site is Disconnected with LTE/5G Providers"
slug: "socket-site-is-disconnected-with-lte-5g-providers"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/socket-site-is-disconnected-with-lte-5g-providers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Site is Disconnected with LTE/5G Providers

## Issue

The Socket fails to establish a DTLS tunnel to the Cato Cloud when connected to LTE/5G providers such as AT&T Mobility, despite having active internet access through the ISP.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20256102732957.png)

## Environment

- Physical Socket
- LTE/5G Provider

## Troubleshooting

- Refer to [Socket Site Tunnel Connectivity Troubleshooting](/v1/docs/socket-site-tunnel-connectivity-troubleshooting) to gather detailed connectivity information and PCAP captures from the Socket WebUI.
- Verify that the Socket can successfully ping well-known public IP addresses (e.g., 8.8.8.8) via the WAN port.
- Ensure that there is bidirectional DTLS traffic over port UDP/443 on the WAN connection. This can be checked in the PCAP capture obtained in the first step. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20256086775453.png)
- Further, analyze the PCAP capture for any signs of interference from the ISP during the DTLS handshake. Look for carrier-specific data (e.g., APN information) within the packet payload. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20256086776349.png)

## Solution

Some LTE/5G providers might interfere with DTLS connections on port UDP/443. To resolve this issue, change the DTLS port to UDP/1337 via the Socket WebUI as explained in [Setting a Different Port to Connect to the Cato PoP](/v1/docs/setting-a-different-port-to-connect-to-the-cato-pop)
