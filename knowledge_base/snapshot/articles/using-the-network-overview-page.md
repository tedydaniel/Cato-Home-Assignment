---
title: "Using the Network Overview Page"
slug: "using-the-network-overview-page"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/using-the-network-overview-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Network Overview Page

This article discusses how to use the Network Overview page to analyze how sites are connected to the Cato Cloud across your account.

## Overview of the Network Overview

The Network Overview page lets you view and analyze data for sites and links across the network. It includes widgets that you can use to drill down on usage data, throughput, packet loss, and more to analyze traffic across your entire account.

## Sample Network Overview Use Cases

These are some examples of how you can use the Network Overview pages to monitor your sites:

### Analyzing Bandwidth Usage Trends

You can use the Network Overview to analyze how data and throughput are used over a period of time. For example, if you want to monitor the usage for a sensitive LTE link, you can inspect its total throughput in the last hour or the last month.

### Identifying Top Performance Sites and Links

The Network Overview can provide you with a high-level overview of the network and help identify the top and lowest items for different traffic KPIs. For example, you can sort sites or links in descending order of packet loss to show the sites that experienced the most packet loss.

Another example is monitoring your bandwidth utilization, a site with high utilization may require increased site bandwidth.

## Getting Started with the Network Overview

The following section explains the widgets and metrics available in the Network Overview.

### Showing the Network Overview

**To show the** **Network Overview** **page:**

- From the navigation menu, click **Network > Network Overview**.

For more information about using the dashboard, see [Configuring Filters to Analyze Dashboard Data](/v1/docs/configuring-filters-to-analyze-dashboard-data) and [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter). The maximum date range for the dashboard is 90 days.

### Connectivity Summary Widgets

The Summary Bar displays a short summary of connectivity across your account.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25529562632605.png) |
| --- |

| Item | Description |
| --- | --- |
| Total Sites | Total number of sites in the account |
| Current Sites Connectivity | Shows the current status for sites as: - **Connected** to the Cato Cloud - **Disconnected** from the Cato Cloud - **Disabled** in the Cato Management Application |
| Connected SDP Users | Total number of SDP Users connected to the Cato Cloud |

### Account Throughput

The Account Throughput widget shows the average throughput consumption for sites and SDP users in the account. Use the filters to help analyze the data. For example, only show SDP user data, or group the data and compare traffic for sites vs. SDP users.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25529533638557.png)

Use the **Filter** for the Account Throughput widget to show the average throughput for the following data and analytics:

- Source type:
  - All sources
  - Sites
  - SDP Users
- Throughput direction:
  - Total Throughput
  - Upstream
  - Downstream
- Group by:
  - None - Shows combined average account upstream and downstream throughput for sites and SDP users
  - Direction - Shows separate upstream and downstream average throughput for site and SDP users
  - Source - Shows separate site and SDP user average throughput for combined upstream and downstream traffic

### Sites and Links Analytics

The **Sites** and **Links** section displays network data in an easy-to-read table. You can export the current view of the data to a CSV file (requires edit permissions). Also, you can group links by the service **Provider** with the **Group By** option.

The data in this widget can be shown as:

- Group by:
  - None - Shows combined average account upstream and downstream throughput for all links
  - Provider - Shows information about connectivity for all of your links for each Provider.
- Average - Data average based on the current timeframe
- Max - Maximum values (peak) during the timeframe (only for link analytics)

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25529541065117.png) |
| --- |

The following table explains the columns, not all columns are shown by default.

| Item | Description |
| --- | --- |
| Site Name | Name of site defined in Cato Management Application |
| Link ID | Link role (precedence) |
| Total bytes Upstream | Total upstream throughput |
| Total bytes Downstream | Total downstream throughput |
| Packet Loss Upstream | Packet loss for upstream traffic **Note:** For throughput that is less than 1bps, packet loss is shown as 0% |
| Packet Loss downstream | Packet loss for downstream traffic **Note:** For throughput that is less than 1bps, packet loss is shown as 0% |
| Packets Discarded Upstream | Upstream packets discarded by QoS |
| Packets Discarded Downstream | Downstream packets discarded by QoS |
| Throughput Upstream | Total throughput for upstream traffic |
| Throughput Downstream | Total throughput for downstream traffic |
| Concurrent Hosts | Number of hosts connected to the site |
| Concurrent Flows | Number of flows for the site |
| Distance | Distance from site to the connected Cato PoP |
| Jitter upstream | Jitter for upstream traffic |
| Jitter downstream | Jitter for downstream traffic |
