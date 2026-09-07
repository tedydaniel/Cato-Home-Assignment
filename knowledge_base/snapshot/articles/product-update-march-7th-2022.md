---
title: "Product Update - March 7th, 2022"
slug: "product-update-march-7th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-march-7th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - March 7th, 2022

## New Features & Enhancements

- **Ukraine Situation – Best Practices for Cyber Security and the Cato Cloud:** With military operations currently underway in Ukraine, there is a global increase in cyber-attacks. Cato's Security teams are monitoring the threats and continually adding protections, intelligence feeds, and indicators of compromise (IoCs) to our security solutions. To help protect against potential cyber-attacks, we prepared an article with security best practices and recommendations as part of our response to this crisis. [Read more](/v1/docs/best-practices-for-cyber-security-and-the-cato-cloud).
- **New Device Posture and Client Connectivity Access Policy:** You can define the conditions that a device must meet before the Cato Client is allowed to connect to the Cato Cloud. The Clients and devices are periodically checked to verify that the Device Posture is valid, otherwise the device is not allowed to connect. [Read more](/v1/docs/configuring-the-client-connectivity-policy).
  - This new granular policy can be applied to groups or individual users, and is also based on their geolocation, Client OS, and Device Posture status
  - Device Posture checks the Anti-Malware status with over 200 supported vendors (including their products and versions)
  - This feature will be available starting March 13th, 2022 (included with SDP user license)
  - Supported for SDP users with Windows Client 5.1 and higher
- **Manage DNS over HTTPS (DoH) Service in the Firewall Policy:** DoH provides additional privacy for web browsing. However, since the DNS requests are encrypted this can introduce security risks. Add the new **DNS over HTTPS (DoH)** service to a firewall rule to monitor or block DoH traffic.
- **Improvements to Application Analytics:** The **Domains** tab in the Application Analytics screen (Monitoring > Application Analytics) is now the **Destinations** tab. This new tab includes the following information:
  - WAN destinations – IP addresses and DNs
  - Internet destinations - domains
- **Customize Presets for Events:** The Events screen (Monitoring > Events) includes a number of predefined preset filters for events. We are introducing the ability to save a the filter, timeframe, and fields as a custom preset that you can use again in the future. [Read more](/v1/docs/analyzing-events-in-your-network).
  - The custom presets are saved separately for each admin’s account
  - Custom presets are available for new Cato Management Application admins with editor permissions
- **Export Bandwidth Licenses to CSV:** Admins can export the site bandwidth license data for an account to a CSV file.
- **Upcoming Changes to Applications:** Starting on March 20th, we are improving the definitions of the applications listed below. Please update the rulebases and policies in your accounts to use the new applications:
  - **OneLogin, Inc** will be deprecated, and replaced with the **OneLogin - Web Access** application
  - **ShareFile** will be deprecated, and replaced with the **Citrix ShareFile** application

## PoP Announcements

- **Quito, Ecuador:** We upgraded the PoP in Quito, and are now providing better service for the connections to this PoP

## Security Updates

- **IPS Signatures:**
  - Malware - QSnatch (New)
  - Malware - SolarMarker (Enhancement)
  - CVE‑2020‑28269
  - CVE-2019-9082
  - CVE-2019-5127
  - CVE-2018-15982
  - CVE-2017-2810
- **Application Database:**
  - DNS over HTTPS - DoH (New)
- **Application Control Policy:**
  - Slack - Delete Message (Enhancement)
  - Facebook - comment (New)

## Knowledge Base Updates

- [Best Practices for Cyber Security and the Cato Cloud (Related to the Ukraine Crisis)](/v1/docs/best-practices-for-cyber-security-and-the-cato-cloud)
- [How Can I Download the Cato Client?](/v1/docs/downloading-the-cato-client)
- [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client)
