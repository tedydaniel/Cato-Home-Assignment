---
title: "Understanding Expiring Session for Users"
slug: "understanding-expiring-session-for-users"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/understanding-expiring-session-for-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Expiring Session for Users

Users are authenticated to the Cato Cloud for the duration of the SSO or MFA session. When the session expires, users are disconnected from the Cato Cloud and must re-authenticate in order to reconnect. The Cato Management Application lets you configure the duration of the authentication token for the Cato Client, when the token expires so does the session.

A message appears in the Windows notification area when the session is about to expire. A notification also appears in the Cato Client and gives users the option to re-authenticate. This means users can re-authenticate to the Client without disconnecting from the Cato Cloud and interrupting the session.

> [!NOTE]
> Note:
> 
> For accounts with Always-on enabled, when the SSO or MFA session expires, end-users cannot connect to the Internet, however, they will still have 10 minutes of access after the SSO or MFA token expires. When users click on **Reconnect**, they will reauthenticate and be able to use the Internet again.

To provide the best user experience, the message behavior depends on the duration of the SSO or MFA token that you configured in the Cato Management Application in one of the following screens:

- SSO token (entire account) - Access > Single Sign-On
- MFA token (entire account) - Access > Authentication > User Authentication
- MFA and SSO token (individual users) - Access > Users > {user name} > User Configuration > Authentication

The MFA and SSO token settings for individual users take precedence and override the account settings.

When the message is shown to the user, the message is continuously shown and counts down until the token and the session expires. If users click **Reconnect**, they re-authenticate and the message disappears. If users do not click **Reconnect**, when the session expires they are disconnected.

| Token Expiration Settings in the Cato Management Application | Message Behavior in the Cato Client |
| --- | --- |
| 48 hours (or more) | Message is shown 24 hours before the token expires |
| Less than 48 hours, and more than 24 hours | Message is shown 12 hours before the token expires |
| 24 hours (or less) | Message is shown 2 hours before the token expires |

## Prerequisites

- The expiring session message is supported from Windows Client v5.3 and higher

## Sample Expiring Session for an User

In this example, an user authenticates to the Cato Client with SSO.

1. The SSO session will expire in 1 day.
2. A message appears in the Cato Client: **This session expires in 1 Days.**.
3. At a convenient time, the user clicks **Reconnect**, and then re-authenticates to the Cato Client.

The Client reconnects to the Cato Cloud with no disruption to the user.

![session_exp__notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218260159901.png)
