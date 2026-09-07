---
title: "Monitoring App Connectors"
slug: "monitoring-app-connectors"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/monitoring-app-connectors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring App Connectors

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Physical and virtual App Connectors connect your private applications to the Cato Cloud. Use the Network Analytics page to monitor App Connector availability, throughput, transport quality, and hardware load. This page helps you determine whether the connector is connected, carrying traffic, experiencing packet loss or discards, or under CPU pressure during the selected time range.

Use the **Site & Tunnels** tab to monitor traffic behavior and the **Hardware** tab to monitor CPU utilization over time.

## Monitor App Connector Throughput

### Show App Connector Site & Tunnels

![NEW_app_connector_monitoring.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809671621405.png)

**To monitor App Connector throughput in the Site & Tunnels tab:**

1. From the navigation menu, select **Access > App Connectors**.
2. Select the relevant App Connector.
3. Click **Network Analytics**, and then select the **Site & Tunnels** tab.

### Review Throughput Metrics

This section explains how to use the Sites & Tunnels tab to review connector availability, traffic levels, and transport quality for the selected time range.

- **Connector Status:** Shows whether the connector is currently connected and available to carry traffic
  - Troubleshooting example: If users report that apps are unreachable, first check whether the connector has connectivity
- **Avg Throughput:** Shows the average upstream and downstream traffic, which helps you verify that the connector handled traffic and understand the overall traffic pattern.
  - Troubleshooting example: If users reported activity, but the throughput is unexpectedly low, traffic might not have used this connector at that time
- **Avg. Packet Loss:** Shows the average upstream and downstream packet loss, which helps you identify transport quality issues that can affect application performance and session stability
  - Troubleshooting example: If users report slow performance or unstable sessions, check whether packet loss is elevated during the relevant time range
- **Avg. Discards:** Shows the average upstream and downstream discarded traffic, which helps you identify whether traffic was dropped instead of forwarded successfully
  - Troubleshooting example: If application sessions fail or degrade during busy periods, review discards together with throughput to see whether traffic quality was impacted

## Monitor App Connector Hardware

### Show the Hardware Page

![app_connector_monitoring_hardware.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809648340381.png)

**To monitor App Connector hardware metrics:**

1. From the navigation menu, select **Access > App Connectors**.
2. Select the relevant App Connector.
3. Click **Network Analytics**, and then select the **Hardware** tab.

### Review Hardware Metrics

Use this procedure to review the App Connector CPU utilization and determine whether physical or virtual hardware resources were under pressure during the selected time range.

- **Avg. CPU:** Shows the average CPU utilization for the connector, which helps you determine whether the connector was under sustained hardware load
  - Troubleshooting example: If throughput increases at the same time that CPU remains elevated, the connector might be approaching capacity limits
- **CPU Load:** Shows CPU utilization over time for each core, which helps you see whether CPU activity was steady, briefly elevated, or sustained
  - Troubleshooting example: If users reported intermittent slowness, review the graph for sustained periods of higher CPU utilization during the relevant time window
