---
title: "Product Update - May 8th, 2023"
slug: "product-update-may-8th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-may-8th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 8th, 2023

## New Features & Enhancements

- **Cato DLP Supports Automated Import for MIP Labels:** You can now automatically import your Microsoft Information Protection (MIP) labels and use them in [DLP Data Types](/v1/docs/working-with-custom-data-types-for-dlp) for the Data Control policy. The labels are fully managed in your Microsoft tenant and then the DLP engine applies them to identify the sensitive content.
- **Enhancement for Site Analytics**: Over the next several weeks, we are gradually migrating the [Site Analytics data](/v1/docs/showing-the-site-network-analytics) to a new infrastructure for better accuracy and performance.
  - The following screens will be affected by this change: Site Analytics, User Analytics, Site Overview, and SDP User Overview
  - There is no change to the AccountMetrics API, however the data will be retrieved from a new source
  - After this change is applied to an account, the earliest start date for data in Site Analytics will be from March 1st. To gain access to previous data, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new)
- **Configuration File for the SDP Client is No Longer Supported:** Starting from 4 June, to harden remote access security, using the Configuration File to provide user credentials for new SDP users will be unavailable.
  - There is no change for existing SDP users that have downloaded and used a Configuration File
  - SDP Users can still authenticate by entering their Username and Password manually
- **Cato Management Application Enhancement:**
  - **Improved Visibility for Socket Link Connectivity Status:** The [Socket configuration](/v1/docs/managing-sockets) screen now shows the physical connectivity status of each link

## Cato SDP Client Releases

- **macOS Client v5.4:** We are planning to start the rollout for macOS Client v5.4 during the week of **May 14th**. These are the planned features and enhancements for this version:
  - **New Device Posture Check for Device Certificates Provides Increased Security:** You can now include a check for a device certificate within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and security policies. This check:
    - Improves Device Authentication by ensuring the SDP users or user groups in the rulebased policy have the required certificate before connecting to your network
    - Lets you define stricter Device Posture requirements in your Firewall policies to access corporate resources
  - **Always-On Now Supports Temporarily Bypassing the Cato Network:** SDP users with [Always-On](/v1/docs/protecting-users-with-always-on-security) can temporarily bypass Cato security and access the Internet by entering a bypass code in the macOS Client (the same experience as bypass code for the Windows Client).
  - **Bug fixes:**
    - Improved reconnect after a device wakes up from sleep mode
    - Re-authentication with external browser opens single browser tab
    - Improved Client connectivity when downloading or transferring large files
    - SDP users can disable office mode
  - For more information about the Client rollout process, see the following articles:
    - [Best Practices for Cato Windows and macOS Client Upgrades](/v1/docs/recommendations-for-cato-client-upgrades)
    - [Client Lifecycle Management](/v1/docs/client-lifecycle-management)

## PoP Announcements

- **Tokyo, Japan:** A second Cato PoP is now available in Tokyo.
- **Austin, United States:** A new Cato PoP will shortly become available in Austin.
