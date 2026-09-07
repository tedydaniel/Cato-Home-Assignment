---
title: "Preparing to Migrate to SCIM (Part 1)"
slug: "preparing-to-migrate-to-scim-part"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/preparing-to-migrate-to-scim-part"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preparing to Migrate to SCIM (Part 1)

## Overview

Migrating from LDAP-based user provisioning to SCIM (System for Cross-domain Identity Management) streamlines identity management and enhances integration with modern Identity Providers (IdPs) such as Microsoft Entra ID. This article provides technical administrators with a clear pathway for migrating existing user and group management from LDAP servers to SCIM within the Cato Management Application (CMA).

The migration leverages existing user data already synchronized through LDAP and transitions provisioning responsibilities to SCIM, ensuring minimal disruption and enhanced operational efficiency. Specifically, this guide uses Microsoft Entra ID as the IdP example, detailing the necessary configuration and field mappings. However, the principles and procedures outlined can easily be adapted to other IdPs that support SCIM.

After you complete preparing to migrate to SCIM provisioning, continue with:

1. [Testing User Provisioning (Part 2)](/v1/docs/testing-user-provisioning-part-2)
2. [Migrating LDAP to SCIM (Part 3)](/v1/docs/migrating-ldap-to-scim-part-3)

## Prerequisites

1. Temporarily disable Always-On for all the users you are migrating.
2. Add the **All SCIM Users** user group to the [License Assignment page](/v1/docs/assigning-ztna-licenses-to-users).

The reason for this is that users might be disconnected from the network during the migration.
3. Verify that the number of users to be migrated is not more than the number of SDP licences assigned.

If there are more users than licences, prioritise migration of the groups that require licences, and then remove the **All SCIM Users** user group from the Licence Assignment page before continuing with the rest of the migration.
4. Clean up the LDAP directory and remove all unnecessary users and groups
5. Update the setting in LDAP sync to remove users rather than disable them if they no longer exist.
  1. In the CMA, navigate to **Access > Directory Services** and click the **LDAP** tab.
  2. Select the LDAP domain, and in the **General** section, select **Disable**.

| ![image1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28000353882141.png) |
| --- |
6. Check existing AD Groups for the presence of any nested groups - Cato does not support nested groups
7. Find WAN or Internet firewall rules that have important user groups as the **Source/Destination**, and add the **All Users** user group to the rule.

Make sure to revert this change post-migration.
  1. Identify rules where users were individually added and convert those users into groups.

**Note:** This is not a mandatory step, and it depends on downtime - if it is acceptable for users to not have access to the resources during the migration time.
8. Make sure that the group settings in SCIM are the same as the LDAP group settings. For example, LDAP domain users have the same group in the SCIM app
9. User and Group attributes such as email, UPN, first name, last name should be identical in the IdP (ie. Entra ID, Okta) and LDAP (AD) to prevent update failures or duplicate objects.
10. If changes to email or other attributes are necessary as part of the migration, these adjustments should be made either before or after the transition to prevent conflicts in the CMA.

We strongly recommend that you use a change freeze period during the migration.
11. Adequate permissions must be in place to configure the IdP application.
12. Validating the user and group attributes before the migration needs to be done using tools such as PowerShell (for example) to identify and correct any discrepancies between LDAP and SCIM providers before the maintenance starts.
13. **(Optional)** Create an export (or screenshots) of impacted CMA pages: the firewall (Internet / WAN) rules, Network Rules, Always-On policy, Client Connectivity policy, User Directory, and user groups.
14. Check the maintenance window for the CMA services so that it will not coincide with the actual maintenance window of the migration: [https://status.catonetworks.com](https://status.catonetworks.com)

## Prepare to Migrate Users

This is the logic for SCIM provisioned users in your Cato account:

- SCIM provisioned users override LDAP provisioned users and manually created users.
- Users are matched based on Internal ID, Object ID, UPN, or email

Make sure that the users who were provisioned with LDAP meet these conditions:

1. The existing users are in the CMA Access > Users > User Directory.
2. Have the same UPN or email address as the users that will be provisioned with SCIM.
  1. If the UPN or email address is different, duplicate users will be created.
  2. If duplicate users are mistakenly created, follow these steps:
    1. Remove the user from the SCIM Cato Network Provisioning app.
    2. Remove the duplicate user from the CMA.
    3. Update the email address in the LDAP IdP and then provision the user again.
3. If there’s more than one user with the same Object ID or UPN, the SCIM user does not override the existing LDAP user, and an event is generated.

## Prepare to Migrate User Groups

1. SCIM provisioned user groups override LDAP provisioned user groups
2. If there are multiple groups with the same Object ID or Group Name, the override fails. In this case, we recommend deleting the duplicate groups.
3. User Groups for LDAP - after you complete the migration to SCIM provisioning, the users are automatically removed from the LDAP user groups and added to the new SCIM user groups.

Example of migrating user groups: If a user is part of multiple user groups, they will remain active on the user groups that are migrated to SCIM and removed temporarily from user groups not yet migrated (marked as LDAP in the CMA). Once all the user groups are migrated to SCIM, the users will be re-enabled in those user groups. This might result in downtime for some users when rules with different user group types (SCIM and LDAP) are used in the CMA for some applications, and the user group types are not in the same migration batch.
