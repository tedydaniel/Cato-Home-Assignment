---
title: "Product Update - February 7th, 2022"
slug: "product-update-february-7th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-february-7th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 7th, 2022

## Introducing Cato’s CASB Solution

- **Secure Cloud Apps and Discover Shadow IT in your Network:** [Cato’s Cloud Access Security Broker (CASB) Solution](https://www.catonetworks.com/news/cato-networks-delivers-instant-visibility-and-control-of-cloud-application-data-risk/) provides seamless visibility and assessment for cloud app usage in your organization. Cato’s CASB solution lets you straight-away discover cloud apps (Shadow IT), assess app risk and compliance, monitor user activities and govern app use, and identify and mitigate cloud-based threats.

CASB is a separate license that includes: Application Control Policy, Cloud Apps Dashboard, and defining sanctioned vs. unsanctioned apps.
  - **Granular Application Policy:** You can create different types of Application Control rules, including:
    - Enforcing traffic for specific security and compliance characteristics
    - Fine-grained access that restrict activities within an app
  - **New Dashboard that Provides Excellent Visibility for Apps and Shadow IT:** The Cloud Apps Dashboard has dedicated views and insights for cloud app usage within the organization.
    - Easily identify risky apps and cloud-based vulnerabilities for WAN and Internet traffic
    - Identify and monitor app usage according to specific users

## New Features & Enhancements

- **IPS Protection to Automatically Block Pentest Tools:** Starting on February 6th 2022, Cato's IPS will block vulnerability scanners for all Protection Scopes (WAN, inbound, and outbound) because they represent a potential security risk to your network. You can use the [IPS Policy Allow List](/v1/docs/allowlisting-ips-signatures) to allow a specific tool for Protection Scopes with these signatures:
  - cid_scan_attack_tools_inbound
  - cid_scan_attack_tools_wanbound
  - cid_scan_attack_tools_outbound
- **User Awareness Now Compatible with Microsoft DCOM Patch:** Microsoft announced that they are hardening their infrastructure and patching a DCOM vulnerability described [here](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26414). We are updating the Cato service User Awareness so that it is compatible with Microsoft’s changes.
- **Improved Sync with Disabled Users for SCIM Provisioning:** Starting on February 6th, when you disable users in your Identity Provider (IdP), they are synced to your Cato account as disabled. When you then enable the users in the IdP, they will also be enabled in your Cato account.
  - Users that were disabled in your IdP prior to February 6th, make a change to the user in the IdP so that the SCIM service updates the user.
- **Improved Descriptions for Some Apps and Services:**
  - This is a cosmetic change, and there is no impact on behavior or functionality
  - Changed **Office365 Login** app name to:
    - Microsoft Login
  - Changed **Radius** services names to:
    - RADIUS Protocol - Accounting Phase
    - RADIUS Protocol - Authentication Phase
    - RADIUS Protocol - Over TLS
    - RADIUS Protocol - Over DTLS
  - Changed **Socks Proxy** service names to:
    - Socks4 Proxy
    - Socks5 Proxy

## Cato SDP Client Releases

- **Windows Client v5.2:** We are starting the gradual release of the Windows Client version 5.2. This version includes:
  - Enhancements for Client SSO authentication and support for Internet Explorer as the OS browser
  - Device Posture (EA) enhancement, periodic checks that devices are compliant with the Device Posture policy
  - Cato authentication server supports CA issued certificates (non-self-signed)

## Security Updates

- **IPS Signatures:**
  - CVE-2021-20022
  - CVE-2021-22056
  - CVE-2021-26085
  - CVE-2021-26086
  - CVE-2021-39226
  - CVE-2021-43283
  - CVE-2020-29607
  - CVE-2020-35576
  - CVE-2020-5804
  - CVE-2019-9670
  - CVE-2012-0391
  - Malware - Cobalt Strike Malware (Enhancement)
  - Metasploit Meterpreter (Enhancement)
  - Vulnerability Scanning Tools (New)
- **Application Database:**
  - Logitech (New)
  - Windstream Video Conferencing (New)
  - Thomsonreuters (Enhancement)

## Knowledge Base Updates

- [(New) What is the Cato CASB Solution](/v1/docs/what-is-the-unified-casb-solution)

## Support Tickets Resolved

- #133616, #134551, #134680, #134688, #134806, #134572, #135881, #136275, #136427, #136450, #137151, #137611, #137941, #138433, #139247, #139825
