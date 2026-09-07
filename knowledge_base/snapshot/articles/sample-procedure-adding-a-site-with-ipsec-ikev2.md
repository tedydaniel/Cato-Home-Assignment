---
title: "Sample Procedure - Adding a Site with IPsec IKEv2"
slug: "sample-procedure-adding-a-site-with-ipsec-ikev2"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/sample-procedure-adding-a-site-with-ipsec-ikev2"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sample Procedure - Adding a Site with IPsec IKEv2

## Overview

This article is a sample procedure that explains how to create a new site with an IPsec IKEv2 connection. After you configure the site settings in the **Add Site** window, go to the **IPsec IKEv2** section and configure the settings for the VPN tunnels.

This sample deployment has a secondary connection to a different PoP.

For Cisco ASA appliances, there is a known incompatibility with Cato, [read more](/v1/docs/configuring-ipsec-ikev2-sites).

**To add a new IPsec IKEv2 site to your account:**

1. From the navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![AddSite_IKEv2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275594499869.png)
3. Enter the **Site Name** and for **Type** select **Branch**.
4. Set the **Connection Type** to **IPsec IKEv2**.
5. Configure the **Country**, **State**, and **Time Zone**.
6. Configure the **Native Range** for the internal LAN to **10.30.30.0/24**.
7. Click **OK**.

The new site is added to the account.
8. To configure the IPsec IKEv2 settings for the primary and secondary connections, click **Site Configuration > IPsec**.
9. In the **General** section, set the **Service Type** to **Generic**.
10. Because this is a new site, select the PoP IP addresses for the tunnels:
  1. Expand the **Primary** section, and click **IP Allocation Settings**.
  2. In the **Configuration** window, select **New York**, **Chicago**, and **London**.

![360002878458-AllocatedIP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275603784477.png)
  3. Click **Submit**.
11. Configure the settings for the primary connection:

![IPsec_Primary_IKEv2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275610783389.png)
  1. Set the **Public IP** settings:
    - **Cato IP (Egress)** - select **London**
    - Enter the **Primary Destination IP** address as **192.168.3.18**
  2. Do not enter values for **Private IPs**, this site does not use BGP dynamic routing.
  3. Set the **Downstream** bandwidth to **200** and the **Upstream** bandwidth to **100** Mbps.
  4. In **Primary PSK**, and click **Edit Password** enter the pre-shared key for the primary connection.
12. Configure the settings for the secondary connection:
  1. Expand the **Secondary** section.
  2. Set the **Public IP** settings:
    - **Cato IP (Egress)** - select **Dublin**
    - Enter the **Primary Destination IP** address as **192.168.4.20**
  3. Do not enter values for **Private IPs**, this connection does not use BGP dynamic routing.
  4. Set the **Downstream** bandwidth to **200** and the **Upstream** bandwidth to **100** Mbps.
  5. In **Secondary PSK**, and click **Edit Password** enter the pre-shared key for the secondary connection.
13. Expand the **Routing** section, and make sure that **Initiate connection by Cato** is selected.
14. Click **Save**. The IPsec IKEv2 connections for the site are configured.
