---
title: "Configuring Multiple Identity Providers"
slug: "configuring-multiple-identity-providers"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-multiple-identity-providers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Multiple Identity Providers

You can configure multiple identity providers (IdPs) to provision and authenticate users with SSO in your account. This article explains how to configure more than one IdP in your account.

## Overview

If your organization manages users across multiple IdPs, they can all be integrated with Cato so that you do not need to combine your users into a single tenant. You can provision users from multiple IdPs (or multiple tenants from the same IdP), configure multiple SSO providers and then map which users authenticate with each provider.

When a user signs into the Cato Client, or [Browser Access](/v1/docs/configuring-the-browser-access-portal), they are only presented with the SSO provider configured for them.

> [!NOTE]
> **Note:** Configuring multiple identity providers should not be used as a method to migrate users from an existing IdP instance. To move an existing instance from one IdP to another, follow [these](/v1/docs/changing-between-scim-and-ldap-user-provisioning) instructions.

### Use Case - Company Merger

Company ABC uses Microsoft Azure as its IdP and has merged with company XYZ which uses Okta as its IdP. Both companies use Cato as their remote access solution. Instead of migrating all users from one IdP to another, the company starts to provision users from both Azure and Okta and configures them both as SSO authentication methods for remote users. Configuring multiple IdPs ensures all users can authenticate in the Cato Client without migrating any data.

## Configuring Multiple IdPs

Follow these steps to configure multiple IdPs:

1. Configure multiple SCIM directories
2. Configure multiple SSO providers to your account
3. Map directories to an SSO provider

### Step 1: Configure Multiple SCIM Directories

![Directory_Services.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26186537979677.png)

On the **Access > Directory Services** page, click **New** to add more than one SCIM directory to provision users from multiple sources. For more information on how to provision users with SCIM, see [SCIM User Provisioning](https://support.catonetworks.com/hc/en-us/sections/13651147040413-SCIM-User-Provisioning). The UPN and Object ID must be unique across all SCIM Directory Services.

### Step 2: Add Multiple SSO Providers to your Account

You can add more than one identity provider to be used in your account. The provider designated as the **Default** is used by admin to sign into the CMA. Multiple SSO providers are not supported for Admin to sign into the CMA.

![Multiple_providers.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26186538062877.png)

**To add multiple SSO providers to your account:**

1. From the navigation menu, select **Access > Single Sign-On**.
2. Click **New**.

The **Add Authentication Method** panel opens.
3. Select the identity provider you want to add and add a name.
4. (Optional) To make this identity provider the default provider for your account, enable the **Default** toggle.
5. Add the **Authentication Details** of the identity provider. Each provider has different configuration requirements. For more information on how to configure an identity provider, see the [configuration article for the identity provider](https://support.catonetworks.com/hc/en-us/sections/4963959594141-Single-Sign-On).

**Note:** If your identity provider is Azure, click **Apply** and then click **Save**. Then edit the entry for the **Setup Microsoft Consent link** to be enabled.
6. Select **Allow login with Single Sign-On** for one or more types of users in your account:
  - SDP Client users (set the **Token validity** settings)
  - Clientless SDP users (set the Cookie type)
  - Cato Management Application admins
7. Click **Apply** and then click **Save**.

### Step 3: Map Directories to an SSO Provider

On the **User Authentication** page, you can define the default authentication method for your users. If you select SSO, by default the **All Directory Services** option is selected. With this configuration, all users authenticate with the default SSO provider. You can change this configuration and map which directory should use each SSO provider.

On the **Additional Settings** tab you can configure the browser (embedded or external) that is used for authenticating in the Client and the Re-authentication prompt. For more information, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients).

![User_Authentication.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26186557442077.png)

**To map directories to an SSO provider:**

1. From the navigation menu, select **Access > User Authentication**.
2. Click the **Default Method** dropdown and select **SSO**.
3. Choose **Selected Directory Services**.
4. Click **New**.

The **New Directory Service SSO Provider** panel opens.
5. Click the **Directory Services** dropdown and choose the provisioning method of the users you want to map.
6. Click the **Single Sign On Provider** dropdown and choose the provider to be used.
7. Click **Apply** and then click **Save**.

## Disabling an Identity Provider

You can disable an identity provider that is no longer needed in your account. After the identity provider is disabled, it cannot be used by users to sign into the Cato Client.

![Disable.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26186543457309.png)

**To disable an identity provider**

1. From the navigation menu, select **Access > Single Sign-On**.
2. Click on the identity provider you want to disable.
3. Turn the **Enabled** toggle to off.
4. Click **Apply** and then click **Save**.

## Understanding the User Experience

There is no impact on users if multiple identity providers are configured for your account. After a user enters their email address to sign in, the Client displays the sign-in page of the SSO provider mapped to the user.

## Known Limitations

- Supported for SCIM or manual user provisioning only
- Once configured, an IdP cannot be deleted.
  - An IdP can be disabled
