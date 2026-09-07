---
title: "Drilling-Down and Analyzing App Activities Stories"
slug: "drilling-down-and-analyzing-app-activities-stories"
updated: 2026-08-10T13:18:03Z
published: 2026-08-10T13:18:03Z
canonical: "knowledge.catonetworks.com/drilling-down-and-analyzing-app-activities-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Drilling-Down and Analyzing App Activities Stories

## Overview

XOps App Activities stories help you identify risky and anomalous activity in sanctioned SaaS applications. By analyzing activity data collected through [App Activities integrations](/v1/docs/what-is-application-control-via-api-with-app-activities), XOps detects suspicious behavior and generates stories that help you investigate potential security incidents.

These stories provide visibility into user actions performed directly in cloud applications, including activity from users who aren't connected to the Cato Cloud. Each story contains details about the relevant users, activities, and application to help you understand the context of the activity and determine if remediation is required.

App Activities stories are supported for GitHub, Microsoft 365, Slack, and Google Workspace.

### Prerequisties

- To generate App Activities stories, your account must have XOps and CASB licenses, and the relevant App Activities integrations must be configured.

## Showing the Stories Workbench Page

The Stories Workbench page shows a summary of the App Activities stories for your account. For App Activities stories, the **Producer Type** is **Generic Incident** and **Producer Name** is the app name.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For more about using the Stories Workbench page, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(170).png)

### Understanding the Story Drill-Down Widgets

These are the story drill-down widgets:

| Name | Description |
| --- | --- |
| **Story summary** | At the top of the page there is a summary of basic information about the story, including: - The story type (indication) - The producer that generated the story - The story's criticality - Details such as the story's first signal and duration |
| **Details** | Basic information for analyzing the story, including the time of the first signal for the story, when the story was created, the story ID number, and other relevant information such as the vendor and product name for the app. |
| **Timeline** | Shows a timeline of changes in the story status |
| **Entities** | The entities where the stories occurred. These could be Users, Sites, Data stores, applications, etc. |
| **Evidence** | Supporting evidence for the story. |
| **Raw Data** | Dynamic table containing the raw events that generated the story. |
