---
title: "Product Update - June 9, 2025"
slug: "product-update-june-9-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-june-9-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 9, 2025

## New Features & Enhancements

- **Enhancements for Best Practice Checks in the CMA:**
  - **Control Which Best Practice Checks are Relevant for your Account:** Ignore items that are not relevant to your environment and focus on actionable recommendations by [enabling/disabling individual Best Practice checks](/v1/docs/reviewing-posture-checks-for-your-account).
    - Disabled Best Practice checks are excluded from the **Cato Score**
  - **Best Practice Check Links to Relevant Policy:** For Best Practice checks that fail to meet the recommended settings, we added a link that directly opens the relevant page to help you quickly remediate the issue.
  - Click [here](https://academy.catonetworks.com/best-practices-page-enhanced) to watch a video recording of this feature
- **Granular Control Over TLS Versions and Cipher Suites in TLS Inspection**: The [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) rules now support enforcing the minimum TLS versions and cipher suite strength. This enhancement reduces exposure to risks associated with legacy encryption protocols and enhances policy flexibility by:
  - Blocking outdated and insecure TLS versions
  - Preventing the use of weak cipher suites in encrypted traffic
  - Aligning encrypted communications with modern cryptographic standards
  - Click [here](https://academy.catonetworks.com/tls-inspection-enforcing-tls-versions-cipher-suites) to watch a video recording of this feature

- **DEM Enhancement - Underlay Performance Monitoring:** The [Experience Monitoring](/v1/docs/understanding-the-experience-monitoring-drill-down-pages) (DEM) page now shows packet loss and distance metrics specific to the last-mile underlay. This helps identify and diagnose out-of-tunnel issues that could impact last-mile performance for Socket sites.
  - The new metrics are shown in the **Underlay Probes** section in the **Last Mile** tab for a specific site
  - Sites require Socket v21.1.18975 (or higher)

- **Improved DEM Drilldown Pages:** Over the next few weeks, we’re releasing redesigned [Experience Monitoring](/v1/docs/understanding-the-experience-monitoring-drill-down-pages) (DEM) pages that make it easier to view and access data when you drill down on an item. This lets you see more information at a glance to quickly assess and diagnose user experience issues.

- **New Report for Network Alerts as Stories:** We're introducing a new **Site Network Story Report** that consolidates network alerts into stories, delivering valuable performance insights. You can generate this report on demand or schedule it to run automatically from the **Home > Reports** page.
  - Requires an ILMM or NOCaaS license
- **Updates to the Cato Terraform Module for Azure:** We are releasing a new [Terraform](/v1/docs/using-terraform-with-the-cato-cloud) module that aligns with Azure's current cloud implementation.
  - The previous module included the deprecated `azurerm_virtual_machine` resource and is now replaced by the `azurerm_linux_virtual_machine` resource
- **Query mDNS Status via the API:** You can now retrieve the mDNS status for a network range with the `mdnsReflector` helper field in the [entityLookup query](https://api.catonetworks.com/documentation/#query-entityLookup).

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2022-31137 (New)
    - CVE-2024-21136 (New)
    - CVE-2024-38475 (New)
    - CVE-2024-6047 (New)
    - CVE-2025-1684 (New)
    - CVE-2025-21377 (New)
    - CVE-2025-25291 (Enhancement)
    - Malware Ballista Malware Botnet (New)
    - Ransomware - Adobe (Enhancement)
    - Ransomware - AnarchyRansom (Enhancement)
    - Ransomware - APEX (Enhancement)
    - Ransomware - ARCH WIPER (Enhancement)
    - Ransomware - Arrow (Enhancement)
    - Ransomware - Asulo (Enhancement)
    - Ransomware - Bbq (Enhancement)
    - Ransomware - BlackHeart (MedusaLocker) (Enhancement)
    - Ransomware - CryptData (Enhancement)
    - Ransomware - Data (Enhancement)
    - Ransomware - Datarip (Enhancement)
    - Ransomware - Govcrypt (Enhancement)
    - Ransomware - Hazard (MedusaLocker) (Enhancement)
    - Ransomware - HentaiLocker 2.0 (Enhancement)
    - Ransomware - ITSA (Enhancement)
    - Ransomware - LegionRoot (Enhancement)
    - Ransomware - Midnight (Enhancement)
    - Ransomware - Mkp (Enhancement)
    - Ransomware - NightSpire (Enhancement)
    - Ransomware - PANDA (Enhancement)
    - Ransomware - RALEIGHRAD (Enhancement)
    - Ransomware - Se7en (Enhancement)
    - Ransomware - Smile (Enhancement)
    - Ransomware - SparkLocker (Enhancement)
    - Ransomware - StarFire (Enhancement)
    - Ransomware - TXTME (Enhancement)
    - Ransomware - Veluth (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the SAM service:
    - Outbound SOCKS5 Proxy traffic on high ports and without authentication (New)
    - Outbound SOCKS5 Proxy traffic on ports 443 or 80 and without authentication (New)
    - Outbound SOCKS5 Proxy traffic to Bulletproof hosting service (New)
    - Outbound SOCKS4 Proxy traffic to Bulletproof hosting service (New)
    - Execution of AT Service on Remote Host (New)
- **Apps Catalog**
  - More than 40 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Tor Network (Enhancement)
- **XDR Indications Of Attack Signatures:**
  - **Anomaly Detection:**
    - Abnormal Access Attempts to Malicious Targets (New)
    - First Occurrence of WANBOUND Scanning Activity in a Site (New)
    - First Occurrence of WMI Activity in a Site (New)
    - First Occurrence of TeamViewer Activity in a Site (New)
  - **Threat Hunting:**
    - Outbound Communication to Low-Popularity IPs (Enhancement)
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
    - **IoT**
      - Payment Terminal
        - Castles Technology (Enhancement)
      - Unidentified IoT
        - Zebra (Enhancement)
      - VoIP
        - Algo (Enhancement)
        - Mitel (Enhancement)
        - Yealink (Enhancement)
      - IP Camera
        - Ubiquiti IP camera(Enhancement)
      - Speaker
        - Amazon Echo
    - **PC**
      - Desktop
        - Dell (Enhancement)
      - Loptop
        - Apple (Enhancement)
        - Dell (Enhancement)
        - Toshiba (Enhancement)
      - Workstation
        - MSI (Enhancement)
    - **Mobile**
      - Mobile Phone
        - Zebra (Enhancement)
    - **Server**
      - Print Server
        - HP (Enhancement)
      - Server
        - Windows Server (Enhancement)
        - Linux Server (Enhancement)
        - Ubuntu Server (Enhancement)
      - NAS
        - I-O Data NAS (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
