---
title: "Product Update - June 13th, 2022"
slug: "product-update-june-13th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-june-13th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 13th, 2022

## New Features & Enhancements

- **Dynamic NAT for Local Routing Rules:** You can now configure dynamic NAT for a local routing rule in a Socket site. [Read more](/v1/docs/local-routing-at-the-socket).
  - Supported from Socket v13.0 and higher

- **LAN Blocking for SDP Clients:** In some cases, an SDP user can’t connect to the network because a local resource (like a wireless printer) has the same IP address as an internal server. Enabling the LAN Blocking feature sets Clients to route traffic to the Cato Cloud (ignoring local devices) and connect to the internal corporate resources.
  - Supported from Windows Client v5.3 and higher

- **Supporting IP Ranges in WAN and Internet Firewalls:** The Cato Management Application supports adding the **IP Range** item to the **Source** of a firewall rule. [Read more](/v1/docs/what-is-the-cato-wan-firewall).
- **Enhancement to LDAP Sync Settings to Limit Amount of Deleted or Disabled Users:** Today to help with user management, you can set a maximum number of users that are deleted from your Cato account as part of the LDAP sync. Now, this feature includes both users that are scheduled to be deleted or disabled. [Read more](/v1/docs/syncing-users-with-ldap).
- **Improvements to the Cato Management Application:** Cato is constantly working to make the Cato Management Application better and easier to use. Check out these improvements to configuring rules and settings:
  - Hover over a group or category and a pop-up window shows the group members
  - When searching for an item (entity), you can search according to a wide range of meta-data and not just according to the name. For example, in a firewall rule search for network ranges according to the **Description** of the range.

## Security Updates

- **New Application for Yahoo Mail:** Previously the **Yahoo** application was in the General category and was responsible for all Yahoo services. Now there is a new application **Yahoo Mail** in the Email category for Yahoo email services and the **Yahoo** application is for all the other Yahoo services.
- **IPS Signatures:**
  - Malware - Suncrypt (New)
  - Malware - Quantum (New)
  - Malware - AvosLocker (New)
  - Malware - AlphVM (New)
  - Brute-force Attempt - HTTP NTLM Authentication (Enhancement)
  - CVE-2022-30190
  - CVE-2022-28932
  - CVE-2022-26134
  - CVE-2021-43936
- **Application Database:**
  - Netskope (New)
  - Yahoo Mail (New)
  - Yahoo (Enhancement)
  - DNS Over HTTPS – DOH (Enhancement)
  - HTTP (Enhancement)
  - WeTransfer (Enhancement)

## Knowledge Base Updates

- [Client Access Features per OS and Version](/v1/docs/access-features-per-client-os-and-version)
- [Working with Analytics for Specific SDP Users](/v1/docs/working-with-analytics-for-specific-sdp-users)
