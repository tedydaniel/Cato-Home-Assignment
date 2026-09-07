---
title: "Socket Version 10.0 Release Notes"
slug: "socket-version-10-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-10-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 10.0 Release Notes

Socket version 10.0 includes the following features:

- **Socket High Availability Resiliency Enhancement:** This feature enhances Socket connectivity and resiliency during a failover and greatly minimizes interruptions/disconnects for applications and traffic flows.
  - When traffic fails over between the Sockets, the secondary Socket follows the primary Socket and uses the same PoP for the tunnels. This maintains sessions and states to minimize disruptions for end-users.
  - This feature is enabled by default when Sockets upgrade to this version.
- **Stability improvements.**
- **Bug fixes.**

This version also includes the firmware for new features, and in the coming weeks we will update the Cato Cloud and release the following features:

- **DHCP Relay per Network Range:** You can now define DHCP Relay settings for network ranges within a site, and use multiple DHCP Relay servers.
- **High Availability for Azure vSockets (Early Availability Support) :** The ability to add a secondary vSocket to Azure sites to provide redundancy for the site.
