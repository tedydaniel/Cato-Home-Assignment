---
title: "Configuring LDAP Sync and SSO with OneLogin"
slug: "configuring-ldap-sync-and-sso-with-onelogin"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/configuring-ldap-sync-and-sso-with-onelogin"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring LDAP Sync and SSO with OneLogin

This article explains how to use LDAP to import and sync OneLogin users and configure OneLogin as an SSO provider for Cato users.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

## High-Level Overview of LDAP Sync and SSO with OneLogin

This is a high-level overview of the process to configure and integrate OneLogin with your Cato account. After you configure OneLogin to synchronize users with Cato, you can also configure OneLogin as an SSO provider for users.

1. In OneLogin, configure the virtual LDAP settings.
2. In the Cato Management Application, add the OneLogin domain to your account.
3. Add the OneLogin domain controller to the domain.
4. In OneLogin, create an OpenID Connect application to allow Cato to use OneLogin to authenticate users.
5. Import the groups (OneLogin roles) to your account.
6. Select OneLogin as the SSO provider for users.

> [!NOTE]
> Note:
> 
> To use OneLogin as an SSO provider, you must configure LDAP sync between OneLogin and Cato. This requires that the VLDAP service is enabled on your OneLogin account.

## Configuring the Virtual LDAP Settings

To enable SSO and LDAP sync for OneLogin and your Cato account, use the **Authentication** window in OneLogin to enable virtual LDAP and disable multi-factor authentication (MFA). This window also has the Login DN settings that you use to configure the domain in the Cato Management Application.

VPN SSO requires that the OneLogin VLDAP service is enabled. If you are only using OneLogin for LDAP sync, then you don't need to enable VLDAP.

Due to a OneLogin limitation, each LDAP sync is limited to 500 users. For accounts with more than 500 users, run the LDAP sync multiple times.

**To configure the virtual LDAP settings in OneLogin:**

1. In OneLogin, from the menu bar, select **Authentication > VLDAP**.

![OneLogin_VLDAP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24786689839645.png)
2. For accounts that are using SSO, make sure that **Enable VLDAP Service** is enabled.
3. Clear **Multi-factor authentication** to disable MFA for your OneLogin account.
4. In **Virtual distinguished name**, copy the **Virtual DN**. You will enter the virtual DN in[Adding a New Domain for OneLogin](/v1/docs/configuring-ldap-sync-and-sso-with-onelogin#adding-a-new-domain-for-onelogin) (below).
5. Click **Save**. The virtual LDAP settings are configured.

## Configuring the Cato Management Application to Perform LDAP Sync with OneLogin

Add your OneLogin account to the Cato Management Application as a new domain in Directory Services. Then define the domain controller for this domain.

### Adding a New Domain for OneLogin

Use the **Directory Services** window to add a new domain to your account. Then configure the OneLogin LDAP settings for the domain.

**To add a new OneLogin domain to Directory Services:**

1. From the navigation menu, click **Access > Directory Services**.
2. From the **LDAP** section or tab, and click **New**.

The **New Directory Service** panel opens.
3. Enter the **Name** of the domain in the LDAP server.
4. Configure the OneLogin authentication settings in the **LDAP Authentication Connection** section in **Login DN**:

![OneLogin_LDAP_Details.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24786717972637.png)
  1. In **Login DN**, paste the virtual LDAP that you copied above in *Configuring the Virtual LDAP Settings*.
  2. Change the cn to the email address for your OneLogin account.
  3. In **Base DN**, paste the virtual LDAP and delete the **cn** and **ou**. The screenshot above shows these settings:
    - Login DN: cn=admin@samplenetworks.com,ou=users,dc=sample-networks,dc=onelogin,dc=com
    - Base DN: dc=sample-networks,dc=onelogin,dc=com
  4. Enter the admin **Password** for your OneLogin account.
  5. Enable **Use SSL**.
5. Click **Save**. The OneLogin domain is added to the Cato Management Application.
6. Click **Test Connection** to make sure that Cato can connect to your OneLogin account.

### Configuring the Domain Controller for OneLogin

After you configure and save the OneLogin domain, configure the settings for the domain controller. Use the host setting that is appropriate for your OneLogin account:

- US - ldap.us.onelogin.com
- Europe - ldap.eu.onelogin.com

For more about the OneLogin host settings, see the OneLogin [documentation](https://onelogin.service-now.com/support?id=kb_article&amp;sys_id=c94b4578db5ce450ca1c400e0b96191c&amp;kb_category=da76e930db185340d5505eea4b961990#tips).

**To configure the domain controller:**

1. From the **LDAP** section or tab, edit the domain for your OneLogin account.
2. From the **Edit Directory Service** navigation menu, select **Domain Controllers**.
3. From the drop-down window, select **IP or Host**.

![OneLogin_DCOM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24786712204061.png)
4. Enter the OneLogin host for the US or for Europe and click **Add**.

Since SSL is enabled for the domain, the host uses port 636.
5. Click **Save and Close**. The domain controller is added to the OneLogin domain.

## Configuring the OneLogin Application for OpenID Connect

Create a new app in OneLogin that allows the Cato to use OneLogin to authenticate SDP users. Then configure it to connect to Cato.

> [!NOTE]
> Note:
> 
> There is a legacy Cato Networks app in the OneLogin marketplace which currently isn't supported. We recommend that you don't use this app.

### Creating a New App

Create a new Open ID Connect application in OneLogin.

**To create the OpenID Connect application:**

1. In your OneLogin account, from the menu bar select **Applications > Applications**.
2. Click **Add App**.
3. Search for **OpenId Connect** and select the app.
4. In the **Add OpenID Connect (OIDC)** window, enter the **Display Name** for the app.
5. Click **Save**.

### Configuring the OpenID Connect App

Configure the OneLogin app to Cato to support SSO for the SDP users. Cato performs LDAP sync with OneLogin according to the roles and not according to the OneLogin groups.

For new SDP users with Windows Client v5.1 and higher, there is an additional Redirect URI to configure for the OneLogin app. This URI isn't required for earlier versions, or for existing users that are upgrading to the Windows Client v5.1 or higher.

**To configure the app to connect to Cato:**

1. From the left-hand navigation menu, select **Configuration**.
2. In **Redirect URI's**, enter these URIs:
  - https://sso.via.catonetworks.com/auth_results
  - https://sso.proxy.catonetworks.com/auth_results
  - https://auth.catonetworks.com/oauth2/broker/code/onelogin
  - https://auth.us1.catonetworks.com/oauth2/broker/code/onelogin
  - https://auth.in1.catonetworks.com/oauth2/broker/code/onelogin
  - https://auth.jp1.catonetworks.com/oauth2/broker/code/onelogin
  - https://auth.catonetworks.com/endsession/callback
  - https://auth.in1.catonetworks.com/endsession/callback
  - https://auth.jp1.catonetworks.com/endsession/callback
  - https://auth.us1.catonetworks.com/endsession/callback
  - (for new remote users for Windows Client)
    - https://sso.ias.catonetworks.com/auth_results
    - https://169.254.255.254/auth_results
3. From the left-hand navigation menu, select **SSO**, and configure these SSO settings:
  1. Set the **Application Type** to **Web**.
  2. Set the **Authentication Method** to **POST**.
  3. Copy the **Client ID** and the **Client Secret**. Paste these settings in the [Configuring OneLogi as the SSO Provider for SDP Users](/v1/docs/configuring-ldap-sync-and-sso-with-onelogin#configuring-onelogin-as-the-sso-provider-for-sdp-users) section below.
4. Click **Save**.
5. Add the application to the relevant OneLogin users and roles.
6. Perform the initial LDAP sync. In the Cato Management Application, in the **Directory Services** screen, click **Sync Now**.

## Configuring OneLogin as the SSO Provider for SDP Users

In the Cato Management Application, you can configure OneLogin as the global SSO provider for SDP users and admins in your account.

For admins, make sure that the email for the CMA admin is the same as the email address in OneLogin.

**To configure OneLogin as the SSO provider:**

1. From the navigation menu, select **Access > Single Sign-On**.
2. Click **New**
3. From the **Identity Provider** drop-down menu, select **OneLogin**.
4. Enter a **Name**.
5. Enter these settings:
  - **Client ID** - as you copied from OneLogin above
  - **Edit Client Secret** - as you copied from OneLogin above
  - **OneLogin Domain prefix** - your domain as defined in your OneLogin account
  - **OneLogin Domain suffix** - select **onelogin.com**
6. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers).
7. Click **Apply**.
8. Select **Allow login with Single Sign-On** for one or more types of users in your account:
  - SDP Client users (set the **Token validity** settings)
  - Clientless SDP users (set the Cookie type)
  - Cato Management Application admins
9. Click **Save**. OneLogin is configured as the SSO provider for SDP users in your account.
