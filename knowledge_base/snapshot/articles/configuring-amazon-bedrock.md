---
title: "Configuring Amazon Bedrock"
slug: "configuring-amazon-bedrock"
updated: 2026-09-02T06:31:07Z
published: 2026-09-02T06:31:07Z
canonical: "knowledge.catonetworks.com/configuring-amazon-bedrock"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Amazon Bedrock

## Overview

Cato connects to Amazon Bedrock through a CloudFormation stack deployed in your AWS account. The integration provides visibility into Amazon Bedrock Agents (Classic) configurations and Amazon Bedrock AgentCore agent inventory.

To view AgentCore activity, enable CloudWatch Transaction Search and configure tracing for agents that AWS does not instrument automatically.

### Prerequisites

Before you start, confirm the following:

- You have access to the AWS account where you want to install Cato's CloudFormation stack, or to the AWS Organizations management account for a multi-account deployment
- You have the AWS permissions required to create a CloudFormation stack and the IAM role it provisions

## Install Cato's CloudFormation Stack

Cato uses a CloudFormation stack to get read-only access to Amazon Bedrock in your AWS account. Choose the single-account stack to connect one AWS account, or the multi-account stack to connect Bedrock across an AWS Organization.

To install the CloudFormation stack:

1. In the CMA, go to **AI Security** > **Integrations**, locate the **Amazon Bedrock** integration, and click **Connect**.
2. Select **Single Account CloudFormation** or **Multi Account CloudFormation**.
3. In a separate browser tab, make sure you're signed in to your AWS account.
4. Click **Install With CloudFormation** to open the AWS Console in that tab.
5. Follow the CloudFormation wizard to complete the stack installation.

Cato detects the installed stack automatically. The integration shows as connected in the CMA once the stack installation completes, with no additional steps required.

## Review the Requested Permissions

The CloudFormation stack provisions the IAM role and permissions Cato needs to read Bedrock agent configurations. Click **See stack content** on the integration page in the CMA to review the exact permissions before you install the stack.

## Enable AgentCore Activity Monitoring

Cato uses CloudWatch agent traces to show AgentCore activity. Enable CloudWatch Transaction Search once for the AWS account after you install the CloudFormation stack.

To enable CloudWatch Transaction Search:

1. In the AWS Console, open **Application Signals (APM)**.
2. Select **Transaction search**.
3. Select the option to ingest spans as structured logs.
4. Save the changes.

Without this setting, AWS does not deliver AgentCore traces to CloudWatch. Cato can still show AgentCore agents in the inventory, but it cannot show their activity.

## Configure Tracing for AgentCore Agents

The required configuration depends on how you build the AgentCore agent.

### Agents Built with AgentCore Harness

No additional configuration is required. Agent activity appears in Cato within one hour of the first invocation.

### Custom AgentCore Agents

For custom agents, configure the agent to emit OpenTelemetry traces that follow the Generative AI semantic conventions. AWS documents the supported framework configurations in [Add observability to your Amazon Bedrock AgentCore resources](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html).

For agents built with Strands, install the `strands-agents[otel]` package. AgentCore Runtime provides the export configuration, and Strands emits the traces.

To enable tracing for a custom AgentCore agent:

1. In the AgentCore console, open **Agent Runtime**.
2. In the **Runtime agents** pane, select the agent.
3. In the **Tracing** pane, click **Edit**.
4. Enable tracing.
5. Click **Save**.

Cato shows all AgentCore agents in the inventory. Activity is available after AWS generates and delivers traces to CloudWatch.
