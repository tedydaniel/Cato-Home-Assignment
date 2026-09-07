---
title: "Using an Identity Provider for Your Cato Account"
slug: "using-an-identity-provider-for-your-cato-account"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/using-an-identity-provider-for-your-cato-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using an Identity Provider for Your Cato Account

The goal of this article is to show the different options that you can integrate Identity Providers (IdPs) with your Cato account for user provisioning for the following users: clientless SDP, Cato Clients, and admins to the Cato Management Application.

## Overview of IdPs with Cato

Cato lets you select one of several IdPs to provision users who are connecting to your account over the Cato Cloud. The following table gives an overview of connecting an IdP to your Cato account.

For more information about SSO, see [Supported IdPs for SSO Authentication](/v1/docs/supported-idps-for-sso-authentication).

| IdP | Configuring the IdP | Users Provisioned to Cato | Notes |
| --- | --- | --- | --- |
| Azure | Configure the Windows server | LDAP and SCIM |  |
| Okta | Configure the Cato app in Okta | LDAP and SCIM |  |
| OneLogin | Configure Cato app in OneLogin | vLDAP and SCIM | See [Configuring LDAP Sync and SSO with OneLogin](/v1/docs/configuring-ldap-sync-and-sso-with-onelogin) |
| JumpCloud | Configure Cato app in JumpCloud | LDAP |  |
| OneWelcome | Configure connection to your Cato account in OneWelcome | SCIM | For more about OneWelcome and Cato, contact Support |
| DTS | Configure Cato app in DTS | SCIM |  |

For more about user provisioning with SCIM, see article for the relevant IdP:

- [SCIM Provisioning with Azure](/v1/docs/scim-provisioning-with-entra-id-formerly-azure)
- [SCIM Provisioning with Okta](/v1/docs/scim-provisioning-with-okta)
- [SCIM Provisioning with OneLogin](/v1/docs/scim-provisioning-with-onelogin)
- [SCIM Provisioning with DTS](/v1/docs/scim-provisioning-with-dts)
- [Creating a Custom SCIM App for an IdP](/v1/docs/creating-a-custom-scim-app-for-an-idp)

### Selecting the LDAP Provider

The LDAP Directory Service providers show the LDAP provider which is defined for the account. When you are defining the LDAP domain, select the **AD Provider** for your organization.

You can only edit the **AD Provider**, when there is a single domain defined for your account.

**To select the AD provider for the domain:**

1. From the navigation menu, click **Access > Directory Services**, and select the **LDAP** tab or section.
2. Click **New**, or click the **AD Provider**.

The **Edit** or **New Directory Service** panel opens.
3. From the **General** tab, in the **AD Provider** drop-down menu, select the LDAP provider.

![LDAP_AD_Provider.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218222078749(1).png)
4. Click **Save & Close**.
