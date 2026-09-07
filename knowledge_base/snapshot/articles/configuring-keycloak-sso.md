---
title: "Configuring Keycloak SSO"
slug: "configuring-keycloak-sso"
updated: 2026-08-23T05:22:50Z
published: 2026-08-23T05:22:50Z
canonical: "knowledge.catonetworks.com/configuring-keycloak-sso"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Keycloak SSO

This article explains how to configure Keycloak as the only Single Sign-On (SSO) provider for SDP users and Cato Management Application (CMA) admins.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

You can configure Keycloak as the SSO provider to centralize authentication for both CMA admins and remote users connecting with the Cato Client. This integration improves account security and simplifies identity management by enforcing login through Keycloak credentials.

Make sure that the email address for each user and admin in Cato matches the corresponding email in Keycloak.

Once SSO is enabled, admins must authenticate through Keycloak to access the CMA, and both admins and users must authenticate through Keycloak to connect with the Cato Client.

## Configuring Keycloak as an SSO Provider

Follow these steps to configure Keycloak as an SSO provider:

1. Add Cato as a Keycloak client in your Keycloak admin console
2. Enter the details of your Keycloak Host in the CMA

### Step 1: Add Cato as a Keycloak Client

In the Keycloak admin console, add Cato as a client. Allowlist the Cato URIs as part of configuring Cato as a client. You will need these values for the CMA in step 2:

- client ID
- client secret

This procedure refers to the Keycloak console, which is subject to change. To read the latest Keycloak documentation, see [Managing Resource Servers](https://www.keycloak.org/docs/latest/authorization_services/index.html#_resource_server_overview).

**To add Cato as a Keycloak client:**

1. In Keycloak, go to **Clients > Create Client**.
2. In the **General settings** tab, enter the basic settings, including a client ID. You will need the client ID to integrate with Cato later.
3. In the **Capability config** tab, make sure **Client authentication** is enabled.

![keycloak_capability_config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30971045766429.png)
4. In the **Login settings** tab, enter the following Cato URIs in **Valid redirect URIs**:

![keyCloak_login_settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30971041745309.png)
  - https://sso.via.catonetworks.com/auth_results
  - https://sso.ias.catonetworks.com/auth_results
  - https://sso.proxy.catonetworks.com/auth_results
  - https://169.254.255.254/auth_results
  - https://auth.catonetworks.com/oauth2/broker/code/keycloak
  - https://auth.us1.catonetworks.com/oauth2/broker/code/keycloak
  - https://auth.catonetworks.com/endsession/*
  - https://auth.us1.catonetworks.com/endsession/*
5. Click **Save** to create the Keycloak client.
6. Go to the **Client** area and click the client you just created.
7. Go to the **Credentials** tab and copy the **Client Secret**. You will need this value when you create the SSO provider in the CMA.

![keycloak_client_secret.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30971045809821.png)

### Step 2: Configure Keycloak as your SSO Provider

In the CMA, enter the details for your Keycloak client you created in the previous step:

- Keycloak URL
- Client ID
- Client secret

The value for the Keycloak URL is the beginning of the URL until the end of the Realm name, without HTTPS.

For example, if the URL you use to get to Keycloak is **https://keycloak.example.com/realms/myRealm/.well-known/openid-configuration**, you would enter **keycloak.example.com/realms/myRealm** as your Keycloak URL.

Cato supports using [multiple IdPs for SSO](/v1/docs/configuring-multiple-identity-providers) for your account. Only the default SSO provider is used for CMA admins, make sure to define Keycloak as the **Default** authentication method.

![keycloak_cma_config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30971061429277.png)

**To configure Keycloak as your SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **Keycloak**.
4. Enter a **Name** to identify this integration.
5. Enter your **Keycloak URL** without the protocol prefix and only up until your realm name.
6. Enter the **Client ID** and **Client Secret** that were created in step 1.
7. Enable the **Default** toggle to use Keycloak as the only SSO provider for CMA admins.
8. Click **Apply**.

## Known Limitations

- Red Hat build of Keycloak is not supported for SSO
