---
title: "Reviewing Detection & Response XOps Stories in the Stories Workbench"
slug: "reviewing-detection-response-xops-stories-in-the-stories-workbench"
updated: 2026-07-23T12:30:37Z
published: 2026-07-23T12:30:37Z
canonical: "knowledge.catonetworks.com/reviewing-detection-response-xops-stories-in-the-stories-workbench"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reviewing Detection & Response XOps Stories in the Stories Workbench

This article discusses how you can use the Stories Workbench to review stories for potential threats in your account.

## Overview of Detection & Response Stories

Cato Detection & Response is an additional layer of security that creates stories for threats. When Cato’s advanced correlation engines analyze traffic data and find a match for a potential threat, they generate a story. The story contains data from traffic flows with common properties that relate to the same threat. The Stories Workbench page shows the details of each story to help you understand and analyze the threats. You can sort and filter the stories to find the most important potential attacks, and then drill-down on a story to further investigate the details.

These are examples of data that a story can include:

- Sources in your network
- External targets of network traffic
- Identification and description of the threat
- Relevant geolocations
- Related applications
- Relevant events
- Popularity of the target according to Cato internal data
- Malicious score of the target according to Cato machine learning models

### Required Licenses

- Additional licenses may be required. For more information, see [Welcome to the Cato XOps Service](/v1/docs/welcome-to-the-cato-xops-service)

## Showing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

### Understanding the Stories Columns

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/workbench.png)

| Column | Description |
| --- | --- |
| Indication | Indicator of attack associated with the story. For more information, see [Using the Indications Catalog](/v1/docs/using-the-indications-catalog) |
| Criticality | Cato's risk analysis score for the story, from 1 to 10 |
| Source | Device, user, or other entity in your network involved in the story |
| Producer Type | Category of the producer that generated the signal associated with the story. |
| Producer Name | Name of the product, integration, or security engine that generated the story data |
| Created | Date and time the story was created |
| Updated | Date and time the story was most recently updated |
| Occurrences | Number of times the issue occurred, including recurrences after a temporary resolution. |
| Link Name | Name of the WAN link associated with the source device or traffic in the story |
| Provider (ISP) | Internet service provider (ISP) associated with the network link in the story |
| Investigation Status | Current stage of the investigation for the story |
| Status | - Pending Customer - The story was sent to the customer and is waiting for a response - Pending Analyst - The story is waiting for more information from a security analyst - Closed - A security analyst closed the story |
| Labels | Label Cato assigned to the story to help categorize and filter it |
| Muted | Indicates whether the story is muted in the Stories Workbench |
| ID | Unique Cato ID for the story |
| First Signal | Date and time of the earliest signal associated with the story |
| Indication ID | Unique identifier used by Cato's XOps engines to reference a specific indication |
| Severity | Severity assigned to the original signal by the producer or vendor |
| Vendor | Vendor that generated the original signal associated with the story |
| Source IP | IP address of the source entity involved with the story |
| Mitigation | Mitigation action associated with the story |
| Correlation ID | Identifier used to link and track the lifecycle of XOps stories across ITSM platforms |
| Last Comment | Most recent comment added to the story |

## Grouping the Stories

To provide context when reviewing the stories, you can show the stories in groups defined by details including **Source**, **Indication**, **Status**, and **Type**. For example, you can show together all of the stories related to a specific source IP address or all of the Cybersquatting stories. This gives you a broader perspective when analyzing the stories, and can help you reach faster and more accurate conclusions.

Each group highlights the criticality levels for the stories in that group, including the number of high, medium, and low criticality stories.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/group_stories.png)

**To group the stories in the Stories Workbench:**

1. From the navigation menu, click **Home > Stories Workbench**.
2. From the **Group By** drop-down menu, select the required criterion.

The stories are shown in expandable groups.

## Filtering the Stories

There are three ways to filter the data in the Stories Workbench:

- Select a preset filter
- Automatically update the filter with a selected item
- Manually configure the filter

### Preset Filters

You can select a preset filter to focus on either **Network Operations** or **Security Operations** stories. When you select a preset filter, the story columns most relevant for that type of story are shown by default.

**To select a preset filter:**

1. In the filter bar, click the **Select Presets** dropdown menu.
2. Select the preset. The Stories Workbench is updated to show the stories that match the preset.

### Automatically Filtering for an Item

As you hover over an item or field where a filter option is available, the ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356127603997.png) button appears. Click the icon to show the filter options:

- **Add to Filter** - Adds the item to the filter, and the Stories Workbench now only shows stories that include this item. For example, if you filter for a specific Criticality score, the page only shows stories with that Criticality.
- **Exclude from Filter** - Updates the filter to exclude this item, and the Stories Workbench now only shows stories that do NOT include this item.

You can continue to add items to the filter, click ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356127603997.png) again to update the filter and drill-down further.

### Selecting the Time Range

The default time range for the Stories Workbench is the previous two days. You can select a different time range to show a longer or shorter time period. For more information, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter).

The maximum date range for the Stories Workbench is 90 days.

### Manually Configuring the Filter

You can manually configure the story filter for greater granularity to analyze the stories. After you configure the filter, it is added to the stories filter bar, and the page is automatically updated to show the stories that match the new filter.

**To create a filter:**

1. In the filter bar, click the add button.
2. Start typing or select the **Field**.
3. Select the **Operator**, which determines the relationship between the **Field** and the **Value** you are searching for.
4. Select the **Value**.
5. Click **Add Filter**. The filter is added to the filter bar and the **Stories Workbench** is updated to show stories based on the filters.

### Clearing the Filter

You can remove each item in the filter separately, or clear the entire filter.

**To clear the filters for the Stories Workbench page:**

1. To clear a single filter, click the remove button next to the filter.
2. To clear all the filters, click X at the right end of the filter bar.
