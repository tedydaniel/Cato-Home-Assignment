---
title: "Product Update - July 11th, 2022"
slug: "product-update-july-11th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-july-11th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 11th, 2022

## New Features & Enhancements

- **Sections for Firewall Rules:** Firewall rulebases with many rules can be hard to organize, navigate, and manage. Now you can add sections to the WAN and Internet firewalls and group related rules together into a single collapsible and expandable section. [Read more](/v1/docs/adding-sections-to-the-wan-and-internet-firewalls).
- **Duplicate Rules for Firewall Policies:** With one click, you can duplicate a rule in your WAN and Internet firewalls. This creates a new identical rule directly below the original rule, and allows you to modify the conditions and parameters as needed.
  - When using Firewall sections, the duplicate rule is added directly below the original rule in the same section
- **Socket HA Enhancement:** Socket High Availability (HA) is now enhanced for Sockets running different minor versions (e.g., Primary Socket runs 14.0.1111, Secondary Socket runs 14.0.2222). The **same version** condition only verifies that both Sockets run the same major version. [Read more](/v1/docs/what-is-socket-ha).

## Cato SDP Client Releases

- **Linux Client v5.0:** Linux Client version 5.0 is now available to download from the [Cato User Portal](https://myvpn.catonetworks.com/login). This version includes:
  - Support for Single Sign-On (SSO) with external browsers. [Read more.](https://support.catonetworks.com/hc/en-us/articles/5731982914333)
    - Requires Linux browser for authentication
    - Supported Linux OS versions:
      - Ubuntu v18 and higher
      - CentOS v8 and higher
      - Fedora v36 and higher
      - Debian v11 and higher
      - Mint v20.3 and higher
  - Automatic authentication with cached credentials
  - Tunnel resiliency and automatic tunnel recovery
  - Faster reconnection
  - Stabilization fixes
- **macOS Client v5.1:** We are starting the gradual roll-out for the macOS Client version 5.1. This version includes:
  - For Single Sign-On (SSO) - Using the external browser to authenticate with the IdP. [Read more](/v1/docs/configuring-the-authentication-policy-for-cato-clients).
  - Enhancements:
    - Improved overall stability and connectivity to the Cato Cloud
    - Enriched user notifications
    - Improved connectivity when switching networks
  - Bug fixes:
    - Resolved bugs in the SSO authentication flow

## Security Updates

- **IPS Signatures:**
  - Malware - PandorahVNC (New)
  - Brute force Attempt Telnet (Enhancement)
  - Brute force Attempt HTTP User Authentication (Enhancement)
  - CVE-2022-30525
  - CVE-2022-22972
  - CVE-2022-1654
  - CVE-2021-44632
  - CVE-2021-44631
  - CVE-2021-44630
  - CVE-2021-44629
  - CVE-2021-44628
  - CVE-2021-44627
  - CVE-2021-44626
  - CVE-2021-44625
  - CVE-2021-44623
  - CVE-2021-44622
  - CVE-2021-40487 (Enhancement)
  - CVE-2021-31166
  - CVE-2018-19949
  - CVE-2017-6862
  - CVE-2017-12149
  - CVE-2010-1871
  - CVE-1999-0532 (Enhancement)
- **Application Database:**
  - Discord (New)
  - Erecruit (New)
  - Google Chat (New)
  - Google Keep (New)
  - Google Meet (New)
  - Packetix (New)
  - RemoteCall (New)
  - RemoteSupport (New)
  - RemoteView (New)
  - Sendgrid (New)
  - Vidyo (New)
  - WebDav (New Service)
  - Bing (Enhancement)
  - Google Hangouts (Enhancement)
  - Miro (Enhancement)
  - Pastebin (Enhancement)
- **Application Control Policy:**
  - Granular Action: Pastebin - Login with credentials (New)
  - Granular Action: Pastebin - Remove paste (New)
  - Granular Action: Pastebin - Edit (New)
  - Granular Action: Pastebin - Upload paste (New)
- **TLS Inspection**
  - Twitter - for macOS, the native Twitter client is bypassed, only browsers are inspected (Enhancement)
