---
title: "Product Update - Feb. 19th, 2024"
slug: "product-update-feb-19th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-feb-19th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Feb. 19th, 2024

## New Features & Enhancements

- **Security Events Enriched with Full Network Context**: We enriched our Security events with extensive Network data to provide insights and better visibility. For example, using an Internet Firewall event you can now troubleshoot whether the flow was TLS inspected or bypassed and which Network Rule matches it, as well as the QoS priority value and the PoP’s Public Source IP.
  - [New fields](/v1/docs/understanding-event-fields) include:
    - TLS Inspection
    - Network Rule
    - Public Source IP
    - TCP Acceleration
    - Egress PoP Name
    - Egress Site
    - QoS Priority
    - Congestion Algorithm
    - Source Port
    - Host MAC Address
  - We’re gradually releasing these fields over the next few weeks. Queries from earlier than February 5th won’t retrieve events with the enriched fields
  - The new fields are supported in the Cato Management Application only. Support for exporting these fields to third-party systems with eventsFeed API will be available in the future
- **New XDR Detections Report Includes All Security Stories**: The new [XDR Detections](/v1/docs/generating-an-xops-detections-report) report summarizes all the XDR Security stories detected for your account, regardless of whether the stories were investigated. This helps you highlight the comprehensive threat detection capabilities of Cato XDR for relevant stakeholders in the organization. The new report complements the existing XDR Investigations report, which focuses on stories that underwent investigation.
  - The XDR Detections report includes data such as:
    - Number of stories created with breakdown by Criticality
    - Most common sites and indications of attack in XDR stories
  - Available for XDR Core and XDR Pro customers
- **Topology Page Includes Users Connected in Office Mode:** The number of **Connected SDP Users** on the [Topology page](/v1/docs/using-the-topology-page) now includes users connected in Office Mode, behind a site.
  - This aligns the Topology page with the [SDP User Dashboard](/v1/docs/using-the-access-overview-page) and the Users page

## PoP Announcements

- **Tokyo, JP:** A new IP range will soon become available in the Tokyo PoP location - 150.195.219.0/24

## Knowledge Base Updates

- [Understanding the Cato Client Connection Flow](/v1/docs/understanding-the-cato-client-connection-flow)

## Video Feature Overviews

- [Enforce Policies Based on User Location](https://support.catonetworks.com/hc/en-us/articles/16843923226013-Enforce-Policies-Based-on-User-Location-Video)
- [Exact Data Matching for DLP](https://support.catonetworks.com/hc/en-us/articles/16844090555293-Exact-Data-Matching-for-DLP-Video)
- [Full Context Enriched Events](https://support.catonetworks.com/hc/en-us/articles/16843816501533-Full-Context-Enriched-Events-Video)
- [Windows Client v5.10](https://support.catonetworks.com/hc/en-us/articles/16843994103325-Windows-Cato-Client-v5-10-Video)

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Ransomware Chaos (New)
    - Ransomware Dx31(New)
    - Ransomware Fastbackdata (New)
    - Ransomware New24 (New)
    - Ransomware Shiel (New)
    - Ransomware Stop/Djvu (New)
    - Ransomware ThreeAM (New)
    - Malware DanaBot (New)
    - Malware Lazagne Download
    - Malware Lumma Stealer CnC Communication - Configuration Request Attempt
    - Malware njRAT CNC Communication - Callback
    - CVE-2024-23897 (New)
    - CVE-2023-7028 (New)
    - CVE-2023-6021 (New)
    - CVE-2023-43177 (New)
    - CVE-2023-4168 (New)
    - CVE-2023-39677 (New)
    - CVE-2023-38203 (New)
    - CVE-2023-35082 (New)
    - CVE-2023-22527 (New)
    - CVE-2019-3967 (New)
    - CVE-2023-45484 (Enhancement)
    - CVE-2023-45480 (Enhancement)
    - Threat Actor r00ts3c-owned-you (New)
- **Detection & Response**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Device fingerprint sending via user agent (Enhancement)
      - Remote Psexec Service Execution (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Ngrok agent established tunnel with Ngrok cloud (New)
    - PuTTY Download (New)
    - Wininet/Winsock (Native Windows Client) to low Popularity (New)
    - SSH to a Low reputation IP (Enhancement)
- **Apps Catalog:**
  - Added over 300 new SaaS applications including (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)):
    - AoL
    - Open VPN protocol
    - OpenVPN
    - Mullvad VPN
  - Enhanced these applications:
    - ADguard
    - Siri
    - Apple
    - Apple Software
    - Applovin
    - Aruba Networks
    - Atlassian
    - Autodesk
    - Blp
    - Bluejeans
    - Bytedance
    - Cisco
    - DailyMotion
    - ExpressVPN
    - Facebook Messenger
    - Flurry
    - Google Play
    - Grammarly
    - Jetbrains
    - Line
    - NBC
    - Nianticlabs
    - NordVPN
    - Okta
    - OpenAI
    - Optimove
    - Sharepoint
    - Slack
    - Speedtest net
    - Statuspage
    - Thomsonreuters
    - Twilio
    - WeChat
    - Zscaler
- **Application Control (CASB and DLP):**
  - Enhanced granular actions for the following apps:
    - Box - Upload
    - Slack - Delete Message
  - Enhanced DLP content matching for the following app:
    - Outlook Upload - Improved TXT and CSV file coverage
- **File Identification:**
  - Enhanced file identification in Cato Cloud services for the following file type:
    - OpenVPN config file

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
