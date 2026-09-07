---
title: "Product Update - December 26th, 2022"
slug: "product-update-december-26th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-december-26th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - December 26th, 2022

## New Features & Enhancements

- **Updated Hardware for the X1700 Socket:** We certified the updated **X1700B** Socket as a second hardware platform for X1700 Socket sites, and we're starting to ship the new model to customers.
  - The two X1700 Sockets are fully interoperable, and can be installed together in the same HA cluster
  - Both models have the same pricing
  - Cato will continue to provide support for both models
  - See this [FAQ](/v1/docs/faq-x1700-socket-hardware-update-x1700b) for more about the X1700 Socket hardware update
- **Accounts Using Registration Codes Can Now Configure SSO for Specific Users:** For accounts that want to migrate from Cato’s Registration Codes (Access > Directory Services > User Provisioning) to Single Sign-On (SSO), we now support the option to configure both methods under the same account. This lets accounts currently using Registration Codes gradually migrate by setting SSO authentication for specific users. [Read more](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).
- **Enhanced Data for Security Rules Export:** When you export security rules, the CSV file now includes the Description field for rules in the following Security policies:
  - Internet and WAN firewall
  - TLS Inspection
  - Application Control and Data Control
- **Easy Creation of New Security Rules by Duplicating Existing Rules:** Starting January 1st, you can duplicate a rule in your security policies and then modify it to create a new rule. Duplicating a rule creates a new identical rule directly below the original, which you can then easily adjust as needed. Rule duplication is supported for these security policies:
  - Anti-Malware
  - TLS Inspection
  - Application Control and Data Control

## Security Updates

- **IPS Signatures:**
  - CVE-2022-37159
  - CVE-2022-36667
  - CVE-2022-34974
  - CVE-2022-41128
  - CVE-2022-24112
  - CVE‑2021‑27561
- **Application Database:**
  - Added more than 250 new SaaS applications (you can view the SaaS apps in Monitoring > Apps Catalog), including:
    - DLP Toolbox
    - WhatsApp Voice Call
    - Windstream Video Conferencing
- **Updates to Application Control Policy:**
  - New granular actions for this app:
    - DLP Toolbox: Upload File, Upload Text
- **Updates to Data Loss Prevention:**
  - New Data actions were added for this app:
    - DLP Toolbox: Upload File, Upload Text
