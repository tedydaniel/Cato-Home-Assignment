---
title: "What does \"Previous Stable\" Mean in the Socket WebUI?"
slug: "what-does-previous-stable-mean-in-the-socket-webui"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/what-does-previous-stable-mean-in-the-socket-webui"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What does "Previous Stable" Mean in the Socket WebUI?

## Question

When you log in to the Socket Web UI, under Status, the Steering data source displays PREVIOUS STABLE. What does this indicate, and could it negatively impact the device's performance?

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25298533341213.png)

## Answer

This can occur in two scenarios.

### 1. The steering list is faulty

When "Preferred PoP Locations" is set to its default setting (Automatic), the Socket continuously receives new steering results at regular intervals, which consist of a list of the most optimal PoPs for the site. This would ensure the site is always connected to the best available PoP. When the Socket receives a new steering result, the Steering data source will reflect "SERVER." However, if the socket wasn’t able to connect to the first pop in the new steering results for any reason (pop down, last mile issues, the HA/VRRP case, etc), the steering result is considered unstable, and the Steering data source will change to PREVIOUS STABLE.

### 2. VRRP is not functioning properly between the HA Sockets

In a [High Availability (HA) Socket deployment](/v1/docs/what-is-socket-ha), the **primary** Socket will receive the steering result for the site. If the VRRP connection between the Sockets fails or doesn’t function correctly, the Steering data source on the *secondary* Socket will switch from SERVER to PREVIOUS STABLE. This is expected and in accordance with our current design. When this happens, follow the steps listed in the [Socket-HA-Status-Troubleshooting](/v1/docs/socket-ha-status-troubleshooting) article to troubleshoot why the VRRP connections between the Sockets are not healthy.
