---
title: "Application Response Time Anomaly for Sites"
slug: "application-response-time-anomaly-for-sites"
updated: 2026-07-12T17:31:03Z
published: 2026-07-12T17:31:03Z
canonical: "knowledge.catonetworks.com/application-response-time-anomaly-for-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Application Response Time Anomaly for Sites

This playbook describes the steps to investigate and resolve Application Response Time issues affecting sites.

## Overview

Application Response Time measures the **Time to First Byte (TTFB)** between a site and an application. Increased response time can be caused by application-side degradation, WAN connectivity issues, ISP problems, congestion, and issues within the site's local network.

This playbook helps identify the source of the degradation using the **Cato Management Application (CMA)** before contacting Cato Support.

## Verify Application Response Time

The following methods can be used by a CMA admin to verify that an **Application Response Time Anomaly** occurred for a site.

### Using the Story Drill-Down

1. From the navigation menu, click **Home > Stories Workbench**.
2. In the filter bar, add a filter set to **Producer Name in Experience Anomaly**.
3. Add the filter **Indication Is Application Response Time Anomaly for Sites**.

![01_App_Response_anomaly.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_App_Response_anomaly.png){height="" width=""}


4. Verify that a story was generated.

![02_App_Response_anomaly.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_App_Response_anomaly.png){height="" width=""}


5. Click the story row to open the drill-down page and review the incident details, including the timeline, affected entity, and application.

![03_App_Response_anomaly.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_App_Response_anomaly.png){height="" width=""}


6. Review the incident timeline to determine whether the issue is ongoing or intermittent.

### Filter for Related Events

In the **Home > Events** page, apply the following filters:

- **Sub-Type** is **Anomaly**
- **Event Message** contains **Application Response Time**

![04_App_Response_anomaly.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/04_App_Response_anomaly.png){height="" width=""}


Verify that anomaly events were generated during the reported timeframe.

## Troubleshooting Steps

### Review Application Performance

1. Open the **Home > Experience Monitoring** page.
2. Filter the data for the affected site and application.
3. Review the **Time to First Byte (TTFB)** and **HTTP/S Error Rate** metrics during the incident timeframe.
4. Compare the TTFB trend with the story timeline to determine whether the degradation is ongoing or intermittent.

If the **HTTP/S Error Rate** increases together with TTFB, verify whether the application provider has reported a service degradation or whether the backend application is experiencing issues.

If only TTFB is elevated while the **HTTP/S Error Rate** remains stable, the application is responding more slowly than usual but is still serving requests. For self-hosted applications, verify the health of the application server and backend infrastructure.

If multiple sites experience increased TTFB for the same application, verify whether the application provider has reported a widespread service degradation.

### Review Site Metrics

In the **Experience Monitoring** page, review the following site metrics during the incident timeframe:

- Packet Loss to the PoP
- Distance to the PoP

Compare these metrics with the TTFB timeline.

If **Packet Loss to the PoP** or **Distance to the PoP** increases together with TTFB, investigate the site's Internet connectivity or contact the ISP if the issue persists.

If the network metrics remain stable while TTFB increases, the degradation is likely application-related rather than network-related.

### Review Connection Details

Review the **Connection Details** widget and examine the traceroute results for:

- Packet loss
- Increased latency
- Route changes
- Other network abnormalities

If packet loss or increased latency is observed before traffic reaches the Cato PoP, investigate the site's local network or ISP connectivity.

If the path to the PoP is healthy while TTFB remains elevated, investigate the hosted application or verify whether the SaaS provider has reported a service degradation.

If no issues were found up to this point, proceed to [Performance Issues for Socket Sites Troubleshooting](https://support.catonetworks.com/hc/en-us/articles/16461575157533-Performance-Issues-for-Socket-Sites-Troubleshooting) for further troubleshooting.

## Raising Cases to Cato Support

If following this playbook has not resolved the issue, submit a [Support ticket](https://support.catonetworks.com/hc/en-us/articles/360017066338-Submitting-a-Support-Ticket). To help Cato Support investigate the issue efficiently, include the results of the troubleshooting steps you performed.
