---
title: "Product Update - Aug. 21st, 2023"
slug: "product-update-aug-21st-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-aug-21st-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Aug. 21st, 2023

## New Features & Enhancements

- **New Global IP Ranges for Policy Rules:** Over the next few weeks, we are adding the new [**Global IP Range** entity](/v1/docs/using-ip-ranges-in-policies) to the Security policies, which is shared across them. For example, you may have an IP Range allocated for office printers, and you want to define various policies controlling the access to and from them including: WAN Firewall, Internet Firewall, and TLS Inspection policies.
  - The **Global IP Range** entities can be configured in a new page **Networking > IP Ranges**. The format can be a range of IPs, a single IP or a CIDR network
  - The existing **IP Range** entity is now called **Custom IP Range** with no change to functionality (the Custom IP Range only applies to the specific policy)
  - When you select the **IP Range** for a setting in the rule, you select if it will be a **Global IP Range** or a **Custom IP Range**
- **Stories Workbench Enhancement - Grouping Stories:** For improved context when reviewing security stories in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench), you can now show the stories in groups sorted by details such as **Source**, **Indication** and more.
  - Each group highlights the number of high-risk stories for that group
- **Allowlisting for DNS Protection:** We are introducing a new feature to our [DNS Protection service](/v1/docs/customizing-the-dns-protections-for-ips) that lets administrators allowlist specific domain names, to exclude them from DNS Protection scans.
  - To allowlist a domain, add it to a rule in the IPS Allow List for the Outbound scope, with Destination defined as the domain. The IPS Allow List for domains are applied to DNS Protection scans
- **SaaS Security API Supports Remediation Actions for OneDrive:** You can now define actions in Data Protection and Threat Protection rules to remediate potential security breaches in your organization’s [OneDrive tenant](/v1/docs/microsoft-onedrive-configuring-the-data-protection-api-connector). When a rule is matched, these actions can be applied:
  - **Remove Share:** When a user tries to share a file, the SaaS Security API engine removes the unauthorized sharing permission
  - **Quarantine:** When a user tries to upload a file, the SaaS Security API engine moves it to a quarantine folder and then users can no longer access it. The admin can access the file to investigate and restore it if necessary
- **SaaS Security API Enhancement - Threat Protection Aligned with Inline Anti-Malware File Exceptions:** The file exceptions defined for the inline Anti-Malware and NG Anti-Malware policies are now also excluded from the SaaS Security API Threat Protection scans.
  - File exceptions can be added from Threat Protection events, and apply to both the SaaS Security API and inline Anti-Malware scans
  - For information on creating file exceptions for Threat Protection scans, see the documentation for the different SaaS Security API connectors [here](/v1/docs/data-protection-api)
- **Enhancement for accountMetrics API** **Site and User Queries:** We are introducing a change to the accountMetrics API, that lets you query specific sites and users. The data is returned separately for Sites and Users.
  - There is no change or impact for queries that only include sites
  - For queries that include users, provide the user IDs as a separate argument

## Cato SDP Client Releases

- **Windows Client v5.8:** We are starting the gradual rollout for Windows Client version 5.8 during the week of Aug. 21, 2023. These are the planned features and enhancements for this version:
  - **SDP Users With Always-On Can Authenticate to a Captive Portal by Default:** Captive Portal Detection temporarily bypasses Always-On to allow login to the Captive Portal. This feature is enabled by default.
    - The Captive Portal Detection checkbox is removed from the Settings page in the Client
    - No impact to SDP users that don’t connect to a captive portal, or aren’t using Always-On
  - **Updated OPSWAT OESIS Framework:** We updated the [OPSWAT OESIS framework](https://www.opswat.com/products/endpoint-security-sdk/device-compliance) used by the Client to version 4.3.3644
  - **Upgrade OpenSSL Library:** We upgraded the OpenSSL Library used by the Client to version 3.1.1
  - **Upgraded Chromium version:** We upgraded the Chromium version used by the embedded browser in the Client to version 107.1.120
  - **New User Interface:** We improved the Client’s user interface so that it is even more intuitive and easy to use
  - For more information about the Client rollout process, see [Best Practices for Cato Client Upgrades](/v1/docs/recommendations-for-cato-client-upgrades)

## Security Updates

- **IPS Signatures:** View more details about the IPS Signatures and Protections in the [Threat Catalog](/v1/docs/using-the-threat-catalog).
  - Cactus Ransomware (New)
  - Rajah Ransomware (New)
  - CVE-2023-3519 (New)
  - CVE-2023-26360 (New)
  - CVE-2023-26359 (New)
  - CVE-2019-17621 (New)
- **Suspicious Activity Monitoring:** These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Downloading NetScan scanner (New)
  - Downloading Splashtop remote admin tool (New)
  - Executing Commands on a Remote Computer Using WMI (New)
  - Net Group query for particular group in the domain (New)
  - Remotely querying a computer using WMI (New)
- **Apps Catalog:**
  - Added dozens of new SaaS applications (you can view the SaaS apps in the [App Catalog](/v1/docs/using-the-app-catalog))
  - Improved detection and reduced false positives of anonymizers including:
    - ExpressVPN (Enhancement)
    - Mullvad VPN (Enhancement)
    - PureVPN (Enhancement)
- **Application Control Policy (CASB):**
  - Enhanced granular actions for the following apps:
    - Google Drive - Download
    - MS Teams - Delete Message
    - MS Teams - Upload File
- **Remote Browser Isolation (RBI):**
  - Improved browser detection
