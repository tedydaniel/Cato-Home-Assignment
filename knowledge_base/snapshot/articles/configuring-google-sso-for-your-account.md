---
title: "Configuring Google SSO for Your Account"
slug: "configuring-google-sso-for-your-account"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-google-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Google SSO for Your Account

This article explains how to use configure Google to provide Single Sign-On (SSO) for your Cato account.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

For more about enabling SSO for the account, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

## Overview of SSO with Cato

You can configure Google as an Identity Provider (IdP) to use SSO to authenticate users with the Cato Management Application and the Cato Client. The users can then use the IdP credentials to authenticate to the Cato Management Application or to the Client.

The **Single-Sign On** section in the Cato Management Application highlights each Client OS that supports SSO.

> [!NOTE]
> ### **Note:** Google as an IdP doesn't support LDAP sync and User Directory features such as only syncing specific groups. All users are enabled for SSO with Google as an IdP.
> 
> SSO with Google is supported with LDAP imported users when they use the same email as in Google Idp.

## Configuring Google as an SSO Provider

Configure the Cato settings for the account to use Google as the IdP for SSO. You don't need to make any changes to the settings for your Google account.

For SSO with SDP users, you must configure **User Provisioning** to NOT send invitation emails to new users that you create in the Cato Management Application. Otherwise, the SDP users need to use the invitation email to activate their account before they can use Google SSO.

In the **SDP Client users** section, use the following **Token validity** settings to define the amount of time the SSO token is valid for before the user needs to authenticate again:

- **Always Prompt** - SSO is always required whenever the user connects.
- **Duration** - Users do not require SSO for the duration you define in **Days** or **Hours**. Users that are logged in must be reauthenticated when the defined time duration expires.

![Google_SSO.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218233939485.png)

**To configure Google as an SSO provider for your Cato account:**

1. From the navigation menu, select **Access > Single Sign-On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **Google**.
4. Enter a **Name** .
5. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
6. Click **Apply**
7. 
  - SDP Client users (set the **Token validity** settings)
  - Clientless SDP users (set the Cookie type)
  - Cato Management Application admins

Select **Allow login with Single Sign-On** for one or more types of users in your account:
8. Click **Save**. Google is configured as the SSO provider for your Cato account.
