---
title: "Configuring ForgeRock SSO"
slug: "configuring-forgerock-sso"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-forgerock-sso"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring ForgeRock SSO

This article explains how to configure ForgeRock as the only Single Sign-On (SSO) provider for users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring ForgeRock as your SSO provider simplifies authentication and enhances the user experience. With SSO configured for your account, users can log in to the Cato Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

## Configuring ForgeRock as an SSO Provider

Follow these steps to configure ForgeRock as an SSO provider:

1. Add an OIDC Client in ForgeRock
2. Enter the details of your ForgerRock Host in the CMA

### Step 1: Add an OIDC Client in ForgeRock

In the ForgeRock admin console, add an OIDC client.

This procedure refers to the ForgeRock console, which is subject to change.

**To add Cato as a ForgeRock client:**

1. In ForgeRock, go to the Top Level Realm and under **Applications > OAuth 2.0 > Clients**, click **Add Client**.
2. In the **Core** tab, enter the basic settings, including a **Client secret**. You will need the **Client secret** to integrate with Cato later.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35887737718301.png)
3. In the **Redirect URIs** field, enter the following Cato URIs:

**For user SSO in the Client:**

**For admin SSO in the CMA:**
  - [https://sso.via.catonetworks.com/auth_results](https://sso.via.catonetworks.com/auth_results)
  - [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
  - h[ttps://sso.proxy.catonetworks.com/auth_results](https://sso.proxy.catonetworks.com/auth_results)
  - [https://auth.catonetworks.com/oauth2/broker/code/forgerock](https://auth.catonetworks.com/oauth2/broker/code/forgerock)
  - [https://auth.us1.catonetworks.com/oauth2/broker/code/forgerock](https://auth.us1.catonetworks.com/oauth2/broker/code/forgerock)
  - [https://auth.jp1.catonetworks.com/oauth2/broker/code/forgerock](https://auth.jp1.catonetworks.com/oauth2/broker/code/forgerock)
  - [https://auth.in1.catonetworks.com/oauth2/broker/code/forgerock](https://auth.in1.catonetworks.com/oauth2/broker/code/forgerock)
  - [https://auth.us1.catonetworks.com/endsession/](https://auth.us1.catonetworks.com/endsession/)
  - [https://auth.catonetworks.com/endsession/](https://auth.catonetworks.com/endsession/)
  - [https://auth.in1.catonetworks.com/endsession/](https://auth.in1.catonetworks.com/endsession/)
  - [https://auth.jp1.catonetworks.com/endsession/](https://auth.jp1.catonetworks.com/endsession/)
4. In the **Scopes** and **Default Scopes** fields, enter **email**, **openid**, and **profile**.
5. In the **Advanced** tab, under the **Token Endpoint Authentication Method** field, make sure **client_secret_post** is selected.
6. Click **Save** to create the ForgeRock client.

### Step 2: Configure ForgeRock as your SSO Provider

In the CMA, enter the details for your ForgeRock client you created in the previous step:

- Well-known URL
- Client ID
- Client Secret

![keycloak_cma_config.png](image/img-4b5443f56886d9ecc9acab3d71a4ec6c.png)

**To configure ForgeRock as your SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **ForgeRock**.
4. Enter a **Name** to identify this integration.
5. Enter your **Well-known URL** as follows:

**https://<AM_HOST>:<PORT>/<AM_DEPLOYMENT_URI>/oauth2/.well-known/openid-configuration?realm=<REALM_PATH>**
6. Enter the **Client ID** and **Client Secret** that were created in step 1.
7. If you are configuring one Single Sign-On provider, enable the Default toggle.

If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
8. Click **Apply**.
