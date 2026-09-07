---
title: "Configuring Azure SSO for Your Account"
slug: "configuring-azure-sso-for-your-account"
updated: 2026-07-15T08:21:09Z
published: 2026-07-15T08:21:09Z
canonical: "knowledge.catonetworks.com/configuring-azure-sso-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Azure SSO for Your Account

This article explains how to configure Azure as the Single Sign-On (SSO) provider for SDP users, clientless users, and Cato Management Application (CMA) admins in your account.

SSO relies on an encrypted token from Cato and your IdP to validate that the user is authenticated and allowed to connect to the network. For more details, see [SSO Authentication for Users with Cato](/v1/docs/sso-authentication-for-users-with-cato).

For more about enabling SSO for the account, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

## Configuring Single Sign-On

With the Cato Single Sign-On (SSO), you can allow Cato users to use their existing Identity Provider (IdP) credentials without the need for dedicated credentials from Cato Networks. Users can connect to Cato using their email address or UPN (User Principal Name) as defined in Azure.

### Overview of SSO with Your Cato Account

After a chain of trust is established between Cato, the IdP, and your company's user directory, Cato trusts the IdP for user authentication.

Cato SSO supports these Client operating systems:

- Windows
- macOS
- iOS
- Android
- Linux

### Known Limitations

- Azure in China is not supported

### Preparing to Configure SSO with Azure

Before you establish trust with Azure, make sure that you complete these prerequisites:

- You must have Global Administrator or Privileged Role Administrator privileges to Azure, using the same email for Azure and the CMA

**Note:** The integration will fail if the CMA admin doesn't have an Entra ID account.
- For LDAP, Azure must be synchronized with your user directory in your Cato account
- For manually created SDP users, SSO is supported for Windows v5.x, macOS v5.x, and Linux v5.x Clients
  - For iOS and Android, only users who were imported from your organization to Cato using LDAP or SCIM provisioning are able to use SSO.
- The **Profile** for each Azure user must have a valid **Email** address.

## Configuring SSO with Microsoft

This section explains how to configure SSO with Microsoft Azure from the Cato Management Application.

![Azure.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32771455195677.png)

**To configure SSO with Microsoft for your account:**

1. From the navigation menu, select **Access > Single Sign-On**.
2. Click **New**.
3. From the **Identity Provider** drop-down menu, select **Microsoft Azure**.
4. Enter a **Name**.
5. Click **Apply** and in the Single Sign On page, click **Save**.
6. In the Single Sign On page, click on the provider you just created.
7. Click **Set up Microsoft Consent**.

The **Permissions requested** pop up window is displayed.

**Note:** Click **Apply** and then click **Save**. Then edit the entry for the **Setup Microsoft Consent link** to be enabled.

![Permission_requested.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32771455224605.png)
8. In the **Permissions requested** pop up window, click **Accept**. See below for more information.
9. If prompted by the CMA to associate your Azure tenant with your Cato account, click **Confirm**.
10. If you are configuring one Single Sign-On provider, enable the **Default** toggle. If you are configuring multiple Single Sign-On providers, see [Configuring Multiple Identity Providers](/v1/docs/configuring-multiple-identity-providers)
11. Click **Apply**.
12. Select **Allow login with Single Sign-On** for one or more types of users in your account:
  - SDP Client users (set the **Token validity** settings)
  - Clientless SDP users (set the Cookie type)
  - Browser Extension users
  - Cato Management Application admins
13. Click **Save**. The Azure SSO settings for your account are configured

## Granting Cato Permissions

This section explains how to use the Cato Management Application to enable SSO with Microsoft Azure AD or Office 365.

To identify users, Cato requires consent to access user's data. As part of the configuration process, an administrator must grant the Cato SSO application access to data on behalf of your users. This does not provide admin rights on the Azure tenant. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/manage-consent-requests#evaluate-a-request-for-tenant-wide-admin-consent).

Granting tenant-wide admin consent for Cato requires you to sign to Azure as a user authorized to consent on behalf of the organization (a Global Administrator or Privileged Role Administrator). For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent?pivots=portal).

For SDP Client users, when you configure the Token validity settings you define in **Days** or **Hours** the amount of time that users remain authenticated. Users that are logged in must reauthenticate when the duration you define in **Days** or **Hours** (since they last logged in) has been reached. The **Always Prompt** options means that users must always authenticate to the Client.

### Required Permissions

To enable SSO, Cato requires the following permissions to be granted. These permissions are automatically requested by Cato during the configuration process. You do not need to manually create an Enterprise Application.

![Azure.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32771509557021.png)

| API Name | Claim value | Permission |
| --- | --- | --- |
| Microsoft Graph | email | View users' email address |
| Microsoft Graph | offline_access | Maintain access to data you have given it access to |
| Microsoft Graph | openid | Sign users in |
| Microsoft Graph | profile | View users' basic profile |
| Microsoft Graph | User.Read | Sign in and read user profile |

## Troubleshooting Azure SSO Connections

| Issue | Probable Cause | Resolution |
| --- | --- | --- |
| AADSTS50105: The signed in user is not assigned to a role ... | Azure Active Directory Application settings for Cato application not configured correctly. | 1. Access your account in the Microsoft Azure portal. 2. In the menu, click **Azure Directory Services**. 3. In the sub menu, under **MANAGE**, click **Enterprise applications**. 4. In the sub menu, under **MANAGE**, click **All applications**. 5. In the right panel, in the applications list, click **Cato Cloud**. 6. In the sub menu, under **MANAGE**, click **Properties**. 7. In the right panel, in the parameter **User assignment required?**, click **No**. 8. Using the client, reauthenticate to the Cato VPN. |
| User enters credentials and is returned to the login page without authenticating | The **Profile** for this Azure user doesn't have a valid **Email** address. | Add the valid email address to the Azure **Profile** for this user. |
| AADSTS90008: The user or administrator has not consented to use the application | You have not provided Cato with consent to access user’s data in your Azure tenant | Provide Cato with consent to access user's data. For more information, see [Update Required for Single Sign-On with Azure](/v1/docs/update-required-for-single-sign-on-with-azure). |
