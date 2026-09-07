---
title: "The User Experience Monitoring Drill-Down Page (Remote and Office Users)"
slug: "the-user-experience-monitoring-drill-down-page-remote-and-office-users"
updated: 2026-08-10T10:51:55Z
published: 2026-08-10T10:51:55Z
canonical: "knowledge.catonetworks.com/the-user-experience-monitoring-drill-down-page-remote-and-office-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# The User Experience Monitoring Drill-Down Page (Remote and Office Users)

This article explains how to use the User Experience Monitoring drill-down page to analyze performance and user experience for remote and office users.

For more about reviewing analytics on the Experience Monitoring page, see [Understanding the Experience Monitoring Drill-Down Pages](/v1/docs/understanding-the-experience-monitoring-drill-down-pages).

## Overview

When you click on a specific remote or office user in the Experience Monitoring page, a User Experience Monitoring drill-down page opens with data for that user. The page shows a set of widgets customized to help analyze application traffic for a user. The following sections describe the widgets shown on the page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Experience Monitoring User Drill-Down Aug 2026.png)

## The User Experience Monitoring Widgets

These are the widgets shown for drilling down and analyzing user experience monitoring data:

- User summary - The widget at the top of the page shows basic information about the user such as the user name, the site the user connected from, the last PoP the user connected to, and the ISP. Additionally, the widget shows details about the user's device, including the last device the user connected from, the OS, the Cato Client version, and the internal and external IP addresses used in the connection.
- **Select Application** - Shows the average experience scores and total data usage for the user's top used applications. Select an application to filter the page to show data specific to that application. By default, the page is filtered for the top application by usage.
- Usage summary - The widget to the right of the **Select Application** widget shows usage and traffic information for the selected application
- **User Devices** - Shows information for the devices the user connected from
- **User Application Experience Score** - Shows the user's average experience score for the selected application (**Good**/ **Fair**/**Poor**), as well as a graph showing the application score over the configured time range compared with the overall score for all applications

The average experience score is based on these application performance metrics:

Cato's AI-based algorithm creates unique thresholds for every app.

For more information about how Application Experience Score is calculated, see [this article](/v1/docs/what-is-cato-experience-monitoring).
  - Time to First byte
  - TCP Connect
  - TLS Connect
  - HTTP Latency
  - HTTP/S error
- **Zoom/Teams Performance** - This widget is shown when the Zoom or Microsoft Teams application is selected. The widget shows:
  - The total meetings over the configured time range, with a breakdown by experience (Good, Fair, Poor)
  - A timeline of the meetings during the configured time range, showing the experience for the various media types (audio, video, screen sharing), as well as when disconnections occurred

![DEM_Zoom_widget.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35977782944413.png)
- **Connection Details** - Shows data for the different logical nodes in the network path. For users, the nodes include: **Device Hardware**, **Wi-Fi**, **LAN Gateway**, **Last Mile**, and the selected **Application**. In addition, there are nodes for the Cato Cloud PoP that the traffic is processed through. If the traffic egresses from a second PoP, both the ingress and egress PoPs are shown. Nodes that relate to the destination are also shown, including:

For more information about the experience monitoring scoring for each node, see [Experience Monitoring Connection Details (EA-Socket and Last Mile Underlay)](/v1/docs/experience-monitoring-connection-details).

The widget also provides expandable sections for each node to let you further drill down into detailed data to identify potential issues in each part of the network path. These are described in the following subsections.
  - **First Mile** - The ISP connection between the destination and the PoP.
  - **Destination Socket** - The Socket for the destination site. For example, if the user is accessing a WAN application behind a Socket site.

### Connection Details > Device Hardware

The **Device Hardware** section shows the following data for the user devices:

- **Device Performance** -
  - **Avg. Experience** - The average experience score for device performance based on the average device CPU usage (CPU Load) and memory usage (Memory Load) for the device over the configured time range. The score displayed for the node is based on the poorest result among the metrics. For example, if the CPU Load is Good, but the Memory Load is Fair, the node score is Fair. These are the metrics for each score:
    - CPU Load
      - Good - CPU in use is less than 70%
      - Fair - CPU in use is between 70-90%
      - Poor - CPU in use is greater than 90%
    - Memory Load
      - Good - Memory used is below 60%
      - Fair - Memory used is between 60-80%
      - Poor - Memory used is greater than 80%
  - **Avg. CPU Load** - The average CPU usage for the user's device over the configured time range
  - **Avg. Memory Load** - The average memory usage for the user's device over the configured time range
- Device Performance graphs - Graphs showing **CPU** and **Memory** load over time

### Connection Details > Wi-Fi

The Wi-Fi section displays information about the Wi-Fi signal strength, including:

- **Wi-Fi Performance** -
  - **Avg. Experience** - The average experience score for wi-fi performance based on the Signal Strength metric. This is how wi-fi experience is scored:
    - Good - signal strength -67 dBm or higher
    - Fair - signal strength between -67 dBm and -80 dBm
    - Poor - signal strength -80 dBm or lower
  - **Avg. Signal Strength** - The average wi-fi signal strength for the user over the configured time range
- **Wi-Fi Signal Strength** - A graph showing signal strenth over time for each of the wi-fi networks used by the user

### Connection Details > Access Point

The Access Point section shows wireless access point events collected from integrated Wi-Fi platforms to help you analyze connectivity and authentication issues that impact user experience on the wireless network. Correlate these events with other network nodes to help isolate whether the issue is caused by the access point or other elements, such as local wireless conditions, ISP connectivity, device hardware, or application issues. This node is displayed when the user is connected through a wireless access point that is integrated with Cato Experience Monitoring.

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

- The Access Point node requires integration by configuring an access point connector. This integration is supported for Juniper Mist access points. For more about configuring this integration, see [Juniper Mist: Creating the Device Management Integration](/v1/docs/juniper-mist-creating-the-device-management-integration).
- The Access Point node is available for office users only

#### Access Point Events

The Access Point Events table shows events generated by the access point for the selected user. This helps you identify incidents that are likely to degrade user experience or interrupt Wi-Fi connectivity, such as client disassociations, authentication failures, and DNS or IP assignment issues.

For each event, the table shows:

- **Event Type** – The type of access point event, such as client disassociation, authentication failures, DNS or ARP failures, and IP assignment events
- **Severity** – The severity level reported by the access point platform, if available
- **Device** – The device name
- **Time** – The time the event occurred
- **SSID** – Name of the wireless network the user is connected to
- **Access Point** – The identifier for the access point that generated the event

When you expand an event, detailed information for the event is shown. The details vary by event type and can include:

- **Time** – The exact timestamp of the event
- **Last Association** – The last association time for the client
- **Device** – The client device type
- **MAC Address** – The MAC address of the client device. Click the address to view the access point events in the access point's third-party application. For example, for a Juniper Mist access point, the Juniper Mist application opens and shows the events.
- **SSID** – The wireless network name
- **BSSID** – The MAC address of the access point
- **Protocol** – The wireless protocol in use (for example, IEEE 802.11ax)
- **Band** – The wireless band used by the client (for example, 5 GHz)
- **Channel** – The wireless channel
- **Security** – The security mode used by the SSID (for example, WPA3-SAE-PSK/CCMP)
- **Reason Code** – The reason code reported by the access point, when applicable
- **Description** – A description of the event or reason code

### Connection Details > LAN Gateway

The LAN Gateway section shows information about the LAN gateway performance, including:

- **LAN Gateway Performance** -
  - **Avg. Experience** - The average experience score for LAN gateway performance based on the average packet loss and distance over the configured time range. The score is calculated based on the least good result between the two metrics. For example, if LAN Gateway Distance is Good and LAN Gateway Packet Loss is Poor, the node score is Poor. These are the metrics for each score:
    - LAN Gateway Packet Loss
      - Good - less than 1% packet loss.
      - Fair - between 1-5% packet loss.
      - Poor - more than 5% packet loss.
    - LAN Gateway Distance
      - Good - below 10 ms.
      - Fair - between 10-50 ms.
      - Poor - exceeding 50 ms
  - **Avg. Packet Loss** - The average percentage of packets lost inside the LAN gateway over the configured time range
  - **Avg. Distance** - The average distance between the site and the Cato Cloud inside the tunnel over the configured time range
- LAN Gateway Performance graphs - Graphs showing **Packet Loss** and **Distance** load over time

### Connection Details > Last Mile

The **Last Mile** section shows the following data for the quality of connection for the encrypted tunnel connection to the PoP:

- **Last Mile Performance** -
  - **Avg. Experience** - The average experience score for last mile performance.

The score for the Last Mile node is based on the following metrics for the Last Mile Overlay, as shown in the widgets:

The score displayed for the node is based on the poorest result between the two metrics. For example, if the Tunnel Packet Loss is Good, and Tunnel Distance is Poor, the node score is Poor.
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
  - **Underlay** - Probes sent on the out-of-tunnel last mile connection, referred to as the underlay, to measure the quality of the ISP connection to the PoP, independent of the in-tunnel connection (the overlay). This helps identify and diagnose out-of-tunnel issues that could impact last-mile performance for Socket sites and remote users.

For Socket sites, underlay probes are sent between the Socket and the PoP. The probes are sent for each WAN interface in the Socket. For remote users, underlay probes are sent by the Client on the user's device to PoP. The widgets show the name of the connected PoP location, the IP address of the connected service node in the PoP, and, for Socket traffic, the interface name. If the PoP name is unavailable, only the service node IP address is shown.

**Note:** For data to be collected for the Underlay Probes feature, the following is required:
    - For office user (Socket site) metrics - Socket v21.1.18975 or higher
    - For remote user metrics - Client versions macOS 5.10 or Windows 5.17, or higher
  - **Overlay** - These probes measure the quality of connection for the Cato tunnel connection to the PoP.

**Note:** For the throughput graphs, use the selector to choose to show **Avg** or **Max** throughput.

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

#### Unified User Last Mile View

By default, the User Experience Monitoring drill-down page is filtered to show metrics for either a remote user or an office user, depending on whether you clicked on the user from the **Remote Users** tab or the **Office Users** tab. However, by removing the filter in the filter bar, you can view combined last-mile metrics for the same user connecting remotely and behind a site. When you remove the filter, these changes apply:

- The graphs in the Underlay section show data lines for both office user (Socket site) and remote user probes for the selected user
- The Overlay section shows the following separate graphs for site data and remote user data:
  - Site Packet Loss Upstream
  - Site Packet Loss Downstream
  - Site Round-Trip Latency
  - Remote User Probe Packet Loss
  - Remote User Probe Round-Trip Latency

### Connection Details > First Mile

The **First Mile** refers to the ISP connection between the destination and the PoP.

The **First Mile** section shows the following data for the quality of connection for the encrypted tunnel connection to the PoP:

- **First Mile Performance** -
  - **Avg. Overlay Experience** - The average experience score for first mile overlay performance.

The score for the First Mile node is based on the following metrics for the First Mile Overlay, as shown in the widgets:

The score displayed for the node is based on the poorest result between the two metrics. For example, if the Tunnel Packet Loss is Good, and Tunnel Distance is Poor, the node score is Poor.

In addition, the following metrics are shown for each Socket WAN link:
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

The **Destination Socket** section shows data for Sockets of the destination site. The following data are shown:

- **Socket Performance** -
  - **Avg. Experience** - The average experience score for Socket performance based on the average Socket CPU usage (CPU Load) for the site over the configured time range. This score is calculated based on the poorest-performing core of the site's primary Socket.
    - Good - CPU in use is less than 70%
    - Fair - CPU in use is between 70-90%
    - Poor - CPU in use is greater than 90%
  - **Avg. CPU Load** - The average Socket CPU usage (CPU Load) for the site over the configured time range (based on the poorest-performing core of the site's primary Socket).
- **CPU Load** - Percent usage for each of the Socket cores for the defined time range. If the site is configured with High Availability (HA), the graph shows the usage for both the primary and secondary Socket cores.

![Socket_CPU_-_DEM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35977825999517.png)

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

### Connection Details > Zoom, MS Teams, and Webex Meetings

This section shows application-specific metrics for UCaaS traffic including Zoom, Microsoft Teams, and Webex sessions. The metrics provide insights into the experience of video, audio, and screen sharing during meetings.

These metrics require the configuration of Cato connectors. For more information, see these articles:

- [Microsoft Teams: Configuring the Experience Monitoring UCaaS Connector](/v1/docs/microsoft-teams-configuring-the-experience-monitoring-ucaas-connector)
- [Zoom: Configuring the Experience Monitoring UCaaS Connectors](/v1/docs/zoom-configuring-the-experience-monitoring-ucaas-connectors)
- [Webex: Configuring the Experience Monitoring UCaaS Connector](/v1/docs/webex-configuring-the-experience-monitoring-ucaas-connector)

![DEM_Zoom_Graphs.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35977807750685.png)

**To view metrics for Zoom, MS Teams, or Webex meetings:**

1. On the User Experience Monitoring drill-down page, in the [Select Application](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users#the-user-experience-monitoring-widgets) widget, select Zoom, Teams, or Webex.
2. In the **Connection Details** widget, open the **Zoom Meetings**, **MS Teams Meetings**, or **Webex Meetings** section.

> [!NOTE]
> Note:
> 
> The Zoom, MS Teams, and Webex sections only appear for a user once the user has connected to the app after the connector is configured.

#### Understanding the Zoom, Teams, and Webex Metrics

The information shown for each meeting includes the **Device** used, **Meeting date**, **Call duration**, **Total participants**, and overall **Experience** for the meeting (**Poor**, **Fair**, or **Good**). This **Experience** score is based on the scores for **Audio**, **Video**, and **Screen sharing** experience, and equals the lowest score of those three.

The scores for **Audio**, **Video**, and **Screen sharing** experience are based on a calculation of Mean Opinion Score (MOS) taking into account packet loss, jitter, and latency. The scores are based on an average of the MOS calculated for upstream and downstream traffic.

For Zoom and Webex meetings, the data is shown as granular time series graphs for precise detection and troubleshooting. You can use the time series graphs to correlate the meeting timeline with network metrics. The graphs include the experience score for **Audio**, **Video**, and **Screen sharing**, as well as **Packet Loss**, **Jitter**, **Latency** , and **Bitrate** metrics for each media type. The experience score graph highlights any disconnection events during the call.

Due to limitations in the Teams application, the Teams meetings graphs show the various metrics as an average value over the entire duration of the call, or as the maximum value reached during the call duration.

- Select **Max** for the graphs to show metrics based on the maximum value during each interval
- Select **Avg.** for the graphs to show metrics based on the average value during each interval
- You can toggle on and off the **Sending** and **Receiving** data lines

This is the formula for calculating MOS:

- MOS = 1 + 0.035 * R + 0.000007 * R * (R - 60) * (100 - R) where R is the rating factor determined by effective latency and packet loss

> [!NOTE]
> Notes:
> 
> - For Microsoft Teams
>   - It may take up to 30 minutes for meeting data to be shown
>   - The connector generally accesses meeting data up to 1 hour back. However, when the connector is first configured, up to 5 hours of data can be accessed
>   - The metrics include data from both Microsoft Teams and Skype meetings
