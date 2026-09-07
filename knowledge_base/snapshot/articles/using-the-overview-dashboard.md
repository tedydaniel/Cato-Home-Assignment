---
title: "Using the Overview Dashboard"
slug: "using-the-overview-dashboard"
updated: 2026-06-30T17:07:57Z
published: 2026-06-30T17:07:57Z
canonical: "knowledge.catonetworks.com/using-the-overview-dashboard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Overview Dashboard

The Overview dashboard displays a wide variety of widgets to help you analyze and review key information about your account, such as security risks, network traffic, and license information.

## Overview

You can review the Overview Dashboard to gain insights into security posture, user experience, and license usage to help you gain the most from Cato's visibility into your network and environment. The widgets let you easily drill down to the relevant dashboards and pages in the CMA to gain more information about each widget.

The Dashboard widgets help answer key questions, such as:

- Which sites generate the most traffic?
- Where are risky applications most active?
- How many sites are located in Europe?

![overview_dashboard_main.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29494448854685.jpeg)

## Getting Started with the Overview Dashboard

The Overview dashboard contains these sections:

- Overview
- Network
- Security
- Insights
- Map

**To show the Overview Dashboard:**

- From the navigation menu, click **Home > Overview**.

### Filtering the Overview Dashboard

You can choose to filter the Overview dashboard for greater granularity. After you configure the filter, the dashboard is automatically updated to show the analytics and data to match the new filter.

You can filter the data by specifying a time range of up to three months.

## Understanding the Overview Dashboard Widgets

This section describes the different widgets on the Overview dashboard.

### The Overview Widget

The Overview widget gives you a high-level summary of your account, displaying information about best practices, licenses, and remote users.

You can use this widget to quickly view if any of your sites are disconnected, and drill down to the Sites page to view the specific sites with that status.

![overview_dashboard_overview.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28315065344925.jpeg)

These are the metrics displayed in the **Overview** widget:

| Name | Description |
| --- | --- |
| Best Practices | The percentage of [best practice checks](/v1/docs/reviewing-posture-checks-for-your-account) your account has passed. |
| Sites | Total number of sites across your account broken down by status. You can click the statuses to drill down to the Sites page, filtered to display sites with the relevant status. |
| Remote Users | Total number of remote users across your account, as well as how many of them are currently connected. You can click the user statuses to drill down to a filtered version of the Users page, filtered to display users with the relevant status. |
| Licenses | Total number of pooled and site bandwidth licenses that are being used, compared with the total number of licenses or bandwidth in your account. You can click the statuses to drill down to a filtered version of the License page, filtered to display licenses with the relevant status. |

### The Network Widgets

The Network widgets provide information on the traffic and applications running on your account.

For example, you can use this widget to determine which sites are using an unusual amount of data, and investigate whether any users are downloading Netflix movies over your corporate network.

![overview_dashboard_network.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29494448934941.jpeg)

These are the **Network** widgets:

| Name | Description |
| --- | --- |
| Traffic | The max throughput over time that has flowed through the Cato Cloud for the configured time range and filter. Filter this widget based on sites or users, and drill down to the Network Overview dashboard to get more information. |
| Application Categories by Traffic | The amount of traffic from each [category](/v1/docs/working-with-categories) during the time range and filter. You can drill down to the [App Analytics page](/v1/docs/understanding-app-analytics) filtered by the time range in the Overview Dashboard, which contains more information about application and network usage for your entire account as well as for specific sites, users, and applications. |

### The Security Widgets

The Security widgets provide information on threats and risks to your account.

You can use this widget to see the threats for a site and evaluate their severity and scope by drilling down to the [Security Threats dashboard](/v1/docs/using-the-security-threats-dashboard).

![overview_dashboard_security.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28315067453853.jpeg)

These are the **Security** widgets:

| Name | Description |
| --- | --- |
| Threat Events | The total number of detected threats and the distribution of threat types during the time range and filter. You can filter the widget to see which sites, users, or hosts have the most threats in general, or the most threats of a particular type (such as suspicious activity). |
| Risky Applications | The total number of risky applications and a graph of the apps according to their risk. The graph also displays the bandwidth used by each application. You can drill down to the App Activity dashboard to view more detailed information. |

### The Insights Widgets

The Insights widgets provide a taste of Cato's more advanced capabilities. The widgets display information from paid services, but you can get a high-level sneak peek here even if you have not yet purchased those services. You can view information about which devices are connected to your network, a summary of your potential threats to your network, and an overview of your users' experience with different applications.

For example, you can use the **Experience Monitoring** widget to identify applications with poor user experience and drill down to the [Experience Monitoring page](/v1/docs/using-the-experience-monitoring-page) to investigate the source of the problem.

![overview_dashboard_insights.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29494449022109.jpeg)

These are the **Insights** widgets:

| Name | Description |
| --- | --- |
| Devices | A summary of all devices connected to your network, broken down by device type. You can drill down to the [Device Inventory page](/docs/using-the-overview-dashboard#UUID-55380749-2cc5-f238-8773-46c5f78f4ff6) to view more details. |
| XOps Stories Summary | A summary of the Stories Dashboard, including the number of open stories, unique stories, and your Risk Score. You can drill down to the [Stories Overview page](https://support.catonetworks.com/document/preview/90659#UUID-9620929f-3d28-a300-ee40-2d5f525bd0d2) for more information. |
| Experience Monitoring | A summary of the experience score for applications used in your account, indicating the network performance users experience when using each application. You can drill down to the [Experience Monitoring page](/v1/docs/using-the-experience-monitoring-page) for more information. |

### The Licenses Widgets

The Licenses widgets display a summary of your licenses and services.

![overview_dashboard_licenses.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29494403629853.jpeg)

These are the Licenses widgets:

| Name | Description |
| --- | --- |
| License Usage | Displays the usage and total licenses in your account, such as site licenses and remote user licenses. You can drill down to the Licenses page **Bandwidth** tab to view more details. |
| Services | Displays the services that you have purchased and enabled, as well as the services that you have purchased but not yet enabled. You can drill down to the Licenses page **Service** tab to view more details. |

### The Map Widget

The map widget provides an overview of the geographical location of your sites and users. View the status of sites and users, focusing on current connectivity status, traffic volume, threat events, or connectivity over time.

![map_widget2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32004179481757.png)

| Name | Description |
| --- | --- |
| Map | Define which data is displayed by selecting an **indication**: - Current Connectivity Status. You can filter this data based on the status using the filter button. - Connectivity Over Time (data for Users only) - Total Threat Events. You can filter this data to only view blocked or unblocked (monitored and allowed) threat events. - Total Traffic Volume If you are viewing sites, this widget always shows the current sites in your account and is not impacted by the time range filter. **Note:** Users may be represented more than once if they moved locations within the selected time frame. |
| Summary Pane | Displays an overview of the indication you selected, broken down by country. |

## Known Limitation

- Total Threat Events shows all security events and doesn't filter for ​​**Not blocked​​**
