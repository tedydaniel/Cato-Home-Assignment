---
title: "Updating the Socket WAN Interface Bandwidth"
slug: "updating-the-socket-wan-interface-bandwidth"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/updating-the-socket-wan-interface-bandwidth"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating the Socket WAN Interface Bandwidth

Configure the Socket WAN interface bandwidth setting according to the terms of the Cato site license.

- Active/Active configurations - Assign the link bandwidth for half of the total site bandwidth license

For example, if the site license is for 1000 Mbps, define the bandwidth for the two active links (upstream and downstream) as 500 Mbps.
- Active/Passive configurations - Assign the active and passive links to the total site bandwidth

For example, if the site license is for 1000 Mbps, define the bandwidth for the active and passive link (upstream and downstream) as 1000 Mbps.

If the Cato site license has a higher bandwidth value than the ISP link bandwidth, set each link’s bandwidth according to the ISP bandwidth. For more about Cato site licenses, see [Managing Site Bandwidth Licenses](/v1/docs/managing-site-bandwidth-in-licenses).

For links that are dedicated to off-cloud or Alt WAN traffic, this is not part of the site bandwidth license, and set the link to the actual last-mile bandwidth.​

> [!NOTE]
> Note:
> 
> For sites with multiple links, follow the procedure below for each link.

**To update the Socket WAN interface bandwidth:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Select the Socket Interface. The **Edit Socket Interface** panel opens.
4. In **Bandwidth**, enter the new **Downstream Mbps** and **Upstream Mbps** values. If your site license includes global and regional bandwidth, you should enter the total bandwidth here (global + regional).

You can set values as whole numbers or include up to one decimal.
5. Click **Apply**, and then click **Save**.

![Edit_Socket_Interface.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248020879645.png)
