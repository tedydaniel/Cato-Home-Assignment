---
title: "Configuring RSA SSO"
slug: "configuring-rsa-sso"
updated: 2026-08-02T12:33:52Z
published: 2026-08-02T12:33:52Z
canonical: "knowledge.catonetworks.com/configuring-rsa-sso"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring RSA SSO

This article explains how to configure RSA as the Single Sign-On (SSO) provider for users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

### 

## Overview

Configuring RSA as the SSO provider simplifies authentication and enhances user experience. When you enable SSO for the account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

## Configuring RSA as an SSO Provider

Follow these steps to configure RSA as an SSO provider:

1. Create an OIDC application in the RSA Administration Console
2. Configure the details in the Cato Management Application (CMA)
3. Configure how RSA is used in your account

### Step 1: Creating an Application in the RSA Administration Console

In the RSA Administration Console, create an application and identify the following values to enter into the CMA:

- Authorization Server Issuer URL
- Client ID
- Client Secret

**To create an application:**

1. Log in to your RSA Administration Console.
2. Navigate to **Access > OIDC Settings**.
3. Enter these details:
  - **Claim Name:** email
  - **Source:** Identity Source
  - **Property:** mail
  - **Type:** default
4. Click on the plus then **Save Settings**.
5. On the **Scopes** tab create these scopes:
  - email
  - openid
  - profile
6. Click **Save Settings**.
7. On the **Application** tab, click **Add an Application** then click **Create From Template**.
8. Select **OIDC**.
9. Add a name for the application.
10. On the **Connection Profile** tab, add these details:
  - **Connection URL**: [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
  - **Redirect URI:**
    - [https://auth.catonetworks.com/oauth2/broker/code/rsa](https://auth.catonetworks.com/oauth2/broker/code/rsa)
    - [https://auth.us1.catonetworks.com/oauth2/broker/code/rsa](https://auth.us1.catonetworks.com/oauth2/broker/code/rsa)
    - [https://auth.in1.catonetworks.com/oauth2/broker/code/rsa](https://auth.in1.catonetworks.com/oauth2/broker/code/rsa)
    - [https://auth.jp1.catonetworks.com/oauth2/broker/code/rsa](https://auth.jp1.catonetworks.com/oauth2/broker/code/rsa)
    - [https://auth.catonetworks.com/endsession/](https://auth.catonetworks.com/endsession/)
    - [https://auth.us1.catonetworks.com/endsession/](https://auth.us1.catonetworks.com/endsession/)
    - [https://auth.in1.catonetworks.com/endsession/](https://auth.in1.catonetworks.com/endsession/)
    - [https://auth.jp1.catonetworks.com/endsession/](https://auth.jp1.catonetworks.com/endsession/)
    - [https://sso.via.catonetworks.com/auth_results](https://sso.via.catonetworks.com/auth_results)
    - [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
    - [https://sso.proxy.catonetworks.com/auth_results](https://sso.proxy.catonetworks.com/auth_results)
  - **Client Authentication Method:** CLIENT_SECRET_POST
  - **Scopes:**
    - openID
    - profile
    - email
  - **Claims:**
    - email
11. Copy and save the **Authorization Server Issuer URL** so it can be entered into the CMA.
12. Choose a **Client ID** and copy and save it so it can be entered into the CMA.
13. Under Authorization Code Flow, click **Generate** and copy and save the **Client Secret** so it can be entered into the CMA.
14. In the **Allow CORS Authentication** section, enable the **Participate in Unified Logout** and **Include Session Identifier** toggles.
15. In the **Relying Party Logout URL** field add: `https://auth.sta.catonet.works/endsession`
16. In the **Logout Redirect URIs** field, add: `https://auth.sta.catonet.works/endsession/callback`
17. On the **Portal Display** tab, click **Save and Finish**.
18. Navigate to **Access > My Page**.
19. Set the **Applications** toggle to **Enabled**.

### Step 2: Configure RSA as an SSO Provider

In the CMA, enter the details for the RSA application you created in the previous step:

- Authorization Server Issuer URL is the Well-Known URL
- Client ID
- Client secret

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(16).png)

**To configure RSA as an SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **RSA**.
4. Enter a **Name** to identify this integration.
5. (Optional) To configure RSA as your default SSO provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers-1).
6. Enter the **Well-Known URL** and **Client ID** you created in Step 1.
7. Click **Edit Client Secret** and enter the value you created in Step 1.
8. Click **Apply**.

### Step 3: Configure How RSA is Used in your Account

You can choose to allow users, Cato Management Application admins, or both to authenticate with SSO using RSA.

You can also configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(17).png)

**To configure how RSA is used in your account:**

1. On the **Access > Single Sign On** page, define which users can authenticate with SSO and if necessary, define the **Token validity**, **Cookie type**, and **Duration** settings.
2. Click **Save**.
