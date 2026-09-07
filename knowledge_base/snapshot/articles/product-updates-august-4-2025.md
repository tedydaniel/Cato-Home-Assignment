---
title: "Product Updates - August 4, 2025"
slug: "product-updates-august-4-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-august-4-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - August 4, 2025

## New Features & Enhancements

- **Introducing Cato XOps - Providing Actionable AI-Driven Insights:** As previously [announced](/v1/docs/product-update-june-23-2025), [XOps](/v1/docs/xops-faq) is Cato’s analytics layer that unifies Security Detection & Response and AIOps to provide insights and guided remediation tools to help you efficiently detect, respond to, and resolve security and operational incidents.
  - XOps enables Detection & Response stories that show insights correlated from billions of events to identify potential incidents and operational issues
    - On **August 6, 2025**, the existing Detection & Response stories that were part of the XDR Core offering are transitioning to the enhanced XOps service and license, including: [Threat Prevention](/v1/docs/drilling-down-and-analyzing-xops-security-stories), [network](/v1/docs/sase-detection-response-xops-1) and operations, and third-party data. The Stories Overview and [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) will also require the XOps license
    - For customers without an XOps license, a demo is available on the XOps pages to demonstrate the value and learn more about this product
  - No impact for XDR Pro customers, and they can seamlessly renew to the XOps license
  - Please contact your Cato representative to learn more about migration plans
  - Click [here](https://academy.catonetworks.com/cato-xops-updates) to watch a video recording of this feature

- **New IoT/OT SecurityIntegration with Intune for Enriched Device Visibility**: To enhance device intelligence, you can integrate [Intune’s](/v1/docs/microsoft-intune-configuring-the-device-management-integration) device metadata with Cato’s device discovery for the IoT/OT Security service. A unified view with merged attributes from both data sources is visible on the Home > Device Inventory page. This integration provides:
  - Enriched device profiles for managed and unmanaged assets, combining metadata from both Cato and Intune
  - Additional data increases the accuracy of device identification and classification
  - A clearer, more complete view of your connected devices empowering informed security decisions
  - Click [here](https://academy.catonetworks.com/device-inventory-ms-intune-integration/) to watch a video recording of this feature

- **Support for CyberArk SSO Authentication:** [CyberArk](/v1/docs/configuring-cyberark-sso-for-your-account) can now be used as an IdP by remote users to authenticate with SSO.
  - Click [here](https://academy.catonetworks.com/sso-support-for-cyberark/) to watch a video recording of this feature
- **Browser Extension Now Includes Support for Network Rules:** We improved the [Chrome Browser Extension](/v1/docs/configuring-the-cato-browser-extension) to support routing traffic according to the Network Rules policy.
- **New Connectivity Events for Socket Sites:** In the next few weeks, we’re adding new connectivity event types to gain improved visibility into port status and HA readiness for Socket sites, including **LAN port up/down**, **Alt. WAN Link up/down**, and **HA not ready**.
- **Reminder EoL for Fields and Types in EventFieldName:** 8 fields and types in the <kbd>EventFieldName</kbd> API were end-of-life (EOL) as of May 1, 2025, and will be removed from the Cato GraphQL schema on Aug 3, 2025. For details, see this [article](/v1/docs/cato-api-potentially-breaking-changes-and-eol).
- **Manual PoP Selection for Socket Sites via API:** For greater control over routing behavior and failover handling, the <kbd>updateSiteGeneralDetails</kbd> GraphQL mutation now supports the <kbd>preferedPoPLocation</kbd> setting. This lets you set primary and secondary PoP locations for Socket sites via the API and optionally enforce connections only to those preferred PoPs.
- **CMA Enhancements:**
  - To more accurately reflect the nature of the alerts, all filters and stories previously labeled **Network XDR** are renamed to **Site Operations**.
  - DEM - Splitting Hosts from Users: the **Users/Hosts** tab in the [Experience Monitoring page](/v1/docs/using-the-experience-monitoring-page) is changing to **Site Hosts** and will show information only for devices with no user identity. All data for identified users will be included in the **Remote Users** and **Office Users** tabs.
- **Join Cato's Product Rewind Session on Aug 6:** Product Rewind is a fast-paced monthly webinar, where we will break down the most compelling product updates from July 2025. See the latest innovations in action with live demos and get practical insights on how these updates can enhance your experience.
  - Register [here](https://academy.catonetworks.com/product-monthly-rewind/269140) for Aug 6, 12 pm ET

## PoP Announcements

- **Update for Localized Austria Range:** The geo-localized range for Austria (209.206.0.0/24) is serviced through the Vienna PoP location.
  - Previously, the range was serviced through Munich, DE

## Security Updates

- **App Catalog**
  - Google Drive (Enhancement)
  - Amazon CloudTrail (New)
  - Anydesk (Enhancement)
  - Mps Monitor Srl (Enhancement)
  - SNMP (Enhancement)
- **IPS Signatures**
  - IPS Signatures: View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2020-29390 (New)
    - CVE-2023-32571 (New)
    - CVE-2025-20281 (Enhancement)
    - CVE-2025-45985 (New)
    - CVE-2025-49701 (New)
    - CVE-2025-49704 (New)
    - CVE-2025-49724 (New) CVE-2025-53770 (New)
    - CVE-2025-6514 (New)
    - Heuristic - Mythic C2 - Mythic C2 Agent Download (New)
    - Heuristic - Mythic C2 communication (New)
    - Heuristic - Mythic C2 traffic (New) Heuristic - Putty Downloaded From Unofficial Domain
    - Ransomware - AMERILIFE (Enhancement)
    - Ransomware - AntiHacker (Enhancement)
    - Ransomware - Atomic (Enhancement)
    - Ransomware - Backups (Enhancement)
    - Ransomware - Bash 2.0 (Bash Red) (Enhancement)
    - Ransomware - BlackFL (Enhancement)
    - Ransomware - BlackHeart (MedusaLocker) (Enhancement)
    - Ransomware - Blackransombdbot (Enhancement)
    - Ransomware - Blocker (Enhancement)
    - Ransomware - BQTLOCK (Enhancement)
    - Ransomware - Cowa (Enhancement)
    - Ransomware - Darkness (Enhancement)
    - Ransomware - DataLeak (Enhancement)
    - Ransomware - DeadLock (Enhancement)
    - Ransomware - DELTA (Enhancement)
    - Ransomware - Destroy (Enhancement)
    - Ransomware - Dire Wolf (Enhancement)
    - Ransomware - EnCiPhErEd (Enhancement)
    - Ransomware - Harma (Enhancement)
    - Ransomware - KaWaLocker (Enhancement)
    - Ransomware - Kyj (Enhancement)
    - Ransomware - NightSpire (Enhancement)
    - Ransomware - Nitrogen (Enhancement)
    - Ransomware - RA World (Enhancement)
    - Ransomware - REVRAC (Enhancement)
    - Ransomware - RTRUE (Enhancement)
    - Ransomware - Sinobi (Enhancement)
    - Ransomware - THRSX (Enhancement)
    - Ransomware - UraLocker (Enhancement)
    - Ransomware - Vatican (Enhancement)
    - Ransomware - Ziver (Enhancement)
- **SAM Signatures**
  - Impacket dcomexec Execution (New)
  - Low Reputation Script Download (New)
- **Application Control Policy**
  - Inline tenant control for Intralinks (New)
- **XDR Indications of Attack**
  - **Threat Prevention**
    - Known C2 Frameworks (Enhancement)
    - Suspicious Network Activity (Domains) (Enhancement)
  - **Threat Hunting**
    - Abnormal SAMR Activity (New)
  - **Anomaly Detection**
    - Abnormal SSH/TELNET Activity (Enhancement)
    - Abnormal Outbound SSH/Telnet over Non-Standard Ports Activity (New)
    - Unusual Outbound Remote Access Tool Activity from a Site (New)
- **Device Inventory**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - **Networking**
      - FortiSwitch (New)
    - **Server**
      - VMware Virtual Machine (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
