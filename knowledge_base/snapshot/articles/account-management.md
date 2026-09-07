---
title: "Configuring the Socket Upgrade Maintenance Window"
slug: "configuring-the-socket-upgrade-maintenance-window"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuring-the-socket-upgrade-maintenance-window"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Socket Upgrade Maintenance Window

This article discusses how to configure the maintenance window for Sockets to upgrade to the newest version.

## Configuring the Maintenance Window for the Account

Cato automatically ensures that your Sockets are up-to-date with the newest Socket software versions which offer support for new features and stability and security improvements. Upgrading a Socket can result in a few minutes of downtime during the upgrade. To help minimize the impact on your account, use the Socket Maintenance Window screen to set a time window for the Socket upgrade.

The account setting for the Socket upgrade maintenance window is applied to the local time zone that is defined for each site (see below). For example, the maintenance window is set to Sunday from 1:00 am - 3:00 am. The Tokyo site upgrades the Socket from 1:00 am - 3:00 am according to the Tokyo time zone, and the London site upgrades the Socket from 1:00 am - 3:00 am according to the London time zone.

To notify customers about upcoming Socket upgrades, there is a 48 hour buffer before the maintenance window. If there are less than 48 hours before the site maintenance window, then the site waits until the following week to initiate the Socket upgrade. For example, the Tokyo site maintenance window is 1:00 am - 3:00 on Sundays. On Friday March 3 at 6:00 pm, Cato releases a new Socket version. Since this is less than 48 hours before the maintenance window, the Tokyo site waits until Sunday March 12 to upgrade the Sockets for the site.

![SocketMaintenanceWindow.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24198361770653.png)

**To set the account maintenance window for Socket upgrades:**

1. From the navigation menu, click **Resources > System Settings**.
2. Select the **Maintenance Window** section.
3. Select the **Day** of the week and the **Time** slot for the Socket upgrades.
4. Click **Save**.

## Changing the Time Zone for a Site

The Time Zone setting for a Socket site determines when the maintenance window is applied to that specific site. You can edit the time zone for a site to make sure that the Socket is upgrading to the new version at the correct time.

The Time Zone setting is configured when the site is created.

**To change the Time Zone for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > General**.
3. Select the **Time Zone** for the site.
4. Click **Save**.
