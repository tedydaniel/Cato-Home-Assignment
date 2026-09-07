---
title: "ChatGPT Integration with AI Security"
slug: "chatgpt-integration-with-ai-security"
updated: 2026-09-02T12:16:47Z
published: 2026-09-02T12:16:47Z
canonical: "knowledge.catonetworks.com/chatgpt-integration-with-ai-security"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ChatGPT Integration with AI Security

Create a ChatGPT connector in the Cato Management Application (CMA) to monitor prompts with AI Security.
## Overview
Cato AI Security uses the ChatGPT Enterprise Compliance API to monitor prompts.

- **Unified AI Auditing** - AI Security uses the ChatGPT Enterprise Compliance API to consume conversation history and add it to the unified AI engine. Our customers use this auditing for security detections, adoption analytics, compliance, and eDiscovery.
- **Prompt detection and response** - AI Security runs a detection engine with pre-defined signals for risky interactions and customizable data detections.
- **AI asset management** - AI Security creates a list of all GPTs and other types of AI assistants.
- **Knowledge and capabilities mapping and risk management** - AI Security graphs the relationships between users, assistants, knowledge, and the outer world to clarify the risks.
- **Scanning for GPTs misconfigurations and remediation** - AI Security scans your AI assets with a predefined list of over 100 types of misconfigurations found by


## Creating a ChatGPT Admin Key for AI Security

To enable prompt monitoring for the OpenAI connector, create a workspace-scoped ChatGPT Admin key with the permissions required for the integration. Cato AI Security uses this access to retrieve workspace activity and conversation data for inspection and policy enforcement.

The Compliance Platform is available for eligible managed ChatGPT workspaces, including ChatGPT Enterprise and Edu. To monitor conversation content, a workspace Owner must create or authorize the Admin key.

For more information, see the [OpenAI Admin API reference](https://chatgpt.com/admin/api-reference#tag/Introduction).

**To create a ChatGPT Admin key for the AI Security integration:**

1. Sign in to the [OpenAI Admin Console](https://admin.openai.com/) and select the ChatGPT workspace to monitor.

2. Go to **Credentials > Admin keys**.

3. Select **Create new admin key** and enter a descriptive name.

4. Select **Custom** permissions, then grant the compliance and conversation-message read permissions required by Cato AI Security.

5. Set an appropriate expiration, create the key, and securely copy the secret. OpenAI displays the secret only once.

6. In the CMA, configure the ChatGPT connector with the Admin key.

If the required compliance or conversation-message permission is unavailable, contact OpenAI Support.

## Connecting ChatGPT Compliance API

**To connect AI Security to ChatGPT Enterprise:**

1. From the CMA navigation menu, click **AI Security > Integrations**.
3. In **ChatGPT Compliance API**, click **Connect**.
![ai_sec_chat_Gpt.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/ai_sec_chat_Gpt.png){height="" width=""}

4. In the **Add ChatGPT Compliance API** panel, add the following details:

   - API Key
   - Workspace ID
   - Workspace Name

5. Click **Test Connection** to verify the integration.
6. Click **Connect**.
