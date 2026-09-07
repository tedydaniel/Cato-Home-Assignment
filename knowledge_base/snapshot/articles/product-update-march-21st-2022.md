---
title: "Product Update - March 21st, 2022"
slug: "product-update-march-21st-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-march-21st-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - March 21st, 2022

## New Features & Enhancements

- **Internet Traffic Backhauling:** You can use network rules to backhaul specific Internet traffic to sites that are designated as backhauling gateways. The specific Internet traffic is then forwarded to the backhauling site’s local IP gateway for further processing. [Read more](/v1/docs/configuring-internet-traffic-backhauling).
  - The backhauling gateway sites require Socket 12.0 or higher
  - Backhauling traffic is supported for sites and SDP users
- **Improved SDP User Experience with Browser Authentication:** We updated the Authentication (Access > Client Access > Authentication) screen so you can select the Browser Authentication experience for your Client users and use the in-Client browser or the external default OS browser. [Read more](/v1/docs/configuring-the-authentication-policy-for-cato-clients).
  - In-Client browser is supported from Windows Client v5.2 and macOS Client v5.0 and higher
  - Please note that in some cases, external default OS browser is still required. [Read more](/v1/docs/preparing-to-install-the-cato-client)
- **Improvements to Events:** Over the next two weeks, we are gradually implementing a significant performance improvement to the new Cato Management Application Events screen. This will provide better response times, visibility for distribution of events entries, and bug fixes. [Read more](/v1/docs/analyzing-events-in-your-network).
  - Starting on March 27th, you will only be able to view events in the new Cato Management Application, and the legacy Event Discovery screen will no longer be available
- **Announcing End-of-Life for EventFeed API Query:** The Cato API EventFeed query was replaced by the more robust and improved EventsFeed in July 2021. Starting on March 27, 2022, the EventFeed query will be end-of-life and will not be available to customers. Read more about the EventsFeed query [here](/v1/docs/cato-api-eventsfeed-large-scale-event-monitoring).
  - Questions? Please contact [api@catonetworks.com](mailto:api@catonetworks.com?subject=Question%20About%20EventFeed%20API%20Query)

## Cato SDP Client Releases

- **macOS Client v5.0:** The new macOS Client version 5.0 is now available and we added the capability for SDP users to directly download the macOS Client PKG file for version 5.0 from a [new portal](https://myvpn.catonetworks.com/downloadMvpnClient). This version includes:
  - Improved user experience with in-Client browser and re-authentication enhancements
  - Initial installation of v5.0 requires that you deploy it on all the macOS devices, available either with a PKG file or using an MDM
    - Version 4.5 is only available from the App Store (if it’s necessary to rollback to this version, install from the App Store)
  - Supports Managed Upgrades with an MDM ([read more](/v1/docs/deploying-and-upgrading-macos-clients-with-an-mdm))
  - Known Limitations - In some cases, this version might experience problems with these configurations:
    - Azure Conditional Access
    - Proxy configuration
    - For accounts that use a third-party proxy, make sure to whitelist the following items (for both HTTP and HTTPS):
      - IP address - 85.255.31.1
      - URL - sso.ias.catonetworks.com

## Security Updates

- **IPS Signatures:**
  - Malware -Bondat (Enhancement)
  - CVE-2015-7645 (Enhancement)
- **Application Control Policy:**
  - Granular App: Outlook - add attachment (Enhancement)
- **TLS Inspection (for CASB license):**
  - Dropbox on browsers (New)
  - Google Services on browsers (Enhancement)

## Knowledge Base Updates

- [(New) Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients) (Updated to include Setting the Browser Authentication for the Account)
