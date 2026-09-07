---
title: "Showing the DHCP Pools for a Site"
slug: "showing-the-dhcp-pools-for-a-site"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/showing-the-dhcp-pools-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Showing the DHCP Pools for a Site

## Overview of DHCP Pools

The DHCP Pools screen shows all the networks and VLANs that are configured to receive IP addresses from Cato's DHCP server. The network ranges for a site are configured in the Networks screen for that site (Network > Sites > {site name} > Site Configuration > Networks).

![DHCP_Pool.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247990698525.png)

**To show the DHCP pools for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Monitoring > DHCP Pools**.
3. Click **Reload** to refresh the data on the screen (the data isn't automatically updated).

## Understanding the DHCP Pools Fields

This section explains the columns and fields in the DHCP Pools screen.

- Network Range - **Name** and **Subnet** of the range that is configured for a DHCP range
- DHCP Range - DHCP range that is configured for this network segment
- Allocated IPs - Number of IP addresses in the range that the Cato DHCP server has allocated to hosts
- Available IPs - Number (and percentage) of IP addresses that are currently available for this network segment
