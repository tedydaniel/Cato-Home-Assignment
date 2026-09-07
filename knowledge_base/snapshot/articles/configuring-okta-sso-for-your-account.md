---
title: "Configuring Okta SSO for Your Account"
slug: "configuring-okta-sso-for-your-account"
updated: 2026-08-13T08:52:03Z
published: 2026-08-16T13:00:00Z
canonical: "knowledge.catonetworks.com/configuring-okta-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Okta SSO for Your Account

This article explains how to configure Okta as the Single Sign-On (SSO) provider for SDP users, clientless users, and Cato Management Application admins in your account.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

For more about enabling SSO for the account, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

## Overview of SSO with Your Cato Account

After a chain of trust is established between Cato, the IdP, and your company's user directory, Cato trusts the IdP for user authentication.

Cato SSO supports these Client operating systems:

- Windows
- macOS
- iOS
- Android
- Linux

## Supported Features

Okta SSO with Cato Networks supports the Service Provider Initiated Authentication Flow. This authentication flow occurs when:

- The user attempts to log in to the [Application Portal](/v1/docs/customizing-browser-application-portal) .
- The user attempts to log in to the [Cato Client](https://support.catonetworks.com/hc/en-us/sections/4963933250461-Cato-SDP-Clients).

## Preparing to Configure SSO with Okta

Before you establish trust with Okta, make sure that you complete these prerequisites:

- You must have administrator privileges to Okta
- Okta must be synchronized with your user directory.
- For manually created SDP users, SSO is supported for Windows v5.x, macOS v5.x, and Linux v5.x Clients
  - For iOS and Android, only users who were imported from your organization to Cato using Directory Services or SCIM provisioning are able to use SSO.

### Known Limitations

- On macOS devices, if the token expires and the device restarts, the Client does not re-authenticate automatically. The user must manually enter their password to re-authenticate.

## Configuring Okta as the SSO Provider

Add the Okta app for Cato Networks SSO, and then configure your Okta Client ID and Client secret. Then configure the Cato Management Application to use Okta as the SSO provider for your account.

For SDP Client users, when you configure the Token validity settings you define in **Days** or **Hours** the amount of time that users remain authenticated. Users that are logged in must reauthenticate when the duration you define in **Days** or **Hours** (since they last logged in) has been reached. The **Always Prompt** options means that users must always authenticate to the Client.

**To configure Okta as the SSO provider for your account:**

1. Enable the admin permissions for your Okta account, from the Okta portal menu bar click **Admin**.
2. From the Okta **Applications** window, click **Browse App Catalog** and search for **Cato Portal**.
3. Click **Add Integration**.
4. In the **Add Cato Portal** window, select **Do not display application icon to users**:
5. Click **Done**.
6. In the **Assignments** tab, assign the People and Groups to the application.
7. Click **Assign**.
8. The **Sign On > Settings** window, shows the **Client ID** and the **Client secret** for your Okta account.

![Okta3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28728189939741.png)

Keep this window open, you need to copy the Client ID and Client secret to the Cato Management Application.
9. Click **Save**. Okta is configured as an SSO provider for your Cato account.
10. In a new tab or window, open the Cato Management Application.
11. From the navigation menu, select **Access > Single Sign-On**.
12. Click **New**.
13. From the **Identity Provider** drop-down menu, select **Okta**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(175).png)
14. Enter a **Name**.
15. In the **Well-Known URL** field enter `https://&lt;your tenant URL&gt;/.well-known/openid-configuration` . For example, if your Okta tenant URL is https://exmple.okta.com, in the **Well-Known URL** field, enter `https://example.okta.com/.well-known/openin-configuration` .
16. From the Okta window, copy these settings and paste them in the Cato Management Application:
  - Client ID
  - Client Secret
17. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
18. Click **Apply**.
19. Select **Allow login with Single Sign-On** for one or more types of users in your account:
  - SDP Client users (set the **Token validity** settings)
  - Clientless SDP users (set the Cookie type)
  - Cato Management Application admins
20. Click **Save**. Okta is configured as the SSO provider for your account.

## Using SSO for the Browser Access Portal

When you log in to the Browser Access Portal, choose to connect with **Okta** and then enter your Okta credentials. After you successfully log in to Okta, you are redirected to the Browser Access Portal and can select an application from the portal.

To log in to the Browser Access Portal using SSO, you must [allow access](/v1/docs/configuring-the-browser-access-portal) to the SSO domain.
