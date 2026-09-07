---
title: "Using the Access Overview Page"
slug: "using-the-access-overview-page"
updated: 2026-08-02T13:22:23Z
published: 2026-08-02T13:22:23Z
canonical: "knowledge.catonetworks.com/using-the-access-overview-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Access Overview Page

## Using the Access Overview Page

This article discusses how to use the Access Overview page to analyze how users connect to the Cato Cloud across your account.

## Overview

Access Overview helps you understand how users are connecting to your network and whether their access behavior matches your policies. You can see how users connect, which resources and applications they access, and whether traffic is allowed, blocked, monitored, or handled by RBI.

Use the page to identify unusual access patterns, such as users connecting through unexpected PoPs, a high number of blocked events, or remote users with no network access. You can also review connection methods, Client versions, policy enforcement, Always-On bypass activity, and geographic access trends.

The page helps you answer questions such as:

- How are users accessing the network
- Which resources are users accessing, such as WAN or Internet
- Which applications are users accessing
- Which PoPs are users connecting to, and are they connecting to the expected PoPs based on their location
- Are policies blocking more traffic than expected
- Which Client versions are users running
- How often are users bypassing the Always-On Policy

## Use Cases for Access Overview

### Analyzing Access to WAN Applications

An admin wants to understand how users access private applications over the WAN. For example, the admin may need to confirm whether users are connecting with the expected access methods, such as Cato Client, Enterprise Browser, Browser Extension, or through a site.

In **User Flows Analysis**, the admin changes the flow view to show applications. Then, the admin adds **Destination Type: WAN** as a filter to focus only on flows to WAN-based applications.

The filtered view shows how users access WAN applications, which PoPs the traffic flows through, and which applications users access. This helps the admin identify unexpected access methods, unusual PoP selection, or application access patterns that don’t match the organization’s policies.

## Getting Started with Access Overview

To show the Access Overview page:

From the navigation menu, click **Access > Access Overview**.

When you add a filter, the data on the Access Overview page updates across the widgets, except for the top ribbon. The top ribbon always shows recently connected users based on activity in the last 10 minutes.

For more information about filtering dashboard data and configuring the time range, see [Configuring Filters to Analyze Dashboard Data](/v1/docs/configuring-filters-to-analyze-dashboard-data) and [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter).

The maximum date range for the Access Overview page is 90 days.

## Understanding the Top Ribbon

The top ribbon shows recently connected users across the account. This data is not affected by filters that you apply to the page.

| Item | Description |
| --- | --- |
| Recently Connected | Shows the number of unique users with activity in the last 10 minutes, based on events generated from Cato policies |
| Remote | Shows how many recently connected users connected remotely |
| Remote access methods | Shows the number of recently connected users by access method, such as Cato Client, Enterprise Browser, Browser Extension, and Clientless App Portal |
| Site | Shows how many recently connected users connected from a site |
| Best Practices | Shows the percentage of completed best practice checks and lets you resolve open checks |

## Understanding the Analysis Section

The Analysis section includes the **User Flows Analysis** diagram. The diagram helps you visualize how users access your network, which PoPs they connect to, which resources they use, and which applications they access.

Each column in the diagram represents a stage in the flow. The bands between the columns show how events move between stages. Wider bands indicate higher event volume.

You can interact with the diagram in these ways:

- Hover over a band or item to show event details, including the number of events and unique users
- Click an item in the flow to add it as a filter
- Use the flow selector to change the analysis view
- Use the **Source by** drop-down menu to group the source by connection origin or country

| Flow View | Description |
| --- | --- |
| Source > PoP > Destination Type > Action | Shows how users access WAN and Internet resources, and whether the traffic was allowed, blocked, monitored, or handled by RBI |
| Source > PoP > Destination Type > Applications | Shows which applications users access, and how application traffic flows through PoPs and destination types |

## Understanding the Connectivity Section

The Connectivity section shows how users connect and what level of network access they receive.

| Widget | Description |
| --- | --- |
| Connected Remote Users By Network Access | Shows the number of remote users by network access permission, such as WAN and Internet or No Access |
| Users Connected Over Time | Shows the number of remote users and site users connected over time |
| View Client Connectivity Policy | Opens the Client Connectivity Policy page |

## Understanding the Access Methods Section

The Access Methods section shows how users access the Cato Cloud and which operating systems they use.

| Widget | Description |
| --- | --- |
| Cato Agents | Shows access requests by Cato agent type, such as Cato Client |
| Agent and OS filters | Lets you filter the widget by agent type and operating system |
| OS distribution | Shows access requests by operating system for the selected agent type |
| View Client Management | Opens the Client Management page |

## Understanding the Enforcement Section

The Enforcement section shows policy hit counts and Always-On bypass activity.

| Widget | Description |
| --- | --- |
| Hit Count | Shows the number of allowed or blocked events for the selected policy |
| Policy filter | Lets you select the policy type, such as Client Connectivity Policy |
| Group by filter | Lets you group the hit count by a dimension, such as Rule Name |
| Action filter | Lets you show allowed or blocked events |
| View Client Connectivity Policy | Opens the Client Connectivity Policy page |
| Always-On Bypass | Shows Always-On bypass events over time |
| View Always-On Policy | Opens the Always-On Policy page |

## Understanding the Map Section

The Map section shows the geographic distribution of users and sites. You can use the map to review where users connect from and identify unexpected access patterns.

| Widget | Description |
| --- | --- |
| Map | Shows user or site locations on the map |
| User and site toggle | Lets you switch the map between users and sites |
| Users by Country | Shows the number of users by country |
| Zoom controls | Lets you zoom in or out of the map |

## Viewing Events from Access Overview

To further analyze user connections, you can drill down from a widget and view the relevant events. The Events page opens with a predefined filter for the selected item and uses the time frame from the Access Overview page.

The Device ID is gathered for hosts connected by Clients that are not in office mode. For Windows Clients, this is the MAC address of the device. For macOS Clients, this is the UUID of the device.

To view events from the Access Overview page:

1. Click the menu icon next to the item you are viewing events for.
2. Click **View Events**.

The Events page opens with the relevant predefined filter.
