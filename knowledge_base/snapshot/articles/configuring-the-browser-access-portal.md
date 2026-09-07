---
title: "Configuring the Browser Access Portal"
slug: "configuring-the-browser-access-portal"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/configuring-the-browser-access-portal"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Browser Access Portal

This article discusses how to configure the settings for the Browser Access Portal and how clientless SDP users are authenticated.

## Configuring the Basic Settings for the Browser Access Portal

The Browser Access **Settings** tab shows the **Portal URL** for end-users to access the portal. The URL is based on the subdomain for the account. You can use letters and numbers in the subdomain. Dashes are valid **only when the account is first created** (the subdomain initially matches the account name). If you later attempt to edit the subdomain, dashes are no longer allowed, and you'll receive an error message. For more about the subdomain for your account, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

To define a custom branded logo for the portal, see [Customizing Browser Application Portal](/v1/docs/customizing-browser-application-portal).

You can also define if users can authenticate to the portal using their Cato username and password. Use the **Single Sign-On** screen to enable users to authenticate with the SSO provider.

**To configure the basic settings for the Browser Access Portal:**

1. From the navigation menu, click **Access > Browser Access Control**.
2. On the **Settings** tab, enable the **Applications Portal** slider.
3. Click **Save**.

## Authenticating Clientless Users to the Browser Access Portal

The Browser Access Portal supports authenticating users with the SSO provider for the account, and also the user credentials for the Cato Management Application. You can choose to use one or both of these methods.

For more about configuring SSO for your account, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

**Configuring Browser Access Cookies**

Configure the Browser Access Portal to use persistent or session cookies. For persistent cookies, you can configure the time duration that the cookie is valid. After this time, the user needs to log in to the Browser Access Portal again.

If you use session cookies, then when users close the browser or end the session they are immediately logged out of the Browser Access Portal. If the session is idle for more than the configured **Duration**, then the session expires and the user needs to log in to the Browser Access Portal again.

The following screenshot shows the cookies policy configured for Browser Access users in the **Single Sign-on** screen:

![Clientless_SSO.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25891520218781.png)

**To configure the authentication settings for Browser Access users:**

1. To let Browser Access users to log in using the SSO provider:
  1. From the navigation menu, click **Access > Single Sign-On**.
  2. In the **Clientless SDP Users** section, select **Allow login with Single Sign-On**.
  3. In **Cookie type**, select the type of authentication cookies that the Browser Access Portal uses: **Session** or **Persistent**.
  4. Set the **Duration** for which the cookie is valid.
  5. Click **Save**.
2. To let Browser Access users authenticate with their Cato user credentials:
  1. From the navigation menu, click **Access > Applications Portal**.
  2. In the **Authentication** section, select **Allow login with Cato user credentials**.
  3. Click **Save**.

## Defining the NAT IP Range for the Browser Access Portal

You can define the range of translated source IP addresses for the users that connect to the Browser Access Portal. For example, some applications use an Access Control List (ACL) to only allow connections from a specific IP range. We recommend that you define the NAT IP address range, and then enable the source NAT IP range for each of the relevant Browser Access applications.

> [!NOTE]
> Note:
> 
> You can use one of the private IP ranges for the Browser Access NAT IP range. This IP range is only used between the portal and the application server.

**To define the source NAT IP range for the Browser Access Portal:**

1. In the **Settings** section or tab, in **NAT IP Range** enter the source NAT IP range with the CIDR subnet.
2. Click **Save**.
3. To enable an application to use the source NAT IP range:
  1. In the **Applications** tab or section, edit the application. The **Edit Application** panel opens.
  2. Select **Use source NAT IP range**.
  3. Click **Apply** and then click **Save**.

## Allowing Access from Generic Domains

To authenticate to the application portal using SSO, the SSO domain must be included in the Allowed Domains.

You can also list generic domains that are allowed to use Browser Access. This provides Browser Access to third-party clientless SDP users and prevents domains that are not listed from using Browser Access.

The Allowed Domain is applied to all of the Access Policy rules in your account.

> [!NOTE]
> Note:
> 
> Browser Access users that you create manually, are allowed to access the portal with username and password from any domain.

**To add Allowed Domains to the Browser Access portal:**

1. From the navigation menu, click **Access > Applications Portal**.
2. On the **Settings** tab, in the **Allowed Domains** section, click the plus sign (![Domain_plus.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25891520247581.png)).
3. Add the domain(s) you want to be able to use Browser Access. Separate multiple domains with a comma. If your organization authenticates using SSO, you must include the SSO domain or access will be blocked.
4. Click **Save**.
