---
title: "Cato Socket Link SLA Architecture"
slug: "cato-socket-link-sla-architecture"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-socket-link-sla-architecture"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Socket Link SLA Architecture

## Overview

The Cato Cloud is a private global backbone built over tier-1 providers to deliver consistent and predictable SLA performance for WAN traffic between enterprise sites. Each Cato PoP is interconnected through this backbone, providing controlled latency and packet delivery independent of the public Internet.

To maintain these guarantees, Cato developed proprietary technology that enables continuous coordination between the [Cato Socket](/v1/docs/what-are-cato-sockets) and the PoP. The Socket measures key performance metrics for each link, while the PoP aggregates and correlates these measurements to maintain the optimal path between the site and the backbone. Together, they ensure consistent link performance, adapting in real time to preserve service continuity and maximize the efficiency of available WAN resources.

Cato provides full end-to-end visibility into the network conditions of every site, user, and application. Cato’s XOps service applies AI-driven analytics to transform this data into clear, actionable stories that help IT teams resolve issues faster. By continuously ingesting metrics into a single-context engine, XOps delivers real-time insights and alerts that reduce repetitive investigation and accelerate root cause identification, ensuring optimal user experience.

### Behavior by Site Deployment Type

- **Active/Active:** Cato dynamically evaluates and routes traffic across both active WAN links. Traffic is steered to the better-performing link based on real-time conditions. The settings are dynamically configured by the Cato backbone and you can [customize SLA thresholds](/v1/docs/configuring-the-connection-sla-settings-for-active-active-socket-sites) on the account level or per site.
- **Active/Passive:** Only the primary link carries traffic during normal operation. When performance falls below SLA thresholds, the Socket activates the passive link and redirects traffic to maintain connectivity. This behavior is governed by Smart SLA, which automatically evaluates link quality for failover decisions. You can also [customize SLA thresholds](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites) on a per-site basis
- **Active/Passive with Last-Resort:** To ensure critical connectivity during severe WAN outages, you can define a last-resort link for the Socket. Typically, a cellular connection, the Socket only utilizes this link in emergency situations

## Link SLA Operation and Architecture

The Cato Cloud backbone and the Socket operate as a unified SD-WAN fabric that maintains consistent link performance across the WAN. Through continuous telemetry exchange between the Socket and its connected PoP, the platform monitors each link’s real-time quality and proactively adjusts routing to prevent degradation.

### Socket and PoP Harmony

The Socket measures latency, packet loss, jitter, and congestion for each WAN link and sends this data to the connected PoP. The PoP then validates the measurements against its own backbone-side telemetry. Working together, the Socket and PoP make synchronized routing decisions, ensuring end-to-end visibility and avoiding local anomalies. For more information, see [Understanding Acceptable and Unacceptable SLA for Sites](/v1/docs/understanding-acceptable-and-unacceptable-sla-for-sites).

### Real-Time Link Evaluation

The Socket assigns a dynamic score to each link based on real-time performance, with scores updated every few seconds. When network conditions change, traffic paths are automatically adjusted without manual intervention. Admins can view both real-time and historical metrics in the CMA, which reflect insights from both the Socket and PoP. For more information, see [Part 1: The Socket Interfaces and Precedence](/v1/docs/part-1-the-socket-interfaces-and-precedence).

### Backbone-Level Optimization

The PoP integrates link telemetry into Cato’s global routing engine. If consistent degradation is reported by the Socket, the PoP may reroute the site’s traffic through an alternate backbone path. This approach ensures SLA enforcement beyond the site level.

### Example Sequence: Degradation Detection and Path Adjustment

This example illustrates how a physical site in Philadelphia, USA, maintains SLA compliance by switching between nearby Cato PoPs in New York and Washington, D.C.

1. **Degradation Detection:** The Socket at the Philadelphia site detects increased packet loss and latency on the link connected to the New York PoP. These degraded metrics are immediately reported to the New York PoP.
2. **Telemetry Exchange:** The Washington D.C. PoP validates the report against its own backbone-side telemetry. Both PoPs confirm that the degradation is consistent and not caused by a transient local issue.
3. **Path Adjustment:** The Philadelphia Socket reroutes the impacted flows from the New York PoP to the Washington D.C. PoP. The transition occurs automatically, preserving session continuity and restoring SLA compliance.
4. **Post-Adjustment Monitoring:** The Socket and PoPs continue to monitor link quality. When the New York PoP connection returns to normal performance, traffic automatically migrates back to the optimal path through New York. This behavior is driven by preemptive logic that ensures the Socket always reconnects to the geographically closest and best-performing PoP once the issue is resolved.

## Active/Active Site Behavior

To provide load balancing, the Socket uses its scoring data to balance traffic intelligently across the active WAN links. This ensures efficient bandwidth utilization and consistent application performance. Cato’s SD-WAN logic evaluates both upstream and downstream directions to maintain bidirectional quality for real-time applications such as voice and video.

When degradation is detected, the Socket and PoP seamlessly redirect traffic to the better-performing link. Existing sessions remain stable, and users experience no noticeable disruption.

## Active/Passive Site Behavior

In Active/Passive deployments, one WAN link carries traffic while the second remains on standby. For Active/Passive/Last-resort deployments, to avoid unnecessary data charges or bandwidth usage, minimal data is sent over the link while it remains passive. It is activated only when both the active and passive WAN links are either unavailable or performing outside the defined SLA thresholds. For more information, see [Configuring a Last-Resort Link](/v1/docs/configuring-a-last-resort-link).

### Failover and Recovery

Failover causes a brief but expected disruption as the passive link initializes. Once stable, the Socket resumes link evaluation on both paths. When the primary link recovers, traffic transitions back automatically.

## Active/Passive Link Evaluation with Smart SLA

For active/passive Socket sites, the default SLA setting is Cato’s Smart SLA. This setting ensures traffic flows over the most reliable link using real-time performance evaluation. The Socket applies predefined thresholds for latency, jitter, and packet loss. Degraded metrics are reported to the PoP, which validates the data using backbone telemetry.

Smart SLA removes the need to configure site-specific thresholds, while still adapting to real-time conditions. This ensures failover and recovery decisions are made quickly and accurately.

Smart SLA samples link data every few seconds, aggregating metrics into moving averages. When no user traffic is present, synthetic probes are used to maintain visibility. Dual validation between Socket and PoP prevents false positives caused by localized anomalies.

Failover only occurs after a minimum number of threshold violations. Metric weighting favors latency and jitter for real-time traffic, while packet loss is prioritized for bulk data flows. For more information, see [Configuring the Connection SLA Settings for Active/Passive Socket Sites](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites).

## Monitoring Link Performance

Cato provides multiple ways to monitor WAN link performance across your network. You can view real-time and historical SLA metrics in the CMA, access raw telemetry via the Cato API, or use XOps to analyze incidents and trends through story-based insights. These options give you visibility at both the operational and event levels, helping you proactively manage performance and troubleshoot connectivity issues.

### Monitoring Links with XOps

Cato’s XOps service adds an AI-driven operational layer that helps admins proactively identify and resolve link-related issues across the network. The Site Operations engine detects conditions like link instability, BGP disconnects, or site outages and automatically correlates them into unified stories. Each XOps story aggregates relevant metrics, events, and topology details into a single view that reflects the issue’s root cause and timeline. These stories are visible in the Stories Workbench page, where you can sort, filter, and drill into events by site, indication type, or criticality level.

Stories link to the relevant playbooks to guide investigations, and also generate dynamic AI-based story summaries to accelerate analysis. Stories close automatically after resolution, making it easier to track recurring problems and operational health over time without manual cleanup. For example, a Site Operations story is opened because the site was forced to reconnect to the PoP to optimize performance. After two hours, the story is automatically closed because the issue is not repeated.

Related Articles:

- [Getting Started with XOps](/v1/docs/getting-started-with-xops)
- [Reviewing Site Operations Stories](/v1/docs/reviewing-site-operations-stories)

### Monitor Links in the CMA

Admins can view link data from all Sockets and PoPs via dashboards and pages:

- [Network > Sites](/v1/docs/working-with-sites): Displays current **Connectivity Status** and degraded links
- [Site > Network Analytics](/v1/docs/showing-the-site-network-analytics): Metrics (ie, packet loss) history, including failovers and recovery
- [Network > Sites Overview](/v1/docs/analyzing-traffic-for-all-account-sites): Summarized SLA performance across sites
- [Network > Network Overview](/v1/docs/using-the-network-overview-page): Real-time SLA map of global site connectivity

### Monitor Link SLA via the API

Use the following APIs to retrieve SLA telemetry:

- accountMetrics API – Historical SLA between site and backbone
- socketPortMetrics API – Real-time performance per Socket interface and transport

Related Articles:

- [What is the Cato API](/v1/docs/what-is-the-cato-api)
- [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/)

### Integrations and Notifications

Cato integrates with SIEMs and collaboration tools. [Webhooks](/v1/docs/sending-cma-notifications-via-webhooks) can deliver alerts for:

- Link degradation via health alerts and XOps network stories
- Socket failover and recovery events

For more information, see [Working with Link Health Rules](/v1/docs/working-with-link-health-rules).
