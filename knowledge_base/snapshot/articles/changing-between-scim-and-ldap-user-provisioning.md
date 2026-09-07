---
title: "Changing Between SCIM and LDAP User Provisioning"
slug: "changing-between-scim-and-ldap-user-provisioning"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/changing-between-scim-and-ldap-user-provisioning"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changing Between SCIM and LDAP User Provisioning

This article explains the considerations of changing provisioning methods from SCIM to LDAP or vice versa.

## Overview

Cato leverages your existing Identity Provider (IdP), which is a centralized service for managing user identities, and supports the ability to easily provision and synchronize users to your account. The IdP is integrated with your Cato account and automatically imports and updates users. This ensures that you have a single source of truth for user identity and gives you consistent user identity across your environment. For more information about SCIM vs LDAP user provisioning, see [Provisioning Users with SCIM and LDAP](/v1/docs/provisioning-users-with-scim-and-ldap).

Cato supports the following methods to import and create users:

- Import users from an IdP via SCIM
- Import users from an IdP via LDAP
- Manually create users in the Cato Management Application

For more information on how to configure each method, see the articles in [Directory Services](/v1/docs/directory-services).

### Benefits of SCIM Import

- User Awareness is supported from Windows Client v5.4 and higher and macOS Client v5.3 and higher. For more information, see Using Cato Identity Agents for User Awareness.
- Immediately synchronize users from the IdP to your Cato account.
- Updates or changes to group membership or user profiles are updated in near real time.
- Integrate the IdP to your Cato account without configuring any in-bound firewall rules.
- SCIM is widely supported by IdP vendors, and is easy to integrate with your account.

## Changing How Users are Provisioned

Before you change how your users are provisioned, it is important you understand the impact on users and User groups.

### Changing from LDAP to SCIM Provisioning

These are the rules that are applied to users and User groups when you change from LDAP to SCIM provisioning:

- SCIM provisioned users override LDAP provisioned users and manually created users
  - Users are identified as a match based on their UPN or email

> [!NOTE]
> Note:
> 
> When changing from LDAP to SCIM, follow these best practices:
    1. Ensure the users that were provisioned with LDAP:
      - Have the same UPN or email address as the users to be provisioned with SCIM
      - Are existing users in the Cato Management Application
    2. If the UPN or email address are different, duplicate users are created.
    3. Assign SDP licenses to **All SCIM Users**. This avoids users losing their SDP licenses as their provisioning transitions from LDAP to SCIM.
    4. If duplicate users are mistakenly created, remove the duplicate user from the Cato Management Application, update the email address in your IdP and then provision the user again.
      - If there’s more than one user with the same Object ID or UPN, the SCIM user does not override the existing SCIM user and an Event is triggered.
- SCIM provisioned User groups override LDAP provisioned User groups. Once SCIM provisioning is enabled, no updates can be made to the LDAP provisioned User groups in the Cato Management Application.
  - User groups are identified as a match based on their name or Object ID
  - If there are multiple groups with the same Object ID or Group Name the override fails. We recommend deleting duplicate groups for the override to be successful
  - Users are removed from all LDAP provisioned User groups and are assigned to SCIM provisioned User groups
  - For example:
    - 100 users are in a User group called R&D that was provisioned with LDAP
    - 10 users are in a User group called R&D that was provisioned with SCIM
    - In the Cato Management Application, the R&D user group only contains the 10 users provisioned with SCIM

**To gradually change from LDAP to SCIM user provisioning:**

1. From the navigation menu, click **Access > License Assignment**.
2. Select **Assign SDP license to selected users or groups**.
3. From the drop downs select **System Group** and **All SCIM Users**.

This prevents uses losing their SDP license.
4. Enable SCIM provisioning. For more information, see [Provisioning Users with SCIM](/v1/docs/scim-user-provisioning).

Users are provisioned with SCIM following the rules outlined above.

**Note:** After a user is provisioned with SCIM, they are removed from LDAP provisioned groups. This can impact the policy rules that are applied.

### Changing from LDAP to SCIM Azure Provisioning for Hybrid Azure AD Joined

The provisioning rules that are applied to users and user groups when you change from LDAP to SCIM for on-premises AD and Azure AD are the same as changing from LDAP to SCIM provisioning, outlined above.

Users provisioned with SCIM must have a SDP license to be identified by User Awareness. To identify users without an SDP license, provision them with LDAP. The user needs to authenticate once so that they can be identified.

In Windows Client v 5.9 and later, a SDP license is not required and the user does not need to authenticate once to be identified by the Identity Agent.

### Changing from SCIM to LDAP Provisioning

These are the rules that are applied to users and User groups with you change from SCIM to LDAP provisioning:

- LDAP provisioned users do not override SCIM provisioned users
  - Before changing, remove all SCIM provisioned users from the IdP. This disables the user in the Cato Management Application
- LDAP provisioned User groups do not override SCIM provisioned User groups
  - Before changing, remove all SCIM provisioned User groups from the IdP
- Before changing, remove SCIM provisioned users and User groups from policies and delete from the Cato Management Application
