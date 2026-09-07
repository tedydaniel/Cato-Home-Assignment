---
title: "Product Update - May 26, 2025"
slug: "product-update-may-26-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-may-26-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 26, 2025

## New Features & Enhancements

- **Application Control via API Support for Dropbox:** Connecting SaaS apps to Cato lets you understand who is accessing each app and identify suspicious activities or trends even when users are not connected to the Cato Cloud. You can now connect your [Dropbox account](/v1/docs/dropbox-configuring-the-app-activities-integration) to provide visibility into user activities.
  - The Dropbox app is available from the **Integrations Catalog**, under **App Activities**
  - This feature is included in the CASB license
- **New Terraform Modules for AWS vSockets:** We added [new Cato Terraform modules](/v1/docs/using-terraform-with-the-cato-cloud) that create the vSockets and their resources, and attach the deployment to a Transit Gateway.
  - Separate modules for single vSocket and HA deployment
- **Endpoint Visibility from CrowdStrike in Stories Workbench (Early Availability):** We are extending XDR to include incident data from [CrowdStrike](/v1/docs/crowdstrike-configuring-the-xops-integration) to generate stories for endpoint devices to investigate in the Stories Workbench.
  - Configuring the EDR integration enables you to review correlated related stories based on Cato native signals, providing a comprehensive view of EDR and network-based signals within a single XDR platform
  - Stories incorporate data about suspicious activity from CrowdStrike incidents, including:
    - Device and user details
    - Relevant processes, files, registry values, and more
  - Click [here](https://academy.catonetworks.com/crowdstrike-edr-stories-in-xdr) to watch a video recording of this feature
  - We’re looking for more Early Availability (EA) participants, please contact us [ea@catonetworks.com](mailto:ea@catonetworks.com)

## Upcoming Cato Events

- **Join Cato's Product Rewind Session on June 4:** Product Rewind is a fast-paced monthly webinar where we will break down the most compelling product updates from May 2025. See the latest innovations in action with live demos and get practical insights on how these updates can enhance your experience.
  - Register [here](https://academy.catonetworks.com/product-monthly-rewind/269140) for June 4, 12 pm ET

## PoP Announcements

- New ranges are available for the following PoP locations:
  - **London, UK:** 216.252.191.0/24
  - **Sydney, AU:** 202.75.244.0/24

- New ranges will soon be added to these PoP locations:
  - **Ashburn, US:** 199.27.40.0/24
  - **Taipei, TW:** 202.75.246.0/24
  - **Tokyo, JP:** 113.30.128.0/24

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2020-10824 (New)
    - CVE-2020-14993 (New)
    - CVE-2021-35392 (New)
    - CVE-2023-38950 (New)
    - CVE-2024-10486 (New)
    - CVE-2024-2054 (New)
    - CVE-2024-57968 (New)
    - CVE-2025-1743 (New)
    - CVE-2025-2775 (New)
    - CVE-2025-2776 (New)
    - CVE-2025-2777 (New)
    - CVE-2025-2905 (Enhancement)
    - CVE-2025-29809 (New)
    - CVE-2025-32102 (New)
    - CVE-2025-32433 (Enhancement)
    - CVE-2025-32819 (New)
    - CVE-2025-4427 (New)
    - CVE-2025-4428 (New)
    - Kerberosting Attack (New(
    - Malicious Traffic to Low-Popularity Server after Multiple Connections to Malicious IPs (New)
    - Malicious Traffic to Low-Popularity Server after Multiple Connections to Malicious Domains (New)
    - Ransomware - AnarchyRansom (Enhancement)
    - Ransomware - Anubi (Anubis) (Enhancement)
    - Ransomware - APEX (New)
    - Ransomware - Bbq (Enhancement)
    - Ransomware - BlackHeart (MedusaLocker) (Enhancement)
    - Ransomware - CRFILE (Enhancement)
    - Ransomware - Crone (Enhancement)
    - Ransomware - CryptData (Enhancement)
    - Ransomware - Data (Enhancement)
    - Ransomware - Govcrypt (Enhancement)
    - Ransomware - HentaiLocker 2.0 (Enhancement)
    - Ransomware - HexaLocker (Enhancement)
    - Ransomware - ITSA (Enhancement)
    - Ransomware - LegionRoot (Enhancement)
    - Ransomware - Lockedfile (Enhancement)
    - Ransomware - Mkp (Enhancement)
    - Ransomware - NightSpire (Enhancement)
    - Ransomware - PANDA (New)
    - Ransomware - RALEIGHRAD (Enhancement)
    - Ransomware - Se7en (Enhancement)
    - Ransomware - Spyhunter (Enhancement)
    - Ransomware - TXTME (Enhancement)
    - Ransomware - Warning (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the SAM service:
    - Enumeration of Domain Controller Registry Information (associated with SharpHound) (New)
    - Enumeration of Local Groups Users on Devices, Associated with SharpHound (New)
    - Execution of All Component in Sharphound (New)
    - Execution of Computers Only Component in Sharphound (New)
    - Execution of Default Component in Sharphound (New)
    - Suspected Stunnel Activity (New)
- **Apps Catalog**
  - More than 130 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Tor Network (Enhancement)
- **XDR Indications of Attack Signatures:**
  - **Anomaly Detection:**
    - Abnormal Access Attempts to Malicious Targets
    - First Occurrence of WANBOUND Scanning Activity in a Site
    - First Occurrence of WMI Activity in a Site
    - First Occurrence of TeamViewer Activity in a Site
  - **Threat Hunting:**
    - Outbound Communication to Low-Popularity IPs
    - Suspicious Network Activity (User-Agent) (Enhancement)
    - Low Popularity External SSL Self Signed (New)
  - **Threat Prevention**
    - Malware Activity (Enhancement)
    - Blocked Remote Tool Execution Following Reconnaissance Activity (New)
- **Application Control (CASB and File Control):**
  - **Application Control:**
    - Remote MCP Connect (New)
    - Remote MCP List Tools (New)
    - Remote MCP Tool Call (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - **OT**
      - CCTV
        - IDIS (Enhancement)
      - Docking Station
        - Action Star (Enhancement)
      - Multifunction Device
        - Toshiba (Enhancement)
      - Payment Terminal
        - Verifone (Enhancement)
      - Printer
        - HP (Enhancement)
      - Smart TV
        - Samsung (Enhancement)
      - VoIP
        - Cisco (Enhancement)
        - Mitel (Enhancement)
        - Polycom (Enhancement)
    - **Networking**
      - Network Appliance
        - enGenius (Enhancement)
        - Ubiquiti (Enhancement)
      - PC
        - Desktop
          - HP (Enhancement)
        - Laptop
          - Dell (Enhancement)
          - HP (Enhancement)
          - Lenovo (Enhancement)
        - Workstation
          - Apple (Enhancement)
          - Asus (Enhancement)
    - **Mobile**
      - Mobile Computer
        - Honeywell (Enhancement)
      - Mobile Phone
        - Oppo (Enhancement)
        - Samsung (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
