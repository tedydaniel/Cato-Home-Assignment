---
title: "Importing Users to Cato"
slug: "importing-users-to-cato"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/importing-users-to-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Importing Users to Cato

This article discusses the features and options to import SDP users to your Cato account for secure remote access to the network.

## Overview

User identity is a foundational element of zero trust and Cato makes it easy to import and manage users. Cato leverages your existing Identity Provider (IdP), which is a centralized service for managing user identities, and supports the ability to easily provision and synchronize the users to your account. The IdP is integrated with your Cato account and automatically imports and updates users.

This ensures that you have a single source of truth for user identity, and gives you consistent user identity across your environment.

Cato supports the following methods to import and create users:

- Import users from an IdP via LDAP
- Import users from an IdP via SCIM
- Manually create users in the Cato Management Application

For more information about IdPs that Cato supports, see [Using an Identity Provider for Your Cato Account](/v1/docs/using-an-identity-provider-for-your-cato-account).

## Importing Users with LDAP

You can provision users to your account with LDAP to synchronize the users from the IdP to Cato. Cato supports these IdPs for LDAP import:

- Microsoft on-premise or Azure Active Directory (AD)

(Synchronize groups with LDAP protocol)
- Okta
- OneLogin (requires vLDAP)
- Jump Cloud

For more information on how to configure LDAP provisioning with your IdP, see the articles in the [LDAP User Provisioning](https://support.catonetworks.com/hc/en-us/sections/11726226373917) section.

### Prerequisites for LDAP Import

- Domain name
- Login DN or Bind DN and associated password for authenticating to AD or the LDAP provider
- Base DN: The starting point an LDAP server uses when searching for user authentication within your directory
- Configure inbound firewall rules to allow Cato to connect to on-premise AD or Azure AD

### Lifecycle Management of Users and Groups

The LDAP sync process occurs automatically, once every 24 hours, at 0:00 GMT. Any updates to users, or deleted users, or different group memberships in the IdP are synced to your account.

### Securing LDAP with LDAPS

Cato provides the ability to improve security while importing users via LDAP between your AD and Cato, and move from LDAP to LDAPS. Cato uses TLS (SSL) to secure the LDAP connection.

Steps to configure LDAPS for your Cato account:

1. Enable LDAPS on the IdP (such as AD).
2. In the Cato Management Application, enable encryption for LDAP user provisioning.
3. Cato attempts to connect to the IdP over port 636.

For cloud-based IdPs, such as Azure AD or Okta, Cato only supports LDAPS because these flows go over the public Internet (which is inherently not secure).

Cato never imports or synchronizes the passwords for IdP user accounts.

### Benefits of Importing Users with LDAP

LDAP is a long established technology and practice for importing users.

### Additional Resources for Importing Users with LDAP

- [Overview of Directory Services and User Awareness](/v1/docs/overview-of-directory-services-and-user-awareness)
- [Configuring Directory Services with Okta LDAP](/v1/docs/configuring-directory-services-with-okta-ldap)
- [Configuring LDAP Sync and SSO with OneLogin](/v1/docs/configuring-ldap-sync-and-sso-with-onelogin)

## Importing Users with SCIM

SCIM defines a standard for exchanging identity information across different cloud app vendors and lets you sync the relevant identity data between your IdP and your Cato account.

Cato supports the following IdPs:

- Azure AD
- Okta
- OneLogin
- OneWelcome

### Prerequisites for SCIM Import

Cato supports SCIM from version 2.0 and higher.

### Benefits of SCIM Import

- Immediately synchronize users from the IdP to your Cato account.
- Updates or changes to group membership or user profiles are updated in near real time
- Integrate the IdP to your Cato account without configuring any in-bound firewall rules
- SCIM is widely supported by IdP vendors, and is easy to integrate with your account

### Additional Resources for Importing Users with SCIM

- [SCIM Provisioning with Azure](/v1/docs/scim-provisioning-with-entra-id-formerly-azure)
- [SCIM Provisioning with Okta](/v1/docs/scim-provisioning-with-okta)
- [SCIM Provisioning with OneLogin](/v1/docs/scim-provisioning-with-onelogin)

## Manually Creating Users in the Cato Management Application

You can also create users manually in the Cato Management Application. Manually creating users is often used for specific situations, and it is not a scalable solution because it requires ongoing manual effort to manage the user identity lifecycle.

For more information about manually creating users, see [Working with Users](/v1/docs/working-with-users).

### Prerequisites for Manually Creating Users

The account for each in the Cato Management Application user must include: first name, last name, and email address.

## Best Practices for Importing Users

- Importing users with SCIM is generally a better solution than importing users with LDAP:
  - SCIM is near real-time, and any changes in the directory service are automatically and quickly synced to your Cato account.
  - LDAP automatically syncs with your account once every 24 hours.
- SCIM is an easier, consistent, modern, and scalable way to manage identities from a centralized IdP to downstream applications.
- We only recommend importing users with LDAP, when it's not possible to use SCIM.
