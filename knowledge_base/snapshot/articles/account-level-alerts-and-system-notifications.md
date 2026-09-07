---
title: "Account Level Alerts and System Notifications"
slug: "account-level-alerts-and-system-notifications"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/account-level-alerts-and-system-notifications"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Account Level Alerts and System Notifications

This article discusses how to configure the Cato Management Application to send alerts and notifications to Subscription Groups, mailing lists, or integrations for different activities in your account.

## Overview

The Cato Management Application can proactively notify you and send alerts to help detect issues related to your Cato account.

Use the **System Notifications** page to define which types of activities generate alerts and who receives them. By default, all system alerts are enabled and are configured to send alerts to the **All Admins** mailing list (see [Working with Mailing Lists](/v1/docs/working-with-mailing-lists)).

For notifications based on system events, additional details about certain types of events can be viewed in **Monitoring > Events**.

These are the alerts and notifications that you can enable for the account:

- **Expired Signing Certificate:** A signing certificate in your account is expired. These certificates are used for Device Authentication.
- **SCIM Provisioning:** Each hour, the Cato Management Application sends notifications that summarize the SCIM provisioning actions (success or failure).
- **Admin Locked/Unlocked:** An admin account is locked or unlocked. Cato follows PCI guidelines and best practices, and an admin is locked and disabled for 30 minutes after six consecutive failed logins to the Cato Management Application. A different admin can enable the admin and unlock the account (see [Managing Admins](/v1/docs/managing-admins)).
- **User Locked/Unlocked:** A user is locked or unlocked. Cato follows PCI guidelines and best practices, and a user is locked for 30 minutes after six consecutive failed logins to the Cato Client. An admin can enable the user and unlock the account (see [Working with Users](/v1/docs/working-with-users)).
- **License Updated:** A license for the account is expired, updated, or modified.
- **Activate New Socket:** A new Socket is ready to be activated for a site.
- **General Notification:** A special announcement in the Cato Management Application for situations that impact the accounts.

These special Cato announcements are rarely sent.
- **Socket Upgrade:** There is an upcoming maintenance window for a Socket to upgrade to a new version (see [Configuring the Socket Upgrade Maintenance Window](/v1/docs/configuring-the-socket-upgrade-maintenance-window)).
- **DC Connectivity Failure:** Sends a notification if the WMI Controller used for syncing Directory Services for User Awareness failed (see [Configuring the Windows Server for Directory Services](/v1/docs/configuring-the-windows-server-for-directory-services) ).

> [!NOTE]
> Note:
> 
> Cato generates a DC connectivity failure alert once an hour. So it's possible that a single failure alert can indicate many DC connectivity failure events.
- **Directory Services Sync:** Sends a notification when a Directory Services sync event occurs.

You can limit to only send the notification for only certain types of Directory Services Sync events and statuses. The default setting is to only send notifications when a scheduled Directory Services Sync failed.
- **Data Export:** Data is exported from the Cato Management Application, such as a CSV file of all sites in the account.
- **Account Access:** A request from your managing partner to access your account has been submitted or approved.
- **Hardware and Shipping:** After purchasing hardware, reminders are sent if you have not yet provided the [required shipping details](/v1/docs/monitoring-socket-shipping).

![EmailNotifications.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27754174386077.png)

## Configuring System Notifications

By default, all the activities in the **System Notifications** page are enabled to send notifications to all the admins in the Cato Management Application (the **All Admins** mailing list). You can disable notifications or for each activity, choose to send a notification to a different item.

The different items you can choose are:

- **Subscription Group** (for more information on Subscription Groups, see [Creating Subscription Groups](/v1/docs/creating-subscription-groups))
- **Mailing List** (You can click **New** to create a new mailing list, for more information, see [Working with Mailing Lists](/v1/docs/working-with-mailing-lists))
- **Webhook** (For more information, see [Sending CMA Notifications via Webhooks](/v1/docs/sending-cma-notifications-via-webhooks))

For more about the Directory Services Sync notifications, see below [Configuring System Notifications for Directory Services Sync](/v1/docs/account-level-alerts-and-system-notifications#configuring-system-notifications-for-directory-services-sync).

**To configure system notifications:**

1. From the navigation menu, click **Administration > System Notifications**.
2. Click the **Activity** that generates the notification. The **Edit System Notification** panel opens.
3. Use the slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27754222691997.png) to enable (green) or disable (gray) the notification.
4. From the **Sync Type** drop-down menu, select the sync type that generates a notification.
5. From the second drop-down menu, select which **Subscription Group**, **Mailing list** or **Webhook** receives this notification.
6. Click **Apply**. The settings are changed.
7. Click **Save**. The system notifications are configured for your account.

### Configuring System Notifications for Directory Services Sync

You can configure the LDAP Directory Services Sync activity to only send notifications for specific sync types and sync actions.

- Sync Types
  - **Scheduled:** Sends a notification for daily scheduled syncs, verify that in **Directory Services** > **Connection Settings**, the **Daily sync Directory Service Groups and Users (User Awareness)** and/or **Daily synchronize SDP users** options are enabled. By default, these options are enabled in the Cato Management Application.
  - **Sync:** Sends a notification when a sync is manually initiated by clicking **Sync Now** in **Access > Directory Services**.
  - **Any:** Sends a notification when any Sync type is initiated.
- Sync Actions - sends notifications for the following sync results:
  - **Failed:** An error or issue caused the Directory Services sync to fail. You can find more information in **Monitoring > Events**.
  - **Succeeded:** Directory Services successfully completed the sync.
  - **Any:** Any Directory Services sync action.
  - **Succeeded with warning:** Directory Services partially syncs (for example, if there are issues with the first or last name of an SDP user).

**To configure system notifications for Directory Services Sync:**

1. From **Activity**, click **Directory Services Sync**. The **Edit System Notification** panel opens.
2. Use the slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27754222691997.png) to enable (green) or disable (gray) the notification.
3. From the **Sync Type** drop-down menu, select the sync type that generates a notification.
4. From the **Action** drop-down menu, select the action that generates a notification.
5. From the **Sync Type** drop-down menu, select the sync type that generates a notification.
6. From the second drop-down menu, select which **Subscription Group**, **Mailing list** or **Webhook** receives this notification.
7. Click **Apply**. The settings are changed.
8. Click **Save**. The Directory Services Sync notifications are saved.
