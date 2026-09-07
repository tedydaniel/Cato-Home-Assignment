---
title: "Using Ask AI to Create Internet Firewall Rules"
slug: "using-ask-ai-to-create-internet-firewall-rules"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/using-ask-ai-to-create-internet-firewall-rules"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Ask AI to Create Internet Firewall Rules

## Overview

Ask AI is a generative AI agent that helps you analyze events and account data using natural-language prompts. When you have analyzed the events, Ask AI can suggest an Internet Firewall rule and add it to the policy. This helps you move faster from investigation to policy creation without manually building the rule from scratch.

Ask AI creates the rule as an unpublished revision, and the rule is only enforced after you publish the policy.

**Note:** Advanced AI Assistant capabilities, including account-specific answers and creating Internet Firewall rules, are currently available as a free trial.

## How It Works

When you use Ask AI to create an Internet Firewall rule, it suggests the rule settings in the chat based on your prompt. After you approve the suggestion in the chat, the Ask AI agent adds the new rule to the **Internet Firewall** policy as part of an unpublished revision. By default, the new rule is added at the end of the policy to reduce the chance that it interferes with the existing rulebase. Until you publish the revision, there is no impact on traffic.

If you need to update settings in the suggested rule, click **Reject** and tell Ask AI what needs to be changed. When the rule is correct, click **Approve**, and the rule is added as an unpublished revision.

Before you publish the policy, review the generated rule and verify that it matches your intended action, scope, and placement.

### CMA Admin Permissions

Using Ask AI to create Internet Firewall rules is subject to the [RBAC and role settings](/v1/docs/configuring-rbac-for-policy-management) for admins.

To create a new rule with Ask AI, you must have permissions to edit the Internet Firewall policy or sub-policy.

If an admin only has view permissions, Ask AI can still provide information about the existing rules. It can't add a new rule to the policy or sub-policy.

If an admin does not have permissions for the policy or sub-policy, Ask AI can still suggest a new rule, but it does not provide information about the existing rules and cannot add the rule to the policy or sub-policy.

## Creating an Internet Firewall Rule with Ask AI

Use Ask AI to create a suggested Internet Firewall rule from a natural-language prompt. After Ask AI creates the rule, review the unpublished revision and then publish the policy to enforce the rule.

![Ask_AI_INT_FW.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35761927150109.png)

**To create an Internet Firewall rule with Ask AI:**

1. From the navigation menu, click **Home > AI Workspace**. You can also use the Ask AI right-hand panel.
2. Enter a natural-language prompt that describes the rule you want to create.
3. Review the suggested rule details.
  1. If you need to update the rule, click **Reject** and tell Ask AI what it needs to change.
4. Click **Approve**.

The new rule is added as the lowest priority of the Internet Firewall policy.
5. Open the **Internet Firewall** page and review the unpublished revision.
6. Click **Publish**.
7. In the **Publish Revision** confirmation window, click **Publish**.

The Internet Firewall policy is updated with the new rule.

### Audit Trail

Changes made to an Internet Firewall rule with Ask AI are logged in the [Audit Trail](/v1/docs/using-the-audit-trail) in the same way as rules that you create manually.

## Creating Rules with the Cato Remote MCP Server

This functionality is also available through the Cato Remote MCP Server. You can use a connected MCP client to investigate policy behavior and generate an Internet Firewall rule suggestion.

Permissions for this functionality are controlled by the API key that the MCP client uses. To prevent users from creating or modifying rules, assign them a read-only API key that lets them investigate account data and policy information.

## Related Resources

- [What is Cato's Ask AI Agent](/v1/docs/what-is-cato-s-ask-ai-agent)
- [What is the Cato Internet Firewall?](/v1/docs/what-is-the-cato-internet-firewall)
- [Working with Policy Revisions](/v1/docs/working-with-policy-revisions)
- [Working with the Cato Remote MCP Server](/v1/docs/working-with-the-cato-remote-mcp-server)
