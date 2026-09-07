---
title: "Product Update - October 7, 2024"
slug: "product-update-october-7-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-october-7-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - October 7, 2024

- **Azure vSockets Include Support for 2 NICs**: The newest vSocket firmware includes an enhancement for supporting Azure VMs with 2 NICs. This lets you use smaller VM instance types to reduce Azure costs.
  - Existing 3 NIC vSockets can [migrate](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution) to a new 2 NIC VM instance
  - Previously, only instances with 3 NICs were supported (now you can choose 2 or 3 NICs)
  - Supported from Socket v21.0.18735 and higher (requires a [manual upgrade](/v1/docs/manually-upgrading-a-socket))
  - Click [here](https://academy.catonetworks.com/azure-vsocket-support-for-2-nics) to watch the video

- **Upcoming Update for Connectivity Health Rules to No Longer Include Users or User Groups:** Users regularly connect and disconnect from a network and can generate many Connectivity Health Rules email notifications that are unrelated to link connectivity or quality. To improve the accuracy of Connectivity Health Rule alerts, starting from January 2, 2025, users and user groups can no longer be included as a **Source** in [Connectivity Health Rules](/v1/docs/working-with-link-health-rules).
  - For more information, see this [article](/v1/docs/users-user-groups-can-no-longer-be-included-as-source-in-connectivity-health-rul)
  - Click [here](https://academy.catonetworks.com/eol-link-health-alerts-for-remote-users) to watch the video
- **CMA Enhancement** - **Admin Settings Menu:** For a more intuitive and user-friendly experience, we redesigned the [admin settings](/v1/docs/setting-the-cma-user-interface-preferences) menu.
  - The Branding page settings are applied to the new menu.
  - No impact on CMA functionality
