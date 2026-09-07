---
title: "Customizing the WAN Keepalive Frequency"
slug: "customizing-the-wan-keepalive-frequency"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/customizing-the-wan-keepalive-frequency"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Customizing the WAN Keepalive Frequency

> [!NOTE]
> Note:
> 
> This feature is supported from Socket v12.0 and higher.

## Overview of WAN Keepalive Frequency in Cato

The Socket and the PoP continuously exchange keepalive messages to maintain the tunnel. You can set the frequency of the keepalive messages for each WAN link precedence. For example, if there are two precedence 1 WAN links, the same keepalive frequency is applied to both links. The valid frequency values are 1 - 60 seconds between each message. The default value is 3 seconds. A larger keepalive frequency can help to reduce traffic on cellular LTE/4G links.

After three consecutive unanswered keepalive messages, the Socket considers the link as down.

> [!NOTE]
> Note:
> 
> If you set a large keepalive frequency value, it can cause a slow reaction due to underlying connectivity issues for a site.

## Configuring the WAN Keepalive Frequency

Use the **Keepalive** setting to customize how often the Socket sends keepalive packets to maintain the DTLS tunnel to the PoP. You can set a different keepalive frequency for each link according to the precedence. For example, you can customize only the Last-resort links (precedence 3) to 45 second interval between keepalive messages, and the other links use the default value of 3 second intervals.

You can define this setting as a Global Setting for the entire account, and different **Keepalive** settings for specific sites. The Keepalive for a specific site overrides the account settings.

### Customizing the Keepalive Frequency for the Account

You can customize the keepalive setting that is applied to each site in the account.

**To customize the WAN Keepalive frequency for the account:**

1. From the navigation menu, click **Network > Connection SLA**. The **Connection SLA** screen opens.
2. Expand the **Keepalive** section.
3. For the **Active**, **Passive**, or **Last-resort** link, from the drop-down menu select **Custom**.
4. Enter the number of seconds in between each keepalive packet.

![keepalive.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247992096925.png)
5. Click **Save**.

### Customizing the Keepalive Frequency for a Site

You can customize different keepalive settings for specific sites. The setting for a specific site overrides the account setting.

**To customize the WAN Keepalive frequency for a specific site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Advanced Settings > Connection SLA**.
3. Expand the **Connection SLA** section.
4. Expand the **Keepalive** section.
5. Select **Override account settings**.
6. For the **Active**, **Passive**, or **Last-resort** link, from the drop-down menu select **Custom**.
7. Enter the number of seconds in between each keepalive packet.
8. Click **Save**.
