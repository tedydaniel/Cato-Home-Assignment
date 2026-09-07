---
title: "The Application Experience Monitoring Drill-Down Page"
slug: "the-application-experience-monitoring-drill-down-page"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/the-application-experience-monitoring-drill-down-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# The Application Experience Monitoring Drill-Down Page

This article explains how to use the Application Experience Monitoring drill-down page to analyze performance and user experience for a site.

For more about reviewing analytics on the Experience Monitoring page, see [Understanding the Experience Monitoring Drill-Down Pages](/v1/docs/understanding-the-experience-monitoring-drill-down-pages).

## Overview

When you click on a specific application in the Experience Monitoring page, an Application Experience Monitoring drill-down page opens with data for that application. The page shows a set of widgets customized to help analyze traffic for the application. The following sections describe the widgets shown on the page.

![Application_Experience_Monitoring_Drilldown.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29319159512605.png)

## The Application Experience Monitoring Widgets

These are the widgets shown for drilling down and analyzing application experience monitoring data:

- Application summary - The widget at the top of the page shows the following information about the application:
  - **App** name
  - **Security Risk** - Risk score for the application (Cato provides a risk score for each application from 0 (no risk) to 10 (very high risk). The risk score is calculated based on the analysis of millions of data flows.

For more information about applications and your Cato account, see [Using the App Catalog](/v1/docs/using-the-app-catalog).
  - **Category** - The Cato system category that the application belongs to. For more about categories, see [Working with Categories](/v1/docs/working-with-categories).
- **Application Experience Score** - Shows the site average experience score for the selected application (**Good**/ **Fair**/**Poor**), as well as a graph showing the application score over the configured time range

The average experience score is based on these application performance metrics:

Cato's AI-based algorithm creates unique thresholds for every app.

For more information about how Application Experience Score is calculated, see [this article](/v1/docs/what-is-cato-experience-monitoring).
  - Time to First byte
  - TCP Connect
  - TLS Connect
  - HTTP Latency
  - HTTP/S error
- **Application Performance** - This tab shows the following widgets:
  - **Time to First Byte** - Duration of time between the HTTP request and the receipt of the first byte
  - **TCP Connect** - Time taken to establish a TCP connection
  - **TLS Connect** - Time taken to establish a TLS connection
  - **HTTP/S Latency** - Duration of time between the request and the response
  - **HTTP/S Error Rate** - Percentage of HTTP errors
- **Remote Users**, **Office Users**, **Site Hosts** - These tabs show a list of users or hosts currently working with the selected application, including usage statistics and connection information, such as the country from which they're connecting and through which PoP. You can also click on a user or host to open the drill-down page for that entity
