---
title: "Product Update - Mar. 18th, 2024"
slug: "product-update-mar-18th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-mar-18th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Mar. 18th, 2024

## New Features & Enhancements

- **Enhanced RBI Security Controls:** We added granular security controls to [Remote Browser Isolation (RBI)](/v1/docs/configuring-the-rbi-service-for-browsing-sessions) that let you customize the security settings for RBI sessions.
  - You can now block or allow these actions: upload, download, copy/paste, and print
  - We also added a **Read Only** setting that prevents users from entering credentials or other sensitive data on the site
- **Increased Visibility of Remote User Access and Security:** We added new widgets to the [User Dashboard](/v1/docs/using-the-access-overview-page). These widgets show:
  - How the [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) is used to control network access for remote users
  - How often the [Always-On Policy](/v1/docs/protecting-users-with-always-on-security) is bypassed and with which bypass method
  - This feature will be gradually enabled over the next few weeks
- **Enhanced XDR Stories for Microsoft Defender Endpoint Alerts:** We added data to [Microsoft Endpoint Alert](/v1/docs/microsoft-defender-for-endpoint-alerts-configuring-the-xops-integration) stories that can help you identify key Indicators of Compromise in stories related to outbound network traffic, such as for phishing attacks.
  - These are the new data fields:
    - **Target:** The URL involved in the story
    - **Destination IP:** The remote IP address involved in the story
  - Available for XDR Core, XDR Pro and MDR customers
- **Updated the Threshold for Link Congestion Alerts:** We [updated the threshold](/v1/docs/working-with-link-health-rules) when **Congestion** is configured to **True** to trigger an event only when more than 1% of packets are discarded. This change improves the accuracy for detecting link congestion, and can change the frequency of the email notifications.
- **New Banner Announcing Expiration for Trial Site Licenses:** When there are [sites with trial licenses](/v1/docs/working-with-cato-license-types) that are expired or about to expire, the Cato Management Application will now show a banner indicating the expiration date for these licenses.
  - The banner is displayed on all pages, until all sites have valid licenses
- **Cato Management Application Enhancement:**
  - **Enter Socket Description:** We added a new **Description** field to the Sockets page, and you can add information (such as Socket hostname or an ID) to quickly identify the correct Socket in your account. For HA sites, you can configure different descriptions for Primary and Secondary Sockets

## PoP Announcements

- **Tokyo, JP**: A new IP range is now available in the Tokyo PoP location - 150.195.219.0/24

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Ransomware Frea (New)
    - Ransomware RSA-4096 (New)
    - Ransomware WoXoTo (New)
    - Ransomware DoNex (Enhancement)
    - Ransomware Duralock (Enhancement)
    - Ransomware Dxen (Enhancement)
    - Ransomware Genesis (Enhancement)
    - Ransomware Ma1x0 (Enhancement)
    - Ransomware Payuranson (Enhancement)
    - Ransomware Rocklee (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - Ransomware Zarik Locker (Enhancement)
    - CVE-2024-21412 (New)
    - CVE-2023-52251 (New)
    - CVE-2023-47218 (New)
    - CVE-2023-46731 (New)
    - CVE-2023-40289 (New)
    - CVE-2023-25573 (New)
    - CVE-2022-48323 (New)
    - CVE-2022-42139 (New)
    - CVE-2022-36883 (New)
    - CVE-2022-31499 (New)
    - CVE-2022-31188 (New)
    - CVE-2018-14716 (New)
    - CVE-2023-46263 (Enhancement)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indication:
      - Suspicious Executable File Download (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Download impersonated image
    - Enumerating user terminal sessions in RPC
    - Harnessing spools service to gain authentication on target machine
    - Pastebin bot communication
    - PowerShell impersonated IMG
- **TLS Inspection:**
  - Added global bypass for these applications, preventing possible [TLS inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) errors:
    - Brother Industries
    - Cisco Meraki Cloud
    - Oculus
    - Ring
    - Western Digital
    - Xerox
- **Apps Catalog:**
  - Added over 100 new SaaS applications including (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)):
    - Trados
  - Enhanced this application:
    - Zoom
- **File Identification:**
  - Enhanced file identification in Cato Cloud services for the following file types:
    - BAT and CMD
    - Binary files

## Knowledge Base Updates

- [Glossary of Cato Terms](/v1/docs/glossary-of-cato-terms)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
