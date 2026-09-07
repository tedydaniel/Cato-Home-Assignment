---
title: "Syncing Users with LDAP"
slug: "syncing-users-with-ldap"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/syncing-users-with-ldap"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Syncing Users with LDAP

In this article we will explain and demonstrate how to configure your Cato account to work with Active Directory (LDAP integration). The feature will allow you to fetch the users and add them automatically to the Cato Management Application (CMA). It will NOT authenticate to the AD server.

The `sAMAccountName` attribute is used for the name of the User Group in the Cato Management Application.

The sync has two main options:

1. Syncing with a local AD server

2. Syncing with an external AD server

## Understanding User Sync Settings

Changes to LDAP users on the Domain Controller can trigger a high number of user modifications in the Cato Management Application. To reduce the risk of errors, you can choose to limit the number of changes made in each sync in these ways:

- **Prevent removing or disabling users:** You can limit the number of users that are removed or disabled.
- **Prevent updating group membership:** If an LDAP sync changes user group membership of 1500 or more users, Microsoft on-premise Active Directory may remove the users from the group. To prevent this, you can customize the maximum number of users that can change user group membership in a single sync. For more information, see [Directory Services and User Awareness Errors Troubleshooting](/v1/docs/directory-services-and-user-awareness-errors-troubleshooting)
- **Update user emails:** You can limit the number of user email addresses that are updated.

If the limit is exceeded, the next LDAP sync will fail and an event with the **Directory Services** Sub-Type is created.

> [!NOTE]
> Note:
> 
> A single group containing more than 10,000 members cannot be synced.

## Syncing a Local AD Server

If the LDAP sync isn't working correctly, see [LDAP Sync and Provisioning Troubleshooting](/v1/docs/ldap-sync-and-provisioning-troubleshooting).

**How to sync a local AD server (server behind a Cato site):**

1. Add the AD server to the **Static Host Reservations** page for the site.

![Hosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218214952349.png)
  1. From the navigation menu, select **Network > Sites**, and select the site.
  2. From the navigation menu, select **Site Configuration > Static Host Reservations**.
  3. Click **New** and enter the settings for the AD server.
  4. Click **Apply** and then click **Save**.
2. Add a new domain to the **LDAP** services for the account.
  1. From the navigation menu, click **Access > Directory Services**, and select the **LDAP** tab or section.
  2. Click **New**, and configure the settings for the AD domain.

![New_DirectorySevice.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218225793309.png)
    - Login DN and Base DN - The unique string for the AD (authenticating for fetched users)
    - Password - The password to access the Active Directory DN
    - Encryption - Select **Use SSL** to secure the connection, not supported by all servers
    - SDP User Sync Settings - Select the limits to add to an LDAP sync
  3. Click **Save**.
3. Add the AD server (from step 1) as a domain controller (DC) to the domain.
  1. In the panel navigation section, click **Domain Controllers**.
  2. In the top drop-down menu, select **Host**, and in the next drop-down menu, select the host from step 1.

![AD_host.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218212619293.png)
  3. Click **Save**.
4. Select the AD groups you are syncing to your Cato account.

> [!NOTE]
> Note:
> 
> - If no groups are selected, then all the AD groups are imported for User Awareness.
> - Nested groups are synced if you select the parent group
> - The User Principal Name (UPN) AD parameter must be configured for a user to be identified by User Awareness
  1. In the panel navigation section, click **User Groups**.
  2. Select the AD groups that your are syncing.

![Edit_User_Groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218215217949.png)

> [!NOTE]
> Note:
> 
> Capitalization matters when importing organizational units from Active Directory. **ExampleGroup** will be treated differently from **EXAMPLEGROUP**.

If you change the name of the OUs within Active Directory, please ensure that you also change the selected OUs within the CMA.
  3. Select **Daily Sync User Groups** to enable automatically syncing the groups and users each day.
  4. Click **Save and Close**.
5. In the **Directory Services** screen, click **Sync Now**.

After users are synced, they can be assigned an [SDP license](/v1/docs/assigning-ztna-licenses-to-users).

For User Awareness, users can be identified by [AD query](/v1/docs/using-ad-query-for-user-awareness) or the [identity agent](/v1/docs/using-cato-identity-agents-for-user-awareness).

## Syncing an External AD Server

If you need to sync an external AD server, then you can perform the same procedure as above.

- When the UPN and/or email address of an LDAP user has been changed in the AD, the status of the affected LDAP user remains unchanged in the CMA.
- When syncing the Azure AD, both the **Member** and **Guest** user types are synchronized.
- Make sure that the first and last names are configured for AD users. Otherwise, users missing a first or last name are NOT synced to your Cato account.

## Syncing a Local AD Server

If your Domain Controller is behind an IPsec connection or if you are routing only some subnets to the Socket, be sure to include the IP address of the CMA in your VPN tunnel routing configuration. Traffic from and to this IP should be routed via the Cato tunnel.

For more information about the IP address for the CMA, see [Resolving Issues with LDAP Sync](/v1/docs/resolving-issues-with-ldap-sync) (you must be logged in to your Cato Knowledge Base account to view this article).
