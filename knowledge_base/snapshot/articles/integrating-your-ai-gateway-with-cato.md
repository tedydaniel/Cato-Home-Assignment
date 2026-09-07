---
title: "Configuring a LiteLLM AI Gateway Integration with Cato AI Security"
slug: "integrating-your-ai-gateway-with-cato"
updated: 2026-07-21T11:19:55Z
published: 2026-07-21T11:19:55Z
canonical: "knowledge.catonetworks.com/integrating-your-ai-gateway-with-cato"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a LiteLLM AI Gateway Integration with Cato AI Security

## Overview

Cato AI Security lets you inspect and enforce policy for AI traffic that flows through your existing LiteLLM AI Gateway. Instead of configuring each application separately, you connect the gateway to a Cato Guard and apply centralized monitoring, data protection, and policy enforcement to gateway traffic.

This article explains how to configure a LiteLLM AI Gateway integration, map homegrown apps, and validate policy enforcement in Guard Logging.

## Prerequisites

Before you start, make sure these requirements are met:

- AI Security license that supports AI Gateway Guards
- Admin permissions for **AI Security > Guards** and **AI Security > Guards Interaction Policy**
- Deployed and working LiteLLM AI Gateway
- Access to edit the LiteLLM `config.yaml` file
- Permission to restart or reload the LiteLLM AI Gateway
- LiteLLM Virtual Key and Key Alias for each homegrown app you want to map
- Test app or client that sends traffic through the LiteLLM AI Gateway
- Network access from LiteLLM to `https://api.aisec.catonetworks.com`

## Configuration Workflow

The integration includes these stages:

| Stage | Task | Result |
| --- | --- | --- |
| 1 | Create an AI Gateway Guard | Cato creates the Guard and provides connection details for LiteLLM |
| 2 | Configure LiteLLM | LiteLLM sends AI traffic to Cato for inspection |
| 3 | Map a homegrown app | Cato attributes gateway traffic to a specific homegrown app |
| 4 | Configure policy enforcement | Cato applies AI Security policy rules to matching traffic |

## Create the AI Gateway Guard

Create an AI Gateway Guard to define the Cato enforcement point for LiteLLM traffic.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/AI-Gateway_New.png)

To create the Guard:

1. From the navigation menu, select **AI Security > Guards**
2. Click **New**
3. In **Guard Name**, enter a name for the Guard

Example: `LiteLLM Test`
4. In **Type**, select **AI Gateway**
5. In **AI Gateway Integration Type**, select **LiteLLM**
6. In **Guard's Host**, select **Cato's Cloud**
7. Leave **Homegrown Agent Mapping** empty
8. Click **Save**

After you save the Guard, it is ready to receive traffic from the LiteLLM AI Gateway. The Guard is active, but it does not enforce rules until you configure a policy rule.

Map homegrown apps after validating the gateway integration.

## Configure LiteLLM

Configure LiteLLM with the Guard connection details so the AI Gateway can send traffic to Cato for inspection.

### Retrieve the Guard Connection Details

To retrieve the Guard connection details:

1. From the navigation menu, select **AI Security > Guards**
2. Select the AI Gateway Guard
3. Copy the connection details from the Guard configuration

The Guard connection details include:

- API keys
- LiteLLM guardrails configuration snippet
- Cato API base URL

The LiteLLM guardrails configuration uses this structure:

```yaml
guardrails:
  - guardrail_name: cato_networks
    litellm_params:
      guardrail: cato_networks
      mode: [pre_call, post_call]
      api_key: <AI_GATEWAY_API_KEY>
      api_base: "https://api.aisec.catonetworks.com"
      default_on: true
```

The key fields are:

| Field | Description |
| --- | --- |
| `mode: [pre_call, post_call]` | Sends prompts to Cato before the LLM request and responses to Cato after the LLM response |
| `api_key` | Authenticates LiteLLM to the Cato Guard |
| `default_on: true` | Enables the Guard by default for the traffic covered by this LiteLLM configuration |

Store the API key securely and avoid committing it to source control. If your deployment supports environment variables or a secrets manager, use that method instead of storing the key directly in `config.yaml`.

### Update the LiteLLM Configuration

You can configure the Cato guardrail globally for all LiteLLM traffic or apply it to specific model definitions, depending on your LiteLLM deployment. The example below applies the guardrail to the `travel-bot-model`.

To update the LiteLLM configuration:

1. Open the LiteLLM `config.yaml` file
2. Add the Cato guardrails configuration to the relevant model definition
3. Replace the placeholder API key with the API key from the Guard
4. Save the file
5. Restart or reload the AI Gateway if required for your LiteLLM deployment

Example LiteLLM configuration:

```yaml
model_list:
  - model_name: travel-bot-model
    litellm_params:
      model: openai/openai.gpt-oss-120b
      api_base: "https://bedrock-mantle.eu-north-1.api.aws/v1"
      api_key: "[LLM_API_KEY]"
      ssl_verify: false
    guardrails:
      - guardrail_name: travel-bot-model
        litellm_params:
          guardrail: cato_networks
          mode: [pre_call, post_call]
          api_key: "cato-xxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
          api_base: "https://api.aisec.catonetworks.com"
          default_on: true
```

## Verify Gateway Traffic in Cato (Optional)

Use Guard Logging to confirm that LiteLLM traffic reaches Cato.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/AI-Gateway_Interaction-Explorer.png)

To verify gateway traffic in Cato:

1. Generate a test prompt from your app.
2. From the navigation menu, select **AI Security > Interaction Explorer**
3. From the **Guard** dropdown, filter the selection by your Guard.
4. Confirm that the log entry shows the Guard name

At this point, the **Homegrown Agent** column shows a dash (`-`) for each entry. This is expected because no homegrown apps are mapped to the Guard yet.

In this stage, Cato logs gateway traffic. After app mapping, Cato also attributes traffic to the specific homegrown app.

## Verify Gateway Traffic in LiteLLM (Optional)

Use LiteLLM logs to confirm that requests are processed end-to-end by the AI Gateway and the Cato Guard.

To verify the integration in LiteLLM:

1. Send a test request through the LiteLLM AI Gateway
2. Open the LiteLLM logs
3. Confirm that the request includes the expected model and provider routing
4. Confirm that the request completed successfully

The logs can include:

- Model and provider routing
- Token counts
- Request duration
- Success status

Use both Cato Guard Logging and LiteLLM logs to confirm that requests are processed end-to-end.

## Map a Homegrown App to the Guard

Map a homegrown app so Cato Networks can attribute AI Gateway traffic to the correct app.

In LiteLLM, create a Virtual Key for each application that you want Cato to identify separately.

1. In LiteLLM, navigate to **Virtual Keys**
2. Copy the **Key Alias** for each homegrown app you want to add to your Guard

In Cato, map the app using the LiteLLM **Key Alias**. You can map a homegrown app from the Guard configuration or from the homegrown app configuration. This procedure uses the Guard configuration.

To map a homegrown app to the Guard:

1. From the navigation menu, select **AI Security > Guards**
2. Select the AI Gateway Guard
3. In **Homegrown Agent Mapping**, click **Add Mapping**
4. In **Homegrown Agent**, select the homegrown app

Example: `TravelBot`
5. In **Virtual Key Alias**, enter the LiteLLM Key Alias for the app
6. Click **Save**

## Verify App Attribution

Verify that Cato attributes gateway traffic to the mapped homegrown app.

To verify app attribution:

1. Send a test request from the mapped homegrown app through LiteLLM
2. From the navigation menu, select **AI Security > Interaction Explorer**
3. Filter the view by the mapped **Homegrown Agent**

Example: `TravelBot`
4. Confirm that the **Homegrown Agent** column shows the mapped app

When the app is mapped correctly, Guard Logging shows the app name instead of a dash (`-`).

## Configure a Guards Interaction Policy Rule

Configure a Guards Interaction Policy rule to enforce AI Security controls on matching LiteLLM traffic.

Before you create a rule, understand how scope affects enforcement:

| Scope | Enforcement behavior |
| --- | --- |
| Guard only | Applies to all traffic through the selected AI Gateway Guard |
| Specific Homegrown Agents | Applies only to traffic from the selected homegrown apps |

To configure a Guards Interaction Policy rule:

1. From the navigation menu, select **AI Security > Guards Interaction Policy**
2. Click **New**
3. In **Name**, enter a name for the rule

Example: `Block PII`
4. Use the **Enabled** toggle to enable the rule

The toggle is green when enabled.
5. In **Guards**, select the AI Gateway Guard

Example: `LiteLLM Test`
6. In **Agents**, select the mapped homegrown app

Example: `TravelBot`
7. In **Engine Profile**, select the profile used to detect the relevant content

Example: **Personal Identifier**
8. In **Action**, select the enforcement action

Example: **Anonymize & Monitor**
9. Click **Save**
10. Click **Publish**

After the policy is published and propagated, the rule is enforced on matching traffic.

## Verify Policy Enforcement

Verify policy enforcement by sending test traffic that matches the rule scope and engine profile.

To verify policy enforcement:

1. Send a test request from the mapped homegrown app through LiteLLM
2. Include content that matches the selected **Engine Profile**
3. From the navigation menu, select **AI Security > Guards**
4. Select the AI Gateway Guard
5. Open **Guard Logging**
6. Filter the logs by the mapped **Homegrown Agent**
7. Confirm that **Violated Rules** shows the policy rule

Example: `Block PII`

Traffic that does not match the selected **Engine Profile** shows no violated rules and passes through normally.
