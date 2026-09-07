---
title: "Configuring Amazon Quick"
slug: "configuring-amazon-quick"
updated: 2026-07-27T15:05:30Z
published: 2026-07-27T17:46:45Z
canonical: "knowledge.catonetworks.com/configuring-amazon-quick"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Amazon Quick

## Overview

Cato connects to Amazon Quick through a CloudFormation stack deployed in your AWS account, which gives admins visibility into agent configurations built in Amazon Quick.

### Prerequisites

Before you start, confirm the following:

- You have access to the AWS account where you want to install Cato's CloudFormation stack, or to the AWS Organizations management account for a multi-account deployment
- You have the AWS permissions required to create a CloudFormation stack and the IAM role it provisions

## Install Cato's CloudFormation Stack

Cato uses a CloudFormation stack to get read-only access to Amazon Quick in your AWS account. Choose the single-account stack to connect one AWS account, or the multi-account stack to connect Amazon Quick across an AWS Organization.

To install the CloudFormation stack:

1. In the CMA, go to **AI Security** > **Integrations**, locate the **Amazon Quick** integration, and click **Connect**.
2. Select **Single Account CloudFormation** or **Multi Account CloudFormation**.
3. In a separate browser tab, make sure you're signed in to your AWS account.
4. Click **Install With CloudFormation** to open the AWS Console in that tab.
5. Follow the CloudFormation wizard to complete the stack installation.

Cato detects the installed stack automatically. The integration shows as connected in the CMA once the stack installation completes, with no additional steps required.

## Review the Requested Permissions

The CloudFormation stack provisions the IAM role and permissions Cato needs to read Amazon Quick agent configurations. These permissions differ from the Amazon Bedrock integration. Click **See stack content** on the integration page in the CMA to review the exact permissions before you install the stack.
