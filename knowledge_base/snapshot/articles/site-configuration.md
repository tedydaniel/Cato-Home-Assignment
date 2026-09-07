---
title: "Managing Sockets"
slug: "managing-sockets"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/managing-sockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Sockets

## Overview

This article describes these features that help you manage Cato Sockets that are configured for your account:

- Use the Cato Management Application (CMA) Socket page (or Socket WebUI) to manage a Socket from one site, and then reassign it to a different one
- Changing the Socket password from the Socket WebUI
  - Understanding Socket WebUI Certificates
- Using the Socket reset button to:
  - Reset the Socket password
  - Unassign the Socket from the site

## Managing Cato Sockets for a Site

You can use the Socket page to manage your Sockets for a site, and it shows a detailed overview of each Socket's ports and their state. You can also enable and disable ports.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33722594013469.png) |
| --- |

it is possible to assign and unassign Sockets for a site via this page. After you unassign a Socket, it is automatically reset to factory default settings. When you assign a Socket to a site, the Cato Management Application pushes the settings to the Socket and overwrites any manual configurations.

### Unassigning a Socket from a Site

When you unassign a Socket from a site, it is automatically reset to factory default settings and then detected as a new, unassigned Socket. The account receives a notification to activate the Socket.

> [!NOTE]
> Note:
> 
> After you unassign a Socket, we recommend waiting at least 5 minutes before disconnecting or powering off the Socket, or before performing any other action with the Socket. This ensures the unassign and reset processes complete correctly.

**To unassign a Socket from a site:**

1. From the navigation menu, click **Network > Sites**, and select the site with the Socket you are unassigning.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the site you are unassigning, select **Unassign**.

A warning window opens.
4. Click **OK**.

The Socket is unassigned from the site. The account receives a new **Notification** to activate a new Socket.

### Assigning a Socket to a Site

After receiving the Socket and connecting it to the Internet, you can assign the Socket to a site from the CMA **Notifications** panel.

**To assign a socket to a site:**

1. Click the notification icon ![notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33722608604701.png).
2. In the **Notifications** panel, click **Activate New Socket**.

The message shows the serial number (S/N) for each available Socket.
3. Click **Accept**.

The **Assign Socket to a Site** window opens.
4. From the drop-down menu select the site for the Socket.

> [!NOTE]
> Note:
> 
> If **No Results** appears in the window, click **Cancel** and make sure you selected the right Socket type in the **Connection Type** field for the site.
5. Click **Continue**.

The Socket is added to the site.

### Manually Switching a Socket HA Role

In some scenarios, switching the HA roles assigned to your Sockets might be necessary. For example, if your secondary Socket has better throughput than the primary.

> [!NOTE]
> Note:
> 
> Cato recommends manually switching the HA role during a maintenance window or during off-hours as this process will have some minimal downtime.

**To manually switch the HA role:**

1. Unassign the primary Socket using the procedure above. This triggers a switch to the secondary Socket, which becomes the primary.
2. Reassign the Socket to the site. It will now receive the role of secondary Socket.

### Understanding Socket WebUI Certificates

Socket WebUI certificates have a TTL (Time to Live) of 300 days. When a Socket is started, rebooted, or upgraded, Cato checks when the Socket WebUI’s certificate is due to expire. If the certificate is set to expire within 90 days, a new certificate is generated. Meaning, if you have not upgraded or rebooted your Socket in the last 210 days, you will be issued a new certificate.

Therefore if you wish to update the certificate outside of the account upgrade window, reboot the Socket. Take into account that rebooting the Socket will cause some temporary downtime of your network, while the Socket reboots and reconnects to the PoP.

> [!NOTE]
> Note:
> 
> In a HA pair, if you wish to reboot the Sockets, Cato recommends rebooting the Secondary socket first, and then rebooting the Primary. This would mean that on failover to the Secondary, it will be updated with the new certificate, while the Primary updates with the new certificate.

## Unassigning a Socket Using the Socket WebUI

There are some situations where after using the Cato Management Application to unassign a Socket, you can't then assign the same Socket to a different site. For example, if the Socket was disconnected from the Cato Cloud before clicking **Unassign**. In this case, use the Socket WebUI to unassign the Socket and reset the Socket settings, and then you can use the Cato Management Application to assign it to a different site. The Socket remains at the same hardware version.

Only use the Socket WebUI to unassign a Socket after performing the unassign procedure in the Cato Management Application (see above).

Supported from Socket v15 and higher.

**To use the Socket WebUI to unassign a Socket:**

1. Log in to the Socket WebUI locally, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).
2. From the **Administrations** tab, click **Unassign**.

## Changing the Socket Password

You can change the password for the Socket from the Socket WebUI.

The password policy for Cato Sockets is that you must change the password every 90 days. After 90 days, the password expires and the login window for the Socket WebUI prompts you to authenticate and enter a new password. The new password can't be the same as the previous three passwords.

**To change the Socket password from the Socket WebUI:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the socket, select **Socket WebUI**.

The browser opens a new tab and logs in to the Socket WebUI.
4. From the menu bar, select **Administration**.
5. In the **Administrator Password** section, enter the current and new password.
6. Click **Confirm**. The Socket password is changed.

## Resetting the Admin Password and Resetting a Socket

You can use the Socket reset button to perform these actions on the physical Socket:

- Reset the admin password to the factory default password (**admin**), which has no impact on the network traffic
- Reset the Socket to the default settings

After physically resetting a Socket, if you want to re-assign it to a different site, unassign the Socket from the original site (see above [Managing Cato Sockets for a Site](/v1/docs/managing-sockets#managing-cato-sockets-for-a-site)).

You must have physical access to the Socket to perform these reset actions. Make sure to press and hold the reset button for the reset actions, instead of repeatedly pressing the button.

> [!NOTE]
> Note:
> 
> You need to use a paper clip and push the button inside the hole for the relevant Socket model. For more information about identifying the correct Socket model see, [Overview of Reimaging Cato Sockets](/v1/docs/overview-of-reimaging-cato-sockets).

**To reset the admin password on the Socket:**

- X1500 and X1500B Socket models - Press and hold the **F/D** button for about 10 seconds. The password is reset to the default value: **admin**.
- X1600 and X1600 LTE Socket models - Press and hold the **Reset/FD** button for about 10 seconds. The password is reset to the default value: **admin**.
- X1700 Socket models - Press and hold the **FD** button for about 10 seconds. The password is reset to the default value: **admin**.
- X1700B Socket models - Press and hold the **Reset/FD** button for about 10 seconds. The password is reset to the default value: **admin**.

**To reset the Socket to the default settings**

> [!NOTE]
> Note:
> 
> The following should be used only if the Cato tunnel is unavailable and you can't access the Cato Management Application.

- X1500 and X1500B Socket models - Press and hold the reset button for about 30 - 35 seconds. The Socket is reset to the default settings and the configurations are erased. To unassign the Socket from a site, see above [Managing Cato Sockets for a Site](/v1/docs/managing-sockets#managing-cato-sockets-for-a-site).
- X1600 and X1600 LTE Socket models - Press and hold the **Reset/FD** button for about 30 - 35 seconds. The Socket is reset to the default settings and the configurations are erased. To unassign the Socket from a site, see above [Managing Cato Sockets for a Site](/v1/docs/managing-sockets#managing-cato-sockets-for-a-site).
- X1700 Socket models - Press and hold the **FD** button for about 30 - 35 seconds. The Socket is reset to the default settings and the configurations are erased. To unassign the Socket from a site, see above [Managing Cato Sockets for a Site](/v1/docs/managing-sockets#managing-cato-sockets-for-a-site).

Pressing the **Reset** button powers on and off the Socket.
- X1700B Socket models - Press and hold the **Reset/FD** button for about 30 - 35 seconds. The Socket is reset to the default settings and the configurations are erased. To unassign the Socket from a site, see above [Managing Cato Sockets for a Site](/v1/docs/managing-sockets#managing-cato-sockets-for-a-site).

## Using the Traceroute Tool from the Socket

Traceroute is used to identify the routers (hops) between a source and destination. Traceroute works by first sending a packet to the destination IP with a time-to-live (TTL) value of 1. When the packet hits the first router in the path, the router decrements the TTL by 1. Since the new TTL is 0, the router drops the packet and responds with an ICMP time-to-live exceeded message sourced from its own IP address. Traceroute now has the IP address of the first router in the path, so it sends out another packet with the TTL value of 2 (the original TTL incremented by 1), and the second router in the path responds with a TTL exceeded message.

This process is repeated until the traceroute reaches the destination IP address. There is a timer of 60 seconds to complete the traceroute and a maximum of 20 hops.

Choose the Socket link that you are using to run the traceroute and enter the destination hostname or IP address.

These are the types of Socket links that you can run traceroute:

- LAN - The packets are sent using the internal LAN network for the site.
- ALT WAN - The packets are sent using the Alt. WAN tunnel over the MPLS network.
- WAN via Cato - The packets are sent using a tunnel over the Cato Cloud.
- WAN <ISP> directly - The packets are sent using a tunnel over the Internet directly to the ISP. The Cato Cloud is bypassed.

![traceroute_cma.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33722608605725.png)

**To run traceroute from the Socket link:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the socket, select **Network Tools**. Traceroute is automatically selected.
4. Under **Type**, select if the packets are sent through the Cato Cloud or bypass the Cato Cloud.
5. In **Interface**, select the link that is sending the packet.
6. In **Destination** enter the domain or IP address for the traceroute.
7. Click **Apply**.

The window shows the results of the traceroute test.

## Socket Port Statuses

You can view the status for each port in the Socket page for a site. In addition, you can hover over each port to get more detailed information about the status. For example, if a port is showing a status of **Up and Disconnected**, you can hover and see if the problem is that the tunnel is down or an IP address has not been allocated.

In addition, you can hover over the Socket Status to see the Socket's uptime. This can help you understand if a Site Down issue is related to power outages.

For detailed information about the Socket status and port statuses, see [Working with the Site Preview Pane](/v1/docs/working-with-the-site-preview-pane).
