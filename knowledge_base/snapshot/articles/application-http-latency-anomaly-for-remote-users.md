---
title: "Application HTTP Latency Anomaly for Remote Users"
slug: "application-http-latency-anomaly-for-remote-users"
updated: 2026-07-12T18:26:21Z
published: 2026-07-12T18:26:21Z
canonical: "knowledge.catonetworks.com/application-http-latency-anomaly-for-remote-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Application HTTP Latency Anomaly for Remote Users

This playbook describes the steps to investigate and resolve HTTP latency issues affecting remote users connecting with the Client (SDP users).

## Overview

HTTP latency can be caused by a variety of factors, including network conditions, endpoint performance, and application responsiveness. This playbook helps identify the root cause and determine the appropriate mitigation.

## Verify HTTP Latency

The following methods can be used by a **Cato Management Application (CMA)** administrator to verify that an **HTTP Latency Anomaly** occurred for remote users.

### Using the Story Drill-Down

1. From the navigation menu, click **Home > Stories Workbench**.
2. In the filter bar, add a filter set to **Producer Name in Experience Anomaly**.
3. Add the filter **Indication in Application HTTP Latency Anomaly for SDP users**.

![01_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_App_Anomaly_Users(1).png){height="" width=""}


4. Verify that a story was generated.

![02_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_App_Anomaly_Users(1).png){height="" width=""}


5. Click the story row to open the drill-down page and review the incident details, including the timeline and affected users.

![03_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_App_Anomaly_Users(1).png){height="" width=""}


6. Review the incident timeline and the number of affected users to determine when the incident started and whether it is isolated or widespread.

### Filter for Related Events

In the **Home > Events** page, apply the following filters:

- **Sub-Type** is **Anomaly**
- **Event Message** contains **HTTP Latency**

![04_App_Anomaly_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/04_App_Anomaly_Users(1).png){height="" width=""}


Verify that anomaly events were generated during the reported timeframe.

## Troubleshooting Steps

### Review Application Performance

1. Open the **Home > Experience Monitoring** page.
2. Filter the data for the affected users and applications.
3. Review the application performance metrics and determine whether increased HTTP latency correlates with the incident timeline.

### Review Related Network Metrics

In the **Experience Monitoring** page, review the user metrics for any degradation during the incident timeframe, such as:

- High CPU or memory utilization
- Poor Wi-Fi signal quality (if applicable)
- Increased packet loss or latency toward the host gateway
- Increased packet loss or latency toward the Cato PoP

Review the **Connection Details** widget and examine the traceroute results for:

- Packet loss
- Increased latency
- Other network abnormalities

Review whether these conditions coincide with the incident.

**Note:** Traceroute metrics are available only with Windows Client v6.10 or later and macOS Client v5.14 or later.

### Review Endpoint Performance

If no issues are identified in the previous steps, proceed to [Cato SDP Client Performance Troubleshooting](https://support.catonetworks.com/hc/en-us/articles/360012713038-Cato-SDP-Client-Performance-Troubleshooting) and investigate potential endpoint-related causes.

## Raising Cases to Cato Support

If following this playbook has not resolved the issue, submit a [Support ticket](https://support.catonetworks.com/hc/en-us/articles/360017066338-Submitting-a-Support-Ticket). To help Cato Support investigate the issue efficiently, include the results of the troubleshooting steps you performed.
