---
title: "Why Do Primary and Secondary Sockets Reconnect at the Same Time?"
slug: "why-do-primary-and-secondary-sockets-reconnect-at-the-same-time"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/why-do-primary-and-secondary-sockets-reconnect-at-the-same-time"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Why Do Primary and Secondary Sockets Reconnect at the Same Time?

## Question

In a high-availability (HA) socket deployment, we may observe instances where both the primary and secondary sockets undergo reconnection, as depicted in the following events:

![reconnect.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13825810502301.jpeg)

This article will discuss the possible reasons.

## Answer

Following are some of the possibilities that the tunnels from both sockets will reconnect at the same time:

1. Both sockets are connected to the same upstream device and it's possible that this common device experienced a glitch, impacting the connectivity from both sockets
2. This situation is somewhat similar to point 1, wherein both sockets connect to the same Internet Service Provider (ISP), and there may be an issue with a shared component within the ISP infrastructure, leading to the reconnection of both sockets.
3. The PoP becomes unavailable for some reasons and both sockets will reconnect to another PoP.
4. The primary socket experienced a connection problem, which could have arisen from various factors such as ISP link issues, hardware problems, and more. Once the primary socket successfully reconnected, it directed the secondary socket to follow suit. Consequently, both sockets show a "Reconnected" status in the event. This is the expected behavior.
