---
title: "How Cato MFA and Expiration Mechanism Works"
slug: "how-cato-mfa-and-expiration-mechanism-works"
updated: 2026-08-05T10:28:24Z
published: 2026-08-05T10:28:24Z
canonical: "knowledge.catonetworks.com/how-cato-mfa-and-expiration-mechanism-works"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How Cato MFA and Expiration Mechanism Works

Cato's MFA tokens are based on time windows, meaning they aren't valid for a constant time starting when they were generated, but instead they are valid in a constant window of time encompassing of when they were generated. The window size is 30 seconds, so no matter where the token is created it will be the same in the same 30 seconds window.

For VPN users, Cato supports both SMS and use an authentication app (such as Google Authenticator) as methods to deliver the token (token will be the same regardless of the delivery method). For usability purpose and in order to avoid user getting a code and while populating it, the code will expire, Cato provides a grace period of approximately 3 and half minutes so to account for the window that has just passed.

Resending auth code: A user can ask for a token twice (re-send auth code) and get the same code, or it may be different. i.e. asking for a code at 12:00:05 will give you the same code as 12:00:29. But asking for a code at 12:00:29 will be different than the code generated at 12:00:31.

When will Cato re-ask for authentication code: At this time, Cato supports up till 30 days or upon Geo-Changes, assuming a user has selected to trust the device he is connecting from. If a user has not selected to trust, then a code will be required upon the next login attempt.
