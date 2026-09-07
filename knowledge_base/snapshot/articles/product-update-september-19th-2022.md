---
title: "Product Update - September 19th, 2022"
slug: "product-update-september-19th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-september-19th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - September 19th, 2022

## New Features & Enhancements

- **Client Connectivity Policy Logic Change:** We improved the logic for the Client Connectivity Policy so that it follows logic as the Internet and WAN firewall ([read more](/v1/docs/what-is-the-client-connectivity-policy)):
  - Ordered rulebase, and rules are sequentially applied to a connection
  - Supports the Block action in addition to Allow, for better granularity of rules
- **SDP Client Pre Login for Windows Devices:** Cato’s SDP Pre Login allows devices to establish a secure connection to the Cato Cloud before Windows login. For example, a new remote user receives a new Windows device, and can’t connect to the corporate AD to authenticate. [Read more](/v1/docs/using-windows-pre-login-and-the-sdp-client).
  - Requires that Windows Client v5.4 is installed on the device
    - See the Knowledge Base article above for a complete list of prerequisites
- **Identity Agent Based User Awareness:** Cato’s User Awareness now supports using the Cato Client as an identity agent to identify Azure AD users, in addition to on-prem AD users. [Read more](/v1/docs/using-cato-identity-agents-for-user-awareness).
  - No SDP licenses are required for the users and the identity is reported without any action by the user
  - Supported from Windows Client v5.4 and higher
- **Updates to the Cato Management Application:**
  - **IP Range in Security Rules:** We enhanced the rules for the following Security policies and you can configure the **IP Range** entity for:
    - TLS Inspection (source)
    - Application Control (source)
    - IPS Allowlist (source)
  - **Easily Show Relevant Events for a Firewall Rule:** The Internet and WAN firewall screens let you drill-down and show the recent events related to a specific firewall rule.
  - **Improvements to the Cloud Apps Dashboard:** The **Top Apps** widget in the Cloud Apps Dashboard includes these new actions:
    - Add the app to the Sanction Apps Category with one click
    - Drill-down and show the data for the app in the Application Analytics screen
    - Show the information for the app in the Cloud Apps Catalog

## Cato SDP Client Updates and Releases

- **Cato Client Automatically Directs to IdP Portal for SSO Authentication:** Over the next few weeks, for accounts that have SDP users which authenticate with Single Sign On (SSO), the Client will automatically direct the user to the IdP login page.
- **Android Client v5.0:** Android Client version 5.0 includes the newest infrastructure for Cato’s SDP Client solution and will soon be available to download from the Google Play Store. This version includes:
  - Support for Always On and SSO ([read more](/v1/docs/protecting-users-with-always-on-security))
  - Improved look and feel
  - Support for Device Authentication with certificates ([read more](/v1/docs/legacy-device-authentication))
  - Support for the following Client Access features:
    - Split Tunnel (for include mode)
    - External browser
  - Install the Client with an MDM
  - Improved tunnel resiliency
  - Bug fixes and enhancements
- **Windows Client v5.4:** Windows Client version 5.4 will soon be available in the [User Portal](http://myvpn.catonetworks.com/). This version includes:
  - Improved error messages with better explanations for connectivity issues in the Client for SDP users
  - Performance enhancements
  - Bug fixes:
    - When the Client is in Office Mode, it now uses the PAC file of the local system instead of the PAC file defined in the Cato Management Application

## PoP Announcements

- **Monterrey, Mexico:** A new Cato PoP will shortly become available in Monterrey
- **Montreal, Canada:** A new Cato PoP will shortly become available in Montreal

## Security Updates

- **Application Database:**
  - Added more than 70 new SaaS Applications (you can view the SaaS apps in Monitoring > Cloud Apps Catalog)
  - Enhanced 17 SaaS applications
- **Updates to Application Control Policy:** New granular actions for these apps:
  - Google Data Studio: Create Report, Authorize App, Invite People, Download Report (Export)
  - WhatsApp: Voice Message, Download, Upload
- **TLS Inspection:**
  - Webex: inspected over browsers
  - Bitbucket: inspected over browsers
