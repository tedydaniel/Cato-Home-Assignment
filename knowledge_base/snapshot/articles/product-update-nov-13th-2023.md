---
title: "Product Update - Nov. 13th, 2023"
slug: "product-update-nov-13th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-nov-13th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Nov. 13th, 2023

## New Features & Enhancements

- **New XDR Security Report**: The new [XDR Report](/v1/docs/generating-an-xops-investigations-report) summarizes XDR story investigations and provides an overview of the account security posture.
  - The report includes data such as:
    - Number of stories investigated with breakdown by verdict
    - Summary of malicious and suspicious stories with breakdown by site, severity, and country
    - Available for XDR Core, XDR Pro, and MDR customers
- **New Third-Party Integrations with Cato Events:** Leverage native integration with these platforms:
  - [Axonius](https://docs.axonius.com/docs/cato) integration: Cato customers that also use Axonius cybersecurity and asset management
  - [Zenoss ZenPack](https://zenpacks.zenoss.io/zenoss/PS.CatoNetworks/) integration: Cato customers that also use the Zenoss ZenPack extension module
  - [Read more](/v1/docs/cato-data-third-party-supported-integrations) about other third-party vendors that support native integration with Cato events
- **Reminder - Upcoming Deprecation of the Account Snapshot ‘metrics’ Field:** Cato previously [announced that on Nov. 15, 2023](/v1/docs/deprecating-metrics-field-in-accountsnapshot-api-on-jan-15-2024), we will deprecate the **metrics** field in the [accountSnapshot](https://api.catonetworks.com/documentation/#query-accountSnapshot) API.
  - After this date, the [metrics](https://api.catonetworks.com/documentation/#definition-Metrics) field in the accountSnapshot API will no longer be available
  - All traffic metrics and data are available using the [accountMetrics](https://api.catonetworks.com/documentation/#query-accountMetrics) API.

## PoP Announcements

- **Los Angeles, United States**: A new range (216.205.115.0/24) is now available in the Los Angeles PoP location

## Security Updates

- **IPS Signatures:** View more details about the IPS Signatures and Protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - SSH Client OpenVAS Scanner
  - SSH Client Vulnerability Scanner Client SSH Version 9.9
  - SSH Vulnerability Scanner Client Nessus
  - SSH Vulnerability Scanner Client Nmap
  - SSH Vulnerability Scanner Client Qualys
  - SSH Vulnerability Scanner Client Rapid7
  - SSH Vulnerability Scanner Client Sentinel1
  - SSH Vulnerability Scanner Client TenableRocks
  - CVE-2023-46747
  - CVE-2023-42793
  - CVE-2023-32315
  - CVE-2023-29800
  - CVE-2023-22518
- **Apps Catalog:** See the new SaaS applications in the [Apps Catalog](/v1/docs/using-the-app-catalog).
- **Application Control (CASB):**
  - New granular actions for the following apps:
    - Workplace: Comment, Post, Call, Upload File, Login
    - Instagram: Send Message
- **Detection and Response:** These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
  - Threat Hunting IOA signatures:
    - Blocked IP/Domain
    - Common Scanner (WAN bound)
    - Common Scanners (Outbound)
    - Downloading a Suspicious Script
    - Known Cobalt Strike Profile
    - Known Scanner (WAN bound)
    - Malware Activity
    - Potential Downloader
    - Potential Unwanted Program (PUP) Activity
    - PSExec Execution
    - Sinkholed Domain
    - Sinkholed IP
    - Suspicious Network Activity (Domains)
  - Threat Prevention IOA signatures:
    - Downloading From Exploit-DB
    - Suspicious Network Activity
    - Suspicious Network Activity (User-Agent)
    - Suspicious Tool Download
- **File Identification:**
  - Enhanced file identification in Cato Cloud services for the following file types:
    - CMD (Windows Command File)
    - DOC (Microsoft Office Document)
    - MSI (Microsoft Windows Installer Package)
    - PPT (Microsoft Office Powerpoint)
    - XLS (Microsoft Office Excel)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
