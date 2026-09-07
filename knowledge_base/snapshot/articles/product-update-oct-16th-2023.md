---
title: "Product Update - Oct. 16th, 2023"
slug: "product-update-oct-16th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-oct-16th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Oct. 16th, 2023

## New Features & Enhancements

- **Network Rules Also Support Global IP Range Objects:** We are enhancing the Network Rules to support the [**Global IP Range**](/v1/docs/using-ip-ranges-in-policies) object.
  - When you select the **IP Range** for a setting in the rule, you can choose a **Global IP Range** or a **Custom IP Range**
  - **Global IP Range** entities can be a range of IPs, a single IP, or a CIDR network
  - The existing **IP Range** entity in Network Rules is now called **Custom IP Range** with no change to functionality
- **Enhancement for DLP Predefined Data Types - Visibility for Minimum Match Threshold:** You can view the threshold of matches for [predefined Data Types](/v1/docs/creating-dlp-content-profiles) in a DLP Content Profile. For example, a Data Control rule has a profile set to a threshold of 3, the rule only triggers when a specific Data Type is matched 3 times for the file scan. This lets you align data control policies with increased precision to help ensure effective data protection.
- **SaaS Security API Events Now Include the Full Path URL for the File:** We enhanced the [events](/v1/docs/analyzing-events-in-your-network) for SaaS Security API with the full file URL to make it easier to locate and investigate events.
  - The file URL is shown in the field **Full Path URL** for events with the Type **Security** and the Sub-Type **SaaS Security API Data Protection**
    - For API and Cloud Storage feeds, the field name is **full_path_url**
    - For more about event consumption, see these articles: [EventsFeed API](https://api.catonetworks.com/documentation/#query-eventsFeed), [Events fields](https://api.catonetworks.com/documentation/#definition-EventFieldName), [Events Integration](https://support.catonetworks.com/hc/en-us/articles/9726441847965-Integrating-Cato-Events-with-AWS-S3-)
- **Default Rules Now Visible in Security Policies:** Over the next few weeks, we are exposing our existing default security rules to admins to help them better understand rulebase behavior and improve policy decision making. The default rules are visible in the [Anti-Malware](/v1/docs/what-is-the-cato-anti-malware-policy), [WAN Firewall](/v1/docs/what-is-the-cato-wan-firewall), and [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) policies. For example, the existing default Any-Any Inspect rule for TLS Inspection will be shown at the bottom of the rulebase.
  - The default rules can’t be edited
  - There are no changes to current policy behavior
- **Enhanced Filters for Sites Page:** We added new filters to the [Sites page](/v1/docs/working-with-sites), so you can quickly filter by Site Connectivity Status, Connection Types, or Socket Versions. In addition, you can click the widgets at the top of the page to apply the same filters.
- **New Help Menu in the Cato Management Application:** Over the next few weeks, we are adding a new **Help** button in the Cato Management Application that opens a panel and shows the related Knowledge Base articles and videos for each page.
  - We moved the **Contact Support** and **Send Feedback** buttons to this new panel

## PoP Announcements

- Added 216.205.112.0/20 as an [IP Range Owned by Cato Networks](/v1/docs/production-pop-guide)

## Security Updates

- **IPS Signatures:** View more details about the IPS Signatures and Protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - Ransomware Cloak (New)
  - Ransomware Pwpdvl (New)
  - Malware DarkGate (Enhancement)
  - Remote Code Execution over HTTP
  - CVE-2023-38035
  - CVE-2023-37582
  - CVE-2023-32235
  - CVE-2023-26258
  - CVE-2023-22515
  - CVE-2023-21839
  - CVE-2022-31199
  - CVE-2012-2336
  - CVE-2012-2311
- **Suspicious Activity Monitoring:** These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Exfiltration Over FTP to Low Reputation Server
  - FTP Client (ClientSFTP) over SSH
  - FTP Client (CyberDuck) over SSH
  - FTP Client (edtFTPjPro) over SSH
  - FTP Client (FileZilla) over SSH
  - FTP Client (FTP Voyager) over SSH
  - FTP Client (Rclone) over SSH
  - FTP Client (Rloader) over SSH
  - FTP Client (ServiceNow Shazzam) over SSH
  - FTP Client (sftp_null) over SSH
  - FTP Client (WinSCP) over SSH
  - FTP Client (WS_FTP) over SSH
  - Phishing Heuristic
- **Detection and Response:** Threat Hunting IOA signatures:
  - Transferring a Suspicious Script (New)
  - Traffic to an IP address as host name with a redirection (New)
  - Suspicious INK File Download (New)
  - Suspicious Execution - High Risk (New)
  - Suspected Exfiltration to Cloud Storage Applications (New)
  - SDP File Sharing Application Upstream Bandwidth Anomaly (New)
  - Remote PsExec Service Execution (New)
  - PSTools Download Detection (New)
  - HTA File Found in MS Office (New)
  - Downloading a Suspicious Script (New)
  - Device Attributes Exfiltration (New)
- **Apps Catalog:** Added dozens of new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including these highlights:
  - Thomsonreuters (Enhancement)
  - Skype and MS Teams (Enhancement)
  - PureVPN (Enhancement)
  - Kakaotalk Upload (Enhancement)
  - Disney Plus (Enhancement)
  - Microsoft Azure Devtunnels (New)
- **Application Control (CASB):**
  - Granular App: MS Teams - Upload File (Enhancement)
  - Granular App: Dropbox - Upload (Enhancement)
- **OS Detection:**
  - OS Detection (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
