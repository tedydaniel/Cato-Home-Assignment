---
title: "XOps FAQ"
slug: "xops-faq"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-faq"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps FAQ

This article answers frequently asked questions about the transition from XDR to XOps.

## What is XOps?

XOps is Cato’s analytics layer that unifies Security Detection & Response and AIOps to provide insights and guided remediation tools to help you efficiently detect, respond to, and resolve security and operational incidents.

As was [announced](/v1/docs/product-update-june-23-2025), on **August 6, 2025**, the existing Detection & Response stories that were part of the XDR Core offering are transitioning to the enhanced XOps service and license, including: [Threat Prevention](/v1/docs/drilling-down-and-analyzing-xops-security-stories), [network](/v1/docs/reviewing-site-operations-stories) and operations, and third-party data. The [Stories Overview](https://support.catonetworks.com/document/preview/90659#UUID-9620929f-3d28-a300-ee40-2d5f525bd0d2) and [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) will also require the XOps license.

XOps introduces an AI-driven layer to your SASE environment. It combines our advanced XDR (security) and AIOps (network and operations) capabilities into a unified solution. Designed to drive operational efficiency, XOps turns vast volumes of raw security and network events into clear, actionable insights.

This AI layer enables IT and security teams to quickly understand what's happening across their entire SASE estate and take meaningful action. For example, the AIOps component, available as part of the XOps license, uses AI and machine learning to detect operational issues, identify root causes, and suggest mitigation steps. A practical case would be predicting issues due to high socket CPU usage and offering recommendations to prevent service degradation or loss of connectivity.

## What Will Happen to the XDR Pro License?

The introduction of XOps means the XDR Pro license is being retired. Existing XDR Pro customers will be seamlessly transitioned to the new XOps license at their next renewal. See below for more details of available stories based on license.

## What Data Does XOps Use to Generate Insights?

XOps analyzes signals from across your entire SASE deployment. This includes core events like SD-WAN and Firewall traffic, as well as data from any add-on services you've licensed, such as Threat Prevention, CASB, and Digital Experience Monitoring (DEM). By aggregating this data, XOps delivers comprehensive stories and actionable insights.

## What Happens to XDR Core Stories on August 6?

As of August 6, 2025, free access to XDR Core stories will be discontinued. To continue accessing these stories, and gain even more advanced operational insights and threat detections, you need to purchase the XOps license. XOps includes enhanced insights beyond what was previously available through XDR Core.

If you have been using XDR core stories and have questions about this transition and licensing change, please reach out to your Cato Representative.

## Is There Any Impact to the MDR Service?

No, there is no impact to the security service. You will continue to receive the same high-quality service from Cato’s Managed Detection and Response (MDR) team without any changes. The service will continue to focus on security stories and detections.

Network XDR stories, that were previously included in XDR Core, are now called Site Operation stories and are included within the XOps license. MDR customers that would like to maintain visibility of these stories can purchase an XOps license.

## Is There an Impact to ILMM and NOCaaS?

ILMM customers are currently being migrated, and retain access to the Detection and Response screens as expected. The transition is being managed proactively to ensure continuity of service.

**NOCaaS**

All **operational stories**, including ILMM (last-mile operational issues, e.g., BGP session down, LAN Host Monitoring), will be visible.

**ILMM**

Only **last-mile operational stories** (Site down, Link down, Alt WAN Link down, Quality SLA issues) will be visible.

## What Stories are Available for Each License?

This table summarizes the stories available for each license:

| License | Available Stories |
| --- | --- |
| No XOps or Managed Services | Events are generated for some third party integrations, however Stories are not generated |
| XOps | - Security (e.g., Threat Hunting, UEBA anomalies, CrowdStrike) - Operational (e.g. BGP session down, LAN Host Monitoring) storied are generated |
| MDR | - Security stories (e.g., threat hunting, UEBA anomalies, Crowdstrike EDR alerts), including 3rd party security stories |
| NOCaaS | - Operational (e.g. BGP session down, LAN Host Monitoring) storied are generated |
| ILMM | - Last-mile operational stories (e.g. Site down, Link down, Alt WAN Link down, Quality SLA issues.) If you have ILMM, and the ILMM license is not allocated to the sites, then the ILMM stories are muted |
| Cato EPP | - Cato Endpoint Alerts |
