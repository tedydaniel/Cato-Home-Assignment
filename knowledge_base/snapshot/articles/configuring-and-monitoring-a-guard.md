---
title: "Configuring and Monitoring a Guard"
slug: "configuring-and-monitoring-a-guard"
updated: 2026-09-01T13:49:27Z
published: 2026-09-01T13:49:27Z
canonical: "knowledge.catonetworks.com/configuring-and-monitoring-a-guard"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring and Monitoring a Guard

A guard is the enforcement point for AI Security in your custom AI applications. You use guards to inspect AI interactions, apply policy actions, and gain visibility into how protected applications are used. For more information about guard concepts and use cases, see [Working with AI Security Guards](/v1/docs/working-with-ai-security-guards).

This article explains how to create a guard, use the generated authentication key to connect it to your AI application, and monitor guard activity after deployment.

## Defining a Guard

You create and manage guards from the AI Security > Guards page. This page lists all guards in your account and includes summary information such as the guard type, hosting location, AI interactions, violation count, and creation date.

**To create a guard**

1. From the navigation menu, select **AI Security > Guards**, and click **New**.
2. Enter the Guard Name. Cato recommends you provide a descriptive name to help you remember which application the guard applies to.
3. Select the **Guard Type**:
  - Proxy: The guard intercepts prompts inline, and Cato performs the configured action
  - API: The guard scans prompts without intercepting them, and Cato returns the detection result so your application can apply the action
  - AI Gateway: The guard integrates with an existing AI gateway to scan prompts and intercept them automatically
4. If you selected a proxy guard type, select the **AI Service** with which the guard will interface, and enter the API key for the service.
  1. Click **Validate** to ensure you entered the correct key

If you selected an API guard type, determine whether to host the guard on an Outpost.
  2. (Optional) Determine how Cato handles requests that can't be inspected. Enable the **Allow Passthrough** toggle to forward requests to the AI service endpoint without prompt inspection. Disable **Allow Passthrough** to reject these requests.
5. Click **Save**.

## Implementing the Guard in Your AI Application

After you create a guard, open it from the Guards page to view the implementation details for your application. The guard details page provides the information you need to connect your application traffic to the guard.

Depending on the guard type and service, the page can include:

- Endpoint details
- Required headers
- Request body format
- Guard API keys

The page also includes sample request code that you can copy and use as a starting point for your application integration.

Use the generated snippet to update your application so traffic is sent through the guard or evaluated by the guard, based on the selected integration type.

## Monitoring Guard Activity

After you deploy a guard, you can review its activity to understand how it is used, which rules apply to it, and whether it detects policy violations. If you click on a specific session, you can also see the actual interaction data that was sent to and from the model.

**Note:** Viewing session data is only possible if you have the necessary Read Sensitive Content permissions. For more information about the roles and permissions, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

![guard-monitoring-overview.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35138738161693.png)

The guard overview page shows summary information for the selected guard, including Interactions, Violation Rate, Active Rules, and more.

You can use this data to understand how often the guard is used, which policies are actively enforced for it, and how frequently interactions trigger detections or violations.

### Guard Logging

The Guard Logging page provides session-level visibility into traffic handled by the guard. For each session, you can review summary fields such as:

- Session ID
- Invocations
- Detections
- First Activity
- Last Activity

Expand a session to view more detailed information, such as what action was taken, a timestamp for the session, and more.

![guard-monitoring-logging.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35138752809757.png)

This data helps you investigate guard activity in more detail and verify that the guard is enforcing policy as expected.
