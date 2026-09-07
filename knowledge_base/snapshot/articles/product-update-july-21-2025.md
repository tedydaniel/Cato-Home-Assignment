---
title: "Product Update - July 21, 2025"
slug: "product-update-july-21-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-july-21-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 21, 2025

## New Features & Enhancements

- **Enhanced Admin Experience for Managing the Always-On Policy at Scale:** We improved management of the [Always-On Policy](/v1/docs/protecting-users-with-always-on-security) with the following features:
  - Ability to [modify the policy](/v1/docs/working-with-policy-revisions) in parallel by multiple admins
  - A faster and more responsive page for policies with many rules
  - Public API support will be available soon
- **New Release for iOS Client v5.6:** Starting the week of July 21, 2025, a new Client version 5.6 for iOS will be available for download in the App Store. This version includes:
  - Support for [Internet recovery](/v1/docs/protecting-users-with-always-on-security) when a connection to Cato can’t be established
    - Previously, this was only supported for Windows and macOS Clients
  - Support for users to control temporarily [bypassing Always-On](/v1/docs/protecting-users-with-always-on-security#h_01JZ52JT48NAQ2345KZJW0ZNP3)
    - Previously, this was only supported for Windows and macOS Clients
  - Security update: Client embedded browser upgraded to Chromium version 135.0.220
  - Performance enhancements and bug fixes
  - Click [here](https://academy.catonetworks.com/cato-client-releases-ios-v56) to watch a video recording of this feature
- **Improved Management of IoC Lists using Containers:** To provide increased granularity, flexibility, and control of threat intelligence data, you can make the following updates to [Containers](/v1/docs/integrating-custom-ioc-lists-with-containers) (Resources > Categories > Containers):
  - Add or remove individual IoCs within a Container
  - Create new Containers without uploading a file
  - View and search IoCs within a Container
  - Click [here](https://academy.catonetworks.com/ioc-management-enhancements) to watch a video recording of this feature
- **CMA Notifications for Shipping Page:** The [Shipping page](/v1/docs/monitoring-socket-shipping) lets you manage hardware shipments more efficiently, including: enter and validate shipping addresses, and import/export CSV files. Now you can also receive CMA notifications when shipping details are missing for hardware orders.
  - The **Hardware and Shipping** notifications are enabled by default, you can manage them in the [Account > System Notifications page](/v1/docs/account-level-alerts-and-system-notifications)

## PoP Announcements

**Oslo, NO:** A new Cato PoP is now available in Oslo with the IP range 85.255.22.0/24

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2017-7921 | Hikvision IP Camera Authentication Bypass
    - Darkness Ransomware (Enhancement)
    - Ziver Ransomware (Enhancement)
    - Sinobi Ransomware (Enhancement)
    - BlackFL Ransomware (Enhancement)
    - Blocker Ransomware (Enhancement)
    - Kyj Ransomware (Enhancement)
    - Vatican Ransomware (Enhancement)
    - Blackransombdbot Ransomware (Enhancement)
    - KaWaLocker Ransomware (Enhancement)
    - UraLocker Ransomware (Enhancement)
    - THRSX Ransomware (Enhancement)
    - Dire Wolf Ransomware (Enhancement)
    - DELTA Ransomware (Enhancement)
    - AMERILIFE Ransomware (Enhancement)
    - DataLeak Ransomware (Enhancement)
    - Puld Ransomware (Enhancement)
    - Backups Ransomware (Enhancement)
    - ZV Ransomware (Enhancement)
    - SafeLocker Ransomware (Enhancement)
    - NightSpire Ransomware (Enhancement)
    - BlackHeart (MedusaLocker) Ransomware
    - EnCiPhErEd Ransomware (Enhancement)
    - Pgp Ransomware (Enhancement)
    - Harma Ransomware (Enhancement)
    - CVE-2025-34085 (New)
    - CVE-2019-18211 (New)
    - CVE-2025-32813 (New)
    - CVE-2025-5777 (Enhancement)
    - CVE-2025-33071 (New)
    - CVE-2025-33070 (New)
    - CVE-2025-33053 (New)
    - CVE-2025-32756 (New)
    - CVE-2022-44356 (New)
    - CVE-2025-5777 (New)
    - Fake Captcha Detection (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the SAM service:
    - Access Executable on External WebDAV Server
    - Utilizing ADWS to Gain Domain Information, Associated with SoapHound
- **Apps Catalog**
  - New Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Kandji (Enhancement)
    - Japanese apps (New)
    - datart (New)
    - gen ai apps (New)
    - ultraviewer (New)
    - WhatsApp (Enhancement)
- **XDR Indications Of Attack Signatures:**
  - **Anomaly Detection:**
    - Abnormal Suspicious Activity
    - Abnormal ICMP Network Scanning Activity
- **Application Control (CASB and File Control):**
  - **Application Control:**
    - Granular App: Adobe Creative Cloud - Login (New)
    - Granular App: Adobe Creative Cloud – Upload (new)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - Generic Server (Enhancement)
    - Unidentified IoT (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
