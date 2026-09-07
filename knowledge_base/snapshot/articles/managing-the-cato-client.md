---
title: "Managing the Cato Client"
slug: "managing-the-cato-client"
updated: 2026-09-06T06:58:52Z
published: 2026-09-06T06:58:52Z
canonical: "knowledge.catonetworks.com/managing-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing the Cato Client

This article provides information about how to manage the Cato Clients installed in your organization, perform certain support actions, and see a history of those actions.

## Overview

The Client Management page gives you centralized visibility into all Cato Clients installed in your organization. You can monitor service status and perform remote actions for troubleshooting. This helps you proactively support users and maintain endpoint health at scale.

Each row in the Client Management page represents a user with the Cato Client and provides details about connection status, device details, the client version, and service status.

**Notes:**

- Supported for Cato Client for Windows v5.21and higher
- This feature is being gradually rolled out and may not be available for your account

### Communication with Cato

The Client sends status updates directly to the Cato Management Application, even when it isn’t connected to a Cato PoP. This gives admins visibility into Client status during disconnections and error conditions.

Actions from the Client Management page are also sent directly to the Client, without routing through a Cato PoP. This helps ensure that actions can still reach the Client during disconnections and error conditions.

### Use Case

![Client-Management-Actions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35992845441821.png)

An employee at ABC Company has been having issues with the Cato Client, and the IT admin opened a ticket with Cato Support. To help resolve the issue, the IT admin navigates to the Client Management page and, using the **Actions > Upload Logs** feature, provides Cato Support with the necessary information to resolve the issue. In addition, the IT Admin uses the **Actions > Bypass Always On** feature to ensure that the user's connectivity is not affected in the meantime.

## Understanding the Client Management Page

The Client tab presents a list of all of the Clients currently listed in your account, and provides the following information:

| Column | Description |
| --- | --- |
| Client ID (hidden by default) | A unique identifier provided by the operating system. |
| Device Name | The name of the device as it appears in the operating system |
| Last User | The most recent user connected from this device. |
| Operating System | The operating system installed on the device |
| Cato IP | The IP address provided by the Cato Client interface |
| Client version | The Cato Client version installed on the device |
| Services | A visual indication of the status for each of the services, Private Access and Internet Security. Possible values are: - Connected - The service is connected to the Cato PoP and is running correctly - Connected, Warning - the service is connected to the Cato PoP, but there might be an issue, such as an expiring token. - Error - the service is unable to connect - Disconnected - the service is currently not connected |
| Last Available | When was communication with the Client most recently successful |
| Client Availability | Indicates if the Client is available to receive actions and update its connection status |

## Performing Actions on the Client

There are scenarios where you will need to provide support or intervene in the Client's status to resolve an issue. You can [filter the data](/v1/docs/filtering-data-on-a-page) on the page to make it easier to find the Client you need. You can also bypass Always On for all Clients in your account.

**To perform an action on the Client**

1. Navigate to **Access > Client Management**.
2. Select the Client(s) on which you want to perform the action, and click **Actions**.
  - Upload Logs from the device to Cato Support to help troubleshoot any issues the user might be experiencing. When asked by Cato Support, provide the reference ID shown in the Actions History tab.
  - Bypass Always-On when the user needs to disable Always On and cannot bypass it themselves. When the timer expires, Always On will be re-enforced automatically. This action does not change any of the settings as defined in the [Always On policy](/v1/docs/protecting-users-with-always-on-security).
  - Bypass Anti Tamper when the user needs to disable Anti Tamper and cannot bypass it themselves
  - Delete the entry from the table, perhaps for users who are no longer with the organization or this connection data is no longer needed.

> [!NOTE]
> Note:
> 
> This does not remove the Cato Client from the user's device nor from the account.

## Reviewing Action History

There is an audit log of all the actions taken on all of the Clients in your account in the Actions History tab. There you can see the action taken, by whom, the status of the action, and, if necessary, a reference ID for the uploaded log files.

![client-management-actions_history.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35992788405021.png)
