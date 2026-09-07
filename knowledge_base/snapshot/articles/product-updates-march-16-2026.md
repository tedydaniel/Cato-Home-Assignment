---
title: "Product Updates - March 16, 2026"
slug: "product-updates-march-16-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-march-16-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - March 16, 2026

## New Features & Enhancements

- **Forensic Analysis for DLP - Support for Google Cloud Storage:** To investigate DLP policy violations, forensic evidence helps you effectively understand their context and validate false positives. Evidence is encrypted and can now be stored only in [Google Cloud Storage](/v1/docs/google-cloud-configuring-the-forensic-storage-connector).
  - Sensitive data is stored only on the customer environment
  - DLP license required
- **Detailed Visibility of Interconnected Apps - Support for Salesforce**: View detailed information about third-party apps and plugins connected to [Salesforce](/v1/docs/salesforce-configuring-the-interconnected-apps-integration). This visibility helps you understand which external apps are used in your environment and how they interact with core services.
  - View the **Plugins** option on Security > Applications in the **Inventory** tab
  - CASB license required
- **IoT/OT Security Integration with Claroty for High-Precision Device Inventory:** To increase the accuracy of device discovery, you can now integrate [Claroty](/v1/docs/claroty-configuring-the-device-management-integration) device intelligence data with Cato’s device inventory. A unified view with enriched attributes from both systems is presented on the Home > Device Inventory page.
  - Requires an IoT/OT Security license
- **Application Control via API - Support for Workday:** Connecting SaaS apps to Cato lets you understand who is accessing each app and identify suspicious activities or trends even when users are not connected to the Cato Cloud. You can now connect your [Workday](/v1/docs/workday-configuring-the-app-activities-integration) account to provide visibility into user activities.
  - The Workday connector is available from the **Integrations Catalog**, under **App Activities**
  - CASB license required
- **Support for ForgeRock SSO for Admin:** We added [ForgeRock](/v1/docs/configuring-forgerock-sso) as an SSO provider for authenticating admins in the Cato Management Application.

- **Generate Historical Posture Reports:** To review the Posture checks for your account at a specific point in time, you can generate a [Best Practices report](/v1/docs/generating-a-posture-or-posture-compliance-report) from a date in the past. This capability helps you compare historical results with the current report to track improvements and demonstrate progress over time.
- **Advanced Groups Supported as Destination in Internet Firewall:** In the Internet Firewall, [Advanced Groups](/v1/docs/working-with-cma-advanced-groups-and-groups) can now be used as a Destination as well as a Source. For example, this lets you use public IP ranges as destination conditions in the firewall.
- **DLP Extracts and Scans Embedded Images:** Data Loss Prevention ([DLP](/v1/docs/creating-dlp-content-profiles)) inspection now includes images embedded in documents. The engine extracts images and scans them for sensitive data, detecting potential data leaks within image content.
  - Supported for Microsoft Office and PDF files

## PoP Announcements

- New ranges will soon be available for the following PoP locations:
  - **Amsterdam, NL:** 159.117.241.0/24
  - **New York, US:** 199.27.50.0/24
  - **Paris, FR:** 159.117.240.0/24

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 5 new apps (ConnexAI, Microsoft attack simulation, OpenCode, Questera, Tasklet)
  - Enhanced Apps:
    - 1Password
      - Added domain **agilebits.com**
    - Adobe Ads
      - Application is now available in Application Control rules
    - Adobe Creative Cloud
      - Application is now available in Application Control rules
    - Autodesk
      - Added domains **autocad360.com**, **autocadws.com**
    - Filestack, Inc.
      - Added domain **filepicker.io**
    - Goldcast
      - Updated app domains
    - MagickPen
      - Application is now available in Application Control rules
    - Microsoft Login
      - Added domain **msidentity.com**
    - Microsoft Office365
      - Added domain **microsoft365.com**
    - OptinMonster
      - Application is now available in Application Control rules
    - PandaDoc Inc.
      - Added domain **pandadoc-static.com**
    - PDF Converters Unified
      - Removed domain **pandadoc-static.com**
    - Postman
      - Added domains **postman.co**, **pstmn.io**
    - Scribd-
      - Updated app domains
    - Sentry
      - Updated app IPs
    - Soti
      - Added domain **mobicontrolcloud.com**
      - Updated app IPs
    - Vasion Print (formerly PrinterLogic)
      - Modified name from **Printer Logic** to **Vasion Print (formerly PrinterLogic)**
      - Application is now available in Application Control rules
    - Zscaler
      - Added domains **zdxbeta.net**, **zdxgov.net**, **zdxten.net**, **zpabeta.net**, **zpagov.net**, **zpagov.us**, **zpatwo.net**, **zscalergov.com**, **zscalerten.net**, **zslogin.net**, **zsloginbeta.net**
  - Category Changes:
    - Business Information:
      - Added apps: N|Solid, PandaDoc Inc.
    - Computers and Technology:
      - Added app: N|Solid
    - General:
      - Added app: PandaDoc Inc.
    - Generative AI Tools:
      - Added app: Outreach Corporation
      - Removed app: N|Solid
    - Information Security:
      - Added app: N|Solid
    - Productivity:
      - Added app: Outreach Corporation
      - Removed app: N|Solid
    - Shopping:
      - Removed app: PandaDoc Inc.
  - Socket:
    - New Apps: 1 apps (Zscaler (Domains and IP based))
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2024-9643 (New)
  - CVE-2025-24786 (New)
  - CVE-2025-34299 (New)
  - CVE-2025-40536 (New)
  - CVE-2025-40554 (New)
  - CVE-2026-24423 (New)
  - CVE-2026-25512 (New)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Abnormal Anti-Malware Block Activity (New)
    - First occurrence of a non-risky GenAI application in the Organization (New)
    - First Occurrence of Inbound Activity towards OT Device (New)
    - First Occurrence of Inbound Application Activity to IoT Device (New)
  - Threat Hunting
    - AI Agent Registration to Moltbook (New)
    - Automated Exfiltration Attempt (New)
    - First Occurrence of NDAA-Restricted Device Vendor activity (New)
    - Inbound Traffic to Non-Compliant IoT Device (New)
    - IoT Device Communication with Malicious Targets (New)
    - OpenClaw Installation Script Download (New)
    - Potential AI Agent Identified by HTTP Headers (New)
    - Potential AI Agent Identified by User-Agent (New)
- **Application Control Policy / CASB**
  - Gmail
    - Send Mail (Enhancement)
  - GMX
    - Upload (New)
  - Instagram
    - Login (Enhancement)
  - Yahoo Webmail
    - Upload (Enhancement)
  - Box
    - Upload (Enhancement)
  - DropBox
    - HTTP API upload (New)
- **OS Detection**
  - IOS
    - OS detection (Enhancement)
- **TLS Inspection**
  - Added global bypass rules for the TikTok and Snapchat apps (for native, non-browser clients)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - SalesForce
    - Third Party Apps (New)
  - CRWD
    - EDR (Enhancement)
  - Zoom
    - Experience (Enhancement)
  - Microsoft Teams
    - Activity (Enhancement)
  - Atlassian
    - Improve Activity type and category mapping (Enhancement)
  - Box
    - Improve Activity type and category mapping (Enhancement)
  - GitHub
    - Improve Activity type and category mapping (Enhancement)
  - Google Apps
    - Improve Activity type and category mapping (Enhancement)
  - Microsoft Exchange
    - Improve Activity type and category mapping (Enhancement)
  - Microsoft General
    - Improve Activity type and category mapping (Enhancement)
  - Salesorce
    - Improve Activity type and category mapping (Enhancement)
  - SharePoint
    - Improve Activity type and category mapping (Enhancement)
  - Slack
    - Improve Activity type and category mapping (Enhancement)
  - Zendesk
    - Improve Activity type and category mapping (Enhancement)
