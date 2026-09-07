---
title: "The Site Experience Monitoring Drill-Down Page"
slug: "the-site-experience-monitoring-drill-down-page"
updated: 2026-08-31T08:03:31Z
published: 2026-08-31T08:03:31Z
canonical: "knowledge.catonetworks.com/the-site-experience-monitoring-drill-down-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# The Site Experience Monitoring Drill-Down Page

This article explains how to use the Site Experience Monitoring drill-down page to analyze performance and user experience for a site.

For more about reviewing analytics on the Experience Monitoring page, see [Understanding the Experience Monitoring Drill-Down Pages](/v1/docs/understanding-the-experience-monitoring-drill-down-pages).

## Overview

When you click on a specific site in the Experience Monitoring page, a Site Experience Monitoring drill-down page opens with data for that site. The page shows a set of widgets customized to help analyze application traffic for a site. The following sections describe the widgets shown on the page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Experience Monitoring Site Drill-Down Aug 2026.png)

## The Site Experience Monitoring Widgets

These are the widgets shown for drilling down and analyzing site experience monitoring data:

- Site summary - The widget at the top of the page shows basic information about the site such as its connection status, HA status, Socket type, and ISP.
- **Select Application** - Shows the average experience scores and total data usage for the site's top used applications. Select an application to filter the page to show data specific to that application. By default, the page is filtered for the top application by usage.
- Usage summary - The widget to the right of the **Select Application** widget shows usage and traffic information for the selected application
- **Top Site Hosts/Users using** - Shows average experience score and total usage over the configured time range for the top users or hosts that used the selected application. Use the dropdown to select data for **Site Hosts** or **Users**
- **Site Application Experience Score** - This widget includes the following:
  - A graph showing the application score over the configured time range compared with the overall score for all applications

The average experience score is based on these application performance metrics:

Cato's AI-based algorithm creates unique thresholds for every app.

For more information about how Application Experience Score is calculated, see [this article](/v1/docs/what-is-cato-experience-monitoring).
    - Time to First byte
    - TCP Connect
    - TLS Connect
    - HTTP Latency
    - HTTP/S error
  - An Events feed showing events relevant to the experience for the selected application
- **Connection Details** - Shows data for the different logical nodes in the network path. For sites, the nodes include: **Site Hosts**, **Socket**, **Last Mile**, and the selected **Application**. In addition, there are nodes for the Cato Cloud PoP that the traffic is processed through. If the traffic egresses from a second PoP, both the ingress and egress PoPs are shown. Nodes that relate to the destination are also shown, including:

For more information about the experience monitoring scoring for each node, see [Experience Monitoring Connection Details (EA-Socket and Last Mile Underlay)](/v1/docs/experience-monitoring-connection-details).

The widget also provides expandable sections for each node to let you further drill down into detailed data to identify potential issues in each part of the network path. These are described in the following subsections.
  - **First Mile** - The ISP connection between the destination and the PoP.
  - **Destination Socket** - The Socket for the destination site. For example, if the user is accessing a WAN application behind a Socket site.

### Connection Details > Socket

The **Socket** section shows the following data for the site Sockets:

- **Socket Performance** -
  - **Avg. Experience** - The average experience score for Socket performance based on the average Socket CPU usage (CPU Load) for the site over the configured time range. This score is calculated based on the poorest-performing core of the site's primary Socket.
    - Good - CPU in use is less than 70%
    - Fair - CPU in use is between 70-90%
    - Poor - CPU in use is greater than 90%
  - **Avg. CPU Load** - The average Socket CPU usage (CPU Load) for the site over the configured time range (based on the poorest-performing core of the site's primary Socket).
- **CPU Load** - Percent usage for each of the Socket cores for the defined time range. If the site is configured with High Availability (HA), the graph shows the usage for both the primary and secondary Socket cores.

![Socket_CPU_-_DEM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27304835370653.png)

If you notice high Socket CPU utilization, here are the steps to troubleshoot:

If you observe constant high CPU usage concurrent with network packet loss:

For more information about troubleshooting Socket CPU usage, see [Performance Issues for Socket Sites Troubleshooting](/v1/docs/performance-issues-for-socket-sites-troubleshooting).
  1. Access the [Socket WebUI](/v1/docs/using-the-socket-webui-tools) and select the HW Status tab.
  2. Check the current CPU % usage for each core.
  3. Monitor for consistent CPU utilization above 90%, as this will directly impact Socket performance and cause packet loss and high latency.
  1. Document when the high CPU usage occurs.
  2. Note which cores are experiencing high utilization.
  3. Contact Cato Support for assistance.
  - This feature requires minimum Socket versions as follows:
    - For physical Sockets - Socket version 21.1.18975
    - For virtual Sockets - Socket version 22
- **Memory Usage** - Percent of Socket memory in use for the defined time range. For HA sites, the graph shows the usage for both the primary and secondary Sockets.
- **Flows per Second** - Number of network flows processed by the Socket per second for the defined time range. For HA sites, the graph shows the flows for both the primary and secondary Sockets.
- **Socket Process Uptime** - Length of time the Socket software process has been running since it was last restarted. For HA sites, the graph shows the uptime for both the primary and secondary Sockets.

### Connection Details > Last Mile

The **Last Mile** section shows the following data for the quality of connection for the encrypted tunnel connection to the PoP:

- **Last Mile Performance** -
  - **Avg. Experience** - The average experience score for last mile performance.

The score for the Last Mile node is based on the following metrics for the Last Mile Overlay, as shown in the widgets:

The score displayed for the node is based on the poorest result among the metrics. For example, if Tunnel Packet Loss Upstream is Good, Tunnel Packet Loss Downstream is Good, and Tunnel Distance is Poor, the node score is Poor.
    - Tunnel Upstream Packet Loss
      - Good - less than 1% packet loss.
      - Fair - between 1-5% packet loss.
      - Poor - more than 5% packet loss.
    - Tunnel Downstream Packet Loss
      - Good - less than 1% packet loss.
      - Fair - between 1-5% packet loss.
      - Poor - more than 5% packet loss.
    - Tunnel Distance
      - Good - below 20 ms.
      - Fair - between 20-100 ms.
      - Poor - exceeding 100 ms
  - **Avg. Packet Loss** - Percentage of packets that were lost over the last mile inside the tunnel for upstream and downstream traffic, averaged over the configured time range
  - **Avg. Distance** - Distance between the site and the Cato Cloud inside the tunnel, averaged over the configured time range
- Last Mile graphs - These graphs include metrics based on two different types of probes. These are the probe types and the widgets shown for each:
  - **Underlay** - Probes sent on the unecrypted out-of-tunnel last mile connection to measure the quality of the ISP connection to the PoP, independent of the encrypted overlay. This helps identify and diagnose out-of-tunnel issues that could impact last-mile performance for Socket sites.

The probes are sent for each WAN interface in the Socket. The widgets show the interface name and the name of the connected PoP location, as well as the IP address of the connected service node in the PoP. If the PoP name is unavailable, only the service node IP address is shown.

**Note:** For data to be collected for the Underlay Probes feature, Socket v21.1.18975 or higher is required

| Graph | Description |
| --- | --- |
| Packet Loss | Percentage of packets that were lost over the last mile outside the tunnel. |
| Round-Trip Latency | Round-trip time between a given node in the network path (e.g. a site or user device) and the Cato Cloud, measured outside the tunnel. |
  - **Overlay** - These probes measure the quality of connection for the Cato tunnel connection to the PoP.

| Graph | Description |
| --- | --- |
| Packet Loss Upstream | Percentage of packets that were lost over the last mile inside the tunnel for upstream traffic. |
| Packet Loss Downstream | Percentage of packets that were lost over the last mile inside the tunnel for downstream traffic. |
| Discarded Packets Upstream | Percentage of packets that were received but not processed for upstream traffic. |
| Discarded Packets Downstream | Percentage of packets that were received but not processed for downstream traffic. |
| Round-Trip Latency | Distance between the site and the Cato Cloud inside the tunnel. |
| Tunnel Age | Total time that the current DTLS tunnel between the Socket and the PoP is connected. |
| Jitter Upstream | Difference in time delay in milliseconds (ms) between upstream data packets. |
| Jitter Downstream | Difference in time delay in milliseconds (ms) between downstream data packets. |
| Max Throughput Upstream | Maximum measured throughput inside the tunnel for upstream traffic |
| Max Throughput Downstream | Maximum measured throughput inside the tunnel for downstream traffic |
| Avg Throughput Upstream | Average upstream throughput inside the tunnel for each link (over the length of the bucket) |
| Avg Throughput Downstream | Average downstream throughput inside the tunnel for each link (over the length of the bucket) |

### Connection Details > First Mile

The **First Mile** refers to the ISP connection between the destination and the PoP.

The **First Mile** section shows the following data for the quality of connection for the encrypted tunnel connection to the PoP:

- **First Mile Performance** -
  - **Avg. Overlay Experience** - The average experience score for first mile overlay performance.

The score for the First Mile node is based on the following metrics for the First Mile Overlay, as shown in the widgets:

The score displayed for the node is based on the poorest result between the two metrics. For example, if the Tunnel Packet Loss is Good, and Tunnel Distance is Poor, the node score is Poor.

In addition the following metrics are shown for each Socket WAN link:
    - Tunnel Upstream Packet Loss
      - Good - less than 1% packet loss.
      - Fair - between 1-5% packet loss.
      - Poor - more than 5% packet loss.
    - Tunnel Downstream Packet Loss
      - Good - less than 1% packet loss.
      - Fair - between 1-5% packet loss.
      - Poor - more than 5% packet loss.
    - Tunnel Distance
      - Good - below 20 ms.
      - Fair - between 20-100 ms.
      - Poor - exceeding 100 ms
  - **Avg. Packet Loss** - Percentage of packets that were lost over the first mile inside the tunnel (Overlay) for upstream and downstream traffic, averaged over the configured time range
  - **Avg. Distance** - Distance between the site and the Cato Cloud inside the tunnel (Overlay), averaged over the configured time range
  - **Avg. Underlay Experience** - The average experience score for the first mile out-of-tunnel connection.
- First Mile graphs - These graphs include metrics based on two different types of probes. These are the probe types and the widgets shown for each:
  - **Underlay** - Probes sent on the unecrypted out-of-tunnel first mile connection to measure the quality of the ISP connection to the PoP, independent of the encrypted overlay. This helps identify and diagnose out-of-tunnel issues that could impact first-mile performance for Socket sites.

The probes are sent for each WAN interface in the Socket. The widgets show the interface name and the name of the connected PoP location, as well as the IP address of the connected service node in the PoP. If the PoP name is unavailable, only the service node IP address is shown.

**Note:** For data to be collected for the Underlay Probes feature, Socket v21.1.18975 or higher is required

| Graph | Description |
| --- | --- |
| Packet Loss | Percentage of packets that were lost over the first mile outside the tunnel. |
| Round-Trip Latency | Round-trip time between a given node in the network path (e.g. a site or user device) and the Cato Cloud, measured outside the tunnel. |
  - **Overlay** - These probes measure the quality of connection for the Cato tunnel connection to the PoP.

| Graph | Description |
| --- | --- |
| Site Packet Loss Upstream | Percentage of packets that were lost over the destination site first mile inside the tunnel for upstream traffic. |
| Site Packet Loss Downstream | Percentage of packets that were lost over the destination site first mile inside the tunnel for downstream traffic. |
| Site Round-Trip Latency | Round-trip time between a given node in the network path (e.g. a site or user device) and the Cato Cloud, measured inside the tunnel. |
| Tunnel Age | Total time that the current DTLS tunnel between the Socket and the PoP is connected. |
| Jitter Upstream | Difference in time delay in milliseconds (ms) between upstream data packets. |
| Jitter Downstream | Difference in time delay in milliseconds (ms) between downstream data packets. |
| Max Throughput Upstream | Maximum measured throughput inside the tunnel for upstream traffic |
| Max Throughput Downstream | Maximum measured throughput inside the tunnel for downstream traffic |
| Avg Throughput Upstream | Average upstream throughput inside the tunnel for each link (over the length of the bucket) |
| Avg Throughput Downstream | Average downstream throughput inside the tunnel for each link (over the length of the bucket) |

### Connection Details > Destination Socket

The **Destination Socket** section shows data for Sockets of the destination site. The metrics shown for the destination Sockets are the same as those for the source site Sockets. For descriptions of these metrics, see above, [Connection Details > Socket](/docs/the-site-experience-monitoring-drill-down-page#UUID-3378985d-79a2-ae40-41a3-4373501cf5e1_section-idm2174832873912074).

### Connection Details > Application

The **Application** section shows the following metrics for application performance:

- **Avg. Experience** -

The average experience score is based on these application performance metrics:

Cato's AI-based algorithm creates unique thresholds for every app.

For more information about how Application Experience Score is calculated, see [this article](/v1/docs/what-is-cato-experience-monitoring).
  - Time to First byte
  - TCP Connect
  - TLS Connect
  - HTTP Latency
  - HTTP/S error
- Application graphs - These metrics are described in the following table:

| Graph | Description |
| --- | --- |
| Time to First Byte | Duration of time between the HTTP request and the receipt of the first byte. |
| TCP Connect | Time taken to establish a TCP connection. |
| TLS Connect | Time taken to establish a TLS connection. |
| HTTP/S Latency | Duration of time between the request and the response. |
| HTTP/S Error Rate | Percentage of HTTP errors. |
| Packet Loss | Percentage of packets that were lost over the last mile inside the tunnel. |
| Distance | Distance between the site and the Cato Cloud inside the tunnel. |
