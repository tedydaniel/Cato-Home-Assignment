---
title: "Socket Version 15.0 Release Notes"
slug: "socket-version-15-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-15-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 15.0 Release Notes

Socket version 15.0 includes the following features:

- **Blocking Local Routing when a Site is Disconnected from PoP:** If a site is temporarily disconnected from the Cato Cloud, the default behavior is fail-open. You can change the behavior to fail-closed and block the local routing traffic for specific sites or the entire account.
- **Use the Socket WebUI to Reset Registration Data for a Socket:** After using the Cato Management Application to unassign a Socket, if you can't reassign the Socket to a different site, use the Socket WebUI to force the Socket to enter the unassigned state. [Read more](/v1/docs/managing-sockets).
  - After the Socket is unassigned, a notification is shown in the Cato Management Application that lets you assign the Socket to a different site.
- Stability improvements
  - The Socket now drops traffic arriving with the incorrect VLAN tagging from the LAN switchAs part of implementing enhancements for the packet handling mechanism, the Socket applies a stricter policy for misconfigured connectivity settings. For example:
- Security updates

- Bug fixes

This version also includes the firmware for new features, and in the coming weeks we will update the Cato Cloud and release the following feature:

- **Setting Socket Port when Bypassing the Cato Cloud:** For sites with bypass rules, you can choose to assign a preferred Socket WAN port to egress the traffic.
