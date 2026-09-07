---
title: "Microsoft OneDrive: Configuring the Data Protection API Connector"
slug: "microsoft-onedrive-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/microsoft-onedrive-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft OneDrive: Configuring the Data Protection API Connector

This article explains how to configure the Microsoft OneDrive connector for the App & Data API Protection policy for your account and create a OneDrive rule for the Data Protection Policy

The App & Data API Protection policy requires a separate license from Cato. Please contact your Cato representative or official reseller for more information.

> [!NOTE]
> Note:
> 
> Please contact [SaaSecAPI@catonetworks.com](mailto:SaaSecAPI@catonetworks.com) or your official Cato reseller for more information about using the App & Data API Protection policy.

## Overview of the Microsoft Connectors

Create the connectors for the Microsoft 365 and OneDrive SaaS apps.

Each Microsoft OneDrive app and Azure tenant (according to the 365 app) are subject the Microsoft's rate limiting. For more information, see the [Microsoft documentation](https://docs.microsoft.com/en-us/graph/throttling#pattern).

### Prerequisites

- The Microsoft 365 connector requires an admin with the global admin role to give permissions to Data Protection API

### Required Permissions for the API Connectors for OneDrive

To enable Data Protection API to scan assets and content for OneDrive files and folders, the connector gives Cato the following permissions and actions with the OneDrive app:

- Grant access to the app using Oauth2
- Receive a token from the app to establish and maintain a secure connection
- Connect to the Microsoft APIs and fetch data and scan files according to the App & Data API Protection policy, including:
  - Read files in all the sites collections
  - Sign in and read the full profiles of the users
  - Write files in all the sites collections (coming soon)

## Working with Microsoft OneDrive API Connectors

This section explains how to create API connectors for Microsoft 365 and OneDrive, and to connect them to your Cato account.

### Understanding the API Connectors for Microsoft OneDrive

To enable Data Protection API to scan assets and content for Microsoft OneDrive, first you need to configure the Microsoft 365 connector as the parent app to give read permissions for the OneDrive connector. The parent app only has permissions to manage the Microsoft connectors. Afterwards, if necessary, you can create a separate Microsoft 365 connector for each Azure tenant.

### Step 1: Creating the Microsoft 365 Connector

Use the Cato Management Application to create the Microsoft 365 SaaS application connector for the Azure tenant for the Microsoft OneDrive app that your are scanning with Data Protection API . You must have the correct credentials to authenticate to the Microsoft OneDrive app to add it to your Cato account.

Before you can create and configure the connector settings, first you need to enable Data Protection API for your account.

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

![Create_API_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640002747805.png)

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640002784029.png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639971610781.png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

### Step 2: Creating the Microsoft OneDrive Connector

The Microsoft OneDrive connector lets the Data Protection API engine scan files for the content that you define in the Data Protection policy.

> [!NOTE]
> Note:
> 
> When you create an API connector for a Microsoft 365 app, the connector creates an authentication certificate that is valid for 3 months, and renews the certificate 7 days before expiration.

**To create the connector for Microsoft OneDrive:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. Create a new **OneDrive SaaS Application**, for the **Connector Parent** you created in the previous section.
4. Click **Authorize and Save**.
5. In a new browser tab, authenticate to the OneDrive app.
  1. Select the Microsoft account for the OneDrive app and log in.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions for Cato to access the OneDrive app.

![OneDrive_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639988464413.png)
  4. The screen shows that you have successfully applied the permissions for the app.

You can close the browser tab and return to the Cato Management Application.

It can take Microsoft Azure several seconds to process the request, so if you receive an error, refresh the browser.
6. The OneDrive SaaS application is added to the **Integrated Apps** tab.

### Understanding the Connector Status

The **Status** column on the Connectors Settings screen shows the status of the connection between the Microsoft app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Connection Warning** - Some of the users in the Azure tenant are not configured correctly to support Data Protection API (such as, no email address defined for the user). Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Connection Error** - Connectivity or permissions issue, or rate limiting (Microsoft limitation) with the Microsoft connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Pending User Consent** - The OneDrive connector is created in the Connect Settings screen, however you haven't completed the process in the OneDrive account to authorize it to connect to Cato.

## Adding OneDrive Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor and manage the actions that your users perform with OneDrive files. For example, sharing files, creating new files, uploading and so on.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).

### Understanding OneDrive Actions

When you create a Data Protection rule, you can define different actions to monitor or remediate the policy violations when the rule is matched. Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/microsoft-onedrive-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

These are the actions you can set for the Data Protection engine to perform when a rule is matched:

- **Monitor** - Generates an event to let you monitor traffic that matches the rule.
- **Remove Share** - When a user tries to share a file, the Data Protection API engine removes the unauthorized sharing permission, and the user who receives a link to the shared file won't have permissions to access the file.
- **Quarantine** - When a user tries to upload a file, the Data Protection APIengine moves it to a quarantine folder and then users can no longer access it. The Onedrive admin can access the file in the quarantine folder. For information about configuring quarantine folders, see [Preparing for File Quarantine](/v1/docs/microsoft-onedrive-configuring-the-data-protection-api-connector#preparing-for-file-quarantine).

### Preparing for File Quarantine

Configure quarantine folders for Data Protection and Threat Prevention rules, and define the OneDrive admin with permissions to access the folders. You can configure quarantine folders for each OneDrive admin for the tenant. When you configure the folders, you can then create rules with the **Quarantine** action, and define the folder that the file is moved to.

![SaaS_Security_API_Settings_Onedrive.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639991650973.png)

**To configure quarantine folders for a OneDrive admin:**

1. From the navigation pane, select **Security > App & Data API Protection** and select the **Settings** tab.
2. Click **New**. The **Quarantine Folder** panel opens.

![SaaS_Security_API_Settings_Onedrive_Quarantine_Folder.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639972225437.png)
3. Select the **OneDrive** application connector.
4. Select the OneDrive admin to have access to these quarantine folders.
5. Click **Save**.

A Data Protection folder and a Threat Prevention folder are created for the admin, and can be configured in rules with the **Quarantine** action. The folders are named with the admin's email address, and located in the following OneDrive directories:
  - Data Protection folder: Cato_Qarantine/Cato_Qarantine_DataProtection
  - Threat Prevention folder: Cato_Qarantine/Cato_Qarantine_ThreatPrevention

### Configuring OneDrive Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

Create a Data Protection rule to define the traffic that is scanned by Data Protection API. Create separate rules for each SaaS app connector, and then define the criteria which determines which traffic is scanned.

For more information about the OneDrive rule settings, see below [Understanding the OneDrive Rules](/v1/docs/microsoft-onedrive-configuring-the-data-protection-api-connector#understanding-the-onedrive-rules).

![OneDrive_Data_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639972293277.png)

**To create a new Data Protection rule for the OneDrive app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the OneDrive app.
4. In the **General** section, enter the settings for the rule.
5. In **Owner**, select one or more OneDrive file owners (default value is **Any**).

When you select multiple owners, there is an OR relationship between them.
6. In **Sharing Options**, select one or more file permission types (default value is **Any**).

When you select multiple options, there is an OR relationship between them.
7. In **Attachments**, define the criteria to specify the files which are scanned (the default setting is to scan all files).
8. In **Content Profile**, select the DLP Content Profile for this rule.
9. Select an **Action**.

For the **Quarantine** action, select a **Quarantine folder path**. For more about quarantine folders, see above ???.
10. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
11. Click **Save**. The rule is added to the Data Protection policy.

#### Understanding the OneDrive Rules

This section explains how to define the settings for the Data Protection rules to scan the correct OneDrive traffic. Each rule can be defined according to the following criteria:

- Owner - individual users, or Azure types of users that are the owners of the relevant OneDrive directories (default value is Any)
- Sharing Options - Select the types of file sharing permissions that match this rule (default value is Any)

For example, to monitor files that are shared with any external users, select **External Link**.
- Attachments - Criteria for attachments that are scanned (default value is all attachments)
  - File Type
  - File Name
  - File Size (maximum file size is 100 MB)
- Content Profile - DLP Content Profile that defines the DLP content inspection (Security > DLP Profiles > DLP Profiles > Content Profile)
- Actions - See above [Understanding OneDrive Actions](/v1/docs/microsoft-onedrive-configuring-the-data-protection-api-connector#understanding-onedrive-actions)

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

You can create Threat Protection rules for the connector to scan files and attachments for malware and viruses using the Anti-Malware and Next Gen Anti-Malware engines that are enabled for your account. The Data Protection API engine scans the connector traffic and applies the action and tracking options that you configure for the rule.

These are the actions you can set for the Threat Protection engine to perform when a rule is matched:

- **Monitor** - Generates an event to let you monitor traffic that matches the rule.
- **Remove Share** - When a user tries to share a file, the Data Protection API engine removes the unauthorized sharing permission, and the user who receives a link to the shared file won't have permissions to access the file.
- **Quarantine** - When a user tries to upload a file, the Data Protection APIengine moves it to a quarantine folder and then users can no longer access it. The Onedrive admin can access the file in the quarantine folder. For information about configuring quarantine folders, see [Preparing for File Quarantine](/v1/docs/microsoft-onedrive-configuring-the-data-protection-api-connector#preparing-for-file-quarantine).

Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/microsoft-onedrive-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

When you create a App & Data API Protection rule, the Anti-Malware engines that are enabled for your account (Security > Anti-Malware) perform malware scans on the files that are sent for that connector application.

The following screenshot shows a Threat Protection rule for the OneDrive connector that scans files sent by Internal users or Guests:

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639989244317.png)

### Creating an Exception for a File

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
| Collaborators | Email addresses of the users that received the file |
| Connector Name | Name for the connector that is defined for the rule |
| Connector Type | SaaS app that is defined for this connector |
| DLP Profile | DLP Content Profile that generated this event |
| File Name | Name of the attached file |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Owner | File owner |
| Parent Connector Type | Parent Microsoft 365 connector |
| Rule | Name of the rule in the Data Protection policy |
| Severity | Severity defined for the rule |
| Sharing Scope | Sharing Options for the OneDrive file |
