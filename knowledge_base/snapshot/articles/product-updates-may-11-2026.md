---
title: "Product Updates - May 11, 2026"
slug: "product-updates-may-11-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-may-11-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - May 11, 2026

## New Features & Enhancements

- **Anti-Tampering for the Windows Client:** [Anti-Tampering](/v1/docs/working-with-anti-tampering-for-the-cato-client) prevents users from stopping the Client service, and modifying or deleting different Client resources, such as the registry or files. This includes users with local admin privileges.
  - You can add exceptions for specific trusted processes or paths to let them interact with protected components without disabling Anti-Tampering, reducing operational friction while preserving security controls
  - Anti-Tampering is available from the Access > [Always-On policy](/v1/docs/protecting-users-with-always-on-security)
- **Improved Admin Experience for Static IP Allocation Policy at Scale:** Easily manage complex rulebases with more speed, flexibility, and control across the [Static IP Allocation policy](/v1/docs/ip-allocation-policy-for-remote-users). Enhancements include:
  - **Concurrent editing** – Multiple admins can [modify the policy](/v1/docs/working-with-policy-revisions) in parallel without conflicts
  - **Improved management of rules** - Disable individual rules and export the entire rule base to CSV
  - **Improved performance** – Policy page is more responsive, especially for a large number of rules
  - **GraphQL API support** – Use the API to manage the Static IP Allocation policy
- **Enhanced API Support for Managing Users:** Search, create, update, and delete users and revoke user sessions through the API instead of managing them manually in the Cato Management Application. This helps you automate session management and keep user access aligned with your operational workflows.
- **Browser Extension v1.8:** During the week of May 10, 2026, a new [Browser Extension version 1.8](/v1/docs/summary-of-browser-extension-releases) will be available in the Chrome Web Store. This version includes:
  - Improved user experience as the Browser reconnects
  - Stability improvements
  - Security updates
  - Bug fixes
- **New Experience Monitoring Metrics for Webex:** Experience Monitoring includes application-specific metrics for [Webex](/v1/docs/webex-configuring-the-experience-monitoring-ucaas-connector) sessions. The [new metrics](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users) provide insights into video, audio, and screen sharing during calls.
  - Requires a Cato Webex connector and a DEM license
- **Experience Anomaly Detection for Application Outages:** We added a new XOps Experience Monitoring Anomaly story for [potential application outages](/v1/docs/analyzing-experience-monitoring-anomalies). The story is generated based on spikes in HTTP error rates detected across the Cato global backbone, which can indicate a global application issue.
  - Requires DEM and XOps license
- **Updated DTLS Port for China Connectivity**: To improve connectivity and avoid misclassification of DTLS traffic, Cato now supports [using UDP port 1337](/v1/docs/using-an-alternate-udp-port-for-socket-and-client-dtls-traffic) as the default port for DTLS tunnels for Socket and Client traffic in China.
  - Account-level configuration
  - Supported from Socket v26 and Windows Client v6.4
- **Expanded Security Events via Google Drive & Workspace Connector:** The [Google Drive and Workspace](/v1/docs/google-drive-and-workspace-configuring-the-app-activities-integration) connector for App Activities supports collecting additional security event data from the Google Alert Center. This includes data such as suspicious logins, leaked passwords, and sensitive admin actions.
  - Additional permission required, see the [documentation](/v1/docs/google-drive-and-workspace-configuring-the-app-activities-integration) for more information

## PoP Announcements

- **New Delhi, IN:** We added a new Cato PoP location in New Delhi with the range 202.75.240.0/24.
- **Chicago, US:** A new range (199.27.51.0/24) is now available for the Chicago PoP location.
- The following new ranges will soon be available:
  - **Manchester, UK:** 159.117.243.0/24
  - **Mumbai, IN:** 113.30.136.0/24
  - **Munich, DE:** 85.255.18.0/24
  - **Santa Clara, US:** 199.27.52.0/24

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 11 new apps - A2A (Agent2Agent) Protocol, FeeLogic, Instantly, Kiro AI IDE, Microsoft Quick Assist, Naver Chat, Naver Dictionary, Naver Map, Naver Search, Naver Smartstore, Naver Webtoon
  - Enhanced Apps:
    - Freepik
      - Added domain **cdnpk.net**
    - SiriusXM
      - Modified name from **Automatic Labs Inc.** to **SiriusXM**
      - Added domain **siriusxm4biz.com**
    - Threads An Instagram App
      - Added domain **threads.com**
  - Category Changes:
    - Entertainment:
      - Added app: SiriusXM
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2025-66744 (New)
  - CVE-2025-71258 (New)
  - CVE-2025-71259 (New)
  - CVE-2026-0560 (New)
  - CVE-2026-2329 (New)
  - CVE-2026-2699 (New)
  - CVE-2026-27174 (New)
  - CVE-2026-33626 (New)
  - CVE-2026-33826 (New)
  - CVE-2026-3854 (New)
  - CVE-2026-41940 (New)
  - Exploitation - Bot Activity Following Suspicious Activity (Enhancement)
  - Exploitation - Outbound Low Reputation Access Following Suspicious Activity (Enhancement)
  - Exploitation - Service Scan Activity Following Suspicious Activity (Enhancement)
  - Exploitation - Tool Download Following Suspicious Activity (Enhancement)
  - Exploitation - Tool Transfer Following Suspicious Activity (Enhancement)
  - Heuristic - DNS Tunneling Abusing KEY Queries (New)
  - Heuristic - DNS Tunneling Abusing TXT Queries (New)
  - Heuristic - Suspected DNS re-binding (New)
  - Automated Execution Following Suspicious Activity (Enhancement)
  - Browser Impersonation Following Suspicious Activity (Enhancement)
  - Java Execution Following Suspicious Activity (Enhancement)
  - Python Execution Following Suspicious Activity (Enhancement)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - dns2tcp Activity (New)
  - Suspected DNS re-binding (New)
- **Dynamic Prevention**
  - Denied Source IP from accepting TeamViewer Inbound Remote Session Due to PsExec Anomaly Detection (New)
  - Denied Source IP from ADFind SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from AT Task Execution Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Batch Script SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Cloud Services Exfiltration Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Curl HTTP Request to Low Reputation Domain Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Curl HTTPS Request to Low Reputation Domain Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading AnyDesk Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading AnyDesk from 3rd Party Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Atera Agent Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Rclone Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Rclone from Official Site Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading ScreenConnect Access Agent Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading ScreenConnect Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading SimpleHelp Remote Work Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading SimpleHelp Unattended Access Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Splashtop Business Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Splashtop Business for Linux Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Splashtop from 3rd Party Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Splashtop Streamer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Splashtop Streamer for Linux Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Splashtop Streamer Prerequisite Handler via ManageEngine Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading TeamViewer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Zoho Assist Attended for Mac Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Zoho Assist Attended for Windows Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Zoho Assist Tech App for Linux Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Zoho Assist Tech App for Mac Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Zoho Assist Tech App for Windows Due to PsExec Anomaly Detection (New)
  - Denied Source IP from downloading Zoho Assist Unattended for Windows Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing AnyDesk Remote Desktop Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing AnyDesk WAN Remote Desktop Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing SimpleHelp Direct Lateral Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing SimpleHelp General Lateral Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing SimpleHelp Remote UDP Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing Splashtop Relay Client Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing Splashtop Relay Server Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing Splashtop Web Client Aggregated Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing Splashtop Web Client Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing Splashtop Web Client Fulong API Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing Splashtop Web Client HTTP API Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing Splashtop Web Client HTTP Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing TeamViewer Remote Session to Low Popularity IP Due to PsExec Anomaly Detection (New)
  - Denied Source IP from establishing TeamViewer WAN Lateral Remote Connection Due to PsExec Anomaly Detection (New)
  - Denied Source IP from FileZilla SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from FTP on Evasive Port Due to PsExec Anomaly Detection (New)
  - Denied Source IP from FTP to Low Reputation Domain Due to PsExec Anomaly Detection (New)
  - Denied Source IP from FTP to Low Reputation IP Due to PsExec Anomaly Detection (New)
  - Denied Source IP from LDAP Admin User Query Due to PsExec Anomaly Detection (New)
  - Denied Source IP from LDAP Computers Query Due to PsExec Anomaly Detection (New)
  - Denied Source IP from LDAP Groups Query Due to PsExec Anomaly Detection (New)
  - Denied Source IP from LDAP Persons Query Due to PsExec Anomaly Detection (New)
  - Denied Source IP from LDAP Trust Dump Query Due to PsExec Anomaly Detection (New)
  - Denied Source IP from LSARPC Builtin Admin Lookup Due to PsExec Anomaly Detection (New)
  - Denied Source IP from MEGA API Exfiltration Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Mimikatz SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from MobaXterm SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Netcat SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Nmap SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Pastebin Bot Access Due to PsExec Anomaly Detection (New)
  - Denied Source IP from PowerShell Script SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from PuTTY SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from RDP over TLS Due to PsExec Anomaly Detection (New)
  - Denied Source IP from RDP Tunneling Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Remote Scheduled Tasks Execution Due to PsExec Anomaly Detection (New)
  - Denied Source IP from SAMR Admin Lookup Due to PsExec Anomaly Detection (New)
  - Denied Source IP from SAMR Local Admin Enumeration Due to PsExec Anomaly Detection (New)
  - Denied Source IP from SAMR Query Display Info Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Service Creation via SVCCTL Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Service Deletion via SVCCTL Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Service Start via SVCCTL Due to PsExec Anomaly Detection (New)
  - Denied Source IP from TDSSKiller SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from transferring AnyDesk via SMB Due to PsExec Anomaly Detection (New)
  - Denied Source IP from transferring Splashtop Application via SMB Due to PsExec Anomaly Detection (New)
  - Denied Source IP from transferring Splashtop Streamer via SMB Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using CSExec Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using Impacket DCOMExec Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using Impacket PsExec Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using Impacket SMBExec Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using PAExec Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using PsExec Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using Rclone via HTTP Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using Rclone via SSH Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using RemCom Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using WinRM PowerShell Due to PsExec Anomaly Detection (New)
  - Denied Source IP from using WinRM WinRS Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Wget HTTP Request to Low Reputation Domain Due to PsExec Anomaly Detection (New)
  - Denied Source IP from Wget HTTPS Request to Low Reputation Domain Due to PsExec Anomaly Detection (New)
  - Denied Source IP from WinSCP SMB Transfer Due to PsExec Anomaly Detection (New)
  - Denied Source IP from WMI Execution Due to PsExec Anomaly Detection (New)
  - Detected Source IP Executing PsExec at Site with Anomalous Behavior, Limiting Lateral Movement, Discovery, Data Exfiltration, Command and Control (New)
  - OpenClaw Application Detected - Denying Tool Transfer (New)
  - OpenClaw Installation Detected - Denying Command and Control, Lateral Movement and Data Exfiltration (New)
  - OpenClaw Agent Detected - Denying Command and Control, Lateral Movement and Data Exfiltration (New)
  - Denied Source IP from Using NPM Due to OpenClaw Application Detection (New)
  - Denied Source IP from Installing OpenClaw through GitHub Repository Due to OpenClaw Application Detection (New)
  - Denied Source IP from Installing OpenClaw Due to OpenClaw Application Detection (New)
  - Denied Source IP from Outbound HTTP Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Accessing Internal Web Resources Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with Low Popularity IP Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with Low Popularity Domain Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with Low Reputation IP Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with Low Reputation Domain Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with Slack Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with MS Teams Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with Telegram Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with Cloud Storage Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with GitHub Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Downloading Skills Due to OpenClaw Installation Detection (New)
  - Denied Source IP from Communicating with MS Teams Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with Slack Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with Low Reputation Domain Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with Low Reputation IP Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with Low Popularity Domain Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with Low Popularity IP Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Accessing Internal Web Resources Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Outbound HTTP Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with Telegram Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with GitHub Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Communicating with Cloud Storage Due to OpenClaw Agent Detection (New)
  - Denied Source IP from Downloading Skills Due to OpenClaw Agent Detection (New)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Apps Security API Activity from Unusual Country (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - Google Apps
    - Anomalies (Enhancement) - Added vendor-native anomaly detection from the Google Alert Center API, covering security alerts such as phishing, suspicious logins, and admin setting changes
  - Salesforce
    - Third Party Apps (Enhancement) - Improved app permission accuracy by using per-user permissions and including a base-level app entry alongside user-specific entries
  - CrowdStrike
    - Device (Enhancement)
    - EDR (Enhancement)
  - Microsoft Exchange
    - Activity (Enhancement)
