---
title: "Using the Data Protection API Dashboard"
slug: "using-the-data-protection-api-dashboard"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/using-the-data-protection-api-dashboard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Data Protection API Dashboard

This article discusses how to use the Data Protection API Dashboard to get a quick overview of violations and events related to the App & Data API Protection policy. You can then drill-down and analyze the threat types and easily open the relevant events.

> [!NOTE]
> Note:
> 
> Please contact [SaaSecAPI@catonetworks.com](mailto:SaaSecAPI@catonetworks.com) or your official Cato reseller for more information about using the Data Protection API Dashboard.

## Overview of Data Protection API Dashboard

The Data Protection API Dashboard lets you view the data and content-related activity for the connectors that you configured for your account. The page contains several widgets that provide visibility for the different data violation criteria for the specific connectors in Data Protection rules (Security > App & Data API Protection > Data Protection) and for the general SaaS app traffic. The page also lets you add items to the dashboard filter to drill-down and focus on the relevant data violation information and events in your account.

### Getting Started with the Data Protection API Dashboard

The Data Protection API Dashboard shows the total number of data violations and SaaS app events over the time range.

![SaaS_API_Dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24898005173789.png)

### Selecting the Time Range

The default time range for the data violations is the previous two days. You can select a different time range for the Data Protection API Dashboard to show a longer or shorter time period. For more information, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter).

The maximum date range for the **Data Protection API Dashboard** is 90 days.

## Configuring Filters to Analyze Data Protection API Data

There are two ways to filter the data in the Data Protection API Dashboard and show the items that are most relevant: automatically update the filter with the selected item, or manually configure the filter.

### Automatically Filtering for an Item

As you hover over an item or field where a filter option is available, the ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24898039249181.png) button appears. Click the icon to show the filter options:

- **Add to Filter** - Adds the item to the filter, and the dashboard now only shows data that includes this item. For example, if you filter for a specific activity, the page only shows data that is related to that activity. No other Data Protection API data is available until you change or clear the filter.
- **Exclude from Filter** - Updates the filter to exclude this item, and the dashboard now only shows data that does NOT include this item.
- **View Events** - Adds this item to the filter, and the Events page opens and shows all the events that match the filter.

You can continue to add items to the filter, click ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24898039249181.png) again to update the filter and drill-down further.

### Manually Configuring the Filter

You can manually configure the filter for greater granularity to analyze the SaaS API data control violations. After you configure the filter, it is added to the filter bar and the page is automatically updated to show the Data Protection API data that matches the new filter.

![SaaS_Security_Manual_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24898021904797.png)

**To manually configure a filter:**

1. In the filter bar, click the plus symbol.
2. Start typing or select the **Field**.
3. Select the **Operator**, which determines the relationship between the **Field** and the **Value** you are searching for.
4. Select the **Value**.
5. Click **Add Filter**. The filter is added to the filter bar and the **Data Protection API Dashboard** is updated to show results based on the filters.

### Clearing the Filter

You can remove each item in the filter separately, or clear the entire filter.

![SaaS_Security_API_Dashboard_Remove_Filter_callout.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24898005512093.png)

1. To clear a single filter, click the X next to the filter (item 1 above).
2. To clear all the filters, click X at the right end of the filter bar (item 2 above).

## Working with Data Protection API Dashboard Widgets

The Data Protection API Dashboard widgets give you a high-level overview of Data Protection rule violations and connector related events for SaaS app traffic.

### Understanding the Data Protection API Widgets

The Data Protection API widgets provide information about the data violations detected by the Data Protection API engines. These are the Data Protection API widgets:

- **Top Violating Rules** - Shows the top Data Protection rules according to the rule name and the number of events for each one.

Click a rule to open the **Events** page and show the prefiltered events for the rule and time range.
- **Events by Activity/Sharing Options** – Shows the number of events based on the **Activity** and **Sharing Options** defined for the rules.

Click an activity or sharing option to open the **Events** page and show the prefiltered events for the item and time range.
- **Events by Severity** – Shows the number of events based on the severity for the Data Control rules.

Click a severity to open the **Events** page and show the prefiltered events for the severity and time range.
- **Events by Actions** - The number of events for each rule action.

Click an action to open the **Events** page and show the prefiltered events for the action and time range.
- **Events Over Time** - Shows the number of connector-related events over the time frame. You can filter the widget by:

Use the mouse to select a smaller time range for the threat data, the page is automatically updated.
  - Rule name - select the Data Protection rule that is shown in the widget.
  - App connector - select the connector that are shown in the widget (only shows connectors that were actually used during the time frame).
- **Top Owners** - Shows a list of the top owners and users with the number of Data Protection API violation events for each owner.
- **Top Violations by Data Profile** - Shows a list of top DLP Content Profiles with the number of DLP violation events for each profile.

Click a Content Profile to open the **Events** page and show the prefiltered events for the profile and time range.
- **Top Violations by File Type** - Shows a list of top File Types for Data Control rules with the number of Data Protection API violation events for that file type.

Click a file type to open the **Events** page and show the prefiltered events for the file type and time range.
