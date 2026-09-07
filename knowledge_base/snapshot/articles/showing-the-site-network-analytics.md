---
title: "Showing the Site Network Analytics"
slug: "showing-the-site-network-analytics"
status: "update"
updated: 2026-09-07T08:39:12Z
published: 2026-09-07T08:39:12Z
canonical: "knowledge.catonetworks.com/showing-the-site-network-analytics"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Showing the Site Network Analytics

The **Network Analytics** page helps you analyze the state and quality of the connections of a site to the Cato Cloud. The data in this page shows information for the site and tunnel, port utilization, and LTE statistics.

For more information, [watch this video](/v1/docs/how-to-show-network-analytics-for-sites-video).

> [!NOTE]
> Notes:
> 
> - Cato calculates the link connectivity data every millisecond, however the minimum bucket size in the **Network Analytics** page is 5 seconds. It is possible that packets are discarded, even though the analytics in this page don't show 100% usage.
> - The **Network Analytics** page is typically up-to-date within a 5 minutes time frame. However, it is possible that some data will be delayed up to 30 minutes.
> - Port utilization and LTE data is available only for Socket sites, and only from v20 and higher.
> - The **CPU Load** graph in the **Hardware** tab requires minimum Socket versions as follows:
>   - For physical Sockets - Socket version 21.1.18975
>   - For virtual Sockets - Socket version 22

## Using the Overview Section

**To show the network analytics for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Monitoring > Network Analytics**

This example and the table that follows explain the fields in the **Overview** section:

![Metrics_Overview_Callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34976102813469.png)

| Item | Name | Description |
| --- | --- | --- |
| 1 | Network Analytics site | Select the site that is showing network analytics data |
| 2 | Network Analytics fields for the site | See below, [Explanation of the Network Analytics for a Site](/v1/docs/showing-the-site-network-analytics#explanation-of-the-network-analytics-for-a-site) |
| 3 | Devices | Select which device analytics to display. See below, [Explanation of the Network Analytics for a Site](/v1/docs/showing-the-site-network-analytics#explanation-of-the-network-analytics-for-a-site) |
| 4 | Tunnel, Site, Socket Utilization, and Hardware tabs | Select a tab to show the graphic **Overview** of the links and tunnel metrics, site-level metrics aggregated for all links, Socket utilization metrics, or the Socket hardware metrics. For Socket X1600 LTE models, an additional LTE tab is available. |
| 5 | Bucket Granularity | Amount of time for a specific data point. In the example above, each data point represents 12 minutes of aggregated traffic |
| 6 | Pin for Overview and Details tabs | The **Overview** and **Details** tabs are unpinned by default when they are pinned, then these tabs are still shown when you scroll down |
| 7 | Link connection status | Data of an individual link for the site - The green bar shows the active link - The light green bar shows the passive link with connectivity to the Cato Cloud - A gray bar indicates that the link is down - A yellow section within the bar indicates 2% or more packet loss in either upstream or downstream |
| 8 | Aggregated connection status | Aggregated data of the links for the site The aggregated bar shows the status of the link with the best health for that bucket granularity. For example, if the link for ISP A had a green status and the link for ISP B had a yellow status, the aggregated bar shows a green status. |

> [!NOTE]
> Note:
> 
> The ISP data in this window is provided by [ip2location.com](https://www.ip2location.com/)

### Explanation of the Network Analytics for a Site

- **Status** - the site is **Connected** or **Disconnected** to the Cato Cloud
- **HA Status** - for sites with Socket high availability (HA), status of the HA configuration (otherwise, shows N/A if the site)
- **Master** - indicates whether the **Primary** or **Secondary** Socket is actively sending/receiving traffic
- **Socket or IPsec**- Socket type or IPsec connection
- **PoP** - PoP the site is connected to
- **Avg Distance** - Average round-trip time between the site’s active links and the Cato Cloud
- **#Hosts** - number of hosts in the LAN for this site
- **Devices** - select the Socket data that is displayed in the **Network Analytics** window:
  - Merged - combines data for the primary and secondary Socket
  - Primary - only shows data for the primary Socket
  - Secondary - only shows data for the secondary Socket

### Chinese PoP Locations

For PoP locations in China, some locations have multiple PoPs that a site can connect to. For example, Shanghai_DC1 and Shanghai_DC3.

## Using the Tunnel Graphs

The following graphs display data related to traffic inside the secure tunnel to the Cato Cloud:

- **Max Throughput** - maximum upstream and downstream throughput for each link (over the length of the bucket)
- **Avg Throughput** - average upstream and downstream throughput for each link (over the length of the bucket)
- **Packet Loss** - packet loss percentage over the last mile inside the tunnel. Available only for Socket sites (physical and vSocket).
- **Round-Trip Latency** - round trip time between the site and the Cato Cloud inside the tunnel
- **Tunnel Age** - total time that the current DTLS tunnel between the Socket and the PoP is connected
- **Jitter** - difference in time delay in milliseconds (ms) between data packets

This is an example of the **Throughput** graphs:

![Metrics_Throughput.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34976088037533.png)

These graphs show analytics that are related to the last mile connection (outside of the secure tunnel) between the Socket site and the Cato Cloud. The goal of this data is to show you the quality of the ISP link to the Cato Cloud:

- **Last Mile Packet Loss** - packet loss percentage over the last mile outside the tunnel
- **Last Mile Distance** - round trip time (RTT) between the site and the destination (ie. domain or IP address) outside of the tunnel

For more information about defining the last mile domains, see [Last Mile Monitoring Probes and Connectivity](/v1/docs/last-mile-monitoring-probes-and-connectivity)

## Using the Site Graphs

The following graphs show metrics for traffic inside the secure tunnel to the Cato Cloud aggregated for all links in all Sockets for a site:

- **Max Throughput** - maximum upstream and downstream throughput for the site (over the length of the bucket)
- **Flows** - flow count during the specified period of time
- **Hosts** - host count during the specified period of time

## Using the Socket Utilization Graphs

The following graphs display the data related to the Socket's physical port utilization for its interfaces (LAN1, LAN2, WAN1, etc.):

![Socket_Utilization.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34976071194653.png)

- **Total Bytes by Transport** - the total amount of data sent (Tx) and data received (Rx) for all transport types over your different interfaces. This gives you insight into how much traffic you're sending to the cloud, how much over the internet, and more. You can filter the information to only see a specific interface, or interfaces, using the drop-down menu.
  - Cato - traffic sent over the Cato Cloud
  - Local-breakout - Internet traffic that the Socket sent directly to the destination, such as [Bypass](/v1/docs/bypassing-the-cato-cloud-site-level-policy) rules
  - Off-cloud - WAN traffic sent over the Internet, and not via the Cato Cloud
  - Alt. WAN - traffic sent over Alt. WAN links
  - LAN - includes all LAN traffic (e.g. LAN-LAG-Master and LAN-LAG-Members)
- **Avg. Throughput by Transport** - the amount of data sent and received per transport type over time. You can filter to only see a specific interface and select the checkboxes for the transport types to display.
- **Avg. Throughput by Port** - the amount of data sent and received per interface. You can filter to only see a specific transport type and select the checkboxes for the interfaces to display.

> [!NOTE]
> Note:
> 
> The data in the graphs is from the perspective of the Socket. Meaning, if someone in the LAN downloads a file, the Socket will show it as received (Rx) from the Cato Cloud or internet, and transferred (Tx) to the user.

## Using the Hardware Graphs

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Network Analytics Hardware Graphs.png)

The following graphs display data related to the Socket hardware for a site:

- **CPU Load** - Percent usage for each of the Socket cores for the defined time range. If the site is configured with High Availability (HA), you can show the usage for the primary or secondary Socket, or merge both into the graph.

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

## Using the LTE Graphs

The following graphs display data related to traffic from the LTE connection, and are available under the LTE tab of the Site Analytics page:

> [!NOTE]
> This tab is available only for X1600 LTE Sockets.

- **Cellular Interface Data Usage** - the amount of data sent and received over the LTE connection. You can also filter for specific transport types in the **Show Transports** drop-down menu.
- **Avg. Signal Strength** - the quality of the cellular connection over time.
- **Avg. RSRQ** - the quality of the received reference signal over time. Is used together with Avg. RSRP to determine the overall quality of the connection.
- **Avg. RSRP** - the strength of the received reference signal. Is used together with Avg. RSRQ to determine the overall quality of the connection.
- **Avg. RSSI** - the quality of the signal your device receives from an access point or router.
- **Avg. SINR** - the ratio of signal strength to noise over the cellular line.

## Comparing App Analytics and Network Analytics

The analytics and metrics for the App Analytics page and the pages for network analytics (such as Network > Sites Overview) can have a small discrepancy because the data is calculated differently.

- For network analytics data (including the [accountMetrics API query](https://api.catonetworks.com/documentation/#query-accountMetrics)):
  - Upstream and downstream bytes are counted for encapsulated packets (including DTLS headers overhead)
  - Upstream and downstream data for all flows related to the given tunnel are aggregated together
- For the App Analytics data:
  - Upstream and downstream bytes are counted for non-encapsulated packets (before DTLS encapsulation).
  - Upstream and downstream data are displayed per application
