---
title: "Revoking a Remote User Session"
slug: "revoking-a-remote-user-session"
updated: 2026-08-30T09:23:20Z
published: 2026-08-30T09:23:20Z
canonical: "knowledge.catonetworks.com/revoking-a-remote-user-session"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoking a Remote User Session

This article explains how to revoke a remote user's session so they are forced to reauthenticate for continued access to your network.

## Overview

To maintain the compliance of remote users connecting to your network, you can revoke the session of a remote user. After a session is revoked, the remote user is prompted to authenticate in the Client using their configured [authentication method](/v1/docs/configuring-the-authentication-policy-for-cato-clients). On a Windows device, if the user does not authenticate within 10 minutes, WAN and Internet access is blocked for the remote user on any device. This reduces the risk of unauthorized access. To regain access, the remote user must authenticate in the Client using their configured authentication method.

By forcing the remote user to authenticate, the Client runs the configured device checks. For more information on the Client connection flow, see [Understanding the Cato Client Connection Flow](/v1/docs/understanding-the-cato-client-connection-flow).

Revoking a remote user's session is supported on all authentication methods, IdPs, and all supported Client versions.

### Use Case - Stolen Device

A remote user has Always-On enabled and authenticates with SSO with a token duration of 2 weeks. Their device is stolen creating a security risk of up to 2 weeks of unauthorized access. To mitigate the risk, the admin revokes the user's session preventing access to the network from the stolen device.

### Use Case - Unusual User Activity

Using the Stories Workbench, analysts at company ABC identified a user who is uploading a large amount of data to a file-sharing application. They are unsure if this action is being taken by the user for legitimate reasons or not. They revoke the user session to force reauthentication on the device. The analysts can then continue their investigation knowing that only a legitimate authenticated user can access the network from the device.

### Known Limitations

- Revoking a remote user's session is not supported for [Browser Access](/v1/docs/configuring-the-browser-access-portal).

## Revoking a Remote User's Session

Revoking a session helps you maintain control over user access.

![Revoke_User.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218209935773.png)

**To revoke a remote user's session:**

1. From the navigation menu, click **Access > Users**.
2. On the **Users Directory** tab, select the user(s) whose session you want to revoke.
3. From the **Actions** drop-down menu, select **Revoke Session**.

You can also revoke a user session from the **User Risk** page. For more information, see [Understanding the User Risk Level](/v1/docs/understanding-the-user-risk-level).
