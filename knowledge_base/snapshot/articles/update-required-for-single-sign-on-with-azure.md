---
title: "Update Required for Single Sign-On with Azure"
slug: "update-required-for-single-sign-on-with-azure"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/update-required-for-single-sign-on-with-azure"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Required for Single Sign-On with Azure

Azure Single Sign-On (SSO) is not correctly configured in your account. As recommended by Azure, you have not provided Cato with consent to access user’s data in your Azure tenant. Cato requires this data to authenticate users.

Starting October 15th, 2023, Azure SSO authentication to the Client will only be available if consent has been provided.

## What Is the Impact to My Account?

Starting October 15th, 2023, users will only be able to authenticate to the Client if you have given consent for Cato to access user’s data. Without Cato receiving this consent, users will not be able to authenticate with Azure SSO.

Granting tenant-wide admin consent for Cato requires you to sign in to Azure as a user authorized to give consent on behalf of the organization (a Global Administrator or Privileged Role Administrator). For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent?pivots=portal).

## How Do I Provide Cato Consent to Access User's Data?

You can use the Single Sign-On settings in the Cato Management Application to provide Cato with the required consent to access user data in your Azure tenant.

**To provide Cato with consent to access user’s data:**

1. In the Cato Management Application, navigate to **Access > Single Sign-On.**

1. Click **Microsoft Credentials.** The ​**Permissions requested​​** pop up window is displayed.

1. In the **Permissions requested** pop up window, click **Accept.**

Users will not be disconnected or required to re-authenticate as a result of this change.

For more information, see [Configuring Azure SSO for Your Account.](/v1/docs/configuring-azure-sso-for-your-account)

## Who Do I Talk to If I Have Questions?

Please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
