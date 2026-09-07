---
title: "Application HTTP Latency Anomaly for ISP Egress IPs"
slug: "application-http-latency-anomaly-for-isp-egress-ips"
updated: 2026-07-12T17:23:32Z
published: 2026-07-12T17:23:32Z
canonical: "knowledge.catonetworks.com/application-http-latency-anomaly-for-isp-egress-ips"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Application HTTP Latency Anomaly for ISP Egress IPs

This playbook describes the steps to investigate and resolve application HTTP latency issues affecting traffic from ISP egress IPs for remote users.

## Overview

An **Application HTTP Latency Anomaly for ISP Egress IPs** story indicates that HTTP latency for a specific application increased significantly for traffic exiting through a specific ISP egress IP.

This story is relevant for **user-sourced traffic** and helps identify whether the degradation is related to a specific ISP link, site path, application, or external service.

## Verify HTTP Latency

### Using the Story Drill-Down

1. From the navigation menu, click **Home > Stories Workbench**.
2. In the filter bar, add a filter set to **Producer Name in Experience Anomaly**.
3. Add the filter **Indication Contains Application HTTP Latency Anomaly for ISP Egress IPs**.
![01_HTTP_lat.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_HTTP_lat.png){height="" width=""}


4. Verify that a story was generated.

![02_HTTP_lat.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_HTTP_lat.png){height="" width=""}


5. Click the story row to open the drill-down page and review the incident details.

 ![03_HTTP_lat.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_HTTP_lat.png){height="" width=""}


6. Note the affected **application** and **ISP Egress IP**.
7. Review the incident timeline to determine when the anomaly started and whether the degradation is ongoing or intermittent.

## Troubleshooting Steps

### Review Application Performance

1. Open the **Home > Experience Monitoring** page.
2. Filter the data for the user, affected application, and ISP Egress IP.
3. Review the **HTTP Latency** and **HTTP/S Error Rate** metrics during the incident timeframe.
4. Compare the HTTP Latency trend with the story timeline.

If the **HTTP/S Error Rate** increases together with HTTP Latency, verify whether the application provider has reported a service degradation or whether the backend application is experiencing issues.

If only HTTP Latency increases while the **HTTP/S Error Rate** remains stable, the degradation is likely related to the network path rather than the application itself.

If multiple ISP Egress IPs experience increased HTTP Latency for the same application, verify whether the application provider has reported a widespread service degradation.

### Review User Metrics

In the **Experience Monitoring** page, review the users associated with the affected ISP egress IP during the incident timeframe.

Review the following metrics:

- CPU utilization
- Memory utilization
- Wi-Fi signal quality
- Packet Loss to the LAN Gateway
- Distance to the LAN Gateway
- Packet Loss to the PoP
- Distance to the PoP

Compare these metrics with the HTTP Latency timeline.

If multiple users show increased packet loss or latency at the same time as the HTTP Latency anomaly, investigate whether the ISP or Internet path is experiencing degradation.

If only one or a small number of users show degraded metrics, investigate those users' local network connectivity and endpoint performance.

### Review Traceroute Results

Open the **Connection Details** widget for one or more affected users and review the available traceroute results for the destination application.

Review the traceroute results for:

- Packet loss
- Increased latency
- Route changes
- Other network abnormalities

If packet loss or increased latency is observed before traffic reaches the Cato PoP, investigate the user's local network or ISP connectivity.

If the path to the PoP is healthy while HTTP Latency remains elevated, investigate the destination application or verify whether the SaaS provider has reported a service degradation.

 **Note:** Traceroute metrics are available only with Windows Client v6.10 or later and macOS Client v5.14 or later.

### Review Endpoint Performance

If no issues are identified in the previous steps, proceed to [Cato SDP Client Performance Troubleshooting](https://support.catonetworks.com/hc/en-us/articles/360012713038-Cato-SDP-Client-Performance-Troubleshooting) and investigate potential endpoint-related causes.

## Raising Cases to Cato Support

If following this playbook has not resolved the issue, submit a [Support ticket](https://support.catonetworks.com/hc/en-us/articles/360017066338-Submitting-a-Support-Ticket). To help Cato Support investigate the issue efficiently, include the results of the troubleshooting steps you performed.
