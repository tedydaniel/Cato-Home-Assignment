---
title: "Using Traceroute for Path Analysis in Experience Monitoring"
slug: "using-traceroute-for-path-analysis-in-experience-monitoring"
status: "update"
updated: 2026-09-06T12:43:24Z
published: 2026-09-06T12:43:24Z
canonical: "knowledge.catonetworks.com/using-traceroute-for-path-analysis-in-experience-monitoring"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Traceroute for Path Analysis in Experience Monitoring

This article explains how to use Traceroute data in the Experience Monitoring drill-down pages to analyze experience degradation issues.

For more about reviewing analytics on the Experience Monitoring page, see [Understanding the Experience Monitoring Drill-Down Pages](/v1/docs/understanding-the-experience-monitoring-drill-down-pages).

## Overview

Cato Experience Monitoring lets you use Traceroute to investigate network path issues for both Socket site traffic and Client remote-user traffic. You can identify where packet loss or latency begins between a Socket or Client and the connected PoP, and from the PoP to configured application destinations. With continuous hop-by-hop monitoring, you can analyze packet loss and latency across the path and use historical traceroute data to troubleshoot intermittent issues and provide evidence when escalating to Internet Service Providers (ISPs).

The Path Analysis widget in the Experience Monitoring drill-down pages shows Traceroute data visualized as a diagram and in tabular form.

Traceroute data for Socket traffic is shown on the following Experience monitoring drill-down pages:

- [Site Experience Monitoring](/v1/docs/the-site-experience-monitoring-drill-down-page)
- [Office User Experience Monitoring](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users)
- [Host Experience Monitoring](/v1/docs/the-host-experience-monitoring-drill-down-page)

Traceroute data for Client traffic is shown on the [Remote User Experience Monitoring](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users) drill-down page.

![DEM_Traceroute_tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35029005178525.png)

### Probes for Traceroute Data

The Traceroute data shown is based on Traceroute probes configured in the Experience Monitoring Probes policy. The predefined **Underlay Path Trace** probe monitors the underlay path from the probe source, either a Socket or Client, to the connected PoP. You can configure separate probe intervals for Socket and user traffic. In addition, you can configure custom Traceroute probes for specific application destinations to monitor the path between the PoP and the application network. For more information about configuring probes, see [Configuring the Experience Monitoring Probes and Policy](/v1/docs/configuring-the-experience-monitoring-probes-and-policy).

The probes shown below include an example of a custom Traceroute probe for the Google application:

![Traceroute_probes.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35028955089053.png)

## Prerequisites

- For Socket Traceroute data:
  - Socket version 25 and higher
- For Client Traceroute data:
  - Windows Client v6.12 and higher
  - macOS Client v6.0.1 and higher

## Understanding the Traceroute Data

The **Traceroute** and **Command Line** tabs in the **Path Analysis** widget let you choose to show the Traceroute data as a user-friendly diagram or in a tabular format that resembles CLI Traceroute tools. Both tabs show data based on the same Traceroute probes.

### The Traceroute Tab

![Traceroute_tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35029018848285.png)

The **Traceroute** tab provides a visual representation of the network path between the source site and the destination. The diagram shows separate path sections for:

- **Last Mile Routes** from the Socket to the connected PoP
- **Application Routes** from the PoP to the application destination
  - For application path data you must configure a custom Traceroute Experience Monitoring probe for the application. For more information see [Configuring the Experience Monitoring Probes and Policy](/v1/docs/configuring-the-experience-monitoring-probes-and-policy).

Each hop in the path is displayed as a node in the diagram.

- Use the followng dropdown menus to select the data to display:
  - **Device Name** - In a High Availability configuration, select which Socket to show data for
  - **PoP Destination** - If a PoP change occurred during the configured time range, select which PoP to show data for
  - **Application Destination** - If Traceroute probes are configured for multiple applications, select the application to show data for
- Hover over a node to view detailed hop metrics
- Select a different time range to analyze historical path behavior
- Click **Show Full Traceroute Data** to open a panel that shows the Traceroute raw data with an option to copy the data. This panel shows data for all Socket links and connected PoPs (for example, if a PoP change occurred during the configured time range).

When the network path includes many hops, the diagram may collapse intermediate nodes for readability. Collapsed nodes appear as grouped indicators (for example **+5**) in the path. You can expand these nodes to reveal the hidden hops and review their metrics.

### The Command Line Tab

![Traceroute_Command_Line_tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35028988622877.png)

The **Command Line** tab provides a tabular representation of the traceroute data. This view presents the same traceroute results shown in the visual graph but in a format similar to CLI traceroute tools. The tab includes two sections:

- **Last Mile Hops** - The route from the Socket to the connected PoP
- **Application Hops** - The route from the PoP to the application destination
  - For application path data you must configure a custom Traceroute Experience Monitoring probe for the application. For more information see [Configuring the Experience Monitoring Probes and Policy](/v1/docs/configuring-the-experience-monitoring-probes-and-policy).

Each hop includes detailed Traceroute metrics that help you analyze path performance and identify the point where degradation begins.

These are the metrics shown in the **Command Line** tab:

- **TTL** - Hop number in the traceroute path
- **Hop IP** - IP address of the responding node
- **Location** - Detected geographic location (city and country code)
- **Loss%** - Packet loss observed for this hop
- **Snt** - Number of probes (packets) sent
- **Rcv** - Number of responses received
- **Avg** - Average round-trip latency
- **Best** - Lowest latency observed
- **Wrst** - Highest latency observed
- **StDev** - Latency variation across probes

## Recommended Practices for Troubleshooting with Traceroute

These are recommendations for effective troubleshooting using the different Traceroute metrics:

- When site connectivity or experience is degraded, use the last mile metrics to review the hops between the Socket and the PoP to identify where packet loss or latency increases. When analyzing last mile routes:

If packet loss or latency begins before the PoP, the issue is typically located in the local network or the last-mile ISP connection.
  - Identify the hop where packet loss or latency begins
  - Check whether the same behavior continues in downstream hops
  - Compare multiple WAN routes if the site uses multiple interfaces
- When degradation impacts a specific application, use the application Traceroute metrics to review the hops between the Cato PoP and the application destination to determine whether the issue occurs on this path segment. Application route analysis helps you:

This analysis helps distinguish between site connectivity issues and application-side network problems.
  - Identify latency or packet loss between the PoP and the application network
  - Determine whether the issue occurs inside the destination network
  - Confirm whether application performance issues originate outside the site network
