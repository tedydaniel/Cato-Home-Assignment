---
title: "XOps Network Playbook - SCIM Provisioning Failed"
slug: "xops-network-playbook-scim-provisioning-failed"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-scim-provisioning-failed"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - SCIM Provisioning Failed

This playbook describes steps to resolve issues when scheduled SCIM provisioning fails.

## Overview

SCIM syncs are critical for provisioning users to CMA, ensuring seamless onboarding and consistent access to resources. The sync frequency depends on the Identity Provider (IdP) used, as described in [SCIM User Provisioning](/v1/docs/scim-user-provisioning).

When SCIM provisioning fails, newly created users may be unable to connect or access required services, and security policies may not be enforced correctly. To help ensure rapid detection and resolution, an XOps story is automatically generated whenever a provisioning failure occurs between the IdP and CMA.

When responding to Network XOps stories, it is essential to approach the problem in a systematic manner. First, verify that the issue is ongoing, then troubleshoot it, and finally confirm that the problem is resolved.

## Step 1 - Verifying the SCIM Sync Failed

The following are the different ways that a Cato Management Application admin can verify that a SCIM Sync has failed.

### Using the Story Drill-down

- An XOps story will be generated when the SCIM Sync fails.
- Go to the **Stories Workbench** page and use the Network Operations preset, including the filter 'Indication **Contains** SCIM**'.** Adjust the time frame as necessary. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32573433433117.png)
- Verify if a story is generated as shown below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32573496367517.png)
- Click on the story to drill down into the details. It provides information on the story status, an incident timeline, and, more importantly, the status of the SCIM sync. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32569602539037.png)
- As you scroll further down in the story drill-down, you'll find the Incident Timeline. This timeline highlights any changes in the status of the SCIM syncs. On the right pane, you’ll see the playbook workflow that outlines the steps for troubleshooting the issue.

### Using the Event

- SCIM sync failures can also be verified by examining the relevant event entries.
- To view this event, filter the Event Dashboard by setting **Sub-Type** to **SCIM Provisioning** and **Action** to **Failed**. Adjust the **timeframe** as needed to match when the issue occurred. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32573433438749.png)
- If a SCIM sync failure is detected, you will see events similar to the example shown below. The event message will show the reason for the sync failure. In the example shown below, this is due to an "**Internal Server Error**".

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574229730973.png)

## Step 2 - Troubleshooting SCIM Sync Failure

This section outlines the tools available in Cato for a structured troubleshooting approach to incidents of this type. While the steps are generally meant to be followed in order, the results of each check may influence the next step in the process.

### Perform On-Demand Provisioning

- To determine whether the issue was a one-time occurrence, perform a **provision on demand** from the IdP platform. For Azure, navigate to **Enterprise Applications > Cato Networks Provisioning > Provisioning** and click "**Provision on demand**." ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574229731741.png)
- Select a user or group assigned to the Application and click the **"Provision"** button.
- If the SCIM sync completes successfully, it may indicate that the SCIM Sync Failure was an **isolated** incident. The administrator should verify whether any **provider interruptions** or **Cato** [**maintenance activities**](https://status.catonetworks.com/) coincided with the SCIM sync time.
- If the SCIM sync also fails, it indicates that the issue persists and the sync with the IdP is not completing successfully. In this case, review any **recent configuration changes** that may have led to the problem.

### Reviewing Changes in Audit Trail

- Review the changes on the [Audit Trail page](/v1/docs/using-the-audit-trail) to determine if a configuration change is the cause of this issue. This step is especially important if the scheduled sync had been functioning normally but stopped working unexpectedly.
- To view any changes made to the domain configuration, filter the Audit Dashboard by setting **Model Type** to **Domain**. Adjust the **timeframe** as needed to match when the issue occurred. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574229732509.png)
- For example, the screenshot below shows that the admin made configuration changes to the Okta SCIM provisioning. If the timing of this activity aligns with the SCIM Sync Failure, the admin can revert the changes to determine if the changes are the cause.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574292485917.png)
- Another factor that could affect SCIM connectivity is changes to the Application on the IdP side. For Azure, navigate to **Enterprise Applications > Cato Networks Provisioning** and check the **Audit logs** and **Provisioning logs** to determine whether a configuration change triggered the SCIM failure. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574229734941.png)

### Update Admin Credentials

- To verify a credential failure with the IdP, generate a new token from CMA under **Directory Services > SCIM**. Click **"generate token"** and copy the new token.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574292487325.png)
- For Azure, navigate to **Enterprise Applications > Cato Networks Provisioning > Provisioning** and expand **Provisioning > Admin Credentials**. Enter the token generated from CMA and click "Test Connection". ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574292489245.png)
- If the authentication succeeds, the issue may be related to a token mismatch between the IdP and CMA.

## Step 3 - Verifying the SCIM Sync is Working

After identifying and resolving the issue that caused the SCIM sync to fail, verify that the sync is now showing as resolved in the Story.

### Using the Story Drill-down

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574292490269.png)

**NOTE:** Once the issue is resolved, the status of the story will change from "Open" to "Monitoring." It will remain in this state for the next hour, provided there are no further incidents. For more information, refer to [Understanding the Stories Columns](https://support.catonetworks.com/hc/en-us/articles/19442391484061-Reviewing-XDR-Stories-in-the-Partner-Stories-Workbench#h_01J0TWBQYTPPZVCC9CYR2733GK).

### Incident Timeline

The incident timeline displays changes in the status of the Scheduled Sync. You can use it to confirm whether the most recent status has been updated to "Closed".

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32574292491293.png)

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
