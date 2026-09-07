---
title: "Product Update - June 19th, 2023"
slug: "product-update-june-19th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-june-19th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 19th, 2023

## New Features & Enhancements

- **Security Update - IPS Protection for MOVEit Vulnerability:** On June 9th, 2023, Cato deployed a protection for the IPS service to protect against an exploit leveraging CVE-2023-34362 found in Progress MOVEit software. (See this [blog post](https://www.catonetworks.com/blog/cato-protects-against-moveit-vulnerability-cve-2023-34362/) for more information).
- **Anti-Malware Protection Now Includes Encrypted Files:** We enhanced the [Anti-Malware](/v1/docs/configuring-the-anti-malware-policy) service with the ability to identify and block downloads of encrypted files. This helps secure your organization by preventing users from downloading malicious files disguised as legitimate encrypted files, which is a common technique in ransomware and other cyber attacks.
  - When the Anti-Malware service identifies an encrypted file, it returns a verdict of **Encrypted**
    - Anti-Malware rules set for **All Files** now also include the verdict of **Encrypted**, and block or allow all files that match the rule
    - Previously, Anti-Malware verdicts included **Suspicious** and **Malicious**
  - You can configure an Anti-Malware rule to allow downloading **Encrypted** files to meet the needs of your users
- **Improved Troubleshooting for TLS Inspection:** To help resolve issues related to [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account), we added these enhancements to help understand and resolve untrusted server certificate related issues:
  - Events now include a new field with a better explanation for these issues
  - The **Block/Prompt** page now shows users more information about these issues for them to communicate to you
- **accountMetrics API Supports Specific Sites or SDP Users:** We added an optional **scope** field to the accountMetrics API, which lets you specifically query sites (SCOPE_SITES) or SDP users (SCOPE_SDP_USERS).
  - There is no impact or change to existing queries
  - We recommend that you use this field to avoid potential inconsistencies where specific site and SDP user IDs are provided for a single API query
- **Upcoming Change to eventsFeed Cato API - Ending Support for the Fields Format:** As of July 16th, 2023 Cato will stop supporting the **fields** format for the eventsFeed read-only Cato API.
  - The **fields** format is functionally compatible with the **fieldsMap** or **flatFields** formats
  - No changes or impact to **fieldsMap** or **flatFields** formats
  - We recommend using the **fieldsMap** format for eventsFeed API calls

## PoP Announcements

- **Osaka, Japan:** A second Cato PoP is now available in Osaka.
