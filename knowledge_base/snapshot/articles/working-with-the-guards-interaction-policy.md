---
title: "Working with the Guards Interaction Policy"
slug: "working-with-the-guards-interaction-policy"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/working-with-the-guards-interaction-policy"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with the Guards Interaction Policy

Custom AI applications can process prompts that contain sensitive data, unsafe content, attack attempts, or requests that violate your organization's AI usage policies. Blocking access to these applications can reduce risk, but it can also limit the value of approved AI workflows.

The Guards Interaction Policy lets you control how specific guards handle AI interactions by inspecting content in real time and applying actions when risky or non-compliant content is detected. Instead of applying the same protection to every guarded workflow, you can create granular rules for selected guards and assign the engine profiles and actions that match the security requirements of each application.

Using Guards Interaction Policy rules, you can detect, block, anonymize, or monitor AI interactions based on your organization's security and governance requirements. This helps you protect sensitive information and enforce AI usage policies for AI applications you build without disrupting legitimate business use.

## Configuring Guards Interaction Policies

Before you create rules, enable the Guards Interaction Policy for end users in the Cato Management Application.

**To enable the policy:**

1. From the navigation menu, select **AI Security**.
2. Under **AI App Security**, select **Guards Interaction Policy**
3. Enable the **AI Apps Policy** toggle.

### Configuring a Guards Interaction Policy Rule

Rules in the Guards Interaction policy are evaluated regardless of their position in the rule base. If more than one rule is triggered, the stricter action is applied. For example, if there is a rule with a Monitor action, and another rule with a Block action, the Block action will be applied.

![Guard-Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36393939299101.png)

**To create a rule:**

1. From the AI Interaction Policy page, click **New**.
2. In the **General** section, configure the fields, for example **Name** and **Description**, as well as the position of the rule.
3. In the **Guards** section, select the specific guards that the rule applies to, or click **Select All** to apply the rule to all guards.
4. In the **Engine Profile** section, select the profile used to evaluate AI prompts.

Engine profiles are the data type against which the content is checked. For example, PII to see if there are Social Security numbers included in the prompt.
5. In the **Action** section, select the action to apply when a prompt matches the content profile, such as Block.
6. To determine the scope of the rule, select at least one **Direction** on which to apply the rule.
7. Click **Save**.
