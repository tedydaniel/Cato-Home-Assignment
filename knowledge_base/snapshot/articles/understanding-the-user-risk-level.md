---
title: "Understanding the User Risk Level"
slug: "understanding-the-user-risk-level"
updated: 2026-08-30T09:17:48Z
published: 2026-08-30T09:17:48Z
canonical: "knowledge.catonetworks.com/understanding-the-user-risk-level"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the User Risk Level

This article provides information about the Cato User Risk Level, how it is calculated, and how you can implement it to improve your security posture.

## Overview

As part of Cato’s approach to universal ZTNA and continuous assessment and verification, Cato calculates a dynamic User Risk Level for each of the users in your organization to determine the risk that they pose.

The User Risk Level helps you improve your security posture and adaptive access capabilities. You can create rules in your various policies to determine access to resources based on this level. For example, create a rule that blocks traffic to sensitive company resources from users with a Risk Level of **High** or above.

You can view the Risk Level for all users in your organization, whether they have an SDP license or not. This gives you an indication of the overall security posture. In addition, you can see all security events that are connected to a specific user and determine their risk level.

**Note:** To view the user risk level, you must have the necessary permissions in the [Access Admin](/v1/docs/managing-admin-roles-using-rbac) role.

To use a 3rd-party vendor user risk level, for example, Entra ID, see [Configure User Risk Score with Entra ID](/v1/docs/configure-user-risk-score-with-entra-id).

### Use Case - SaaS

ABC Company works with SaaS applications and, following security best practices wants to make sure that only the necessary people can access these applications. In addition, they want to make sure that nobody in the authorized group with a risk level of High or greater can access these applications.

The company creates a rule in their Internet firewall to block any traffic to their SaaS applications.

When John Doe is unable to access the Saas application, he contacts the IT department who see that his risk level is High. However, after reviewing the events that determined the level, the IT department decide he doesn't pose a risk, and reset the level so he is able to access the applications he needs.

### Use Case - Private Apps

ABC Company has a database server that needs to be accessed from its various offices. They want to ensure that it is accessible to the developers but also need to ensure that it is secure, as it provides access to sensitive and proprietary data.

The company creates a rule in the WAN firewall to only allow access to authorized users whose Risk Level is lower than High.

## How Cato Calculates the Risk Level

Every user activity is monitored and logged, leveraging the Cato shared context, and users are dynamically assigned a Risk Level based on a proprietary algorithm that considers a range of different data points. The Risk Level can then be used in the Internet and WAN policies to only allow access to users who present the lowest risks.

### User Attributes Incorporated into the Risk Score

Cato collects the following attributes.

User attributes marked policy can be used in policies. For more information, see the [Client Connectivity Policy](/v1/docs/what-is-the-client-connectivity-policy).

| Item | Attribute | Examples |
| --- | --- | --- |
| 1 | Trojan Activity | Dridex, Peacomm, PeacommBanking |
| 2 | Banking Malware | Bancos, Banload, Banker |
| 3 | Information Stealers | Zeus/Zbot, Agent, Symmi |
| 4 | Backdoor Activity | Various signatures mapped to MITRE ATT&CK techniques |
| 5 | Botnet Traffic | Mirai, various C2 signatures |
| 6 | DNS Tunneling | Multiple DNS tunneling detections |
| 7 | Beaconing Activity | Regular Command & Control check-ins |
| 8 | Multiple Domain Communications | Multiple Threatening Domains then Low Reputation Server |
| 9 | Ransomware Communications | SMB activity and external communications |
| 10 | Encryption Behavior | File system encryption activity |
| 11 | Ransom Note Delivery | Ransom note placement or delivery |
| 12 | Mining Pool Communications | CryptInject, Cryptomineext, Groupfabric Bitcoinminer |
| 13 | Resource Utilization | Abnormal system usage for mining |
| 14 | Data Transfer to Suspicious Destinations | System Information Exfiltration, RaiDrive Exfiltration |
| 15 | Credential Theft | Credential theft activity and exfiltration |
| 16 | Large Data Transfers | Abnormally large outbound transfers |
| 17 | CVE Exploitation | CVE-2018-0101, CVE-2017-0199, CVE-2021-44228 (Log4Shell) |
| 18 | Zero-day Exploitation | Signatures for emerging threats |
| 19 | Command Injection | Detected command injection attempts |
| 20 | Directory Traversal | Path traversal behavior |
| 21 | File Upload Attempts | Suspicious file uploads to web apps |
| 22 | SQL Injection | SQLi attack attempts |
| 23 | Cross-site Scripting and CSRF | XSS and CSRF detections |
| 24 | Obfuscated Phishing | Detection of hidden phishing tactics |
| 25 | Credential Phishing | Insertion of sensitive data into phishing pages |
| 26 | Brand Impersonation | DHL-related phishing |
| 27 | Automated Scanning Tools | Nikto, Nessus, OpenVAS |
| 28 | Targeted Vulnerability Probes | CVE-focused scans |
| 29 | Network Enumeration | Port scanning and network discovery |
| 30 | Known Bad IP/Domain Communication | Low-reputation domain access, TOR/proxy |
| 31 | User Email | (policy - see below) |
| 32 | User Group | (policy - see below) |
| 33 | User Confidence level | (policy - see below) |
| 34 | Platform | (policy - see below) |
| 35 | Country | (policy - see below) |
| 36 | Connection origin | (policy - see below) |
| 37 | Remote Execution via SMB | PsExec, PAExec, RemCom, CSExec |
| 38 | WinRM Remote Execution | WinRS command shell, WinRM PowerShell |
| 39 | Impacket Remote Execution | Impacket PsExec, Impacket SMBExec, Impacket DCOMExec |
| 40 | WMI Remote Execution | WMI execution over DCOM |
| 41 | Remote Service Manipulation | SVCCTL Service Create, SVCCTL Service Start, SVCCTL Service Delete |
| 42 | Remote Scheduled Tasks | schtasks remote, AT task execution via atsvc |
| 43 | LDAP Reconnaissance | LDAP trust dump, persons, computers, admin users, groups queries |
| 44 | SAMR / LSARPC Reconnaissance | SAMR admin lookup, SAMR query display info, SAMR local admin enum, LSARPC builtin admin |
| 45 | Multi-Service Port Scanning | Scanning FTP, SSH, RDP services from single source IP |
| 46 | Credential Tool Transfer | Mimikatz SMB transfer |
| 47 | Offensive Tool Transfer via SMB | Netcat, Nmap, ADFind, TDSSKiller, PowerShell scripts, Batch scripts |
| 48 | File Transfer Tool Transfer via SMB | WinSCP, FileZilla, PuTTY, MobaXterm |
| 49 | Rclone Exfiltration | Rclone SSH, Rclone HTTP, Rclone download |
| 50 | Cloud Storage Exfiltration | MEGA API non-browser upload, low-popularity cloud services upload |
| 51 | Pastebin Bot Access | Non-browser raw content access to Pastebin |
| 52 | FTP to Suspicious Destinations | FTP to low reputation IP, low reputation domain, non-standard port |
| 53 | Protocol Tunneling | RDP tunneling over web ports, RDP over TLS on non-standard ports |
| 54 | RMM Tool Download | TeamViewer, AnyDesk, ScreenConnect, Splashtop, SimpleHelp, Atera, Zoho Assist |
| 55 | RMM Active Connection | TeamViewer WAN/inbound session, AnyDesk remote desktop, Splashtop relay, SimpleHelp lateral/UDP |
| 56 | RMM Tool Transfer via SMB | AnyDesk SMB transfer, Splashtop SMB transfer |
| 57 | Suspicious CLI Tool Usage | curl / wget to low-reputation sites, curl / wget binary download |
| 58 | PSTools Suite Download | PSTools download followed by mass PsExec (15+ hosts in 10 min) |

### Indicators Cato Uses for the Risk Score

Cato looks at many different indicators to determine risky behavior and classifies them into the 4 categories above. These indicators include:

- Indicators of systems that have already been compromised - more than 2500 signatures, including:
  - Malware, such as Trojans, financial-based malware, and various backdoor techniques
  - Command & Control communications, such as botnet traffic, DNS tunneling, and multiple domain communications
  - Ransomware activity, such as encryption behavior, ransomware note delivery, and ransomware communications
  - Crypto mining, such as mining pool communications and resource utilization
  - Exfiltration activities, such as data transfer to suspicious destinations, credential theft, and large data transfers
- Indicators of blocked attempts that could lead to infection - more than 2300 signatures, including:
  - Remote Code Execution (RCE) attempts, such as CVE exploitation, 0-day exploitation attempts, and command injection
  - Web application attacks, such as directory traversal, file upload attempts, and XSS/CSRF
  - Phishing activities, such as credential phishing and brand impersonation
  - Vulnerability scanning, such as the use of automated scanning tools and network enumeration
- Policy violations and risky activities that could potentially lead to compromise - more than 1500 signatures, including:
  - Lateral movement attempts, such as psexec usage, WinRM usage, and PowerShell remoting
  - Information disclosure, such as sensitive data exposure, error message leaks, and directory listings
  - Reputation-based indicators, such as TOR or proxy usage, suspicious domain access, and communication with known bad IP addresses
  - Block events triggered by Agentic Threat Prevention. For more information, see [What is Agentic Prevention?](/v1/docs/what-is-dynamic-prevention)

## Define User Risk Level Policies

User Risk Level is a vital tool for network and security teams, enabling zero-trust dynamic access control policies to protect both internal application traffic and internet traffic. It offers valuable insights into your risk posture, letting you adjust your security strategies dynamically in response to evolving threats.

You can create risk-based policies in your Internet and WAN firewalls to block access to your applications.

![User-Level-Attribute.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35729934493213.png)

**To define a risk-based rule in your firewalls:**

1. When configuring your [Internet](/v1/docs/managing-the-internet-firewall-policy) or [WAN](/v1/docs/managing-the-wan-firewall-policy) firewall policies, add the User or User Groups to which the rule applies.
2. In the **Device** section of the rule, under **User Attributes**, click **Add Attribute**.
3. Enter the Risk Level criteria to match the rule against.
4. Define the **Action** to take when the rule is matched and click **Save**.

## Viewing Risk Levels for All Users

The **Access > Users** page provides visibility into all of the users in your system, and their risk levels.

![Users-Directory.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35729898504221.png)

You can filter the information on the page based on the Risk Level so you can easily find the ones that potentially pose the greatest threat to the organization. Risk Level values are:

- Critical
- High
- Medium
- Low

From this page, you can perform specific actions based on the Risk Level, such as revoke a user session or resetting the Risk Level.

![User-Score-Reset.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35729923308317.png)

### Investigating and Monitoring a Specific User

To gain a better understanding of what determines the Risk Level for a user, you can click on an individual user and navigate to the **User Risk** page, which then presents their Risk Score dashboard. Use the User Risk Score Dashboard to investigate the risk posture of a specific user and take immediate remediation actions. The dashboard helps you understand how a user’s risk changes over time, what contributes to that risk, and which security events are related, so you can move quickly from investigation to remediation. You access the dashboard from the Users Directory.

To view the information for a specific user, you must have the necessary permissions set as part of the [Access Admin](/v1/docs/managing-admin-roles-using-rbac) role:

- None - you can't access the risk score dashboard for a specific user
- View - you can view the risk score dashboard, but can't perform any actions
- Edit - you have full permissions to view the risk score dashboard and perform actions such as revoke a session or reset the risk score

![risk-score-dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35729923405213.png)

Use the dashboard views to investigate why the user’s risk score changed and what is contributing to it. Review Risk over time to identify score spikes and trends, Risk contributors to see the factors driving the current score, Related security events to view security events associated with the user, and Score Contribution Events to see the specific events that contributed to score changes, for each of the following:

- IPS
- Anti-malware
- Suspicious activity
- Firewall
- Agentic Threat Prevention

![risk-score-dashboard-events.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35729905131293.png)

You can click on any of the links in a given section, for example, **View all IPS events** to navigate to the Events page, which is then filtered by the user and event type.
