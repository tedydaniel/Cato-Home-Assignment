---
title: "Creating Bi-directional Integrations With Service Management Platforms"
slug: "creating-bi-directional-integrations-with-service-management-platforms"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/creating-bi-directional-integrations-with-service-management-platforms"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Bi-directional Integrations With Service Management Platforms

## Overview

XOps supports bi-directional synchronization between XOps stories and an external service management platform. This integration helps keep investigation activity aligned across platforms, so updates made in one platform are reflected in the other.

Using the response policy and webhooks lets you create and update external tickets on ITSM platforms from XOps stories. Updates made in the ITSM can also appear in the related XOps story. This includes changes such as investigation status updates and comments.

The supported platforms are with predefined webhooks are:

- [ServiceNow](/v1/docs/servicenow-configuring-integration-with-xops-stories)
- Zendesk

### Understanding the Ticket Workflow

When an XOps story is created, a response policy rule creates a linked ticket in the external service management platform. The status of the ticket and comments made by users are automatically reflected in both systems. For example, when a user updates the investigation status or adds a comment in the ticket, the corresponding update appears in the XOps story in the Cato Management Application (CMA).

The workflow is:

1. An XOps story is created
2. A Response Policy rule triggered by status change or comment addition to the story, uses a webhooks integration with the service management platform to create a ticket (this can be tracked using the correlation ID)
3. Status updates to the story are automatically reflected in the service management platform and comments made in the service management platform are reflected in the CMA.

### Use Case

A company uses Cato XOps to monitor and investigate network and security stories, while its operations team uses an external case management system in a separate platform.

When a new XOps story is generated, a response policy automatically creates a linked ticket in the company’s service management platform. This allows the operations team to continue working in the system they already use for case management, without needing to manually copy story details from the CMA.

The operations team adds an important comment in the service management platform, which is visible in the CMA.

This bi-directional workflow helps the company:

- Reduce manual ticket updates between platforms
- Improve coordination between internal teams and service teams
- Maintain consistent investigation records across systems
- Ensure that comments and status changes are visible to all relevant stakeholders

## Configuring the Bi-directional Integration

To enable the bi-directional integration, you need to:

1. Create the integration in the third-party service management platform to enable story updates from the platform
2. Create the webhook integration
3. Create the response policy

### Step 1: Create the Integration in the Third-Party Platform

Configure the integration in third-party platform. For step-by-step instructions on configuring the integration, see the link below. The supported service management platforms with predefined webhooks are:

- ServiceNow
- Zendesk

### Step 2: Create the Webhook Integration

Create a predefined webhook integration with the service management platform for each of the following templates.

![Webhooks.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35697303501213.png)

- ServiceNow/Zendesk Create Ticket - To create a ticket in the service management platform
- ServiceNow/Zendesk Update Ticket - For status updates and comments

**Note:** To enable different responses for status updates and comments, create multiple

For more information about creating a webhook integration, see [Sending CMA Notifications via Webhooks](/v1/docs/sending-cma-notifications-via-webhooks).

### Step 3: Create the Response Policy

The Response Policy defines the criteria for synchronization between XOps stories and the external service management platform. To update your service management platform with updates from XOps stories, use these Criteria in a Response Policy rule:

- Investigation Status Change - To update the status of the story
- Added User Comment - To update a comment made by admin
- Added Managed Service Comment - To update a comment made by Cato Managed Services (Managed Service customers only)

After you have defined your required criteria, configure the Response in the rule to send a notification using the webhook you created in Step 2.

For more information about the XOps Response Policy, see [Creating the Response Policy for XOps Stories](/v1/docs/creating-the-response-policy-for-xops-stories).

#### Example Response Policies

There are some example Response Policies.

#### Creating Tickets in ServiceNow and Zendesk

In this example, any Story created by the Site Operations produces creates a ticket in both ServiceNow and Zendesk (A single webook was crated for both service management platforms).

![Policy1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35697276917277.png)

#### Updating Status in ServiceNow

In this example, if the status of a Site Operations Story changes, it is updated in ServiceNow.

![Policy_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35697303610653.png)

#### Adding a Comment from Zendesk

In this example, a Site Operations story is updated with a comment from Zendesk.

![Policy_3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35697265512221.png)
