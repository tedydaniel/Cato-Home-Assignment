---
title: "Action Required: Upgrade Azure SSO to the latest Version"
slug: "action-required-upgrade-azure-sso-to-the-latest-version"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/action-required-upgrade-azure-sso-to-the-latest-version"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Required: Upgrade Azure SSO to the latest Version

Microsoft has released a new version of the Azure Single Sign-On (SSO) integration. To benefit from the latest Azure and Cato functionality, you must upgrade your Azure SSO integration to Cato.

## What Action Do I Need to Take?

Upgrade your Azure SSO integration from the Cato Management Application (CMA) by following these steps:

1. In the CMA, navigate to **Access > Single Sign-On**.
2. Click edit on your **Azure SSO** configuration.
3. Click Upgrade **Azure**.
4. You are redirected to the **Azure authentication page**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34663024570397(1).png)
5. Select your Azure account.
6. When prompted, click **Confirm** to associate your Azure tenant with your Cato account.

After completing these steps, a confirmation message appears indicating that the Azure tenant is successfully associated with the Cato account.

## What are the Benefits of Upgrading?

The following features are supported by the latest Azure version (and not the old version), and are available to enable:

- [Admin CMA login](/v1/docs/authenticating-admins)
- [Clientless access](/v1/docs/browser-application-portal-overview-securing-remote-access-to-applications) (Application portal)
- [Seamless authentication](/v1/docs/authenticate-users-automatically-with-windows-credentials)
- [Browser extension](/v1/docs/what-is-the-cato-browser-extension)
- [Enterprise browser](/v1/docs/what-is-the-cato-enterprise-browser)

## What are the Impacts to My Account?

If you do not upgrade, you cannot benefit from the features listed above.

Once you upgrade, connected users remain authenticated. After users disconnect their Cato Client, they are prompted to re-enter their credentials on the next connection. This re-authentication occurs **only once** after the upgrade.
