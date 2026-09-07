---
title: "SCIM Provisioning with Entra ID (formerly Azure)"
slug: "scim-provisioning-with-entra-id-formerly-azure"
updated: 2026-09-01T15:38:58Z
published: 2026-09-01T15:38:58Z
canonical: "knowledge.catonetworks.com/scim-provisioning-with-entra-id-formerly-azure"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Provisioning with Entra ID (formerly Azure)

This article explains how to use the Azure SCIM app to automatically sync user and group information, and provision users and groups from Entra ID to your Cato account.

## Capabilities Supported

- Create and disable users in the Cato Management Application
- Synchronize users and attributes from Azure AD to the Cato Management Application
- Single Sign-On (SSO) to Azure
- Users can authenticate with email or UPN, depending on your Azure configuration.

## Prerequisites

Make sure that these items are ready before you create the Azure SCIM app:

- An Entra ID tenant
- Entra ID permissions to configure user provisioning

## Limitations

- Removing a user from the IdP application disables the user in the Cato Management Application (see below [Removing Users or User Groups from the SCIM App](/v1/docs/scim-provisioning-with-entra-id-formerly-azure#removing-users-or-user-groups-from-the-scim-app))
- For accounts that use LDAP sync for users, when you enable SCIM provisioning, this sync is disabled for your account.
  - LDAP sync for User Awareness continues to work regularly and isn't impacted by SCIM provisioning.
- Nested groups provisioning are not supported
- SCIM sync overrides existing LDAP groups with the same name. For more information, see How SCIM Sync Overrides Existing LDAP Groups
- SCIM provisioned users are not identified with WMI-based User Awareness. User Awareness with SCIM is supported using Cato [Identity Agent](/v1/docs/using-cato-identity-agents-for-user-awareness)
- On demand provisioning does not support assigning users to a user group

## Planning the User Sync

This section describes how to plan Entra ID to sync users with your Cato account. For more about planning the user sync between Azure and Cato, see these Microsoft articles:

- [What is automated SaaS app user provisioning in Azure AD?](https://docs.microsoft.com/en-us/azure/active-directory/app-provisioning/user-provisioning)
- [Attribute-based application provisioning with scoping filters](https://docs.microsoft.com/en-us/azure/active-directory/app-provisioning/define-conditional-rules-for-provisioning-user-accounts)
- [Tutorial - Customize user provisioning attribute-mappings for SaaS applications in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/app-provisioning/customize-application-attributes)

### Defining Users and Groups for the User Sync

Entra ID lets you define the users that are included in the user sync with Cato according to one of these methods:

- Assigning users to the Entra ID app
- Filtering users based on the attributes for [users or groups](https://docs.microsoft.com/en-us/azure/active-directory/app-provisioning/define-conditional-rules-for-provisioning-user-accounts)

As part of the process to plan the user sync with Cato, we recommend that you start with a small group of users. Depending on the method above, you can:

- Assign a few users to the Entra ID app
- Create an attribute-based scoping filter that only matches a few users

## Configuring Automatic User Sync to Cato with the Cato SCIM App

You can connect Entra ID to your Cato account and sync users between them. Add the Cato SCIM app in the Azure gallery to your account and then configure the settings to connect to your Cato account. Azure initiates the automatic user sync every 40 minutes.

Then you can define the Entra ID groups and users that are synced and enable automatic provisioning.

The status of users in your Identity Provider (IdP) is automatically synced to your Cato account. For example, when you disable users in the IdP, they are synced to your Cato account as disabled.

**Note:** When considering the total number of users in a SCIM group in Azure compared to the CMA SCIM group, note that you will have fewer users in the CMA SCIM group. This is because we do not account for disabled users, who have either been synced over and were later disabled or have always been disabled.

### Configuring the Cato SCIM App

Configure the settings for the Cato SCIM app from the Azure gallery and then set the app to automatically sync users to Cato.

In the Cato Management Application, enable SCIM Provisioning and copy the URL and token to the Admin Credentials section in the Cato SCIM app.

To add new attributes to your existing app, [update the SCIM app](/v1/docs/scim-provisioning-with-entra-id-formerly-azure#h_01KTGM1RRW5P2CEFX66TSNG0Z8).

**To connect Cato Management Application to the SCIM app:**

1. From the [Azure portal](https://portal.azure.com/), go to **Enterprise Applications**.
2. Go to **New application**, search for the Cato Networks Provisioning app, and click **Create**.
3. In the Cato Management Application, from the navigation menu select **Access > Directory Services** and click the **SCIM** tab.

![SCIM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982319478557.png)
4. Select **Enable SCIM Provisioning** to set your account to connect to the SCIM app.
5. Click **Save**.
6. Copy and paste the SCIM URL and token to blank text file.
  1. In **Base URL**, click the copy icon to copy the SCIM URL to the clipboard and then paste it in the text file.
  2. In **Bearer Token**, click the copy icon to copy the unique account token to the clipboard and then paste it in the text file.
7. In Azure, go to the **Provisioning** section for the SCIM app, and paste the SCIM URL and token.
  1. Paste the URL in **Tenant URL**.
  2. Paste the token in **Secret Token**.
  3. Click **Save**.
8. In Azure, click **Test Connection** to make sure that Azure AD can connect to the Cato SCIM app.
9. Enable automatic provisioning in the app.
  1. From the navigation menu, select **Provisioning**.
  2. In the **Provisioning** screen, click **Get started**.
  3. From the **Provisioning Mode** drop-down menu, select **Automatic**.
  4. Click **Save**.
10. Assign groups and users to the app.

### Provisioning Users to Your Cato Account

After the Cato SCIM app can connect to your account, enable automatic provisioning and select the users and groups that are synced.

**To provision users to your Cato account:**

1. In the Cato SCIM app, go to the **Provisioning** section.
2. In **Provisioning Status**, click **Start provisioning**.

![Azure_StartProvisioning.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982275273757.png)

The initial synchronization between your Azure AD and Cato account starts.

## Updating an Existing SCIM App

Use the following steps to update the attribute list and attribute mappings for an existing Microsoft Entra ID SCIM application so that additional user attributes are provisioned to Cato. This is required to get access to the latest attributes used by Cato, for example Job Title and Department.

> [!NOTE]
> Note:
> 
> If the SCIM application was created before November 2025, you must [create a new SCIM application](/v1/docs/scim-provisioning-with-entra-id-formerly-azure#h_01KTGM1RRW15KSP25MDT06NWA0) and configure the attributes as described below.

**Update an existing SCIM app:**

1. From the [Azure portal](https://portal.azure.com/), go to **Enterprise applications > All applications** and select your Cato SCIM app.
2. Click **Provisioning** and then **Attribute mapping**.
3. In the Attribute Mapping page, select the **Show advanced options** checkbox and click **Edit attribute list for <appName>**.
4. Add the attribute and from the **Type** dropdown select the relevant value.

Repeat this process for each attribute you want to add.
5. Click **Save**.
6. In the Attribute mapping page, click **Edit attribute**.
7. In the Edit Attribute page, select the **Source attribute** and map it to the **Target attribute**.

For example, select jobTitle as the source, and map it to title in the target.

Repeat this process for each attribute you're adding.
8. Click **Save**.
9. [Provision](/v1/docs/scim-provisioning-with-entra-id-formerly-azure#h_01KTGM1RRW7QF28GCYJ20PKCXP) users and groups to the account.

## Reviewing the SCIM Provisioning Attributes

After you configure the Cato SCIM app, you can review the mapping for the SCIM provisioning attributes between Entra ID and the Cato Management Application.

| Azure AD Attribute | Cato User Attribute | Notes about User |
| --- | --- | --- |
| userPrincipalName | userName | User name for user |
| Coalesce([mail], [userPrincipalName]) | emails[type eq "work"].value | Email address |
| givenName | name.givenName | First name |
| surname | name.familyName | Last name |
| telephoneNumber | phoneNumbers[type eq "work"].value | Phone number (including prefix) |
| objectId | externalId | ID for user (used in events) |
| Switch([IsSoftDeleted], , "False", "True", "True", "False") | active | When a user is unassigned from the SCIM app, the user is soft deleted with the parameters: "False", "True", "True", "False" |
| onPremisesSecurityIdentifier | onPremisesSecurityIdentifier |  |
| dirSyncEnabled | dirSyncEnabled |  |
| jobTitle | title |  |
| department | urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:department |  |

## Assigning SDP Licenses

In the IdP, define the groups and users that are synced to your Cato account. After the initial sync is completed, all users are then created in the Cato Management Application and visible on the **Users Directory** page .

You can then assign SDP licenses to users, for more information, see [Assigning ZTNA Licenses to Users](/v1/docs/assigning-ztna-licenses-to-users).

#### **Removing Users or User Groups from the SCIM App**

> [!NOTE]
> Important:
> 
> Although users can be deleted within the CMA, we recommend you delete users or user groups that are provisioned with the SCIM app directly from the Azure portal.

When you want to remove users or user groups that are provisioned to your Cato account with the SCIM app, unassign them in the app. The users and user groups are automatically disabled the next time the SCIM app syncs with your account.

**To remove users or user groups that are synced to your Cato account:**

1. In the Cato SCIM app, unassign the users or user groups.

During the next sync, the SCIM app disables the users or user groups in your Cato account.
2. **(Optional)** After the users or groups are disabled, you can delete them from the Cato Management Application.

It can take up to 15 minutes before you can manually delete users or user groups.

## Understanding Events for SCIM Provisioning

The Cato Management Application generates events whenever users and groups are blocked because they fail to meet the requirements of the Client Connectivity Policy.

Each hour, the Cato Management Application sends email alerts that summarize the SCIM provisioning actions (success or failure).

The following table explains the different events.

| Event Type | Action | Description |
| --- | --- | --- |
| SCIM Provisioning | Success | The action to sync the users or groups to your account with the SCIM app succeeded. |
| SCIM Provisioning | Failure | The SCIM app failed to sync the IdP with your account. The **event message** explains the reason for the sync failure. |
| SCIM Provisioning | Disabled | A disabled user in the IdP was successfully synced and disabled in your Cato account. |
