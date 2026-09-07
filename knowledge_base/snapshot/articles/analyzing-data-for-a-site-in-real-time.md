---
title: "Analyzing Data for a Site in Real Time"
slug: "analyzing-data-for-a-site-in-real-time"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/analyzing-data-for-a-site-in-real-time"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyzing Data for a Site in Real Time

This article discusses how to monitor and analyze the traffic metrics for a site in real time.

## Overview

The **Site Monitoring > Real Time** page shows the analytics data for a site in real time. You can show these kinds of network data:

- **Transport** - Network data for each transport similar to the Network Analytics window, for example: average throughput, packet loss, jitter, and so on
- **QoS** - Network data similar to the Priority Analyzer window, for example: average throughput for each Bandwidth Management profile, and MOS

## Showing the Real Time Page

**To show the analytics for a site in real time:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Monitoring > Real Time**.

### Real Time Transport Analytics

The Transport section focuses on the real time top hosts and apps for the transport links. The top half of the window shows the metrics for each link, and the bottom half shows the data in separate graphs. The following example explains the sections in the Site Real Time Transport page:

![real-time.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36487718480285.png)

| Item | Name | Description |
| --- | --- | --- |
| 1 | **QoS** and **Transport** tabs | Click the relevant tab to show real time QoS or transport data. |
| 2 | General Indicators | - **Capacity** - the link capacity metrics depend on the Socket version for the site as follows: - Sockets v21.x and higher - total capacity of Cato WAN links (upstream, downstream) plus Alt WAN links (upstream only) at the site - Sockets v20.x and lower - total capacity of Cato WAN links (upstream, downstream) plus Alt WAN links (upstream only) at the site, minus the Cato system traffic (about 9% of the upstream bandwidth) - **Avg Throughput** - current average throughput (upstream, downstream). - **Queue Size** - Traffic (upstream, downstream) that is queued by the QoS engine in a buffer due to bandwidth congestion. The packets are stored until the QoS engine is able to send them (or discards them). - **Discarded** - current number of packets (upstream, downstream) discarded by the QoS engine due to congestion. |
| 3 | Timeline graphs of transport traffic | Select one of the views to choose how the data is displayed on the graph. You can also pause the data flow. |
| 4 | Transport links | Overview of real time traffic data for each Transport link. |
| 5 | Top hosts and applications | List of top hosts and applications with network usage for the link. |

### Real Time Transport Graphs

The lower half of the Transport section shows connectivity graphs for data related to traffic inside the secure tunnel to the Cato Cloud:

- **Distance** - round trip time between the site and the Cato Cloud inside the tunnel
- **Avg Throughput** - average upstream and downstream throughput for each link (over the length of the bucket)
- **Jitter** - difference in time delay in milliseconds (ms) between data packets
- **Discarded** - current number of packets (upstream, downstream) discarded by the QoS engine due to congestion.
- **Packet Loss** - packet loss percentage over the last mile inside the tunnel

### Real Time QoS Analytics

The QoS section focuses on the real time top hosts and applications for the QoS Bandwidth Management profiles. The following example explains the sections in the Site Real Time QoS window:

![realt-time-qos.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36487739683229.png)

| Item | Name | Description |
| --- | --- | --- |
| 1 | **QoS** and **Transport** tabs | Click the relevant tab to show real time QoS or transport data. |
| 2 | Timeline graphs of transport traffic | Select one of the views to choose how the data is displayed on the graph. You can also pause the data flow. |
| 3 | Bandwidth Management profiles | Overview of real time traffic data for each Bandwidth Management profile. This section also shows the following metric: **Pkt Loss** - Packet Loss of the last-mile ISP link |
| 4 | **Top hosts** and **Top Apps** | List of top hosts and apps with network usage for the profile. |
