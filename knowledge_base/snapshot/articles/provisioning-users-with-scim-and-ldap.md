---
title: "Provisioning Users with SCIM and LDAP"
slug: "provisioning-users-with-scim-and-ldap"
updated: 2026-07-02T15:34:55Z
published: 2026-07-02T15:34:55Z
canonical: "knowledge.catonetworks.com/provisioning-users-with-scim-and-ldap"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Provisioning Users with SCIM and LDAP

## Overview

Cato leverages your existing Identity Provider (IdP), which is a centralized service for managing user identities, and supports the ability to easily provision and synchronize users to your account. The IdP is integrated with your Cato account and automatically imports and updates users.

Cato supports the following methods to provision users and user groups:

- Import users from an IdP via SCIM and LDAP
- Import users from an IdP via SCIM
- Import users from an IdP via LDAP

For more information, see [Changing Between SCIM and LDAP User Provisioning](/v1/docs/changing-between-scim-and-ldap-user-provisioning).

### Assigning Licenses

Once a user or user group is provisioned through any of these methods, they can be included in any policy and be assigned a ZTNA license. For example, you can import one user from SCIM and another user with LDAP, and both can be assigned a remote user license. For more information, see [Defining Remote Access for Users](/v1/docs/assigning-ztna-licenses-to-users).

## Adding LDAP Directories When SCIM Is Configured

The number of SCIM directories configured in the CMA determines whether you can add LDAP directories:

- If one SCIM directory is configured, you can add multiple LDAP directories. There is currently no known limit to the number of LDAP directories you can add
- If two or more SCIM directories are configured, you can’t add LDAP directories

To add an LDAP directory when two or more SCIM directories are configured, first disable SCIM directories until only one SCIM directory remains configured. Then add the LDAP directory.

## Using SCIM and LDAP to Provision Users

SCIM and LDAP can be used together to provision users. However, each individual user must be provisioned exclusively through either SCIM or LDAP, not both. This guarantees a single source of truth for each user.

If the same user is identified as being provisioned with both SCIM and LDAP, the SCIM provisioned user overrides the LDAP provisioned user. This means the LDAP provisioned user is removed from LDAP provisioned groups and added to SCIM provisioned groups.

SCIM provisioning is used as the single source of truth to ensure consistent behavior. This can influence whether users are provided with the intended access. For example:

- User John Doe is provisioned with LDAP and a member of a User group that has gambling sites blocked by an Internet Firewall rule
- John Doe is then provisioned with SCIM, no SCIM groups are in the Internet Firewall rule
- The SCIM provisioned user overrides the LDAP provisioned user, and John Doe is removed from the User group that blocks access to gambling sites
- John Doe is not included in the Internet Firewall rule and can access gambling sites

Users are identified as a match based on email address or UPN.

## Using SCIM and LDAP to Provision User Groups

SCIM and LDAP can be used together to provision User Groups. However, each individual User group must be provisioned exclusively through either SCIM or LDAP, not both. This guarantees a single source of truth for user identity, and ensures a consistent user identity across your environment.

If the same User group is provisioned with both SCIM and LDAP, the SCIM provisioned user group overrides the LDAP provisioned user group. If the LDAP provisioned User group contained users that are not included in the SCIM provisioned User group, those users are removed from the User group in the Cato Management Application. This can have implications on ensuring that you provide users with the intended access. For example:

- The Finance Team User group is provisioned with LDAP and has gambling sites blocked by an Internet Firewall rule. It contains the following users:
  - John Doe
  - Jane Phillips
  - Simon Thompson
- The Finance Team User group is then provisioned with SCIM and contains the following users:
  - John Doe
  - Jane Phillips
- The SCIM provisioned User group overrides the LDAP provisioned user group
- Simon Thompson is removed from the Finance Team User group and can access gambling sites
