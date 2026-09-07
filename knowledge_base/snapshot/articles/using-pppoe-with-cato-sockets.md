---
title: "Using PPPoE with Cato Sockets"
slug: "using-pppoe-with-cato-sockets"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/using-pppoe-with-cato-sockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using PPPoE with Cato Sockets

## Overview

**PPPoE** is a network protocol used to encapsulate PPP (Point-to-Point Protocol) frames inside Ethernet frames. It combines the PPP that owns the function of authentication and encryption and the Ethernet protocol that can support multiple users in a LAN.

If a site that uses PPoE connections is experiencing connectivity issues, sometimes these issues can be resolved by disabling EEE for the site. To disable EEE for a site, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

If required by your Internet Service Provider, you can define a PPPoE connection for the WAN interface on the Cato Sockets using the procedure below.

![PPPoE_Network-Settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248057618973.png)

## Configuring PPPoE for a WAN Link

Configure PPPoE for your WAN network traffic. When PPPoE is selected, the values in the **Primary DNS** and **Secondary DNS** fields are ignored.

Configure PPPoE from the [Socket WebUI](/v1/docs/accessing-the-socket-webui).

**Configuring PPoE for the WAN link on a Socket:**

1. In the Socket WebUI, navigate to **Network Settings** and click **PPPoE** .
2. Enter the configuration parameters to establish your PPPoE connection. The following fields are mandatory:
  - PPP account (user) name
  - PPP account secret (password)
  - Confirm password
3. The following additional fields are optional and should be configured as instructed by your ISP:
  - Service name
  - Configured IP address
  - Configured primary DNS server address
  - Configured secondary DNS server address
  - Configured MTU
  - Configured VLAN tag
4. Click **Update**.
