---
title: "Understanding the Single User Identity"
slug: "understanding-the-single-user-identity"
updated: 2026-07-01T11:25:17Z
published: 2026-07-01T11:25:17Z
canonical: "knowledge.catonetworks.com/understanding-the-single-user-identity"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the Single User Identity

## Overview

Managing users and enforcing policies is a key component of an administrator's role in controlling user access and Cato implements this with a single user identity. To simplify operations for administrators and increase visibility when applying policies, there is a single user for User Awareness users and remote access with a Cato Client.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(41).png)

- The single user identity in the Cato Management Application (CMA) is referred to as a **User**
- All users in your account are shown on the **Users Directory** page with a clear indication of remote users that have a ZTNA license
- With the single user identity, after you add a User to a policy, it is enforced whether the user is located behind a site or remotely

### Working with User Groups

- All existing user groups only include a single user identity.
- These are the different system user groups:
  - **All Remote Users** - policies are only enforced when working remotely. The policies are NOT enforced when the users are located at the office.
  - **All Users** - policies are enforced whether users in this group are located at the office or working remotely.
  - **All Manual Users** - Users created manually in the CMA (only for assigning licenses, can't use in policies)
  - **All SCIM Users** - Users provisioned from an IdP using SCIM (only for assigning licenses, can't use in policies)
  - **All LDAP Users** - Users provisioned from an IdP using LDAP (only for assigning licenses, can't use in policies)

For more information, see [Working with User and System Groups](/v1/docs/working-with-user-and-system-groups).

### Use Case - Enforcing an Internet Firewall Policy

In an Internet Firewall policy, you want to block access to gambling sites and apps for specific users.

- Users behind a Socket are automatically blocked when the rule is implemented.
- To include remote users in this rule, you should add the **Users** entity as a source.

## Assigning a License from the CMA

A license is required for a user to connect to the network remotely. Licenses are assigned and managed from the **Access > License Assignment** page. This increases visibility for administrators as they can manage licenses from a single page.

Users must be provisioned with an email address to be assigned a license.

![License_Assignment.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25078034542621.png)

Also, see [Defining Remote Access for Users](/v1/docs/assigning-ztna-licenses-to-users).

## Identifying Manually Created Users

You can get the identity for manually created users behind a site using the [Cato Identity Agent](/v1/docs/using-cato-identity-agents-for-user-awareness). Users are required to authenticate once.
