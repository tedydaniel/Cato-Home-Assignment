---
title: "XOps Network Playbook - LDAP Active Directory Sync Failed"
slug: "xops-network-playbook-ldap-active-directory-sync-failed"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-ldap-active-directory-sync-failed"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - LDAP Active Directory Sync Failed

This playbook describes steps to resolve issues when the scheduled sync with the LDAP Active Directory fails.

## Overview

Active Directory is essential for provisioning users to the CMA, ensuring seamless onboarding and access to resources. If synchronization with AD fails, new users may be unable to connect or access necessary services, and security policies may not be properly enforced. Recognizing the importance of this process, an XOPs Story will be generated whenever a sync failure occurs between Active Directory and the CMA, enabling prompt resolution and minimizing potential disruptions.

When responding to Network XOps stories, it is essential to approach the problem in a systematic manner. First, verify that the issue is ongoing, then troubleshoot it, and finally confirm that the problem is resolved.

## Step 1 - Verifying the Scheduled Sync Failed

The following are the different ways that a Cato Management Application admin can verify that a Scheduled Sync has failed.

### Using the Story Drill-down

- An XOps story will be generated when the Scheduled Sync fails.
- Go to the **Stories Workbench** page and use the Network Operations preset, including the filter 'Indication **Contains** LDAP**'.** Adjust the time frame as necessary. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32079214766365.png)
- Verify if a story is generated as shown below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32079182626333.png)
- Click on the story to drill down into the details. It provides information on the story status, an incident timeline, and, more importantly, the status of the scheduled sync. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32079182629405.png)
- As you scroll further down in the story drill-down, you'll find the Incident Timeline. This timeline highlights any changes in the status of the scheduled syncs. On the right pane, you’ll see the playbook workflow that outlines the steps for troubleshooting the issue. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32079214770461.png)

### Using the Event

- Scheduled sync failures can also be verified by examining the relevant event entries.
- To view this event, filter the Event Dashboard by setting **Sub-Type** to **Directory Service** and **Directory Sync Type** to **Scheduled**. Adjust the **timeframe** as needed to match when the issue occurred. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31670392662045.png)
- If a scheduled sync failure is detected, you will see events similar to the example shown below. The event message will show the reason for the sync failure. In the example shown below, this is due to a "**connect error**".

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31670392662173.png)

#### Commonly Seen Event Message

| **Event Message** | **Description** |
| --- | --- |
| Failed to import LDAP data. Error Code: 81 (server down) | Domain controller is down. Check connectivity to the server. |
| Unable to connect to any domain controller. Error code: 91 (connect error) | Domain controller is up, but unable to connect successfully. Check configurations. |
| Invalid Credentials | Wrong credential configured for the Login DN |

## Step 2 - Troubleshooting Scheduled Sync Failure

This section outlines the tools available in Cato for a structured troubleshooting approach to incidents of this type. While the steps are generally meant to be followed in order, the results of each check may influence the next step in the process.

### Perform On-Demand Sync

- To determine whether the issue was a one-time occurrence, perform a **manual sync** with the AD/DC. Navigate to **Access > Directory Services > LDAP**, and click **Sync Now**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31670656324637.png)
- If the manual sync completes successfully, it may indicate that the Scheduled Sync Failure was an **isolated** incident. The administrator should verify whether any **network interruptions** or **server maintenance activities** coincided with the scheduled sync time.
- If the manual sync also fails, it indicates that the issue persists and the sync with the AD/DC is not completing successfully. In this case, review any **recent configuration changes** that may have led to the problem.

### Reviewing Changes in Audit Trail

- Review the changes on the [Audit Trail page](/v1/docs/using-the-audit-trail) to determine if a configuration change is the cause of this issue. This step is especially important if the scheduled sync had been functioning normally but stopped working unexpectedly.
- To view any changes made to the domain configuration, filter the Audit Dashboard by setting **Model Type** to **Domain**. Adjust the **timeframe** as needed to match when the issue occurred. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31670453845661.png)
- For example, the screenshot below shows that the admin made configuration changes to the domain. If the timing of this activity aligns with the Scheduled Sync Failure, the admin can revert the changes to determine if the changes are the cause.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31670432755869.png)
- Another factor that could affect connectivity to the domain is the Static Host Reservation configured at the site where the domain is located.
- To check whether any changes were made to the Static Host Reservation, open the Audit Dashboard and filter the results by setting **Model Type** to **Site** and **Model Name** to the site where the domain resides. In the example below, the domain is located at the HQ Office.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31670656329885.png)

### Perform Connectivity Test to Domain Controller

- To verify connectivity to the domain controller, perform a **ping test** from the **LAN interface** of the Socket where the domain controller is located.
- From the **CMA**, open the [**Socket web UI**](/v1/docs/accessing-the-socket-webui), then navigate to **Tools,** selecting the **Ping** tab. Under **Route via**, choose **LAN**, enter the **IP address of the domain controller**, and click **Run** to execute the test. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31686282455069.png)
- If the ping test succeeds, the issue may be related to a configuration mismatch between the DC and CMA, rather than a connectivity issue.
- If the ping test fails, verify that the domain controller (DC) is powered on and reachable. If the DC is running, check whether any intermediate devices (such as firewalls or routers) are blocking the connection.

## Step 3 - Verifying the Scheduled Sync is Working

After identifying and resolving the issue that caused the scheduled sync to fail, verify that the sync is now showing as resolved in the Story.

### Using the Story Drill-down

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32117073001501.png)

**NOTE:** Once the issue is resolved, the status of the story will change from "Open" to "Monitoring." It will remain in this state for the next hour, provided there are no further incidents. For more information, refer to [Understanding the Stories Columns](https://support.catonetworks.com/hc/en-us/articles/19442391484061-Reviewing-XDR-Stories-in-the-Partner-Stories-Workbench#h_01J0TWBQYTPPZVCC9CYR2733GK).

### Incident Timeline

The incident timeline displays changes in the status of the Scheduled Sync. You can use it to confirm whether the most recent status has been updated to "Closed"

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32117073005213.png)

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
