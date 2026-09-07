---
title: "Product Update - November 11, 2024"
slug: "product-update-november-11-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-november-11-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - November 11, 2024

## New Features & Enhancements

- **New Default Cato Certificate for TLS Inspection:** The default Cato certificate used by the TLS Inspection policy and Threat Prevention engines was issued in 2015 and expires on Oct. 29, 2025. You must complete the migration process before the current certificate expires.
  - In the coming weeks, you can download the new certificate from the [Security > Certificate Management page](/v1/docs/managing-certificates-for-tls-inspection), and then [distribute](/v1/docs/distributing-and-installing-device-certificates) it to your organization
  - After **Oct. 29, 2025**, customers who haven’t migrated to the new certificate will experience the following issues:
    - TLS Inspection won’t function properly
    - The Threat Prevention services won’t be able to inspect traffic encrypted with TLS
    - Users may experience issues accessing the Internet and SaaS apps (HTTPS websites)
  - See this [FAQ](https://support.catonetworks.com/hc/en-us/articles/22781778613149-Frequently-Asked-Questions-for-the-New-Default-Cato-Certificate-for-TLS-Inspection) for more information
- **Adjusting Data Unit Size for Cato Data Lake:** We are increasing the size of each [Data Unit](/v1/docs/guide-to-cato-data-lake) by 25%, so the free-of-charge Data Unit included in each account will now be 2.5 million events per hour instead of 2 million events per hour.
  - The cost of each Data Unit remains the same
  - This adjustment is aligned to reflect recent improvements of additional events that provide rich contextual data
  - There are no changes to the estimated required Data Unit calculation
  - You can optimize event logging by following the guidelines provided in [Best Practices for Cato Event Log Storage and Ingestion](/v1/docs/best-practices-for-cato-event-logs-and-ingestion), and also upgrade your total capacity by purchasing additional Data Units if needed
- **Improved CMA Login Security with CAPTCHA**: To enhance account security, we added [CAPTCHA protection](/v1/docs/cma-technical-guidelines) to the admin authentication flow for the Cato Management Application (CMA).
  - This invisible protection runs in the background to prevent unauthorized access by bots without disrupting your regular login process
  - In rare cases, admins may be prompted to re-enter their credentials to complete the login
  - Not applicable for SSO-authenticated admins
- **Linux Client v5.3:** From November 10, 2024 we are starting the rollout of Linux Client version 5.3. This version contains:
  - **Device Checks Applied Behind a Site:** To enforce device compliance requirements behind a site, [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks) are applied to devices behind a Socket
  - **Updated OPSWAT OESIS Framework:** We updated the [OPSWAT OESIS framework](https://www.opswat.com/products/endpoint-security-sdk/device-compliance) used by the Client to version 4.3.3404
  - Bug fixes and enhancements, including:
    - In some cases, the Identity Agent did not correctly identify users
- **New Madrid and Singapore PoP Locations for Cloud Interconnect:** New PoPs for [Cloud Interconnect](/v1/docs/cloud-interconnect-availability) in Madrid (Spain), and Singapore, are now available to immediately connect a site, expanding connectivity and access in the EMEA and APJ regions.
- **API Support for City Field for Sites:** Defining the city for a Socket site improves the accuracy of the automatic PoP selection mechanism, and now you can edit and query the `cityName` using these APIs:
  - Mutation API - `UpdateSiteLocationInput`
  - Query API - `Siteinfo` used in these queries: `SiteSnapshot&nbsp;`and `SiteMetrics`
- **CMA Enhancement - View Public IP Address for IPsec Sites:** We improved the usability of the [Network > Sites page](/v1/docs/working-with-sites) with a new **Public Site IP Address** column so you can easily see the public IPs for IPsec sites without drilling down into the individual site.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - Heuristic - Download of executables/scripts using WebDAV (Enhancement)
    - Microsoft Office 365 Open Redirect
    - Ransomware - Dark Eye (Enhancement)
    - Ransomware - DarkDev (New)
    - Ransomware - Defi (Enhancement)
    - Ransomware - Destroy (New)
    - Ransomware - ElonMuskIsGreedy (Enhancement)
    - Ransomware - FIOI (Enhancement)
    - Ransomware - GonzoFortuna (New)
    - Ransomware - Harma (Enhancement)
    - Ransomware - Heda (Enhancement)
    - Ransomware - Ncov (Enhancement)
    - Ransomware - Nyxe (Enhancement)
    - Ransomware - PlayBoy Locker (Enhancement)
    - Ransomware - Root (New)
    - Ransomware - Shadaloo (Enhancement)
    - Ransomware - Solution (Enhancement)
    - Ransomware - Sougolock (Enhancement)
    - Ransomware - Spider (New)
    - Ransomware - The Bully (Enhancement)
    - Ransomware - Ztax (Enhancement)
    - CVE-2024-6049 (New)
    - CVE-2023-47105 (New)
    - CVE-2020-15415 (New)
    - CVE-2024-44466 (New)
    - CVE-2024-41468 (New)
    - CVE-2024-41473 (New)
    - CVE-2023-0260 (New)
    - CVE-2023-0261 (New)
    - CVE-2023-26256 (New)
    - CVE-2024-45409 (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Compressed LNK File Download over HTTP (New)
    - PsExec After Downloading PsTools from a general site (New)
    - Collecting Security Identifier (SID) from a remote computer, PsGetSID (New)
- **XDR Indications Of Attack Signatures:**
  - Threat Hunting:
    - Suspicious Outbound FTP Activity (New)
    - Multiple PsExec Execution Over SMB (New)
    - Suspicious Remote Management Tool Activity (New)
- **Apps Catalog**
  - More than 200 new Cloud apps (see Apps Catalog):
    - Citrix )Enhancement)
    - Westpac(Enhancement)
    - ServiceNow (Enhancement)
    - Webtorrent (New)
    - Exploit-Db (New)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following apps:
    - Trello – Upload (Enhancement)
    - Box – Upload (Enhancement)
    - Outlook - Send Mail (DLP)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - Networking
      - Network Appliance
        - Aruba Networks (Enhancement)
        - Cisco Meraki (Enhancement)
      - PC:
        - Workstation
          - MSI (Enhancement)
      - IOT
        - Printer
          - Xerox (Enhancement)
          - Lexmark (Enhancement)
      - VoIP
        - Cisco (Enhancement)
        - Polycom (Enhancement)
        - Digium (Enhancement)
        - Yealink (Enhancement)
      - Single Board Computer
        - Raspberry Pi Foundation (Enhancement)
    - OT,IOT
      - IP Camera
        - Verkada (Enhancement)
    - Mobile
      - Mobile Phone
        - Redmi (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
