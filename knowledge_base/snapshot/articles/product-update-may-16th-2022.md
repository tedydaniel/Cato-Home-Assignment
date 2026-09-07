---
title: "Product Update - May 16th, 2022"
slug: "product-update-may-16th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-may-16th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 16th, 2022

## New Features & Enhancements

- **SDP Users Can Enjoy SSO Simplicity and with Security of Never-Off/Always-On:** Cato Clients now support the ability to authenticate with Single Sign-On (SSO) and at same time the Client Access Connectivity policy is set to Never-Off for Windows and Always-On for macOS. [Read more](/v1/docs/protecting-users-with-always-on-security).
  - Minimum supported Client versions are Windows Client v5.3, and macOS Client v5.0
  - You can configure SSO and Never-Off/Always-On for the entire account or for specific SDP users
- **New Anti-Malware Allowlist:** We are enhancing the Anti-Malware policy with a new Allowlist screen that lets you easily define rules to bypass Anti-Malware scans (**Security > Anti-Malware > Allowlist**). For example, you can allowlist traffic for sensitive devices that can experience issues with these scans. [Read more](/v1/docs/managing-anti-malware-exceptions).
  - The Allowlist rules are applied to the Anti-Malware engines before the Protection Policy rules
  - For accounts that aren’t experiencing issues with Anti-Malware scans, it’s not necessary to create new allowlist rules
- **Enhancement for LDAP Directory Services:** You can select the **AD Provider** for LDAP services in the Cato Managment Application (**Access > Directory Services > Edit Directory Service**). [Read more](/v1/docs/using-an-identity-provider-for-your-cato-account).

## Security Updates

- **IPS Signatures:**
  - Malware - Rclone (New)
  - Malware - Lockbit (Enhancement)
  - CVE-2022-29464
  - CVE-2022-26925
  - CVE-2022-1388
  - CVE-2021-30116
  - CVE-2020-8816
  - CVE-2020-4006
  - CVE-2020-2555
  - CVE-2019-3929
  - CVE-2018-7602
  - CVE-2018-0798
  - CVE-2018-0171
  - CVE-2017-11512
  - CVE-2010-5330
  - CVE-2007-3010
- **Application Database:**
  - DNS over HTTPS - DoH (Enhancement)
- **Application Control Policy:**
  - Gmail - Add attachment (Enhancement)
  - OneDrive Business & SharePoint – Download (Enhancement)
  - OneDrive Personal – Download (Enhancement)
  - Skype and MS Teams - Upload (Enhancement)

## Knowledge Base Updates

- [Allowlisting Anti-Malware Traffic](/v1/docs/managing-anti-malware-exceptions)
