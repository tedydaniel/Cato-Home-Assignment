---
title: "How to Find DHCP Host Allocation"
slug: "how-to-find-dhcp-host-allocation"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/how-to-find-dhcp-host-allocation"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Find DHCP Host Allocation

## Overview

This article will explain the steps required to view the allocated DHCP host entries in both the Cato Management Application (CMA) and the local Socket WebUI.

> [!NOTE]
> Note:
> 
> Please be aware that the number of DHCP hosts displayed may differ between the Socket WebUI and the CMA.

## Showing DHCP Host in the CMA

**To view the allocated DHCP addresses and hosts within the CMA:**

1. Verify that a DHCP range is configured for the network range for a site:
  1. From the navigation menu, select **Network > Sites**, and select the site.
  2. From the navigation menu, select **Site Configuration > Networks**.
  3. Review the DHCP range configured for the network. The example below shows the range 192.168.43.2 - 192.168.43.50 configured for the Native Range.

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247950459421.png)
2. From the navigation menu, click **Site Monitoring > Known Hosts**.
3. Filter for **Hosts in DHCP ranges**, the assigned hosts, and their allocated IP addresses are shown.

![360002694677-mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247950536349.png)

## Socket WebUI

It is also possible to view the DHCP entries on the webpage of the Socket WebUI.

1. From the Site Configuration > Socket page for the site, [open the Socket WebUI](/v1/docs/accessing-the-socket-webui).
2. On the **Monitor** page, you can see the DHCP Server Entries at the bottom of the page.
