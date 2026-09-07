---
title: "Client Connectivity Policy - Continuous Posture Checks (Check Policy)"
slug: "client-connectivity-policy-continuous-posture-checks-check-policy"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/client-connectivity-policy-continuous-posture-checks-check-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Client Connectivity Policy - Continuous Posture Checks (Check Policy)

## Overview

The Client Connectivity Policy includes Device Posture Checks that validate the posture of a device. In the **Check Policy** settings, you can configure how often the Client runs these checks.

Device Posture Checks can run continuously at configured intervals, including before the Client connects to the Cato Cloud. This helps keep device posture data up to date and can reduce Client connection time.

The possible configurations are:

- **Continuous checks, even when disconnected (recommended):** The Client continuously checks the device posture at the configured intervals, even if the Client is not connected to the Cato Cloud
- **Check on connect and while connected**: The Client continuously checks the device posture at the configured intervals, only if the Client is connected to the Cato Cloud
- **One-time check**: The Client checks the device posture only during the connection process

To understand the user experience if a periodic check fails, see [Configuring the Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy).

> [!NOTE]
> Notes:
> 
> - The Check Policy is supported from Windows Client v5.15 and macOS Client v5.9 and higher.
> - When enabled, device posture collection for all users (remote and onsite) includes all of the device checks (regardless of the Device Posture Profiles definition in the CMA).

## Configuring the Check Policy

The **Check Policy** defines how often the Client runs Device Posture Checks and when the checks are performed.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144410402077.png)

**To configure Check Policy:**

1. From the navigation menu, select **Resources > Device Posture**.
2. Click the **Check Policy** tab.
3. Choose your required configuration (the recommended option is **Continuous checks, even when disconnected)**
4. If required, set the frequency of the check (the recommended frequency is 10 minutes).
5. Click **Save**.
