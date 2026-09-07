---
title: "How to Reduce the Citrix Recovery Time"
slug: "how-to-reduce-the-citrix-recovery-time"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/how-to-reduce-the-citrix-recovery-time"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Reduce the Citrix Recovery Time

**How can I reduce the Citrix client application reconnection time after a Socket HA failover?**

For two Cato Sockets in High-Availability (HA) mode that provide redundancy, during a failover, all the connections move from the primary Socket to the secondary Socket. Some applications can reconnect very quickly and for others, like the Citrix client, it can take longer.

To reduce the recovery time of the Citrix client, we recommend that you disable the **TCP Acceleration** and **Packet Loss Mitigation** features in Cato’s Network Policy for the Citrix client.

Note that the Citrix protocol is already optimized, so removing the Cato TCP acceleration isn’t affecting the end user experience.

For more about TCP acceleration and packet loss mitigation, see [Accelerating and Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic).
