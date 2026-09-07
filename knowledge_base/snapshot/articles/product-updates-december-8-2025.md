---
title: "Product Updates - December 8, 2025"
slug: "product-updates-december-8-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-december-8-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - December 8, 2025

## New Features & Enhancements

- **Off-Cloud Network Rules and WAN Recovery Enhancements:** We added support for China Socket sites to communicate via [off-cloud direct tunnels](/v1/docs/routing-traffic-to-an-off-cloud-link). This enhancement allows for routing high-volume traffic directly between sites within China, and [business continuity use cases](/v1/docs/socket-site-resiliency-with-wan-recovery).
- **Browser Extension v1.3:** Starting the week of December 8, the new [Browser Extension v1.3](/v1/docs/summary-of-browser-extension-releases) will be available in the Chrome Web Store, and includes the following bug fix:
  - We improved how the extension writes and stores logs, which had caused slowness and pages to be unresponsive

## PoP Announcements

- **Ürümqi, China:** A new Cato PoP is now available in Ürümqi with the IP range 124.88.46.0/26.
- New ranges will soon be added to these PoP locations:
  - **Frankfurt, DE:** 159.117.236.0/24
  - **Bangkok, TH:** 113.30.130.0/24

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - **Enhanced Apps:**
    - AI Playground
      - Added domain **ai-sdk.dev**
    - Corsearch
      - Added new category Business Systems
      - Removed categories Generative AI Tools, Productivity
      - App risk decreased from 4 to 3
    - FullStory
      - Added categories Business Information, Business Systems
      - Removed category Shopping
    - Jumio
      - Added categories Business Information, Finance, Business Operations AI
      - Removed category Productivity
    - mediafire
      - Added domain **mediafireuserupload.com**
    - Microsoft Copilot
      - Removed domain **copilot.cloud.microsoft**
    - Microsoft Copilot (enterprise)
      - Added domain **copilot.cloud.microsoft**
      - Removed domain **deprecated.deprecated**
    - Naver Blog
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Cafe
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Chzzk
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Finance
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Land
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Mail
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver News
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Papago
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Pay
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - Naver Shopping
      - Application is now available in Application Control rules
      - App risk increased from 1 to 3
    - TeaMate+
      - Added new category Business Systems
      - Removed categories Generative AI Tools, Productivity
      - App risk decreased from 4 to 3
    - USPTO
      - Modified name from **USPTO Virtual Assistant** to **USPTO**
      - Added new category Government
      - Removed categories Generative AI Tools, Productivity
      - App risk decreased from 4 to 2
    - v0 by Vercel
      - Added domain **v0.app**
  - **Category Changes:**
    - Business Information:
      - Added apps: FullStory, Jumio
    - Business Operations AI:
      - Added app: Jumio
    - Business Systems:
      - Added apps: Corsearch, FullStory, TeaMate+
    - Finance:
      - Added app: Jumio
    - Generative AI Tools:
      - Removed apps: Corsearch, TeaMate+, USPTO
    - Government:
      - Added app: USPTO
    - Productivity:
      - Removed apps: Corsearch, Jumio, TeaMate+, USPTO
    - Shopping:
      - Removed app: FullStory
- **Application Control Policy / CASB**
  - Deepseek - Conversation (New)
  - iCloud - Upload (New)
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2024-8068 (Enhancement)
  - CVE-2025-25256 (New)
  - CVE-2025-31137 (New)
  - CVE-2025-41243 (New)
  - CVE-2025-54253 (New)
  - CVE-2025-55752 (New)
  - CVE-2025-57790 (Enhancement)
  - CVE-2025-58360 (New)
  - CVE-2025-59287 (Enhancement)
  - Heuristic - Sliver C2 - Http Session CnC Polling (New)
  - Heuristic - TurboVPN Anonymizer (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - Enhanced Apps
    - Microsoft 365 Apps - Activity (Enhancement)
    - SharePoint - Activity (Enhancement)
    - Exchange - Activity (Enhancement)
    - Entra ID - Activity (Enhancement)
  - New fields added
    - Actor Type
      - Slack
      - Sharepoint
      - Exchange
      - Microsoft 365 Apps
      - Entra ID
      - Amazon Cloudtrail
    - User Origin
      - Sharepoint
      - Exchange
      - Microsoft 365 Apps
      - Entra ID
    - Service Name
      - Zendesk
      - Slack
      - ServiceNow
      - salesForce
      - Sharepoint
      - Exchange
      - Microsoft 365 Apps
      - Make
      - Google Drive
      - Google Apps
      - GitHub
      - Egnyte
      - ChatGPT
      - Box
      - Entra ID
      - Atlassian JIRA and Confluence
      - Amazon Cloudtrail
      - Dropbox
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam).
  - Download File with Common Malware Name (New)
  - ICMP Tunneling Indication | Abnormal Response Count (New)
- **TLS Inspection**
  - ChatGPT macOS client (Enhancement)
- **Device Inventory**

These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
  - MOBILE
    - Mobile Phone
      - Apple iPhone (Enhancement)
  - OT
    - Single Board Computer
      - Raspberry Pi (Enhancement)
    - Industrial Control
      - Advantech (Enhancement)
  - IOT
    - Printer (Enhancement)
  - General
    - NIC Vendor Translation (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
