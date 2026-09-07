---
title: "Using the Endpoint Protection Dashboard"
slug: "using-the-endpoint-protection-dashboard"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/using-the-endpoint-protection-dashboard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Endpoint Protection Dashboard

This article discusses how to use the Endpoint Protection (EPP) Dashboard to get a quick overview of threats detected by EPP in your network.

## Overview

The EPP Dashboard lets you view the malicious and suspicious threat activity in your network detected by the EPP engines. The page contains a number of widgets that provide visibility for threat activity and the impacted users. The page also lets you add items to the threats filter to drill-down and focus on the relevant threat data and events in your account. For more information about Cato's EPP solution, see [Getting Started with Cato's Endpoint Protection (EPP)](/v1/docs/getting-started-with-cato-s-endpoint-protection-epp).

## Getting Started with the Endpoint Protection Dashboard

The Endpoint Protection Dashboard page shows the total threat activity over the time range.

![EPP_Dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275726506909.png)

**To show the Endpoint Protection Dashboard:**

- From the navigation menu, click **Monitoring > Endpoint Protection Dashboard**.

For more information about using the dashboard, see [Configuring Filters to Analyze Dashboard Data](/v1/docs/configuring-filters-to-analyze-dashboard-data) and [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter). The maximum date range for the dashboard is 90 days.

| Name | Description |
| --- | --- |
| Total Endpoints | The number of endpoints protected by Cato's EPP solution. |
| Assigned Licenses | The percentage of of EPP licenses that have been used. |
| Total Threats Found | The number of threats found on all endpoints. |
| Total Files Quarantined | The number of files quarantined on all endpoints. |
| Time Range | The time range applied to the page. |
| Top Threats | The most common threats detected on your endpoints. |
| Threats per Day | The number of threats detected per day. |
| Threats by Detection Engine | The number of threats detected by each EPP detection engine. |
| Top Threatened Users | The users with the highest number of threats detected on their endpoint. |
| Top Malicious Files | The most common malicious files detected on your endpoints. |
| Top Malicious Hashes | The most common file hashes detected on your endpoints. |
| Version Distribution per Endpoint | The number of each EPP agent version installed on your endpoints. |

## Viewing Events from the Endpoint Protection Dashboard

To further analyze threats identified by EPP, you can view the events for items within a widget. For example, you can view the events of a threatened user.

**To view events from the Endpoint Protection Dashboard:**

1. Click the menu icon (![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275719551005.png)) next to the item you are viewing the events of.
2. Click **View Events**.

The **Events** page is displayed with a pre-defined filter of item and time frame from the EPP Dashboard.
