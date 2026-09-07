---
title: "Configuring CyberArk SSO for your Account"
slug: "configuring-cyberark-sso-for-your-account"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-cyberark-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring CyberArk SSO for your Account

This article explains how to configure CyberArk as the Single Sign-On (SSO) provider for users to authentication to the Cato Client.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring CyberArk as your SSO provider simplifies authentication and enhances the user experience. With SSO configured for your account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

### Limitations

CyberArk does not support headless authentication, meaning authentication with no UI.

## Configuring CyberArk as an SSO Provider

Follow these steps to configure CyberArk as an SSO provider:

1. Add Cato as an application in your CyberArk console
2. Enter the details of your CyberArk instance in the Cato Management Application
3. Configure the Token Validity

### Step 1: Add Cato as an OIDC Web APP

In your CyberArk instance, add Cato as a custom OIDC web application. The following procedure might change from time-to-time and you should check your [CyberArk documentation](https://docs.cyberark.com/identity/latest/en/content/applications/appscustom/openidaddconfigapp.htm?Highlight=create%20a%20custom%20OIDC%20web%20app) for exact details about creating an OIDC App in CyberArk.

![CyberArk-SSO_Trust.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28314269147677.png)

**To add Cato as an application:**

1. In the CyberArk Admin console, navigate to the **Apps and Widgets > Web Apps** page.
2. Click **Add Web Apps.**
3. In the Add Web Apps page, under the **Custom** tab, find the **OpenID Connect** app and click **Add**.
4. Under **Settings**, provide the following information and click **Save**:
  - In the **Application ID** field, enter the name of the App, and optionally provide a **Description**.
5. Under **Trust**, enter the following information and click **Save**:
  - Enter the password in the **OpenID Connect client secret** field
  - Under **Service Provider Configuration**, select **Login initiated by relying party (RP)**
  - Under **Authorized redirect URIs**, enter the following:
    - [https://sso.via.catonetworks.com/auth_results](https://sso.via.catonetworks.com/auth_results)
    - [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
    - [https://sso.proxy.catonetworks.com/auth_results](https://sso.proxy.catonetworks.com/auth_results)
6. Under **Permissions**, add all of the users to whom this app applies.
7. Click **Save**.

### Step 2: Configure CyberArk as your SSO Provider

In the Cato Management Application, enter the unique details for your CyberArk account.

![CMA-CyberArk.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28314269185949.png)

**To configure CyberArk as your SSO provider:**

1. In the Cato Management Application, from the Navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **CyberArk**.
4. Enter a **Name**.
5. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
6. From the CyberArk Admin console, from the App you created above, copy the OpenID Connect metadata URL and under **Authentication Details**, paste the value in the **CyberArk Well Known URL** field. This enables Cato to extract the necessary configuration information from CyberArk.
7. Copy the Client ID and Client Secret fields from the CyberArk Admin console and paste them in the **Client ID** and **Client Secret** fields, respectively.
8. Click **Apply**

### Step 3: Configure the Token Validity

You can configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

![Token_Valid.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28314283991197.png)

**To configure the token validity:**

1. On the **Access > Single Sign On** page, define the **Token validity** settings.
2. Click **Save**.
