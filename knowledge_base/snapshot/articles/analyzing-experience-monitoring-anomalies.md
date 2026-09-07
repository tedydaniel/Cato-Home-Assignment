---
title: "Analyzing Experience Monitoring Anomalies"
slug: "analyzing-experience-monitoring-anomalies"
updated: 2026-07-05T12:53:19Z
published: 2026-07-05T12:53:19Z
canonical: "knowledge.catonetworks.com/analyzing-experience-monitoring-anomalies"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyzing Experience Monitoring Anomalies

This article explains how to use the XOps Stories Workbench and story drill-down page to analyze XOps stories for anomalous behavior detected by the Experience Monitoring Anomaly engine.

For more about using the Stories Workbench, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).

## Overview

Cato's XOps service detects anomalous activities based on Experience Monitoring, which may indicate an issue with an application or network performance to an application. The Anomaly engine monitors and analyzes the network traffic of each site and each application for an initial period of 14 days to establish a baseline for each new application based on the TTFB (Time to First Byte).

After that period, the engine runs once a day on the data from the previous day and sees if there was a significant deviation from the baseline. In the event that an anomaly occurred, a story is generated.

> [!NOTE]
> Note:
> 
> If several deviations occur on the same day, only one story is generated for all of them.

Even after the baseline is established, it is a dynamic measurement that is updated with each day’s data. Meaning, the initial baseline is established after the first 14 days, but continues to evolve with the data from each new day.

When the anomaly engine generates a story, you can review it in the Stories Workbench and drill down for further analysis of the story data.

### Experience Anomaly Story Indications

These are the indications of anomalous behavior detected by the Experience Monitoring Anomaly engine to generate stories:

| Indication | Description |
| --- | --- |
| **Application Response Time Anomaly in Site** | Detects anomalies in the Time to First Byte (TTFB) metric for an application at a specific site. |
| **Potential Application Outage Due to Widespread HTTP Errors** | Detects anomalies in the ratio of HTTP failures to successes for specific applications in traffic across the Cato global backbone. |

## Drilling-Down and Analyzing Experience Monitoring Anomaly Stories

You can click on an Experience Anomaly story in the Stories Workbench to drill down and investigate the details on a different page. This page contains additional information to help you start your investigation of the incident.

### Showing an Experience Anomaly Story

Click an Experience Anomaly story in the Stories Workbench page to show the details for the UEBA story.

**To view the Stories Workbench page:**

1. From the navigation menu, click **Home > Stories Workbench**.
2. Under **Producer**, select **Experience Anomaly**.

### Understanding the Experience Anomaly Widgets

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Experience Monitoring Anomalies New.png)

These are the widgets for an Experience Anomaly story:

| Name | Description |
| --- | --- |
| Story summary | At the top of the page, the story summary shows basic information about the story, including: - Indication for the detected issue - The producer that generated the story - Source site where the story occurred - Application with which the site was communicating - Story status |
| Story timeline | Under the story summary, the timeline shows changes in the story status |
| Details | Basic details about the story, including: - A description and summary - **First Signal** - Time of the first signal (traffic flow) associated with the anomaly - **Creation Date** - Time the story was generated - **Last Updated** - Time of the latest story update, such as a new target or changed verdict - **Similar Stories** - Shows stories with similar details such as site and application. - **Criticality** - The potential impact of the issue on your network. Values are from 1 (low impact) to 10 (high impact) |
| Experience Anomaly | Visual representation of the application experience the day of the story |
| Entities | The entities where the story occurred. These could be users, sites, data stores, applications, etc. |
| Time to First Byte | Graph showing the duration between the HTTP request and the receipt of the first byte over time |
| Incident Timeline | A list of the detected events for issues and resolutions in the story. - Click **Event log** to show the [Events](/v1/docs/analyzing-events-in-your-network) page pre-filtered for the incident |
| Playbook Workflow | A step-by-step troubleshooting guide tailored to the specific issue detected in the story. This helps you quickly identify root causes and resolve the problem using clear, actionable plays. Includes links to relevant documentation. |

### Investigating Anomalies

Once you have the basic information of the anomaly, including the site on which it occurred, the application and time, you can use the Experience Monitoring widgets to further investigate the story.

For example, you can filter by application and, using the Application Performance tab, view more information about possible issues that occurred at the time of the anomaly. In addition, you can use the Tunnel tab to see if there was a problem with the tunnel, or maybe in the Hosts tab you can see that there was a sudden spike in the number of users who were accessing the application, which might have caused the experience to degrade.
