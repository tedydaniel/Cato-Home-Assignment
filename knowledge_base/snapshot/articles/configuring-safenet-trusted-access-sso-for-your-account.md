---
title: "Configuring SafeNet Trusted Access SSO for your Account"
slug: "configuring-safenet-trusted-access-sso-for-your-account"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-safenet-trusted-access-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring SafeNet Trusted Access SSO for your Account

This article explains how to configure SafeNet Trusted Access as the Single Sign-On (SSO) provider for users to authenticate to the Cato Client.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring SafeNet Trusted Access as your SSO provider simplifies authentication and enhances the user experience. With SSO configured for your account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials. For more information, see the SafeNet Trusted Access [documentation](https://resources.eu.safenetid.com/help/CATO_NETWORKS_1/CATO_NETWORKS_Help/CATO_NETWORKS_Help/Index.htm).

### Known Limitations

- Admin log in to the Cato Management Application is not supported

## Configuring SafeNet Trusted Access as an SSO Provider

Follow these steps to configure SafeNet Trusted Access as an SSO provider:

1. Add Cato as an application in your STA Access Management console
2. Enter the details of your SafeNet Trusted Access Host in the Cato Management Application
3. Configure the token validity

### Step 1: Add Cato as an Application

In your STA Access Management console, add Cato as an application.

![Safenet9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345709322269.png)

**To add Cato as an application:**

1. In the STA Access Management console, on the Applications page, click Add Application.
2. Select Generic Template.

![Add_App.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345681471133.png)
3. Choose **OCID** as the Integration Protocol.
4. (Optional) Change the display name of the application.
5. Click **Next**.
6. On the **Configure** tab, in the **STA Setup** section, enter this URL as the Service Login URL:

`https://sso.via.catonetworks.com/login`
7. Enter these URLs in as **Valid Redirect URLs**:

`https://sso.via.catonetworks.com/auth_results`

`https://sso.ias.catonetworks.com/auth_results`

`https://sso.proxy.catonetworks.com/auth_results`
8. On the **Assign** tab, choose the users that will use SafeNet SSO.
9. Click **Save**.

### Step 2: Configure SafeNet Trusted Access as your SSO Provider

In the Cato Management Application, enter the unique details for your SafeNet Trusted Access account.

![Safenet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345709546397.png)

**To configure SafeNet Trusted Access as your SSO provider:**

1. In the Cato Management Application, from the Navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **SafeNet**.
4. Enter a **Name**.
5. Select your **Zone** and enter your **Client ID**, **Tenant ID**, and **Client Secret**.

The **Client ID** and **Client Secret** information is available from the Configure tab in your STA Access Management console.
6. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
7. Click **Apply**.

### Step 3: Configure the Token Validity

You can configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![Token_Valid.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345697880733.png)

**To configure the token validity:**

1. On the **Access > Single Sign On** page, define the **Token validity** settings.
2. Click **Save**.
