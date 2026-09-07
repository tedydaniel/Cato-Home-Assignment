---
title: "Analyzing Traffic for all Account Sites"
slug: "analyzing-traffic-for-all-account-sites"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/analyzing-traffic-for-all-account-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyzing Traffic for all Account Sites

This article discusses how to use the Sites Overview page to show analytics for all sites in your account.

## Overview

The Sites Overview page shows throughput data for each site in your account. The timeline graph shows the network throughput for the site and performance for the selected time range. You can then select a site to drill-down and show more specific analytics.

## Getting Started / Using the Timeline Graph for Sites

**To show the Sites Overview page:**

- From the navigation menu, select **Network > Sites Overview**.

This table explains the fields in the timeline graph for a site.

![Sites_Overview__callouts_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275670685981.png)

| Item | Name | Description |
| --- | --- | --- |
| 1 | Site information | Name and status of the site |
| 2 | Network analytics | Average throughput, distance, and packet loss for this site |
| 3 | PoP location | PoP location that the site is connected to |
| 4 | Throughput drop-down menu | Filter for the site throughput: **Total Throughput** , **Upstream**, or **Downstream** |
| 5 | Monitoring icon | Opens the Network > Network Analytics page to show analytics for that site |
| 6 | Configuration icon | Opens the Network > General page to configure settings for that site |
| 7 | Connection status | Connection status for specific links and indicates if there are performance issues |

## Using the Sites Overview Page

You can use the mouse to show specific throughput data for a point on the timeline. In addition, you can show or hide the connection status for the links.

**To show specific throughput data:**

- Hover the mouse pointer on the timeline, the specific timestamp and throughput for each link are shown.

**To show or hide the link connection status:**

- For a site with multiple links, click the plus or minus icon to show or hide the link connection status.

**These are the explanations of the connection status:**

- Green ![360003838397-Connection_Status_-_Green.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275670776989.png) - link is connected and active, no issues detected
- Olive ![360003930618-Connection_Status_-_Olive.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275687513117.png) - link is connected and passive, no issues detected
- Yellow ![Connection_Status_-_Orange.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275664106269.png) - link experienced a moderate performance issue
- Orange ![Connection_Status_orange.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27098885183389.png) - link experienced a severe performance issue
- Gray ![Connection_Status_-_Gray.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275655353757.png) - link is not connected

## Link Metrics for the Health Bars

If the link suffers from packet loss or a high distance, the colors of the Analytics link health bars indicate the metrics about the link health:

| Link Health | Packet Loss | Distance |
| --- | --- | --- |
| Green (Healthy) | 0 - 2 % | Less than 900 ms |
| Yellow (Issues) | 2 - 5 % | 900 - 950 ms |
| Red (Critical Issues) | Greater than 5 % | Greater than 950 ms |
