---
title: "Using an Alternate UDP Port for Socket and Client DTLS Traffic"
slug: "using-an-alternate-udp-port-for-socket-and-client-dtls-traffic"
updated: 2026-07-13T17:09:15Z
published: 2026-07-13T17:09:15Z
canonical: "knowledge.catonetworks.com/using-an-alternate-udp-port-for-socket-and-client-dtls-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using an Alternate UDP Port for Socket and Client DTLS Traffic

This article explains how to configure your account to use an alternate UDP port for DTLS tunnel traffic for Socket sites and Clients.

## Overview

In some locations with restrictive network controls or traffic filtering, such as China, DTLS tunnels using UDP port 443 can experience connectivity issues such as packet loss. Cato lets you configure UDP port 1337 as a preferred DTLS port for Socket and Client traffic to improve connectivity.

By default, DTLS tunnels for Socket site and Client traffic use UDP port 443 as the preferred port, and fall back to port 1337 when connectivity issues are experienced. The System Settings page lets you enable an account-level setting that changes the preferred port for DTLS traffic to UDP port 1337, with port 443 as fallback.

**Note:** This setting applies to traffic for Socket sites and Client users located in China. Traffic for other locations is not impacted.

Cato recommends as a best practice configuring the alternate UDP port for accounts with Socket sites and Client users located in China. For accounts where this is relevant, a posture check is added. For more about posture checks, see [Reviewing Posture Checks for Your Account](/v1/docs/reviewing-posture-checks-for-your-account).

> [!NOTE]
> Notes:
> 
> - When you enable the alternate UDP port setting, the DTLS tunnels for Socket sites reconnect, which may briefly impact connectivity.
> - As of May 11, 2026, new accounts have the system setting for alternate DTLS UDP port enabled by default.

### Prerequisites

- For Socket sites - Socket v26 and higher
- For Client traffic - Windows Client v6.4 and higher

### Known Limitations

- For Client traffic, this feature is supported only for Windows. Clients for other operating systems continue using UDP port 443 as the preferred port.

## Configuring the Alternate DTLS UDP Port

Use the System Settings page to enable the alternate DTLS UDP port setting for the account for remote users and sites connected to PoPs located in China.

**To configure the alternate DTLS UDP Port:**

1. From the navigation menu, click **Resources > System Settings**.
2. In the **Alternative DTLS Port** section, use the toggle to enable the setting.

**Note:** When you enable this setting, the DTLS tunnels for Socket sites reconnect, which may briefly impact connectivity.

![Alternative_DTLS_Port_setting.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35977968149405.png)
3. Click **Save**. The configuration settings are saved.
