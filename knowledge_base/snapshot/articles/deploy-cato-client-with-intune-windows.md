---
title: "Deploy Cato Client with Intune (Windows)"
slug: "deploy-cato-client-with-intune-windows"
updated: 2026-08-20T06:25:26Z
published: 2026-08-20T06:25:26Z
canonical: "knowledge.catonetworks.com/deploy-cato-client-with-intune-windows"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Cato Client with Intune (Windows)

In this guide, we’ll walk through how to configure Microsoft Intune from scratch and use it to deploy the Cato SDP Client for Windows.

**Note**: This article is based on Intune versions up to February 2024. For troubleshooting, please contact Intune support

## What is Intune?

Microsoft Intune is a cloud-based service that focuses on mobile device management (MDM).

With Intune, you can:

- Set rules and configure settings on personal and organization-owned devices to access data and networks
- Deploy and authenticate apps on devices – on-premises and mobile
- Be sure devices and apps are compliant with your security requirements

In order to access Intune, you need to have either a Microsoft 365 or Enterprise + Mobility E3/E5 subscription. If you’re using a free Azure account, you’ll need to sign up for a trial or pay per user (which can get costly).

For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune).

## Before you Begin

When adding an app to Intune, you’ll be prompted to allocate the groups of users (or devices) that the app will be rolled out to. Hence before beginning, ensure you have the users of Cato inside of an AD or Azure AD group that you can assign the Cato SDP Client app to.

Depending on whether you want the Cato SDP client app to be mandatory or optional for certain groups of users, you may want to divide your users into two groups:

- The users to which the app is MANDATORY. Any user in this group will have the app automatically pushed out to them.
- The users to which the app is OPTIONAL. The app will not be automatically pushed for users in this group, allowing them to go to the Company Portal and download it themselves if they choose.

### Deploying the Client with Installation Parameters

When installing the Windows Client with Microsoft Intune, you can configure supported feature settings using MSI installation parameters. Use the `CATO_REGISTRY_OPTIONS` property to provide each approved registry option as a key-value pair. The installer applies these options only during a new installation. It ignores the property during upgrades and repairs. The installer validates each option against an approved list. It then uses the predefined registry data type for each supported option.

Accepted values are written to:

`HKLM\SOFTWARE\CatoNetworksVPN`

#### Input Format

Use a comma-separated list of key/value pairs:

`CATO_REGISTRY_OPTIONS="Key1=Value1,Key2=Value2"`

| Rule | Value |
| --- | --- |
| Option separator | Comma: **,** |
| Key/value separator | Equals sign: **=** |
| Maximum options per install | 15 |
| Maximum key and value length | 50 characters each |
| DWORD values | Boolean flag: **0** disabled, **1** enabled. |
| String values | ASCII letters, digits, dot, and hyphen; no leading or trailing dot. |

#### Supported Parameters

| Option Key | Registry Value Name | Purpose | Type | Allowed Value | Additional Resources |
| --- | --- | --- | --- | --- | --- |
| InitialAlwaysOn | InitialAlwaysOn | Force Always-On to be enabled | REG_DWORD | 0 or 1 | [Always On](/v1/docs/protecting-users-with-always-on-security) |
| ForceAuthTrafficToTunnel | ForceAuthTrafficToTunnel | In Always-On mode, forces all traffic, including authentication traffic, through the Cato tunnel | REG_DWORD | 0 or 1 | [Always On](/v1/docs/protecting-users-with-always-on-security) |
| ConnectOnBoot | ConnectOnBoot | Configure Client to connect every time the device boots | REG_DWORD | 0 or 1 | [Connect on Boot](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| LaunchAuthPageOnStartup | LaunchAuthPageOnStartup | Automatically launch the Client after initial installation for the next Windows user who logs in | REG_DWORD | 0 or 1 | [Automatically Launching Client](/v1/docs/installing-the-cato-client) |
| SubdomainForSeamlessAuth | SubdomainForSeamlessAuth | Define the Cato SSO subdomain for automatic authentication with Windows credentials | REG_SZ | Subdomain string | [Automatic Authentication](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| SeamlessAuthEnableMS | SeamlessAuthEnableMS | Enable Microsoft/Entra ID seamless authentication using Windows Web Account Manager | REG_DWORD | 0 or 1 | [Automatic Authentication](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| SeamlessAuthEnableAddUser | SeamlessAuthEnableAddUser | Enable Microsoft/Entra ID seamless authentication using Windows Web Account Manager, when adding another user. Only supported if `SeamlessAuthEnabeMS` is enabled | REG_DWORD | 0 or 1 | [Automatic Authentication](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| SeamlessAuthAllowUICMA | SeamlessAuthAllowUICMA | Allows the authentication UI to be shown during automatic-auth reauthentication | REG_DWORD | 0 or 1 | [Automatic Authentication](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| Subdomain | Subdomain | Specifies the account workspace/subdomain for pre-login authentication | REG_DWORD | Subdomain string | [Pre Login](/v1/docs/using-windows-pre-login-and-the-sdp-client) |
| PreLogin | PreLogin | Enable Pre-login for a specific device | REG_DWORD | 0 or 1 | [Pre Login](/v1/docs/using-windows-pre-login-and-the-sdp-client) |

#### Examples

The following are some examples of using the installation parameters:

MSI Installation:

- To enable Connect On Boot and automatically launch the Client after installation: msiexec /i "C:\path\CatoNetworksSetup.msi" CATO_REGISTRY_OPTIONS="ConnectOnBoot=1,LaunchAuthPageOnStartup=1" /l*v "C:\temp\cato_install.log"

- NSIS Bootstrapper Installation:
  - When using **CatoNetworksSetup.exe**, pass MSI properties through the bootstrapper with `/props=`.
    - To enable Always On and Connect On Boot: CatoNetworksSetup.exe /props=CATO_REGISTRY_OPTIONS=InitialAlwaysOn=1,ConnectOnBoot=1

## Microsoft Intune Admin Center

We’ll be using the Microsoft Intune Admin Center to orchestrate Intune. You can log in using the same Azure Portal credentials here: [https://endpoint.microsoft.com](https://endpoint.microsoft.com).

### Deploying the SDP Client

To deploy the SDP Client using the MEM, complete the following three steps:

1. Add a new Line-of-Business App
2. Customize the App details
3. Assign users to the App

#### Add a new Line-of-Business App

Add the Client to the MEM portal.

**To add a new Line-of-Business App:**

1. In the **Apps** menu, navigate to **Apps > All Apps**.
2. Click **Add**.

The **Select app type** panel opens.
3. In the panel, under the **Other** heading, select **Line-of-business app** and click **Select**.
4. Upload the MSI file for the Cato SDP Client. For more information, see [Downloading the Cato Client](/v1/docs/downloading-the-cato-client).
5. Click **OK**.

#### Customize the App Details

Customize the app details in the MEM portal.

**To customize the app details:**

- On the **Add App** screen, under the **App information** tab, enter the following details:

  - **Name:** Cato SDP Client
  - **Description:** Cato Client
  - **Publisher:** Cato Networks
  - **Ignore App Version:** Select **No**
  - **Category (Optional):** Select an app category to allocate to the Cato SDP Client

#### Assign Users to the App

Depending on how you want the app rolled out to users, there are two different sections you can allocate users or groups to:

- **Required:** The app is MANDATORY for these users/groups. Any user or group in this section will have the App automatically pushed out to them
- **Available for enrolled devices:** The app is OPTIONAL for these users/groups. The app will not be automatically pushed, and the users can go to download the app themselves from within the Company Portal

**To assign users to the app:**

1. In the Microsoft Intune admin center, navigate to **Apps > All Apps > Cato SDP Client > Properties > Assignments**
2. Click **Next**
3. On the **Review + Create** screen, click **Create**.

Your Line-of-Business application is created, and the MSI file is uploaded.

**Note:** Wait until the MSI file upload is completed before closing the MEM.
