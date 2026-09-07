---
title: "SCIM Provisioning with OneLogin"
slug: "scim-provisioning-with-onelogin"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/scim-provisioning-with-onelogin"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Provisioning with OneLogin

This article explains how to use the OneLogin Cato SCIM app to automatically sync users from your OneLogin account to your Cato account.

## Capabilities Supported

Cato Networks delivers a next generation secure networking architecture that eliminates the complexity, costs, and risks associated with legacy IT approaches based on disjointed point solutions. From Single Sign-On (SSO) to user provisioning, OneLogin's Cato integration handles user access and groups throughout the user's lifecycle, including:

- Create and remove users in the Cato Management Application
- Sync users and attributes from OneLogin to the Cato Management Application
- Single Sign-On (SSO) to OneLogin
- Update user attributes
- Deactivate users
- Import users
- Import groups (OneLogin roles)

### Requirements

Make sure that before you create the custom Cato SCIM app, you have admin permissions in OneLogin to configure applications and user provisioning.

### Known Limitations

- Users that are deleted from OneLogin are disabled in the Cato Management Application
- Roles that are deleted from OneLogin, the corresponding groups are NOT deleted in the Cato Management Application
- Nested groups aren't supported
- SCIM sync overrides existing LDAP groups with the same name. For more information, see How SCIM Sync Overrides Existing LDAP Groups

## Configuring the Cato SCIM App to Automatically Sync Users to Cato

You can use the Cato SCIM app in the OneLogin app library, to connect and sync users from your OneLogin account to your Cato account. This section explains how to configure this SCIM app, according to the following workflow:

- In the Cato Management Application, enable SCIM provisioning for your Cato account
- Add the Cato SCIM app to your OneLogin account
- Configure the app to connect to your Cato account
- Define the OneLogin users that are synced
- Define the OneLogin roles that are synced to the groups in your Cato account

The status of users in your Identity Provider (IdP) are automatically synced to your Cato account. For example, when you disable users in the IdP, they are synced to your Cato account as disabled.

### Configuring the Cato Management Application for the SCIM App

In the Cato Management Application, enable SCIM Provisioning and copy the URL and token to a text file. You will enter these settings in the Cato SCIM app that you configure in your OneLogin account.

**To connect** **Cato Management Application** **to the SCIM App**

1. In the Cato Management Application, from the navigation menu select **Access > Directory Services** and click the **SCIM** tab.

![SCIM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218199917469.png)
2. Select **Enable SCIM Provisioning** to set your account to connect to the SCIM app.
3. Click **Save**.
4. Copy and paste the SCIM URL and token to blank text file.
  1. In **Base URL**, click the copy icon ![copy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218199999517.png) to copy the SCIM URL to the clipboard and then paste it in the text file.
  2. In **Bearer Token**, click the copy icon ![copy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218199999517.png) to copy the unique account token to the clipboard and then paste it in the text file.

### Adding the Cato SCIM App

You can add the Cato SCIM application to your OneLogin account, and use it to provision users from your OneLogin account to your Cato account.

To add the Cato SCIM app to your OneLogin account:

**To add the** **Cato** **SCIM app to your OneLogin account:**

1. From your OneLogin admin dashboard, click **Applications > Applications**.
2. Click **Add App**.
3. Search for the **Cato Networks** app, and then click the **Cato Networks** application with **SAML2.0, provisioning**.

![OneLogin_CatoApp.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218224303901.png)
4. In the **App Listing / Add Cato Networks** window, enter the **Display Name** for the application and click **Save**.

![OneLogin_CatoApp_AddApp.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218224381725.png)

The message shows that the application is successfully added to your account.

### Configuring the SCIM App to Connect to Your Account

Configure the settings in the **Configuration** and **Provisioning** sections of the application so that it can connect to your Cato account. You need to enter the URL and Token that you copied from the Cato Management Application in [Configuring the Cato Management Application for the SCIM App](/v1/docs/scim-provisioning-with-onelogin#configuring-the-cato-management-application-for-the-scim-app) above.

**To configure the SCIM application to connect to your** **Cato** **account:**

1. From the application navigation pane, click **Configuration**.
2. In the **API Connection** section, configure OneLogin to integrate with your account:

![OneLogin_CatoApp_Configuration.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218224455965.png)
  1. In **SCIM Base URL**, paste the URL that you copied from the Cato Management Application.
  2. In **SCIM Bearer Token**, paste the token that you copied from the Cato Management Application.
3. In **API Status**, click **Enable**.
4. Click **Save**.
5. From the navigation pane, click **Provisioning**.

![OneLogin_CatoApp_Provisioning.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218213678493.png)
6. Configure these provisioning settings for the application:
  1. Select **Enable provisioning**.
  2. **(Optional)** Configure the **Require admin approval before this action is performed** settings:
  3. In **When users are deleted in OneLogin, or the user's app access is removed, perform the below action**, select **Suspend**.
  4. Make sure that the **Refresh** link in the **Entitlements** section is clickable.
7. Click **Save**.

The Parameters for the Cato SCIM application are configured and the application is ready to connect to your Cato account.

## Syncing VPN Users to Your Cato Account

After the SCIM application can connect to your account, assign the users that you are syncing to Cato. Then you can continue with the next section to add groups to application.

**To provision individual users to your** **Cato** **account:**

1. From top menu, select **Users > Users**.
2. Select the user that you are assigning to the SCIM application.

![OneLogin_SelectUser.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218238784285.png)
3. From the navigation pane for the user, select **Applications**.

![OneLogin_User_Applications.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218238871325.png)
4. Assign the SCIM application to the user:
  1. Click the plus button to add a new application to the user.
  2. In the **Assign new login to** window, from the **Select application** drop-down menu, select the SCIM application.

![OneLogin_User_Applications_AssignApp.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218200549789.png)
  3. Click **Continue**.
  4. In the pop-up window, click **Save**.

![OneLogin_EditAppForUser.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218200628125.png)

The SCIM app is assigned to the user.
5. Click **Save User**. The settings for this user are updated.
6. Repeat steps 4 and 5 above for each user that you are provisioning to your Cato account.

To show the users that are assigned to the SCIM application, go to the SCIM application and from the application navigation pane select **Users**.

## Syncing OneLogin Roles to Your Cato Account

You can assign roles in OneLogin with users that you are syncing to Cato. You can choose to manually add users to this role.

For each role, create a rule that connects the role to the application. Then assign the role to the application and the roles and their associated users are synced to new groups in your Cato account.

**To provision OneLogin roles to you** **Cato** **account:**

1. From top menu, select **Users > Roles**.
2. Select the role that you are assigning to the SCIM application.
3. **(Optional)** Manually assign users to the role:
  1. From the navigation menu in the role, select **Users**.

![OneLogin_Role_AddUser.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218239197469.png)
  2. In **Check existing or add new users to this rule**, enter the username that you're adding to the application.
  3. Click **Check**, the window shows the user.
  4. Click **Add To Role**. The user is added to the **Users Added Manually** section.
4. Create a rule to connect the role to the SCIM application.
  1. From the top menu, click **Applications > Applications** and then open the SCIM application.
  2. From the application navigation pane, select **Rules**.
  3. Click **Add rule**.
  4. In the **New mapping** window, enter a **Name** for the rule.

![OneLogin_App_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218195700381.png)
  5. In the **Actions** section, select **Set Groups in <application name>**. The screenshot above shows the option as **Set Groups in Sample Cato SCIM App**.
  6. From the **For each** drop-down menu, select the role.
  7. Enter the **value that matches** for the name of the role. The screenshot above shows the role name **sample role**.
  8. Click **Save**. The rule is added to the application.

![OneLogin_Rule_Configured.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218239313693.png)
  9. Click **Save**. The rule connecting the role to the application is saved to the application.
5. Assign the SCIM application to the role.

The SCIM application syncs the roles from OneLogin to your Cato account.
  1. From the navigation menu in the role, select **Applications**.
  2. Click the plus button to show the applications in your OneLogin account.
  3. Select the Cato SCIM application and click **Save**. The application is added to the role.

![OneLogin_Role_Add_App.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218225187357.png)

**Removing Users or Groups from the SCIM App**

### Important

**Important:** Do not delete Users or Groups that are provisioned with the SCIM app directly from the Cato Management Application. You must first unassign them in the SCIM app.

When you want to remove users or groups that are provisioned to your Cato account with the SCIM app, unassign them in the app. The users and groups are automatically disabled during the next time the SCIM app syncs with your account.

**To remove users or groups that are synced to your** **Cato** **account:**

1. In the Cato SCIM app, unassign the users or groups.

During the next sync, the SCIM app disables the users or groups in your Cato account.
2. **(Optional)** After the users or groups are disabled, you can delete them from the Cato Management Application.

## Assigning ZTNA Licenses

In the IdP, define the groups and users that are synced to your Cato account. After the initial sync is completed, all users are then created in the Cato Management Application and visible on the **Users Directory** page.

You can then assign ZTNA licenses to users, for more information, see [Assigning ZTNA Licenses to Users](/v1/docs/assigning-ztna-licenses-to-users).

## Understanding Events for SCIM Provisioning

The Cato Management Application generates events whenever users and groups are blocked because they fail to meet the requirements of the Client Connectivity Policy.

Each hour, the Cato Management Application sends email alerts that summarize the SCIM provisioning actions (success or failure).

The following table explains the different events.

| Event Type | Action | Description |
| --- | --- | --- |
| SCIM Provisioning | Success | The action to sync the users or groups to your account with the SCIM app succeeded. |
| SCIM Provisioning | Failure | The SCIM app failed to sync the IdP with your account. The **event message** explains the reason for the sync failure. |
| SCIM Provisioning | Disabled | A disabled user in the IdP was successfully synced and disabled in your Cato account. |
