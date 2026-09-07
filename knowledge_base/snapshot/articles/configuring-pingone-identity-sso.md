---
title: "Configuring PingOne Identity SSO"
slug: "configuring-pingone-identity-sso"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/configuring-pingone-identity-sso"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring PingOne Identity SSO

This article explains how to configure PingOne as the Single Sign-On (SSO) provider for users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Configuring PingOne as the SSO provider simplifies authentication and enhances user experience. When you enable SSO for the account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

## Configuring PingOne as an SSO Provider

Follow these steps to configure PingOne as an SSO Provider:

1. Create an OIDC application in the PingOne console
2. Configure the details in the Cato Management Application (CMA)
3. Configure how PingOne is used in your account

### Step 1: Creating an Application in the PingOne Console

In the PingOne console, create an application and identify the following values to enter into the CMA:

- OIDC Discovery Endpoint
- Client ID
- Client Secret

**To create an application:**

1. Sign in to your PingOne console.
2. In the environment you want use, navigate to **Applications > Applications**.
3. Click on the + symbol to create a new application.
4. Choose an **Application Name** and under **Application Type** choose **OIDC Web App**, and click **Save**.
5. Click on the Application you created, on the **Configuration** tab, click the pencil icon.
6. Configure the following:
  - **Response Type:** Check **Code**.
  - **Grant Type:** Check **Authorization Code** and in the **PKCE Enforcement** drop-down, select **Optional**.
  - Add the following **Redirect URIs**:
    - [https://auth.catonetworks.com/oauth2/broker/code/pingone](https://auth.catonetworks.com/oauth2/broker/code/pingone)
    - [https://auth.us1.catonetworks.com/oauth2/broker/code/pingone](https://auth.us1.catonetworks.com/oauth2/broker/code/pingone)
    - [https://auth.in1.catonetworks.com/oauth2/broker/code/pingone](https://auth.in1.catonetworks.com/oauth2/broker/code/pingone)
    - [https://auth.jp1.catonetworks.com/oauth2/broker/code/pingone](https://auth.jp1.catonetworks.com/oauth2/broker/code/pingone)
    - [https://auth.catonetworks.com/endsession/](https://auth.catonetworks.com/endsession/)
    - [https://auth.us1.catonetworks.com/endsession/](https://auth.us1.catonetworks.com/endsession/)
    - [https://auth.in1.catonetworks.com/endsession/](https://auth.in1.catonetworks.com/endsession/)
    - [https://auth.jp1.catonetworks.com/endsession/](https://auth.jp1.catonetworks.com/endsession/)
    - [https://sso.proxy.catonetworks.com/auth_results](http://https://sso.proxy.catonetworks.com/auth_results)
    - [https://sso.via.catonetworks.com/auth_results](https://sso.via.catonetworks.com/auth_results)
    - [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
7. Click **Save**.
8. Navigate to the **Attribute Mappings** tab and click the pencil icon.
9. Click **Add** and add an **Email** attribute with the PingOne Mapping **Email Address**.

![Ping1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35583708826781(1).png)
10. Click **Save**.
11. On the **Overview** tab, copy and save the **OIDC Discovery Endpoint** URL so it can be entered into the CMA.
12. On the **Configuration** tab, copy and save the **Client ID** and **Client Secret** so they can be entered into the CMA.

### Step 2: Configure PingOne as an SSO Provider

In the CMA, enter the details for the PingOne application you created in the previous step:

- OIDC Discovery Endpoint is the Well-Known URL
- Client ID
- Client secret

![Ping11.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35583713758365(1).png)

**To configure PingOne as an SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **Ping One**.
4. Enter a **Name** to identify this integration.
5. (Optional) To configure PingOne as your default SSO provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
6. Enter the **Well-Known URL** and **Client ID** you created in Step 1.
7. Click **Edit Client Secret** and enter the value you created in Step 1.
8. Click **Apply**.

### Step 3: Configure How PingOne is Used in your Account

You can choose to allow users, Cato Management Application admins, or both to authenticate with SSO using PingOne.

You can also configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![PingFederate2.png](https://support.catonetworks.com/hc/article_attachments/35583713818269)

**To configure how PingOne is used in your account:**

1. On the **Access > Single Sign On** page, define which users can authenticate with SSO and if necessary, define the **Token validity**, **Cookie type**, and **Duration** settings.
2. Click **Save**
