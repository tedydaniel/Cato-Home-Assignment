---
title: "Dropbox: Configuring the Data Protection API Connector"
slug: "dropbox-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/dropbox-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dropbox: Configuring the Data Protection API Connector

This article explains how to configure the Dropbox connector for the App & Data API Protection policy for your account and create rules that use this connector in the Data Protection Policy.

The App & Data API Protection policy requires a separate Cato license. Please contact your Cato representative or official reseller for more information.

## Overview of the Dropbox Connector

Create the connector for the Dropbox tenant for your organization. Then define rules in the [Data Protection policy](/v1/docs/dropbox-configuring-the-data-protection-api-connector#adding-dropbox-rules-to-the-data-protection-policy) that include the Dropbox connector and define that files that are scanned and inspected. You can create a single Dropbox connector for each tenant.

### Prerequisites

- Team admin permissions for the Dropbox tenant
- Supported with the Dropbox Business Plus plan

### Required Permissions for the API Connectors for Dropbox

To enable the Data Protection API to scan files and folders in your Dropbox account, the connector gives Cato the following permissions and actions with the Dropbox app:

- Individual permissions
  - View content of members' Dropbox files and folders
  - View members' Dropbox file requests and Dropbox sharing settings and collaborators
  - View basic information about members' Dropbox accounts, such as username, email, and country
- Team permissions
  - View information about your team's files and folders
  - View and edit content of, governance data of, and information about your team's files and folders
  - View your team membership
  - View your team's activity log
  - View the structure of your team's and members' folders
  - View basic information about your team, including names, user count, and team settings

### Known Limitations

- The connector identifies a share activity after any subsequent activity is performed in the Dropbox tenant by any of the account users (not at the original file sharing action)

## Working with Dropbox Connectors

This section explains how to create API connectors for Dropbox, and to connect your organization's Dropbox tenant to your Cato account.

### Creating the Dropbox Connector

Use the Cato Management Application to create the Dropbox connector, there's no need to configure settings in Dropbox. The Dropbox connector lets the Cato SaaS API engine scan files for the content that you define in the Threat Protection and Data Protection policy.

**For EA** - Currently the **Monitor** action is supported which only requires **Read** permissions. However, we recommend configuring the Dropbox connector with **Read/Write** permissions so you will not need to make any changes to the connector to apply additional actions in the future (i.e. Quarantine).

**To create the connector for Dropbox:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **SaaS Application** dropdown, select **Dropbox**.
4. In the **Capability** section, select **Data and Threat Protection**.
5. Enter the **Connector Name**.
6. In the Cato Management Application , click **Authorize and Save**.

A Dropbox permissions screen opens in a new browser tab.
7. Give permissions for your Cato account to access the Dropbox tenant.
  1. Click **Continue** to confirm that you want Cato to access the Dropbox tenant.

![01_Dropbox_permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640024031517.png)
  2. Click **Allow** to allow Cato to access the Dropbox tenant.

![02_Dropbox_permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640004945309.png)
  3. The screen shows that you have successfully applied the permissions for the tenant.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640019427101.png)

You can close the browser tab and return to the Cato Management Application. It can take Dropbox several seconds to process the request, so if you receive an error, refresh the browser.

While Dropbox is processing the request, the Status for the connector is **Pending user consent** (see below *Understanding the Connector Status*).
8. The Dropbox SaaS connector is added to the **Integrated Apps** tab.

### Understanding the Connector Status

The **Status** column on the Connectors Settings screen shows the status of the connection between the Dropbox app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Connection warning** - Some of the users in the Dropbox tenant are not configured correctly to support the Data Protection API. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Connection error** - Connectivity or permissions issue with the Dropbox connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).

Dropbox supports only creating one connector per tenant.
- **Pending user consent** - The Dropbox connector is created in the Connect Settings screen, however you haven't completed the process to authorize Cato to connect to your Dropbox account.

## Adding Dropbox Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor and manage the files and folders that your users upload and download with Dropbox.

### Understanding Dropbox Actions

When you create a Data Protection rule, you can define different actions to monitor or remediate the policy violations when the rule is matched. Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/dropbox-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

These are the actions you can set for the Data Protection engine to perform when a rule is matched:

- **Monitor** - Generates an event to let you monitor traffic that matches the rule.

### Configuring Dropbox Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

Create a Data Protection rule to define the traffic that is scanned by Data Protection API. Create separate rules for each SaaS app connector, and then define the criteria which determines which traffic is scanned.

For more information about the Dropbox rule settings, see below [Understanding the Dropbox Rules](/v1/docs/dropbox-configuring-the-data-protection-api-connector#understanding-the-dropbox-rules).

![Dropbox_rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640034404893.png)

**To create a new Data Protection rule for the Dropbox app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the Dropbox app.
4. In the **General** section, enter the settings for the rule.
5. In **Owner**, select one or more Dropbox users that you are monitoring (default value is **Any**).

When you select multiple users, there is an OR relationship between them.
6. In **Sharing Options**, select permission level for files and folders that are scanned (default value is **Any**).

When you select multiple options, there is an OR relationship between them.
7. In **File Attributes**, define the criteria to specify the files which are scanned (the default setting is to scan all files).
8. In **Content Profile**, select the DLP Content Profile for this rule.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
9. Select an **Action**.
10. **(Optional)** Define the tracking options for the rules to generate email notifications.

For more information about events and email notifications, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).
11. Click **Save**. The rule is added to the Data Protection policy.

#### Understanding the Dropbox Rules

This section explains how to define the settings for the Data Protection rules to scan the correct Dropbox traffic. Each rule can be defined according to the following criteria:

- **Owner** - Dropbox users in your workspace (default value is Any)
  - **Internal** - Owner is any user in your company
  - **Dropbox User** - Owner is a specific user
- **Sharing Options** - Select the types of file and folder sharing permissions that match this rule (default value is Any)
  - **Private** - Only user has access
  - **People with the link** - Publicly accessible to anyone with the link (no need to sign in to Dropbox)
  - **People in the company** - Any user in your company with the link
  - **Invited only company people** - Any user in your company that were invited to share the file
  - **Invited only public people** - External users that were invited to share the file
- **File Attributes** - Criteria for attachments that are scanned (default value is all attachments)
  - **File Type**
  - **File Name**
  - **File Size** (maximum file size is 20 MB)
- Content Profile - DLP Content Profile that defines the DLP content inspection

You can create or edit Content Profiles in Security > DLP Profiles > DLP Profiles > Content Profile
- Actions - Select if you want to generate an event or email notification when the rule is matched

#### Defining Files or Attachments for a Rule

You can define specific files (or attachments) for a rule and limit the SaaS API engine to only scan the specified files to see if they match the DLP Content Profile.

When you add multiple files to a rule, select the relationship between them:

- **Satisfy any (OR)** - Match only one of the File Types in the rule
- **Satisfy all (AND)** - Match all the File Types in the rule (otherwise, the rule is ignored)

You can use the File Name setting in a rule to define the exact file name or use wildcards to define keywords. For example, you can define the File Name as **internal** to match all file names that contain the word **internal**.

#### Working with Ordered Data Protection Rules

The Data Protection API engine inspects the data sequentially, and checks to see if it matches a rule. If the data does not match a rule, then it is not inspected. Rules that are at the top of the rulebase have a higher priority and they are applied before the rules lower down in the rulebase. Each type of application or connector is only applied to the data once.

Best Practice - To maximize the efficiency of your rulebase, we recommend that for each connector type, rules for specific users have a higher priority than rules that apply to **Any** users.

For example, if the data matches a connector in rule #2, the data is inspected by the Data Protection API engine. The engine does not continue to apply rules #3 and below for the same connector. However, the data could match a lower priority rule with a different connector.

## Adding Threat Protection to the Connector

You can create Threat Protection rules for the connector to scan files and attachments for malware and viruses using the Anti-Malware and Next Gen Anti-Malware engines that are enabled for your account. The Data Protection API engine scans the connector traffic and applies the action and tracking options that you configure for the rule.

These are the actions you can set for the Threat Protection engine to perform when a rule is matched:

- **Monitor** - Generates an event to let you monitor traffic that matches the rule.

Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/dropbox-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

When you create a App & Data API Protection rule, the Anti-Malware engines that are enabled for your account (Security > Anti-Malware) perform malware scans on the files that are sent for that connector application.

The following screenshot shows a Threat Protection rule for the OneDrive connector that scans files sent by Internal users or Guests:

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005072925.png)

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
| File Size | Size of the attached file |
| File Type | File type for the attached file |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Collaborators | Email addresses of the users that received the file |
| Rule | Name of the rule in the Data Protection policy |
| Owner | File owner |
| Severity | Severity defined for the rule |
| Sharing Scope | Sharing Options for the Dropbox attachment |
