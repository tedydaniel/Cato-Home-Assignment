---
title: "Product Update - October 14, 2024"
slug: "product-update-october-14-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-october-14-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - October 14, 2024

## New Features and Enhancements

- **New Best Practice Check for Socket Site Resilience and Recovery:** Cato's [WAN Recovery feature](/v1/docs/socket-site-resiliency-with-wan-recovery-1) is one of multiple recovery features that provide resiliency if your Socket sites can't communicate using the Cato Cloud. We are introducing a Best Practice check to verify that WAN Recovery is enabled on your Socket sites.
  - The check is 'Passed' when all sites are configured correctly for WAN recovery. Otherwise, the check shows the sites that are not ready.
- **Static MAC Entry for Socket Sites:** To support connectivity with devices that do not support ARP, you can now manually add the MAC addresses as a static entry for Socket sites in the [Site Configuration > Advanced Configuration](/v1/docs/advanced-configurations-for-a-site) page.
  - Available for Socket v20 and higher
- **New IdPs for SSO Authentication:** [JumpCloud](/v1/docs/configuring-jumpcloud-sso-for-your-account) and [SafeNet Trusted Access](/v1/docs/configuring-safenet-trusted-access-sso-for-your-account) can now be used by remote users to authenticate with SSO.
- **DEM for App Performance and User Experience:** Starting Nov. 3, 2024, we are releasing the enhanced [Digital Experience Monitoring](/v1/docs/what-is-cato-experience-monitoring) (DEM), which proactively monitors the performance of sites, users, and apps. You can seamlessly start using DEM without deploying any agents or configurations.
  - [Network path analysis](/v1/docs/experience-monitoring-connection-details) to pinpoint issues for sites and users
    - DEM for remote users requires installing the Cato Client, but no SDP license
  - Identify user experience anomalies in your account
  - Create scheduled reports that summarize the overall account experience and highlight top issues
  - An additional license is required for DEM features

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - ElonMuskIsGreedy - Ransomware (New)
    - Socks5Systemz - CnC Connection (New)
    - Bixi Ransomware - (Enhancement)
    - Cipher (Proton) Ransomware - (Enhancement)
    - Dark Eye Ransomware - (Enhancement)
    - Defi Ransomware - (Enhancement)
    - Eject Ransomware - (Enhancement)
    - Foxtrot Ransomware - (Enhancement)
    - Pgp Ransomware - (Enhancement)
    - Secdojo Ransomware - (Enhancement)
    - Shadaloo Ransomware - (Enhancement)
    - Solution Ransomware - (Enhancement)
    - Stop/Djvu Ransomware - (Enhancement)
    - Stormous Ransomware - (Enhancement)
    - The Bully Ransomware - (Enhancement)
    - ZAKI ESCOVINDA Ransomware - (Enhancement)
    - CVE-2024-38816 (New)
    - CVE-2024-38200 (New)
    - CVE-2024-25852 (New)
    - CVE-2023-47253 (New)
    - CVE-2024-20439 (Enhancement)
    - CVE-2021-28799 (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Download pstools heuristic (New)
    - Download Rclone Official Site (New)
    - LNK File Download over HTTP (New)
    - Ngrok agent established tunnel - new domains (New)
    - PsExec After Downloading PsTools (New)
    - ScreenConnect Download (New)
- **Apps Catalog**
  - More than 100 new Cloud apps (see Apps Catalog):
    - SmartRoom (New)
    - Azure Digital Twins (Enhancement)
    - Barco (Enhancement)
    - Carlsberg Breweries A/S (Deprecated)
    - Centrastage renamed to Datto RMM (Enhancement)
    - Egnyte (Enhancement)
    - OpenVPN protocol (Enhancement)
    - Squarespace (Enhancement)
    - Zscaler (Enhancement)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following apps:
    - Granular App: Dropbox Download Multiple Files (New)
    - Granular App: OneDrive Sync files (Enhancement)
    - Granular App: YouTube - Watch (Enhancement)
- **TLSi:**
  - ChatGPT native client on MacOS - default bypass
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT:
      - Docking Station
        - Action Star (Enhancement)
      - Printer
        - Xerox (Enhancement)
        - Zebra (Enhancement)
      - VoIP
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
    - OT, IOT
      - Power Device
        - APC (Enhancement)
        - Eaton (Enhancement)
    - Mobile:
      - Mobile Phone
        - Samsung (Enhancement)
    - Networking:
      - Network Appliance
        - Aruba Networks (Enhancement)
        - Netgear (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
