---
title: "Product Update - March 3, 2025"
slug: "product-update-march-3-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-march-3-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - March 3, 2025

## New Features & Enhancements

- **New Monitoring for Socket CPU Usage:** Use the CMA to monitor metrics for Socket CPU usage, and identify if the Socket CPU is related to performance issues for a site.
  - Available for all customers in the Site Monitoring > [Network Analytics](/v1/docs/showing-the-site-network-analytics) page for a site
  - Customers with a DEM license can also view the Socket CPU metrics as part of [path analysis](/v1/docs/experience-monitoring-connection-details) and other tools
  - Required Socket versions:
    - For physical Sockets - from v21.1
    - For vSockets - from v22.0
  - Click [here](https://academy.catonetworks.com/socket-cpu-usage-metrics/) to watch a video recording of this feature
- **App Activities via API for the GitHub SaaS App:** Extend your CASB App Control functionality by connecting your corporate [GitHub tenant](/v1/docs/github-configuring-the-app-activities-integration) to Cato. This lets you understand who is accessing it and identify suspicious activities or trends even when users are not connected to the Cato Cloud.
  - The GitHub App is available from the Resources > Integrations Catalog, under **App Activities**
  - Requires a CASB license

- **New Regions for vSockets from AWS Marketplace:** AWS vSockets are now available from the Marketplace in these additional AWS regions:
  - Thailand (ap-southeast-7)
  - Malaysia (ap-southeast-5)
  - Mexico (mx-central-1)

- **API Support for Secondary vSockets:** To enable full end-to-end API support to automate creating HA vSocket sites, we added the following [new APIs](https://api.catonetworks.com/documentation/#group-Operations-Mutations) for secondary vSockets in AWS and Azure:
  - addSecondaryAwsVSocketInput
  - addSecondaryAzureVSocketInput

- **View and Investigate Apps Used in Your Environment:** We improved the [Cloud Apps Dashboard](https://support.catonetworks.com/hc/en-us/articles/24373642591389-Working-with-the-Cloud-Apps-Dashboard) for better visibility of the apps used in your environment. You can now:
  - View every app accessed by your users, previously only the top 5 were shown
  - Use the app filter to refine the entire dashboard view based on a specific app

## PoP Announcements

- **Ashburn, US**: A new range (149.20.197.0/24) will soon be added to the Ashburn PoP location.
- **Cincinnati, US**: A new range (199.27.35.0/24) will soon be added to the Cincinnati PoP location.
- **Portland, US**: A new range (199.27.34.0/24) will soon be added to the Portland PoP location.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2021-20123 (New)
    - CVE-2021-35394 (New)
    - CVE-2021-42237 (New)
    - CVE-2023-1162 (New)
    - CVE-2023-50094 (New)
    - CVE-2024-27172 (New)
    - CVE-2024-29895 (New)
    - CVE-2024-39914 (New)
    - CVE-2024-43468 (New)
    - CVE-2024-55591 (New)
    - CVE-2024-57727 (New)
    - CVE-2025-0108 (New)
    - CVE-2025-21309 (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget AxHostState (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget TextFormattingRunProperties (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget TypeConfuseDelegate (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget WindowsIdentity (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget WindowsPrincipal (New)
    - Heuristic - Fake Captcha Detection - New Variant (New)
    - Ransomware - BlackLock (Enhancement)
    - Ransomware - Bot (New)
    - Ransomware - Cerber (Enhancement)
    - Ransomware - CipherLocker (Enhancement)
    - Ransomware - Cloak (Enhancement)
    - Ransomware - CmbLabs (Enhancement)
    - Ransomware - Crypt (MedusaLocker) (Enhancement)
    - Ransomware - CryptoFortress (Enhancement)
    - Ransomware - DeathHunters (Enhancement)
    - Ransomware - ETHAN (Enhancement)
    - Ransomware - FOX (Enhancement)
    - Ransomware - Heda (Enhancement)
    - Ransomware - Hunter (Enhancement)
    - Ransomware - Hunter (Prince) (Enhancement)
    - Ransomware - Hunters (Xorist) (Enhancement)
    - Ransomware - King (Enhancement)
    - Ransomware - LCRYPTX (Enhancement)
    - Ransomware - Loches (New)
    - Ransomware - LockBit 3.0 (Enhancement)
    - Ransomware - Locked (MedusaLocker) (Enhancement)
    - Ransomware - Lucky (MedusaLocker) (Enhancement)
    - Ransomware - Mania Crypter (Enhancement)
    - Ransomware - Ncov (Enhancement)
    - Ransomware - Purgatory (Enhancement)
    - Ransomware - REDKAW (Enhancement)
    - Ransomware - Vgod (Enhancement)
    - Ransomware - Weaxor (Enhancement)
    - Scanners - Sipvicious Scanner (New)
- **Suspicious Activity Monitoring:**
  - This protection was added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Zoho Assist Download (Enhancement)
- **Apps Catalog**
  - More than 100 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)):
    - BeyondTrust (New)
    - Tidal Security (New)
    - Dalival (New)
    - NinjaRMM (Enhancement)
    - Obic Business Consultants (Enhancement)
    - Google Ads (Enhancement)
    - ExtremeCloud IQ (Enhancement)
    - Smash )New)
    - Five9 )Enhancement)
- **XDR Indications of Attack Signatures:**
  - Threat Prevention:
    - Fake CAPTCHA Detection (Enhancement)
  - Threat Hunting:
    - Monitored Outbound OT Communication (New)
  - Anomaly Detection:
    - File Transfer Protocol Anomaly (New)
- **Application Control (CASB and File Control):**
  - ChatGPT Conversation (Enhancement)
  - Microsoft Teams Upload (Enhancement)
  - GitHub Upload (via browser)
  - GitHub Download (via browser)
- **Data Loss Prevention (DLP):**
  - GitHub Upload (via browser)
  - GitHub Download (via browser)
- **File Control**
  - IPA (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - **IOT**
      - Docking Station
        - Action Star (Enhancement)
      - Multifunction Device
        - Toshiba (Enhancement)
      - Printer
        - Epson (Enhancement)
      - Smart TV
        - LG (Enhancement)
        - Samsung (Enhancement)
      - VoIP
        - Aastracom (Enhancement)
        - Ubiquiti (Enhancement)
    - Mobile
      - Mobile Phone
        - Google (Enhancement)
        - Samsung (Enhancement)
    - Networking
      - Network Appliance
        - Aruba Networks (Enhancement)
    - PC
      - Workstation
        - Apple (Enhancement)
        - HP (Enhancement)
      - Laptop
        - Dell (Enhancement)
        - HP (Enhancement)
        - Toshiba (Enhancement)
    - Server
      - Print Server
        - Axis (Enhancement)
        - HP (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
