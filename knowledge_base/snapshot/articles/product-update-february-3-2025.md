---
title: "Product Update - February 3, 2025"
slug: "product-update-february-3-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-february-3-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 3, 2025

## New Features and Enhancements

- **Reminder - New Default Cato Certificate for TLS Inspection:** Following the [announcement](/v1/docs/product-update-november-11-2024) on November 11, 2024, the default Cato certificate used by the TLS Inspection policy and Threat Prevention engines expires on October 29, 2025. You must complete the migration process before the current certificate expires.
  - You can download the new certificate from the [Security > Certificate Management page](/v1/docs/managing-certificates-for-tls-inspection), and then [distribute](/v1/docs/distributing-and-installing-device-certificates) it to your organization
  - After **October 29, 2025**, customers who haven’t migrated to the new certificate will experience the following issues:
    - TLS Inspection won’t function properly
    - The Threat Prevention services won’t be able to inspect traffic encrypted with TLS
    - Users may experience issues accessing the Internet and SaaS apps (HTTPS websites)
  - See this [FAQ](https://support.catonetworks.com/hc/en-us/articles/22781778613149-Frequently-Asked-Questions-for-the-New-Default-Cato-Certificate-for-TLS-Inspection) for more information
- **CMA Enhancements:**
  - 
    - **Improved Visibility of Integrated Apps:** On the [Resources > Integrations page](/v1/docs/using-the-integrations-page), the **Integrated Apps** tab displays the SaaS Apps you have integrated, the integration status, and the capabilities enabled for each app.
    - **New Name for SaaS Security APIs:** We are updating the name of the **SaaS Security API** to **Data Protection API** to reflect its functionality better.
      - No change to functionality or license requirements
      - For more information about App & Data protection, see these [articles](/v1/docs/app-control-data-protection)
    - **New Location for Devices Page:** The [Devices](/v1/docs/using-the-device-inventory-page) page has moved from the Resources tab to the Home tab.

## PoP Announcements

- **Chicago, United States:** A new range (216.205.127.0/24) is now available for the Chicago PoP location.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2021-4445 (New)
    - CVE-2022-23227 (New)
    - CVE-2022-26138 (Enhancement)
    - CVE-2022-26148 (New)
    - CVE-2023-28461 (Enhancement)
    - CVE-2024-11972 (New)
    - CVE-2024-1483 (New)
    - CVE-2024-20419 (Enhancement)
    - CVE-2024-39205 (New)
    - CVE-2024-50550 (New)
    - CVE-2024-56145 (New)
    - CVE-2024-9047 (New)
    - Insecure Deserialization ActivitySurrogateDisableTypeCheck (New)
    - Insecure Deserialization ActivitySurrogateSelector (New)
    - Ransomware - Aptlock (Enhancement)
    - Ransomware - BlackPanther (Enhancement)
    - Ransomware - Clone (Enhancement)
    - Ransomware - Dark 101 (Enhancement)
    - Ransomware - Hyena (Enhancement)
    - Ransomware - innok (Enhancement)
    - Ransomware - Locked (MedusaLocker) (Enhancement)
    - Ransomware - NoDeep (Enhancement)
    - Ransomware - Prince (Enhancement)
    - Ransomware - RA World (Enhancement)
    - Ransomware - Risen (Enhancement)
    - Ransomware - SatanCD (Enhancement)
    - Ransomware - Weaxor (Enhancement)
    - Ransomware - YE1337 (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Collecting System Info on a Remote Computer, PsInfo (New)
- **Apps Catalog**
  - More than 130 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)):
    - HP Printer Signaling (New)
    - Formsmash (New)
    - DeepSeek )New)
    - Microsoft Defender For Endpoint )Enhancement)
    - ExtremeCloud IQ )Enhancement)
    - Suno (New)
- **XDR Indications of Attack Signatures:**
  - Threat Prevention:
    - Potential Downloader (New)
  - Anomaly Detection:
    - Failed User Login Anomaly (New)
    - Download Events Anomaly (New)
    - Upload Events Anomaly (New)
    - Unusual Deletion Activity (New)
    - Unusual File Creation Activity (New)
    - C&C Traffic Anomaly (Enhancement)
    - Mail Deletion Anomaly (New)
- **Application Control (CASB and File Control):**
  - Wordtune - Login (New)
  - Wordtune - Upload (New)
  - Wordtune – Writing Assistance (New)
  - Quillbot – Writing Assistance (New)
  - Claude – Login (New)
  - Claude – Upload (New)
  - Granular activities of the applications:
    - Dropbox
    - ChatGPT
    - Google Drive
    - Outlook Now have an additional "Username" field, allowing more flexibility on tenant control for these activities. This feature is expected to work for browser access.
- **Data Loss Prevention (DLP):**
  - Wordtune - Upload (New)
  - Wordtune – Writing Assistance (New)
  - Quillbot – Writing Assistance (New)
  - Claude – Login (New)
  - Claude – Upload (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - Networking
      - Network Appliance
        - Aruba Networks (Enhancement
    - PC
      - Workstation
        - HP (Enhancement)
    - Mobile
      - Mobile Phone
        - Samsung (Enhancement)
      - Tablet
        - Samsung (Enhancement)
    - IoT
      - Printer
        - Xerox (Enhancement)
      - Single Board Computer
        - Raspberry Pi Foundation (Enhancement)
      - VoIP
        - Aastracom (Enhancement)
        - Innovaphone (Enhancement)
        - Mitel (Enhancement)
        - Yealink (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
