---
title: "XOps Network Playbook - CPU Usage Nearing Full Capacity"
slug: "xops-network-playbook-cpu-usage-nearing-full-capacity"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-cpu-usage-nearing-full-capacity"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - CPU Usage Nearing Full Capacity

## Overview

High socket CPU usage can occur for several reasons, including normal load conditions or the socket operating near its throughput capacity. Identifying the source of this behavior is important for maintaining stable site performance. This playbook walks you through a story in which your site experiences elevated socket CPU usage and outlines the key checks needed to determine whether the socket is approaching its operational limits.

## Step 1 - Verify Current CPU Usage

The following are the different ways that the Cato Management Application admin can verify current CPU usage.

### Using the Story Drill-down

- An XOps story will be generated when the socket CPU is predicted to go above 85%.
- Go to the **Stories Workbench** page and use the Network Operations preset, including the filter 'Indication **Contains** CPU**'.** Adjust the time frame as necessary. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32835417907229.png)
- Verify if a story is generated as shown below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32835417908125.png)
- Click on the story to drill down into the details. It information showing the current CPU load by timeline, and, more importantly, prediction for when the CPU usage will reach 90%. ![socket_cpu.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32835429375773.jpeg)

### Socket Web UI

In Socket UI, browse to the HW Status tab to check the current CPU load. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32787272145693.png)

### Socket Site Network Analytics

In the Cato Management Application, navigate to the Site Network Analytics and select the Hardware tab to view the current and historical CPU load.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32787272146205.png)

## Step 2 - Troubleshooting high CPU Levels

### Socket Resource Limitations

High CPU usage can occur when the socket is operating at or near its maximum throughput capacity. To check whether this is the cause, review the current throughput using the site [network analytics](/v1/docs/showing-the-site-network-analytics) section throughput graphs and compare it to the limits defined for your specific socket type. These limits are listed in the [Socket Resource Limitations](/v1/docs/performance-issues-for-socket-sites-troubleshooting). If your throughput is approaching these values, it indicates the socket is close to running at full capacity, which explains the elevated CPU utilization.

Review site [App Analytics](/v1/docs/understanding-app-analytics) tab for the time CPU levels were elevated to find if its related to a burst of a specific traffic that was originated from one or several hosts. if this is not a one-time event consider applying bypass or select a non-Cato transport for this traffic.

### Applying LAN FW Policy

When site throughput and Socket CPU usage are already close to the socket limit, adding the site under LAN Firewall settings and applying policy may contribute to increased resource usage. This may result in the Socket approaching its maximum supported throughput or increase the socket CPU above 90%. To confirm review events from the relevant timeframe and search for events with Sub-Type is LAN Firewall

### 

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
