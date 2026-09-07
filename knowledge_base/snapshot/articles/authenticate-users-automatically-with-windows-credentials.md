---
title: "Authenticate Users Automatically with Windows Credentials"
slug: "authenticate-users-automatically-with-windows-credentials"
updated: 2026-07-26T14:04:58Z
published: 2026-07-26T14:04:58Z
canonical: "knowledge.catonetworks.com/authenticate-users-automatically-with-windows-credentials"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticate Users Automatically with Windows Credentials

This article explains how to configure the Client so that it relies on the user's Windows credentials to authenticate.

## Overview

For remote access, implementing your security policies requires that users successfully authenticate to the Client. Ensuring seamless authentication increases your network security and creates a simple user experience. For users who authenticate with SSO, you can configure the Client to use their Windows credentials to authenticate. This lets users sign in once to their device, without needing to re-enter credentials when connecting to the Client. Authentication can occur automatically or be initiated by the user. In this process, a [Primary Refresh Token (PRT)](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token) is issued, which the Cato Client retrieves to authenticate the user. After the SSO session expires and the PRT token is valid, the Client silently re-authenticates using the Windows credentials, maintaining a seamless login and re-authentication flow.

If you configure this feature together with the [Windows registry key](/v1/docs/installing-the-cato-client) to automatically launch the Client after initial installation and [Connect on Boot](/v1/docs/protecting-users-with-always-on-security), the Client always launches, authenticates, and connects without a user taking any action.

> [!NOTE]
> **Note:** Registry entries might be case sensitive and should be entered exactly as they appear in this article.

### Use Case - Simplifying Client Authentication

Company ABC wants a simple user experience for their users so that they can connect to Cato with as few clicks as possible. To do this they want to make the Client authentication process automatic. This means that to connect to Cato, users only need to open the Client and click **Connect**.

The admin configures the Cato SSO settings to automatically use the user's Windows credentials to authenticate.

Every time users log in to their device, even if the SSO token has expired, the Client is able to connect to the network without requiring additional authentication from the user.

### Use Case - Seamless Client Authentication and Connection

Company ABC wants to ensure their users are connected to the Client as often as possible. To do this they want to make the Client connection process automatic so that new and existing users do not need to remember to manually click the **Connect** button in the Client.

The admin configures these settings:

- So that the Client launches straight away for new users the first time that they start the device, they define a Windows registry key on the device
- So that the Client connects every time the device boots, they enable **Connect on Boot**
- To remove the requirement of manual user authentication, they enable Automatic Client Authentication to use the user's Windows credentials to authenticate

Every time users log into their device, the Client launches, authenticates and connects without any action from the user.

> [!NOTE]
> **Note:** If Azure can't provide the authentication token for the user, then the end user follows the standard authentication flow by entering the Azure credentials in the Client.

### Prerequisites

- Authenticating with Windows credentials is supported:
  - On Windows Client v5.8 and higher
  - On devices running Windows 10 or higher
  - On Azure AD joined devices (Hybrid AD joined is supported from Client v5.11 and above)
  - With Azure configured as the SSO provider for your account and users allowed to log in with SSO
  - OID and [SID](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers) mapping is configured (for more information, see the [Microsoft Documentation](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc))
  - The Client can fetch the PRT token. If the PRT token cannot be fetched, the user may need to manually authenticate or re-authenticate to Windows. For troubleshooting PRT token issues, see the [Microsoft Documentation](https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-primary-refresh-token).

#### Known Limitations

- Azure AD that requires user interaction (such as MFA), is supported from Client v5.11 (it is not supported on Clients below v5.11)
- The registry key `InitialAlwaysOn` is not supported for this feature

## Configuring Authentication with Windows Credentials

This feature is enabled within your Azure SSO configuration. Once you enable it, you can choose the user experience.

![Windows_Auth.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28518181596317.png)

**To authenticate with Windows credentials:**

1. From the navigation menu, click **Access > Single Sign-On**.
2. From the **SDP Client users** section, select **Sign in with Windows credentials**.
3. From the drop-down menu configure the user experience:
  - **Automatically:** The Client automatically uses Windows credentials to authenticate
  - **User Selection:** The user has to confirm authentication with their Windows credentials, however does not need to re-enter them or can choose to authenticate as a different user
4. Click **Save**.

Users now authenticate to Cato with their Windows Credentials. New users automatically authenticate with their Windows credentials. Configured users automatically authenticate the next time the SSO session expires.

> [!NOTE]
> **Note:** If multiple users are configured on a device, only the user configured in the Client can authenticate with their Windows credentials.

## Configuring a Seamless User Experience

You can configure authentication with Windows Credentials with other features to create a seamless user experience. This means that the Client launches, authenticates, and connects without any action from the user.

After configuring the Windows registry keys, reboot the device.

This can also be configured using installation parameters; for more information, see [Deploy Cato Client with Intune (Windows)](/v1/docs/deploy-cato-client-with-intune-windows).

### Define Subdomain for Seamless Authentication

Define your Cato account name as it appears in the CMA using the `SubdomainForSeamlessAuth` Windows registry key. You can identify the subdomain for your account on **Access > Single Sign-On** page. After the Client successfully performs the initial authentication to the Cato Cloud, the registry is automatically updated

**To define your Cato account name:**

1. Go to this location in the registry: **HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN**
2. Define this key:
  - SubdomainForSeamlessAuth = <your account name> (String)

### Automatically Launching the Client

Define the `LaunchAuthPageOnStartup` Windows registry key to automatically launch the Client after initial installation. This feature is for new users the first time they log in to their device.

**To configure the Windows registry to automatically launch the Client:**

1. Go to this location in the registry: **HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN**
2. Define this key:
  - LaunchAuthPageOnStartup=1 (DWORD)

### Using Connect on Boot for Entire Account

You can choose to enable [Connect on Boot](/v1/docs/protecting-users-with-always-on-security) in the Cato Management Application for the entire account, so that the Clients always connect every time the device boots. This feature is configured for users to enforce Client connection without any action from the user.

#### Customizing Connect on Boot for Specific Users

For accounts that only want to enable Connect on Boot for specific users, you can define the `ConnectOnBoot` registry key on the devices for the required users.

**To configure the Windows registry to connect the Client when the device boots:**

1. Go to this location in the registry: **HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN**
2. Define this key:
  - ConnectOnBoot=1 (DWORD)

### Additional Settings

If there is need for the user to complete additional authentication steps, for example, MFA, the `SeamlessAuthAllowUI` registry key is required to let users manually authenticate.

**To configure the additional registry key:**

1. Go to location in the registry: **HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN**
2. Define this key:
  - SeamlessAuthAllowUI=1 (DWORD)

## Using Always Prompt Token Validity and Authentication with Windows Credentials

If your SSO **Token validity** configuration is set to [**Always Prompt**](/v1/docs/configuring-sso-and-the-subdomain-for-the-account) and you enable authentication with Windows Credentials, the Client silently authenticates with the users Windows Credentials without any prompt.
