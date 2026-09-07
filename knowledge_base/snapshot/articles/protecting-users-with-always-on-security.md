---
title: "Protecting Users with Always-On Security"
slug: "protecting-users-with-always-on-security"
updated: 2026-09-07T07:49:31Z
published: 2026-09-07T07:49:31Z
canonical: "knowledge.catonetworks.com/protecting-users-with-always-on-security"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Protecting Users with Always-On Security

This article discusses how to configure your Always-On policy to increase Internet security for users in your account.

## Overview

The Always-On Policy enhances Internet security by defining rules for when users or User groups always connect to the Cato Cloud. This ensures all traffic goes through a PoP, and Cato security engines inspect the traffic to ensure it complies with your security policies.

### Use Case - Customize the Always-On Policy for Employees and Third-Party Contractors

Company ABC's network is used by its own employees, who have access to corporate resources, and third-party contractors, who cannot access corporate resources. They create a rule to enable Always-On for their employees while the third-party contractors are able to directly access the Internet. This ensures all traffic from company employees is passed through the Cato Cloud and is protected by security policies.

### Use Case - Enable Always-On Policy only for Managed Devices

Company ABC installs the Cato Client on all of its managed devices, and also allows its employees to install the Client on their personal devices so they can access company resources if necessary. The corporate security policy requires that the managed devices are always connected to the network.

The IT team creates a [Device Posture](/v1/docs/creating-device-posture-profiles-and-device-checks) profile that uses a Device Check that verifies that a signing certificate is installed on the device.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_always_on.png)

Then they create rules in the Always-On policy to only require Always-On for devices that match the Device Posture profile for certificates.

![always-on-managed.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31661517417245(1).png)

### Working with the Ordered Always-On Policy

The Always-On Policy is an ordered rule-base. The rules in your policy are applied to a User or Group as follows:

- When they meet a rule, the Client follows the configuration set in the rule
- If they do not meet any rules, they are able to disconnect from the network

### Always-On Policy Prerequisites

- Always-On is not supported for Linux Clients

## Always-On with Managed Devices

This section describes the configuration flow to apply the Always-On policy only to managed devices using a Device Check for signing certificates.

1. Prepare devices to use Device Check for the signing certificate.
  - Distribute the certificate to the managed devices. See articles in [Distributing and Installing Device Certificates](/v1/docs/distributing-and-installing-device-certificates).
  - Upload the signing certificate to the CMA. See [Managing Signing Certificates for Remote Access](/v1/docs/managing-signing-certificates-for-remote-access).
2. To identify managed devices based on the installed certificate, configure a Device Check for certificates and assign it to a Device Profile. See [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks).
3. In the Always-On policy, create a new rule that requires managed devices to always connect to the network:
  1. **User/Groups** - Assign user groups or users to the managed devices.
  2. **Device Posture Profiles** - Select the Device Profile that you created in step 2.
  3. **Connected** - Select **Always-On**.
4. Duplicate the rule from step 3, and change the **Connected** setting to **On-Demand**.

![always-on-managed.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31661517417245(1).png)
5. Publish the Always-On policy.

## Providing Internet Access with the Always-On Policy

With the Always-On Policy enabled, you can still provide users with direct access to the Internet by:

- Using a temporary bypass method
- Creating a rule with an **On-Demand** connected status
- Allowing Internet access in Recovery mode

### Temporarily Bypassing Secured Internet Access

There can be some situations where users need to temporarily bypass the Cato Cloud and directly access the Internet. For example, to temporarily access a website that is blocked by an Internet Firewall rule. For each rule, you can configure how users temporarily bypass the Cato Cloud.

On Windows v5.9 and higher, you can also configure how long users are able to bypass the Cato Cloud. During this period, Internet traffic does not flow through the Cato Cloud and is unsecured.

When the Client temporarily disconnects, events are generated that show the user details and the time duration that the Client was disconnected for. To view these events, on the **Events** page apply a filter for the sub-type **VPN Never-Off Bypass**. The **Bypass Method** in the event displays the method used to bypass the Client. For more about events in your account, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

Users can temporarily bypass the Cato Cloud using either:

- Admin controlled bypass with a bypass code
- User controlled bypass

#### Admin Controlled Bypass with a Bypass Code

**Note:** Supported on Windows, Android, iOS, and macOS Clients

Use this option to generate a one-time password (OTP) in the Cato Management Application that you can give to any user and let them temporarily disconnect the Client. In Windows Client versions lower than 5.9 and other supported operating systems, the Client is bypassed for up to 15 minutes at a time. Each code can be valid for up to 15 minutes.

In addition, you can use an authentication app (such as Google Authenticator) to scan the QR code on this screen. Then you can always get an OTP for users from the authentication app. The authentication app refreshes the code every 30 seconds, so each code is only valid for 30 seconds.

You can use the same bypass code for multiple users, as long as the code is still valid.

#### User Controlled Bypass

**Note:** Supported on Windows, macOS Clients, and [iOS Client v5.6 and higher](/v1/docs/summary-of-cato-ios-client-releases).

This option lets users temporarily disconnect the Client on request. In the Client, the user must provide a reason for disconnecting the Client in a free text field. and then can immediately access the Internet. This reason is included in the event.

The Client is allowed to disconnect for the time duration that is configured in the **Disconnect Duration**.

#### Use Case - Pre-approved Access to the Internet for Specific Teams

A retail company's engineering team is responsible for ensuring their website has 100% availability to receive online orders. This means that they always need access to an online SaaS application required for troubleshooting issues. Access to the application is required out of hours and when working remotely. The company's security policy states that all Internet access must be secure.

To comply with the security policy, IT enables Always-On. As a precaution, to avoid a situation where, during a potential outage, the Client cannot connect to the Cato Cloud, the IT team provides the engineers with a way to immediately access the Internet. The IT team created a rule in their Always-On policy for the engineer User group, where Bypass Mode is configured to let users temporarily disconnect on request.

If an engineer needs to troubleshoot website issues in the middle of the night, the IT team can be sure that they can access the troubleshooting SaaS application even if there is an issue with the Client. The engineer does not need to wait for IT approval to bypass the Cato Cloud and begin troubleshooting the website issues.

### Creating a Rule with an On-Demand Connected Status

If there are users who regularly need direct access to the Internet, you can add them to a rule with the connect status **On-Demand**. This configuration lets users connect or disconnect the Client as required.

### Client Recovery Mode

**Note:** Supported on Windows, macOS Clients, and [iOS Client v5.6 and higher](/v1/docs/summary-of-cato-ios-client-releases).

You can also choose the Client behavior in a scenario where a connection to the Cato Cloud cannot be established. The Client can be configured to:

- **Allow Internet access (Default configuration):** Users can access the Internet and LAN. Traffic does not flow through the Cato Cloud and is unsecured until a connection to the Cato Cloud is established
- **Restrict Internet access:** Users cannot access the Internet until a connection to the Cato Cloud and secured Internet is established

#### Use Case - Internet Connection When Traveling

Company ABC has Always-On enabled for all users. Their C-suite executives often travel and connect to the Internet from airports and hotels. Occasionally, the Client doesn't detect the captive portal and is unable to establish an encrypted tunnel. To ensure the C-suite can continue to work when they are traveling, the IT team configures Recovery Mode in the Always-On rule for the C-suite User group to allow access to the Internet.

If the Client doesn't detect a captive portal, the C-suite users are able to continue to work because the Client allows Internet access according to the Always-On policy. As soon as the Client reestablishes a tunnel, traffic flows through the Cato Cloud as expected.

## Preparing to Implement Always-On Policy

Before you enable your Always-On Policy, consider how Always-On interacts with other features and Client versions in your environment. This section provides recommendations for how to use SSO, Client Connectivity, Device Authentication, and the Windows Client with your Always-On Policy.

### Working with Always-On and SSO

For accounts that use Single Sign-On authentication for users, you can also configure the supported Clients to always remain connected to the Cato Cloud (Always-On). This configuration provides users with the simplicity of SSO and the security of Always-On. The Client is able to access the IdP provider, and access to other resources is in accordance with your security policy.

**Note:** To help users who can't authenticate to the Client, we recommend that you enable a method of bypassing the Cato Cloud and review bypass events. Otherwise, the unauthenticated device can't connect to the Internet or the Cato Cloud.

#### Implementing Always-On and SSO

This section contains best practices and recommendations for implementing Always-On with SSO in your account.

- Start by enabling Always-On and SSO for a small number of users to minimize the impact on your account
- Review bypass events to monitor the usage of Bypass codes in your organization
- Since unauthenticated users don't have Internet connectivity, make sure that users can log in to the device without relying on the Internet
- Make sure that all the Clients are updated to the minimum supported version for the relevant OS. If a Client of an unsupported version is used, the Client cannot re-authenticate and traffic to the internet is blocked.
- For deployments that use a third-party proxy, only In-Client **Browser Authentication** is supported for Always-On and SSO (for more about **Browser Authentication**, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients))

### Using Client Connectivity Policy and Device Authentication with Always-On

Your [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) and [Device Authentication](/v1/docs/legacy-device-authentication) settings apply Device Postures and Checks performed on devices for users. If the device fails to comply with the policy that was set for the profile, then the user can't connect to the Cato Cloud. Your Client Connectivity Policy and Device Authentication settings take precedence over your Always-On Policy.

### Installing Windows Clients and Always-On

For IT teams delivering or shipping brand new devices to users around the world, we can provide Always-On Security out-of-the-box.

Starting with Windows Client v5.6, you can enhance Internet security even before a user authenticates to Cato. The Always-On policy is available out-of-the-box, and Internet access is only permitted after the user authenticates to your Cato account.

To enable this feature, simply add a registry key to the Windows device to enable Always-On. Once the user is added to the Client, the Always-On settings defined in the Cato Management Application are applied to that user.

For accounts that use the [Pre login feature](/v1/docs/using-windows-pre-login-and-the-sdp-client), the device is only allowed to access the **Allowed Destinations** before the user is added to the Client. All other Internet access is blocked.

We also recommend adding the registry key that launches the Client on startup. For more information, see [Installing the Cato Client.](/v1/docs/installing-the-cato-client)

This can also be configured as an installation parameter when deploying the Client with an MDM. For more information, see [Deploy Cato Client with Intune (Windows)](/v1/docs/deploy-cato-client-with-intune-windows).

**Note:** Before users are added to the Client, it's not possible to bypass the Cato Cloud.

**To configure the Windows registry to enforce Always-On:**

1. Go to the registry key: `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN`
2. Define this key:
  - InitialAlwaysOn=1 (DWORD)

## Configuring the Always-On Policy

This section explains how to create the Always-On Policy.

### Creating the Always-On Policy

The Always-On Policy lets you define the users or User Groups for Clients that are required to always connect to the network.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/always-on_policy.png)

**To create the Always-On Policy:**

1. From the navigation menu, click **Access > Always-On Policy**.
2. Click **New**.

The **New Rule** panel opens.
3. Enter a **Name** and set the **Rule Order**.
4. Define the **Users & Groups** and **Platforms**.
5. Define the **Connected** status and **Bypass Mode** for Always-On.

![Bypass.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31661536083229(1).png)
6. For **SDP Anti-Tampering**, determine what action to take when a user attempts to make changes. By default, the changes are allowed. To prevent users from making changes, select **Enable**. For more information, see [Working with Anti-Tampering for the Cato Client](/v1/docs/working-with-anti-tampering-for-the-cato-client).
7. Determine for how long Always-On and Anti-Tampering are disabled in **Disconnect & Tampering Duration.**

The timer for each bypass begins when a code is entered. For example, the Duration is set to 60 minutes. If the bypass code for Anti-Tampering is entered at 12:30, the timer starts, and Anti-Tampering will again be enabled at 13:30. A bypass code for Always On is entered at 13:00, and that will expire at 14:00.
8. Configure how the Client operates when in **Recovery Mode**.
9. Click **Apply**.
10. Repeat steps 2-5 for each rule in the Always-On Policy.
11. Enable the **Always-On Policy** and then click **Save**.

The slider ![enable.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31661551052701(1).png) is green when the rule is enabled, and gray when the rule is disabled.

#### Configuring the Default Settings

**Note:** Supported for Windows and Linux Clients

You can provide users with an **On-Demand** connected status with additional security by configuring the Client to automatically connect during boot phase. Once connected, users can choose to disconnect and reconnect the Client whenever they need to. For users with an **Always-On** connected status, the Client automatically connects without this configuration.

- If the **Connect on boot** or the **Start minimized** options are selected in the Cato Management Application:
  - This is enforced on all Clients in your environment
  - Users cannot disable this setting from the Client

- If the **Connect on boot** or the **Start minimized** options are cleared in the CMA:
  - Users can choose to enable these features on the **Settings** tab in the Client

**Note:** With **Connect on boot** enabled, if a user logs out of their Windows session, the Client connects to the Cato Cloud. This is to provide access to a Domain Controller to allow the user to log back in.

**To configure default settings for Clients:**

1. From the navigation menu, click **Access > Always-On Policy**.
2. Open the **Settings** tab.
3. In the **Connect on Boot** section, define the default settings for Windows Clients.
4. Click **Save**.

#### Enforcing Authentication Behind a Cato Site

**Note:** Supported for Windows and Linux Clients

When a user connects behind a Cato Socket or IPsec site, the Client automatically connects to that site in Office Mode. For more information on Office Mode, see [Configuring Office Mode](/v1/docs/configuring-office-mode).

You can configure whether users with always-on enabled are required to authenticate to Cato when the Client is connected in Office Mode. This configuration has no impact on security policies.

When this option is enabled:

- The Client establishes an SDP control tunnel to the connected PoP for authentication, keep-alive, and other control communications.
- User data traffic does not traverse the SDP tunnel. Instead, it continues to exit through the device's network interface (NIC) and is forwarded by the local Cato Site.

**To enforce authentication at a Cato site**

1. From the navigation menu, click **Access > Always-On Policy**.
2. Open the **Settings** tab.
3. In the **Enforce Always-On in Office** section, select **Require authentication in an office**.
4. Click **Save**.

## Generating a Bypass Code

A bypass code is a 6 digit code that is entered in the Client to let users temporarily disconnect from the Cato Cloud.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Always-On-Bypass-Code.png)

**To generate a bypass code:**

1. From the navigation menu, click **Access > Always-On Policy**.
2. Open the **Settings** tab.
3. Expand the **Show bypass code** or **Show QR code for authentication app** section.
4. Determine how long before the bypass code expires. **Note:** Supported from Windows Client 5.18 and macOS Client 5.10.6
5. You can now send the bypass code or QR code to a user.

## Understanding the User Experience

### Generating an Anti-Tampering Bypass Code

An Anti-Tampering bypass code is a 6 digit code that is entered in the Client to let users temporarily make changes to the Cato Client, or its ability to operate, e.g., changing relevant registry entries.

**To generate a bypass code:**

1. From the navigation menu, click **Access > Always-On Policy**.
2. Open the **Settings** tab.
3. Expand the **Show anti tamper bypass code** or **Show anti tamper QR code for authentication app** section. Each code is valid for 15 minutes.
4. Copy the Anti-Tamper bypass code or QR code and send it to the user.

Depending on the **Bypass Mode** configured in the Cato Management Application, users can temporarily disconnect the Client using either a bypass code or by entering a reason to bypass.

### Entering a Bypass Code

The bypass code is generated by admins and sent to a user to be entered into the Client. After a valid code is entered, the Client temporarily bypasses the encrypted tunnel, and the user can access the Internet. Windows Clients below v5.9, macOS, iOS, and Android Clients can be temporarily disconnected for a maximum of 15 minutes. Windows Client v5.9 and above can be disconnected for the length of time configured in the **Disconnect Duration**.

Users who authenticate with SSO or MFA need to re-authenticate to the Cato Client when re-connecting.

**Note:** Bypassing the Always-On configuration doesn't affect Anti-Tampering protection.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/enter_bypass_code.png)

**To enter a bypass code:**

- In the Windows Client, users can right-click the Client icon in the system tray and select **Temporary Bypass**
- In the macOS Client, users can right-click the Client icon in the system tray and select **Temporary Disconnect**
- In the iOS Client, on the Client home screen, select **Bypass Always-on**
- In the Android Client, from the side menu, select **Temporary Bypass**

### Entering a Reason to Bypass

Users are able to temporarily disconnect the Client after they provide a reason. After the user enters the reason, the Client temporarily bypasses the Cato Cloud and the user can access the Internet. The Client is disconnected for the length of time configured in the Cato Management Application.

Users who authenticate with SSO or MFA need to re-authenticate to the Cato Client when re-connecting.

**To enter a bypass reason:**

1. In the Windows Client, users can right-click the Client icon in the system tray and select **Temporary Bypass**.
2. Provide a reason for temporarily disconnecting the Client.
3. Click **Enter**.

The Client is disconnected.

#### Enter an Anti-Tamper Bypass Code

**Notes:**

- Supported from Windows Client v5.14 and higher
- Bypassing the Always-On configuration doesn't affect Anti-Tampering protection

Users are able to temporarily disable the Anti-Tamper protection for the Client after they receive a code from an admin.

**To disable Anti-Tamper protection:**

1. In the Client, click **Settings**.

By default, the **Bypass** section is hidden from users. To display the field, use the key sequence CTRL + SHIFT + O
2. Contact an admin and enter the code they receive in the **SDP tamper release** field.
3. Click **Submit**.

Anti-Tampering is disabled for the duration configured by an admin.

## Customizing Always-On for Specific Users

You can customize the Always-On Policy for an individual user.

**To configure the Always-On Policy for a specific user:**

1. From the navigation menu, click **Access > Always-On Policy**.
2. Click **New**.

The **New Rule** panel opens.
3. Enter a **Name** and set the **Rule Order**.
4. In the **User & Groups** section, select **SDP User**.
5. Choose the specific user.
6. Define the **Platforms** and **Connected** status.
7. Click **Apply**.
8. Enable the **Always-On Policy** and then click **Save**.

The slider ![enable.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31661551052701(1).png) is green when the rule is enabled, and gray when the rule is disabled.
