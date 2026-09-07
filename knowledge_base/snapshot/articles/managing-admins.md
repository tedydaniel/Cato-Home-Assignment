---
title: "Managing Admins"
slug: "managing-admins"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/managing-admins"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Admins

The Administrators page lets you add and configure admins for the Cato Management Application (CMA) that manages your account. To learn more about Admins, see [What are Admins and Role-Based Access Control (RBAC)](/v1/docs/what-are-admins-and-role-based-access-control-rbac).

You can also create and manage admins using an IdP. For more details, see [Manage Admins with your Identity Provider (IdP).](/v1/docs/manage-admins-with-your-identity-provider-idp)​

![admin_page.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26255642126877.png)

## Adding an Admin

When adding an admin, you define the roles and permissions each admin has, as well as the settings that define password expiration.

**To add an admin:**

1. From the navigation menu, click **Account > Administrators**.
2. Click **New**.

The **Create Administrator** panel opens.
3. Enter these **General** settings for the admin:
  - **First name** and **Last name**
  - **Email** - Admins use this email address as the username when logging in to the CMA
    - **Select an existing admin** - For Cato resellers, you can add an admin that is already configured in the CMA

Select this option and choose the admin from the drop-down list with all the admins in the customer accounts
4. Select the **Role** that will define the permissions for this admin. To learn about roles, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).
5. **(Optional)** To exclude this admin from the password expiration policy, select **Password never expires**. For more information, see [Authenticating Admins](/v1/docs/authenticating-admins).
6. Click **Apply**. The admin is added to the **Administrators** page and an email invitation is sent to the admin with instructions for how to activate the admin.

## Using the Actions Menu

The actions menu lets you perform the following actions on admins:

- Enable
- Disable
- Resend Invitation
- Reset Password
- Reset MFA
- Delete Admin

You can select more than one admin and perform these actions in bulk.

![admin_actions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26255672498205.png)

**To use the action menu:**

1. From the navigation menu, click **Account > Administrators**.
2. Select one or more administrators.
3. Click **Actions** and then from the drop-down menu, select the relevant option.
4. In the confirmation window, click **OK**.
