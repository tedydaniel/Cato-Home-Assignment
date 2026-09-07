---
title: "Product Updates - October 27, 2025"
slug: "product-updates-october-27-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-october-27-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - October 27, 2025

## New Features & Enhancements

- **Granular Tenant Awareness for SaaS Apps**: You can now define Application Control rules based on specific SaaS tenants, adding [granular visibility](/v1/docs/restricting-access-to-saas-application-tenants) and control over user activity across apps like Microsoft OneDrive, Google Drive, and Dropbox. This enables you to differentiate between corporate and personal app instances. For example, you can allow users to upload to your corporate Google Drive but block them from uploading to personal accounts to prevent data exfiltration. Key benefits include:
  - Enforce CASB and DLP policies with tenant-level precision
  - Restrict access to personal or unsanctioned tenants
  - Reduce compliance risk and data leakage
  - Requires CASB or DLP license
  - Click [here](https://academy.catonetworks.com/granular-tenant-awareness-for-saas-apps) to watch a video recording of this feature
- **Streamlined LDAP User Management - Import Filters and Dynamic Groups:**[Easily manage](/v1/docs/ldap-query-filters-and-dynamic-groups) which LDAP users are imported into Cato (Access > Directory Services) and create dynamic user groups based on LDAP attributes.
  - **Import LDAP Users with Custom Filters:** Use LDAP query filters to control which users are imported into Cato.
    - Import only relevant users (e.g., full-time employees) based on LDAP conditions
    - The filter defines the user directory that dynamic groups are based on
  - **Create Dynamic LDAP-Based User Groups:** Define user groups in the CMA that automatically reflect LDAP attribute values, which helps maintain accurate, role-based policies without manual adjustments.
    - The dynamic group is a subset of the user directory you defined via the filter
    - Group users based on attributes like **department**, **location**, or **title**
    - Membership updates automatically with every LDAP sync
    - Click [here](https://academy.catonetworks.com/ldap-users-management-filters-dynamic-groups) to watch a video recording of this feature
- **New URL for Cato Client Upgrade Service:** To ensure seamless upgrades, you must allowlist a new URL used by the [Cato Client upgrade service](/v1/docs/recommendations-for-cato-client-upgrades).
  - Add <kbd>https://clients.cdn.catonetworks.com/</kbd> to your allowlist
  - Required for automatic upgrades on Windows, macOS, and Linux
- **WAN Recovery Site-to-Site Tunnels Status in CMA:** To ensure WAN Recovery readiness at all times, the site-to-site tunnels feature enables [recovery of WAN traffic](/v1/docs/socket-site-resiliency-with-wan-recovery) in case of an unlikely failure, such as a severe Cato Cloud issue. To enhance operational visibility, we have added a new status that indicates whether sites are fully, partially, or not ready for WAN Recovery. The status is displayed for sites as well as WAN interfaces.
  - You can view the status in these CMA pages: Topology, Sites, Site Configuration > Socket
  - Each site and interface can be viewed in wanRecoveryStatus in the accountsnapshot API queries
  - Supported for Socket v24 and higher
- **Support for Keycloak SSO for Users:** We added [KeyCloak as an SSO provider](/v1/docs/configuring-keycloak-sso) for authenticating users.
  - Previously, it was only possible to authenticate CMA admins using Keycloak
  - Click [here](https://academy.catonetworks.com/sso-keycloak) to watch a video recording of this feature
- **Identical Internet-Only IP Ranges For IPsec Sites:** To simplify network management and improve security for guest traffic, you can now [configure identical IP ranges](/v1/docs/configuring-network-ranges-for-a-site) in multiple IPsec sites to be used for Internet-only traffic.
  - Previously was supported for Socket sites
  - Click [here](https://academy.catonetworks.com/internet-only-ranges) to watch a video recording of this feature

**Final Reminder - Expiring 2015 Certificate for TLS Inspection**

- The default 2015 Cato root certificate used for TLS Inspection and Threat Prevention will expire on **October 29, 2025**. You must **immediately** distribute and activate the new Cato certificate. Otherwise, there will be service disruptions and security vulnerabilities in your account.
  - For more information, see this [video](https://catonetworks.wistia.com/medias/tbq3v1nlu1) and [FAQ article](https://support.catonetworks.com/hc/en-us/articles/22781778613149?utm_source=Notification&amp;utm_medium=emailfaq&amp;utm_campaign=email0408faq&amp;utm_id=TLSnewcert0408faq).
  - No action is needed if you’ve already activated the 2024 Cato certificate

## PoP Announcements

- **Lima, PE:** A new range (199.27.45.0/24) is now available for the Lima PoP location.

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 17 new apps – Google Alerts, Google Books, Google Scholar, Google Trends, Google Vertex AI, Naver Blog, Naver CHZZK, Naver Cafe, Naver Finance, Naver Land, Naver Mail, Naver News, Naver Papago, Naver Pay, Naver Shopping, Poka, Tplink Omada Discovery Protocol
  - Enhanced Apps:
    - 8x8
      - Added domains **8x8cloud.com**, **p8t.us**, **packet8.net**, **wavecell.com**
    - Fortinet
      - Updated app IPs
    - Google Calendar
      - Updated app domains
    - Google Finance
      - Updated app domains
    - Google keep
      - Updated app domains
    - Google meet
      - Updated app domains
    - Google News
      - Updated app domains
    - Google Pay
      - Updated app domains
    - Google Shopping
      - Updated app domains
    - Google Travel
      - Updated app domains
    - Grok (X.ai)
      - Modified name from **X Ai Corporation** to **Grok (X.ai)**
    - Grok (X.ai) API
      - Modified name from **X.ai API** to **Grok (X.ai) API**
    - HubSpot
      - Updated app domains
    - Make by Celonis
      - Modified name from **Celonis S R O** to **Make by Celonis**
    - OneDrive Personal
      - Modified name from **OneDrive** to **OneDrive Personal**
    - PDF Converters Unified
      - Removed domain **athena.io**
    - Skype and MS Teams
      - Updated app domains
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2020-20601 (New)
  - CVE-2021-46104 (New)
  - CVE-2022-24288 (Enhancement)
  - CVE-2022-37122 (New)
  - CVE-2024-34470 (New)
  - CVE-2024-9166 (New)
  - CVE-2025-0674 (New)
  - CVE-2025-10035 (New)
  - CVE-2025-20362 (New)
  - CVE-2025-27222 (New)
  - CVE-2025-36604 (New)
  - CVE-2025-49844 (New)
  - CVE-2025-57822 (New)
  - CVE-2025-59049 (New)
  - CVE-2025-61882 (New)
  - Heuristic - ICMP Tunneling - Abnormal Response Count (New)
  - Block Malicious Domain After Multiple Anti-Malware Detections (New)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - TeamViewer WAN Lateral Remote Connectivity (Enhancement)
- **Out of Band Integrations**
  - GitHub Activities
    - Code Scan Alerts (New)
    - Vulnerability Scan Alerts (New)
    - Secret Scan Alerts (New)
  - Slack Activities
    - Security Anomalies (New)
  - Microsoft 365 App Activities
    - Security Anomalies (New)
  - Google Activities
    - Security Anomalies (New)
  - Crowdstrike EDR
    - Device Inventory - Reporting devices from the EDR connector (New)
  - ChatGPT Activities (Enhancement)
- **Application Control Policy / CASB**
  - Box - Inline tenant control (New)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Abnormal Remote Access Protocols Activity Over The LAN (New)
    - First Occurrence of Generative AI Application in the Organization (New)
    - First Occurrence of File Transfer Protocols Activity Over The LAN (New)
    - Abnormal Suspicious Activity (Enhancement)
  - Threat Hunting
    - Outbound DNS Queries for Local Domains (New)
- **Device Inventory**

These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
  - IOT
    - Multifunction Device
      - Canon (Enhancement)
    - Payment Terminal
      - Castles Technology (Enhancement)
      - Verifone (Enhancement)
    - Printer
      - Brother Industries (Enhancement)
      - Epson (Enhancement)
      - HP (Enhancement)
      - Konica Minolta (Enhancement)
      - Kyocera (Enhancement)
      - Lexmark (Enhancement)
      - Xerox (Enhancement)
      - Zebra (Enhancement)
    - Signage Media Player
      - BrightSign (Enhancement)
    - Speaker
      - Algo (Enhancement)
    - Video Conferencing
      - Cisco (Enhancement)
    - VoIP
      - Aastracom (Enhancement)
      - Avaya (Enhancement)
      - Cisco (Enhancement)
      - Digium (Enhancement)
      - Grandstream Networks (Enhancement)
      - Polycom (Enhancement)
      - Snom (Enhancement)
      - Yealink (Enhancement)
  - PC
    - Desktop
      - Dell (Enhancement)
      - HP (Enhancement)
      - Lenovo (Enhancement)
    - Laptop
      - Apple (Enhancement)
      - Dell (Enhancement)
      - HP (Enhancement)
      - Lenovo (Enhancement)
      - Microsoft (Enhancement)
      - Toshiba (Enhancement)
      - Vaio (Enhancement)
    - Thin Client
      - Dell (Enhancement)
    - Workstation
      - Apple (Enhancement)
      - Fujitsu (Enhancement)
      - HP (Enhancement)
      - NEC (Enhancement)
      - Panasonic (Enhancement)
  - MOBILE
    - Mobile Computer
      - Zebra (Enhancement)
    - Mobile Phone
      - Newland (Enhancement)
      - Oppo (Enhancement)
      - Samsung (Enhancement)
      - Vivo (Enhancement)
    - Tablet
      - Samsung (Enhancement)
  - NETWORKING
    - Network Appliance
      - 3Com (Enhancement)
      - Aruba Networks (Enhancement)
      - Juniper Networks (Enhancement)
      - Ubiquiti (Enhancement)
  - OT, IOT
    - IP Camera
      - Axis (Enhancement)
      - Uniview (Enhancement)
  - SERVER
    - Media Server
      - Roku (Enhancement)
    - Print Server
      - HP (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://support.catonetworks.com/hc/en-us/articles/11968052021277-Understanding-Cato-s-Gradual-Rollout). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
