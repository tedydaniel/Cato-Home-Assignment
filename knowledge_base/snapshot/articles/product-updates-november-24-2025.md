---
title: "Product Updates - November 24, 2025"
slug: "product-updates-november-24-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-november-24-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - November 24, 2025

## New Features & Enhancements

- **Active/Active Support for IPsec Sites:** You can configure IPsec sites to establish and route traffic through [multiple active tunnels](/v1/docs/configuring-ipsec-ikev2-sites). This lets you obtain higher bandwidth and improved stability for your IPsec sites by better utilizing multiple last-mile links.
  - You can establish up to 3 active tunnels per role (Primary and Secondary)
  - All active tunnels for a role must be connected to the same PoP location
  - Previously available only for new accounts
  - Click [here](https://academy.catonetworks.com/multiple-active-tunnels-for-ipsec-sites) to watch a video recording of this feature
- **~~Visibility for Key Metrics in Overview Map:~~** ~~Explore your site and user activity interactively with the~~ [~~improved map component~~](https://support.catonetworks.com/hc/en-us/articles/28315079624221-Using-the-Account-Overview-Dashboard) ~~in the Overview page. Quickly view data-based geographical patterns for sites and users, including:~~
  - ~~Current connectivity status, traffic volume, threat events, and connectivity over time~~
- **New Connectivity Health Alerts for Socket Sites:** For improved monitoring of port and link status and HA readiness, we’re adding new [Connectivity Health Alerts](/v1/docs/working-with-link-health-rules), including:
  - LAN Port Disconnect
  - Alt. WAN Disconnect
  - HA Not Ready
  - Click [here](https://academy.catonetworks.com/connectivity-health-alerts) to watch a video recording of this feature
- **Enterprise Directory Page for Managing Locations:** Streamline shipping operations by centrally managing your organizational locations in one place with the Account > [Enterprise Directory](/v1/docs/managing-locations-in-the-enterprise-directory) page.
  - You can apply the **Locations** to items on the Account > Shipping page
  - Click [here](https://academy.catonetworks.com/enterprise-directory) to watch a video recording of this feature

## PoP Announcements

- **Cape Town, ZA:** A new Cato PoP is now available in Cape Town with the IP range 159.117.232.0/24
- **Paris, FR:** A new range (159.117.234.0/24) is now available for the Paris PoP location

## Security Updates

- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2021-24212 (New)
  - CVE-2021-42071 (New)
  - CVE-2022-47966 (Enhancement)
  - CVE-2025-2611 (New)
  - CVE-2025-34023 (New)
  - CVE-2025-44137 (New)
- **Application Control Via API and Data Protection API Integrations** The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities) and [Data Protection API](/v1/docs/data-protection-api) integrations:
  - Enhanced Apps
    - Zoom - Experience (Enhancement)
    - Egnyte - Activity (Enhancement)
  - Tenant field added to the following Activity apps
    - Box
    - ChatGPT
    - Dropbox
    - Egnyte
    - Entra ID
    - Google Apps
    - Google Drive
    - Make
    - Microsoft Apps
    - Microsoft Exchange
    - Salesforce
    - SharePoint and OneDrive Business
    - Slack
    - Zendesk
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Impacket psexec Execution (Enhancement)
  - Impacket smbexec Execution (Enhancement)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Wanbound FTP First Occurrence Anomaly (Enhancement)
- **Device Inventory**

These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
  - IOT
    - Card Printer
      - CPI CardAtOnce (New)
    - Payment Terminal
      - Payter (New)
      - Payter P6 (New)
      - Payter Apollo (New)
    - Printer
      - Kyocera (Enhancement)
    - Multifunction Device
      - Kyocera (Enhancement)
      - Kyocera Taskalfa (Enhancement)
    - Single Board Computer
      - Raspberry Pi (Enhancement)
  - OT
    - PLC
      - Siemens Simatic S7 (Enhancement)
  - Device Type
    - Card Printer (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
