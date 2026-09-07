---
title: "Product Updates - October 6, 2025"
slug: "product-updates-october-6-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-october-6-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - October 6, 2025

## New Features & Enhancements

- **New Browser Extension Version:** In the coming weeks, Cato is gradually releasing Browser Extension v1.1, which includes the following features:
  - Browser Extension WAN Access: The [Cato Browser Extension](/v1/docs/configuring-the-cato-browser-extension) now lets users securely access WAN applications (HTTP/S) directly from their Chrome browser
  - This version requires that [TLS Inspection is enabled](/v1/docs/tls-inspection)
  - Improved monitoring for when the Browser Extension disconnects from the PoP
- **New macOS Client v5.10.5:** Starting October 5, 2025, we will gradually roll out the new [macOS Client version 5.10.5](/v1/docs/summary-of-cato-macos-client-releases). This version includes:
  - Support for macOS Tahoe version 26
  - Stability improvements
  - Security updates
  - Bug fixes
- **X1700B Socket Supports Higher Port Density for Data Center and Campus Sites:** We added the option to use two add-on port cards, allowing a total of eight 10Gbps fiber ports.
  - Use the [Site Configuration > Socket page](/v1/docs/working-with-socket-sites) in the CMA or the <kbd>addSocketAddOnCard</kbd> API to enable the second card
  - Supported for Socket v24 and higher
  - Previously, only a single add-on card was supported
- **Upcoming Change to Cato Password Policies:** To enhance security and align with industry best practices, we will update the password requirements for both SDP users and CMA admins. We will start rolling out this change on October 15, 2025, for new or updated passwords.
  - This impacts CMA admins and SDP users authenticating with a Cato password
  - Passwords must contain one of each: lowercase letter, uppercase letter, number, and a special character (new requirement)
  - Additionally, admin passwords cannot contain an email address or be on our list of common passwords (e.g., **aB12345!**)
  - This change applies only to newly created or updated passwords. **There is no impact on existing passwords**
- **Read IPsec Tunnel Configurations via API:** You can now programmatically retrieve all IPsec tunnel configurations using the Cato API. This streamlines tunnel monitoring and configuration management across large deployments.
  - Access detailed IPsec tunnel configuration data via the <kbd>tunnelConfig</kbd> object under <kbd>IPsecInfo</kbd> in the <kbd>accountSnapShot</kbd> query

## PoP Announcements

- **Lima, PE:** A new range (199.27.45.0/24) will soon be added to the Lima PoP location.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
