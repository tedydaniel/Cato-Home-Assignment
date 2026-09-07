---
title: "Box: Configuring the Data Protection API Connector"
slug: "box-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/box-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Box: Configuring the Data Protection API Connector

This article explains how to configure the Box connector for the App & Data API Protection policy for your account and create rules that use this connector in the Data Protection or Threat Protection Policy.

The App & Data API Protection policy requires a separate Cato license. Please contact your Cato representative or official reseller for more information.

## Overview of the Box Connector

Create the connector for the Box tenant for your organization. Then define rules in the Data Protection policy that include the Box connector and define that files that are scanned and inspected. You can create a single Box connector for each tenant.

### Prerequisites

- Admin or co-admin permissions for the Box tenant
- The connector monitors files, other actions will be supported soon

### Required Permissions for the API Connectors for Box

To enable the Data Protection API to scan files and folders in your Box account, the connector gives Cato the following permissions and actions with the Box app:

- Grant access to the app using Oauth2
- Receive a token from the app to establish and maintain a secure connection
- Connect to the Box APIs and fetch data and scan files according to the App & Data API Protection policy, including:
  - For monitoring action - Read all files and folders stored in Box
    - For other actions - Write permissions for all files and folders stored in Box
  - Access user data in your Box account
  - Cato admin can make calls on behalf of Box users

### Known Limitations

- Files uploaded to the root folder, can take up to 24 hours to be available to the connector
  - Files uploaded to sub-folders and directories are available right away

## Working with Box Connectors

This section explains how to create API connectors for Box, and to connect your organization's Box tenant to your Cato account.

### Creating the Box Connector

When you create the Box connector, the Cato Management Application generates the Client ID for that connector. Then, log in to the Admin Console for your Box account, and create a new User Authentication app. Enter the Client ID in the Cato Box app, and then authorize Cato to connect to your Box account. Finally, save the Box connector in the Cato Management Application and Cato is now ready monitor Box files and folders.

**To create the connector for Box:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. From the **SaaS Application** drop down, select **Box**.

Currently, only **Read** permissions and actions are supported for the Box app. However, **Read/Write** permissions and actions will be supported soon.
4. In the **Capability** section, select **Data and Threat Protection**.
5. Enter the **Connector Name**.
6. Copy the **Client ID** to the OS clipboard.
7. Create the Cato Box app for this connector:
  1. Click the link to open the Box admin console for your account.

The Box screen opens in a new browser tab.
  2. Log in to your Box tenant.
  3. From the Box navigation menu, select **Admin Console**.
  4. Select **Apps > Platform Apps Manager > User Authentication Apps**.

![Box_User_Apps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640004472861.png)
  5. Click the plus symbol.
  6. In the **Add App** window, paste the **Client ID** (from step 5 above).

![Box_Client_ID.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640004518941.png)
  7. Click **Next**.
  8. In the **Authorize App** window, click **Authorize** to give Cato permission to access the Box app.

![Box_Authorize_App.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640004553757.png)

The new app is added to your Box account.
8. In the Cato Management Application , click **Authorize and Save**.

A Box permissions screen opens in a new browser tab.
9. Give permissions for your Cato account to access the Box app.
  1. Click **Grant access to Box** to allow Cato to access the Box app.

![Grant_Access_Box.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640023768349.png)
  2. The screen shows that you have successfully applied the permissions for the tenant.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640034066333.png)

You can close the browser tab and return to the Cato Management Application. It can take Box several seconds to process the request, so if you receive an error, refresh the browser.

While Box is processing the request, the Status for the connector is **Pending user consent** (see below *Understanding the Connector Status*).
10. The Box SaaS application is added to the **Integrated APIs** tab.

### Understanding the Connector Status

The **Status** column on the Connectors Settings screen shows the status of the connection between the Box app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Connection warning** - Some of the users in the Box tenant are not configured correctly to support the Data Protection API. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Connection error** - Connectivity or permissions issue with the Box connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).

Box supports only creating one connector per tenant.
- **Pending user consent** - The Box connector is created in the Connect Settings screen, however you haven't completed the process to authorize Cato to connect to your Box account.

## Adding Box Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor and manage the files and folders that your users upload and download with Box.

### Understanding Box Actions

When you create a Data Protection rule, you can define different actions to monitor or remediate the policy violations when the rule is matched. Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/box-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

These are the actions you can set for the Data Protection engine to perform when a rule is matched:

- **Monitor** - Generates an event to let you monitor traffic that matches the rule.
- **Remove Share** - When a user tries to share a file, the Data Protection API engine removes the unauthorized sharing permission, and the user who receives a link to the shared file won't have permissions to access the file.

> [!NOTE]
> Note:
> 
> New files added to the root folder can take up to 24 hours before they are scanned and before rule actions are applied to them. Files in sub-folders are scanned immediately after they are uploaded.

### Configuring Box Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

Create a Data Protection rule to define the traffic that is scanned by Data Protection API. Create separate rules for each SaaS app connector, and then define the criteria which determines which traffic is scanned.

For more information about the Box rule settings, see below [Understanding the Box Rules](/v1/docs/box-configuring-the-data-protection-api-connector#understanding-the-box-rules).

![Box_Data_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640006841501.png)

**To create a new Data Protection rule for the Box app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the Box app.
4. In the **General** section, enter the settings for the rule.
5. In **Owner**, select one or more Box users that you are monitoring (default value is **Any**).

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

#### Understanding the Box Rules

This section explains how to define the settings for the Data Protection rules to scan the correct Box traffic. Each rule can be defined according to the following criteria:

- Owner - Box users in your workspace (default value is Any)
  - Internal - Owner is any user in your company
  - Box User - Owner is a specific user
- Sharing Options - Select the types of file and folder sharing permissions that match this rule (default value is Any)
  - Private - Only user has access
  - People with the link - Publicly accessible to anyone with the link (no need to sign in to Box)
  - People in the company - Any user in your company with the link
  - Invited only company people - Any user in your company with the link
  - Invited only public people - External users that received an invitation with the link
- File Attributes - Criteria for attachments that are scanned (default value is all attachments)
  - File Type
  - File Name
  - File Size (maximum file size is 20 MB)
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
- **Remove Share** - When a user tries to share a file, the Data Protection API engine removes the unauthorized sharing permission, and the user who receives a link to the shared file won't have permissions to access the file.

Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/box-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

When you create a App & Data API Protection rule, the Anti-Malware engines that are enabled for your account (Security > Anti-Malware) perform malware scans on the files that are sent for that connector application.

The following screenshot shows a Threat Protection rule for the OneDrive connector that scans files sent by Internal users or Guests:

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640023958557.png)

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
| Sharing Scope | Sharing Options for the Box attachment |
