---
title: "Configuring SecureAuth SSO"
slug: "configuring-secureauth-sso-for-your-account"
updated: 2026-08-02T12:32:16Z
published: 2026-08-02T12:32:16Z
canonical: "knowledge.catonetworks.com/configuring-secureauth-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring SecureAuth SSO

This article explains how to configure SecureAuth as the Single Sign-On (SSO) provider for users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring SecureAuth as the SSO provider simplifies authentication and enhances user experience. When you enable SSO for the account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

## Configuring SecureAuth as an SSO Provider

Follow these steps to configure SecureAuth as an SSO provider:

1. Step 1: Create an OIDC application in the SecureAuth Administration Portal
2. Step 2: Configure the details in the Cato Management Application (CMA)
3. Step 3: Configure how SecureAuth is used in your account

### Step 1: Creating an Application in the SecureAuth Administration Portal

In the SecureAuth Administration Portal, create an application through the process below, and identify the following values to enter into the CMA:

- Client ID
- Client Secret

**To create an application:**

1. In the SecureAuth admin portal, navigate to **Internal Application Manager** and click **Add New Internal Application Manager**.
2. Add an **Application Name** and **Application Description**.
3. Configure the following details:
  - **Data Store:** The data store you want to use to import your users from.
  - **Allow every group in your selected data stores to access this application:** Enter the Groups to have access or enable to allow every group in your selected data stores to access this application
  - **Authentication Policy:** The policy you want to use for this Realm
  - **Realm Number:** Any number on the list
  - **Authentication User Redirect:** Generic
  - **Generic (HTTP/OAuth/OPenID/etc):** OpenID Connect/OAuth2
4. Click **Create Connection**.
5. Click on the **Go to Advanced Settings to finish the configuration for this application** link.
6. On the **Post Authentication** tab, ensure **Email 1** is selected for the **User ID Mapping** field.
7. In the **OpenID Connect/OAuth 2.0 - Settings,** configure the following details:
  - **Enabled:** True
  - **Signing Cert:** Select a valid certificate
  - **Auto Accept User Consent:** True
  - **Enable User Consent:** True
8. In the **OpenID Connect/OAuth 2.0 - Scopes** section, click the **Discoverable** check box for these scopes:
  1. openid
  2. profile
  3. email
9. Click **Save**.
10. In the **OpenID Connect/OAuth 2.0 - Clients** section, click **Add Client**.
11. Configure the following details:
  - **Name:** Add a name for the Client
  - **Allowed Flows:**
    - **Implicit:** False
    - **Hybrid:** False
    - **Client Credentials:** False
12. In the **OpenID Connect/OAuth 2.0 - Client RedirectURIs** section, add these URIs:
  - [https://auth.catonetworks.com/oauth2/broker/code/secureauth](https://auth.catonetworks.com/oauth2/broker/code/secureauth)
  - [https://auth.us1.catonetworks.com/oauth2/broker/code/secureauth](https://auth.us1.catonetworks.com/oauth2/broker/code/secureauth)
  - [https://auth.in1.catonetworks.com/oauth2/broker/code/secureauth](https://auth.in1.catonetworks.com/oauth2/broker/code/secureauth)
  - [https://auth.jp1.catonetworks.com/oauth2/broker/code/secureauth](https://auth.jp1.catonetworks.com/oauth2/broker/code/secureauth)
  - [https://auth.catonetworks.com/endsession/](https://auth.catonetworks.com/endsession/)
  - [https://auth.us1.catonetworks.com/endsession/](https://auth.us1.catonetworks.com/endsession/)
  - [https://auth.in1.catonetworks.com/endsession/](https://auth.in1.catonetworks.com/endsession/)
  - [https://auth.jp1.catonetworks.com/endsession/](https://auth.jp1.catonetworks.com/endsession/)
  - [https://sso.proxy.catonetworks.com/auth_results](https://sso.proxy.catonetworks.com/auth_results)
  - [https://sso.via.catonetworks.com/auth_results](https://sso.via.catonetworks.com/auth_results)
  - [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
13. Click **Save**.
14. Copy and save the **Client ID** and **Client Secret** so they can be entered into the CMA.
15. Click **Back.**
16. In the **Open ID Connect Access / ID Token Claims** section, set the value for **sub** to **Email 1** and check the **Discoverable** checkbox.
17. Click **Save**.

### Step 2: Configure SecureAuth as an SSO Provider

In the CMA, enter the details for the SecureAuth application you created in the previous step.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(14).png)

**To configure SecureAuth as an SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **SecureAuth**.
4. Enter a **Name** to identify this integration.
5. (Optional) To configure SecureAuth as your default SSO provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
6. In the **Well-Known URL** field enter:
  - https://<your SecureAuth tenant name>.identity.secureauth.com/<realm name or number>/.well-known/openid-configuration **Note:** The Well-Known URL is case sensitive
7. Enter the **Client ID** you created in Step 1.
8. Click **Edit Client Secret** and enter the value you created in Step 1.
9. Click **Apply**.

### Step 3: Configure How SecureAuth is Used in your Account

You can choose to allow users authenticate with SSO using SecureAuth.

You can also configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![PingFederate2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35583699196445(1).png)

**To configure how SecureAuth is used in your account:**

1. On the **Access > Single Sign On** page, define which users can authenticate with SSO and if necessary, define the **Token validity**, **Cookie type**, and **Duration** settings.
2. Click **Save**
