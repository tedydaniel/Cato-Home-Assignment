---
title: "Remotely Pinging the Socket Interface"
slug: "remotely-pinging-the-socket-interface"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/remotely-pinging-the-socket-interface"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remotely Pinging the Socket Interface

You can configure specific sites or the entire account to allow admins to ping the Socket WAN or LAN interfaces from any remote location. To enable this feature on your account, please contact Cato Support.

## Contacting Support to Configure Remote Ping

The remote ping feature is controlled by a configuration in the Cato Cloud. You must give the IP addresses or IP ranges for the ACL to allow those remote locations to ping the WAN or LAN interfaces.

To configure this feature, open a [Support](https://support.catonetworks.com/hc/en-us/requests/new) ticket and give them the following information:

- For the entire account, IP addresses or IP ranges (CIDR format) for the remote ping ACL
- For specific sites, for each site:
  - Name of the site
  - IP addresses or IP ranges (CIDR format) for the remote ping site ACL

If both a site and the account are configured for remote ping, then the settings for the site override the settings for the account.

## Showing the Socket IP Address

Use the **Network Settings** tab in the Socket WebUI to show the IP address for each Socket interface. You can then ping the interface using this IP address. For more information, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

**To show the Socket IP address for a Socket interface:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the socket, select **Socket WebUI**.

The browser opens a new tab and logs in to the Socket WebUI.
4. Click the **Network Settings** tab.

The window shows the public IP address for each interface.

## Pinging the WAN Interface - Public or Private IP Address

When you ping the WAN interface, the options are different depending on whether it has a public or private IP address. You can ping an interface with a public IP address from any remote location over the Internet.

For interfaces with a private IP address, you can ping the interface from another private IP address on the same subnet. You can also configure the router for that site to allow ping requests from remote locations.

### Pinging an Interface with a Public IP Address

When Support [completes the request](/v1/docs/remotely-pinging-the-socket-interface#contacting-support-to-configure-remote-ping) (see above) to enable this feature for your account, WAN interfaces on a Socket with a public IP address allow ping requests over the Internet. Use the Socket WebUI to identify the public IP address for each WAN interface.

### Pinging an Interface with a Private IP Address

By default, WAN interfaces on a Socket with a private IP address only allow ping requests from an IP address on the same subnet. You can't ping the interfaces from remote locations.

For Sockets that are behind a NAT device, some routers support adding the ICMP forwarding rule to allow ping requests to the private IP address for the interface.

Use the Socket WebUI to identify the private IP address for each WAN interface.

## Pinging the LAN Interface

For traffic that originates from the Cato Cloud (WAN traffic), on the Gateway IP address for the site Native Range responds to a ping request. Other ranges (i.e., VLAN, direct Gateway IP) don't respond to pings.
