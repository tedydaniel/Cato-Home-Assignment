---
title: "Configuring a Last-Resort Link"
slug: "configuring-a-last-resort-link"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/configuring-a-last-resort-link"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a Last-Resort Link

This article explains how to configure a backup cellular link (such as 4G/LTE) as a Last-resort link.

## Overview of Last-Resort Links

For Sockets that are connected to multiple WAN links, you can designate one or more backup links as passive or Last-resort. Cato has two options for backup links, precedence 2 (passive) and precedence 3 (Last-resort links). Precedence 2 links are primarily used for wired links, whereas precedence 3 links are designed primarily for wireless (4G/LTE) links. **Note:** Off-Cloud traffic is not supported for WAN links that are configured as a last-resort link.​

**When does a Socket activate a Last-resort link?**

The Socket activates the passive/Last-resort links in the following scenarios:

1. All active and passive links are down.
2. All active and passive links fail to meet the connectivity SLA thresholds.

For more information, see [Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites).

**What are the special characteristics of a Last-resort link?**

- Bandwidth utilization - The Socket only sends a minimal amount of Cato system traffic over the Last-Resort links to reduce usage and expense of the 4G/LTE links

The actual bandwidth usage depends on multiple factors, including routing table size, number of site-to-site channels, account size, configuration changes and so on.
- Grace Timer (Optional) - The Socket waits a set period of time to allow its self-healing mechanisms to fix connectivity issues on active (precedence 1) links, before it activates the Last-Resort link

**How does the Grace Timer Work?**

When a link is set as a Last-Resort link (precedence 3), you have the option to customize the Grace Timer for this link. The default value for the Grace Timer is 0 seconds, which means that the Socket doesn't wait any time before activating the Last-Resort link.

If you customize the Grace Timer, the Socket waits to repair connectivity on the active links. During this waiting time, the site may experience connectivity issues (or no connectivity) before the Socket activates the Last-Resort link.

Once the Last-Resort link is activated, it starts to send and receive traffic for the site.

**How long does the Last-Resort link remain active?**

The Socket deactivates the Last-Resort link when a precedence 1 or precedence 2 link meets the connectivity SLA thresholds for a continuous time period of 10 minutes. If during this 10 minute time period, the higher precedence link experiences connectivity SLA issues again, then the deactivation timer of 10 minutes is reset.

### Customizing WAN Keepalive Frequency for Last-Resort Link

You can also configure a different WAN keepalive frequency for the Last-Resort links. A larger keepalive frequency can also help to reduce traffic on these links. For more about configuring the Keepalive settings, see [Customizing the WAN Keepalive Frequency](/v1/docs/customizing-the-wan-keepalive-frequency).

## Configuring a Last-Resort (Cellular) Link

For each site with a cellular backup link, you can define it as a Last-resort link. You can also configure the Grace Timer setting to create a waiting period before the Socket activates the Last-resort link for a site.

### Defining the Last-Resort Link for a Site

In the **Socket** section for the site, define the cellular (4G/LTE) backup link as the Last-resort link with precedence 3.

The following screenshot shows port 3 defined as the Last-resort link for an X1700 Socket:

**To define the** **Last-resort** **link for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click on the **Port** to be edited or configured. The **Edit Socket Interface** panel opens.
4. In the **Socket** section, set the **Precedence** to **3 (Last-resort)**.
5. Click **Apply**.

### Customizing the Grace Timer

The Connection SLA **Grace Timer** setting lets you define a waiting period before the Socket activates the Last-resort link.

> [!NOTE]
> Note:
> 
> When you configure a Grace Timer that is greater than the default value of 0 seconds, the site can lose connectivity during the waiting period.

You can define the Grace Timer setting for the entire account, and a different Grace Timer setting for specific sites. The Grace Timer for a specific site overrides the account settings.

#### Configuring the Grace Timer for the Account

Configure the Grace Timer setting that is applied to the Last-resort links for each site in the account.

**To configure the account setting for the Grace Timer for the** **Last-resort** **link:**

1. From the navigation menu, click **Network > Connection SLA**. The **Connection SLA** screen opens.
2. Expand the **Last Resort Link** section.
3. In the **Grace Timer** section, enter the number of seconds that the Socket waits before activating the Last-resort link.

The following screenshot shows a Grace Timer that is set to 120 seconds.

![last-resort.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247991925021.png)
4. Click **Save**.

#### Configuring the Grace Timer for a Site

You can configure a different Grace Timer setting for specific sites. The setting for a specific site overrides the account setting.

**To define the Grace Timer settings for a specific site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Advanced Settings > Connection SLA**.
3. Expand the **Connection SLA** section.
4. Expand the **Last-Resort Link** section.

![siteLastResortoverride.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248002525597.png)
5. Select **Override account settings**.
6. In the **Grace Timer** section, enter the number of seconds that the Socket (for this site) waits before it activates the Last-resort link.
7. Click **Save**.

## Best Practices for Configuring Cellular Links for a Site

This section describes the recommended settings to configure a cellular link as a Last-Resort link in the Cato Management Application. The goal of this configuration is to minimize the amount of traffic that is sent over this link, when it is passive or when the Socket activates it.

The specific requirements of your site or network may require a different configuration. Only the first step is required, the other steps are suggestions to minimize traffic over the cellular link.

1. **Mandatory:** In the **Network > Sites > {Site Name} > Site Configuration > Socket** page, edit the Socket **WAN Precedence** for this link as **3 (Last-Resort)**.
2. In the same location, make sure that **Off-Cloud Traffic** is disabled for this link.
3. If **Last Mile-Monitoring** is enabled for this site, in the **Last Mile-Monitoring** section for the site, exclude this link from the monitoring.
4. Configure the **Grace Timer** for the site.
  - The Grace Timer delays the activation of the Last-Resort link and lets the Socket try to remedy the connectivity issue with the primary active link. If the issue isn't resolved during the Grace Time period, then the Socket activates the Last-Resort link. It is possible that the site loses connectivity during the Grace Time period.
  - The default setting for the Grace Timer is 0 seconds, then the Socket can immediately activate the Last-Resort link.
5. In the **Connection SLA** settings for the site, increase the keepalive settings for the **Last-Resort** link.
