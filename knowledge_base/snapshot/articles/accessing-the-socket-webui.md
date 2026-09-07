---
title: "Accessing the Socket WebUI"
slug: "accessing-the-socket-webui"
updated: 2026-08-24T08:39:11Z
published: 2026-08-24T08:39:11Z
canonical: "knowledge.catonetworks.com/accessing-the-socket-webui"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Accessing the Socket WebUI

## Overview of the Socket WebUI

The Socket WebUI shows options and information directly related to the Cato Socket. It lets you configure settings and shows data that aren't available in the Cato Management Application.

> [!NOTE]
> **Important!** Making changes in the Socket WebUI can have a significant impact on the network and is primarily intended for experienced Cato admins.

Some of the options and windows in the Socket WebUI are designed for Support and internal use. For example, the **Logging** tab is only for internal data and doesn’t contain customer logs. Use the [Events](/v1/docs/analyzing-events-in-your-network) screen for logs and events related to a specific Socket.

Internet Explorer is end-of-life and isn't supported for using the Socket WebUI, we recommend using a different browser.

### Socket WebUI Password Requirements

- The Socket WebUI password must be at least 8 characters long and include at least one uppercase letter, one number, and one special character.
- The password policy for Cato Sockets is that you must change the password every 90 days. After 90 days, the password expires, and the login window for the Socket WebUI prompts you to authenticate and enter a new password.

## Logging In to the Socket WebUI

There are several ways to log in to the Socket WebUI, centralized access or local access, and for vSocket sites also over the public Internet. With centralized access, you can automatically log in to the Socket WebUI from the Cato Management Application without entering the Socket WebUI password. Your Cato Management Application credentials are used to authenticate to the Socket WebUI.

With local access, you can use the local IP address for the Socket LAN interface to connect to the Socket WebUI. For this option, you must have IP connectivity to the local IP of the Socket, and authenticate with the Socket WebUI credentials.

If necessary, you can assign a public IP address to the MGMT interface of a vSocket to access the Socket WebUI over the public Internet. Cato highly recommends using an inbound security policy to restrict access to specific source IP addresses and HTTPS (TCP/443) only.

### Logging in to the Socket WebUI from the Cato Management Application

Admins with [editor permissions for the specific site](/v1/docs/managing-admin-roles-using-rbac) can automatically log in to the Socket WebUI from the CMA

**To log in to the Socket WebUI from the Cato Management Application:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the socket, select **Socket WebUI**.

The browser opens a new tab and logs in to the Socket WebUI.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248019878301(1).png)

The Socket WebUI automatically logs out when the window is idle for more than 10 minutes.

## Logging in to the Socket WebUI over the Network

Use the credentials for the Socket WebUI to log in from an Internet browser using the Socket IP address.

**To log in to the Socket WebUI from an Internet browser:**

1. (For a single Socket site) Locate the IP address for the Socket LAN interface:
  1. From the navigation menu, select **Network > Sites**, and select the site.
  2. From the navigation menu, click **Site Settings > Networks**.
  3. Locate the row for the **Native** range.
  4. The **Local IP** setting shows the IP address for the Socket WebUI.
2. (For an HA site) Locate the management IP address for the Socket:
  1. From the navigation menu, select **Network > Sites**, and select the site.
  2. From the navigation menu, select **Site Configuration > Socket**.
  3. Expand the **High Availability** section, and locate the Web Management IP settings for the relevant Socket.
3. From an Internet browser, enter the following URL: `https://[your Cato Socket's IP address]`.

For example, https://10.0.0.15
4. Enter the login credentials for the Socket WebUI.

### Logging in to the Socket WebUI Locally for a New or Re-Imaged Socket

For an explanation of how to log in to the Socket WebUI over a local network, for new Sockets or Sockets that were re-imaged and reset to factory default settings, see [Logging in to the Socket WebUI Locally for a New or Re-Imaged Socket](https://auth.catonetworks.com/?backTo=https://%7Bsubdomain%7D.auth.catonetworks.com/zd/authenticate?brand_id%3D1168669%26locale_id%3D1%26return_to%3Dhttps%253A%252F%252Fsupport.catonetworks.com%252Fhc%252Fen-us%252Farticles%252F36331569017117%26timestamp%3D1781772799) (you must be logged in to view this article).

## Changing the Initial Password

After you log in to the Socket for the first time, you must change the password. For the initial login credentials for a Socket, see [Logging in to the Socket WebUI Locally for a New or Re-Imaged Socket](https://auth.catonetworks.com/?backTo=https://%7Bsubdomain%7D.auth.catonetworks.com/zd/authenticate?brand_id%3D1168669%26locale_id%3D1%26return_to%3Dhttps%253A%252F%252Fsupport.catonetworks.com%252Fhc%252Fen-us%252Farticles%252F36331569017117%26timestamp%3D1781772825) (you must be logged in to view this article).

## Showing the Link Status

The **Monitor** tab in the Socket WebUI shows the status for each Socket link.

**To show the status message for a link:**

- Click the link icon.

The window opens and shows more information about the link status.

### Understanding the Link Status Icons

The **Link Status** column has a colored icon that indicates the status of the Socket link. The **Media Status** is for USB links, and indicates if the USB device is plugged or unplugged. This section describes the details of each link status icon.

![webUI_status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248009902877(1).png)

- Green - The link is up and connected to the Cato Cloud
- Orange - The link is up and has an IP address, but can't connect to the Cato Cloud. See below, Troubleshooting a Link Connectivity Issue
- Purple - The link is up, but doesn't have an IP address (for example, a DHCP server didn't assign an IP address to this link)
- Red - The link is down
- Grey - The link is down and the **Media Status** is unplugged

### Troubleshooting a Link Connectivity Issue

When a link status icon is orange, then there is a connectivity issue with that link. The most common issues are:

- The link has Internet connectivity, but there are problems with the DNS server
- The link has no Internet connectivity

The following procedure are suggested steps to help identify the connectivity problem with the specific link. From a host, resolve a DNS query to a popular FQDN. Then use the Socket WebUI to ping that FQDN from the specific Socket link. If the Socket link can't successfully ping the FQDN, then there is probably an issue with the DNS server.

**To troubleshoot a link with an orange status icon:**

1. From a host behind the link, from the CLI complete a DNS lookup of a popular hostname. For example, `dnslookup www.yahoo.com`
  - If there is no response to this command, there is a problem with the Internet connectivity. Please contact your ISP (Internet Service Provider).
2. Log in to the Socket WebUI.
3. From the menu bar, select **Tools**.
4. In **Hostname/IP**, enter an IP address that you received from the DNS lookup command in step 1.
5. From **Route via**, select the link with the orange status icon for direct traffic. For example, **WAN 01 directly**.
6. Click **Ping**.
  - If the ping is successful, then there are no Internet connectivity issues for this link.
  - Otherwise, there is a problem with the Internet connectivity. Please contact your ISP.
7. Change the **Hostname/IP** to the FQDN of the hostname from step 1. For example, [**www.yahoo.com**.](/docs/www.yahoo.com.)
8. Click **Ping**.
  - If the ping is successful, then this link can resolve DNS requests. Please contact Cato Support.
  - Otherwise, the Socket link can't resolve the FQDN using the Socket WebUI Ping tool. Continue with the suggestions below.
9. To investigate DNS resolution for this link:
  1. From a host behind the link, verify that the configured DNS server can resolve the FQDN.
  2. In the Socket WebUI, ping the resolved IP address through the affected link to confirm Internet connectivity.
  3. If the IP ping succeeds but the FQDN ping from the Socket WebUI fails, verify that DNS traffic to Google Public DNS is allowed through the selected Socket link.
  4. Make sure that port 53 isn’t blocked by a firewall or the ISP.
  5. If you need help, or the problem persists, contact Cato Support.
