---
title: "Configuring DUO SSO for Your Account"
slug: "configuring-duo-sso"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/configuring-duo-sso"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring DUO SSO for Your Account

This article explains how to configure Cisco DUO as the Single Sign-On (SSO) provider for users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring DUO as the SSO provider simplifies authentication and enhances user experience. When you enable SSO for the account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

## Configuring DUO as an SSO Provider

Follow these steps to configure DUO as an SSO provider:

1. Step 1: Create an OIDC application in the DUO Admin Panel
2. Step 2: Configure the details in the Cato Management Application (CMA)
3. Step 3: Configure how DUO is used in your account

### Step 1: Creating an Application in the DUO Admin Panel

In the DUO Admin Panel, create an application through the process below, and identify the following values to enter into the CMA:

- OIDC Discovery URL
- Client ID
- Client Secret

**To create an application:**

1. Log into your Duo Admin Panel.
2. Navigate to **Applications > Applications**.
3. Click **Add application**.
4. Search for OAuth OIDC application and select that option.
5. Add a name for the application and configure these details:
  - **User access** - Choose Enable for all users
  - **Grant Type** **(General tab)** - Check the Authorization Code check box
  - **Sign-in Redirect URLs** - Add these URLs:
    - [https://auth.catonetworks.com/oauth2/broker/code/duo](https://auth.catonetworks.com/oauth2/broker/code/duo)
    - [https://auth.us1.catonetworks.com/oauth2/broker/code/duo](https://auth.us1.catonetworks.com/oauth2/broker/code/duo)
    - [https://auth.in1.catonetworks.com/oauth2/broker/code/duo](https://auth.in1.catonetworks.com/oauth2/broker/code/duo)
    - [https://auth.jp1.catonetworks.com/oauth2/broker/code/duo](https://auth.jp1.catonetworks.com/oauth2/broker/code/duo)
    - [https://auth.catonetworks.com/endsession/](https://auth.catonetworks.com/endsession/)
    - [https://auth.us1.catonetworks.com/endsession/](https://auth.us1.catonetworks.com/endsession/)
    - [https://auth.in1.catonetworks.com/endsession/](https://auth.in1.catonetworks.com/endsession/)
    - [https://auth.jp1.catonetworks.com/endsession/](https://auth.jp1.catonetworks.com/endsession/)
    - [https://sso.via.catonetworks.com/auth_results](https://sso.via.catonetworks.com/auth_results)
    - [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
    - [https://sso.proxy.catonetworks.com/auth_results](https://sso.proxy.catonetworks.com/auth_results)
  - **Scopes & Claims > Scope Authorization** **(Access Policy tab)** - Add these scopes:

![Duo2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35583725210141(1).png)
    - openid
    - profile
    - email
  - **Public Client Registration** **(Clients tab)** - Add these scopes:

![Duo3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35583738234141(1).png)
    - openid
    - profile
    - email
6. Click **Save**.
7. In the **Metadata** section, copy and save the **OIDC Discovery URL** so it can be entered into the CMA.
8. In the **Static Client Registration** section, copy and save the **Client ID** and **Client Secret** so they can be entered into the CMA.

### Step 2: Configure DUO as an SSO Provider

In the CMA, enter the details for the DUO application you created in the previous step.

**To configure DUO as an SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **Duo**.
4. Enter a **Name** to identify this integration.
5. (Optional) To configure DUO as your default SSO provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
6. Enter the OIDC Discovery URL as the **Well-Known URL** and **Client ID** you created in Step 1.
7. Click **Edit Client Secret** and enter the value you created in Step 1.
8. Click **Apply**.

### Step 3: Configure How DUO is Used in your Account

You can choose to allow users, Cato Management Application admins, or both to authenticate with SSO using DUO.

You can also configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![PingFederate2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35583699196445(1).png)

**To configure how DUO is used in your account:**

1. On the **Access > Single Sign On** page, define which users can authenticate with SSO and if necessary, define the **Token validity**, **Cookie type**, and **Duration** settings.
2. Click **Save**
