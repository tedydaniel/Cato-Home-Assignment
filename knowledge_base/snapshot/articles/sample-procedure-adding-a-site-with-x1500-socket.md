---
title: "Sample Procedure - Adding a Site with X1500 Socket"
slug: "sample-procedure-adding-a-site-with-x1500-socket"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/sample-procedure-adding-a-site-with-x1500-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sample Procedure - Adding a Site with X1500 Socket

## Example of Creating a New X1500 Socket Site

This article is a sample procedure that explains how to create a new site with an X1500 Socket. After you configure the settings for the new site, you can then assign the Cato Socket to it.

This sample deployment uses WAN2 for a secondary connection to a different ISP.

**To add a new Socket site to your account:**

1. From the navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![AddSite_X1700.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275610352029.png)
3. Enter the **Site Name** and for **Type** select **Branch**.
4. Set the **Connection Type** to **Socket X1500**.
5. Configure the **Country**, **State**, **Time Zone**, and **City** to set the time frame for the **Maintenance Window** for Socket upgrades.
6. Select **Enable WAN2** to configure a link for the secondary ISP connection.
7. Configure the **WAN1 Bandwidth** and **WAN2 Bandwidth** to 200 Mbps for **Downstream** and 200 Mbps for **Upstream**.
8. Configure the **WAN2 Bandwidth** and **WAN2 Bandwidth** to 100 Mbps for **Downstream** and 100 Mbps for **Upstream**.
9. Configure the **Native Range** for the internal LAN to **192.2.2.0/24**.
10. Click **OK**.

The new site is added to the account.
11. Open the notification area ![notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275603423517.png) (in the upper-right menu bar), and expand the **Activate New Socket** message.

![Activate_Socket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275610498717.png)
12. Click **Accept**. Select the site that the Socket is assigned to.
13. To see the settings for the WAN1 and WAN2 connections, from the navigation menu click **Site Configuration > Socket**.

Below is an example of the **Socket** screen for the X1500 Socket High Availability configuration:

![360002878538-SocketX1500Config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275610565149.png)
