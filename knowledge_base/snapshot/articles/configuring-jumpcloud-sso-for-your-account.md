---
title: "Configuring JumpCloud SSO for your Account"
slug: "configuring-jumpcloud-sso-for-your-account"
updated: 2026-07-27T14:17:00Z
published: 2026-07-27T14:17:00Z
canonical: "knowledge.catonetworks.com/configuring-jumpcloud-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring JumpCloud SSO for your Account

This article explains how to configure JumpCloud as the Single Sign-On (SSO) provider for users to authentication to the Cato Client.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring JumpCloud as your SSO provider simplifies authentication and enhances the user experience. With SSO configured for your account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

### Known Limitations

- Always prompt is not supported for the token validity
- Admin log in to the Cato Management Application is not supported

## Configuring JumpCloud as an SSO Provider

Follow these steps to configure JumpCloud as an SSO provider:

1. Add Cato as an application in your JumpCloud console
2. Enter the details of your JumpCloud Host in the Cato Management Application
3. Configure the Token Validity

### Step 1: Add Cato as an Application

In your JumpCloud console, add Cato as an application.

![JumpCloud.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33550807495453.png)

**To add Cato as an application:**

1. In the JumpCloud console, navigate to the **SSO Application** page.
2. Click **Add New Application**
3. Configure the JumpCloud application with these SSO settings:
  1. - Set **Manage Single Sign-On** to **Configure SSO with OIDC**.
    - Set the **Client Authentication Type** to **Client Secret Post**. For more information, see the [JumpCloud](https://jumpcloud.com/support/sso-with-oidc) SSO documentation.
4. Click **Add URI** and enter these URIs in as **Redirect URIs**:
  1. `https://sso.via.catonetworks.com/auth_results`

`https://sso.ias.catonetworks.com/auth_results`

`https://sso.proxy.catonetworks.com/auth_results`
5. Under **Login URL**, again enter `https://sso.ias.catonetworks.com/auth_results`
6. Configure the following **Attribute Mapping**:
  1. - Under **Standard Scopes**, select the **Email** checkbox.
    - Under **USER ATTRIBUTE MAPPING**:

      - In the Service Provider Attribute Name field, type `email`
      - In **JumpCloud Attribute Name**, select **email**
7. Click **Save**.

###

### Step 2: Configure JumpCloud as your SSO Provider

In the Cato Management Application, enter the unique details for your JumpCloud account.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(84).png)

**To configure JumpCloud as your SSO provider:**

1. In the Cato Management Application, from the Navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **JumpCloud**.
4. Enter a **Name**.
5. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
6. Enter the **Well-Known URL** for your region:
  - **US:** `https://oauth.id.jumpcloud.com/.well-known/openid-configuration`
  - **EU:** `https://oauth.id.eu.jumpcloud.com/.well-known/openid-configuration`
  - **IN:** `https://oauth.id.in.jumpcloud.com/.well-known/openid-configuration ` For more information, see the [Jumpcloud documentation](https://jumpcloud.com/support/sso-with-oidc).
7. Enter your **Client ID** and **Client Secret**.

This information is available from your JumpCloud console.
8. Click **Apply**

### Step 3: Configure the Token Validity

You can configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

![Token_Valid.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33550823275293.png)

**To configure the token validity:**

1. On the **Access > Single Sign On** page, define the **Token validity** settings.
2. Click **Save**.
