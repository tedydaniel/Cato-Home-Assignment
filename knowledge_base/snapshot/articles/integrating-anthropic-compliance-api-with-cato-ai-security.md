---
title: "Integrating Anthropic Compliance API with Cato AI Security"
slug: "integrating-anthropic-compliance-api-with-cato-ai-security"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/integrating-anthropic-compliance-api-with-cato-ai-security"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Anthropic Compliance API with Cato AI Security

Cato AI Security integrates with your Anthropic Compliance API to track user activities and pull logs of all the conversations with Claude.

## Deployment Steps

**To connect Cato AI Security to Anthropic:**

1. In Claude.ai, navigate to the **Settings > Data Management** page of your account.
2. In the **Compliance access keys** section, click **Create key**.

If you do not see the Compliance access keys section, it means that either you are not a Primary Owner of the organization or that the Compliance API is not enabled for your organization, and the Primary Owner needs to contact support to request access.

![anthropic_access_keys.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36706034539293.png)
3. Provide the following information:
  - **Name** - a descriptive name for this key, e.g., Cato AI Sec
  - Select the following scopes:
    - read:compliance_activities
    - read:compliance_user_data

![anthropic_access_scope.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36706050113949.png)
4. Click **Create**. Make sure to copy the key, as you will not be able to access it again once you click **Close**. ![anthropic_save_key.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36706050115229.png)

## Configure the Connection in Cato

**To configure the connection in the CMA:**

1. Navigate to **AI Security > Integrations** and under **Anthropic Compliance API**, click **Connect**.
2. In the **API token** field, enter the value you copied in step 4, above.
