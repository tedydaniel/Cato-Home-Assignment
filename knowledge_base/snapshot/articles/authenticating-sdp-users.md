---
title: "Authenticating SDP Users"
slug: "authenticating-sdp-users"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/authenticating-sdp-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticating SDP Users

Once you added (or synced) the SDP users and groups to your account, you can then determine how they will authenticate and be allowed to access the network. The different authentication options let you meet the security requirements of your also organization while at the same time providing the best experience for the end-users.

## Overview of Cato's User Authentication

Some of the authentication options and settings are controlled in the Cato Management Application (CMA) and Cato [Cato User Portal](/v1/docs/managing-sdp-clients-with-the-cato-user-portal). For Single Sign-On (SSO), the user data and passwords are managed in the Identity Provider (IdP) portal or console, and the SSO token behavior is configured in the CMA.

These are the different authentication methods that Cato supports for end-users to connect to the Cato Cloud:

- Authentication options managed in the CMA and User Portal:
  - Password
  - Multi-Factor Authentication (MFA)
- Authentication option managed in the CMA:
  - Registration Code
- Authentication options managed in the CMA and IdP:
  - SSO

### Best Practices for User Authentication

We recommend that you use SSO with an IdP with MFA to authenticate users. This provides consistent security, compliance, and can lower IT costs.

## Understanding Cato's Authentication Methods

This section explains the different authentication methods you can use for SDP users.

### Authenticating with Passwords

Users managed in the CMA can authenticate with a password that authenticates to the Cato Cloud. They create their own passwords and can reset the password in the User Portal. Admins can also reset the password from the CMA.

When the user attempts to connect with the Client, they must enter their password into the Client to authenticate and then connect to the network.

For more about authenticating with passwords, see [Working with Users](/v1/docs/working-with-users).

### Authenticating with MFA

You can choose to require a second authentication factor for users managed in the CMA, and enable MFA for the entire account or for specific users. Cato supports these MFA methods:

- Authentication app that generates temporary codes (such as Google Authenticator)
- SMS codes

You can configure your account to support one or both methods. For accounts that support both methods, users log in to the User Portal and select the MFA method.

When the user attempts to connect with the Client, they must authenticate with their password and then enter the MFA code in the Client.

For more about using MFA, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients).

### Authenticating with Registration Codes

You can use the CMA to generate a CSV file with codes that are used to authenticate to the Client. After a user successfully authenticates with the code, they are not required to authenticate again.

For more about using registration codes, see [Activating Users with a Registration Code](/v1/docs/activating-users-with-a-registration-code).

### Authentication with SSO

Cato supports user authentication using OIDC to enable seamless SSO with your existing Identity Provider (IdP) authentication mechanism. Additionally, you can leverage MFA capabilities of SSO providers to enhance the security of user authentication.

Supporting SSO provides you with greater security and compliance, consistent user authentication, improved usability and satisfaction and lower IT costs. OIDC offers simplicity and is increasingly becoming popular for user authentication in modern applications.

For a list of supported SSO providers and configuring SSO, see the articles in the [Single Sign-On](/v1/docs/single-sign-on) section.

For more about IdPs and Cato, see: [Using an Identity Provider for Your Cato Account](/v1/docs/using-an-identity-provider-for-your-cato-account).
