---
title: "Cato Client Login Errors"
slug: "cato-client-login-errors"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/cato-client-login-errors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Client Login Errors

This article shows common error messages which may be displayed when using the Cato Client.

**Note:** If the below action items do not solve the login error, we recommend collecting [SDP Client logs](/v1/docs/collecting-client-logs) and contacting [Cato Support](/v1/docs/submitting-a-support-ticket) for further troubleshooting.

| Error message | Possible Reason | Action Items |
| --- | --- | --- |
| "Can't login to the SSO provider. Please try again, or copy the Details and send them to your network admin" | IdP provider blocked authentication attempts | Check IdP logs to find the reason |
| "Incorrect username. Please try again, or copy the Details and send them to your network admin" | - Cato could not find the username. - The user is not imported into CMA. - The user has no assigned SDP license. | Confirm that the username entered matches CMA's user configuration and whether it's imported in CMA with an assigned [SDP license](/v1/docs/assigning-ztna-licenses-to-users) |
| "Internal Cato error. Please try again, or copy the Details and send them to your network admin" | - Misconfigured user password/MFA. - Internal PoP error. | - Confirm that the user is [fully configured](/v1/docs/managing-sdp-clients-with-the-cato-user-portal). - Collect [Client logs](/v1/docs/collecting-client-logs) and report the issue to [Cato Support](/v1/docs/submitting-a-support-ticket) |
| "Internal authentication error. Please try again, or contact your network admin" | - Wrong credentials. - Invalid MFA token. - Invalid SSO cookie. | - Check the user's credentials. - [Reset password or MFA](/v1/docs/managing-sdp-clients-with-the-cato-user-portal). - Clear [SSO cookies](/v1/docs/recording-issues-using-the-cato-client). |
| "Unable to connect to server. Please try again later" "Connection error. Make sure you are connected to the internet and try again. Contact your admin for additional support" | - The client is unable to resolve the necessary URLs - Some client processes cannot run - Ports UDP/53, TCP/443, and UDP/443 are blocked - Cato PoPs are not reachable via the Internet | - Confirm that the URLs and processes listed in [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client) are allowed on the end device - Confirm that the URLs listed in [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client) can be resolved with the local DNS server - Confirm that the necessary ports are allowed. Alternatively, port 1337 can be forced, as explained in [this article](/v1/docs/configuring-a-different-udp-port-for-the-cato-client) - Confirm that no other VPN Client is installed on the device. - Check Internet Connectivity |
| "Can’t connect to the Internet. Please check your Internet connection (or WiFi) and try again" | The client failed to find a valid network adapter with a valid IP address and/or a valid default gateway | Check the device's network adapter |
| "Your device is not compliant with the enterprise posture. Please contact your administrator" | The device does not meet device posture requirements | Review Client Connectivity Policy Events and policy configuration as described in [Configuring the Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) |
| "Cato SDP service error. Please restart the Cato Client and try again" | - Client service crash - Client Error due to OS Sleep State | Collect [Client logs](/v1/docs/collecting-client-logs) and report the issue to [Cato Support](/v1/docs/submitting-a-support-ticket) |
| "Incorrect registration code. Please try the code again or contact your network admin" | Trying to add a user with an invalid registration code | Confirm that the user has a valid registration code as described in [Activating Users with a Registration Code](/v1/docs/activating-users-with-a-registration-code) |
| "Secured Private Access is unavailable" | The user gets "Internet Only" access in High Confidence | Check Client Connectivity Policy actions for High and Any confidence levels as described in [Remote Internet Security with One Time Authentication](/v1/docs/remote-internet-security-with-one-time-authentication) |
