---
title: "SSO Session Behavior for Windows SDP Client"
slug: "sso-session-behavior-for-windows-sdp-client"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/sso-session-behavior-for-windows-sdp-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SSO Session Behavior for Windows SDP Client

This article discusses the behavior of the Single Sign-On (SSO) authentication session regarding the IdP token and Cato token with the Windows Client.

## Overview

End-users are authenticated to the Cato Client based on Cato's authentication token. The duration of this token is configured in the Cato Management Application. The duration of the IdP authentication token is based on the settings for the IdP. The starting time for these tokens is not synced, so even if they are set to the same duration, they usually expire at different times. When both tokens are expired, the user must re-authenticate to the IdP. For more about SDP user session expiration, see [Understanding Expiring Session for SDP Users](/v1/docs/understanding-expiring-session-for-users).

This article explains the Client behavior when the Cato token has expired, but the IdP token is still valid. This behavior is different depending on the Client version.

> [!NOTE]
> **Notes:**
> 
> - For all Client versions, as long as the Cato token is valid the user is authenticated (even if the IdP token has expired).
> - For accounts that set the **Token validity** setting to **Always Prompt** instead of **Duration**, the SDP user must authenticate to the IdP for each time they connect with the Client. The IdP token is ignored.

For more about SSO authentication sessions, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

## Windows Client v5.x Token Expiration Behavior

This section describes how the Client automatically re-authenticates when the Cato token expires and the IdP token is still valid for Windows Client v5.0 and higher.

10 minutes before the Cato token expires, the Client attempts to automatically re-authenticate with the IdP with no impact or messages to the end-user. When the IdP token is valid, the Client automatically re-authenticates and Cato generates a new SSO token based on the token duration settings for the account.

You configure the amount of time that the Cato token is valid in the Cato Management Application (Access > Single Sign-On). For more information about the user experience and expiring tokens, see [Understanding Expiring Session for SDP Users](/v1/docs/understanding-expiring-session-for-users).

If both tokens are expired, the end-user authenticates to the IdP and then a new Cato token is generated.

### Example of Windows Client v5.x Token Expiration Behavior

This is an example of the session behavior for Windows Client v5.0 and higher.

1. The user authenticates to the Client by entering the IdP credentials (username and password). The IdP generates an SSO token for the user.
2. A Cato token is generated with a duration of 10 days (based on the Single Sign On settings in the Cato Management Application).
3. 10 days later - 10 minutes before the Cato token expires, the Client attempts to silently re-authenticate to the IdP token.
  1. If the IdP token is valid, the Client automatically re-authenticates with no impact to the user (the session is not interrupted). The Cato token is valid for another 10 days.
  2. If the IdP token is expired, the user is prompted to authenticate to the IdP, and then the Cato token is valid for another 10 days (the session is not interrupted).

If the user does not re-authenticate to the IdP, then the session expires after the remaining 10 minutes ends.

### Client SSO Re-authentication Message Behavior for Windows Client v5.0 (and Higher)

When the user's session is going to expire soon, the Client shows a [message to users](/v1/docs/understanding-expiring-session-for-users) to let them easily re-authenticate. The goal of this message is to provide the best user experience, so the message behavior depends on the settings for the IdP and Cato token.

The following table explains the re-authentication experience for SDP users based on the different settings for the duration of the Cato and IdP token.

| IdP Token Duration | Cato Token Duration | Client Message Behavior | SDP User Experience |
| --- | --- | --- | --- |
| 2 days | 7 days | The IdP token is expired. The Client shows the message 24 hours before Cato token expires. | The SDP user clicks **Reconnect** and re-authenticates to the IdP. |
| 7 days | 2 days | The IdP token is still valid. The Client shows the message 24 hours before the Cato token expires. | The SDP user clicks **Reconnect**, and the Client automatically re-authenticates to the IdP. |
| 23 hours | 3 days | The IdP token is expired. The Client shows the message 24 hours before Cato token expires. | The SDP user clicks **Reconnect** and re-authenticates to the IdP. |
| 23 hours | 36 hours | The IdP token is still valid. The Client shows the message 12 hours before the Cato token expires. | The SDP user clicks **Reconnect**, and the Client automatically re-authenticates to the IdP. |
| 23 hours | 14 hours | The IdP token is still valid. The Client shows the message 2 hours before the Cato token expires. | The SDP user clicks **Reconnect**, and the Client automatically re-authenticates to the IdP. |

### Windows Client v4.7 (and Earlier) Token Expiration Behavior

This section describes how the end-user re-authenticates when the Cato token expires and the IdP token is still valid for Windows Client v4.7 and earlier. The Client automatically disconnects, and the end-user clicks **Connect**, then the Client automatically re-authenticates using the valid IdP token. You configure the amount of time that the Cato token is valid for in the Cato Management Application (Access > Single Sign-On).

#### Example of Windows Client v4.7 (and Earlier) Token Expiration Behavior

1. The user authenticates to the Client by entering the IdP credentials (username and password). The IdP generates an SSO token for the user.
2. A Cato token is generated with a duration of 10 days (based on the Single Sign-On settings in the Cato Management Application).
3. After 10 days, the Cato token expires and the Client automatically disconnects.
  1. If the IdP token is valid, in the Client . The user clicks **Connect** and is re-authenticated, the Cato token is valid for another 10 days.
  2. If the IdP token is expired, the user is prompted to authenticate to the IdP, and then the Cato token is valid for another 10 days (the session is not interrupted).
