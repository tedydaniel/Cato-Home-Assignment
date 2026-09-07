---
title: "Product Update - February 17, 2025"
slug: "product-update-february-17-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-february-17-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 17, 2025

## New Features and Enhancements

- **iOS Client v5.5:** iOS Client version 5.5 is available to download for testing [here](https://testflight.apple.com/join/ob2m1ra0) and will be gradually rolled out in the App Store from the week of February 23. The version contains:
  - ​Improved detection of Office Network
  - ​Idle mode enhancements
  - Connectivity flow improvements to reduce the time it takes the Client to connect
  - Bug fixes, including:
    - If detection of Captive Portal is blocked by a network rule, the Client continues to try and reconnect
    - Removed user notification for certificate check when not required
  - Supported from iOS v16.x and higher
- **Network Stories and XDR Enhancements:**
  - **Additional Muting Conditions for Network Stories in XDR:** You can now [mute Network stories](/v1/docs/muting-xops-stories) according to a specific WAN interface or site type. This provides enhanced granularity for muting stories, for example, ISP maintenance windows on a specific WAN interface.
  - **Updated Thresholds for Network Stories in XDR:** To reduce false positives and help you focus on meaningful [Network stories](/v1/docs/reviewing-site-operations-stories), we updated the thresholds for creating the following story types:
    - Link is down
    - LAN port down
    - Alt WAN link down
    - BGP session disconnected
- **View Recent CMA Pages:** For easier navigation, you can now view the 10 CMA pages that you most [recently visited](/v1/docs/welcome-to-the-cma).
- **Share your Feedback on the Product Updates:** Please take a few minutes to [complete our survey](https://www.surveymonkey.com/r/CatoRN) on the Cato weekly Product Updates (release notes). Your input helps us ensure the information we provide is clear, relevant, and useful to you.

## PoP Announcements

- **Marseille, France**: A new range (216.252.182.0/24) will soon be added to the Marseille PoP location.
- **Houston, US**: A new range (199.27.33.0/24) will soon be added to the Houston PoP location.
- **New localized range for Albania:** A new localized IP range (216.252.183.0/28) for Albania (serviced through the Milan PoP location) will soon be available

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2019-10068 (New)
    - CVE-2020-2883 (New)
    - CVE-2021-23758 (Enhancement)
    - CVE-2022-23134 (New)
    - CVE-2023-31447 (New)
    - CVE-2024-12847 (New)
    - CVE-2024-40711 (Enhancement)
    - CVE-2024-41585 (New)
    - CVE-2024-41592 (New)
    - CVE-2024-42640 (New)
    - CVE-2025-21309 (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget ClaimsIdentity (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget DataSet (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget ObjectDataProvider (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget RolePrincipal (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget SessionSecurityToken (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget SessionViewStateHistoryItem (New)
    - Tactical RMM Agent config update (New)
    - Tactical RMM Mesh client check-in (New)
    - Rhadamanthys CnC Activity(New)
    - Malware - Formbook(Enhancement)
    - Malware - Generic InfoStealer(New)
    - Ransomware - BlackLock (Enhancement)
    - Ransomware - BlackPanther (Enhancement)
    - Ransomware - Cloak (Enhancement)
    - Ransomware - Clone (Enhancement)
    - Ransomware - CmbLabs (Enhancement)
    - Ransomware - CryptoFortress (Enhancement)
    - Ransomware - Dark 101 (Enhancement)
    - Ransomware - EByte Locker (New)
    - Ransomware - Hunter (Enhancement)
    - Ransomware - Hyena (Enhancement)
    - Ransomware - innok (Enhancement)
    - Ransomware - King (Enhancement)
    - Ransomware - LCRYPTX (Enhancement)
    - Ransomware - Locked (MedusaLocker) (Enhancement)
    - Ransomware - Mania Crypter (Enhancement)
    - Ransomware - Ncov (Enhancement)
    - Ransomware - Prince (Enhancement)
    - Ransomware - Purgatory (Enhancement)
    - Ransomware - REDKAW (Enhancement)
    - Ransomware - Weaxor (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Enumerating User Rights on Multiple Devices (New)
    - Enumerating Local Administrator Group Members on Multiple Devices (New)
    - Utilizing SAMR to Gain Domain User Data (New)
    - Enumerating Active Sessions in Multiple Devices (New)
    - Utilizing Winreg and Wkssvc to Collect Logged on Users (New)
    - Zoho Assist Download (New)
- **Apps Catalog**
  - More than 100 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)):
    - Formsmash (New)
    - Codeium (New)
    - VMware vCenter Agent (New)
    - NinjaRMM (Enhancement)
    - Druva (Enhancement)
    - Univoip (Enhancement)
    - Bitdefender (Enhancement)
    - Invoca )Enhancement)
    - WPEngine)Enhancement)
    - SalesForce Data Loader )Enhancement)
- **XDR Indications of Attack Signatures:**
  - Threat Prevention:
    - Blocked Outbound OT Traffic (New)
  - Anomaly Detection:
    - Anomalous RDP Activity (New)
- **Application Control (CASB and File Control):**
  - Box – EntraID SSO Login (New)
  - Quillbot - Login (New)
  - OpenAI - Login (New)
  - OneDrive Business & SharePoint – Download (Enhancement)
  - Google Gemini – Upload (New)
- **Data Loss Prevention (DLP):**
  - OneDrive Business & SharePoint – Download (Enhancement)
  - Google Gemini - Upload (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - Networking
      - Network Appliance
        - Aruba Networks (Enhancement)
        - TP-Link WAP (Enhancement)
    - PC
      - Workstation
        - HP (Enhancement)
        - Windows workstation
    - Server
      - Print Server
        - Axis (Enhancement)
        - HP (Enhancement)
    - Mobile
      - Mobile Phone
        - Samsung (Enhancement)
    - Vendors
      - Sony (Enhancement)
      - Apple (Enhancement)
      - Welch Allyn (New)
      - Roche (New)
      - Silex (New)
      - Chuangmi (New)
      - Amazon (Enhancement)
      - Shure (New)
      - Nintendo (New)
      - Motorola (Enhancement)
      - Honeywell (New)
      - Ingersoll-Rand (New)
      - CyberPower Systems (New)
      - UKG (New)
    - IoT
      - Printer
        - Xerox (Enhancement)
      - Smart TV
        - Samsung (Enhancement)
      - Docking Station
        - Action Star (Enhancement)
      - VoIP
        - Aastracom (Enhancement)
        - Grandstream Networks (Enhancement)
        - Ubiquiti (Enhancement)
        - Cisco IP Phone (Enhancement)
        - Siemens OptiIpPhone (Enhancement)
      - Workforce Management Terminal (New)
        - Clock Device (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
