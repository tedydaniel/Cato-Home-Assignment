---
title: "Using the Data Protection Inline Dashboard"
slug: "using-the-data-protection-inline-dashboard"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/using-the-data-protection-inline-dashboard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Data Protection Inline Dashboard

This article discusses how to use the Data Protection Inline dashboard to get a quick overview of data related violations and events in your network. You can then drill-down and analyze the threat types and easily open the relevant events.

## Overview of Data Protection Inline Dashboard

The Data Protection Inline dashboard lets you view the data and content related activity in your network based on the data control policies. The page contains several widgets that provide visibility for the different data violation criteria. The page also lets you filter according to a specific time frame to drill-down and focus on the relevant data violations and events in your account.

### Getting Started with the Data Protection Inline Dashboard

The Data Protection Inline dashboard shows the total number of data violations over the time range.

**To show the** **Data Protection Inline** **dashboard:**

- To access the Data Protection Inline dashboard, from the navigation menu, click **Security > Data Protection**. Inline data is displayed on the **Inline Protection** tab.

For more information about using the dashboard, see [Configuring Filters to Analyze Dashboard Data](/v1/docs/configuring-filters-to-analyze-dashboard-data) and [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter). The maximum date range for the dashboard is 90 days.

![DLP_Dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24898494374045.png)

## Working with Data Protection Inline Dashboard Widgets

The Data Protection Inline dashboard widgets give you a high-level overview of data control violations in your network.

### Understanding the Data Protection Inline Widgets

The Data Protection Inline widgets provide information about the data violations detected by the DLP engines. These are the DLP widgets:

- **Top Violating Rules** - Shows the top data control rules in the Application Control page according to the rule name and the number of events for each one.
- **Events Violations Over Time** - Shows the number of data violations over the time frame. You can filter the widget by:

Use the mouse to select a smaller time range for the threat data, the page is automatically updated.
  - Rule name - select the data control rule that is shown in the widget.
  - Application - select the applications that are shown in the widget (only shows applications that were actually used during the time frame).
- **Events by Actions** – Shows the percentage of events based on the rule actions.

Hover over the widget to show the absolute number of events.
- **Events by Severity** – Shows the number of events based on the severity for the Data Control rules.
- **Event Violations by Sites** - Map of the top physical site locations with the number of events per site.
- **Top Hosts** - Shows a list of the top hosts (source IP address) with the number of DLP violation events for each host.
- **Top Violations by Data Profile** - Shows a list of top DLP Content Profiles with the number of DLP violation events for each profile.
- **Top Violations by File Properties** - Shows a list of top Content Types for Data Control rules with the number of DLP violation events.
