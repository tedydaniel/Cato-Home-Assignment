---
title: "Manage Admins with your Identity Provider (IdP)"
slug: "manage-admins-with-your-identity-provider-idp"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/manage-admins-with-your-identity-provider-idp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Admins with your Identity Provider (IdP)

This article discusses provisioning Cato admins with your IdP.

## Overview

Cato leverages your existing Identity Provider (IdP), which is a centralized service for managing user identities, and supports the ability to easily provision and synchronize admins to your account. The IdP is integrated with your Cato account and automatically imports and updates admins.

Synchronizing admins from your Identity Provider (IdP) to Cato streamlines onboarding and offboarding, improves security, and helps maintain consistency when managing admin roles.

After users are synchronized from your IdP, you assign them admin roles to define them as admins in Cato. You can then add, delete, or modify users in your IdP, and the changes will be synchronized to Cato.

## Connect the IdP to your Cato Account

If you are not yet managing Cato user provisioning with your IdP, see the articles in the following sections to configure an integration:

- [SCIM User Provisioning](/v1/docs/scim-user-provisioning)
- [LDAP User Provisioning](/v1/docs/ldap-user-provisioning)

## Assign Roles to Provisioned Admins

All users imported from your IdP are treated as Cato users by default. You define them as admins by assigning them admin roles.

**To assign roles to admins imported from IdPs:**

1. From the navigation menu, click **Account > Administrators**.
2. In the **Role Assignments** tab, click **New**.
3. In Users and Groups, select individual users or groups of users that you want to give admin roles.
4. In the **Roles** area, define one or more roles to assign to the admins.
5. In the **Permissions** area, define which sites and users the admins can view or edit.

## FAQs

---

### 

#### What happens if a group is removed from a role assignment?

- All members of the group lose any roles assigned through that group.
- If a user has no other role assignments, they are removed as an admin.
- If a user has individual role assignments, those roles remain active and unaffected.

#### Can an IdP-provisioned user override a manually created user?

Yes. When a user is provisioned through the IdP and has the same email address as an existing, manually created user:

- The IdP user will override the manual user.
- Authentication settings, secrets, and user attributes are preserved.
- Admin roles previously assigned manually are replaced with those defined through the IdP.
- This behavior ensures clean, consistent access management and prevents permission conflicts.

#### Can the same email be used across multiple accounts?

No. Each email address must be unique across all accounts. This applies to both manually created users and users synced from the IdP.
