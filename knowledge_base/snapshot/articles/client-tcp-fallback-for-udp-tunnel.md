---
title: "Client TCP Fallback for UDP Tunnel"
slug: "client-tcp-fallback-for-udp-tunnel"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/client-tcp-fallback-for-udp-tunnel"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Client TCP Fallback for UDP Tunnel

The default behavior for the Cato Client is to connect to the PoP with a UDP tunnel using port 443. However, there are times where this UDP port is blocked (such as airports and hotels), and as a result the Cato Client can't connect to the Cato Cloud. When UDP port 443 is blocked, the Cato Client automatically falls back to TCP traffic and attempts to connect to the PoP with a TCP tunnel using port 443. The Client continues to use TCP traffic and doesn't return to UDP during the session. If you disconnect the Client from the network and then reconnect it later, the Client tries to connect to the PoP with a UDP tunnel.

To force all Client traffic to only use TCP traffic, please contact Support.

**Notes:**

- There are certain regions, such as Egypt, that restrict or censor VPN-like traffic, and may block Client tunnels forming via UDP (port 443 and then 1337).
- TCP is provided as a last resort attempt to connect to the PoP
- TCP connectivity can cause a slower throughput due to TCP overhead, and is susceptible to slowdown in the event of last-mile packet loss
