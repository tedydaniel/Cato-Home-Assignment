---
title: "Product Update - March 20th, 2023"
slug: "product-update-march-20th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-march-20th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - March 20th, 2023

## New Features & Enhancements

- **Easy to Manage Granular Always-On Policy:** Over the next few weeks, you can implement the security of [Always-On](/v1/docs/protecting-users-with-always-on-security) with an ordered rulebase, and a granular approach that includes user groups and SDP users. Until now, it was only possible to manage Always-On for individual users.
  - Includes **Platform** specific settings, for example to only require Always-On for Windows devices, but not for mobile devices
  - SDP users that don’t match any rules are allowed to disconnect from the network (no Always-On)
  - The current Always-On settings are migrated to the new policy with no impact for your account. For more information, see this [article](https://support.catonetworks.com/hc/en-us/articles/9927211182493)
- **Cato Management Application Enhancements:**
  - **For MDR Service Customers Only:**
    - **Navigation Menu Enhancement:** The [Detection & Response](/v1/docs/reviewing-detection-response-stories-for-mdr-customers) screen is now located in the **Monitoring** menu (previously it was located under **Managed Services**)

## Security Updates

- **IPS Signatures:**
  - BlackByte Ransomware
  - Cl0p ELF Ransomware
  - Docker Daemon API Remote Code Execution
  - Generic protection for Server Side Request Forgery
  - Hive Ransomware
  - Mallox Ransomware
  - Medusa Ransomware
  - MedusaLocker Ransomware
  - Play Ransomware
  - RagnarLocker Ransomware
  - Royal Ransomware
  - DarkSide Ransomware
  - Stop Ransomware
  - Qakbot Malware (Enhancement)
  - Suspicious SMB traffic associated with Ransomware (Enhancement)
  - CVE-2023-23415
  - CVE-2019-18394
  - CVE-2020-4786
  - CVE-2022-25026
  - CVE-2022-41343
  - CVE-2022-41828
  - CVE-2022-44267
  - CVE-2022-44268
  - CVE-2023-24880
  - CVE-2022-31706 (Enhancement)
  - CVE-2023-0669 (Enhancement)
- **Application Database:**
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog))
  - Microsoft Office Login (Enhancement)
- **Application Control Policy (CASB):**
  - Enhanced granular actions for these apps:
    - Microsoft Login: Login

## Knowledge Base Updates

- [Cato Cloud to FortiGate via HA IPSec Tunnels (CLI Guide)](/v1/docs/cato-cloud-to-fortigate-via-ha-ipsec-tunnels)
