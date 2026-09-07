---
title: "Analyzing QoS and Bandwidth Management for a Site (Priority Analyzer)"
slug: "analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyzing QoS and Bandwidth Management for a Site (Priority Analyzer)

## Overview of Analyzing Traffic with the Priority Analyzer

The Priority Analyzer window lets you analyze QoS and Policy Based Routing (PBR) data, and can present you with a better understanding of how the network bandwidth for a site is used and routed. Based on your analysis, you can then make changes to the Bandwidth Management profiles and PBR configuration.

Where applicable the data is shown for each separate WAN link.

**To show the analytics for site QoS and traffic priority:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Monitoring > Priority Analyzer**.
3. To filter for a specific Class of Traffic, in **Search** enter the string.

The **Priority Analyzer** window updates and only shows Priorities that match the search string.

This example and the table that follows explain the fields in the Priority Analyzer for the Bandwidth Management Profiles:

![Priority_Analyzer.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247916646685.png)

| Name | Description |
| --- | --- |
| **Bucket Granularity** | The amount of time that is represented in each bucket |
| **Priority** | The Bandwidth Management Profile from **Network > Bandwidth Management** |
| Used In | Name of network rule where this Bandwidth Management Profile is used |
| **Usage & Health** | - **Usage** - Shows total amount and percentage of traffic that is sent over each link - **Health** - Colors of the health bars indicate the traffic status based on discarded packets: idle (![Connection_Status_-_Gray.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247916727965.png) gray), OK (![Connection_Status_-_Green.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247960912413.png) green), issues (![Connection_Status_-_Orange.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247960981021.png) yellow), critical issues (![Connection_Status_-_Red.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247916984861.png) orange) |
| **Throughput** | The average throughput for the time frame (upstream and downstream) |
| **Discarded Packets** | The average percentage of packets discarded by the QoS engine (upstream and downstream) |
| **Delay** | The average traffic delay caused by the QoS engine (upstream and downstream) |

## Drilling Down to Bandwidth Management Profile Data

You can expand a row for a specific Bandwidth Management Profile to drill-down and show the traffic data for that profile.

**To drill down to a Bandwidth Management Profile:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click Site Monitoring > Priority Analyzer
3. In the **Priority Analyzer** screen, click the expand button ![Expand.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247917055005.png) for the Bandwidth Management Profile and the row expands.
4. To show the data for the bucket duration, hover the mouse on one of the graphs.
5. To hide the QoS graphs, click the hide button ![collapse.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247958173981.png) for the Bandwidth Management Profile and the row closes.

The following example shows the additional traffic data for a profile:

![Priority_Analzyer_DrillDown.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247917253149.png)

Use the mouse to hover over on a graph and select a bucket. The following windows and graphs show the traffic data for the bucket:

- **Overview** - (not shown in the screenshot) throughput, discarded packets, and packet delay
- **Throughput** - graph showing the throughput data
- **Packets Delay** - graph showing the packet delay in milliseconds
- **Top Hosts** shows the specific hosts with the highest usage for this profile
- **Top Apps** shows the specific applications with the highest usage for this profile
- **Discarded Packets** - graph showing the number of discarded packets

> [!NOTE]
> Note:
> 
> The graphs in the **Priority Analyzer** window show discarded packets for each QoS profile. However, the graph in the **Metrics** window shows the aggregated discarded packets for the entire site. If there are less than 0.1% discarded packets for the site, then the **Metrics** window shows 0.0% discarded packets. So, it is possible to see discarded packets in the **Priority Analyzer** window, but the **Metrics** window shows 0.0% discarded packets.
