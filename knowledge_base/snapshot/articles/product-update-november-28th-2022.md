---
title: "Product Update - November 28th, 2022"
slug: "product-update-november-28th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-november-28th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - November 28th, 2022

## New Features & Enhancements

- **Improved DNS Protections for the IPS Service:** On December 4th, we are planning to release an IPS engine enhancement to protect against a wider scope of DNS related threats, such as phishing, DGA, command and control, and other categories with potentially malicious content. The new **DNS Protection** screen (Security > DNS Protection) lets admins control which protections are activated on DNS traffic.
  - DNS Protections are included in the IPS license
- **SAM Enhances IPS to Improve Visibility of an Attack:** Starting on Dec. 4th, you can set the IPS service to monitor suspicious traffic with the new Suspicious Activity Monitoring (SAM) feature. SAM provides visibility for suspicious activities on your network, such as network-wide port scans, or attempted access using non-standard ports. When an attack is traced back to suspicious traffic, you can adjust security policies to defend against similar attack vectors in the future.
- **Support for Sanctioned Apps:** The **Application Control** policy (Security > Application Control) supports adding Sanctioned Apps as the **Application** for a rule.
  - You can add Sanctioned Apps to App Control and Data Control rules
- **Use SDP Device Posture for App Control Rules:** Enhanced security for the **Application Control** policy (Security > Application Control), you can now add **Device Posture Profiles** to the rules and provide access based on the actual device of the SDP user.
  - You can add **Device Posture Profiles** to App Control and Data Control rules
- **Better Visibility for IPS Threat Groups**: Starting on Dec. 4th, we are adding a **Categories** section to the **IPS** screen (Security > IPS) that describes all the IPS threat categories and lets you drill-down to the relevant events for each category.
- **Export Security Rules to CSV:** Starting on Dec. 4th, you can easily export rules from the Security policies to a readable spreadsheet format (CSV file). The Security policies include:
  - Internet and WAN firewall
  - TLS Inspection
  - Application Control and Data Control
- **Cato Reseller Accounts Improved Visibility for Socket Inventory:** Reseller accounts can see Socket data and information for all the managed accounts in the **Socket Inventory** screen. This screen provides visibility for all of the Sockets in the managed accounts, including Sockets that Cato has already shipped.
- **Change to Cato License Dates Time Zone:** The start and expiration dates for Cato licenses now use the UTC time format (the start date is always UTC 00:00).
  - Note - For accounts with a license start date set to GMT(+XX:XX), the start and expiration date in UTC will show as one day earlier. For example, a start date of Jan. 10 GMT (+2:00) will show as Jan. 9 UTC.

## Security Updates

- **IPS Signatures:**
  - Malware - Brute Ratel
  - Malware - Raccoon Stealer v2.0 - RecordBreaker
  - Null Byte Injection Enhancement
  - CVE-2022-41091
  - CVE-2022-41049
  - CVE-2022-37299
  - CVE-2022-3180
  - CVE-2022-31268
  - CVE-2022-29303
  - CVE-2022-29081
  - CVE-2022-28958
  - CVE-2022-2633
  - CVE-2018-7445
- **Application Database:**
  - Added more than 200 new SaaS applications (you can view the SaaS apps in Monitoring > Apps Catalog)
  - Enhanced 50 SaaS applications, including:
    - Citrix
    - Mega
    - Office 365 Login
- **Updates to Application Control Policy:**
  - Enhanced actions for these apps:
    - Gmail: Send Mail
    - Dropbox: Download
- **Updated Data Loss Prevention:**
  - New Data actions were added for this app:
    - Trello: Download, Create Attachment
- **Improvements to OS Detection for TLS Inspection:** We improved the accuracy for the TLS Inspection engine to detect the OS for hosts in your network. This means that it’s possible to identify previously unknown hosts as an OS that supports TLS inspection. Traffic for these hosts will then be inspected or bypassed according to TLS inspection policy. [Read more](/v1/docs/configuring-tls-inspection-policy-for-the-account). The following operating systems are included in this improvement:
  - Windows (inspected by default)
  - Android (bypassed by default)
  - Unix (bypassed by default)
  - Unknown (bypassed by default)

## Knowledge Base Updates

- [Cato Cloud to Cisco IOS/IOS-XE via HA IPSec Tunnels](/v1/docs/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels)
- [Cato Cloud to VMware Edge via HA IPsec Tunnels](/v1/docs/cato-cloud-to-vmware-edge-via-ha-ipsec-tunnels)
