---
title: "Product Update - May 15th, 2023"
slug: "product-update-may-15th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-may-15th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 15th, 2023

## Cato SDP Client Releases

- **Linux Client v5.1:** We are planning to release Linux Client v5.1 during the week of **May 22nd**. These are the features and enhancements for this version:
  - **New Device Posture Check Provides Increased Security:** You can now include Anti-Malware, Firewall, Patch Management and Device Certificate checks within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and Security policies. These checks include:
    - Increase access control capabilities by ensuring the SDP users or user groups in the policy have the required device posture before connecting to your network
    - Define Device Posture requirements in your Security policies to access corporate resources
  - **User Awareness Support for Linux Devices:** Cato’s [Identity Agent](https://support.catonetworks.com/hc/en-us/articles/7784362141085) for Linux Clients supports User Awareness for users provisioned with all supported IdPs.
  - **Browserless Support for SSO:** You can now authenticate with SSO on headless devices, without a browser.
    - This is supported on Azure SSO, and requires authenticating via another device.
  - **Support for Cato Automatic Upgrades:** Starting from this version, Linux Clients can be automatically upgraded using the [Cato upgrade service](https://support.catonetworks.com/hc/en-us/articles/4413280522257).
  - For more information about the Client rollout process, see [Client Lifecycle Management](/v1/docs/client-lifecycle-management)

## Security Updates

- **Application Database:**
  - **New Azure Sub-Services Enhance Azure Classification**: We added over 80 Azure sub-services to our application database and you can now set policies for them as specific Azure apps.
    - There is no change to existing policies set for the Azure application
    - Event logs report a specific app ID when a sub-service is identified, instead of the general Microsoft Azure app ID
    - The [Apps Catalog](/v1/docs/using-the-app-catalog) includes a detailed description for each new Azure sub-service app
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Telegram Voice Call
  - Enhanced these SaaS applications:
    - Telegram
    - Kakao Corp Services
    - KakaoTalk
    - Rakuten
- **IPS Signatures:**
  - Ransomware Rea (New)
  - Malware IcedID (Enhancement)
  - CVE-2017-0144/EternalBlue/MS17-010 (Enhancement)
  - CVE-2023-29324
  - CVE-2022-4732
  - CVE-2022-29775
  - CVE-2022-24990
  - CVE-2021-21243
  - CVE-2020-5741
  - CVE-2019-13585
- **Suspicious Activity Monitoring:**
  - Curl response RCE (New)
  - Lateral WinSCP transfer (Enhancement)
  - Lateral Netcat transfer (Enhancement)
  - Downloaded NetCat (Enhancement)
- **Application Control Policy (CASB):**
  - Enhanced granular actions for the following app:
    - Box: Upload
- **Data Loss Prevention (DLP):**
  - Support added for script files, including: VBS, VBE, WSF, WSC, BAT
  - Added these new file types:
    - Executables: MSI, DLL, HTA
    - Archives: CAB
    - Other file types: Flash, Torrent

## PoP Announcements

- **Vancouver, Canada:** A new Cato PoP will shortly become available in Vancouver.
- **Frankfurt, Germany:** A second Cato PoP will shortly become available in Frankfurt.
