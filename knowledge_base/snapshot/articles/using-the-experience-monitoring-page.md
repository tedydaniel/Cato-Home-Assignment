---
title: "Using the Experience Monitoring Page"
slug: "using-the-experience-monitoring-page"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/using-the-experience-monitoring-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Experience Monitoring Page

This article explains how to use the **Experience Monitoring** page to monitor performance and user experience in your network.

## Overview

Traffic and performance of applications can be related to factors outside of the Cato Cloud. The Cato DEM service provides insight into user, application, and site experience, proactively monitoring performance and pinpointing issues. From the **Experience Monitoring** page, you can view a summary of user experience for application usage in your network on the account or site level. You can further drill-down to see the experience for specific sites, applications, or remote and office workers. You can use the filters and widgets to help you see the data to troubleshoot the cause of poor app performance.

The **Experience Monitoring** page displays data from traffic that flows through the Cato Cloud. DEM only analyzes traffic data from sites or remote users via the Clients. For more information about Experience Monitoring, see [What is Cato Experience Monitoring](/v1/docs/what-is-cato-experience-monitoring).

> [!NOTE]
> **Note:**
> 
> Application performance metrics are only calculated for outbound TCP traffic.

### Getting Started with Experience Monitoring

The **Experience Monitoring** page displays the average experience score for all an account. You can further breakdown the score by site, remote and office users, users and hosts, and applications.

When clicking on any of the tabs on the page, you have a list of sites, users, or applications to get more information about the experience of those specific entities. For example, if a user is complaining about a poor experience, you can filter by that user's name or click on the **Remote User** tab to locate them. Once you click on their name, you can see more high-level information in the [Connection Details](/v1/docs/experience-monitoring-connection-details) nodes, and click on the different tabs to see if there is a problem on their computer, Wi-Fi connection, or one of the applications they're using.

![DEM NEW UI May 2026.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36504075529885.png)

**To view the Experience Monitoring page:**

- From the navigation menu, click **Home > Experience Monitoring**.

The following table explains the data and analytics available from the Experience Monitoring page.

| Name | Description |
| --- | --- |
| Summary Bar | At the top of the page, the summary bar shows account-wide experience monitoring data, including: - Connectivity status of account sites - Summary of experience scores for WAN and Internet applications - Summary of app integrations statuses |
| Filter Bar | The filters are applied to the page. Selected filters apply to all widgets on the page. A filter for Sanctioned Applications is applied by default. |
| Time Range | The time range applied to the page. The maximum time range is three months. |
| Account Experience | The average experience score over time for all applications and the number of applications in each experience category (**Good**/**Fair**/**Poor**). The average experience score is based on these application performance metrics: - Time to First byte - TCP Connect - TLS Connect - HTTP Latency - HTTP/S error Cato's AI-based algorithm creates unique thresholds for every app. The graph shows average experience over time for sites, remote users, and the overall account (sites and remote users). |
| Feed | A dynamic feed of recent events related to experience issues. - For accounts with an XOps license, the feed shows recent XOps stories related to experience issues, such as [Experience Anomaly](/v1/docs/analyzing-experience-monitoring-anomalies) stories, [Account Operations](/v1/docs/drilling-down-and-analyzing-xops-account-operations-stories-1) stories, and more. |
| Experience Type Tabs | Each tab shows the analytics and data for that entity in your network: Sites, Remote Users, Office Users, Site Hosts, and Applications. Each tab displays data for the selected entity. You can click on items in this table to open the drill-down page for the entity. |

## Filtering the Experience Monitoring Page

There are two ways to filter the data in the Experience Monitoring page:

- Automatically update the filter with the selected item
- Manually configure the filter

When you manually create a filter or add an item to the update filter, the data and analytics on the Experience Monitoring page is automatically updated and only shows data for filtered items. For example, if you filter for the Microsoft Word application, the page only shows analytics and data that are related to using the Microsoft Word application. No other application data is displayed until you change or clear the filter.

The Experience Monitoring page data is typically up-to-date within a 5 minute time frame. However, it is possible that some data will be delayed up to 30 minutes.

For more about configuring filters, see [Configuring Filters to Analyze Dashboard Data](/v1/docs/configuring-filters-to-analyze-dashboard-data).

## Reviewing Analytics

You can review detailed analytics for each site, remote or office user, user/host, or application used in your network. This provides you with granular data to monitor the experience across your network.

A **User** is a user logged in to a device with the Cato Client installed on it and connecting as follows:

- Remote User - connecting remotely (not from behind a site)
- Office User - connecting from behind a site

A **Site host** is a device that is connecting to the network without the Client located behind a site, for example an IoT device or printer.

### Drilling Down to Review Specific Item Data

Select a tab and then a specific item to drill down and view data for that item in a different page.

**To drill down and review data for a specific item:**

1. Select one of the tabs.
2. Click on an item. A new page opens with data for the specific item.

### Understanding Site Experience Monitoring

The **Sites** tab shows a broad set of experience monitoring data for each site in the account. The **Performance View** dropdown lets you select from a range of tables showing metrics for different nodes in the network path. By default, the **Application** metrics described in the table below are shown. You can also view metrics for these nodes: **Socket**, **Last Mile - Underlay**, **Last Mile - Overlay**. For a description of these additional views, see below [Additional Site Experience Metric Tables](/docs/using-the-experience-monitoring-page#h_01KRXGRPCGDDBM8Q1GTDQT61FP).

When you drill down into a site, the page provides information about the site, such as its current connection and HA status, the PoP it's connected to, and how many hosts are currently connected through the site.

In addition, the Connection Details widget shows nodes in a site to help you pin-point the issue impacting the user experience. This widget provides an instant understanding of how the different nodes in the site are functioning, and gives you a visual indication if there is a problem anywhere in the connection. For example, if the Last Mile node is yellow, you can click to see the widgets for the Last Mile connection to see if there are any issues.

For a full list of the available widgets, see [The Site Experience Monitoring Drill-Down Page](/v1/docs/the-site-experience-monitoring-drill-down-page).

![Site_Experience_Monitoring_drilldown.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29319159339165(1).png)

| Item | Description |
| --- | --- |
| Site | Name of the site defined in the Cato Management Application (CMA). |
| Experience | The average site experience score for all applications |
| # Unique Users | Number of identified users in the site |
| # Apps | Number of applications used in the site |
| Country Code | Code for the country configured for the site in the CMA |
| # Flows | Number of flows generated by the site |
| Avg. TTFB | The average duration of time between the HTTP request and the receipt of the first byte for site flows |
| Usage | Total upstream and downstream bandwidth usage for the site |
| Download | Downstream bandwidth usage for the site |
| Upload | Upstream bandwidth usage for the site |
| Current Status | Status of the site's connection to the Cato Cloud. |
| HA Status | For sites with Socket high availability (HA), status of the HA configuration (Shows N/A if HA is not configured for the site). |
| Master | For Socket HA, the Socket that is actively sending/receiving traffic. |

### Understanding Remote or Office User Experience Monitoring

The **Remote Users** and **Office Users** tabs shows a broad set of experience monitoring data for each of the connected users in the account. The **Performance View** dropdown lets you select from a range of tables showing metrics for different nodes in the network path. By default, the **Application** metrics described in the table below are shown. You can also view metrics for these nodes: **Device**, **Wi-Fi**, **LAN Gateway**, and **Last Mile - Overlay**. For a description of these additional views, see below [Additional Remote and Office User Experience Metric Tables](/docs/using-the-experience-monitoring-page#h_01KRXGRPCGP539ZZR7M2D39A43).

When you drill down into data for a specific user, the page provides information such as the site the user is connected through, their device name, OS, and internal and external IP addresses.

In addition, the Connection Details can provide you with an instant understanding of how the different nodes in the user's connection experience are functioning, and give you a visual indication if there is a problem anywhere in the connection. For example, if the Device node is yellow, you can click to see the widgets for the Device to see if there are issues with the CPU or memory.

The different tabs on the User Experience page provide more information about the connection through the various widgets.

For a full list of the available widgets, see [The User Experience Monitoring Drill-Down Page (Remote and Office Users)](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users).

![User_Experience_Monitoring_drilldown.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29319159368989(1).png)

| Item | Description |
| --- | --- |
| User Name | Name of the user |
| Email | User email address |
| Device Name | Name of the device the user connected from |
| Experience | The average user experience score for all applications |
| # of Apps | Number of applications used by the user |
| PoP | The PoP the user is connected to |
| # Flows | Number of flows generated by the userNumber of flows generated by the site |
| Avg. TTFB | The average duration of time between the HTTP request and the receipt of the first byte for the user flows |
| Usage | Total upstream and downstream bandwidth usage for the user |
| Download | Downstream bandwidth usage for the user |
| Upload | Upstream bandwidth usage for the user |
| Site | For Office Users, the site that the user is located behind |
| Last Connected PoP | Most recent PoP the user is connected to. |
| Last Connected Device | The most recent device the user connected to the Cato Cloud with. |

### Understanding Site Host Experience Monitoring

The **Site Hosts** tab shows all the hosts that are behind a site. When you drill down into a specific item, the page provides information such as the internal IP address, the average TTFB, and the number of flows.

In addition, the Connection Details can provide you with an instant understanding of how the different nodes in the connection experience are functioning, and give you a visual indication if there is a problem anywhere in the connection. For example, if the Application node is yellow, you can click to see the widgets for the Application Performance to see if there are issues with the TTFB or latency.

The different tabs on the Host Experience Monitoring page provide more information about the connection through the various widgets.

For a full list of the available widgets, see [The Host Experience Monitoring Drill-Down Page](/v1/docs/the-host-experience-monitoring-drill-down-page).

![Host_Experience_Monitoring_drilldown.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29319191766173(1).png)

The table below explains the fields for the application experience metrics for a specific host.

| Item | Description |
| --- | --- |
| Host Name | The name of the host |
| Experience | The average experience score for all applications used by the host |
| Site Name | The site that the host is located behind. |
| #Apps | Number of applications used by the host |
| #Country Code | Code for the country of the site the host is connected from |
| PoP | Cato PoP the site is connected to |
| #Flows | Number of flows generated by the host |
| Avg. TTFB | The average duration of time between the HTTP request and the receipt of the first byte for the host flows |
| Usage | Total upstream and downstream bandwidth usage for the host |
| Download | Downstream bandwidth usage for the host |
| Upload | Upstream bandwidth usage for the host |

### Understanding Application Experience Monitoring

The **Applications** tab shows experience data for the different applications being used in your account. The **Performance View** dropdown lets you select to view either metrics for the various applications, or monitoring data collected by probes configured for application traffic. The table below describes the application metrics shown. For a description of the probe data, see below [Additional Application Metric Tables](/docs/using-the-experience-monitoring-page#h_01KRXM39A9MRS79AGZM9A8YXBP).

information for probes for application traffic shown i

When you drill down into a specific item, the page provides information about what kind of security risk the application poses and to which category it belongs.

In addition, the various tabs provide widgets about the specific application performance and which users and hosts are currently using the application.

For a full list of the available widgets, see [The Application Experience Monitoring Drill-Down Page](/v1/docs/the-application-experience-monitoring-drill-down-page).

![Application_Experience_Monitoring.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29319155895069(1).png)

| Item | Description |
| --- | --- |
| Application Name | Name of the identified application |
| Experience | The average experience score for the application |
| #Users/Hosts | Number of users and hosts who used the application during the configured time range |
| #Flows | Number of flows generated by the application |
| Avg. TTFB | The average duration of time between the HTTP request and the receipt of the first byte for application flows |
| Usage | Total upstream and downstream bandwidth usage for the application |
| Download | Downstream bandwidth usage for the application |
| Upload | Upstream bandwidth usage for the application |
| Category | Cato Category that the application belongs to |

## Additional Experience Metric Tables

### Additional Site Experience Metric Tables

#### Socket

The following table describes the information shown in the **Performance View: Socket** table.

| Item | Description |
| --- | --- |
| Site Name | Name of the site defined in the Cato Management Application (CMA). |
| Experience | The average experience score for site traffic over the configured time range for the Socket node, based on Socket hardware performance. |
| Max Socket CPU | The maximum percent of Socket CPU load reached over the configured time range. The graph shows the maximum Socket CPU over time. |

#### Last Mile Underlay

The following table describes the information shown in the **Performance View: Last Mile Underlay** table.

| Item | Description |
| --- | --- |
| Site Name | Name of the site defined in the Cato Management Application (CMA). |
| Experience | The average experience score for site traffic over the configured time range, based on probes sent on the unecrypted out-of-tunnel last mile connection. |
| Round-Trip Latency | Average round-trip time between the site and the Cato Cloud over the time range, measured outside the tunnel. The graph shows round-trip latency over time. |
| Packet Loss | Average packet loss between the site and the Cato Cloud over the time range, measured outside the tunnel. The graph shows packet loss over time. |

#### Last Mile Overlay

The following table describes the information shown in the **Performance View: Last Mile Overlay** table.

| Item | Description |
| --- | --- |
| Site Name | Name of the site defined in the Cato Management Application (CMA). |
| Interface | The connected Socket interface. |
| Experience | The average experience score for last mile traffic sent on the interface over the configured time range, based on probes sent inside the tunnel. |
| Round-Trip Latency | Average round-trip time between the site and the Cato Cloud over the time range, measured inside the tunnel. |
| Packet Loss (Up) / Packet Loss (Down) | Average upstream or downstream packet loss between the site and the Cato Cloud over the time range, measured inside the tunnel. |
| Discards (Up) / Discards (Down) | Percentage of packets that were received but not processed for upstream or downstream traffic, measured inside the tunnel. |
| Throughput (Up) / Throughput (Down) | Average upstream or downstream throughput inside the tunnel over the time range. The graph shows throughput over time. |
| Tunnel Age | Total time that the current DTLS tunnel between the Socket and the PoP is connected. |
| Jitter (Up) / Jitter (Down) | Average difference in time delay in milliseconds (ms) between upstream or downstream data packets over the configured time range. |

### Additional Remote and Office User Experience Metric Tables

The following table describes the information shown in the **Performance View: Device** table. For more information about the metrics, see the [The User Experience Monitoring Drill-Down Page (Remote and Office Users)](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users).

#### Device

| Item | Description |
| --- | --- |
| User Name | Name of the remote or office user. |
| Device Name | The user device name. |
| Experience | The average experience score for device performance based on the average device CPU usage (CPU Load) and memory usage (Memory Load) for the device over the configured time range. The score is calculated based on the least good result between the two metrics. |
| Max CPU | Maximum CPU usage for the user device over the configured time range. |
| Max Memory | Maximum memory usage for the user device over the configured time range. |

#### Wi-Fi

The following table describes the information shown in the **Performance View: Wi-Fi** table.

| Item | Description |
| --- | --- |
| User Name | Name of the remote or office user. |
| Device Name | The user device name. |
| Experience | The average experience score for wi-fi performance over the configured time range, based on the Signal Strength metric. |
| Signal Strength | The average wi-fi signal strength for the user over the configured time range. |
| SSID | Name of the wireless network the user is connected to. |

#### LAN Gateway

The following table describes the information shown in the **Performance View: LAN Gateway** table.

| Item | Description |
| --- | --- |
| User Name | Name of the remote or office user. |
| IP Address | IP address of the LAN gateway. |
| Experience | The average experience score for LAN gateway performance over the configured time range, based on the average packet loss and round-trip latency over the configured time range. The score is calculated based on the least good result between the two metrics. |
| Round-Trip Latency | Average round-trip time between the site and the Cato Cloud over the time range, measured inside the tunnel. |
| Packet Loss | The average percentage of packets lost inside the LAN gateway over the configured time range. |

#### Last Mile Overlay

The following table describes the information shown in the **Performance View: Last Mile Overlay** table.

| Item | Description |
| --- | --- |
| User Name | Name of the remote or office user. |
| Experience | The average experience score for last mile performance inside the tunnel over the configured time range, based on the average packet loss and round-trip latency. The score is calculated based on the least good result between the two metrics. |
| Round-Trip Latency | Average round-trip time between the site and the Cato Cloud over the time range, measured inside the tunnel. |
| Packet Loss | The average percentage of packets lost over the last mile inside the tunnel, averaged over the configured time range. |

### Additional Application Metric Tables

### Probes

The following table describes the information for probes for application traffic shown in the **Performance View: Probes** table.

| Item | Description |
| --- | --- |
| Site Name | Name of the site the probe is configured for. |
| Destination | Destination of the probe. |
| Probe Protocol | The protocol used by the probe. |
| Round-Trip Latency | Average round-trip time between the site and the destination over the time range, measured by the probe. |
| Packet Loss | The average percentage of packets lost between the site and destination over the time range, measured by the probe. |
