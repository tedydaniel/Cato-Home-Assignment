---
title: "Product Update - July 25th, 2022"
slug: "product-update-july-25th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-july-25th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 25th, 2022

## New Features & Enhancements

- **IP Range in Network Rules:** The Cato Management Application now supports adding the **IP Range** item to:
  - Internet network rule (source)
  - WAN network rule (source or destination)
- **Site Pre-Provisioning:** You can create and configure all the settings for a site and prepare to connect it to the Cato Cloud before it has a license. Assign the license to the site when you are ready to activate it. [Read more](/v1/docs/working-with-cato-license-types).
  - Available for new sites and existing sites
- **LAN Monitoring Enhancements:** We made the following improvements to LAN Monitoring (Network > Sites > {site name} > Site Configuration > LAN Monitoring)
  - Monitor up to 50 hosts per site (previously 10 hosts). [Read more](/v1/docs/configuring-lan-monitoring-for-a-site).
  - Improved behavior for events and email notifications - when the host is unreachable, only one event is generated (support for email notifications - coming soon)
- **Manage Email Alerts for SDP Users:** Starting on July 31st, 2022, when you disable SDP users in the Cato Management Application, by default they receive an email notification that their SDP user account is disabled. You can now choose to stop sending these alerts for all users.
- **Enhanced Remote User Data in the Users Screen:** The Users screen (Access > Users) also includes context about the remote devices and shows the **Device** operating system and **Client Version**. [Read more](/v1/docs/working-with-analytics-for-specific-sdp-users).

## Cato SDP Client Releases

- **macOS Client v5.1:** the macOS Client version 5.1 is now available in the [Cato User Portal](https://myvpn.catonetworks.com/login). This version includes:
  - For SSO - Using the external browser to authenticate with the IdP
  - Enhancements:
    - Improved overall stability and connectivity to the Cato Cloud
    - Enriched user notifications
    - Improved connectivity when switching networks
  - Bug fixes:
    - Resolved issue where for some SDP users, when the computer leaves sleep mode, required manually disconnecting and then reconnecting the Client
    - Resolved bugs in the SSO authentication flow

## PoP Announcements

- **Bogota, Colombia:** A new Cato PoP will shortly become available in Bogota
- **Helsinki, Finland:** A new Cato PoP is now available in Helsinki
- **San Jose, Costa Rica:** A new Cato PoP is now available in San Jose

## Security Updates

- **IPS Signatures:**
  - Malware CreepyDrive
  - Malware Lyceum
  - Malware Clipper
  - CVE-2022-33891
  - CVE-2022-26135
  - CVE-2022-0083
  - CVE-2021-27342
  - CVE-2018-13379
  - Brute Force Attempt - HTTP Unauthenticated Redirect
  - Brute Force Attempt - FTP
  - Brute Force Attempt - SMB Authentication
  - Brute Force Attempt - WordPress Login
- **Application Database:**
  - Large update to application definitions in the Cato Cloud:
    - Added over 100 new SaaS applications
    - Enhanced over 90 existing applications
- **Application Control Policy:**
  - Granular Action: Gitlab pull / clone (New)
  - Granular Action: Gitlab push (New)
  - Granular Action: Bitbucket push (New)
  - Granular Action: Bitbucket pull / clone (New)
  - Granular Action: Github push (New)
  - Granular Action: Github pull / clone (New)
  - Granular Action: Quora Login (New)
  - Granular Action: Quora Post (New)
  - Granular Action: Trello Upload (New)
  - Granular Action: Trello Download (New)
  - Granular Action: Trello Login (creds) (New)
  - Granular Action: Trello Login (SSO + Third Party) (New)
  - Granular Action: Pastebin - Login (third party) (New)
  - Granular Action: Atlassian Download (New)
  - Granular Action: Atlassian Upload (New)
  - Granular Action: Google - Logoff (Enhancement)
- **Data Loss Prevention:**
  - Improved DLP scan - minimum files size is 1KB (previously 32KB)
  - Generic textual group includes these file types: TXT, XML, and CSV

## Knowledge Base Updates

- [Analyzing Traffic for all Account Sites](/v1/docs/analyzing-traffic-for-all-account-sites)
