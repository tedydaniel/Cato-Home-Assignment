---
title: "Product Updates - January 5, 2026"
slug: "product-updates-january-5-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-january-5-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - January 5, 2026

## New Features & Enhancements

- **Enhanced Experience Monitoring Topologies for WAN and Internet Apps:** To help you quickly identify where performance issues occur across the full traffic path, the Experience Monitoring page (Home > Experience Monitoring) now shows a richer end-to-end topology for both Internet and WAN applications (DEM license is required).
  - Visibility for both ingress and egress PoPs in [all drill-down views](/v1/docs/experience-monitoring)
  - Additional destination-site nodes and metrics, including:
    - **First Mile** metrics for the destination path
    - Socket, IPsec, or Cloud Interconnect nodes with their relevant metrics
  - This feature is being gradually released over the next few weeks
- **Wiz Integration with XOps for Cloud Environment Visibility:** We are extending [XOps](/v1/docs/welcome-to-the-cato-xops-service) to include issue data from [Wiz](/v1/docs/wiz-configuring-the-xops-integration) to generate stories based on vulnerabilities in your cloud environment to investigate in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) (Home > Stories Workbench).
  - This integration streamlines investigation and correlation across your network and cloud environments by automatically generating stories based on Wiz issue data, including:
    - Issue details and resources
    - Common IOCs (e.g., users, IP addresses, and domains) to correlate between Cato-based and Wiz-based issues
    - XOps license required
- **New Demo Mode Use Case - Investigating Suspicious DNS Activity:** A new [Demo Mode](/v1/docs/cato-s-demo-account) use case shows how to use XOps to investigate suspicious DNS activity. This helps teams understand typical investigation workflows and security insights using sample data.
  - Access Demo Mode through the **AskAI** button at the top of the Cato Management Application (CMA)
- **Reminder - Deprecation of ILMM Scheduled Maintenance Page:** As part of the migration of the ILMM service to the CMA, the [ILMM Scheduled Maintenance](/v1/docs/managing-ilmm-for-your-account) page is now deprecated and fully replaced by the [Mute Stories](/v1/docs/muting-xops-stories) policy.
  - Create Mute Stories rules to suppress alerts during planned maintenance windows
  - Note: Existing Scheduled Maintenance entries **are not automatically migrated** to the Mute Stories policy
  - For more details, see the [original announcement﻿](/v1/docs/upcoming-migration-of-ilmm-service-to-the-cma)

## PoP Announcements

- **Phoenix, US:** A new range (199.27.47.0/24) will soon be added to the Phoenix PoP location.

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 3 new apps – Crunched, Farsight, ProSights
  - Enhanced Apps:
    - doodle
      - Removed category Chat and IM
    - Snapchat
      - Added categories Chat and IM, Media Streams
  - Category Changes:
    - Chat and IM:
      - Added app: Snapchat
      - Removed app: doodle
    - Media Streams:
      - Added app: Snapchat
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2025-20333 (New)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - ICMP Tunneling - Inconsistent Outbound ICMP Payload Detected (New)
- **Application Control Policy / CASB**
  - CASB
    - Perplexity - Login (Enhancement)
- **XDR Indications of Attack**
  - Anomaly Detection
    - First Occurrence of INBOUND RDP Activity in a Site (New)
    - SMTP Application Upstream Bandwidth Anomaly (New)
    - First Occurrence of INBOUND RDP Activity in a Site (New)
    - Abnormal INBOUND RDP Activity (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - Microsoft 365 Activities
    - Anomaly Events (New)
  - GitHub Activities
    - Anomaly Events (Enhancement)
  - Wiz Activities
    - CDR (New)
  - Snyk Activities
    - Anomaly Events (New)
  - Zoom Activities
    - Experience (Enhancement)
- **Device Inventory**

These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
  - NETWORKING
    - Firewall
      - Check Point (Enhancement)
  - OT
    - Industrial Control
      - Wiesemann & Theis (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
