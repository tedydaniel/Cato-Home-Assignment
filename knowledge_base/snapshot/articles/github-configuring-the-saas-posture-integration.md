---
title: "GitHub: Configuring the SaaS Posture Integration"
slug: "github-configuring-the-saas-posture-integration"
status: "update"
updated: 2026-09-03T12:02:54Z
published: 2026-09-03T12:02:54Z
canonical: "knowledge.catonetworks.com/github-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub: Configuring the SaaS Posture Integration

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the GitHub Integration

To configure the GitHub integration, create a new Personal access token.

### Prerequisites

- You must have purchased a **GitHub Enterprise Cloud** or **GitHub Enterprise Server** license.
- The organization you are connecting must be attached to a GitHub Enterprise account.

### Step 1: Configure the Integration in the GitHub Developer Center

In the GitHub Developer Center, identify the access token to enter into the CMA.

**To configure the GitHub integration:**

1. Sign in to your [GitHub account](https://github.com/login) with the user designated to own the token.
2. Navigate to **Personal access tokens > Tokens (classic)** and click **Generate new token → Generate new token (classic)**.
3. Configure these details:
  - **Note:** A recognizable label
  - **Expiration:** Do not set an expiration
  - **Scopes:** Select the following:
    - `admin:org`
    - `read:org`
    - `read:audit_log`
    - `read:enterprise`
    - `repo`
    - `user`
4. Click **Generate Token**
5. Copy and save the token so it can be entered into the CMA.
6. For organizations that enforce SAML SSO only:
  1. Navigate to **Personal access tokens > Tokens (classic)**
  2. Locate the new token row and click **Configure** **SSO**
  3. For each organization that enforces SAML SSO, click **Authorize** and sign in via the organization's identity provider.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations.**
2. Click the **Configured Integrations** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop-down select **SaaS Posture**.
6. Add the details created during step one.
  - **Enterprise Name:** The enterprise slug
  - **Admin Bearer Token:** The token you created in step one
7. Click **Save**.

The app is visible on the **Integrated Apps** table with a **Connected** status.
