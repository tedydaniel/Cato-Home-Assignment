---
title: "Product Updates - December 22, 2025"
slug: "product-updates-december-22-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-december-22-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - December 22, 2025

## New Features & Enhancements

- **Import IoCs from URL:** For faster updates and greater flexibility, you can now [import Indicators of Compromise](/v1/docs/integrating-custom-ioc-lists-with-containers) (IoCs) directly from a URL. This enhances security by enabling the automated or scheduled retrieval of IoC lists from trusted external sources.
  - Previously, IoCs could be imported by uploading files
  - Click [here](https://academy.catonetworks.com/ioc-import-from-url) to watch a video recording of this feature
- **Visibility for Key Metrics in Overview Map:** Explore your site and user activity interactively with the [improved map component](/v1/docs/using-the-overview-dashboard). Quickly view data-based geographical patterns for sites and users, including:
  - Current connectivity status, traffic volume, threat events, and connectivity over time
- **~~Account-Level Custom Allowlists for SSO:~~** ~~You can now~~ [~~define an allowlist of domains and IPs~~](/v1/docs/configure-custom-allowlists-for-sso) ~~for your account to support SSO authentication flows that require access to additional resources during authentication.~~
  - ~~Add specific domains or IPs that are required for SSO authentication~~
  - ~~Support complex identity flows that rely on external resources~~
  - ~~Click~~ [~~here~~](https://academy.catonetworks.com/custom-sso-allowlist) ~~to watch a video recording of this feature~~
- **Cato Management Application Enhancement - Quickly Review Best Practice Checks:** To more easily review and [manage Best Practice checks](/v1/docs/reviewing-posture-checks-for-your-account) (Home > Best Practices), we added a Best Practice Check Review panel, which includes:
  - Details such as status, severity, and description
  - A change history of the check status
  - Adding internal comments
  - Click [here](https://academy.catonetworks.com/quick-review-best-practices) to watch a video recording of this feature

## PoP Announcements

- **Copenhagen, DK:** A new range (159.117.237.0/24) is now available for the Copenhagen PoP location.
- **Rome, IT:** A new Cato PoP is now available in Rome with the IP range 216.252.176.0/24.

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 8 new apps – Canon BJNP, Canon MFNP, Canon Printer Protocols, Payoneer, WeCom (WeChat for work), WeCom Conferences, WeCom Email Service, WeCom Voice Calls
  - Enhanced Apps:
    - Filestack, Inc.
      - Added domains **cdn.filestackcontent.com**, **filestackapi.com**
    - Firebase
      - Updated app domains
    - Screencloud
      - Added domains **screencloudapp.com**, **screencloudapps.com**
    - Tencent Holdings Limited
      - Updated app IPs
    - WeChat
      - Updated app domains
      - Updated app IPs
    - WeChat File Transfer
      - Added new category File Sharing
  - Category Changes
    - File Sharing
      - Added app: WeChat File Transfer
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - ValleyRat (New)
  - JsOutProx RAT (Enhancement)
  - CVE-2025-61757 (New)
  - CVE-2024-53900 (New)
  - CVE-2025-64496 (New)
  - CVE-2025-11953 (New)
  - CVE-2025-6204 (New)
  - CVE-2025-55182 (New)
  - Impacket sambaPipe Execution (New)
  - Generic | Remote Code Execution over HTTP (Enhancement)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Kerberos Authentication using an ESC1-2 Certificate (New)
- **Application Control Policy**
  - CASB
    - Grok Conversation (New)
- **XDR Indications of Attack**
  - Threat Hunting
    - Exfiltration Attempt to Web-based Email Categories (New)
    - Exfiltration Attempt to Chat and IM Categories (New)
    - Exfiltration Attempt to Personal Storage Categories (New)
  - Anomaly Detection
    - User File Sharing Application Upstream Bandwidth Anomaly (Enhancement)
    - First Occurrence of INBOUND SMB Activity in a Site (New)
    - Abnormal Upload Activity (New)
    - Unusual Organization-Wide Identity Deletion Activity (New)
    - First Occurrence of Massive Identity Deletion Activities by User (New)
    - First Occurrence of Failed Login from a New Operating System (New)
    - Abnormal Outbound Remote Access Tool Usage (Enhancement)
    - Abnormal SMB Traffic from an User Over the WAN (Enhancement)
    - ConnectWise ScreenConnect Remote Connection Anomaly (Enhancement)
    - ConnectWise ScreenConnect Remote Connection First Occurrence Anomaly (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
