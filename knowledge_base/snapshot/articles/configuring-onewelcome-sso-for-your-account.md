---
title: "Configuring OneWelcome SSO for your Account"
slug: "configuring-onewelcome-sso-for-your-account"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/configuring-onewelcome-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring OneWelcome SSO for your Account

This article explains how to configure OneWelcome as an Single Sign-On (SSO) provider for your account.

## Overview

Configuring OneWelcome as the SSO provider simplifies authentication and enhances user experience. When you enable SSO for the account, users can log in to the Client by authenticating with their SSO credentials and do not need a different set of dedicated credentials.

## Configuring OneWelcome as an SSO Provider

Follow these steps to configure OneWelcome as an SSO Provider:

1. Create an OIDC application in the OneWelcome console
2. Configure the details in the Cato Management Application (CMA)
3. Configure how OneWelcome is used in your account

### Step 1: Creating an Application in the OneWelcome Console

In the OneWelcome console, create a OIDC application, including these redirect URL. For more information, see the OneWelcome documentation.

- [https://sso.proxy.catonetworks.com/auth_results](http://https://sso.proxy.catonetworks.com/auth_results)
- [https://sso.via.catonetworks.com/auth_results](https://sso.via.catonetworks.com/auth_results)
- [https://sso.ias.catonetworks.com/auth_results](https://sso.ias.catonetworks.com/auth_results)
- [https://auth.catonetworks.com/oauth2/broker/code/onewelcome](https://auth.catonetworks.com/oauth2/broker/code/onewelcome)
- [https://auth.catonetworks.com/endsession/](https://auth.catonetworks.com/endsession/)
- [https://auth.us1.catonetworks.com/oauth2/broker/code/onewelcome](https://auth.us1.catonetworks.com/oauth2/broker/code/onewelcome)
- [https://auth.in1.catonetworks.com/oauth2/broker/code/onewelcome](https://auth.in1.catonetworks.com/oauth2/broker/code/onewelcome)
- [https://auth.jp1.catonetworks.com/oauth2/broker/code/onewelcome](https://auth.jp1.catonetworks.com/oauth2/broker/code/onewelcome)
- [https://auth.us1.catonetworks.com/endsession/](https://auth.us1.catonetworks.com/endsession/)
- [https://auth.in1.catonetworks.com/endsession/](https://auth.in1.catonetworks.com/endsession/)
- [https://auth.jp1.catonetworks.com/endsession/](https://auth.jp1.catonetworks.com/endsession/)

### Step 2: Configure OneWelcome as an SSO Provider

In the CMA, enter the details for the OneWelcome application you created in the previous step:

**To configure OneWelcome as an SSO provider:**

1. In the CMA, from the navigation menu, click **Access > Single Sign On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **OneWelcome**.
4. Enter a **Name** to identify this integration.
5. Add the details from the application you created in Step 1.
6. Click **Apply** then **Save**.

### Step 3: Configure How OneWelcome is Used in your Account

You can choose to allow users, Cato Management Application admins, or both to authenticate with SSO using OneWelcome.

You can also configure how long the [Cato authentication token](/v1/docs/sso-authentication-for-users-with-cato) is valid for. The **Token validity** settings define in Days or Hours the amount of time that users remain authenticated. Users that are logged in must re-authenticate when the duration you define in Days or Hours (since they last logged in) has been reached.

The **Always Prompt** options means that users must always authenticate to the Client.

![PingFederate2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36318795345693.png)

**To configure how OneWelcome is used in your account:**

1. On the **Access > Single Sign On** page, define which users can authenticate with SSO and if necessary, define the **Token validity**, **Cookie type**, and **Duration** settings.
2. Click **Save**
