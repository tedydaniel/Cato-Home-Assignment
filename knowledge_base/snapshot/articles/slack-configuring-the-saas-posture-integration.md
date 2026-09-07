---
title: "Slack: Configuring the SaaS Posture Integration"
slug: "slack-configuring-the-saas-posture-integration"
updated: 2026-08-18T14:28:12Z
published: 2026-08-18T14:28:12Z
canonical: "knowledge.catonetworks.com/slack-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack: Configuring the SaaS Posture Integration

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the Slack Integration

To configure the Slack integration, create an app.

### Prerequisites

- Slack Enterprise Grid license

### Step 1: Configure the Integration in your Slack Tenant

In the Slack API Portal, identify the OAuth Token to enter into the CMA.

**Add the Org Owner to Every Workspace**

1. In the Slack Console, navigate to **Tools & Settings > Organization settings** and from the sidebar, click **Workspaces**.
2. Select a workspace, open **Members** and click **Add members**.
3. Select the Org Owner performing the setup and click **Add to workspace**.
4. Repeat steps 1-4 for every workspace in your organization.

**Create an Organization-Level App**

1. Sign in to the [Slack API Portal](https://api.slack.com/apps) with an **Org Owner** account on the Enterprise Grid organization.
2. Click **Create an App**.
3. Select **From a manifest**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(23).png)
4. In the **Pick a workspace to develop your app** dropdown, select the organization-level entry.
5. In the manifest editor, paste the following YAML:

```yaml
display_information:
  name: Cato SaaS Posture
  description: Read-only Slack posture and audit log access for Cato Networks SaaS Posture monitoring.
oauth_config:
  scopes:
    user:
      - admin.users:read
      - admin.teams:read
      - admin.conversations:read
      - admin.apps:read
      - auditlogs:read
      - users:read
      - users:read.email
      - channels:read
      - groups:read
      - team:read
settings:
  org_deploy_enabled: true
  socket_mode_enabled: false
```
6. Click **Next**, then **Create**.
7. In the app's navigation, navigate to **Settings > Install App**.
8. Click **Install to Organization**.
9. Click **Allow**.
10. Copy and save the **User OAuth Token** so it can be entered into the CMA.

**Add the App to Every Workspace**

1. In the Slack Console, navigate to **Tools & Settings > Organization settings** and from the sidebar, click **Integrations**.
2. On the **Installed Apps** tab, find the **Cato SaaS Posture** app, click on the three dots, and select **Add to more workspaces**.
3. Select every workspace in the organization and check the **Default for future workspaces** checkbox.
4. Click **Next**, then **I'm ready to add this app**, and click **Add App**.

**Note**: When adding scopes to an existing app, reapprove it at the organization level and reinstall or update its workspace installations so every workspace receives the new scopes.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations.**
2. Click the **Configured Integrations** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop-down, select **SaaS Posture**.
6. Add the details created during step one.
  - **Admin Bearer Token:** The User OAuth Token token you created in step one
7. Click **Save**.

The app is visible on the **Integrated Apps** table with a **Connected** status.
