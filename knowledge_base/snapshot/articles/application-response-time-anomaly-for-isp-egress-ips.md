---
title: "Application Response Time Anomaly for ISP Egress IPs"
slug: "application-response-time-anomaly-for-isp-egress-ips"
updated: 2026-07-12T17:18:50Z
published: 2026-07-12T17:18:50Z
canonical: "knowledge.catonetworks.com/application-response-time-anomaly-for-isp-egress-ips"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Application Response Time Anomaly for ISP Egress IPs

This playbook describes the steps to investigate and resolve Application Response Time issues affecting ISP egress IPs for remote users.

## Overview

An **Application Response Time Anomaly for an ISP Egress IP** indicates that the Time to First Byte (TTFB) for a specific application has increased significantly for traffic exiting through a specific ISP egress IP.

Because the anomaly is associated with an ISP egress IP, it represents the experience of one or more remote users using the same ISP path to access the application. This playbook helps determine whether the degradation is caused by the user's network path, the ISP, or the application itself.

## Verify Application Response Time

### Using the Story Drill-Down

1. From the navigation menu, click **Home > Stories Workbench**.
2. In the filter bar, add a filter set to **Producer Name in Experience Anomaly**.
3. Add the filter **Indication is Application Response Time Anomaly for ISP Egress IPs**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_App_response_time.png)
4. Verify that a story was generated. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_App_response_time.png)
5. Click in the row of the story to open the drill-down page to review the incident details. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_App_response_time.png)
6. Review the incident timeline to determine whether the degradation is ongoing or intermittent.

### Filter for Related Events

In the **Home >** **Events** page, apply the following filters:

- **Sub-Type** **is** **Anomaly**
- **Event Message** **contains** **Time anomalies in applications for ISP Egress IPs**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/04_App_response_time.png)

Verify that anomaly events were generated during the reported timeframe.

## Troubleshooting Steps

### Review Application Performance

1. Open the **Home > Experience Monitoring** page.
2. Filter the data for the affected **application** and **ISP Egress IP**.
3. Review the **Time to First Byte (TTFB)** and **HTTP/S Error Rate** metrics during the incident timeframe.
4. Compare the TTFB trend with the story timeline.

If the HTTP/S Error Rate increases together with TTFB, verify whether the application provider has reported a service degradation or whether the backend application is experiencing issues.

If only TTFB is elevated while the HTTP/S Error Rate remains stable, the application is responding more slowly than usual but is still serving requests.

If multiple ISP Egress IPs experience increased TTFB for the same application, verify whether the application provider has reported a widespread service degradation.

### Review User Metrics

In the Experience Monitoring page, review the users associated with the affected ISP egress IP during the incident timeframe.

Review the following metrics:

- CPU utilization
- Memory utilization
- Wi-Fi signal quality
- Packet Loss to the Lan Gateway
- Distance to the Lan Gateway
- Packet Loss to the PoP
- Distance to the PoP

Compare these metrics with the TTFB timeline.

If multiple users show increased packet loss or latency at the same time as the TTFB anomaly, investigate whether the ISP or Internet path is experiencing degradation.

If only one or a small number of users show degraded metrics, investigate those users' local network connectivity and endpoint performance.

### Review Traceroute Results

Open the **Connection Details** widget for one or more affected users and review the available traceroute results for the destination application.

Review the traceroute results for:

- Packet loss
- Increased latency
- Route changes
- Other network abnormalities

If packet loss or increased latency is observed before traffic reaches the Cato PoP, investigate the users' ISP connectivity or local network.

If the path to the PoP is healthy while TTFB remains elevated, investigate the destination application or verify whether the SaaS provider has reported a service degradation.

**Note:** Traceroute metrics are available only with Windows Client v6.10 or later and macOS Client v5.14 or later.

### Compare Other ISP Egress IPs

Use the Experience Monitoring page to compare the affected application across different ISP egress IPs.

If only one ISP egress IP shows elevated TTFB, the issue is likely isolated to that ISP or Internet path.

If multiple ISP egress IPs show elevated TTFB for the same application, the issue is more likely related to the application or SaaS provider.

If multiple applications show increased TTFB for the same ISP egress IP, investigate a possible ISP or network-path issue.

### Review Endpoint Performance

If no issues are identified in the previous steps, proceed to [Cato SDP Client Performance Troubleshooting](https://support.catonetworks.com/hc/en-us/articles/360012713038-Cato-SDP-Client-Performance-Troubleshooting) investigate potential endpoint-related causes.

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](https://support.catonetworks.com/hc/en-us/articles/360017066338-Submitting-a-Support-Ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
