---
title: "Product Updates - January 19, 2026"
slug: "product-updates-january-19-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-january-19-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - January 19, 2026

## New Features & Enhancements

- **XOps Supports Predictive Alerting on Socket CPU Trends:** As part of the Cato Insights platform, XOps analyzes CPU usage trends to [proactively alert](/v1/docs/drilling-down-and-analyzing-xops-predictive-insight-stories) on potential issues before they occur.
  - Stories are created with all supported data and remediation playbooks
  - Webhook notification is supported via Response Policy
  - Requires an XOps license
- **Socket Refresh Policy:** Read this [article](/v1/docs/cato-socket-hardware-refresh-policy) to learn about how Cato manages the lifecycle of Socket hardware devices. This policy helps you understand what to expect when your Socket hardware approaches end-of-support, and how and when Cato initiates hardware replacements.
  - To see which Sockets are approaching end-of-support, use the **Hardware Version** column in the [Sockets & Accessories](/v1/docs/using-the-socket-assignment-page) page (Account > Sockets & Accessories) to see all the Socket models in the account (e.g. X1500 and X1500B). This column is hidden by default.
- **Additional Filtering Capabilities for appStats API:** [Filter aggregated results](https://api.catonetworks.com/documentation/#definition-AppStatsPostAggFilter) of the appStats API. For example, return only users whose total application usage exceeds a defined threshold, or return only apps with traffic volume above a specific value.
  - Apply filters after aggregation, similar to the SQL HAVING clause
  - Filtering aggregated fields is only supported for numeric fields (arrays and string fields are not supported)

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 2 new apps, Chrome Webstore, D.e-Express
  - Enhanced Apps:
    - Windows
      - Updated app domains
    - Zscaler
      - Updated app IPs
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2020-29047 (Enhancement)
  - CVE-2025-14847 (New)
  - CVE-2025-2621 (New)
  - CVE-2025-37164 (New)
  - CVE-2025-54236 (New)
  - CVE-2025-54249 (New)
  - CVE-2025-55183 (New)
  - CVE-2025-55184 (New)
  - CVE-2025-68645 (New)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - ICMP Tunneling - Inconsistent Wan ICMP Payload Detected (New)
- **Application Control Policy**
  - **CASB**
    - Mediafire - upload (New)
- **TLS Inspection**
  - Google ChromeOS Rules (New)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Remote Access Application Upstream Bandwidth Anomaly (Enhancement)
    - Remote Access Netbios Application Upstream Bandwidth Anomaly (New)
    - Unusual Volume of User Password Change Activities (Enhancement)
    - Unusual Volume of User Delete device Activities (New)
    - Unusual Volume of User Delete Activities (New)
    - Unusual Volume of User Password Reset Activities (New)
    - Abnormal Identity Deletion Activity by User (New)
    - Massive login activities by an authorized third-party user (New)
    - IP checking services First Occurrence Anomaly (Enhancement)
    - First Occurrence of Outbound Remote Access Activity from Site (Enhancement)
    - Abnormal File Transfer Protocols Activity Over The LAN (New)
    - Unusual Volume of User Removing member from group Activities (New)
  - Threat Hunting
    - Sensitive Data Transfer via Generative AI Application (New)
- **Application Control Via API and Data Protection API Integrations**
  - **Out of Band Integrations**
    - The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
      - Slack | Anomaly Events
        - (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
