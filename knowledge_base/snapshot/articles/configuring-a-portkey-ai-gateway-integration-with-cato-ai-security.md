---
title: "Configuring a Portkey AI Gateway Integration with Cato AI Security"
slug: "configuring-a-portkey-ai-gateway-integration-with-cato-ai-security"
updated: 2026-08-02T15:15:01Z
published: 2026-08-02T15:15:01Z
canonical: "knowledge.catonetworks.com/configuring-a-portkey-ai-gateway-integration-with-cato-ai-security"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a Portkey AI Gateway Integration with Cato AI Security

## Overview

Cato AI Security lets you inspect and enforce policy for AI traffic that flows through your existing Portkey AI Gateway. Instead of configuring each application separately, you connect the gateway to a Cato Guard and apply centralized monitoring, data protection, and policy enforcement to gateway traffic.

This article explains how to configure a Portkey AI Gateway integration, map homegrown apps, and validate policy enforcement in Guard Logging.

## Prerequisites

Before you start, make sure these requirements are met:

- AI Security license that supports AI Gateway Guards
- Admin permissions for **AI Security > Guards** and **AI Security > Guards Interaction Policy**
- Deployed and working Portkey AI Gateway
- Permission to restart or reload the Portkey AI Gateway
- Connection parameters for each homegrown app you want to map
- Test app or client that sends traffic through the AI Gateway
- Network access from Portkey to `https://api.aisec.catonetworks.com`

## Configuration Workflow

The integration includes these stages:

| Stage | Task | Result |
| --- | --- | --- |
| 1 | Create an AI Gateway Guard | Cato creates the Guard and provides connection details for Portkey |
| 2 | Configure Portkey | Portkey sends AI traffic to Cato for inspection |
| 3 | Map a homegrown app | Cato attributes gateway traffic to a specific homegrown app |
| 4 | Configure policy enforcement | Cato applies AI Security policy rules to matching traffic |

## Create the AI Gateway Guard

Create an AI Gateway Guard to define the Cato enforcement point for Portkey traffic.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/AI-Gateway_portkey.png)

**To create the guard:**

1. From the navigation menu, select **AI Security > Guards**.
2. Click **New**.
3. In **Guard Name**, enter a name for the guard.

Example: `Portkey-Sample`
4. In **Type**, select **AI Gateway**.
5. In **AI Gateway Integration Type**, select **LiteLLM**.
6. In **Guard's Host**, select **Cato's Cloud**.
7. Leave **Homegrown Agent Mapping** empty.
8. Click **Save**.

After you save the Guard, it is ready to receive traffic from the Portkey AI Gateway. The Guard is active, but it does not enforce rules until you configure a policy rule.

Map homegrown apps after validating the gateway integration.

## Configure Portkey

Configure Portkey with the guard connection details so the AI Gateway can send traffic to Cato for inspection.

### Retrieve the Guard Connection Details

**To retrieve the guard connection details:**

1. From the navigation menu, select **AI Security > Guards**.
2. Select the AI Gateway Guard.
3. Copy the connection details from the guard configuration.

The guard connection details include:

- API keys
- Guardrails configuration snippet
- Cato API base URL

The guardrails configuration uses this structure:

```json
curl -i https://api.portkey.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-portkey-api-key: <PORTKEY_API_KEY>"\
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "hi my email is joe@acme.com"}
    ]
  }'
```

The key fields are:

| Field | Description |
| --- | --- |
| `x-portkey-api-key` | Authenticates Portkey to the Cato Guard |
| `model` | Defines the LLM model that Portkey sends the request to |
| `messages` | Contains the user prompt that Portkey sends to the LLM and that Cato inspects |

Store the API key securely and avoid committing it to source control. If your deployment supports environment variables or a secrets manager, use that method instead of storing the key directly in the Portkey settings.

### Configure the Cato Plugin in Portkey

To send Portkey AI Gateway traffic to the Cato Guard, enable the Cato Networks plugin in your Portkey organization settings and configure it with the Guard deployment details from Cato.

1. In Portkey, click your organization settings.

2. Go to the **Plugins** page.

3. Search for the Cato Networks plugin.

4. Enable the Cato Networks plugin.

5. In the plugin settings, enter the values from the Guard deployment page in Cato:

- API Key

- API Base URL

6. Click **Update**.

After the plugin is enabled, Portkey can authenticate to Cato Guard and send LLM inputs and outputs for inspection.

### Create a Portkey Guardrail for Cato Networks

After you enable and configure the Cato Networks plugin, create a Portkey Guardrail that uses the plugin to send LLM inputs and outputs to Cato for inspection.

If you want visibility for each homegrown app, create a separate Portkey Guardrail for each app. If you only need visibility at the Guard level, you can use a single Portkey Guardrail.

1. In Portkey, go to the **Guardrails** page.

2. Click **Create**.

3. In **Available Checks**, click the **Partner** tab.

4. Search for Cato Networks.

5. In the **Cato Networks Guardrail** card, click **Add**.

6. Enter a name for the Guardrail.

7. Click **Save**.

### Connect the Homegrown App to a Portkey Config and API Key

Portkey uses configs and API keys to route traffic through a specific Guardrail. To apply the Cato Guardrail to your homegrown app traffic, copy the Guardrail ID, create a config that references the Guardrail, and then create an API key that uses the config.

If you want visibility for each homegrown app, create a separate Portkey config and API key for each app. If you only need visibility at the Guard level, you can use a single config and API key.

1. In Portkey, go to the **Guardrails** page.
2. Copy the ID of the Cato Guardrail that you created.
3. Go to the **Configs** page.
4. Click **Create**.
5. Edit the config to include the Guardrail ID in both `input_guardrails` and `output_guardrails`.

```json
{ "retry": { 
    "attempts": 3 }, 
    "cache": { 
    "mode": "simple" }, 
    "input_guardrails": [ "pg-portke-sampleID" ], 
    "output_guardrails": [ "pg-portke-sampleID" ] 
}
```
6. Replace sampleID with the Guardrail ID that you copied earlier.
7. Click **Save**.
8. Go to the **API Keys** page.
9. Click **Create New**.
10. Enter a name for the API key.
11. Select the config that you created.
12. Click **Create**.

## Verify Gateway Traffic in Cato (Optional)

Use Guard Logging to confirm that Portkey traffic reaches Cato.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/AI-Gateway_Interaction-Explorer.png)

**To verify gateway traffic in Cato:**

1. Generate a test prompt from your app.
2. From the navigation menu, select **AI Security > Interaction Explorer**.
3. From the **Guard** dropdown, filter the selection by your guard.
4. Confirm that the log entry shows the guard name

At this point, the **Homegrown Agent** column shows a dash (`-`) for each entry. This is expected because no homegrown apps are mapped to the guard yet.

In this stage, Cato logs gateway traffic. After app mapping, Cato also attributes traffic to the specific homegrown app.

## Map a Homegrown App to the Guard

In Cato, map the app using the Portkey Guardrail **name**. You can map a homegrown app from the guard configuration or from the homegrown app configuration. This procedure uses the guard configuration.

**To map a homegrown app to the guard:**

1. From the navigation menu, select **AI Security > Guards**.
2. Select the AI Gateway Guard.
3. In **Homegrown Agent Mapping**, click **Add Mapping**.
4. In **Homegrown Agent**, select the homegrown app.

Example: `Portkey-sample-1`
5. In **Virtual Key Alias**, enter the Portkey Guardrail **name** for the app.
6. Click **Save**.

## Verify App Attribution

Verify that Cato attributes gateway traffic to the mapped homegrown app.

**To verify app attribution:**

1. Send a test request from the mapped homegrown app through Portkey.
2. From the navigation menu, select **AI Security > Interaction Explorer**.
3. Filter the view by the mapped **Homegrown Agent**.

Example: `Portkey-sample-1`
4. Confirm that the **Homegrown Agent** column shows the mapped app.

When the app is mapped correctly, Guard Logging shows the app name instead of a dash (`-`).

## Configure a Guards Interaction Policy Rule

Configure a Guards Interaction Policy rule to enforce AI Security controls on matching LiteLLM traffic.

Before you create a rule, understand how scope affects enforcement:

| Scope | Enforcement behavior |
| --- | --- |
| Guard only | Applies to all traffic through the selected AI Gateway Guard |
| Specific Homegrown Agents | Applies only to traffic from the selected homegrown apps |

**To configure a Guards Interaction Policy rule:**

1. From the navigation menu, select **AI Security > Guards Interaction Policy**.
2. Click **New**.
3. In **Name**, enter a name for the rule.

Example: `Block PII`
4. Use the **Enabled** toggle to enable the rule.

The toggle is green when enabled.
5. In **Guards**, select the AI Gateway Guard.

Example: `Portkey-sample-1`
6. In **Agents**, select the mapped homegrown app.

Example: `Portkey-sample-1`
7. In **Engine Profile**, select the profile used to detect the relevant content.

Example: **Personal Identifier**
8. In **Action**, select the enforcement action.

Example: **Anonymize & Monitor**
9. Click **Save**.
10. Click **Publish**.

After the policy is published and propagated, the rule is enforced on matching traffic.

## Verify Policy Enforcement

Verify policy enforcement by sending test traffic that matches the rule scope and engine profile.

**To verify policy enforcement:**

1. Send a test request from the mapped homegrown app through LiteLLM.
2. Include content that matches the selected **Engine Profile**.
3. From the navigation menu, select **AI Security > Guards**.
4. Select the AI Gateway Guard.
5. Open **Guard Logging**.
6. Filter the logs by the mapped **Homegrown Agent**.
7. Confirm that **Violated Rules** shows the policy rule.

Example: `Block PII`

Traffic that does not match the selected **Engine Profile** shows no violated rules and passes through normally.
