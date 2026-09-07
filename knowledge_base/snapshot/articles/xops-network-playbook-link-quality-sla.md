---
title: "XOps Network Playbook - Link Quality SLA"
slug: "xops-network-playbook-link-quality-sla"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-link-quality-sla"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - Link Quality SLA

This playbook describes steps to resolve issues when there is an issue with the link quality SLA for a site.

## Overview

Poor network conditions between a site and its connected PoP can disrupt traffic and affect connectivity or the reliability of critical services. Cato constantly monitors the link quality SLA KPIs between a site and the PoP based on configured thresholds. If there is an link quality issue that surpasses these configured thresholds, a Last-Mile Quality event with the **Alert** action is generated. The when the issue is resolved, another event with the **Clear Alert** action is generated.

Each Link Quality rule can monitor one or more of these thresholds:

- Packet Loss
- Jitter
- Latency
- Congestion

For more information please view [Monitoring Link Quality with Health Rules](/v1/docs/working-with-link-health-rules).

There are different ways to discover that a Link Quality issue has occurred:

- Go to the **Stories Workbench** page and use the **Site Operations** preset to find the **Link quality SLA** stories.

![quality_sla.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32752937810845.jpeg)

The story provides information about the current status, incident timeline, and more.
- Connectivity alert, sent as an email notification to the Admin group.
- Connectivity event, with the Last-Mile Quality sub-type and the action **Alert**

## 

## Step 1 - Verifying the Link Quality Is Impacted

This section discusses different Cato tools that you can use to identify the scale and impact of your link SLA quality issue. Often times, an issue with one of the metrics can lead to issues with other metrics. For example, what might start as a congestion issue, can lead to problems with jitter and packet loss.

### Reviewing Site Network Analytics

Use the [Network Analytics](https://support.catonetworks.com/hc/articles/4413265630865#UUID-5f7c2b38-7d46-9caa-6c46-64ccbc62fb7c) page for a site to determine the cause for the link quality issue. Network Analytics can help you determine which link is experiencing quality issues, if the issue is on the upstream or downstream connection, and how changes in quality of your last mile links affects traffic within Cato tunnels.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19329503345181.png)

Above is an example of Network Analytics displaying quality issues. Note the packet loss reported on the tunnel connection. You can alter the timeframe to see how this impact is felt over time.

## 

## (Optional) Step 2 - Review Ping & Traceroute data

To check whether the issue is related to your ISP, open the Actions menu in the top‑right corner of the Story and select Export data to ISP template. Choose the relevant time range and link, then review the ping and traceroute results provided. ![ping_result.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32752947357213.jpeg)![mtr_result.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32752937815709.jpeg)

**Note:** Ping and Traceroute probes are sent from the socket directly to the PoP (out of tunnel).

if the results show a problem, export the test data and open a support case with your local ISP. If no issues are detected, continue to the next step.

## Step 3 - Troubleshooting Link Quality Issues

Please follow our playbook for [Socket Site Tunnel Connectivity Troubleshooting](/v1/docs/socket-site-tunnel-connectivity-troubleshooting).

## 

## Raising cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
