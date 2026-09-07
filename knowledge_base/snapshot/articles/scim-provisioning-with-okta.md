---
title: "SCIM Provisioning with Okta"
slug: "scim-provisioning-with-okta"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/scim-provisioning-with-okta"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Provisioning with Okta

This article explains how to use the Okta SCIM app to automatically sync users from your Okta account to your Cato account.

## Capabilities Supported

Cato Networks delivers a next generation secure networking architecture that eliminates the complexity, costs, and risks associated with legacy IT approaches based on disjointed point solutions. From Single Sign-On (SSO) to user provisioning, Okta's Cato integration handles user access and groups throughout the user's lifecycle, including:

- Create and remove users in the Cato Management Application
- Sync users and attributes from Okta to the Cato Management Application
- Create users - Import and create users in Okta from the Cato Management Application
- Update user attributes - Sync user attribute changes from the Cato Management Application to Okta
- Deactivate users
- Group push
- Users can authenticate with email or UPN depending on your Okta configuration.

### Requirements

Make sure that before you use the Okta SCIM app, you have admin permissions in Okta to configure user provisioning.

### Known Limitations

- Nested groups provisioning are not supported
- SCIM is supported on accounts that use Email as the User ID only (you can confirm this setting with Cato Support)
- You can provision users with either LDAP or SCIM (not both)
- Removing a user from the IdP application doesn't remove it from the Cato Management Application, it disables the user
- Group Linking isn’t supported
- SCIM sync overrides existing LDAP groups with the same name. For more information, see How SCIM Sync Overrides Existing LDAP Groups

## Configuring Automatic User Sync to Cato

You can use the Cato SCIM app that is available in Okta to connect and sync users from your Okta account to your Cato account. In the Cato Management Application, enable SCIM provisioning for your account.

In your Okta account, add the Cato SCIM app and then configure the settings to connect to your Cato account. Then you can define the Okta groups and users that are synced and Okta immediately initiates the automatic user sync.

The status of users in your Identity Provider (IdP) is automatically synced to your Cato account. For example, when you disable users in the IdP, they are synced to your Cato account as disabled.

> [!NOTE]
> Note:
> 
> If necessary, you can edit the attribute mapping to meet the specific requirements of your organization. See below, [Schema Discovery](/v1/docs/scim-provisioning-with-okta#schema-discovery).

### Configuring the Cato Management Application for the SCIM App

In the Cato Management Application, enable SCIM Provisioning and copy the URL and token to a text file. You will enter these settings in the Cato SCIM app that you configure in your Okta account.

**To connect** **Cato Management Application** **to the SCIM App:**

1. In the Cato Management Application, from the navigation menu select **Access > Directory Services** and click the **SCIM** tab.

![SCIM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810717071133.png)
2. Select **Enable SCIM Provisioning** to set your account to connect to the SCIM app.
3. Click **Save**.
4. Copy and paste the SCIM URL and token to blank text file.
  1. In **Base URL**, click the copy icon ![copy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810723377309.png) to copy the SCIM URL to the clipboard and then paste it in the text file.
  2. In **Bearer Token**, click the copy icon ![copy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810723377309.png) to copy the unique account token to the clipboard and then paste it in the text file.

### Adding the Cato SCIM App in Okta

Add the Cato SCIM app from the Okta app store and then set the app to automatically sync users to Cato. Enter the SCIM Provisioning URL and token that you copied from the Cato Management Application.

**To create the** **Cato** **SCIM app:**

1. Log in to your Okta account and go to the admin console.
2. From the menu bar, click **Applications > Applications**.

![SCIM_Okta_AddApp.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730773277.png)
3. Add the Cato SCIM app to your Okta account:
  1. Click **Add Application**.
  2. Search for the Cato**Networks Provisioning** and select the app. The app overview opens in a new window.
  3. Click **Add**. The **Add Cato Networks Provisioning** wizard opens.

![Okta_GeneralSettings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810723458333.png)
  4. Enter the **Application label** and configure the app settings.
  5. Click **Next**.
  6. Configure the settings for user authentication and credentials.

![Okta_SSO_SWA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810701070365.png)
  7. Make sure that **Update application username** on is set to **Create and update**.
  8. Click **Done**. The Cato SCIM app is added to your account.
4. Click the **Provisioning** tab, and the **Integration** window opens.
5. Click **Configure API Integration**.
6. Select **Enable API Integration**.

![SCIM_Okta_Integratoin.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730827037.png)
7. Configure Okta to integrate with your Cato account:
  1. In **Base URL**, paste the URL that you copied from the Cato Management Application.
  2. In **API Token**, paste the token that you copied from the Cato Management Application.
8. Click **Test API Credentials** to make sure that the Cato SCIM app can connect to your Cato account.
9. Click **Save**.

#### Configuring the SCIM App for Provisioning

Configure the settings in the SCIM app to provision users to your Cato account. For more about the SCIM attributes, see below [Schema Discovery](/v1/docs/scim-provisioning-with-okta#schema-discovery).

**To configure the SCIM app to provision users:**

1. In the new SCIM app, click the **Provisioning** tab.
2. From the **Settings** section, select **To App**.
3. Configure the **Provisioning to App** settings, click **Edit**.
4. Select **Enable** for these options:
  - Create Users
  - Update User Attributes
  - Deactivate Users
5. Click **Save**.

### Updating the Cato SCIM App for Okta

From time-to-time, Cato adds attributes to its SCIM schema that provide you with more granular information about your users. To have access to these attributes in the CMA, you need to update the Cato app in Okta with the new attributes, and configure which attributes are included when creating and updating users in the CMA.

**To update the Cato SCIM app:**

1. Navigate to **Okta Admin Console > Applications > Cato Networks SCIM Application > Profile Editor > App User Profile**.
2. Click **Add Attribute**.
3. Define the attributes you want to add as follows:

When the **Required** field value is No, the field is optional in the CMA

| Attribute Name (Cato SCIM) | Okta External Name | Data Type | Required | Multi-Value | SCIM Schema/Namespace |
| --- | --- | --- | --- | --- | --- |
| title | title | String | No | No | urn:ietf:params:scim:schemas:core:2.0:User |
| department | department | String | No | No | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User |
4. Navigate to **Okta Admin Console > Applications > Cato Networks SCIM Application > Provisioning > To App**.
5. Under **App User Attributes**, enable the **Create** and **Update** options for each attribute that is sent to the CMA when the SCIM app processes a create or update request.
6. Click **Save**.

### Syncing VPN Users to Your Cato Account

After the SCIM app can connect to your account, assign the users that you are syncing to Cato. Then you can continue with the next section to add groups to app.

**To provision individual users to your** **Cato** **account:**

1. In the Cato SCIM app, click the **Assignments** tab.

![SCIM_Okta_Assign.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810723501597.png)
2. Assign the people and groups that you are adding to the SCIM app to sync to your Cato account:

The users are synced from Okta to your Cato account.
  1. Click **Assign** and select **People**.
  2. For the person, click **Assign**.
  3. Click **Save and Go Back**.
  4. Repeat the previous steps for all the people or groups, and then click **Done**.

### Syncing Okta Groups to Your Cato Account

You can assign groups in Okta with users that you are syncing to Cato. Then create or assign the Okta Push Groups to the SCIM app and the app syncs the groups and the associated users to your Cato account.

> [!NOTE]
> Note:
> 
> Users must be members of the pushed group and assigned to the Okta Cato OIN application for their group membership to populate correctly within the app.

**To provision Okta groups to you** **Cato** **account:**

1. Assign the groups that you are adding to the SCIM app to sync to your Cato account:
  1. In the **Assignments** section, click **Assign** and select **Groups**.
  2. For the group, click **Assign**.
  3. Click **Save and Go Back**.
  4. Repeat the previous steps for all the groups, and then click **Done**.
2. Go to the **Push Groups** section.
3. Select **Push Groups > Find groups by name**.
4. Enter the name for the Okta Push Group and select the group.

![SCIM_Okta_PushGroup.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730856221.png)
5. If you need to add more Push Groups, click **Save & Add Another**, otherwise click **Save**. The app syncs the groups and associated users to your Cato account.

## Assigning SDP Licenses

In the IdP, define the groups and users that are synced to your Cato account. After the initial sync is completed, all users are then created in the Cato Management Application and visible on the **Users Directory** page .

You can then assign SDP licenses to users, for more information, see [Assigning ZTNA Licenses to Users](/v1/docs/assigning-ztna-licenses-to-users).

**Removing Users or User Groups from the SCIM App**

> [!NOTE]
> Important:
> 
> Although users can be deleted within the CMA, we recommend you delete users or user groups that are provisioned with the SCIM app directly from the Cato Management Application.

When you want to remove users or user groups that are provisioned to your Cato account with the SCIM app, unassign them in the app. The users and user groups are automatically disabled the next time the SCIM app syncs with your account.

**To remove users or user groups that are synced to your** **Cato** **account:**

1. In the Cato SCIM app, unassign the users or user groups.

During the next sync, the SCIM app disables the users or user groups in your Cato account.
2. **(Optional)** After the users or groups are disabled, you can delete them from the Cato Management Application.

It can take up to 15 minutes before you can manually delete users or user groups.

Users that are deleted in the CMA and not your SCIM app, are permanently deleted.

## Schema Discovery

You can use the **Attribute Mappings** in the **Provisioning** tab of the app to configure the SCIM attributes. The **Apply on** setting for the attributes is **Create and update**.

| Attribute | Cato VPN User Attribute |
| --- | --- |
| Username userName | Configure the **email** option in the **Sign On** settings for the Okta app |
| Given name givenName | user.firstName |
| Family name familyName | user.lastName |
| Primary email email | user.email |
| Display name displayName | user.displayName |
| Primary phone primaryPhone | Attribute type - **expression** (user.primaryPhone != null && user.primaryPhone != '') ? user.primaryPhone : '' |
| Primary phone type primaryPhonetype | Attribute type - **expression** (user.primaryPhone != null && user.primaryPhone != '') ? 'work' : '' |
| Job title title | user.title |
| Department department | user.department |

## Understanding Events for SCIM Provisioning

The Cato Management Application generates events whenever users and groups are blocked because they fail to meet the requirements of the Client Connectivity Policy.

Each hour, the Cato Management Application sends email alerts that summarize the SCIM provisioning actions (success or failure).

The following table explains the different events.

| Event Type | Action | Description |
| --- | --- | --- |
| SCIM Provisioning | Success | The action to sync the users or groups to your account with the SCIM app succeeded. |
| SCIM Provisioning | Failure | The SCIM app failed to sync the IdP with your account. The **event message** explains the reason for the sync failure. |
| SCIM Provisioning | Disabled | A disabled user in the IdP was successfully synced and disabled in your Cato account. |

## Deleting an Active SCIM Directory

You can remove a SCIM directory from your account. After you delete a directory, changes to its users and groups are no longer synced. You can delete a directory even if it still has active users. After deletion, those users are no longer associated with the directory.

**To delete an active SCIM directory:**

1. Navigate to **Access > Directory Services**.
2. In the **SCIM** tab, click on the three dots of the directory you want to delete.
3. Click **Delete**.
4. In the confirmation pop up, click **Delete**.
