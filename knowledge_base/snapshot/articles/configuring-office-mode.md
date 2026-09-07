---
title: "Configuring Office Mode"
slug: "configuring-office-mode"
updated: 2026-07-28T15:42:15Z
published: 2026-07-28T15:42:15Z
canonical: "knowledge.catonetworks.com/configuring-office-mode"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Office Mode

This article explains how to use Office Mode to avoid tunnel-in-tunnel traffic when remote users are located behind a site.

## Overview

Office Mode optimizes Client performance when users with a ZTNA license are physically located in a branch office. It avoids tunnel-within-a-tunnel scenarios by seamlessly routing traffic through the local site instead of the Client's encrypted tunnel. This reduces latency and simplifies traffic routing. You can configure Office Mode globally or allow users to enable or disable it manually in the Client.

Use the Advanced Configuration page to manage Office Mode behavior:

- For all users in the account: go to **Resources > Advanced Configuration**
- For an individual user: go to **User Configuration > Advanced Configuration**

### Prerequisites

- Send HTTPS requests over TCP port 443 to the Cato tunnel API services:
  - `tunnel-api.catonetworks.com`
  - `tunnel-ws-api.catonetworks.com`

## How Office Mode Works

Office Mode first detects whether the device is behind a Socket or IPsec site. If it is, and the configuration allows it, the Client operates in Office Mode and uses the site tunnel to the PoP.

When Office Mode is enabled, and the Client detects a direct connection to a site:

- The Client tunnel is bypassed
- All traffic routes through the site’s tunnel to the PoP
- The site’s security policy is enforced instead of the Client policy

### Office Mode Behavior for Always-On Users

For Client resiliency, there are scenarios where the Client maintains a tunnel to the PoP even in Office Mode. The Client is not sending data over this tunnel.

- macOS Clients always maintain a tunnel using UDP
- Windows Clients with **Require auth in Office** setting enabled always maintain a tunnel using UDP For more about the **Require auth in Office** setting, see this [article](/v1/docs/configuring-the-client-connectivity-policy#h_01KSPRX1HQM4T0QWX3FMA80K0Q).

### What Happens When Office Mode Is Disabled

If the user disables Office Mode while connected to the local site:

- All traffic, including local LAN traffic, is routed through the Client’s encrypted tunnel
- Local traffic is sent to the PoP and then back to the site, increasing latency
- The security policy for the user identity is enforced instead of the site policy

### Automatic Connection Behind a Site (Windows, macOS, and Linux)

Starting in Windows Client v5.10, macOS v5.11 and Linux Client v5.2:

- The Client automatically connects behind a site without requiring user authentication
- The Connect button is disabled while behind the site
- Office Mode is enforced to avoid redundant tunnels

This simplifies the user experience and enforces consistent routing policies. For more information, see [Using Cato Identity Agents for User Awareness](/v1/docs/using-cato-identity-agents-for-user-awareness)

## Using Office Mode with a Private DNS Server

For accounts that use a private DNS server, you must make these configuration changes:

- Add the following DNS entry to the private DNS server to support Client office mode:
  - `vpn.catonetworks.net` as IP address 10.254.254.5 (or the customized reserved service range x.y.z.2 IP address)
  - `tunnel-api.catonetworks.com` as IP address 10.254.254.3 (or the customized reserved service range x.y.z.7 IP address)

**Note:** You must also ensure that your firewall is configured to allow traffic to these addresses for Office Mode to function properly.

For configurations where the private DNS server is located on the local LAN, then the static DNS entry and the connectivity over the local LAN means that the SDP users are always identified as being connected with office mode. Even if the site (and the SDP users in office mode) aren't connected to the Cato Cloud, because the SDP users have connectivity to the private DNS server, they are shown as being connected using office mode.

## Allowing Users to Configure Office Mode

By default, users cannot enable or disable Office Mode. You can configure this behavior globally or override it per user.

- **Status** is **Disabled** (Default global setting) - Office mode is enabled for all users, and they can't configure office mode in their specific Clients.
- **Status** is **Enabled** and **Value** is **On** - All SDP users in the account can choose to enable or disable office mode for their Client.
- **Status** is **Enabled** and **Value** is **Off** - Office mode is enabled for all users, and they can't configure office mode in their specific Clients. This functionality is the same as **Disabled**.

### Global Configuration: Allow Users to Control Office Mode

**To allow all users in an account to control Office Mode:**

1. From the navigation menu, select **Resources > Advanced Configuration**
2. In the Office Mode Configuration section, configure these fields:
  - Status
    - Disabled – Users cannot change Office Mode, and it is enabled (default)
    - Enabled – Users can control Office Mode, based on the Value field
  - Value
    - On – Office Mode is enabled by default, but users can disable it
    - Off – Users can't disable Office Mode

### Per-User Configuration

You can allow individual users to override the global setting.

**To configure Office Mode per user:**

1. From the navigation menu, select **Users** and choose a user.
2. From the user configuration panel, go to **Advanced Configuration**:
3. In the Office Mode Configuration section, configure these fields:

This setting only applies when the user connects behind a site.
  - Status - set to **Enabled**
  - Value
    - On – Office Mode is enabled by default, but users can disable it
    - Off – Office Mode is disabled and users cannot enable it

### Disabling or Enabling Office Mode in the Client

After the configuration is applied, users can change the setting in the Cato Client.

**To enable or disable Office Mode:**

1. Connect the Client to ensure it receives the latest configurationץ
2. If already connected, disconnect and reconnect.
3. Open the **Settings** panel in the Client.
4. Locate the **SDP Office Mode** option.
5. Toggle the checkbox to enable or disable Office Mode.
6. Reconnect the Client to apply the change.

## Known Limitations

- Office mode is only supported with a UDP connection
