---
title: "Implementing LDAP User Provisioning"
slug: "implementing-ldap-user-provisioning"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/implementing-ldap-user-provisioning"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Implementing LDAP User Provisioning

The **Directory Service Settings** section lets you configure the settings to sync users between your account and LDAP domains, such as Active Directory (AD).

> [!NOTE]
> Note:
> 
> You need to allowlist the IP addresses for the Cato Management Application (CMA) that is the source IP for the Cato LDAP service, see [Using Cato IP Addresses](https://support.catonetworks.com/hc/en-us/articles/20511945810589-Using-Cato-IP-Addresses) (you must be signed in to view this article).

## High Level Workflow of Configuring a Domain

This is the workflow to use Directory Services to integrate an LDAP domain with your Cato account:

1. [Adding a Domain to the CMA](/v1/docs/implementing-ldap-user-provisioning#adding-a-domain-to-the-cma)
2. [Adding a Domain Controller](/v1/docs/implementing-ldap-user-provisioning#adding-a-domain-controller)
3. [Synchronizing the Domain with Your Cato Account](/v1/docs/implementing-ldap-user-provisioning#synchronizing-the-domain-with-your-cato-account)

## Adding a Domain to the CMA

When you add an LDAP domain to your account, you need to add a Directory Service connection to the CMA. Each domain and child domain in your organization needs a separate connection in the **Directory Service Settings** window. For example, if your account has the domains **sample.com**, **alpha.sample.com**, and **example.com**, then you need to create three connections in **Directory Service Settings**.

For the domain **Password**, the maximum length of a password is 48 characters.

When you enter the distinguished names (DNs) for the domain:

- Login DN refers to the object in the LDAP directory hierarchy for the admin
- Base DN refers to the object in the LDAP directory hierarchy for the users and groups that the admin is syncing with Cato

### Understanding User Sync Settings

Changes to LDAP users on the Domain Controller can trigger a high number of user modifications in the CMA. To reduce the risk of errors, you can choose to limit the number of changes made in each sync in these ways:

- **Prevent removing or disabling users:** You can limit the number of users that are removed or disabled.
- **Prevent updating group membership:** If an LDAP sync changes user group membership of 1500 or more users, Microsoft on-premise Active Directory may remove the users from the group. To prevent this, you can customize the maximum number of users that can change user group membership in a single sync. For more information, see [Directory Services and User Awareness Errors Troubleshooting](/v1/docs/directory-services-and-user-awareness-errors-troubleshooting)
- **Update user emails:** You can limit the number of user email addresses that are updated.

If the limit is exceeded, the next LDAP sync will fail and an event with the **Directory Services** Sub-Type is created.

> [!NOTE]
> Note:
> 
> If a user is disabled and then re-enabled on your AD, they may need to uninstall and reinstall the Cato Client to connect to the network.

#### Changing the Path to a Group in your Domain Controller

If you change the path to a Group in your Domain Controller, you must also update the **Base DN** in the CMA.

If you do not update the CMA to the new path, User groups that have been moved are no longer included in syncs and are deleted. These User groups are no longer visible on the **User Groups** page. Deleted User groups are still visible in policies and marked as deleted and the policy is not applied to the User group. SDP licenses are removed from users within the deleted LDAP provisioned User group and can no longer connect to the network. If the users need to connect to the network, then it's necessary to re-assign SDP licenses to them.

### Adding a Domain to the CMA

![New_DirectorySevice.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038801296541.png)

**To add a domain to the CMA:**

1. From the navigation menu, click **Access > Directory Services**.
2. From the **LDAP** section or tab, and click **New**.

The **New Directory Service** panel opens.
3. Select the **LDAP Provider**.

Only one LDAP provider can be selected.
4. In the **LDAP Authentication Description** section, configure the **Login DN**:
  - For on-premise AD, use the AD account Distinguished Name (DN)
  - For an Azure AD, use the AD account User Principal Name (UPN)
5. Enter the **Login DN**and **Base DN**.
6. Enter the **Password** for the CN user that you created for the Directory Services connection.
7. For LDAP domains that use an SSL connection, select **Encryption**.

The domain is added to the CMA. Configure the Domain Controllers for the domain.
8. Select your **SDP User Sync Settings**.

## Adding a Domain Controller

Add the Domain Controller (DC) that is associated with the LDAP server to the Directory Services domain.

For LDAP servers that are behind a site, you can add the DC using the IP address or as a host that is defined for a site (**Network > Sites > {site name} > Site Configuration > Static Host Reservations**).

For servers that are external and use a public IP address, you can define the DC using an IP address or the domain.

**Allowlisting Cato IPs**

To ensure traffic can reach your AD services, allowlist the IP addresses listed in [Using Cato IP Addresses](https://support.catonetworks.com/hc/en-us/articles/20511945810589-Using-Cato-IP-Addresses) (you must be signed in to view this article). Traffic to and from these IP addresses is routed inside the Cato tunnel.

Make sure that firewalls or routing devices are configured correctly for the following deployments:

- The DC resides behind an IPsec site (instead of a Socket)
- All of the traffic isn't routed to the Socket

![Edit_DC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038801335965.png)

**To add a domain controller:**

1. In the navigation menu of the **New Directory Service** panel, click **Domain Controllers**.
2. Define the connection settings to the DC depending on its location:
  - For DCs on a host defined behind a site, select **Internal Host**, and then select the static host for the LDAP server
  - For DCs that use an internal IP address, select **Internal IP** and enter the IP address for the DC
  - For DCs that aren't behind a site, select **External IP or Domain**, and enter the IP address or domain for the DC
3. Click **Add**.
4. For deployments with multiple DCs, repeat the previous steps to add each DC.
5. Click **Save and Close**.

### Testing Connectivity to a Domain

After you define the domain and add the DC, we recommend that you test the connectivity between the domain and the CMA.

The CMA automatically tests connectivity to all the DCs for the domain, and shows the results for each DC.

If the connectivity test is unsuccessful, see [Troubleshooting Directory Services and User Awareness Errors and Issues](/v1/docs/directory-services-and-user-awareness-errors-troubleshooting) for troubleshooting recommendations.

**To test the connectivity to the domain:**

- From the **Connection** column for the domain, click **Test connection**. The CMA shows the results of the connectivity test.

## Synchronizing the Domain with Your Cato Account

After you add the DCs, configure the settings that define how to synchronize the users in the LDAP groups.

- If you are using Directory Services and you need to modify a user's mobile phone number for MFA, only modify the phone number in the LDAP directory

### High Level Overview of Configuring the Directory Service Settings for a Domain

1. Select the LDAP groups that are synchronized with your account.
2. Enable or disable automatically synchronizing the users each day.
3. Define the behavior for users that are removed from the LDAP group - to disable or to remove them from the CMA.

### Importing Active Directory Groups

Select the LDAP groups to be synced into your account.

**To select the AD groups that are imported to your account:**

1. In the **New Directory Service** panel, click **User Groups**.
2. From the **Select User Groups** dropdown, select the groups that you are syncing with your account.

**Note:** If no groups are selected, the entire Active Directory is imported.

Configure the Synchronization settings for this domain (see below).

### Assigning Licenses and Applying Policies

Once users are synced into your account, you can assign them SDP licenses and apply policies that are enforced wherever the user connects. For more information on assigning SDP licenses, see [Assigning ZTNA Licenses to Users](/v1/docs/assigning-ztna-licenses-to-users).

### Overview of Synchronization Settings

You can enable your account to automatically synchronize each day with the LDAP directory, and update the groups and users in the CMA to match those in the domain.

You can see which users were imported and which users were manually created in the **Directory Name** column - imported users appear with the name of LDAP directory and manually created appear as **Manual**. You can also filter by a directory name, or to see all of the manually added users in your system.

Cato starts the daily automatic LDAP sync for all accounts at 12:00 am UTC. Cato performs the sync one account at a time, and it can take several hours to complete the daily sync of all accounts. If the **Daily Sync User Groups** option is disabled after 12:00 am, but before Cato starts the LDAP sync, then the automatic sync is skipped until the next time window when the option is enabled.

> [!NOTE]
> Note:
> 
> For accounts with multiple domains, the synchronization settings must be the same for all the domains in your account. Otherwise, there can be issues related to possible trust dependencies between the different domains.

**Users that No Longer Exist in Directory Service Groups**

The **If user no longer exists in imported Directory Service groups** setting lets you define the synchronization behavior when users or groups are deleted from the LDAP server or have expired or been disabled. You can choose from the following options:

- **Disable** - the users are disabled and can't connect to the Cato Cloud. The user remains in User Groups they were members of
- **Remove** - the users accounts are removed from the CMA, including from User Groups they were members of

When groups or users are removed from the LDAP server, but they are used by an object or rule in the CMA, this is the sync behavior:
  - Users are disabled instead of deleted
  - Groups are marked as no longer synced
  - The groups or users are labeled as **Manual** instead of **LDAP**

By default, the CMA prevents accounts from deleting or disabling more than 100 users as part of the LDAP sync. At the start of the LDAP sync, if the sync will delete or disable more than 100 users (for the default setting), then the sync is canceled and an email notification is sent. You can disable preventing deleting or disabling users, or change the maximum number of deleted users per LDAP sync.

### Configuring the Directory Service Synchronization Settings

Configure the settings for the sync between the domain and your Cato account. You choose to enable a daily automatic sync and the behavior when a user is removed from a Directory Service group.

**To configure the synchronization settings for a domain:**

1. Manage the automatic sync settings:
  1. In the **New Directory Service** panel, select **User Groups**.
  2. In the **User Groups** section, select to enable or disable **Daily Sync User Groups**.

The toggle is green when enabled.
2. Define the behavior **If user no longer exists in imported Directory Service groups** in the AD domain:
  - **Disable** the user in the CMA
  - **Remove** the user from the CMA
3. **(Optional)** Customize the setting for **Prevent deleting more than** a number of users during LDAP sync:
  - To change the how many users that can be deleted during LDAP sync, in **users**, enter the maximum number of deleted users.
  - To remove the limit of how many users that can be deleted during LDAP sync, disable ![slider_disable.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038825922973.png) this setting.
4. Click **Apply** and then click **Save**.

The domain is configured to sync users and groups with your account.

### Manually Synchronizing the Directory Services

Use the **Sync Now** feature to manually synchronize users and groups between the AD server and the CMA. For accounts with multiple domains, the CMA synchronizes all domains simultaneously because there can be trust dependencies between domains.

Even after you review the candidate changes and click Submit, not all submitted changes are necessarily applied. The CMA validates each change before creating or updating users and groups. For example, a change can fail if a Manual group with the same name already exists. You can review the results of each processed change in the [Events](/v1/docs/analyzing-events-in-your-network) page.

> [!NOTE]
> Note:
> 
> It might take a few minutes for the Events page to update with the changes.

**To manually sync the Directory Services for all domains:**

1. From the navigation menu, click **Access > Directory Services**.
2. In the **LDAP** section or tab, click **Sync Now**.
3. The Manual LDAP Sync window opens and shows the potential changes to users and groups. Review the changes and click **Submit**.
4. A confirmation page indicates that the request was submitted and includes a link to the Events page, already filtered for the relevant system event and sub-type.
  - If the sync is successful, a system event with the sub-type **LDAP Provisioning** is generated with a message similar to:

User 'x' was created
  - If the sync fails, a system event with the same sub-type is generated with a message similar to:

Failed to save user
  - If you want to again search for potential changes that were submitted, look for system events with the sub-type **Directory Services** that have a message similar to:

'x' potential change(s) were submitted

#### Example

In the following example, you can see that 3 potential changes were manually submitted.

![submit-ldap-sync.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038761460253.png)

The changes were submitted successfully, and upon checking the Events page, you can see that Jane Phillips was successfully created:

![ldap-sync-success.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038809901725.png)

However, John Doe could not be created because a manually created user with that email already exists in the account.

![ldap-sync-failed.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038761515421.png)

## Deleting Domains and Domain Controllers

You can delete domains and DCs when they are no longer needed.

> [!NOTE]
> Note:
> 
> When you delete a domain or DC, its users are no longer associated with the domain and are labeled Cato Users. If you add the same users from the same, or a different, domain they are duplicated in the system. Once as Cato Users and once under the domain.

**To delete a domain:**

1. From the navigation menu, click **Access > Directory Services**.
2. In the **LDAP** section or tab, in the row of the domain click ![Delete.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038801523613.svg-xml).
3. Click **Save**. The domain is deleted from your account.

**To delete a domain controller:**

1. From the navigation menu, click **Access > Directory Services**.
2. In **LDAP** section or tab, edit the domain.

The **Edit Directory Services** panel opens.
3. In the navigation menu of the **New Directory Service** panel, click **Domain Controllers**.
4. In the row with the DC, click ![Delete.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34038801523613.svg-xml).
5. Click **Apply** and then click **Save**. The DC is deleted from the domain.

## Managing Multiple Domains

If your organization has more than one domain, you can define Directory Service connections for each domain. Add and configure the new domains to the account.

You must enter the password for each new domain that you add to the account.
