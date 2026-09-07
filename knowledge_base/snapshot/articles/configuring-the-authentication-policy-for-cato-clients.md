---
title: "Configuring the Authentication Policy for Cato Clients"
slug: "configuring-the-authentication-policy-for-cato-clients"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-the-authentication-policy-for-cato-clients"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Authentication Policy for Cato Clients

This article discusses how to configure the authentication behavior and Multi-Factor Authentication (MFA) requirements for SDP users in your account.

## Overview of SDP Client Authentication Policy

The Authentication policy defines how users authenticate to your account: MFA, Single Sign-On (SSO), or username and password. In addition, you can choose the end-user authentication experience using the in-Client browser or the external default OS browser.

## Setting the Browser Authentication for the Account (Windows and macOS)

For Windows and macOS devices, you can configure whether users authenticate using the embedded browser or an external browser. The default setting is to use the embedded browser which provides the best end-user experience. MFA and SSO authentication is completed inside the Client and then seamlessly connects the device to the Cato Cloud.

Sometimes the network configuration of an account doesn't support the embedded browser. In these cases, you can set your account to use the external default OS browser for the device. The end-user starts the connection in the Client, and then users authenticate to the Cato Cloud with the OS browser.

**To set the Client browser authentication for the account:**

1. From the navigation menu, click **Access > User Authentication**.
2. Click the **Additional Settings** tab.
3. In **Browser Authentication**, select one of these options:
  - **Embedded browser** - SDP users authenticate to your account within the Client
  - **External Browser** - SDP users authenticate to your account with the OS browser
4. Click **Save**.

### Best Practices for Browser Authentication

The following are best practices to follow when choosing your Browser Authentication method:

- The Embedded Browser is recommended except when conditional access requires a browser plugin that is only supported by an external browser.
- Use the Embedded Browser when the Always-On is enabled to ensure proper functionality. Not all domains and IPs necessary for SSO authentication are allowed when using an external browser.
- The embedded browser must be used in an ADFS environment, or SSO can not be used for authentication.
- The embedded browser prevents an issue with SSO authentication with the external browser and HSTS enforcement. For more information, see [SSO Authentication Fails When Using External Browser | localhost Error](/v1/docs/sso-authentication-fails-when-using-external-browser-localhost-error).
- Use the external browser for authentication when using the Okta Verify app on either macOS or Windows.

## Configuring the Authentication Policy for All Users

Use the **User Authentication** screen to define the authentication policy for users in your account that connect with the Cato Client. For accounts that enable SSO, this is the default authentication policy.

These are the authentication options:

- SSO - Users authenticate with SSO using the Identity Provider (IdP) configured for your account
- MFA - Users must authenticate using a code they receive from an SMS or an authenticator app (according to RFC-6238 for MFA)
- User Name and Password - Users authenticate with the username and password for the Client (no MFA requirements)

You can also choose to override the MFA policy for individual users, see below [Overriding Authentication Settings for Specific Users](/v1/docs/configuring-the-authentication-policy-for-cato-clients#overriding-authentication-settings-for-specific-users).

If you are using Directory Services and you need to modify a user's mobile phone number for advanced authentication, you must modify the phone number only in the IdP.

> [!NOTE]
> Note:
> 
> Multi-Factor Authentication (MFA) and Single-Sign On (SSO) are NOT supported for users that are provisioned with a [registration code](/v1/docs/activating-users-with-a-registration-code).

**Working with Token Validity Settings**

The **Token Validity > Duration** option depends on whether the device running the Cato client is "trusted" as follows:

- If the user enabled trust for the device running the Cato Client (by selecting the **Don't ask me again on this device/computer** option on the Client when connecting to the Cato Cloud), then MFA is not required if the duration is still valid and the geolocation has not changed to a different country
- If the user did not enable trust for the device running the Cato client (by clearing the **Don't ask me again on this device/computer** option on the client when connecting to the Cato Cloud), the duration setting has no effect and MFA is always required on this device

> [!NOTE]
> Note:
> 
> From Windows Client v5.12, the Client's embedded browser is able to refresh the IdP token. Users are not prompted to reauthenticate when the IdP token expires.

![ClientAccess_Authentication.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218250450845.png)

**To configure the MFA policy for remote users:**

1. From the navigation menu, click **Access > User Authentication**.
2. In the **Method** drop-down list, select **MFA**.
3. Configure the **General** select the **Authentication Method** for the policy:
  - **Any** - Each user selects the authentication method for themselves
  - **Authenticator** - Users must use an authentication app (such as Google Authenticator)
  - **SMS** - Users are sent an SMS text message with an authentication code
4. In the **Token validity** section, select the behavior for the MFA token in the Client:
  - **Always Prompt** - MFA is required whenever the user connects.

Users that are logged in must reauthenticate when the duration you define in **Days** or **Hours** (since they last logged in) is reached.
  - **Duration** - Users do not require MFA for the duration you define in **Days** or **Hours**.
5. Click **Save**.

## Overriding Authentication Settings for Specific Users

You can customize different authentication settings for specific users and override the global authentication policy. Edit a user and then use the **Authentication** screen to customize the authentication method for that user.

**To override the global authentication settings for a specific user:**

1. From the navigation menu, click **Access > Users**.
2. Select the user, and from the navigation menu select **User Settings > Authentication**.
3. Select **Override account Authentication settings**.

![Override_Authentication_Settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218264377245.png)
4. Select the authentication **Method** for the user.
5. Configure the authentication settings for this user.
6. Click **Save**.

### Resetting MFA for a User

You can reset the MFA setting for users when necessary, such as installing the Client on a new device.

**To reset the MFA settings for a user:**

1. From the navigation menu, click **Access > Users**.
2. In the **User** list, select the check box next to the user's name.
3. From the **Actions** drop-down menu, select **Reset MFA**.
4. In the confirmation window, click **OK**.
5. The user receives an e-mail with a link to the Cato User Portal. After signing in to the portal, the user will need to activate MFA settings for the device.

## Related Resources

- [Working with Users](/v1/docs/working-with-users)
