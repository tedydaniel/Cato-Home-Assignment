---
title: "Product Updates - February 2, 2026"
slug: "product-updates-february-2-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-february-2-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - February 2, 2026

## New Features & Enhancements

- **Turnkey Integration with Microsoft Sentinel:** Streamline operations by automatically forwarding [Cato events to Microsoft Sentinel](/v1/docs/integrating-cato-events-with-microsoft-sentinel) for unified monitoring and analysis. The built-in integration:
  - Reduces setup time and eliminates the need for custom scripts or connectors
  - Uses Cato events schema
  - Enhances visibility through centralized event management

- **Detailed Visibility of Interconnected Apps:** View detailed information about [third-party apps and plugins](/v1/docs/viewing-and-analyzing-interconnected-apps) connected to critical business apps. This visibility helps you understand which external apps are used in your environment and how they interact with core services. For example, you can review apps integrated with Slack to quickly assess their security posture.
  - Currently supported for Slack and Entra ID
  - CASB license required

- **DLP Uses Machine Learning to Identify Images:** Data Loss Prevention (DLP) can now inspect image files to detect sensitive data in images and prevent them from being exfiltrated.
  - Machine Learning (ML) is used to [identify sensitive images](/v1/docs/working-with-predefined-data-types-for-dlp) based on models that dynamically learn and evolve with changing data patterns
  - The new Image ML Classifier provides comprehensive detection for images of personal documents, engineering diagrams, and collaboration (for example, images of a handwritten note with sensitive information)
  - DLP license required

- **Granular RBAC for Policy Management:** Delegate [managing a set of rules as a subpolicy](/v1/docs/configuring-rbac-for-policy-management), and then assign admin permissions to access the subpolicies.
  - Maintains centralized control over the global policy and lets you delegate ownership of a subpolicy to specific teams
  - Supported for Internet Firewall and WAN Firewall policies
  - For example, delegate a subpolicy of traffic to sites in France to the French SOC team

- **Access Point Integration for Enhanced Device Inventory Identification:** To improve device visibility and accuracy, you can integrate third-party access point device data with Cato’s [device discovery](/v1/docs/what-is-device-inventory) for the IoT/OT Security service. This integration leverages machine learning–driven capabilities to enhance device identification and classification across wireless networks.
  - Initial support includes [Juniper Mist](/v1/docs/juniper-mist-creating-the-device-management-integration) access points
  - Requires an IoT/OT Security license and configuration of the Juniper Mist connector

- **Turnkey Integration with Splunk:** Streamline operations by automatically [forwarding Cato events to Splunk](/v1/docs/integrating-cato-data-with-splunk) for unified monitoring and analysis. The built-in integration:
  - Reduces setup time and eliminates the need for custom scripts or connectors
  - Uses Cato events schema
  - Enhances visibility through centralized event management

- **Improved Management of Best Practice Checks:** Mute or dismiss a [Best Practice check](/v1/docs/reviewing-posture-checks-for-your-account) or specific findings within a check to increase the accuracy and relevance of your account score displayed on the **Best Practices** page.
  - Initially supported for the Internet Firewall, other policies will be supported in the coming weeks

- **Browser Extension v1.5:** During the week of February 1, 2026, a [new Browser Extension version 1.5](/v1/docs/summary-of-browser-extension-releases) will be available in the Chrome Web Store, and includes improved performance fixes.

## PoP Announcements

- **Bangkok, TH:** A new range (113.30.130.0/24) is now available for the Bangkok PoP location.
- New ranges will soon be added to these PoP locations:
  - **Marseille, FR:** 159.117.239.0/24
  - **Chennai, IN:** 113.30.132.0/24

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 20 new apps – BuzzSumo, Geekbot, Linear, NewReleases, OpenPoll, Peerbound, PollChamp, Polly, Pylon, Redash, Semgrep, Shufflet, Standuply, StatusGator, Stream, Tatsu, Timy, UserGems, Walnut, Workast
  - Enhanced Apps:
    - Genesys
      - Updated app IPs
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2024-29269 (New)
  - CVE-2025-11700 (New)
  - CVE-2025-4009 (New)
  - CVE-2025-52691 (New)
  - CVE-2025-54253 (Enhancement)
  - CVE-2025-64446 (New)
  - CVE-2025-68613 (New)
  - CVE-2026-21859 (New)
  - CVE-2026-24061 (New)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Abnormal Data Upload to AI Application by User (New)
  - Threat Hunting
    - Suspicious Chrome Extension (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - GitHub
    - Anomaly Events (Enhancement)
  - Dropbox
    - Anomaly Events (New)
  - SentinelOne
    - EDR (Enhancement)
  - CrowdStrike
    - EDR (Enhancement)
    - Devices (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
