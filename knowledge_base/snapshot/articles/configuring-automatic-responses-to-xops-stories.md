---
title: "Configuring Automatic Responses to XOps Stories"
slug: "configuring-automatic-responses-to-xops-stories"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/configuring-automatic-responses-to-xops-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Automatic Responses to XOps Stories

This article explains how to create an automatic response to an XOps story to contain potential threats.

## Overview

Automatic responses to XOps stories let you define mitigation actions that are triggered when a story meets specific criteria. This helps contain threats as soon as they are detected, reduces response time, and ensures consistent enforcement of your security posture and network traffic policies across your environment.

You can define automatic responses in rules configured in the [Response Policy](/v1/docs/creating-the-response-policy-for-xops-stories) . Instead of relying on a manual response, each rule evaluates the story attributes such as severity, user involvement, or indication, and automatically triggers the configured action.

To prevent over-enforcement, an automatic action is applied to a specific user once every 30 minutes. During this 30-minute window, additional matching stories do not trigger repeated actions on the same user. This avoids unnecessary disruptions while still ensuring an effective response to real threats.

### Supported Actions

The supported actions are listed below:

- **Revoking the User Session**: This logs the user out and prompts them to reauthenticate via the Client login screen, ensuring only legitimate users regain access. For more information, see [Mitigating Threats in XOps Stories](/v1/docs/mitigating-threats-in-xops-stories).

### Use Case - Automatically Responding to Stories with High Criticality and Severity

Company ABC faces a large volume of XOps stories, making it challenging to ensure that the most critical threats are addressed immediately. To reduce exposure and enforce consistent mitigation, they configure a response policy rule that automatically handles stories with the highest risk indicators.

They create a rule to identify any story with high Criticality, and set the automated action to revoke the user's session. To ensure the automatic action is used safely, the admin adds a filter by Indication and selects only phishing-related story types for this policy. This helps balance security efficacy with proper enforcement and ensures only users who truly require it are blocked.

Any user who is included in a story that matches these criteria is automatically forced to re-authenticate. This approach ensures that critical threats receive immediate attention, improves the consistency of your security posture, and frees analysts to focus on investigation rather than urgent mitigation tasks.

## Creating Automatic Responses

Automatic responses are configured within the Response Policy.

![Response_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32611930765469.png)

**To create an automatic response:**

1. Create a Response Policy rule. For more information, see [Creating the Response Policy for XOps Stories](/v1/docs/creating-the-response-policy-for-xops-stories).
2. In the **Response** section, under **Action** choose the automatic action to apply to the rule. You can also select a notification.
3. Click **Save**. The rule is added to the policy.

### Reviewing Mitigation Actions

If a story matches a rule with an automated response, the action is automatically taken and the story timeline is updated. The action is also visible in the Action Center.

The Action Center tab in the **Home > Detection & Response Policy** page lets you review the XOps mitigation actions taken in your account.

![ACtion_center.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32611926325021.png)

The Action Center shows the following information for each mitigation action:

- **Time** - Timestamp for when the mitigation action was sent
- **Action** - Description of the mitigation action
- **Subject** - The user the action was performed on
- **Status** - Status of the action. For the **Add Target to Blocklist** action, these are the **Status** values:
  - **Success** - The request to revoke the session was sent to the Cato user service
  - **Failure** - There was an issue with the request to revoke the session
- **Author** - Admin who performed the action
- **Trigger** - The **Story ID** for the story from which the action was sent. Click to open the Overview page for the story
- **Note** - For automatic actions, no note is added
