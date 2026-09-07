---
title: "Managing SDP Clients with the Cato User Portal"
slug: "managing-sdp-clients-with-the-cato-user-portal"
updated: 2026-08-03T10:34:28Z
published: 2026-08-03T10:34:28Z
canonical: "knowledge.catonetworks.com/managing-sdp-clients-with-the-cato-user-portal"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing SDP Clients with the Cato User Portal

## Overview of the User Portal

Admins and SDP users can use the Cato User Portal to easily manage the Cato Clients. Users can:

- Change the password for the Cato Client
- Show the trusted devices which only require MFA once during the set time period
- Change their MFA settings

### Downloading the Cato Client and Certificates

You can download the Cato Client and certificates from here: [Client download portal](https://clientdownload.catonetworks.com/)

Install the Cato certificate on a device or host to define it as a root CA. This is necessary to let TLS inspection decrypt and then inspect traffic to provide the best threat protection for these endpoints.

When you install the Windows Cato Client on a host, the Cato certificate is installed automatically.

### Logging In to the User Portal

Generally, users receive an email with the relevant domain that is used to log in to the User Portal, such as **https://myvpn.catonetworks.com/login**. Then they can log in to the User Portal with the Cato Client account name (only lower-case letters), username, and password. The same password is used for the Cato Client and the User Portal.

## Changing the Password for the User Portal and Cato Clients

When you are logged in to the User Portal, you can change the password for the portal and the Cato Client. The same password is used for the Cato Client and the User Portal.

**To change the User Portal and Cato Client password:**

1. From the bottom of the **My Devices** window, click **Change Password**.

![ChangePassword.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31126591436829.png)
2. Enter your Cato Client **Current Password** and the new **Password**.
3. Click **Save**.

### Resetting the Password with Multiple Accounts

For Cato partners and other users that have multiple SDP user accounts with the same username, use the **Advanced Settings** option to reset the password for a specific account.

**To reset the password for a specific account:**

1. At the User Portal login window, click **Forgot Password?**.

The **Email** window opens.
2. Enter the email for your SDP user account.
3. Click **Show Advanced Options**.
4. Enter the specific **Account** that you are resetting the password.
5. Click **Send**.

The reset password email is sent to the SDP user for the specific account.

## Working with Trusted Devices

For accounts or individual users that use Multi-Factor Authentication (MFA) for the Cato Client, the default behavior is to enter the extra authentication code each time they connect to the VPN. Admins can choose to set the time period that the MFA token is valid, during this time the user doesn't require MFA. Users select the **Don't ask me again on this device/computer** option on the Client to designate that device or computer as trusted.

> [!NOTE]
> Note:
> 
> As of February 2026, the My Devices page will no longer be available.

For more about configuring the MFA settings in the Cato Management Application section, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients).

**To configure a Client as a trusted device:**

1. Make sure that MFA is enabled and configured in the Cato Management Application for the entire account or specific SDP user.
2. Log in to the Cato Client with the username and password.
3. On the MFA screen, select **Don't ask me again on this device**.

![iOS-Client_resize.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31126651467549.png)
4. Enter the MFA code and click **Sign In**. After you are connected to the VPN, the device is trusted and MFA isn't required for the duration of the **Token Validity** setting.

### Showing the Trusted Devices

The User Portal shows all the devices and hosts for a user that are defined as trusted devices.

> [!NOTE]
> Note:
> 
> As of February 2026, the My Devices page will no longer be available.

**To show the trusted devices for a user:**

1. Log in to the User Portal.
2. The **My Devices** window shows the trusted devices.

![1679a2f4897174.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31126591490973.png)

## Changing the MFA Settings

The Cato Portal lets users make changes to the MFA settings for the Cato Client and the same settings are applied to the User Portal. For accounts that are configured for SDP users to use **Any Authentication Method** (MFA or SMS), they can change the MFA method that they are using. For example, someone who is using SMS to receive the MFA code can choose to use an authentication app (such as Google Authenticator) instead.

> [!NOTE]
> Note:
> 
> The **View/Change 2FA Settings** link is only shown for accounts that let SDP users choose any MFA option.

**To change the MFA settings:**

1. From the bottom of the **My Devices** window, click **View/Change 2FA Settings**.

![ChangeMFA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31126651505693.png)

The **My Account** window opens.
2. Click **Change Settings**.
3. In the pop-up window, enter the Cato Client password and click **Send**.

The **Secure your account window** opens and helps you change the MFA settings
4. Follow the steps in the **Secure your account window** to make the changes to the MFA settings.
5. Click **OK**.
