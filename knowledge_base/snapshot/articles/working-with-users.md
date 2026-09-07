---
title: "Working with Users"
slug: "working-with-users"
status: "update"
updated: 2026-09-06T10:21:58Z
published: 2026-09-06T10:21:58Z
canonical: "knowledge.catonetworks.com/working-with-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Users

This article explains how to manage your users and view their connection activity across your account.

## Overview

Efficient user management is a fundamental part of an identity management framework. The **Users** page gives you full visibility of all users and their Clients from a centralized location. You can manually add and manage users and view information about how they are using the Client. The filters let you drill-down into usage activity.

### Use Case

Company ABC manages their Client Upgrade Policy (which defines how Clients in their account are upgraded to the latest version) using **Automatic Silent Upgrades**. Following the release of the latest Windows Client, the IT administrator wants to know how many users have upgraded to this version. On the **Activity Based** tab, the IT administrator adds the latest version to the **Client version** filter. The users who have completed the Client upgrade are displayed.

## Getting Started with the Users Page

The **Activity Based** and **Full** **Directory** tabs display the users in your account and how they are connecting to the Cato Cloud.

### Viewing a Summary of a User

Clicking on a user in either tab opens the **User Quick View** panel, which shows a summary of key information about the user.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(202).png)

### Viewing Users Activity

You can view all the users in your account and their connection activity from the **Activity Based** tab. You can sort and filter for each of the fields to quickly show the relevant data, for example: **Connectivity status**, **Last PoP**, **Client version**, and more. Users only appear after connecting.

> [!NOTE]
> **Note:**
> 
> Users connected behind a Cato Site in Office Mode may appear as Disconnected even though they are identified and protected behind the Cato Site. When [authentication is enforced](https://knowledge.catonetworks.com/docs/protecting-users-with-always-on-security#h_01kr8v3fjgmmmcsvhws87mmp99) for Always-On users in office, the user will appear as Connected.

#### Viewing Device and Client Details

The summary bar provides a high level overview of the total number of users in your account and how they are connecting.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36851990355485.png)

In the Users table, the **Devices** column shows each device and operating system that is used by a user to connect to the Cato Cloud. The **Client version** column shows the version the Client is running. This section can be helpful for security auditing purposes.

If a user connects to the Cato Cloud with more than once device, a plus sign with the number of additional devices is displayed (![Plus_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730870045(1).png) ). To view all the devices used by the user, click on this number.

You can also view additional device information, for example the **Name** and **Identifier** of the device.

![devices.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730884253(1).png)

**To show additional device information:**

1. From the navigation menu, click **Access > Users**.
2. Select a user from the list. The **User Quick View** panel shows device information for the user.
3. For more device information, click **View User** and navigate to **User Monitoring > Devices**. The **Devices** page displays all currently defined devices for the user.

#### Viewing Associated Groups for Users

The **Member of Groups** section shows you the groups that a user belongs to.

![MemberofGroups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730900253(1).png)

**To view associated groups of users**

1. From the navigation menu, click **Access > Users**.
2. Select a user from the list. The **User Quick View** panel shows group information for the user.
3. For more group information, click **View User** and navigate to the **Member of Groups** page**.** The **Member of Groups** window opens, showing the groups that the user belongs to.

### 

#### Viewing Policies Applied to a User

For a clear, centralized view of each user’s policy coverage, you can view all the policy rules that are applied to a user on the **Applied Policies** page. You can view whether the policy is applied to the user directly or from the user’s membership in a group.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(203).png)

**To view the policies applied to a user:**

1. From the navigation menu, click **Access > Users**.
2. Select a user from the list. The **User Quick View** panel is displayed.
3. Click **View User** and navigate to the **Applied Policies** page.

### Understanding the Full Directory

You can view and monitor user provisioning information from the **Full Directory** page. This page displays all the users in your account. You can sort and filter for each of the fields to quickly show the relevant data, for example: Status, Source (SCIM, LDAP, or Manual), Department, and more.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36851990355869.png)

#### Filtering by User Status

The **Status** column displays the account status of the user. The following table provides an explanation of each status.

| Status | Explanation |
| --- | --- |
| Configured | The user has been created in the Cato Management Application. |
| Disabled | The user is disabled. They cannot connect to the Cato Cloud. |
| Locked | The user failed six authentication attempts. |

#### Filtering for Users with a License

The **Remote Access** column identifies users who have a license assigned. You can filter the column to clearly display all users with or without a license. For more information on how to assign a license, see [Assigning ZTNA Licenses to Users](/v1/docs/assigning-ztna-licenses-to-users) .

#### Viewing User Monitoring and Configuration

You can view individual User Monitoring and User Configuration from the **User Quick View** panel, the **Activity Based** page or the **Full Directory** page.

**To view User Monitoring:**

1. From the navigation menu, click **Access > Users**.
2. On the **Activity Based** or **Full Directory** tabs, either:
  - Click on a user and view monitoring data in the **User Quick View** panel
  - On either the **Activity Based** or **Full Directory** tabs, click the bar graph icon (![Bar_Graph.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810717369373(1).png)). The **Access > User Monitoring** page is displayed with a predefined filter for the User.

**To view User Configuration:**

1. From the navigation menu, click **Access > Users**.
2. On either the **Activity Based** or **Full Directory** tabs, click the cog icon (![Cog.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810692981021(1).png)). The **Access > User Configuration** page is displayed with a predefined filter for the user.

## Creating and Managing Users

You can administer new and existing users in your account as part of your identity management framework.

### Adding A User Manually

You can manually add individual users to your account. After a user is created, you can choose to send them an onboarding email to welcome them to remote access at Cato. For more information, see [Adding Users to Your Cato Account](/v1/docs/adding-users-to-your-cato-account).

![AddNewUser.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730981277(1).png)

**To manually add a user:**

1. From the Navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Click **New**. The **Add User** panel opens.
4. Enter the user's **First Name**, **Last Name** and **E-mail**.
5. Click **Apply**.

The user is created and can be viewed on the **Full Directory** page.

### Resetting User Passwords

You can reset the password for a user with an SDP license. After you reset the password, the user receives an email with a link to reset the password. The password reset link is valid for one hour after the email is sent. Before you reset the password for users, make sure that they log out of the Client for all of their devices. Otherwise, the user can be locked out of the Client.

Once a password has been updated, users may have to wait up to 4 minutes before they can sign into the Client again. In Windows Clients on the **Users** page, users must be deleted and re-added before they can sign in with the new password.

Passwords must be between 8 - 32 characters and include at least:

- One number
- One lowercase character
- One uppercase character
- One special character

> [!NOTE]
> Note:
> 
> After you reset the password, users can no longer authenticate with the current password. They must create a new one in the User Portal.

**To reset a user's password:**

1. From the Navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Select the user.
4. From the **Actions** drop-down menu, select **Reset Password**.
5. In the **Reset Password** window, click **Confirm**.

The password is reset for the users and they receive an email with a link to create a new password.

### Resending Activation Emails

After a new user is added to the Cato Management Application , you can choose to send them an activation e-mail. For more information, see [Activating SDP Users for Cato Clients](/v1/docs/activating-users-with-a-registration-code). If needed, the activation email can be resent.

**To resend an invitation to a User:**

1. From the Navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Select the user.
4. From the **Actions** drop-down menu, select **Resend activation email**.
5. In the **Resend Invitation** window, click **Confirm**.

The activation email is sent to the user.

### Deleting and Disabling Users

If you no longer want a user to access your network, depending on how they were created, they can be permanently deleted or disabled. After being deleted users are no longer visible on the **Full Directory** page. Deleted users are still visible in policies and marked as deleted, for example, John Doe (Deleted). After being deleted, the user can no longer connect with the Cato Client or have a policy applied.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36852161429661.png)

- Manually created users can be manually deleted.
- Users provisioned with SCIM can be deleted in the CMA but we recommend deleting them directly from your IdP. After the next sync, they are automatically deleted in the CMA and can no longer connect with the Cato Client.
- Users provisioned with LDAP can be deleted or removed, depending on your [configuration](/v1/docs/implementing-ldap-user-provisioning). After you delete a user from your IdP:

After the next sync, they are automatically deleted in the Cato Management Application and can no longer connect with the Cato Client.
  - If you configure users that no longer exist in your IdP to be disabled, after the next sync, you can manually delete the disabled user.
  - If you configure users that no longer exist in your IdP to be removed, after the next sync, they are automatically deleted.

If a user was recreated after they were deleted, in the Client, remove the existing (deleted) user and sign in again.

> [!NOTE]
> Note:
> 
> You cannot undo the delete user action. Ensure that Always-On is disabled for the user before they are deleted.

**To manually delete a user:**

1. From the navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Select the user.
4. From the **Actions** drop-down menu, select **Delete**.
5. In the **Delete** window, click **Delete**.

The user is deleted.

## Restricting User Access

This section explains how to manage users that are disabled or locked.

### Disabling/Enabling Users

If required, you can temporarily disable user accounts, or enable accounts that have been disabled.

A disabled user cannot connect to the Cato Cloud and is not counted as using a user license. However, they will still appear in its relevant references and entries in the Cato Management Application, such as security rules.

**To disable a user account:**

1. From the Navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Select the user.
4. From the **Actions** drop-down menu, select **Disable**.
5. In the **Disable** window, click **Confirm**.

The user is disabled.

**To enable a user account:**

1. From the Navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Select the user.
4. From the **Actions** drop-down menu, select **Enable**.
5. In the **Enable** window, click **Confirm**.

The user is enabled.

### Unlocking Users

Following security best practices, after six authentication failures within a 5-minute window, Cato automatically locks users for 30 minutes (unless you unlock the user earlier).

These six failures are counted separately for password and MFA authentication failures (meaning the lock will be triggered only after six MFA or six password failures).

You can view where the failure occurred (when the user accessed the [Cato User Portal](https://myvpn.catonetworks.com/login) or when authenticating via the Cato Client, and whether the failure was MFA or password related.

> [!NOTE]
> Note:
> 
> Unlocking a user doesn't reset the user's password.

**To unlock a locked user:**

1. From the Navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Select the user.
4. From the **Actions** drop-down menu, select **Unlock**.
5. In the confirmation window, click **OK**.

The user is unlocked.

### Enabling All Users after an Active Directory Sync

For accounts that use LDAP to synchronize users between Active Directory (AD) and the Cato Cloud, this feature lets you enable all the users that are currently disabled. Sometimes, an admin discovers that many users were disabled by mistake in the AD and then synced to Cato Cloud. When you select this option in the **Users** window, all users that were disabled in the most recent sync are enabled.

**To enable all the disabled users after an LDAP sync:**

1. From the Navigation menu, click **Access > Users**.
2. Click the **Full Directory tab**.
3. Select the user.
4. From the **Actions** drop-down menu, select **Re-enable LDAP Disabled Users**.
5. In the **Re-enable disabled LDAP users** window, click **Confirm**.

The user that was disabled in the most recent LDAP sync is now enabled.

### Revoking a Remote User Session

You can revoke the session of a remote user. After a session is revoked, the remote user is prompted to authenticate in the Client using their configured authentication method. For more information, see [Revoking a Remote User Session](/v1/docs/revoking-a-remote-user-session).

## Viewing User Events

You can view user events that take place across your network. You can choose to view all user events together, or only user events from users connecting either remotely or behind a site. For more information about Events, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network)

- To view events from a specific users, irrespective of where they connect from, filter on the **User Email** or **User Display Name** fields

![Use_Email.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810707178525(1).png)
- To view events from users connecting remotely, filter on the **Sources is Site or SDP User** where the Value is **SDP User**

![Site.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810723684765(1).png)
- To view events from users connecting behind a site, filter on the **Sources is Site or SDP User** where the Value is **Site**

![SDP_user.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810731027869(1).png)

### Version Control

| Date | Description |
| --- | --- |
| September 6, 2026 | Updated with details of the **Applied Policies** page |
