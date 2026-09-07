---
title: "Investigating Remote Users with Ask AI"
slug: "investigating-remote-users-with-ask-ai"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/investigating-remote-users-with-ask-ai"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Investigating Remote Users with Ask AI

## Overview

Ask AI is a generative AI agent that helps you analyze events and account data using natural-language prompts. As part of investigating user access issues, you can ask Ask AI to take these remediation actions:

- Resetting a user risk score
- Revoking a remote user session and forcing them to re-authenticate

This helps you easily move from investigation to remediation without manually navigating between multiple pages in the Cato Management Application (CMA).

**Note:** Advanced AI Assistant capabilities, including remote user remediation actions, are currently available as a free trial.

## How it Works

When you use Ask AI to help with a user access issue, it analyzes the relevant account data and suggests a remediation action in the chat. You review the suggested action details and click **Approve** to execute it.

If you need to change something about the remediation action, click **Reject** and tell Ask AI what needs to be changed. When the action is correct, click **Approve**.

The Ask AI agent immediately applies the actions after approval.

### Admin Permissions

Using the Ask AI agent to apply remote user remediation requires [RBAC and role edit permissions](/v1/docs/configuring-rbac-for-policy-management) for the user.

If an admin only has view permissions, Ask AI can help investigate the issue and provide information related to the user, but it can’t execute the action.

## Use Cases

### Resetting a User Risk Score with Ask AI

The CEO sends a message to the IT department because they can’t access Salesforce. You investigate the issue with Ask AI and see that the CEO has an elevated risk score. Ask AI suggests resetting the CEO’s risk score so they can reconnect, and after you review the suggested action, you click **Approve**.

### Revoking User Sessions with Ask AI

A NOC analyst notices that User A is uploading a large amount of data. They investigate the activity with Ask AI, which shows that the user’s risk level is normal, but also indicates that this user does not usually upload large files. Because the behavior is unusual, Ask AI suggests revoking the user’s active sessions as a precaution. After the admin reviews the suggested action and clicks **Approve**, the Ask AI agent revokes the user’s sessions.

## Remote User Remediation with Ask AI

Use Ask AI to investigate a user issue and execute a remediation action from the chat.

![ask_ai_revoke_user.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35813222756637.png)

**To remediate remote users with Ask AI:**

1. From the navigation menu, click **Home > AI Workspace**. You can also use the Ask AI right-hand panel.
2. Enter a natural-language prompt to reset the user's risk score or revoke the user session.
3. Review the suggested action details.
  1. If you need to update the rule, click **Reject** and tell Ask AI what to change.
4. Click **Approve**.

### Audit Trail

Actions performed by Ask AI are logged in the [Audit Trail](/v1/docs/using-the-audit-trail) in the same way as if the admin manually performed the actions.

## Remediating Users with the Cato Remote MCP Server

This functionality is also available through the Cato Remote MCP Server. You can use a connected MCP client to reset the risk score and revoke a user session.

Permissions for this functionality are controlled by the API key that the MCP client uses. To prevent users from remediating users, assign them a read-only API key that lets them investigate account data and policy information.

## Related Articles

- [What is Cato's Ask AI Agent](/v1/docs/what-is-cato-s-ask-ai-agent)
- [Revoking a Remote User Session](/v1/docs/revoking-a-remote-user-session)
- [Understanding the User Risk Level](/v1/docs/understanding-the-user-risk-level)
- [Working with the Cato Remote MCP Server](/v1/docs/working-with-the-cato-remote-mcp-server)
