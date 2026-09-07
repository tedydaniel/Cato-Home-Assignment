---
title: "Slack: Configuring the Data Protection API Connector"
slug: "slack-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/slack-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack: Configuring the Data Protection API Connector

This article explains how to configure the Slack connector for the App & Data API Protectionpolicy for your account and create rules that use this connector in the Threat Protection and Data Protection Policy.

The App & Data API Protection policy requires a separate Cato license. Please contact your Cato representative or official reseller for more information.

## Overview of the Slack Connector

Create the connector for the Slack workspace for your organization. Then define rules in the Threat Protection and Data Protection policy that include the Slack connector and define that traffic that is scanned and inspected. You can create a single Slack connector for each tenant.

### Prerequisites

- Admin permissions for the Slack workspace
- The connector monitors files, other actions will be supported soon
- **Note**: Only Public and Shared Slack channels are supported

### Required Permissions for the API Connectors for Slack

To enable the Data Protection API to scan assets and content for Slack messages, the connector gives Cato the following permissions and actions with the Slack app:

- Grant access to the app using Oauth2
- Receive a token from the app to establish and maintain a secure connection
- Connect to the Slack APIs and fetch data and scan files according to the App & Data API Protection policy, including:
  - Read messages and files in workspace
  - View content and info about:
    - Admin account (you)
    - Channels and conversations
    - Organization's workspace

### Known Limitations

- Private channels are only supported if the Slack user that created the connector is included in the private channel

## Working with Slack Connectors

This section explains how to create API connectors for Slack, and to connect your organization's Slack workspace to your Cato account.

### Creating the Slack Connector

Use the Cato Management Application to create the Slack connector, there's no need to configure settings in Slack. The Slack connector lets the Cato SaaS API engine scan messages and attachments for the content that you define in the Data Protection policy.

**To create the connector for Slack:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **SaaS Application** drop down, select **Slack**.

Only **Read** permissions and actions are currently supported for the Slack app. However, **Read/Write** permissions and actions are coming soon.
4. In the **Capability** section, select **Data and Threat Protection**.
5. Enter a **Connector Name**.
6. Click **Authorize and Save**.

The Slack permissions screen opens in a new browser tab.
7. Give permissions for your Cato account to access the Slack app.
  1. **Allow** the permissions for Cato to access the Slack app.

![Slack_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640019983005.png)
  2. The screen shows that you have successfully applied the permissions for the tenant.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639993835677.png)

You can close the browser tab and return to the Cato Management Application. It can take Slack several seconds to process the request, so if you receive an error, refresh the browser.

While Slack is processing the request, the Status for the connector is **Pending user consent** (see below *Understanding the Connector Status*).
8. The Slack SaaS application is added to the **Integrated APIs** tab.

### Understanding the Connector Status

The **Status** column on the Connectors Settings screen shows the status of the connection between the Slack app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Connection error** - Connectivity or permissions issue with the Slack connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Pending user consent** - The Slack connector is created in the Connect Settings screen, however you haven't completed the process in the Slack account to authorize it to connect to Cato.

## Adding Slack Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor and manage the messages and attachments that your users send and receive over Slack.

### Configuring Slack Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

For Slack users, the connector distinguishes between bots and user accounts. You can define one rule for users and a separate rule for bots.

For more information about the Slack rule settings, see below [Understanding the Slack Rules](/v1/docs/slack-configuring-the-data-protection-api-connector#understanding-the-slack-rules).

![Slack_Data_Protection_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005648541.png)

**To create a new Data Protection rule for the Slack app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the Slack app.
4. In the **General** section, enter the settings for the rule.
5. In **Sender**, select one or more **Slack Users** that are Slack messages (default value is **Any**).

When you select multiple users, there is an OR relationship between them.
6. In **Sharing Options**, select one or more types of Slack messages and channels that are scanned (default value is **Any**).

When you select multiple options, there is an OR relationship between them.
7. In **Attachments**, define the criteria to specify the file attachments which are scanned (the default setting is to scan all files).
8. In **Content Profile**, select the DLP Content Profile for this rule.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
9. In **Actions**, select **Monitor**.
10. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
11. Click **Save**. The rule is added to the Data Protection policy.

### Understanding the Slack Rules

This section explains the settings for the Data Protection rules that use the Slack connector.

- Sender - Slack users in your workspace (default value is Any)
- Sharing Options - Select the types of file sharing permissions that match this rule (default value is Any)
  - Public Channel - Slack channel where any user can join the channel
  - Shared Channel - Slack channels that contain users from outside of your organization
- Attachments - Criteria for attachments that are scanned (default value is all attachments)
  - File Type
  - File Name
  - File Size (maximum file size is 100 MB)
- Content Profile - DLP Content Profile that defines the DLP content inspection

You can create or edit Content Profiles in Security > DLP Profiles > DLP Profiles > Content Profile
- Actions - Select if you want to generate an event when the rule is matched

#### Defining Files or Attachments for a Rule

You can define specific files (or attachments) for a rule and limit the SaaS API engine to only scan the specified files to see if they match the DLP Content Profile.

When you add multiple files to a rule, select the relationship between them:

- **Satisfy any (OR)** - Match only one of the File Types in the rule
- **Satisfy all (AND)** - Match all the File Types in the rule (otherwise, the rule is ignored)

You can use the File Name setting in a rule to define the exact file name or use wildcards to define keywords. For example, you can define the File Name as **internal** to match all file names that contain the word **internal**.

### Working with Ordered Data Protection Rules

The Data Protection API engine inspects the data sequentially, and checks to see if it matches a rule. If the data does not match a rule, then it is not inspected. Rules that are at the top of the rulebase have a higher priority and they are applied before the rules lower down in the rulebase. Each type of application or connector is only applied to the data once.

Best Practice - To maximize the efficiency of your rulebase, we recommend that for each connector type, rules for specific users have a higher priority than rules that apply to **Any** users.

For example, if the data matches a connector in rule #2, the data is inspected by the Data Protection API engine. The engine does not continue to apply rules #3 and below for the same connector. However, the data could match a lower priority rule with a different connector.

## Adding Threat Protection to the Connector

You can create Threat Protection rules for the connector to scan files and attachment for malware and viruses using the Anti-Malware and Next Gen Anti-Malware engines that are enabled for your account. The Data Protection API engine scans the connector traffic and applies the action and tracking options that you configure for the rule:

- Monitor the traffic (block will be supported soon)
- Generate events
- Send email notifications

When you create a App & Data API Protection rule, the Anti-Malware engines that are enabled for your account (Security > Anti-Malware) perform malware scans on the files that are sent for that connector application.

The following screenshot shows a Threat Protection rule for the OneDrive connector that scans files sent by Internal users or Guests:

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005712797.png)

## Creating an Exception for a File

Sometimes there is file blocked by Cato's Data Protection API engines that you know is safe, and you need to allow it in the network. Anti-Malware Exceptions in the File Hash policy also apply to the App & Data API Protection. For more information on adding files to the File Hash Policy, see [Managing Anti-Malware Exceptions](/v1/docs/managing-anti-malware-exceptions).

## Analyzing Data Protection API Events

The Home > Events page shows all the Data Protection API events for your account. The powerful search tools let you drill-down and identify the few events that contain the relevant data that you need.

Data Protection API events can be identified by the following fields:

- Event Type - Security
- Sub-Type - SaaS Security API Data Protection and SaaS Security API Anti Malware

You can learn more about using the Events page [here](/v1/docs/analyzing-events-in-your-network).

### Explaining the Data Protection API Events Fields

| Field Name | Description |
| --- | --- |
| Connector Name | Name for the connector that is defined for the rule |
| Connector Type | SaaS app that is defined for this connector |
| DLP Profile | DLP Content Profile that generated this event |
| File Name | Name of the attached file |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Collaborators | Email addresses of the users that received the file |
| Rule | Name of the rule in the Data Protection policy |
| Sender | Slack user that sent the message or file |
| Severity | Severity defined for the rule |
| Sharing Scope | Sharing Options for the Slack attachment |
