---
title: "Signing In to the Cato Client"
slug: "signing-in-to-the-cato-client"
updated: 2026-08-03T10:35:54Z
published: 2026-08-03T10:35:54Z
canonical: "knowledge.catonetworks.com/signing-in-to-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Signing In to the Cato Client

The Cato Client is installed on a users device to provide remote access to your network. This article explains how users sign in to the Cato Client to connect to your network.

## Overview

The Cato Client is proprietary software that authenticates and identifies remote users, grants access, and inspects traffic based on security policies. A user must be created in the Cato Management Application and signed in to the Cato Client to benefit from these features. Users can sign in to the Client with their configured authentication method and remain signed in for the duration of the token validity period. For more information, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients).

To sign in with an email address and password (and optional MFA), users create their password during the sign in process. Users on headless Linux devices must be sent an [activation email](/v1/docs/adding-users-to-your-cato-account) to create their password.

To sign in with SSO, the Client displays a browser (either in the Client or an external browser) so the user can enter their IdP login credentials.

### Prerequisites

- Cato Client is installed on a device. For more information, see [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client)
- User is created in the Cato Management Application. For more information see [Adding Users to Your Cato Account](/v1/docs/adding-users-to-your-cato-account)

### Known Limitations

- If your userID is your First Name and Last name and multiple users are created with the same email address that authenticate with email and password (and MFA):
  - The more recently created user cannot set their password when signing into the Client
  - To set the password of the user, an admin must resend an [Activation Email](/v1/docs/working-with-users)

## Signing in with Email and Password (and MFA)

Users can sign in to the Cato Client using their email address and a password that they create. For additional security, you can also include MFA.

![Client.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218260603165.png)

**To sign in to with email and password (and MFA):**

1. In the Cato Client, click **Connect**.

![Click_Connect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218254931741.png)
2. Enter your email address and click **Continue**.

![Email.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218269547933.png)
3. Click **Send Email**.

![Send_emial.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218255108637.png)

An email is sent with instructions on how to create your password.
4. In the email, click the link and create your password and if required your MFA configuration.

![Password.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218260902045.png)
5. In the Cato Client, click **Sign in** and enter your email address and password.

![Sign_in.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218289477021.png)

## Signing in with SSO

Users can sign in to the Cato Client using SSO. Your IdP acts as the authentication system to validate the user credentials. For more information, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

![SSO.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218261017629.png)

The above screenshot is for Azure SSO. The sign in page of the SSO provider configured for your account is displayed to your users.

**To sign in with SSO:**

1. In the Cato Client, click **Connect**.
2. Enter your email address and click **Continue**.

The sign in page of your SSO provider is displayed.
3. Sign in with your SSO credentials.
