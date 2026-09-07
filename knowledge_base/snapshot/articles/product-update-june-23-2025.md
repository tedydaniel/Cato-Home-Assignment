---
title: "Product Update - June 23, 2025"
slug: "product-update-june-23-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-june-23-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 23, 2025

## New Features & Enhancements

- **Introducing Cato XOps - Providing Actionable AI-Driven Insights:** XOps is Cato’s analytics layer that unifies Security Detection & Response and AIOps to provide insights and guided remediation tools to help you efficiently detect, respond to, and resolve security and operational incidents.
  - XOps enables Detection & Response stories that show insights correlated from billions of events to identify potential incidents and issues
    - On **August 6, 2025**, the existing Detection & Response stories that were part of the XDR Core offering are transitioning to the enhanced XOps service and license, including: [Threat Prevention](/v1/docs/drilling-down-and-analyzing-xops-security-stories), [network](/v1/docs/sase-detection-response-xops-1) and operations, and third-party data. The [Stories Overview](/v1/docs/sase-detection-response-xops-1) and [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) will also require the XOps license.
  - No impact for XDR Pro customers, and they can seamlessly renew to the XOps license
  - Please contact your Cato representative to learn more about migration plans
- **Overview Dashboard Shows Key Account Metrics:** We are introducing the [Account Overview dashboard](/v1/docs/using-the-overview-dashboard), providing a unified view of important data across your entire account. This new dashboard offers at-a-glance visibility, helping admins quickly assess network health, security posture, site status, and usage trends.
  - Available in the Home > Overview page
  - Includes high-level insights for [Experience Monitoring](/v1/docs/using-the-experience-monitoring-page), the [Stories dashboard](https://support.catonetworks.com/hc/en-us/articles/10432821788573-Working-with-the-Stories-Overview), and the [Devices dashboard](/v1/docs/using-the-device-dashboard) for all customers
  - Click [here](https://academy.catonetworks.com/customer-overview-page) to watch a video recording of this feature
- **New Release for macOS Client v5.9:** During the week of June 22, 2025, we are starting the rollout of the new [Client version 5.9](/v1/docs/summary-of-cato-macos-client-releases) for macOS. This version includes:
  - Bug fixes and enhancements, including:
    - Improved the Client flows for better connection and reconnection times, and reduced errors

## PoP Announcements

- **Sapporo JP:** A new Cato PoP is now available in Sapporo with the IP range 150.195.221.0/24.
  - The Sapporo PoP location was previously available on a limited basis
- New ranges are now available for these PoP locations:
  - **Ashburn, US:** 199.27.40.0/24
  - **Taipei, TW:** 202.75.246.0/24
  - **Tokyo, JP:** 113.30.128.0/24

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2020-0618 (New)
    - CVE-2021-20125 (New)
    - CVE-2023-20118 (New)
    - CVE-2023-22047 (New)
    - CVE-2024-12987 (New)
    - CVE-2024-6235 (New)
    - CVE-2024-7591 (New)
    - CVE-2025-24016 (New)
    - CVE-2025-26670 (New)
    - CVE-2025-2778 (New)
    - CVE-2025-32714 (New)
    - CVE-2025-49113 (New)
    - CVE-2025-5086 (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget ActivitySurrogateSelector (Enhancement)
    - Heuristic - SSH Tunneling via ICMP Protocol (New)
    - Malware- Ducktail-Payload Communication (New)
    - Malware- GhostSocks CnC Activity (New)
    - Ransomware - 9062 (New)
    - Ransomware - Adobe (Enhancement)
    - Ransomware - AMERILIFE (New)
    - Ransomware - APEX (Enhancement)
    - Ransomware - ARCH WIPER (Enhancement)
    - Ransomware - Arrow (Enhancement)
    - Ransomware - Asulo (Enhancement)
    - Ransomware - Backups (Enhancement)
    - Ransomware - BlackHeart (MedusaLocker) (Enhancement)
    - Ransomware - Data (Enhancement)
    - Ransomware - DataLeak (Enhancement)
    - Ransomware - Datarip (Enhancement)
    - Ransomware - EnCiPhErEd (Enhancement)
    - Ransomware - Harma (Enhancement)
    - Ransomware - Hazard (MedusaLocker) (Enhancement)
    - Ransomware - Hero (Enhancement)
    - Ransomware - ITSA (Enhancement)
    - Ransomware - Midnight (Enhancement)
    - Ransomware - NightSpire (Enhancement)
    - Ransomware - Ololo (Enhancement)
    - Ransomware - PANDA (Enhancement)
    - Ransomware - Pgp (Enhancement)
    - Ransomware - Puld (Enhancement)
    - Ransomware - SafeLocker (Enhancement)
    - Ransomware - Smile (Enhancement)
    - Ransomware - SparkLocker (Enhancement)
    - Ransomware - StarFire (Enhancement)
    - Ransomware - TXTME (Enhancement)
    - Ransomware - Veluth (Enhancement)
    - Ransomware - ZV (Enhancement)
- **Suspicious Activity Monitoring**
  - The name of the following SAM signatures have been changed:

| Previous Name | New Name |
| --- | --- |
| cid_sam_atera_agent_probe_activity | cid_sam_rmm_atera_agent_beacon_activity |
| cid_sam_downloading_splashtop_streamer_prerequisite_handler_from_manageengine | cid_sam_rmm_splashtop_download_streamer_prerequisite_handler_from_manageengine |
| cid_sam_anydesk_remote_desktop_connection | cid_sam_rmm_anydesk_remote_connection_desktop |
| cid_sam_rmm_zoho_assist_unattended_1 | cid_sam_rmm_zoho_assist_connection_unattended_1 |
| cid_sam_rmm_zoho_assist_unattended_3 | cid_sam_rmm_zoho_assist_connection_unattended_3 |
| cid_sam_rmm_zoho_assist_unattended_general | cid_sam_rmm_zoho_assist_connection_unattended_general |
| cid_sam_screenconnect_remote_connection_3 | cid_sam_rmm_screenconnect_connection_3 |
| cid_sam_simplehelp_lateral_remote_connectivity_direct | cid_sam_rmm_simplehelp_connection_lateral_direct |
| cid_sam_teamviewer_wan_lateral_remote_connectivity | cid_sam_rmm_teamviewer_connection_wan_lateral_remote |
- **Apps Catalog**
  - More than 20 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - WhatsApp (Enhancement)
    - RDP over TLS (New)
    - SSH over TLS (New)
    - Microsoft Azure (Enhancement)
    - Remote MCP Server (Enhancement)
    - Jetbrains AI (New)
- **XDR Indications Of Attack Signatures:**
  - **Anomaly Detection:**
    - Abnormal LDAP Search Activity (New)
  - **Threat Prevention****:**
    - Suspicious Visual Studio Extensions (New)
- **Application Control (CASB and File Control):**
  - **Application Control:**
    - JetBrains - plugin install (New)
    - Visual Studio - extension install (New)
    - GitHub - Clone (Enhancement)
    - ChatGPT - Conversation (Enhancement)
    - ChatGPT - Share Conversation (New)
- **C****lient Classification**
  - Git (New)
  - IntelliJ IDEA (New)
  - GitHub Copilot (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT
      - Video Conferencing
        - Cisco Webex (New)
        - Yealink VC (New)
        - Logitech VC (New)
        - Logitech Tap Scheduler (New)
        - Logitech Tap IP (New)
        - Logitech RoomMate (New)
        - Logitech Rally Bar (New)
        - Logitech Rally Bar Mini (New)
        - Logitech Rally Bar Huddle (New)
        - Logitech MeetUp 2
        - Polycom VC (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
