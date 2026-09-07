---
title: "Drilling-Down and Analyzing XOps Predictive Insight Stories"
slug: "drilling-down-and-analyzing-xops-predictive-insight-stories"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/drilling-down-and-analyzing-xops-predictive-insight-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Drilling-Down and Analyzing XOps Predictive Insight Stories

This article discusses how you can use the Stories Workbench to review Predictive Insight stories for connectivity and performance issues on your network.

> [!NOTE]
> Note:
> 
> XOps is Cato’s unified analytics layer for security and operations, offering insights and guided remediation. XOps has replaced XDR, for more information, see [XOps FAQ](/v1/docs/xops-faq).

## Overview

Cato XOps uses predictive analytics to identify potential performance and availability risks across your network. The Predictive Insight engine analyzes traffic patterns, resource utilization, and configuration context to forecast developing issues before they impact service. For example, if a site’s Socket CPU is expected to exceed acceptable operating levels, a story is triggered with relevant forecast data and suggested actions.

The Stories Workbench page shows the details of each Predictive Insight story to help you assess and address emerging risks. You can filter and group stories to focus on the most urgent forecasts, review trend visualizations, and follow guided remediation steps through the playbook for the story.

### Predictive Insight Story Indications

The Predictive Insight engine currently generates stories for the following issues:

| Indication | Description | Threshold for Generating a Story |
| --- | --- | --- |
| **CPU Usage Nearing Full Capacity** | A Socket for a site is forecasted to exceed acceptable utilization levels. The **Forecast** graph for this story (see below, [Understanding the Story Drill-Down Widgets](/v1/docs/drilling-down-and-analyzing-xops-predictive-insight-stories#understanding-the-story-drilldown-widgets)) is based on the maximum CPU usage recorded for each hour at the site. To smooth short-term spikes and highlight longer-term trends, the graph applies a 7-day rolling average to these hourly maximum values. The rolling average is calculated using up to 90 days of historical data, providing sufficient context for trend analysis and forecasting. | Socket is forecast to exceed 90% CPU usage in the near future. |
| ​**Event Volume Approaching Quota Limit** | Detects when event volume is likely to exceed limits based on the account’s DPA license. Limits are defined per plan and subtype (1 Data Unit = 2.5M events), with terms varying by DPA version. Trends are smoothed over time, and predictions are used to identify potential breaches in advance. | The account event count is forecast to exceed a subtype limit (based on DPA license and data units) in the near future. |

## Showing the Stories Workbench Page

The Stories Workbench page shows a summary of the Predictive Insight stories for your account.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For more about using the Stories Workbench page, see [Reviewing Site Operations Stories](/v1/docs/reviewing-site-operations-stories).

## Drilling-Down and Analyzing Stories

You can click on a story in the Stories Workbench to drill-down and investigate the details in a different page. This page contains a number of widgets that help you evaluate the emerging issue identified by the Predictive Insight engine.

![CPU_Nearing_Capacity_Drilldown.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33311688269853.png)

### Understanding the Story Drill-Down Widgets

These are the story drill-down widgets:

| Name | Description |
| --- | --- |
| **Story summary** | At the top of the page there is a summary of basic information about the story, including: - The story type (indication) - The producer that generated the story - The source of the story - The story's criticality |
| **Story timeline** | Shows a timeline of changes in the story status |
| **Details** | Basic information for analyzing the story, including the time of the first signal for the story, when the story was created, the story ID number, and other relevant information. For example, for a **CPU Nearing Full Capacity** story, the site name, connection type, and relevant CPU core number are shown. |
| **Forecast** | A graph that visualizes historical trends and projected future behavior for the predicted metric. It is based on the maximum value observed per hour, which highlights peak conditions rather than averages. To reduce noise and expose sustained patterns, the widget applies a rolling average over a 7-day window, calculated from up to 90 days of historical data. The graph displays the historical data alongside a projected trend and forecast range, which represents the expected variability of the prediction. A threshold line indicates the level at which the predicted condition becomes actionable, helping you understand when and how likely the forecasted event is to occur. |
| **Root Cause Analysis** | AI generates an analysis for the story by automatically executing the investigative steps of a playbook to help identify the root cause of issues. |
