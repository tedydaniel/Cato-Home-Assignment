---
title: "Setting a Different Port to Connect to the Cato PoP"
slug: "setting-a-different-port-to-connect-to-the-cato-pop"
updated: 2026-07-13T16:59:49Z
published: 2026-07-13T16:59:49Z
canonical: "knowledge.catonetworks.com/setting-a-different-port-to-connect-to-the-cato-pop"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting a Different Port to Connect to the Cato PoP

## Overview

Oftentimes, the Socket can sometimes disconnect, because the government requires ISPs to restrict using UDP port **443**. You can configure the Socket instead to use UDP port **1337**.

## Solution

Set a different port to establish the tunnel with Cato PoPs.

**To change the port for a Socket:**

1. Log in the Socket [WebUI.](/docs/setting-a-different-port-to-connect-to-the-cato-pop#)
2. Browse to the **Cato Connection Settings** tab:

| ![Screen_Shot_2021-11-10_at_10.55.30.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248010633885.png) |
| --- |
3. Under the **DTLS port settings** section, change the port number to 1337 and click **Update**.

![Screen_Shot_2021-11-10_at_10.57.50.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248052048413.png)
4. Click **Reconnect** to apply the changes to the Socket. (You can also restart the Socket.)

The Socket establishes the DTLS tunnel using the 1337 UDP port.

### Setting a Backup Port

Starting with Socket v26.0 and higher, if the Socket has two failed attempts to connect to the PoP, you can specify a backup port number for it to try.

- Primary port 443, backup port 1337
- Primary port 1337, backup port 443

> [!TIP]
> IMPORTANT!
> 
> Only define a backup port for a Socket after receiving instructions from Cato authorized personnel.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/DTLS_backup.png)

**To set a backup port for the Socket:**

1. Select **Use backup port**.
2. Enter **1337** or **443**.
3. Click **Update**.
4. Click **Reconnect** to apply the changes to the Socket. (You can also restart the Socket.)
