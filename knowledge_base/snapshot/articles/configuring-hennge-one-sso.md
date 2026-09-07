---
title: "Configuring Hennge One SSO"
slug: "configuring-hennge-one-sso"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-hennge-one-sso"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Hennge One SSO

This article explains how to configure Hennge One as the Single Sign-On (SSO) provider for users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## Overview

Configuring Hennge One as the SSO provider simplifies authentication and enhances user experience. When you enable SSO for the account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

### Limitations

Due to how Hennge One implements OIDC, Revoke Session and Always Prompt features are not supported with Hennge One SSO

## Configuring Hennge One as an SSO Provider

Follow these steps to configure Hennge One as an SSO provider:

1. Add a new service with OIDC as a Connected Service in your Hennge One admin console
2. Enter the details of your Hennge host in the CMA

### Step 1: Add an OIDC Service in Hennge One

In the Hennge Connected Services, add an OIDC service. You will need the following values for the CMA in step 2:

- client ID
- client secret

This procedure refers to the Hennge console, which is subject to change. To read the latest Hennge documentation, see [their support site](https://support.hdeone.com/hc/en-us).

**To add Cato as a Hennge Connected Service:**

1. In Hennge Access Control, go to **System > Connected Services** and click **Add Service**.

![hennge_connected-service.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33550842112669.png)
2. In the **Service name** field, enter a descriptive name for the Cato connected service.
3. In the **Application URL** field, enter the Cato Networks URL, as follows:

https://sso.via.catonetworks.com/auth_results
4. In the **Redirect URI** field, enter *https://sso.proxy.catonetworks.com/auth_results*:
5. In the **Additional redirect URIs** field, enter the following:
  - https://sso.via.catonetworks.com/auth_results
  - https://sso.ias.catonetworks.com/auth_results
6. Under **Scopes**, make sure that **openid** and **email** are selected.
7. Click **Save** to create the Connected service.
8. Go to the **Connected services** area and click the service you just created.
9. In the upper right-hand corner, click **Metadata** and copy the **Client ID** and **Client Secret**. You will need these values when you create the SSO provider in the CMA.

![hennge-credentials.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33550831236765.png)

### Step 2: Configure Hennge One as your SSO Provider

In the CMA, enter the details for your Hennge One service you created in the previous step:

- Hennge Metadata URL should be provided in the Well Known URL field
- Client ID
- Client secret

The value for the Hennge URL is located in the Metadata page in the **Metadata URL** field.

Cato supports using [multiple IdPs for SSO](/v1/docs/configuring-multiple-identity-providers) for your account. Only the default SSO provider is used for CMA admins, make sure to define Hennge One as the **Default** authentication method.

![hennge_CMA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33550798813597.png)

**To configure Hennge One as your SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **Hennge**.
4. Enter a **Name** to identify this integration.
5. Enter your **Hennge URL** without the protocol prefix.
6. Enter the **Client ID** and **Client Secret** that were copied above.
7. Enable the **SDP** toggle to use Hennge as the only SSO provider for SDP users.
8. Click **Apply**.
