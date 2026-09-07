---
title: "Overview of Workflow for AI Security Guards for Custom AI Applications"
slug: "overview-of-workflow-for-ai-security-guards-for-custom-ai-applications"
tags: ["AI Sec - Apps", "AI Security"]
updated: 2026-08-10T09:20:48Z
published: 2026-08-10T09:20:48Z
canonical: "knowledge.catonetworks.com/overview-of-workflow-for-ai-security-guards-for-custom-ai-applications"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview of Workflow for AI Security Guards for Custom AI Applications

This article explains the end-to-end flow for creating an AI Security Guard, connecting a custom application to the guard, and configuring the Guards Interaction Policy.

## Overview

Cato AI Security Guards let you secure custom AI applications by routing application traffic through Cato before it reaches the large language model (LLM) provider. This gives admins visibility into AI interactions and lets them enforce policy rules for prompts, responses, tool inputs, and tool outputs.

## Step 1 - Create the AI Security Guard

Create a guard to define how Cato connects to the AI service or custom LLM endpoint. In proxy mode, the application sends traffic to the guard endpoint, and the guard forwards the traffic to the provider endpoint after inspection.

To create an AI Security Guard:

1. From the navigation menu, select **AI Security > Guards**.
2. Click **New**.
3. Enter a **Guard Name**.
4. Under **Select Guard Type**, select **Proxy**.
5. Under **Select AI Service**, select the relevant AI service or custom endpoint.
6. In **Endpoint URL**, enter the provider endpoint.
7. Configure the guard hosting settings.
8. Click **Save**.

The guard is created and available from the **Guards** page.

## Step 2 - Retrieve the Guard Connection Details

After you create the guard, retrieve the connection details that the application uses to send traffic through Cato. These values identify the guard endpoint, authenticate the application to the guard, and define any required provider authentication details.

To retrieve the guard connection details:

1. From the **Guards** page, open the guard.
2. Copy the guard endpoint.
3. Copy the Guard API Key.
4. Review the required request headers.
5. Review the provider authentication requirements.
6. Review the session ID header requirements, when relevant.

Use these values when you update the application configuration.

## Step 3 - Connect the Application to the Guard

Update the application so that it sends AI requests to the guard endpoint instead of directly to the LLM provider. The application authenticates to the guard, and the guard forwards traffic to the provider endpoint according to the guard configuration.

To connect the application to the guard:

1. Update the application destination URL from the LLM provider endpoint to the guard endpoint.
2. Add the required guard authentication header.
3. Add provider authentication details, when required.
4. Add session ID details, when required.
5. Send test traffic through the application.

The application traffic is now routed through the guard.

## Step 4 - Confirm the Guard Is Receiving Traffic

Before you configure policy rules, confirm that the guard receives traffic from the application. This helps verify that the application is correctly connected to the guard and that Cato can inspect the AI interactions.

To confirm that the guard receives traffic:

1. From the navigation menu, select **AI Security > Guards**.
2. Open the guard.
3. Open **Guard Logging**.
4. Review the generated sessions.
5. Confirm that prompts and responses are logged.

At this point, the guard provides visibility into application traffic. Policy enforcement starts only after you create and publish Guards Interaction Policy rules.

## Step 5 - Create and Publish the Guards Interaction Policy Rules

The Guards Interaction Policy defines how the guards handle AI interactions. Each rule specifies the guard it applies to, the detection engine profile, the action, and the traffic direction to inspect.

Rules can apply actions such as monitoring, blocking, anonymizing sensitive data, or combining anonymization with monitoring or blocking. Rules are evaluated regardless of their position in the rulebase. If multiple rules match the same interaction, the stricter action is applied.

To create and publish Guards Interaction Policy rules:

1. From the navigation menu, select **AI Security > Guards Interaction Policy**.
2. Click **New**.
3. Enter a rule **Name** and **Description**.
4. Use the **Enabled** toggle to enable the rule.
5. In **Guards**, select the guard that the rule applies to.
6. In **Engine Profile**, select the detection category for the rule.
7. In **Action**, select the action to apply when the rule matches.
8. In **Direction**, select the traffic direction to inspect.
9. Click **Save**.
10. Repeat these steps for additional rules.
11. Review the unpublished revision.
12. Click **Publish**.

After the policy is published, the guard enforces the active rules on traffic that passes through it.

## Step 6 - Verify the Policy

Verify the policy to confirm that the guard is enforcing the expected rules and that policy activity is visible in the guard logs.

To verify the policy:

1. From the navigation menu, select **AI Security > Guards**.
2. Open the guard.
3. On the **Overview** page, review the active rules.
4. Open **Guard Logging**.
5. Review sessions that match the policy rules.
6. Confirm the detected content, applied actions, and enforcement results.
