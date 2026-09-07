---
title: "Configuring SSO and the Subdomain for the Account"
slug: "configuring-sso-and-the-subdomain-for-the-account"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-sso-and-the-subdomain-for-the-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring SSO and the Subdomain for the Account

This article explains how to configure Single Sign-On (SSO) for users in your account and the subdomain for the Cato Management Application and the Browser Access.

## Overview of Single Sign-On Providers for the Account

The **Access > Single Sign-On** screen lets you choose one Single Sign-On (SSO) provider for your account. You can choose to use this SSO provider to authenticate users to Cato Clients, Browser Access, and admins to the Cato Management Application.

For a list of supported SSO providers, see [Single Sign-On](https://support.catonetworks.com/hc/en-us/sections/4963959594141-Single-Sign-On).

You can choose different SSO authentication settings for users in your account. You can let users only authenticate with the SSO provider, or only with the Cato user credentials, or you can let users choose to authenticate with either option.

For Cato Management Application admins, the SSO provider username (admin's email address) is used as part of the authentication process. Make sure that you use the same email address for the Cato Management Application admin and the SSO provider account.

You can configure multiple SSO providers for your account. For more information, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).

> [!NOTE]
> **Note:** You can choose different authentication settings for SDP users, clientless SDP, and for Cato Management Application admins, but they all use the same SSO provider.

### Using Single Sign-On with the Cato Management Application

For more about enabling SSO authentication for Cato Management Application admins, see [Configuring Authentication Settings for Administrators](/v1/docs/authenticating-admins).

### Customizing Subdomains for Your Account

You can create a custom subdomain for your account so that it's easy for the users to identify the login window for your company. The same subdomain is used for the Cato Management Application and the clientless SDP Portal. See below, [Configuring the Cato Subdomain](/docs/configuring-sso-and-the-subdomain-for-the-account#UUID-27b19ce4-82d3-24f0-6275-f324d593f825_N1633619011203) .

## Configuring the SSO Settings for the Cato Client

> [!NOTE]
> **Note:** Make sure that you configure the SSO app in Azure and Okta before you configure them as the SSO provider for your account. For more information, see:
> 
> - [Configuring Azure SSO for Your Account](/v1/docs/configuring-azure-sso-for-your-account)
> - [Configuring Okta SSO for Your Accoun](/v1/docs/configuring-okta-sso-for-your-account)t

Use the Single Sign-On window to configure the SSO provider to authenticate users for your account. You must have admin permissions to configure the SSO settings in Microsoft Azure and Okta. For more about configuring Azure and Okta SSO, see the relevant Microsoft and Okta documentation.

When you disable Single-Sign-On, then users can only authenticate with Cato user credentials.

You can choose to configure which domains are allowed to authenticate with SSO. Restricting access based on specific domains provides increased security for your account.

As a best security practice, we recommend that the duration for the SSO Token validity is set to a maximum of 30 days. For more about SSO session behavior, see [SSO Session Behavior for Windows SDP Client](/v1/docs/sso-session-behavior-for-windows-sdp-client).

### Using SSO with Always Prompt

For additional security, you can enable the Always Prompt feature, so that the end-users are always required authenticate to the IdP when they connect to the Cato Cloud. This also includes when they are disconnected from the Cato Cloud, for example, the Client moves from one PoP to another.

Configure the maximum amount of time that a device is allowed to be continuously connected to the Cato Cloud before the end-user is forced to re-authenticate. When Always Prompt is enabled, when the end-user disconnects, and connects again, they have the full time duration before they are forced to authenticate.

> [!NOTE]
> **Note:** When disconnecting, there is a two minute grace period where the end-user remains authenticated, if they reconnect to the Cato Cloud.

![SSO_and_Always_Prompt.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218217516701.png)

## Configuring the Single Sign-On Provider for Your Account

### Important

Important: Make sure that you configure the SSO app in Azure and Okta before you configure them as the SSO provider for your account. For more information, see:

- [Configuring Azure SSO for Your Account](/v1/docs/configuring-azure-sso-for-your-account)
- [Configuring Okta SSO for Your Account](/v1/docs/configuring-okta-sso-for-your-account)

Use the **Single Sign-On** window to configure the SSO provider to authenticate users for your account. You must have admin permissions to configure the SSO settings in Microsoft Azure and Okta. For more about configuring Azure and Okta SSO, see the relevant Microsoft and Okta documentation.

When you disable Single-Sign-On, then users can only authenticate with Cato user credentials.

You can choose to configure which domains are allowed to authenticate with SSO. Restricting access based on specific domains provides increased security for your account.

![SSO_Azure.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218217583645.png)

**To configure the SSO provider settings for the account:**

1. From the navigation menu, select **Access > Single Sign-On**.
2. Click **New**.

Continue with one of the SSO provider settings. For more information, see [Single Sign-On](https://support.catonetworks.com/hc/en-us/sections/4963959594141-Single-Sign-On).
3. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
4. Click **Apply**.
5. Select **Allow login with Single Sign-On** for one or more types of users in your account:
  - SDP Client users (set the **Token validity** settings)
  - Clientless SDP users (set the Cookie type)
  - Cato Management Application admins
6. Click **Save**. The SSO settings are configured for your account.

## Configuring the Cato Subdomain

Use the **Single Sign On** window to configure the subdomain for the Cato Management Application and the clientless SDP Portal. You can also see the URL for each login window.

The Cato subdomain doesn't support Top Level Domains (TLDs) such as sample.com. You can use letters and numbers in the subdomain. Dashes are valid **only when the account is first created** (the subdomain initially matches the account name). If you later attempt to edit the subdomain, dashes are no longer allowed, and you'll receive an error message.

![cato_subdomain.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218203861149.png)

> [!NOTE]
> **Note:** When you change the subdomain for the account, all logins to the Cato Management Application and the SDP User Portal must use the new subdomain.

**To configure the subdomain for the account:**

1. From the navigation menu, click **Access > Single Sign-On**.
2. In the **Cato Subdomain** section, enter the **Subdomain** for the account.
3. Click **Save**.

### Logging in to a Subdomain in the Cato Management Application

Admins can log in to the Cato Management Application using the URL that includes the subdomain for your account, `https:/&lt;subdomain&gt;.cc.catonetworks.com`.

If admins log in with the URL `https://cc.catonetworks.com`, then there is an extra window to identify the subdomain.

**To log in to the Cato Management Application with a subdomain:**

1. From an Internet browser, go to the Cato Management Application `https:/&lt;subdomain&gt;.cc.catonetworks.com`.

The screenshot below shows the URL for the subdomain **sample**.

![CC2_login2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218203962269.png)
2. In the login window, enter the username and password.
3. Click **Log In**.

The Cato Management Application opens with the subdomain.
