---
title: "Product Update - January 20, 2025"
slug: "product-update-january-20-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-january-20-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - January 20, 2025

## New Features and Enhancements

- **New AI-Driven Firewall Analysis and Insights:** We’re introducing an AI-driven enhancement to the [Internet Firewall policy](/v1/docs/what-is-the-cato-internet-firewall) that provides admins with actionable insights to optimize their firewall configurations, improve security posture, and ensure compliance with best practices. The Autonomous Firewall engine automatically analyzes your Internet Firewall rulebase and detects issues such as:
  - Temporary rules
  - Rules that are expired or soon to expire
  - Test rules
- **New Policy for Tenant Control with Header Injection:** Limit the app tenants that users can access using header injections managed with granular rules in a full-featured policy. The **Tenant Restriction** tab in the Security > Application Control page lets you control traffic to specific app tenants. For example, you can restrict the tenants that can be accessed by specific user groups or sites.
- **Endpoint Protection Agent v1.3.1:** In the coming days, we are starting the rollout of Endpoint Protection (EPP) Agent version 1.3.1. This version includes:
  - **Self-Healing:** If the Agent encounters an error, in some cases, it will try to resolve the issue autonomously
  - **Improved Error Messages:** Clearer messaging is displayed in the CMA if the EPP Agent has issues
  - Bug fixes and enhancements
- **Share your Feedback on the Product Updates:** We are starting a new survey to get your feedback on our weekly Product Updates (release notes). Your input helps us ensure the information we provide is clear, relevant, and useful to you. Please take a few minutes to [complete our survey](https://www.surveymonkey.com/r/CatoRN) and share your thoughts.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2017-6206 (New)
    - CVE-2019-11001 (New)
    - CVE-2021-31196 (New)
    - CVE-2021-40407 (New)
    - CVE-2021-40408 (New)
    - CVE-2021-40409 (New)
    - CVE-2023-21554 (New)
    - CVE-2023-34990 (New)
    - CVE-2023-50968 (New)
    - CVE-2024-10924 (New)
    - CVE-2024-11680 (New)
    - CVE-2024-20017 (New)
    - CVE-2024-2874 (New)
    - CVE-2024-32238 (New)
    - CVE-2024-34351 (New)
    - CVE-2024-38023 (New)
    - CVE-2024-38024 (New)
    - CVE-2024-38094 (New)
    - CVE-2024-47076 (Enhancement)
    - CVE-2024-47175 (Enhancement)
    - CVE-2024-47176 (Enhancement)
    - CVE-2024-47177 (Enhancement)
    - CVE-2024-49112 (New)
    - CVE-2024-49113 (New)
    - CVE-2024-49122 (New)
    - CVE-2024-50379 (New)
    - CVE-2024-50603 (New)
    - CVE-2024-53677 (New)
    - CVE-2024-55457 (New)
    - CVE-2024-55956 (New)
    - CVE-2024-56337 (New)
    - Generic Directory Traversal - HTTP (Enhancement)
    - Traffic To Low Popularity Destination Within Suspicious ASN (Enhancement)
    - ZTE ZXHN H108N Wifi Password Disclosure(New)
    - CnC Activity - PrivateLoader (New)
    - Ransomware - AnonWorld (Enhancement)
    - Ransomware - Aptlock (Enhancement)
    - Ransomware - Black (Prince) (Enhancement)
    - Ransomware - Contacto (Enhancement)
    - Ransomware - CONTI (Enhancement)
    - Ransomware - Electronic (New)
    - Ransomware - EnCiPhErEd (Enhancement)
    - Ransomware - GANDCRAB 5.0.4 (New)
    - Ransomware - Locklocklock (New)
    - Ransomware - MAGA (Enhancement)
    - Ransomware - NoDeep (Enhancement)
    - Ransomware - Prince (New)
    - Ransomware - RA World (Enhancement)
    - Ransomware - RedLocker (Enhancement)
    - Ransomware - Risen (Enhancement)
    - Ransomware - ROGER (Enhancement)
    - Ransomware - Sage (Enhancement)
    - Ransomware - SatanCD (Enhancement)
    - Ransomware - Secplaysomware (Enhancement)
    - Ransomware - TRUST FILES (Enhancement)
    - Ransomware - Weaxor (Enhancement)
    - Ransomware - XFUN (Enhancement)
    - Ransomware - YE1337 (Enhancement)
- **Apps Catalog**
  - More than 50 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)):
    - Windows Autopatch (New)
    - MQTT (Enhancement)
    - Piktochart )Enhancement)
    - Amazon WorkSpaces )Enhancement)
    - WeTransfer )Enhancement)
    - Microsoft Intune )Enhancement)
- **XDR Indications of Attack Signatures:**
  - Threat Prevention:
    - Fake CAPTCHA Detection (New)
  - Anomaly Detection:
    - First Time Upload to an S3 Bucket (New)
    - Deprecated or Unauthorized Protocols First Occurrence Anomaly (New)
    - Unusual Country Activity for Account (New)
- **Application Control (CASB):**
  - ChatGPT - Download (New)
  - ChatGPT - Upload (New)
  - Claude – Conversation (New)
  - Egnyte – Download (Enhancement)
  - Egnyte – Upload (Enhancement)
- **Data Loss Prevention (DLP):**
  - ChatGPT - Download (New)
  - ChatGPT - Upload (New)
  - Google Drive – Upload (New)
  - Egnyte – Download (Enhancement)
  - Egnyte – Upload (Enhancement)
- **File Control:**
  - PCAP (Enhancement)
  - PCAPNG (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - Networking
      - Network Appliance
        - Aruba Networks (Enhancement)
        - Fortinet (Enhancement)
        - Juniper Networks (Enhancement)
        - Lancom Systems (Enhancement)
        - Ubiquiti (Enhancement)
        - TP-Link (Enhancement)
    - Vendors
      - Hikvisoin (Enhancement)
      - Dell (Enhancement)
      - VMware (New)
      - Sony (New)
      - Epson (New)
    - PC
      - Thin Client
        - PCoIP Endpoint Device (Enhancement)
      - Workstation
        - Windows 10 (Enhancement)
        - Apple (Enhancement)
    - Mobile
      - Mobile Phone
        - Samsung (Enhancement)
    - IoT
      - Printer
        - HP (Enhancement)
        - Xerox (Enhancement)
        - Zebra (Enhancement)
      - VoIP
        - Avaya (Enhancement)
        - Grandstream Networks (Enhancement)
        - Mitel (Enhancement)
        - Snom Technology (Enhancement)
        - Neat (New)

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
