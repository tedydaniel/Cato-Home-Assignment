---
title: "Defining a Preferred PoP for a Site"
slug: "defining-a-preferred-pop-for-a-site"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/defining-a-preferred-pop-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining a Preferred PoP for a Site

This article explains how to designate specific PoP locations that a site prefers to connect to.

## Overview of Preferred PoP Location

The Cato Cloud uses a connectivity algorithm to determine which PoP location a site connects to. The goal of this algorithm is to maximize network speed and the end-user experience.

There are a number of situations where you may want to prioritize specific geographic locations for a Socket site. For example, if there are a number branch offices near the same PoP, then you might want all these sites to connect to it. The Preferred PoP location feature lets you assign a primary and secondary PoP for a Socket site. The connectivity algorithm then includes this priority and increases the likelihood that the site is connected to the primary or secondary PoP location. The greatest priority is for the primary PoP, and then a lower priority is assigned to the secondary PoP.

## Defining the Preferred PoP Location

The **General** section for a Socket site lets you define the primary and secondary (optional) PoP locations for each site.

As a best practice, we recommend that you use the default **Automatic** option while also defining the **City** for the site. The **Automatic** option means that there is no preferred PoP location for this site, and the site always connects to the PoP location with the best connection quality. Defining the city helps ensure that when a site is near a PoP location containing multiple PoP instances, it connects with the best connection quality even among the PoP instances in the same location. For example, there are 4 PoP instances in Tokyo, and you define the site city as Tokyo. When the site uses the Tokyo location it will be connected to the best available connection among the Tokyo instances.

You can also choose to restrict a site to only connect to the Preferred PoP Locations that you configure for the site. In this case, the site doesn't connect to a non-preferred PoP location despite any connectivity or performance issues that the site is experiencing. When you use this option, you must define a primary and secondary PoP location for the site.

**To define the preferred PoP location for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > General**.
3. Expand the **Preferred PoP Location** section.
4. In the **Primary** drop-down menu, select the PoP location that is the primary preferred PoP location for this site.
5. In the **Secondary** drop-down menu, select the PoP location that is the secondary preferred PoP location for this site.

Select **None** if you aren't defining a secondary PoP location.
6. **(Optional)** Select **Only connect to the Preferred PoP Locations** to restrict the Socket from connecting to a non-Preferred PoP location.

This option lets you force the Sockets for this site to only connect to PoP locations in a specific country or geographical region. The **Secondary** PoP location must be defined as a PoP or **Automatic** when you select this option.
7. Click **Save**. The preferred PoP locations are defined for the site.

### PoP Locations in China

When connecting to Cato from within China, you can only connect to PoPs in China. Locations outside of China cannot connect directly to Chinese PoPs.

For PoP locations in China, some locations have multiple PoPs that a site can connect to. For example, Shanghai_DC1 and Shanghai_DC3. For more about optimal PoP selection in China, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

## Reconnecting to the Preferred PoP Location

If the Socket connects to a different PoP in the Cato Cloud, which isn't a preferred PoP location, this is how the Socket reconnects to the preferred PoP location:

- Automatic - the Socket waits for a defined time period before it reconnects to a preferred PoP location.
  - By default, the Socket waits 60 minutes and then reconnects to a Preferred PoP location.
  - You can customize the **Reconnect to Preferred PoP** settings and change the time period that the Socket waits before it reconnects to a Preferred PoP location.
  - You can also disable the **Reconnect to Preferred PoP** feature and configure the Socket to stay at its current PoP location instead of reconnecting to its Preferred PoP location.
- Manual - From the **Network > Sites** screen, in the **Actions** drop-down menu.

### Configuring the Reconnect to Preferred PoP Settings

You can customize how long the Socket waits before it automatically reconnects to the Preferred PoP location.

You can define this setting as a Global Setting for the entire account, and different Reconnect to Preferred PoP settings for specific sites. The Reconnect to Preferred PoP for a specific site overrides the account settings.

#### Customizing the Reconnect to Preferred PoP for the Account

You can customize the Reconnect to Preferred PoP setting that is applied to each site in the account.

**To customize the account setting for reconnecting a** **Socket** **to a Preferred PoP Location:**

1. From the navigation menu, click **Network > Connection SLA**. The Connection SLA screen opens.
2. Expand the **Reconnect to Preferred PoP** section.
3. Define the behavior for reconnecting to a Preferred PoP location:

The following screenshot shows a setting for the entire account that waits 60 minutes before automatically reconnecting to a Preferred PoP location.

![preferredpop.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248002280861.png)
  1. To automatically reconnect to a Preferred PoP location, in **After**, enter how many minutes the Socket waits before it reconnects.
  2. To disable automatically reconnecting to a Preferred PoP location, select **Disabled**.
4. Click **Save**.

#### Customizing the Reconnect to Preferred PoP for a Site

You can customize a different Reconnect to Preferred PoP setting for specific sites. The setting for a specific site overrides the account setting.

**To customize reconnecting a** **Socket** **to a Preferred PoP Location setting for a specific site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Connection SLA**.
3. Expand the **Reconnect to Preferred PoP** section.

![preferredpopSITE.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247991848733.png)
4. Select **Override account settings**.
5. Define the behavior for reconnecting to a Preferred PoP location:
  1. To automatically reconnect to a Preferred PoP location, in **After**, enter how many minutes the Socket waits before it reconnects.
  2. To disable automatically reconnecting to a Preferred PoP location, select **Disabled**.
6. Click **Save**.

### Manually Reconnecting to a Preferred PoP Location

Use the **Reconnect to Preferred PoP** option in the **Sites** page for a site to manually connect the Socket to a Preferred PoP location.

After you click the **Reconnect to Preferred PoP** option, it takes a few seconds to establish a new DTLS tunnel to the Preferred PoP location. We recommend that you perform this action during a maintenance window to avoid a possible service impact during working hours.

If the Socket is already connected to a Preferred PoP location, then the Socket ignores this action.

**To manually reconnect a site to a Preferred PoP location:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the **Actions** drop-down menu, select **Reconnect to Preferred PoP**.
3. In the confirmation window, click **Reconnect**.
