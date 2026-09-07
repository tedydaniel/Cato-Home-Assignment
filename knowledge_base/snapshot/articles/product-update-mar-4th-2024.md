---
title: "Product Update - Mar. 4th, 2024"
slug: "product-update-mar-4th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-mar-4th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Mar. 4th, 2024

## New Features & Enhancements

- **New Device Posture Check for Cato Client Version:** You can require that devices connecting to the network have a minimum Client version installed, by creating a Device Posture check for a specific Client version. This can be added to a [Device Posture Profile](/v1/docs/creating-device-posture-profiles-and-device-checks) and then included in your Client Connectivity and security policies.
  - This feature will be gradually enabled over the next few weeks
- **Easily View Events for a Network Rule:** Now you can use the new **View Rule Events** action to show the events for a specific [Network Rule](/v1/docs/configuring-network-rules). When you select this action, the Events page opens and is immediately pre-filtered for all events that match that rule.

## Video Feature Overviews

- [XDR Detections Report](https://support.catonetworks.com/hc/en-us/articles/17243782639005-XDR-Detection-Report-Video)

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Ransomware 2023lock (New)
    - Ransomware GoodMorning (New)
    - Ransomware Ma1x0 (New)
    - Ransomware Phobos (New)
    - Ransomware SYSDF (New)
    - Ransomware Dxen Ransomware (Enhancement)
    - Ransomware Rocklee Ransomware (Enhancement)
    - Ransomware Stop/Djvu Ransomware (Enhancement)
    - Ransomware Vx-underground Ransomware (Enhancement)
    - Ransomware ZENEX Ransomware (Enhancement)
    - Malware DarkGate CNC Communiaction - Check-In (New)
    - Malware Fewin Stealer Data Exfiltration Attempt (New)
    - Malware GCleaner Downloader - IP Address Retrieval Attempt (New)
    - Malware Lumma Stealer CNC Communication - Exfiltration (New)
    - Malware Reverse Shell Connection - CNC Communication (New)
    - Malware TA402 CnC Communication - User-Agent (New)
    - Malware NodeStealer CNC Communication - Downloaded Archive GET (Enhancement)
    - CVE-2024-22024 (New)
    - CVE-2024-1709 (New)
    - CVE-2023-6623 (New)
    - CVE-2023-51467 (New)
    - CVE-2023-28128 (New)
    - CVE-2023-26255 (New)
    - CVE-2022-36534 (New)
    - CVE-2016-20017 (New)
    - CVE-2023-39677 (New)
    - CVE-2023-38203 (New)
    - CVE-2023-35082 (New)
    - CVE-2023-22527 (New)
    - CVE-2019-3967 (New)
    - CVE-2024-21893 (Enhancement)
    - CVE-2024-21887 (Enhancement)
    - CVE-2023-46805 (Enhancement)
    - CVE-2023-39143 (Enhancement)
    - CVE-2023-45484 (Enhancement)
    - CVE-2023-45480 (Enhancement)
    - Threat Actor r00ts3c-owned-you (New)
    - Lumma Stealer CNC Communication - Check-In (New)
- **Detection & Response**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Kali Linux Detection (New)
      - Suspicious Binary File Download using WinHTTP (New)
      - Suspicious Tool Download (New)
      - WebShell uploaded (New)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - AnyDesk remote desktop connection (New)
    - Process Hacker - download (New)
    - Lateral bash script transfer (New)
    - Phishing heuristic (Enhancement)
- **TLS Inspection**
  - Added global bypass for these applications, preventing possible [TLS inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) errors:
    - Brother Industries
    - Cisco Meraki Cloud
    - Oculus
    - Ring
    - Western Digital
    - Xerox
- **Apps Catalog:**
  - Added over 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced these applications:
    - Microsoft Copilot (formerly BingAI)
    - Google Gemini (formerly Bard)
    - King
    - WireGuard protocol
- **Application Control (CASB and DLP):**
  - This app is included in DLP scans:
    - Google Gemini - Search
- **Client Classification:**
  - Greenbone OS

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
