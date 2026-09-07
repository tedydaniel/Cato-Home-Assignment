---
title: "Security Controls for the Cato Browser Extension and Enterprise Browser"
slug: "security-controls-for-the-cato-browser-extension-and-enterprise-browser"
updated: 2026-08-26T09:15:18Z
published: 2026-08-26T09:15:18Z
canonical: "knowledge.catonetworks.com/security-controls-for-the-cato-browser-extension-and-enterprise-browser"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Security Controls for the Cato Browser Extension and Enterprise Browser

## Overview

The Cato Browser Extension and Enterprise Browser let you provide secure, browser-based access to SaaS, Internet, and WAN applications without installing the full Cato Client. They apply your existing network and security policies, including threat prevention, firewall rules, and conditional access. This makes it an ideal solution for enabling access on unmanaged or BYOD devices. For information, see [What is the Cato Browser Extension](/v1/docs/what-is-the-cato-browser-extension) and [What is the Cato Enterprise Browser](/v1/docs/what-is-the-cato-enterprise-browser).

The Browser Data Protection page in the Cato Management Application (CMA) lets you configure local security controls that prevent users from exfiltrating sensitive data when using the extension.

To address security risks on unmanaged endpoints, Cato uses local controls enforced within the browser session. These controls run directly in the page context and are effective even when:

- The app is end-to-end encrypted (e.g., WhatsApp Web, Telegram)
- User actions generate no network traffic (e.g., clipboard copy)

### Key Benefits

The Browser Data Protection page provides the following benefits:

- Prevent data loss from unmanaged browsers using local control rules
- Ensure visibility and control even for encrypted applications and traffic

### Use Case

ABC Company hires contractors who need access to internal apps like Slack and Salesforce from unmanaged devices.The IT team tells contractors to install the Cato Browser Extension and they configure access in the Client Connectivity Policy. They also add rules in the Browser Data Protection policy to block copy/paste, downloads, and printing, and apply a watermark. This ensures secure, limited access without requiring device management.

## Configure Security Controls

Configure security controls for users or user groups that are working with the Browser Extension or Enterprise Browser. The security controls are an ordered rulebase that defines the policy for users. Once a user or group matches the criteria for a specific rule, the actions are applied to the user or group. Rules that are listed after the matching rule are not applied.

**To configure security controls:**

1. Navigate to **Security > Browser Data Protection**.
2. Click **New** and determine whether the following actions are allowed or blocked:
  - Copy
  - Paste
  - Download
  - Upload
  - Type (in a text box)
  - Print
3. (Optional) Determine if you want to add a watermark to the background of users with the Browser Extension installed.
4. Click **Publish**.
