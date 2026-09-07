---
title: "Configuring DTS Identity SSO for your Account"
slug: "configuring-dts-identity-sso-for-your-account"
updated: 2026-07-15T08:25:28Z
published: 2026-07-15T08:25:28Z
canonical: "knowledge.catonetworks.com/configuring-dts-identity-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring DTS Identity SSO for your Account

This article explains how to configure DTS Identity as the Single Sign-On (SSO) provider for users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring DTS Identity as the SSO provider simplifies authentication and enhances user experience. When you enable SSO for the account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

## Configuring DTS Identity as an SSO Provider

Follow these steps to configure DTS Identity as an SSO Provider:

1. Create an OIDC application in the DTS Identity console
2. Configure the details in the Cato Management Application (CMA)
3. Configure how DTS Identity is used in your account

### Step 1: Creating an Application in the DTS Identity Console

In the DTS Identity console, create an application and identify the following values to enter into the CMA:

- OIDC config
- Client ID
- Client Secret

**Note:** Only users assigned to the application in the DTS Identity console can authenticate with SSO.

**To create an application:**

1. In the DTS Admin Console, navigate to **Applications**.
2. Click **Create Custom App**.

![DTS.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36170769991069(1).png)
3. Add an **Application name** choose **Web Application**.
4. Click **Create Application**.
5. On the **OIDC / OAuth** tab, in the **Client credentials** section, set the **Token endpoint auth method** to **Client Secret (Post)**.

![DTS_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36170741738909(1).png)
6. In the **Login** section, add these URIs to the **Sign-in redirect URIs** field:
  - https://auth.catonetworks.com/oauth2/broker/code/dts
  - https://auth.us1.catonetworks.com/oauth2/broker/code/dts
  - https://auth.in1.catonetworks.com/oauth2/broker/code/dts
  - https://auth.jp1.catonetworks.com/oauth2/broker/code/dts
  - https://auth.catonetworks.com/endsession/
  - https://auth.us1.catonetworks.com/endsession/
  - https://auth.in1.catonetworks.com/endsession/
  - https://auth.jp1.catonetworks.com/endsession/
  - https://sso.proxy.catonetworks.com/auth_results
  - https://sso.via.catonetworks.com/auth_results
  - https://sso.ias.catonetworks.com/auth_results
7. Copy and save the **Client ID**, **Client Secret**, and **OIDC config** so they can be entered into the CMA.
8. Click **Save changes**.

### Step 2: Configure DTS as an SSO Provider

In the CMA, enter the details for the DTS application you created in the previous step:

- OIDC config is the Well-Known URL
- Client ID
- Client Secret

![DTS3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36170741809693(1).png)

**To configure DTS and an SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. Enter a **Name** to identify this integration.
4. (Optional) To configure DTS as your default SSO provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
5. Enter the **Well-Known URL** and **Client ID** you created in Step 1.
6. Click **Edit Client Secret** and enter the value you created in Step 1.
7. Click **Apply**.

### Step 3: Configure How DTS is Used in your Account

You can choose to allow users, Cato Management Application admins, or both to authenticate with SSO using DTS.

You can also configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![PingFederate2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36170754903069(1).png)

**To configure how DTS is used in your account:**

1. On the **Access > Single Sign On** page, define which users can authenticate with SSO and if necessary, define the **Token validity**, **Cookie type**, and **Duration** settings.
2. Click **Save**

## Known Limitations

- For authentication with the Embedded Browser, DTS Identity is supported only from Windows Client v6.7 and higher. For authentication with the external browser, there is no limitation. For more information, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients).
- Reauthentication is not supported for DTS Identity versions lower than version 5.
