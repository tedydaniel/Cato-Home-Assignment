---
title: "Product Update - November 14th, 2022"
slug: "product-update-november-14th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-november-14th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - November 14th, 2022

## New Features & Enhancements

- **Apps Catalog Includes SaaS Apps, On-Prem Apps, and Services:** The new Apps Catalog contains Cloud Applications, on-prem Applications, Services, and information about Sanctioned Apps. In addition, you can easily filter by Type, Category, Risk, and more. [Read more](/v1/docs/using-the-app-catalog).
- **MITRE ATT&CK® Framework Dashboard:** Starting on Nov. 20th, you can analyze threats with the new MITRE ATT&CK® Dashboard. The dashboard enhances visibility for security events by mapping them to standard MITRE framework tactics and techniques. This dashboard lets you extend your analysis and forensics regarding compromised sources and device distribution per technique.
- **Firewall Device Check for Device Posture:** New Device Check that verifies the status of the firewall running on the endpoint device. [Read more](/v1/docs/creating-device-posture-profiles-and-device-checks).
  - Use the Firewall Device Check for Client Connectivity Policy, or firewall Device setting
  - Supported for Windows Client v5.4 and higher
- **Enhancing Internet Network Rules:** New option for network rules to preserve the source port during NAT Translation. [Read more](/v1/docs/configuring-network-rules).
- **Cato Management Application Enhancements**
  - **DLP Dashboard and SaaS Security API Dashboard:** Filter all dashboard widgets with an inline filter
  - **Improved Support for LDAP Domain Controllers:** We are starting the gradual rollout over the next week for improved ability to define the settings for Domain Controllers (DC) as follows:
    - Internal DC - IP address, or select a host defined for a site
    - Public DC - IP address, or a domain

## Cato SDP Client Releases

- **Windows Client v5.5:** We are starting the gradual rollout of Windows Client version 5.5. This version includes:
  - **Client Self Service:** The user can now record and then reproduce an issue that occurred with the Client. Then the user can upload the traffic capture and log files to Cato Support for further analysis.
  - **New Client Installer:** We are introducing a new installer for the Client that includes improved stability for the upgrade process.
  - Bug fixes and enhancements
- **iOS Client v5.0:** the iOS Client version 5.0 will soon be available in the App Store. This version includes:
  - **Always-On and SSO:** The Cato Client now supports authentication with Single Sign-On (SSO) when the Always-On policy is enabled for iOS devices. [Read more](/v1/docs/protecting-users-with-always-on-security).
  - **Bypass Code:** Generate a Bypass Code to allow SDP users to temporarily disconnect the Client. [Read more](/v1/docs/protecting-users-with-always-on-security).
  - Bug fixes and enhancements
- **Android Client v5.0.2:** The new version of the Android Client is now available in the Google Play store. This version includes:
  - Bug fixes and enhancements
- **Linux Client v5.0.2:** The new version of the Linux Client is now available in the [User Portal](https://myvpn.catonetworks.com/login). This version includes:
  - Bug fixes and enhancements
  - Starting with v5.0.2, SDP users can authenticate based on the settings in the Cato Management Application using SSO or username & password

## Security Updates

- **IPS Signatures:**
  - CVE-2022-44032
  - CVE-2022-41040
  - CVE-2022-32417
  - CVE-2019-11358
- **Application Database:**
  - Added more than 240 new SaaS applications (you can view the SaaS apps in Monitoring > Apps Catalog)
  - Enhanced 50 SaaS applications
- **Updates to Application Control Policy:**
  - New granular actions for this app:
    - GigaFile: Upload, Download
  - Enhanced actions for this app:
    - LinkedIn: Add Attachment
- **Updated Data Loss Prevention:**
  - New Data actions were added for this app:
    - GigaFile: Upload, Download
  - Enhanced actions for these apps:
    - Dropbox: Upload, Download
    - Box: Upload, Download

## Knowledge Base Updates

- [Understanding Cato's Managed Socket Upgrade Service](/v1/docs/understanding-cato-s-managed-socket-upgrade-service)
