---
title: "Authenticating Admins"
slug: "authenticating-admins"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/authenticating-admins"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticating Admins

This article describes the different authentication methods you can define for admins to log in to the Cato Management Application (CMA). To learn more about admins, see [What are Admins and Role-Based Access Control (RBAC)](/v1/docs/what-are-admins-and-role-based-access-control-rbac).

## Overview

To best fit the requirements of your organization, you can define the authentication methods for the CMA using the following methods:

- **SSO (recommended) -** Authenticate with the Single-Sign On (SSO) provider that is configured for the account in **Access > Single-Sign On**
- **Cato credentials -** Log in with the username (admin email) and password that you configure in the CMA
- **MFA -** When using Cato credentials, admins use Multi-Factor Authentication (MFA) with an authentication app. This option is enabled by default for new admins, and is always enabled for admins in accounts created after December 10th, 2023.

## Configuring the CMA Authentication Methods

You define which method or methods Cato Management Application admins can use to log in. These settings apply to all admins in the account.

The following tools are supported for SSO with CMA admins:

- [Microsoft Entra ID](/v1/docs/configuring-azure-sso-for-your-account)
- [Google](/v1/docs/configuring-google-sso-for-your-account)
- [PingFederate](/v1/docs/configuring-pingfederate-sso-for-your-account)
- [KeyCloak](/v1/docs/configuring-keycloak-sso)
- [OneLogin](/v1/docs/configuring-ldap-sync-and-sso-with-onelogin)
- [Okta](/v1/docs/configuring-okta-sso-for-your-account)

Make sure that your tool has allowlisted the required IPs. For details, see [CMA IP Allowlist](%%LINK:20511945810589%%). The email for each CMA admin must be the same as the email address for their corresponding user in the SSO provider.

**To configure the authentication methods for CMA admins:**

1. To allow admins to authenticate with SSO:
  1. Follow the procedure for your SSO provider (links above).
  2. From the navigation menu, click **Access > Single Sign-On**.
  3. In the **Cato Management Application Admins** section, select **Allow login with Single Sign-On**.
  4. Click **Save**.
2. To allow admins to authenticate with a username and password:
  1. From the navigation menu, select **Account > Login Restrictions**.
  2. In the **Login Authentication Method for Cato Management Application** section, select **Allow login with Cato user credentials**.
  3. Click **Save**.

## Using Multi-Factor Authentication (MFA) for Admins

To provide additional security, you can configure admins to use Multi-Factor Authentication (MFA) when they log in to the CMA. MFA uses an authentication app (such as Google Authenticator) to generate secure One-Time-Passwords (OTP) that the admin enters as part of the login process. Otherwise, the admin can't authenticate and log in to the CMA.

> [!NOTE]
> Notes:
> 
> - MFA is only supported for Cato user credentials. When admins log in with SSO, you can't require them to enter an MFA code.
> - For accounts created after December 10th 2023, MFA is always enabled for admins that use Cato User Credentials authentication.

### Disabling Multi-Factor Authentication for an Administrator

For accounts that support disabling MFA, after you create an admin, MFA is enabled by default for that admin. If MFA is enabled, the first time that the admin logs in to the CMA, he is redirected to a web page with a QR code. The admin uses the authentication app to scan the QR code, and the CMA MFA is added to the authentication app.

![Admin_General.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26255642416413(1).png)

**To enable MFA for an admin:**

1. From the navigation menu, click **Account > Administrators**.
2. Select the admin.
3. In the **Login Details** section, select **MFA enabled**.
4. Click **Save**.

### Resetting Multi-Factor Authentication

You can reset the MFA permissions for an admin. After you reset the MFA permissions, the admin can no longer use the current authenticator app to log in to the CMA. The next time that the admin logs in to the CMA, he is redirected to a web page with a QR code. The admin uses the authentication app to scan the QR code and the CMA MFA is added to the authentication app.

**To reset the MFA permissions for an admin:**

1. From the navigation menu, click **Account > Administrators**.
2. Select one or more administrators.
3. From the **Actions** drop-down menu, select **Reset MFA**.
4. In the confirmation window, click **OK**. An email notification is sent to the admin.

## Managing Admin Passwords

By default, admins are required to change their passwords for the CMA every 90 days and they receive email notifications 14 days and 3 days before the password expiration date. When you enable the **Password never expires** option for an admin, that admin is never required to change his password.

Admin passwords must contain one lowercase letter, one uppercase letter, one number, one special character, and must be between 8-32 characters. Additionally, admin passwords cannot contain an email address or be on our list of common passwords (e.g., “Password1!”).

### Setting the Administrator Password Expiration

Use the **Password Expiration** setting in the **Login Restrictions** screen to define how long the CMA password is valid for, before the admin is required to change it. The password can be valid for 14 to 730 days.

This setting doesn't apply when the **Password never expires** option is enabled for an admin.

**To set the password expiration for an admin:**

1. From the navigation menu, select **Account > Login Restrictions**.
2. In the **Password Expiration** section, enter how many days the password is valid for.
3. Click **Save**.

### Resetting the Administrator Password

If an administrator is locked out of the account, use the Reset Passwords option to let them log in again.

**To reset an administrator's password:**

1. From the navigation menu, click **Account > Administrators**.
2. Select one or more administrators.
3. Click **Actions** and then from the drop-down menu, select **Reset Password**.
4. In the confirmation window, click **OK**.

The administrator receives an email with a link to change the password.
5. In the email, the admin can click the **here** link to go to the Change Password window.

If the admin receives this email, but did not initiate the request, click the **It wasn't me** link.

## Setting Login Restrictions for Admins

You can require all administrators to only log from specific IP addresses.

For accounts that use egress IP addresses (NATed IPs), you can allow admins to log in from these IP addresses. If you enable the checkbox to ​**Also** **allow logins from the NATed IPs**​​, you must specify the IPs in the ​**Allowed Login IPs​​** area. Otherwise, the admins will be access the CMA from any IP.

![loginrestrictions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26255672830493(1).png)

**To configure admin login restrictions:**

1. From the navigation menu, select **Account > Login Restrictions**.
2. To only allow admins to log in to the CMA from specific IP addresses:
  1. In the **Login Restrictions for Cato Management Application** section, in **Allowed Login IPs**, enter the IP address to allow.
  2. Click the add icon.

The IP address is added to the Allowed Login IPs list.
  3. To remove an allowed IP address, select the IP address and then click the delete icon.
3. (**Optional**) To allow admins to log in from a translated IP, select **Also allow logins from the NATed IPs**.
4. Click **Save**.

## Understanding Secure Login with CAPTCHA

To enhance account security, the admin authentication flow for the CMA includes CAPTCHA protection. The CAPTCHA protection is invisible to the admin and runs in the background to prevent unauthorized access by bots. This ensures a safer experience without disrupting the regular login process. In rare cases, admins may be prompted to re-enter their credentials to prove they are human and complete the login. CAPTCHA protection is not relevant for SSO-authenticated admins.
