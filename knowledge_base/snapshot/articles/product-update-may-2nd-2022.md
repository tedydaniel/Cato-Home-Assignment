---
title: "Product Update - May 2nd, 2022"
slug: "product-update-may-2nd-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-may-2nd-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 2nd, 2022

## New Features & Enhancements

- **Improvements to TLS Inspection Implicit Bypass:** For some applications that implicitly bypassed TLS Inspection (such as Dropbox) are now inspected when accessed from an Internet browser. [Read more](/v1/docs/configuring-tls-inspection-policy-for-the-account).
- **Security Enhancement to Application Control Policy (CASB) to Block QUIC and GQUIC:** When you initially enable the policy, a rule is automatically added to the top of Internet firewall rulebase that blocks QUIC and GQUIC traffic. This follows Cato’s security best practices.
  - If necessary, you can edit this rule based on the requirements of your account

## Security Updates

- **IPS Signatures:**
  - Malware - Clop (Enhancement)
  - CVE-2022-22965
  - CVE-2022-22963
  - CVE-2022-22954
  - CVE-2020-8218
  - CVE-2020-15505
  - CVE-2018-6789
  - CVE-2017-6737
  - CVE-2017-6736
  - CVE-2014-1812
  - CVE-2014-0780

- **TLS Inspection:** The following applications are now inspected when accessed from a browser:
  - Google applications (Enhancement)
  - Google Drive (Enhancement)
  - Microsoft General (Enhancement)
  - Microsoft Live (Enhancement)
  - Microsoft Azure (Enhancement)
  - Dropbox (Enhancement)

## Knowledge Base Updates

- [How the Cato Cloud Protects your Account from Ransomware Encryption Actions](/v1/docs/how-the-cato-cloud-protects-your-account-from-ransomware-encryption-actions)
- [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account)
