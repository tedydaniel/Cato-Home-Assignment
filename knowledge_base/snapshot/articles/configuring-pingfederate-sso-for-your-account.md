---
title: "Configuring PingFederate SSO for your Account"
slug: "configuring-pingfederate-sso-for-your-account"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-pingfederate-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring PingFederate SSO for your Account

This article explains how to configure PingFederate as the Single Sign-On (SSO) provider for users and Cato Management Application admins.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring PingFederate as your SSO provider simplifies authentication and enhances the user experience. With SSO configured for your account, users can log in to the Client and admins can log into the Cato Management Application by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

For information about configuring PingOne SSO, see [Configuring Ping Identity SSO (PingOne)](/v1/docs/configuring-pingone-identity-sso).

## Configuring PingFederate as an SSO Provider

Follow these steps to configure PingFederate as an SSO provider:

1. Add Cato as an OAuth Client in your PingFederate admin console
2. Enter the details of your PingFederate Host in the Cato Management Application
3. Configure which users can authenticate with SSO and the token validity

### Step 1: Add Cato as an OAuth Client

In your PingFederate admin console, add Cato as an OAuth Client.

![Admin_Console.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345708870685.png)

**To add Cato as an OAuth Client:**

1. In the PingFederate admin console, on the **Applications** tab, click **OAuth Clients**.
2. Click **Add Client**
3. Enter a **Client ID**, **Name**
4. Select and define a **Client Secret**.
5. In **Redirect URI's**, enter these URIs:

![URIs.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345672505501.png)
  - https://sso.via.cato networks.com/auth_results
  - https://sso.ias.catonetworks.com/auth_results
  - https://sso.proxy.catonetworks.com/auth_results
  - https://169.254.255.254/auth_results
  - https://auth.catonetworks.com/oauth2/broker/code/pingfederate
  - https://auth.us1.catonetworks.com/oauth2/broker/code/pingfederate
  - https://auth.in1.catonetworks.com/oauth2/broker/code/pingfederate
  - https://auth.jp1.catonetworks.com/oauth2/broker/code/pingfederate
6. Click **Save**.
7. From the navigation menu, click **OpenID Connect Policy Management**.
8. Click **Add Policy**.
9. Choose a **Policy ID** and **Name**
10. Select an **Access Token Manager**.

![PF2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345697207581.png)
11. Select the **Include user info in ID token** checkbox.
12. Click **Next** and then **Save**.

### Step 2: Configure PingFederate as your SSO Provider

In the Cato Management Application, enter the unique details for your PingFederate account.

![PingFederate.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345709152541.png)

**To configure PingFederate as your SSO provider:**

1. In the Cato Management Application, from the Navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **PingFederate**.
4. Enter a **Name**.
5. Enter your PingFederate **Host** that was used when you installed the PingFederate server.

**Note:** If required, you can specify a specific port using the format, `ping-federate.example.com:9310`.
6. Enter the **Client ID** and **Client Secret** that was created at Step 1.
7. (Optional) If required, enter the **Additional Authorization Parameters**.

Use the syntax key=value&amp;key=value.
8. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
9. Click **Apply**.

### Step 3: Configure How PingFederate is Used in your Account

You can choose to allow users, Cato Management Application admins, or both to authenticate with SSO using PingFederate.

You can also configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![PingFederate2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26345709234461.png)

**To configure how PingFederate is used in your account:**

1. On the **Access > Single Sign On** page, define the **Token validity** settings.
2. Choose which users can authenticate with SSO.
3. Click **Save**.
