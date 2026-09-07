---
title: "Provisioning Users with SCIM"
slug: "provisioning-users-with-scim"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/provisioning-users-with-scim"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Provisioning Users with SCIM

This article discusses provisioning users to your Cato account with the SCIM protocol.

## Overview

SCIM defines a standard for exchanging identity information across different cloud app vendors. For example, with SCIM you can easily create, update, or remove user data at scale in your Cato account.

User information is securely synced from your IdP to Cato to create users. Any changes to users details that were made in the IdP are reflected in Cato in near real time. For example, if an employee leaves a company, their account is removed from the company IdP. This change is synced with Cato and the user is deleted.

You can see which users were imported and which users were manually created in the Directory Name column - imported users appear with the name of SCIM directory and manually created appear as Manual. You can also filter by a directory name, or to see all of the manually added users in your system.

Once a user is provisioned with SCIM they can be assigned a license and be included in policies.

> [!NOTE]
> **Note:** Adding a new SCIM provider or directory should not be used to migrate an existing directory. For information about migrating users, see the articles in [this section](/v1/docs/migrating-from-ldap-to-scim-user-provisioning).

## Advantages of Provisioning users with SCIM

Provisioning users with SCIM has these advantages:

- Immediately synchronize users from the IdP to your Cato account.
- Updates or changes to group membership or user profiles are updated in near real time
- Integrate the IdP to your Cato account without configuring any in-bound firewall rules
- SCIM is widely supported by IdP vendors, and is easy to integrate with your account

## Provisioning Users Process Flow

This process explains how users are provisioned from your IdP, and then assigned licenses and added to policies, so they can securely connect to the network.

![User_Provisioning.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810723299869(1).png)

1. In your IdP, define the users and/or groups to be provisioned to Cato.
2. Configure automatic user sync with Cato.
3. Assign licenses to required users
4. Apply polices to users

## Provisioning Users with SCIM

These are the IdPs that are support for provisioning users with SCIM:

- Azure
- Okta
- One Login
- DTS

For more information on how to configure SCIM provisioning for each IdP, see [Provisioning Users with SCIM](/v1/docs/scim-user-provisioning) and [Using an Identity Provider for Your Cato Account](/v1/docs/using-an-identity-provider-for-your-cato-account).

## Removing Users or Groups from the SCIM App

We recommend that you assign or unassign users or groups from the SCIM app in your IdP. However, it is also possible to enable, disable, and delete SCIM-provisioned users and groups directly from the CMA. These changes are synced to the SCIM Service automatically.

> [!NOTE]
> **Note:** Users disabled or deleted in the CMA that were provisioned with SCIM from:
> 
> - Entra ID are revived and enabled at the next provisioning cycle. Entra overrides the disabled or deleted state and re-enables the user automatically.
> - Okta
>   - Disabled users — remain disabled. Okta preserves the disabled state when sending updates. Reassigning a disabled user to the Okta SCIM application fails until the user is re-enabled in the CMA.
>   - Deleted users — remain inactive in the SCIM Service. To re-provision a deleted user, unassign the user from the Okta application and reassign it. The user is reactivated in the SCIM Service and the CMA.

When you want to remove users or groups that are provisioned to your Cato account with the SCIM app, unassign them in the app. The users and groups are automatically disabled during the next time the SCIM app syncs with your account.

If you are removing or changing SCIM providers, ensure you remove all imported users or groups from the SCIM app before deleting your SCIM provider configuration from CMA. After the SCIM app syncs, these entities are disabled in the CMA.

When you disable or remove SCIM provisioned users with a ZTNA (SDP) license, the ZTNA license is unassigned and available for other users.

### Re-provisioning User Groups After Deletion

The behavior when re-provisioning a deleted user group differs by IdP:

- Entra ID: Re-provisioning a deleted user group re-creates it, but membership is not restored. To restore membership, remove the group from the Entra application and add it back. Membership is restored at the next provisioning cycle.
- Okta: Pushing a deleted user group from Okta will fail. To re-provision the user group, remove it from the Okta application and reassign it. This restores the user group and its membership.

### Deleting an Active SCIM Directory

You can delete a SCIM directory from your account. After deletion, changes to its users and groups are no longer synced from the IdP. You can delete a directory even if it still has active users.

**Note:** You cannot delete a SCIM directory that is used for SSO User Authentication. Remove the directory from your User Authentication configuration before deleting it.

![delee_scim.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36330708309277.png)

**To delete a SCIM directory:**

1. From the navigation pane, go to **Access > Directory Services** and click the **SCIM** tab.
2. At the end of the SCIM directory row, click the three-dot icon and select **Delete**.
3. In the confirmation window, click **Delete**. This SCIM directory is deleted from your Cato account. Future changes from the IdP for this directory will no longer be synced.
