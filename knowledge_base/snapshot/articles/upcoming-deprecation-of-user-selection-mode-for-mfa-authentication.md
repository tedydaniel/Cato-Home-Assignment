---
title: "Upcoming Deprecation of User Selection Mode for MFA Authentication"
slug: "upcoming-deprecation-of-user-selection-mode-for-mfa-authentication"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upcoming-deprecation-of-user-selection-mode-for-mfa-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upcoming Deprecation of User Selection Mode for MFA Authentication

In your [Client Authentication Policy](/v1/docs/configuring-the-authentication-policy-for-cato-clients), you configured **User Selection** Mode for MFA Authentication. This means MFA is the default authentication method for remote users in the Cato Client. However, MFA Authentication can be bypassed, and remote users can authenticate and connect to your network using only a username and password. From May 12th, 2024, to increase the security of your account, this option will no longer be available at an account or user level. To continue to use MFA, you need to change your Client Authentication Policy mode to **Enabled** before this date. Alternatively, if you do not want to use MFA, you can change your default authentication method to **User & Password**.

You can override the account policy and customize settings for specific users to allow them to connect with only their username and password. For more information, see [Configuring the Authentication Policy for Cato Clients.](/v1/docs/configuring-the-authentication-policy-for-cato-clients)

## What is the Impact to the Account?

If you do not update your Cato Client Authentication Policy by May 12th, 2024, some users may not be able to authenticate and connect to your network.

## What Action do I Need to Take?

This is how your Client Authentication Policy (Access > Client Access > Authentication) is currently configured:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/ff8c2707-b47c-dfc0-56d5-4ec249238a95.png)

Before May 12th, 2024, you must make one of these changes to your Client Authentication Policy.

#### Option 1

Change the **Mode** for the MFA authentication method to **Enabled**.

For more information on how to change your Client Authentication Policy, see [Configuring the Authentication Policy for Cato Clients.](/v1/docs/configuring-the-authentication-policy-for-cato-clients)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/cc3c05af-cd20-5d65-ac6d-715ee77c4386.png)

#### Option 2

Change the **Default Method** for authentication in your account to **User & Password**.

For more information on how to change the default authentication method, see [Configuring the Authentication Policy for Cato Clients.](/v1/docs/configuring-the-authentication-policy-for-cato-clients)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/f7eff207-7578-1b79-9c0a-b4f38ac81937.png)

## What are the Changes to my Account?

After May 12th, 2024, your Client Authentication Policy will look like this:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/7764aa98-f82e-a170-6991-43f81727474b.png)

## Who Do I Talk to If I Have Questions?

Please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
