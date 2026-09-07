---
title: "Anthropic Integration with AI Security"
slug: "anthropic-integration-with-ai-security"
updated: 2026-07-06T08:18:41Z
published: 2026-07-06T08:18:41Z
canonical: "knowledge.catonetworks.com/anthropic-integration-with-ai-security"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Anthropic Integration with AI Security

Cato AI Security integrates with your Anthropic Compliance API to track user activities and pull logs of all the conversations with Claude.

## Deployment Steps

### To connect Cato AI Security to Anthropic:

1. In Claude.ai, navigate to the **Settings > Data Management** page of your account.

2. In the Compliance access keys section, click **Create key**.

   If you do not see the Compliance access keys section, it means that either you are not a Primary Owner of the organization or that the Compliance API is not enabled for your organization, and the Primary Owner needs to contact support to request access.

![01_Anthropic_panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_Anthropic_panel.png){height="" width=""}


3. Provide the following information:
   - **Name** - a descriptive name for this key, e.g., **Cato AI Sec**
   - Select the following scopes:
     - `read:compliance_activities`
     - `read:compliance_user_data`

![02_Anthropic_create.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_Anthropic_create.png){height="" width=""}

4. Click **Create**. Make sure to copy the key as you will not be able to access it again once you click **Close**.

![03_Anthropic_save.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_Anthropic_save.png){height="" width=""}


## Configure the Connection in Cato

**To configure the connection in the CMA:**

1. Navigate to **AI Security > Integrations** and under **Anthropic Compliance API**, click **Connect**.
2. In the **API token** field, enter the value you copied in step 4 above.
3. Click **Test Connection** to verify the integration.
4. Click **Connect**.
