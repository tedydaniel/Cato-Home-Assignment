---
title: "Creating the Response Policy for XOps Stories"
slug: "creating-the-response-policy-for-xops-stories"
updated: 2026-07-15T08:24:05Z
published: 2026-07-15T08:24:05Z
canonical: "knowledge.catonetworks.com/creating-the-response-policy-for-xops-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating the Response Policy for XOps Stories

This article explains how to use webhooks and other notifications with the XOps Response Policy that defines when you're notified for new and updated XOps stories, and when events are generated.

For more information about XOps stories, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

## Overview

The Response Policy helps you monitor XOps stories by defining when notifications for stories are sent to admins and analysts, and when events are generated for the stories. You can create rules that define the story criteria for sending notifications and generating events, and can use subscription groups, mailing lists, and third-party integrations to configure which admins receive the notifications.

For example, you can create rules that send notifications:

- If the story Criticality is high
- When new stories are created for a specific source (such as a site or IP range)
- When the story targets are updated
- For Security stories with a specific indication of attack
- For Site Operations for specific issues, such as a site or link is down

> [!NOTE]
> Note:
> 
> By default, notifications are not sent for Site Operations that match a [Mute Stories](/v1/docs/muting-xops-stories) rule.

### Generating Events for XOps Stories and Exporting to Third-Party Services

By default, XOps story events are not generated. Events are only generated according to configured rules. When you define rules that generate events for XOps stories, you can view them on the **Events** page, for more information, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

You can also integrate events for XOps stories with your existing third-party services and workflows.

- For a list of vendor-supported integrations for Cato events, see [Cato Data: Third-Party Supported Integrations](/v1/docs/cato-data-third-party-supported-integrations)
- For more about pushing events to a third-party storage account (such as AWS or Azure), see the articles in the [Event Integration](/v1/docs/event-integration) section

The **Events** page shows a set number of fields per event. To access the full Story data, export it as a JSON file available in the additional_data field. You can also create a filter to only export the data you require. For more about XOps event fields, see below [Cato Event and API Fields for XOps Story Events](/v1/docs/creating-the-response-policy-for-xops-stories#cato-event-and-api-fields-for-xops-story-events).

## Adding Rules to the XOps Response Policy

When you add a rule to the Response Policy, configure each section in the rule that is required to define the conditions for sending a notification or generating an event.

For example, if you want to generate an event for every XOps story that is created or updated, configure a rule with the **Source** as **Any**, and the **Trigger** as **Story Created or Updated**.

> [!NOTE]
> Note:
> 
> For MDR customers, please contact `&lt;mdr@catonetworks.com&gt;` to define Response Policy rules for your account. This can be overridden by selecting it as a condition.

![Response_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356111159325.png)

### Response Policy Rule Settings

A Response Policy rule has the following sections:

- **Name** - The name you assign for the rule
- **Description** for the rule
- **Source** - The source of traffic on your network involved in the story. For example: Site, IP address, or user

For more about **Source** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects).
- **Criteria** - Characteristics of the story to match the rule. When you add criteria, select the criteria type, value, and the operator that determines the relationship between the criteria and value. For example: **Criticality** | **Greater Than** | **6**.

Configurable story criteria include the following: Criticality, Severity, Indication, Analyst Verdict, Producer, Added Targets, and Status. For more about these story criteria, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)
  - The **Producer** is the engine that generates the story. For more about Site Operations , see [Reviewing Site Operations Stories](/v1/docs/reviewing-site-operations-stories) . For more about the XOps engines and their required license types, see [Using the Indications Catalog](/v1/docs/using-the-indications-catalog)
  - You can configure multiple values for the following criteria: Indication, Analyst Verdict, Severity, and Producer. When you add multiple values to a single criteria entry, there is an OR relationship between them.
- **Trigger** - Defines when the Response Policy engine checks a story for matching the rule. Settings include:
  - **Story Created** - The Response Policy engine checks for a match to the rule when a new story is created. Existing stories that are updated aren't checked for matching the rule.
  - **Story Created or Updated** - The Response Policy engine checks for a match to the rule when a new story is created or when an existing story is updated. Updates can include changes to the Status, Analyst Verdict, Severity, and Targets of the story.
- **Response** - Select the response for when the rule is matched. Responses can include generating an event and notifications defined by [Subscription Group](/v1/docs/creating-subscription-groups), [Mailing List](/v1/docs/working-with-mailing-lists), or [Webhook Integration](/v1/docs/sending-cma-notifications-via-webhooks).

### Creating New Response Policy Rules

Create a new Response Policy rule and configure the rule's settings to define when a story notification is sent.

![Response_Policy_New_rule_panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356136774429.png)

**To create a new Response Policy rule:**

1. From the navigation menu, click **Home > Detection & Response Policy**.
2. Select the **Response Policy** tab.
3. Click **New**. The **Add to Response Policy** panel opens.
4. Enter a **Name** for the rule.
5. In the **Source** section, select the type (for example: **Host**, **IP Range**, **Site**) and then select one or more objects for the story source for this rule (or you can enter an IP address).

The default **Source** value is **Any**.
6. **(Optional)** Define **Criteria** that specify the characteristics a story must have to match the rule.
7. Select the **Trigger** for the rule. You can configure whether the trigger should be when a story is created, updated or both.
8. Select the **Response**. If you select **Send Notification**, then define the Subscription Group, Mailing List, or Integration to receive the notification.
9. Click **Save**. The rule is added to the policy.

### Creating a Webhook Integration

To send data from XOps Stories to a third-party using a Webhook integration, you need to:

1. Configure the third-party integration in the CMA
2. Create the required rule in the Response Policy

#### Step 1: Configure the Third-Party Integration

You can define a Webhook integration to send alerts to third-party platforms such as ServiceNow, Jira, and Slack, and create alert-based automation flows. Cato's Webhooks support customizable HTTP headers and messages in the alert to meet the specific needs of your organization. For more information, see [Sending CMA Notifications via Webhooks](/v1/docs/sending-cma-notifications-via-webhooks).

#### Step 2: Create the Required Rule

After defining the third-party integration, create a rule in the Response Policy.

![Response.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356127854621.png)

**To create a rule for a third-party integration:**

1. Follow steps 1-7 in [Creating New Response+ Policy Rules](/v1/docs/creating-the-response-policy-for-xops-stories#creating-new-response-policy-rules).
2. In the **Response** section, select **Send Notification**.
3. In the **Send notification to** drop-down, select **Integration**.
4. In the **Integration** drop-down, select the integration you want to use in the rule.
5. Click **Save**. The rule is added to the policy.

## Cato Event and API Fields for XOps Story Events

The Events page shows all the XOps story events generated for your account. You can filter the page to show the events using the Event Type **Detection and Response**.

Below are the relevant fields for story events. The eventsFeed query of the Cato API shows data for XOps stories in these fields for eventFieldName type.

| API enum Value | Event Field | Comments |
| --- | --- | --- |
| user_display_name | User Display Name |  |
| analyst_verdict | Analyst Verdict |  |
| criticality | Criticality |  |
| device_name | Device Name |  |
| event_count | Event Count | For XOps Stories, events are not automatically aggregated, therefore the Event Count will usually have a value of 1. |
| sub-type | Sub-Type |  |
| event_type | Event Type | For XOps story events, the Event Type is **Detection and Response**. |
| indication | Indication |  |
| event_internal_id | Event Internal ID |  |
| producer | Producer | The engine that generated the story. Possible values: Threat Prevention, Threat Hunting, Usage Anomaly, Events Anomaly, Microsoft Endpoint Alert. |
| rule | Rule | Name of the Response Policy rule that generated the event. |
| source_ip | Source IP |  |
| source_is_site_or_sdp_user | Source is Site or User |  |
| source_site | Source Site |  |
| status | Status |  |
| story_id | Story ID |  |
| threat_name | Threat Name |  |
| threat_type | Threat Type |  |
| time | Time |  |
| vendor | Vendor | Possible values: Microsoft (for Microsoft Endpoint Alert stories), Cato. |
| additional_data | N/A | Story data that isn't included in the other event fields. This field is included in exported events, but isn't shown in the Events page. **Note:** This field is exported as raw unparsed data, and may contain escape characters. This format is subject to change. |
