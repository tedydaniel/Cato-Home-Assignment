---
title: "Sending CMA Notifications via Webhooks"
slug: "sending-cma-notifications-via-webhooks"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/sending-cma-notifications-via-webhooks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending CMA Notifications via Webhooks

## Overview

The Cato Management Application (CMA) generates notifications for a wide range of security and network events in your account. You can use webhook integrations to automatically deliver these notifications to third-party platforms such as ServiceNow, Jira, Slack, or Zendesk. This allows external systems to consume Cato event data in real time and trigger automated workflows for incident tracking and response.

Cato supports two types of webhook integrations:

- Standard webhooks use HTTP requests to create or update items in external platforms.
- Correlated webhooks integrate with the XOps service. They use correlation IDs to create and update items that represent the lifecycle of XOps security and network stories in third-party tools. An XOps license is required.

Webhook integrations are fully configurable. You define the HTTP method (POST or PUT), the target URL, the authentication method, and the request body. Templates and field variables let you tailor the payload structure to the requirements of the third-party platform.

### Understanding Cato Webhook Integrations

#### Webhook Integration Types

Cato supports these types of webhooks to integrate your account with third-party platforms and create automation flows:

- Standard webhooks support a wide range of CMA notifications, such as notifications based on account or system alerts, and policy-driven notifications. They let you deliver this data to external platforms and configure whether the webhook creates new records or updates existing ones.
- Correlated webhooks are designed for the XOps service. They extend webhook functionality to security and network stories, so each story in CMA is mapped to a record in the external system and updated as the story progresses. An XOps license is required.

#### Webhook Flows - Create or Update

Webhook flows define how the CMA communicates with a third-party platform, either by creating new records or updating existing ones:

- **POST** (Create) - Creates a new item in the third-party platform each time the webhook is triggered. Example: open a new ServiceNow ticket every time the Internet Firewall rule blocks a traffic flow.
- **PUT** (Update) – Updates an existing item in the third-party platform. The request includes a valid item ID in the URL or body.

#### Authentication Methods

When creating a Webhook integration, there are different authentication methods to choose from:

- **Basic** - Username and password
- **Bearer** - Bearer Token
- **Custom** - Custom headers for services that require unique authentication. Add key-value pairs as needed.

**Note:** If access to the third-party service is limited to specific IP addresses, please refer to this [article](https://support.catonetworks.com/hc/en-us/articles/20511945810589) for the list of Cato IP addresses that you need to allow (you must be signed in to view this article).

### Customizing the Notification Content

The `content` field in the template contains the generated readable summary of the alert, similar to the email alert content. You can choose these formats for the content: `contentText`, `contentMarkdown`, or `contentHTML`.

If you choose to customize the body, there are a number of data fields that you can use in the message content. So you can define a custom body (or structure), and then embed the Cato data fields. When you enter `$`, the available data fields are displayed, and then you select the required field. The fields use auto-complete to filter the list. For more information about the Cato fields, see [Understanding the JSON Fields for Alert Integrations](/v1/docs/understanding-the-json-fields-for-alert-integrations).

### Default Value for Webhook Fields

You can define custom default values for dynamic webhook fields to add flexibility when notification data doesn’t include a value. This lets you override the default **NA** value in the webhook URL, headers, or body. Use the `${field:defaultValue}` format to define the fallback value. For example, you can set **${level:medium}** if the **level** field isn’t populated. In a correlated flow, you can also use a fallback ticket ID in the webhook URL, such as **https://EXAMPLE-INSTANCE.service-now.com/api/now/table/incident/${correlationId:12345}**, so uncorrelated notifications are captured in a default ServiceNow ticket.

## Standard Webhook Integrations

Standard webhooks let you send CMA notifications to third-party platforms for a wide range of use cases. First, define the webhook to integrate with the platform. Then select which CMA notifications and policy rules, such as firewall actions, will generate notifications using the webhook.

### Define a Webhook Integration

Create a webhook integration that sends notifications via items (ticket, Slack message, etc.) in your third-party tool. You can configure a webhook to create new items with a POST request or update existing items with a PUT request. The integration includes settings for the URL, request body, authentication method, and optional custom headers and message body.

After defining the details, you can test the connection and validate that it works.

**To define a Webhook integration:**

1. From the navigation menu, click **Account > Subscriptions** and select the **Webhooks** tab.
2. Click **New Webhook**. The **New Webhook Integration** panel opens.
3. Configure the **Webhook details**:
  1. Enter the integration **Name**.
  2. Click the slider to enable (green) or disable (gray) the integration (it's enabled by default).
4. Configure the settings for the JSON template for the integration:

**Note:** If you choose a different template, the fields in the **Custom Body** are reset. For more information about the templates, see below [Templates and Fields](/v1/docs/sending-cma-notifications-via-webhooks#templates-and-fields).
  - In **Start from template**, select the default JSON template that populates the integration settings.

You can adjust and modify the fields for the **Custom Body** (see below step 7).
5. Configure the **Connection Details**:
  1. Enter the **URL** for the service that is receiving the Webhook.

You can use fields as variables in the URL. Type **$** to see the available fields.
  2. In the **Request Method**, select the flow for this webhook: **POST** or **PUT**.
  3. If necessary, configure the **Authentication Method** and settings for the service.
6. **(Optional)** In **Custom Headers**, define the **Key** and **Value** for each additional HTTP header for the integration.
7. In **Custom Body**, define the content of the Webhook notification:
  1. **(Optional)** Customize the content in **Edit Body**.

The **Response Correlation ID** isn't used for standard webhook integrations
    - Enter `/` as the escape character to use **$** in the body
    - Enter `$` to embed other fields
  2. To define a default value, use the format `${field:defaultValue}`, for example **${ID:12345}**
8. Click **Test**. The CMA sends a test HTTP request with auto-generated content for the fields.

If the integration can connect to the service, then a **Test passed successfully** message is displayed.

If there's a connection error, the page displays the HTTP error code and message reported by the service.
9. Click **Save**. The Webhook integration is saved and added to the **Integrations** tab in the **Subscriptions** page.

### Define The Trigger for Standard Webhook Integrations

Standard webhooks are activated by notifications from the CMA. You can configure two types of notifications:

1. CMA notifications: The CMA can proactively send notifications about your account, such as locked users and admins, or license updates. These notifications can be sent directly via a webhook integration.

For more information, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).
2. Policy rule notifications: You can configure the **Track** setting in a policy rule to send a notification to a webhook whenever the rule is matched.

When defining rules in policies, you can use the **Actions** area to send notifications via webhook integrations.

![rule_webhook.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35315716451869.png)

## Correlated Webhook Integrations

The XOps service supports correlated webhooks that let you integrate the lifecycle of XOps security and network stories with a third-party platform. After you configure the integration, the third-party platform automatically creates a new ticket, issue, or message when a story starts, and then updates it as the story progresses or is resolved.

These integrations use correlation fields from [XOps Stories](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) to map each story in the CMA to a ticket, issue, or message in the external platform. This ensures that updates are consistently applied to the correct item. An XOps license is required.

These integrations require:

- A standard webhook integration
- A correlated webhook integration
- Two types of triggers (one for each integration)

### Define a Standard Webhook

Create a standard webhook integration to create the initial items (ticket, Slack message, etc.) in your third-party tool. These items will then be updated by the correlated webhook integration.

After defining the details, you can test the connection and validate that it works.

**To define a standard Webhook integration:**

1. From the navigation menu, click **Account > Subscriptions** and select the **Webhooks** tab.
2. Click **New Webhook**. The **New Webhook Integration** panel opens.
3. Configure the **Webhook details**:
  1. Enter the integration **Name**.
  2. Click the slider to enable (green) or disable (gray) the integration (it's enabled by default).
4. Configure the settings for the JSON template for the integration:

**Note:** If you choose a different template, the fields in the **Custom Body** are reset. For more information about the templates, see below [Templates and Fields](/v1/docs/sending-cma-notifications-via-webhooks#templates-and-fields).
  - In **Start from template**, select the default JSON template that populates the integration settings.

You can adjust and modify the fields for the **Custom Body** (see below step 7).
5. Configure the **Connection Details**:
  1. Enter the **URL** for the service that is receiving the Webhook.

You can use fields as variables in the URL. Type **$** to see the available fields.
  2. In the **Request Method**, select **POST**.
  3. If necessary, configure the **Authentication Method** and settings for the service.
6. **(Optional)** In **Custom Headers**, define the **Key** and **Value** for each additional HTTP header for the integration.
7. In **Custom Body**, define the content of the Webhook notification:
  1. In **Response Correlation ID**, define the item in your third-party that you will use for correlation in the URL. For example, in ServiceNow this might be result.sys_id , and in Zendesk this might be ticket.id.
  2. **(Optional)** Customize the content in **Edit Body**.
    - Enter `/` as the escape character to use **$** in the body
    - Enter `$` to embed other fields
  3. To define a default value, use the format `${field:defaultValue}`, for example **${ID:12345}**
8. Click **Test**. The CMA sends a test HTTP request with auto-generated content for the fields.

If the integration can connect to the service, then a **Test passed successfully** message is displayed.

If there's a connection error, the page displays the HTTP error code and message reported by the service.
9. Click **Save**. The Webhook integration is saved and added to the **Integrations** tab in the **Subscriptions** page.

### Define a Correlated Webhook

Create a correlated webhook integration that sends notifications via items (ticket, Slack message, etc.) in your third-party tool by updating existing items created in the previous procedure.

When you configure a correlated webhook, the URL uses the correlation ID to update the correct item in the third-party platform. If the correlation ID value is empty, the update can’t be matched to the existing item and is lost. To prevent this, add the item **ID** to the Custom Body of the standard webhook that creates the original ticket, issue, or message. This lets the correlated webhook use that ID as the fallback value for the correlation field, so later updates continue to apply to the original item throughout the story lifecycle.

After defining the details, you can test the connection and validate that it works.

**To define a correlated Webhook integration:**

1. From the navigation menu, click **Account > Subscriptions** and select the **Webhooks** tab.
2. Click **New Webhook**. The **New Webhook Integration** panel opens.
3. Configure the **Webhook details**:
  1. Enter the integration **Name**.
  2. Click the slider to enable (green) or disable (gray) the integration (it's enabled by default).
4. Configure the settings for the JSON template for the integration:

**Note:** If you choose a different template, the fields in the **Custom Body** are reset. For more information about the templates, see below [Templates and Fields](/v1/docs/sending-cma-notifications-via-webhooks#templates-and-fields).
  - In **Start from template**, select the default JSON template that populates the integration settings.

You can adjust and modify the fields for the **Custom Body** (see below step 7).
5. Configure the **Connection Details**:
  1. Enter the **URL** for the service that is receiving the Webhook. Correlated this with an existing item by adding the **Correlated Item Id** field.

You can use fields as variables in the URL. Type **$** to see the available fields.
  2. In the **Request Method**, select **PUT**.
  3. If necessary, configure the **Authentication Method** and settings for the service.
6. **(Optional)** In **Custom Headers**, define the **Key** and **Value** for each additional HTTP header for the integration.
7. In **Custom Body**, define the content of the Webhook notification:
  1. **(Optional)** Customize the content in **Edit Body**.
    - Enter `/` as the escape character to use **$** in the body
    - Enter `$` to embed other fields
  2. To define a default value, use the format `${field:defaultValue}`, for example **${ID:12345}**
8. Click **Test**. The CMA sends a test HTTP request with auto-generated content for the fields.

If the integration can connect to the service, then a **Test passed successfully** message is displayed.

If there's a connection error, the page displays the HTTP error code and message reported by the service.
9. Click **Save**. The Webhook integration is saved and added to the **Integrations** tab in the **Subscriptions** page.

### Define The Trigger for the Standard Webhook Integration

Standard webhooks are activated by notifications from the CMA. You can configure two types of notifications:

1. CMA notifications: The CMA can proactively send notifications about your account, such as locked users and admins, or license updates. These notifications can be sent directly via a webhook integration.

For more information, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).
2. Policy rule notifications: You can configure the **Track** setting in a policy rule to send a notification to a webhook whenever the rule is matched.

When defining rules in policies, you can use the **Actions** area to send notifications via webhook integrations.

![rule_webhook.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35315716451869.png)

### Define the Trigger for the Correlated Integration using Define Detection & Response Notifications

With Detection & Response policies, you can automate creating and updating items in third-party platforms for correlated XOps stories. So your external system always reflects the current story status.

You can configure rules in the policy to:

- Story Created: Trigger a correlated webhook that creates a new item
- Story Updated: Trigger a correlated webhook that updates the same item as the story progresses

To keep stories synchronized, configure two rules: one to create the item when the story starts and one to update it when the story changes.

**To define the trigger for a webhook notification:**

1. From the navigation menu, click **Home > Detection & Response Policy**.
2. Select the **Response Policy** tab.
3. Click **New**. The **Add to Response Policy** panel opens.
4. Enter a **Name** for the rule.
5. In the **Source** section, select the type (for example: **Host**, **IP Range**, **Site**) and then select one or more objects for the story source for this rule (or you can enter an IP address).

The default **Source** value is **Any**.
6. **(Optional)** Define **Criteria** that specify the characteristics a story must have to match the rule.
7. Select the **Trigger** for the rule.
  - **Story Created** for creating new items
  - **Story Updated** for updating existing items
8. In the **Response** tab, select **Send Notification**.
9. In **Send notifications to**, select **Integration**.
10. In **Integration**, select the webhooks integration that is sending notifications.
11. Click **Save**. The rule is added to the policy.

## Templates and Fields

Each webhook can be fully customized to match your third-party system's format and behavior. The webhook is provided in JSON format and can be adjusted to fit the target platform structure. Use Cato field variables for both static and dynamic payloads.

After selecting a template, you can edit the body as a JSON payload and save it as a **Custom** template. You also have the option to embed data fields in the JSON, which will put the relevant value in the payload (or **NA** if not available).

When you type **$**, the available fields are displayed. For more information about the Cato fields, see [Understanding the JSON Fields for Alert Integrations](/v1/docs/understanding-the-json-fields-for-alert-integrations).

You can choose from these templates when creating a webhook:

- **All fields** - includes every available field
- **Basic** - a template with the most commonly used fields
- **Jira** - a basic Jira template
- **ServiceNow Create Ticket** - creates a new ticket in ServiceNow
- **ServiceNow Update Ticket** - updates an existing ticket in ServiceNow
- **Slack** - sends a message to a Slack channel
- **Zendesk Create Ticket** - creates a new ticket in Zendesk
- **Zendesk Update Ticket** - updates an existing Zendesk ticket
- **Custom** - customize settings for a template

You can also use fields when defining the URL of a webhook integration.
