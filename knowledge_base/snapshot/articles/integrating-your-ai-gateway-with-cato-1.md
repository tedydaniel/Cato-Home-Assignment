---
title: "Integrating your AI Gateway with Cato"
slug: "integrating-your-ai-gateway-with-cato-1"
updated: 2026-07-23T08:11:54Z
published: 2026-07-23T08:12:11Z
canonical: "knowledge.catonetworks.com/integrating-your-ai-gateway-with-cato-1"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating your AI Gateway with Cato

This article provides information about integrating an AI Gateway with Cato AI Security to provide you with monitoring and enforcement capabilities for your homegrown agents.

## Overview

Cato AI Security lets you inspect and enforce policy for AI traffic that flows through your existing LiteLLM AI Gateway. Instead of configuring each application separately, you connect the gateway to a Cato Guard and apply centralized monitoring, data protection, and policy enforcement to gateway traffic.

This article explains how to configure a LiteLLM AI Gateway integration, map homegrown agents, and validate policy enforcement in Guard Logging.

## Prerequisites

Before you start, make sure these requirements are met:

- AI Security for Applications license
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

![AI-Gateway_New.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/AI-Gateway_New(1).png){height="" width=""}

To create the Guard:

1. From the navigation menu, select **AI Security > Guards**
2. Click **New**
3. In **Guard Name**, enter a name for the Guard Example: `LiteLLM Test`
4. In **Type**, select **AI Gateway**
5. In **AI Gateway Integration Type**, select **LiteLLM**
6. In **Guard's Host**, select **Cato's Cloud**
7. You [can map the homegrown agents](#map-a-homegrown-app-to-the-guard) using **Homegrown Agent Mapping**. This creates the connection between the specific virtual key in LiteLLM and a homegrown agent in the CMA. You can also leave the guard without any mapping at this stage and include the mapping after you've [verified that AI Gateway traffic](#verify-gateway-traffic-in-cato) is sent to the Guard.
8. Click **Save**

After you save the Guard, it is ready to receive traffic from the LiteLLM AI Gateway. The Guard is active, but it does not enforce rules until you configure a policy rule.

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

We recommend that you store the API key securely and avoid committing it to source control. If your deployment supports environment variables or a secret manager, use that method instead of storing the key directly in `config.yaml`.

### Update the LiteLLM Configuration

Configure the Cato guardrail in your LiteLLM tenant using the [LiteLLM documentation](https://docs.litellm.ai/docs/proxy/guardrails/quick_start). Guardrail is the LiteLLM terminology for implementing guards.

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

## Verify Gateway Traffic in Cato

Use the Interaction Explorer to confirm that LiteLLM traffic reaches Cato.

![AI-Gateway_Interaction-Explorer.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/AI-Gateway_Interaction-Explorer(1).png){height="" width=""}

To verify gateway traffic in Cato:

1. Generate a session by sending a test prompt from an app behind the LiteLLM gateway.
2. From the navigation menu, select **AI Security > Interaction Explorer**
3. From the **Guard** dropdown, filter the selection by your Guard.
4. Confirm that the session you generated in Step 1 appears in the table.

At this point, the **Homegrown Agent** column shows a dash (`-`) for each entry. This is expected because in our example, no homegrown agents have been mapped to the Guard yet.

In this stage, Cato logs gateway traffic. After agent mapping, Cato also attributes traffic to the specific homegrown agent.

If you don't see any traffic after approximately one minute, [troubleshoot the connection in LiteLLM](#verify-gateway-traffic-in-litellm).

## Map a Homegrown Agent to the Guard

Map a homegrown agent so Cato Networks can attribute AI Gateway traffic to the correct agent.

In LiteLLM, create a Virtual Key for each agent that you want Cato to identify separately.

1. In LiteLLM, navigate to **Virtual Keys**
2. Copy the **Key Alias** (might also be called Key Name) for each homegrown agent you want to add to your Guard

In the CMA, map the agent using the LiteLLM **Key Alias**. To map a homegrown agent to the Guard:

1. From the navigation menu, select **AI Security > Guards**
2. Select the AI Gateway Guard
3. In **Homegrown Agent Mapping**, click **Add Mapping**
4. In **Homegrown Agent**, select the homegrown agent from the list, or create a new agent
5. In **Virtual Key Alias**, enter the LiteLLM Key Alias for the agent
6. Click **Save**

## Verify Agent Attribution

Verify that Cato attributes gateway traffic to the mapped homegrown agent.

To verify agent attribution:

1. Generate traffic using a test request from the mapped homegrown agent through LiteLLM
2. From the navigation menu, select **AI Security > Interaction Explorer**
3. Filter the view by the mapped **Homegrown Agent**
4. Confirm that the **Homegrown Agent** column shows the mapped agent

When the agent is mapped correctly, Interaction Explorer shows the app name instead of a dash (`-`).

## Troubleshooting Gateway Traffic in LiteLLM

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
