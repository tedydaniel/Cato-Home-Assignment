---
title: "Reviewing Security Checks for SaaS Apps"
slug: "reviewing-security-checks-for-saas-apps"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/reviewing-security-checks-for-saas-apps"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reviewing Security Checks for SaaS Apps

This article describes how to use the Security Checks screen to review the risk analysis for the SaaS Security API connectors in your account.

> [!NOTE]
> Note:
> 
> Please contact [SaaSecAPI@catonetworks.com](mailto:SaaSecAPI@catonetworks.com) or your official Cato reseller for more information about using the App & Data API Protection policy.

## Overview of the Security Checks

SaaS Security API connectors let you integrate third-party SaaS apps with your Cato account, which then lets Cato automatically review the security posture for each connector. The Security Checks screen shows the status of Cato's risk analysis for the connectors and recommendations for how to improve the security for the relevant connector.

You can easily see the recommended **Security Practice** and **Risk** level for each connector and it's current security status. At the top of the screen is a summary bar that shows the status for all the **Security Practices** for a connector.

![Security_Checks.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27186392444189.png)

**To show the Security Checks for the connectors in your account:**

- From the navigation pane, select **Security > App & Data API** and select **Security Checks**.

These are the columns in the Security Checks screen:

- **Category** - Cato's category for the **Security Practice**, for example **Identity** for user management and authentication.
- **Security Practice** - Description of the specific security check.
- **Risk** - Risk level of the **Security Practice** based on the analysis of Cato's Security team, the values are: **Low**, **Medium**, and **High**.
- **Status** - Current status of the **Security Practice**, the values are: **Passed**, **Partial**, **Failed**, or **Skipped**.

Cato's Security team determines the thresholds for the **Status** for each **Security Practice**. A practice can have the status of **Passed** even if less than 100% of the **Issues** meet the security requirements.

A status of **Skipped** indicates the checks couldn't be completed, for example if there were issues accessing the app data.
- **Issues** - Total number of items for the **Security Practice** that don't meet the security requirements.

In the example above shows the Security Checks for the Microsoft 365 connector. For **Require MFA for users**, 20 out of 49 users in the Microsoft 365 account are not required to authenticate with MFA.
