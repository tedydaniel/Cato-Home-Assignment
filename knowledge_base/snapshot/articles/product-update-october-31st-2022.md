---
title: "Product Update - October 31st, 2022"
slug: "product-update-october-31st-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-october-31st-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - October 31st, 2022

## New Features & Enhancements

- **Enhanced DHCP Monitoring:** Admins can now view and monitor any DHCP IP address allocated by Cato in these screens (Network > {site name} > Site Monitoring):

**DHCP IP Lease Event**: Track DHCP IP allocations in the Events screen
  - **Known Hosts (Updated):** We enriched the Known Host page with additional information including: MAC address, DHCP lease information, DHCP range, Last host activity, and more. [Read more](/v1/docs/showing-known-hosts-for-a-site)
  - **DHCP Pools (New):** This new page shows the following information for each configured DHCP range: Network range, Subnet, DHCP range, Number of Allocated IPs, and Number of Available IPs. [Read more](/v1/docs/showing-the-dhcp-pools-for-a-site)
- **New Features for Socket v15:**
  - **BGP Isolated Routing:** We added a reserved BGP community for Socket sites to prevent specific routes propagation from the Socket to the PoP. [Read more](/v1/docs/cato-reserved-bgp-communities).
    - Supported from Socket version 15.0 and higher
  - **Preferred Socket Port for Bypass Rules:** Assign a preferred Socket WAN port for a bypass rule that the Socket uses for egressing traffic. [Read more](/v1/docs/bypassing-the-cato-cloud-site-level-policy).
    - Supported from Socket version 15.0 and higher
- **Cato Management Application Enhancements:**
  - **Show Host Information Inside Policies:** You can hover over the Host name inside a policy to view the following additional information for each Host: Host IP, Site, Interface, and Network Name
  - **Usability Enhancements to Threats Dashboard and DLP Dashboard:** Added a number of small fixes to make it easier to read and analyze the data in the [Threats Dashboard](/v1/docs/using-the-security-threats-dashboard) and [DLP Dashboard](/v1/docs/creating-device-posture-profiles-and-device-checks)

## Cato SDP Client Releases

- **macOS Client v5.2:** We are starting the gradual roll-out for the macOS Client version 5.2. This version includes:
  - **Device Posture:** macOS Support for [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) and [Device Posture](/v1/docs/creating-device-posture-profiles-and-device-checks).
  - **Enhanced Reauthentication Experience:** A notification lets users know that the SSO or MFA session will soon expire, and allows them to seamlessly reauthenticate. [Read more](/v1/docs/understanding-expiring-session-for-users).
  - **Status Bar Icon:** Users can easily connect, disconnect, quit, and open the Client right from the status bar of macOS devices.
  - Security fixes and enhancements
  - Resiliency enhancements
  - For SDP users upgrading from v5.x to v5.2, a macOS limitation requires rebooting the device after upgrading the Client to v5.2

## PoP Announcements

- **Monterrey, Mexico:** A new Cato PoP will be available in Monterrey in the next few days.

## Security Updates

- **IPS Signatures:**
  - Malware - Rapper Bot
  - Null Byte Injection Enhancement
  - CVE-2022-42889
  - CVE-2022-36804
  - CVE-2022-31814
  - CVE-2022-31474
  - CVE-2022-0441
  - CVE-2021-21234
- **Application Database:**
  - Added over 300 new SaaS applications (You can view the SaaS apps in Monitoring > Cloud Apps Catalog)
  - Enhanced over 80 app definitions
  - **Updates to Application Control Policy:** New granular actions for these apps:
    - Discord: Login, Logout, Send Message, Upload
    - Google Applications: Login (enhancement)
  - **TLS Inspection:**
    - Codeload Github – now supports TLS Inspection over browsers
