---
title: "Product Update - January 24th, 2022"
slug: "product-update-january-24th-2022"
updated: 2026-09-06T12:55:58Z
published: 2026-09-06T12:55:58Z
canonical: "knowledge.catonetworks.com/product-update-january-24th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - January 24th, 2022

## New Features & Enhancements

- **Enhancements to the New Cato Management Application:** We are implementing many improvements and bug fixes, and thanks to everyone who provided us with detailed feedback. Here are the highlights:
  - Added new screens for Maintenance Window and Known Hosts
  - The Topology screen now shows both Disconnected and Disabled sites
  - Improved usability for navigation menus, for Sites and Users, the **Site** and **User Configuration** menus are now at the top of the navigation menu
  - For IPsec sites, added the **Connection Status** button to show details of the site’s connection to the Cato Cloud
- **Improved Granularity for Never-Off for SDP Users:** Now you can define the Cato Client Connectivity Policy settings (including Never-Off) for specific users that are different from the account settings. [Read more](/v1/docs/protecting-users-with-always-on-security).
  - Only available in the new Cato Management Application

## Cato SDP Client Releases

You can also contact Support to request access to the Client v5.0

- **macOS Client v5.0:** We are preparing to release the new macOS Client version 5.0 and you will receive an email with instructions to download the upgrade package. For improved control and visibility, starting with Client v5.0, new versions will no longer be available via the Apple App Store. Instead installation and upgrades are performed via a DMG file or an MDM. This version includes:
  - Initial installation of v5.0 requires that you deploy it on all the macOS hosts, available either with a DMG file or using an MDM
  - Supports distributing Clients via an MDM
  - For future macOS versions, the Client are managed by the Upgrade Policy in the Cato Management Application

**Note:** The current policy settings will also be applied to macOS Clients
  - Improved user experience for re-authentication
  - Known Limitations - In some cases, this version might experience problems with these configurations:
    - Azure Conditional Access
    - Proxy configuration
    - For accounts that use a third-party proxy, make sure to [allowlist the correct IPs](/v1/docs/cma-ip-allowlist)

## Security Updates

- **IPS Signatures:**
  - CVE-2021-43798
  - CVE-2021-41277
  - CVE-2021-3199
  - CVE-2021-28169
  - CVE-2021-23758
  - CVE-2021-22053
  - CVE-2020-5777
  - CVE-2020-4428
  - CVE-2020-4427
  - CVE-2020-3161
  - CVE-2020-29448
  - CVE-2020-25223
  - CVE-2020-19302
  - CVE-2018-4878
  - CVE-2018-20434
  - CVE-2017-9248
  - WordPress Social Warfare Plugin Remote Code Execution
  - Thecus NAS Server Control Panel Command Injection
  - Telesquare LTE Router Denial Of Service
- **Application Database:**
  - AMON PAPI - aruba papi (New)
  - ISAKMP (New)
  - RADIUS (New)
  - Office365 Login (Enhancement)
  - Windows Autopilot (Enhancement)
  - Outlook (Enhancement)
  - Cato Management Application (Enhancement)
  - Zoom (Enhancement)

## Support Tickets Resolved

- #122999, #127034, #127710, #127730, #127794, #128730, #129851, #129978, #130588, #130986, #131580, #132832, #132956, #133807, #134007, #134155, #134176, #134428, #134703, #135212, #136555
