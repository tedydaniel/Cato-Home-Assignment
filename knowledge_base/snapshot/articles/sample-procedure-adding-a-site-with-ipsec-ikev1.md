---
title: "Sample Procedure - Adding a Site with IPsec IKEv1"
slug: "sample-procedure-adding-a-site-with-ipsec-ikev1"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/sample-procedure-adding-a-site-with-ipsec-ikev1"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sample Procedure - Adding a Site with IPsec IKEv1

## Example of Creating a New IPsec IKEv1Site

This article is a sample procedure that explains how to create a new site with an IPsec IKEv1 (Cato-Initiated) connection. After you configure the site settings in the **Add Site** window, go to the **IPsec** section and configure the settings for the VPN tunnels. In this example, the default IKEv1 phase 1 and phase 2 settings are used for the site.

This sample deployment has a secondary connection to a different PoP.

**To add a new IPsec IKEv1 site to your account:**

1. From the navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![360002795417-AddIKEv1site.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275594730013.png)
3. Enter the **Site Name** and for **Type** select **Branch**.
4. Set the **Connection Type** to **IPsec IKEv1 (Cato-Initiated)**.
5. Configure the **Country**, **State**, and **Time Zone**.
6. Configure the **Native Range** for the internal LAN to **192.0.2.0/24**.
7. Click **OK**.

The new site is added to the account.
8. To configure the IPsec IKEv1 settings for the primary and secondary connections, click **Site Configuration > IPsec**.
9. In the **General** section, set the **Service Type** to **Generic**.
10. Because this is a new site, select the PoP IP addresses for the tunnels:
  1. Expand the **Primary** section, and click **IP Allocation Settings**.
  2. In the **Configuration** window, select **New York**, **Chicago**, and **London**.

![360002878458-AllocatedIP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275594825885.png)
  3. Click **Submit**.
11. Configure the settings for the primary connection:

![360002795437-IPsecIKEv1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275626940829.png)
  1. Set the **Public IP** settings:
    - **Cato IP (Egress)** - select **New York**
    - Enter the **Primary Destination IP** address as **192.168.3.18**
  2. Do not enter values for **Private IPs**, this site does not use BGP dynamic routing.
  3. Set the **Downstream** bandwidth to **200** and the **Upstream** bandwidth to **100** Mbps.
  4. In **Primary PSK**, and click **Edit Password** enter the pre-shared key for the primary connection.
12. Configure the settings for the secondary connection:
  1. Expand the **Secondary** section.
  2. Set the **Public IP** settings:
    - **Cato IP (Egress)** - select **Chicago**
    - Enter the **Primary Destination IP** address as **192.168.4.20**
  3. Do not enter values for **Private IPs**, this connection does not use BGP dynamic routing.
  4. Set the **Downstream** bandwidth to **200** and the **Upstream** bandwidth to **100** Mbps.
  5. In **Secondary PSK**, and click **Edit Password** enter the pre-shared key for the secondary connection.
13. Expand the **Routing** section, and select **Implicit**. This means that all WAN traffic is transmitted over the IPsec connection in a single Phase II tunnel with one encryption key.
14. Click **Save**. The IPsec IKEv1 connections for the site are configured.
