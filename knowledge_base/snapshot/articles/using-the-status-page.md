---
title: "Using the Status Page"
slug: "using-the-status-page"
updated: 2026-06-24T11:30:20Z
published: 2026-06-24T11:30:20Z
canonical: "knowledge.catonetworks.com/using-the-status-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Status Page

This article explains how to use the Status Page in the Cato Management Application (CMA) for an overview of status and performance for Cato PoPs, and PoP service health for the connected sites and users.

## Overview

The Cato Cloud is a global network of PoPs, with each PoP serving as a cloud location that contains multiple processing servers for customer traffic and security services. Your sites and remote users connect to specific processing servers within a PoP.

### Investigating Service Impact

If you experience service issues for sites or remote users, you can use the CMA Status Page to investigate the service health of the PoP resources that your account is using. The page helps you identify whether connected PoPs show indications of high processing-server load, elevated resource usage, or maintenance that can affect service quality.

A workload indication for a PoP does not necessarily mean that Cato identified an incident, or that a specific site, remote user, application, or service is down. It reflects a temporary condition on the processing servers that handle traffic for your account assets. When you see a workload indication, check whether the experience for your sites or remote users is impacted. For example, use Digital Experience Monitoring (DEM), monitoring pages and data to help validate the issue. If there is an impact, include the relevant information from the CMA Status Page when you open a Support ticket.

### CMA Status Page vs Public Cato Networks Services Status Website

Cato also provides a public website that reports validated platform-level incidents, maintenance events, and issues that Cato identifies as impacting multiple customers: Cato Networks Services Status ([status.catonetworks.com](http://status.catonetworks.com)). Cato Networks Services Status reflects the overall health of a PoP location across the platform and can include issues beyond processing-server load, such as PoP internet egress health. The CMA Status Page displays notifications from the public page, so you can compare platform-level status with the service health of the PoP resources that your account is using.

The CMA Status Page and public Cato Networks Services Status show the same status for a PoP location, because the CMA Status Page is based on the public page. However, the CMA Status Page includes additional information about the specific PoP resources for your sites and users. For example, the Cato Networks Services Status website can show a PoP as operational for all customers, while the CMA Status Page shows **Service Health** issues for the same PoP.

The Status Page shows real-time data based on a rolling 10-minute window.

### Checking Service Impact with DEM

The Cato Experience Monitoring (DEM) service lets admins use the [Home > Experience Monitoring page](/v1/docs/using-the-experience-monitoring-page) to check whether sites or remote users are experiencing service degradation during the workload indication. Each tab shows assets with degraded experience and lets you drill down to specific performance issues.

- **Sites** tab - Check packet loss, increased latency, jitter, discards, or reduced throughput
- **Remote Users** tab - Check packet loss, increased latency, Wi-Fi issues, or high CPU or memory usage
- **Office Users** tab - Check LAN, Wi-Fi, device, or last-mile performance issues
- **Applications** tab - Check whether business-critical applications degraded during the same time as the workload indication

### Use Case

ExampleCorp's New York site is connected to the New York PoP and is experiencing packet loss issues. Their NOC team has ruled out possible causes such as ISP last mile or Socket issues, and wants to investigate further. In the Status Page, the team sees that there is an ongoing technical incident in the New York PoP. Checking again a few minutes later, the team observes that the PoP returned to optimal service and the issue is resolved.

## Getting Started with the Status Page

**To show the Status Page:**

- From the navigation menu, click **Network** > **Status Page**.

## Understanding the Service Status Data

This section describes the service status information shown on the Status Page.

![Status_Page.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32266096939421.png)

### The Status Summary Bar

The status summary bar at the top of the page provides a high-level view of aggregated statistics for the PoP in use by account sites and users. The metrics show service status information for customer assets such as sites or users, as well as the number of PoPs experiencing a technical incident or under maintenance.

- You can add items in the bar to the page filter. For example, click on **Possibly Affected** in the **Service Health** section to filter the page to show PoPs with connected sites experiencing potential service issues.

![Status_page_summary_bar.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32266097062301.png)

These are the metrics shown:

- **PoPs in Use** - Shows the number of PoPs in use by the account out of the total number of Cato PoPs, and the status for all PoPs. These are the statuses:
  - **Up** - PoP is operating in an optimal manner
  - **Affected** - PoP is experiencing performance issues
  - **Down** - PoP is experiencing service disruption
- **Service Health** -
  - **Connected Sites** - Indicates if sites are affected by congestion or load in the PoP servicing the site. For example, a site connected to a PoP experiencing high CPU load for service to this site will be shown as **Possibly Affected**. When a site is shown as **Healthy** this indicates that the PoP is servicing the site in an optimal manner.

**Notes:**
    - **Service Health** is distinct from [site connectivity status](/v1/docs/connectivity-statuses-for-cato-sites). Connectivity status (for example, **Degraded**) relates to connectivity between the site and PoP, while **Service Health** relates to PoP performance in servicing this site
    - Customer sites that appear in the [Sites](/v1/docs/working-with-sites) page as **Connected** or **Degraded** are shown in the page, while sites that are **Disconnected** aren't included
  - **Connected Remote Users** - Indicates if users connecting with the Client are affected by congestion or load in the PoP they are connected to.
- **Under Maintenance** - Number of PoPs currently undergoing general operational maintenance. Includes only PoPs included in the current [filter](/v1/docs/using-the-status-page#h_01KV2RQ13MZEH18TNC7SG00NGS).
- **With Incidents** - Number of PoPs currently experiencing a technical incident. Includes only PoPs included in the current [filter](/v1/docs/using-the-status-page#h_01KV2RQ13MZEH18TNC7SG00NGS). The incidents are general operational incidents and not necessarily related to service for your account.

### The PoP Table

The PoP table shows status summary data for each PoP. By default, the table is filtered to show only PoPs in use by your account sites or remote users. PoPs experiencing perfomance issues or technical incidents are listed first, and PoPs with service health issues for sites or users are also prioritized in the table. PoPs undergoing maintenance appear with a maintenance icon next to the PoP name. You can hover the mouse over an item to show a menu to add or exclude it from the table filter.

![Status_Page_PoP_Table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982093646493(1).png)

#### Filtering the Table Data

To focus on the most important information, the PoP table is filtered by default to show the PoPs currently in use by account sites and users. You can further filter the table data to quickly pinpoint information related to specific PoPs, affected sites or users, and more. This helps you perform efficient troubleshooting. For more information on using the filter bar to show specific data, see [Filtering Data on a Page](/v1/docs/filtering-data-on-a-page).

![Status_Page_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32266096800029.png)

#### Understanding the PoP Table Data

These are the columns shown in the PoP table:

- **PoP Name** - Name of the PoP as it appears in the CMA
- **Country** - The country where the PoP is physically located
- **PoP Status** - Service status for the PoP. Possible values are **Up**, **Affected**, or **Down**.
- **PoP Usage** - Indicates whether the PoP is being used by account sites or remote users
- **Incidents** - Indicates whether the PoP is currently experiencing technical incidents.
  - Hover the mouse over the incident icon to see the number of incidents and the incident ID numbers. Click on an incident to view the incident information in the [Cato status webpage](https://status.catonetworks.com/)
- **Sites Service Health** - Shows the total number of account sites connected to the PoP, with a health bar showing healthy (green) versus possibly affected (yellow) sites.
  - Hover the mouse on the health bar to show the numbers of healthy and possibly affected sites
  - Click on the number to open a panel showing the account sites connected to the PoP, including the service health status and country for each site.
    - Click a site to open the [Network Analytics](/v1/docs/showing-the-site-network-analytics) page for the site.

![Status_Page_Site_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32266081942813.png)
- **Remote Users Service Health** - Shows the total number of account remote users connected to the PoP, with a health bar showing healthy (green) versus possibly affected (yellow) users.
  - Hover the mouse on the health bar to show the numbers of healthy and possibly affected users
  - Click on the number to open a panel showing the account users connected to the PoP, including the service health status and country for each user.
    - Click a user to open the general settings page for the user.

![Status_Page_User_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982109472797(1).png)
