---
title: "SSO Authentication Fails When Using External Browser | localhost Error"
slug: "sso-authentication-fails-when-using-external-browser-localhost-error"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/sso-authentication-fails-when-using-external-browser-localhost-error"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SSO Authentication Fails When Using External Browser | localhost Error

## Description

Cato SDP Client isn't able to authenticate via SSO when using an external browser.

## The Problem

When using the external browser with SSO authentication, the browser will load http://localhost:49152 during the authentication process. It’s possible that the browser will enforce HTTP Strict Transport Security (HSTS) for the localhost domain and redirect to https://localhost:49152. If this happens, the browser will display an error and authentication will fail.

Example from Microsoft Edge

![edge-example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/9199022697629.png)

## The Solution

1. Switch to the embedded browser for SSO authentication. It has to be enabled for the account under **Access > Client Access > Authentication** in the CMA, or else the client will switch back to the external browser during the authentication process.
2. If using the external browser for authentication is desired, HSTS for the localhost domain can be disabled in the default browser. **Note:** HSTS for the localhost domain may be re-enabled by other local web apps, usually in a dev environment. Using the embedded browser is the preferred solution.

**Chrome/Edge**

1. Paste the relevant URL in the address bar: **Chrome:** chrome://net-internals/#hsts **Edge:** edge://net-internals/#hsts
2. Under the **Delete domain security policies** section, in the **Domain** field, enter **localhost** and click the **Delete** button. ![chrome-example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/9199036814749.png)
3. Restart the Cato SDP Client authentication process.

**Firefox**

1. Close all open tabs in Firefox.
2. Press Ctrl + Shift + H (Cmd + Shift + H on Mac) to open the Library window (History).
3. Enter **localhost** in the search bar.
4. Right-click the localhost entry and select **Forget About This Site**. ![firefox-example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/9199038009629.png)
5. Restart the Cato SDP Client authentication process.
