---
title: "Managing the Endpoint Protection Solution"
slug: "managing-the-endpoint-protection-solution"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/managing-the-endpoint-protection-solution"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing the Endpoint Protection Solution

This article explains how to manage the EPP agents you have installed on your endpoints.

## Overview

After you have installed agents in your environment, you may need to take actions on endpoints for the day-to-day management of your EPP solution.

You can review the protected endpoints in your environment, and if necessary, take various actions to manage the EPP. Agents perform one action at a time, you can choose to terminate an action any time and after 7 days if an action is not taken it expires.

Some of the actions you can trigger in the CMA to take on an endpoint are:

- Full System Scan (for more information, see [Configuring Endpoint Protection](/v1/docs/configuring-endpoint-protection))
- Unlock Anti-Tamper
- Uninstall Agent
- Remove the agent from an endpoint
- Restore from quarantine (for more information, see [Monitoring and Responding to Endpoint Protection Threats](/v1/docs/monitoring-and-responding-to-endpoint-protection-threats))
- Upload Logs/Reinstall Drivers (for more information, see [Installing the Cato EPP Solution](/v1/docs/installing-the-cato-epp-solution))

If necessary, you can also manually upgrade the agent on an endpoint.

## Reviewing Protected Endpoints

After registering Endpoints with your Agent Token, the solution starts reporting data in real time, for example:

- The version used on each endpoint
- The profile applied to each endpoint

![2023-03-16_16-27-48.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318716280605.png)

> [!NOTE]
> Note:
> 
> Devices located in China are not able to register their EPP to Cato due to regional restrictions.

**To review protected endpoints:**

- From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** screen opens.

### Understanding the Protected Endpoint Table Columns

The following table is an explanation of the columns in the **Protected Endpoints** table.

| Column | Explanation |
| --- | --- |
| Endpoint ID | Unique ID of the EEP agent. |
| Endpoint Name | Computer name of the endpoint. |
| User | Last user to log into the endpoint. On shared devices, the user may change over time. |
| IP | IP address of the endpoint. |
| OS Version | Endpoint operating system. |
| EPP Version | Version of the EPP solution installed on the Endpoint. |
| Profile | EPP profile assigned to the Endpoint. The clock symbol displayed in this column means the Endpoint has not yet received the EPP profile. The EPP profile is assigned the next time the endpoint is online. |
| Quarantine Files | Number of quarantined files on the endpoint. |
| Status | Status of the EPP solution. The possible statuses are: - **Starting:** The EPP solution is installing on the endpoint - **Protected:** The EPP solution is online and protecting the endpoint - **Not Protected:** The EPP solution has a Profile with Anti-Malware set to **Monitor** - **Error:** The EPP solution has an error. Hover over to question mark symbol for more information about the error. See EPP Troubleshooting for more information on how to resolve the error. |

### Export the Protected Endpoints Table

You can export the contents of the Protected Endpoints Table to a CSV file to align with an MDM and make sure all of the relevant endpoints appear in the table.

**To export the list of protected endpoints:**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** screen opens.
2. Click **Export** in the upper right-hand corner of the page.

## Protecting Cato's EPP Solution

Cato's EPP has Anti-Tampering protection enabled by default. This protects the processes, files, services, and registries used by the EPP solution from malicious modifications or kill attempts. This also protects against unintentional enduser actions that might compromise security.

### Disabling Protection of EPP

You can temporarily unlock the Anti-Tamping protection for 15 minutes, for example, if you need to uninstall the solution. After this time, or if the endpoint is rebooted, Anti-Tampering protection is reenabled.

**To unlock protection:**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** screen is displayed.
2. Click the three dots (![Three_Dots.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318688016541.png)) on the endpoint that you are unlocking protection.
3. Click **Unlock Anti-Tamper**.

Anti-tampering protection is temporally disabled.

## Removing EPP from an Endpoint

If EPP is no longer required on an endpoint, it can be uninstalled and, if necessary, deleted from your account. After the solution is uninstalled, the EPP engines cannot scan for malicious activity and no Events are reported. The endpoint remains on the **Protected Endpoint** table until it is deleted.

- Uninstall fully removes the EPP client, however, if you reinstall the client, it will automatically be registered as the previous user prior to the uninstallation.
- Deletion deletes this endpoint's association with the account; it will stop protecting, not uploading events, etc. Deletion will also allow the client to reregister using a token

### Uninstalling and Deleting an Endpoint

You can uninstall EPP from an endpoint and delete the endpoint from your account in a single action.

> [!NOTE]
> Note:
> 
> Supported from EPP Agent v1.1. If you try to delete and uninstall EPP Agent v1.0, no action is taken until the Agent is upgraded to v1.1.

**To uninstall and Delete an Endpoint:**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** screen is displayed.
2. Click on the three dots (![Three_Dots.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318688016541.png)) on the endpoint that you are deleting.
3. Click **Remove Endpoint**.

The Remover Endpoint dialog box is displayed.
4. Click **Remove Endpoint & Uninstall Agent**.

EPP is uninstalled from the endpoint and the endpoint is deleted from your account.

### Uninstalling an Endpoint

You can uninstall EPP on an endpoint so that the EPP engines cannot scan for malicious activity and no Events are reported. Until the endpoint is deleted, it is visible on the **Protected Endpoint** table.

**To uninstall an endpoint:**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** screen is displayed.
2. Click on the three dots (![Three_Dots.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318688016541.png)) on the endpoint that you are uninstalling.
3. Click **Uninstall Agent**.

The **Uninstall Agent** dialog box is displayed.
4. Click **Uninstall Agent**.

EPP is uninstalled from the endpoint.

### Deleting an Endpoint

If EPP is no longer installed on an endpoint, the endpoint can be deleted from the **Protected Endpoint** table.

> [!NOTE]
> Note:
> 
> Do not delete an endpoint from the **Protected Endpoint** table before EPP has been uninstalled.

**To delete an endpoint:**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** screen is displayed.
2. Click on the three dots (![Three_Dots.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318688016541.png)) on the endpoint that you are deleting.
3. Click **Remove Endpoint**.

The Remove Endpoint dialog box is displayed.
4. Click **Remove Endpoint**.

The endpoint is deleted from the Protected Endpoints screen.

## Terminating an Action

After an action is created, you can terminate it at any time.

**To terminate an action:**

1. From the navigation menu, click **Access > Protected Endpoints**.
2. Click the **Actions History** tab.
3. Click on the three dots (![Three_Dots.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318688016541.png)) on the action you are terminating.
4. Click **Cancel Action**.

## Reviewing Endpoint Actions

You can view the near real-time status and history of actions sent to the EPP agent. The EPP agent sends an update on the status of an action it has received every 30 seconds.

> [!NOTE]
> Note:
> 
> Actions can be reviewed from agent version 1.2 and higher.

![Actions_EPP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318699166749.png)

**To review endpoint actions:**

1. From the navigation menu, click **Access > Protected Endpoints**.
2. Click the **Actions History** tab.

### Understanding the Actions History Table Columns

The following describes the **Actions History** table.

| Column | Explanation |
| --- | --- |
| Action ID | Unique reference of the action. |
| Endpoint ID | Unique ID of the EPP agent. |
| Created On | Time stamp of when the action was created. |
| Endpoint Name | Computer name of the endpoint. |
| Action | Action taken on the endpoint. |
| Status | The near real-time status of the action. Possible statuses are: - **Pending:** The action has been sent to the EPP agent but it has not been delivered. - **Delivered:** The action has been received by the EPP agent, but it has not been run. - **Running:** The action is running. - **Done:** The action has completed successfully. - **Expired:** The action was not taken after 7 days. - **Termination-Pending:** A termination request of the action has been sent to the EPP agent, but it has not been received. - **Termination-Delivered:** A termination request of the action has been received by the EPP agent. - **Terminated:** The action is stoped. - **Error:** An issue has occurred. |
| Details | Additional information about the action. |
| Last Update Time | Time stamp of the last time an update on the action was received. |
| Created By | The admin that created the action. |
| Endpoint Status | The status of the endpoint. |

## Upgrading an Agent Manually

When a new agent version is released, agents in your account are automatically gradually upgraded to the latest version. For various reasons, you may need to manually upgrade an agent.

**To upgrade an agent manually:**

1. Disable Anti-Tamper on the endpoint:
  - **For online agents**: This can be completed in the CMA. See for more information
  - **For offline agents:** In the file path `C:\Program Files\Cato Networks\CatoEndPointProtection` create an empty file called **disable_anti_tamper** (without an extension)

**Note:** This is only available for agents below v1.3
2. In the CMA, from the navigation menu, click **Access > Client Rollout** and download the EPP agent.
3. Distribute the agent with an MDM or install manually on an endpoint.

**Note:**
  - If you disabled Anti-Tamper from the CMA, you must distribute the agent within 15 minutes of disabling Anti-Tamper
  - If you disabled Anti-Tamper with a file, delete the file after the upgrade is complete
