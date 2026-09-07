---
title: "Application Response Time Anomaly for Remote Users"
slug: "application-response-time-anomaly-for-remote-users"
updated: 2026-07-12T18:21:41Z
published: 2026-07-12T18:21:41Z
canonical: "knowledge.catonetworks.com/application-response-time-anomaly-for-remote-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Application Response Time Anomaly for Remote Users

This playbook describes the steps to investigate and resolve Application Response Time issues affecting remote users connecting with the Client (SDP users).

## Overview

Application Response Time measures the **Time to First Byte (TTFB)** between the user and the application. Increased response time can be caused by network latency, application-side degradation, and endpoint connectivity issues. This playbook helps identify the source of the degradation before contacting Cato Support.

## Verify Application Response Time Anomaly

The following methods can be used by a **Cato Management Application (CMA)** admin to verify that an **Application Response Time Anomaly** occurred for remote users.

### Using the Story Drill-Down

1. From the navigation menu, click **Home > Stories Workbench**.
2. In the filter bar, add a filter set to **Producer Name in Experience Anomaly**.
3. Add the filter **Indication Contains Application Response Time Anomaly for SDP users**.

![01_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_App_Anomaly_Users.png){height="" width=""}


4. Verify that a story was generated.

![02_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_App_Anomaly_Users.png){height="" width=""}


5. Click the story row to open the drill-down page and review the incident details, including the timeline and affected user.

![03_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_App_Anomaly_Users.png){height="" width=""}


6. Review the incident timeline and the number of affected users to determine whether the issue is isolated to a single user or affects multiple users.

### Filter for Related Events

In the **Home > Events** page, apply the following filters:

- **Sub-Type** is **Anomaly**
- **Event Message** contains **Detects Response Time anomalies in applications for SDP users**

![04_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/04_App_Anomaly_Users.png){height="" width=""}


Verify that anomaly events were generated during the reported timeframe.

## Troubleshooting Steps

### Review Application Performance

1. Open the **Home > Experience Monitoring** page.
2. Filter the data for the affected users and applications.
3. Review the **Application Response Time Breakdown** and **HTTP/S Error Rate** metrics during the incident timeframe.
4. If multiple users experience increased response time for the same application, verify whether the application provider has reported a service degradation or outage.
5. For self-hosted applications, verify that there are no issues with the application server or the network where the application is hosted.
6. Compare the response time trend with the story timeline to determine whether the degradation is ongoing or intermittent.

### Review Related Network Metrics

In the **Experience Monitoring** page, review the user metrics for any degradation during the incident timeframe, such as:

- High CPU or memory utilization
- Poor Wi-Fi signal quality (if applicable)
- Increased packet loss or latency toward the host gateway
- Increased packet loss or latency toward the Cato PoP

Review the **Connection Details** widget and examine the traceroute results for:

- Packet loss
- Increased latency
- Route changes
- Other network abnormalities

Review whether these conditions coincide with the incident.

**Note:** Traceroute metrics are available only with Windows Client v6.10 or later and macOS Client v5.14 or later.

### Review Endpoint Performance

If no issues are identified in the previous steps, proceed to [Cato SDP Client Performance Troubleshooting](https://support.catonetworks.com/hc/en-us/articles/360012713038-Cato-SDP-Client-Performance-Troubleshooting) and investigate potential endpoint-related causes.

## Raising Cases to Cato Support

If following this playbook has not resolved the issue, submit a [Support ticket](https://support.catonetworks.com/hc/en-us/articles/360017066338-Submitting-a-Support-Ticket). To help Cato Support investigate the issue efficiently, include the results of the troubleshooting steps you performed.
