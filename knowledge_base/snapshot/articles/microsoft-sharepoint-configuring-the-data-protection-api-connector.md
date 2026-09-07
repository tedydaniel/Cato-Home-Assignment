---
title: "Microsoft SharePoint: Configuring the Data Protection API Connector"
slug: "microsoft-sharepoint-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/microsoft-sharepoint-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft SharePoint: Configuring the Data Protection API Connector

This article explains how to configure the Microsoft SharePoint connector for the App & Data API Protection policy for your account and create a SharePoint rule for the Data Protection Policy

The App & Data API Protection policy requires a separate license from Cato. Please contact your Cato representative or official reseller for more information.

> [!NOTE]
> Note:
> 
> Please contact [SaaSecAPI@catonetworks.com](mailto:SaaSecAPI@catonetworks.com) or your official Cato reseller for more information about using the App & Data API Protection policy.

## Overview of the Microsoft Connectors

Create the connectors for the Microsoft 365 and SharePoint SaaS apps.

Each Microsoft SharePoint app and Azure tenant (according to the 365 app) are subject the Microsoft's rate limiting. For more information, see the [Microsoft documentation](https://docs.microsoft.com/en-us/graph/throttling#pattern).

### Prerequisites

- The Microsoft 365 connector requires an admin with the global admin role to give permissions to Data Protection API

### Required Permissions for the API Connectors for SharePoint

To enable the Data Protection API to scan assets and content for SharePoint files and folders, the connector gives Cato the following permissions and actions with the SharePoint app:

- Grant access to the app using Oauth2
- Receive a token from the app to establish and maintain a secure connection
- Connect to the Microsoft APIs and fetch data and scan files according to the Data Protection API Data Protection policy, including:
  - Read items and files in all the sites collections
  - Sign in and read the full profiles of the users
  - Write files in all the sites collections (coming soon)

## Working with Microsoft SharePoint API Connectors

This section explains how to create API connectors for Microsoft 365 and SharePoint, and to connect them to your Cato account.

### Understanding the API Connectors for Microsoft SharePoint

To enable the Data Protection API to scan assets and content for Microsoft SharePoint, first you need to configure the Microsoft 365 connector as the parent app to give read permissions for the SharePoint connector. The parent app only has permissions to manage the Microsoft connectors. Afterwards, if necessary, you can create a separate Microsoft 365 connector for each Azure tenant.

### Step1: Creating the Microsoft 365 Connector

Use the Cato Management Application to create the Microsoft 365 SaaS application connector for the Azure tenant for the Microsoft SharePoint app that your are scanning with Data Protection API . You must have the correct credentials to authenticate to Microsoft SharePoint app to add it to your Cato account.

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

![Create_API_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639989292701.png)

**To create the Microsoft 365 parent connector:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640003749277.png)
4. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
5. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640003814173.png)

You can close the browser tab and return to the Cato Management Application.
6. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

### Step 2: Creating the Microsoft SharePoint Connector

The Microsoft SharePoint connector lets the Cato SaaS API engine scan emails for the content that you define in the Data Protection policy.

> [!NOTE]
> Note:
> 
> When you create an API connector for a Microsoft 365 app, the connector creates an authentication certificate that is valid for 3 months, and renews the certificate 7 days before expiration.

**To create the connector for Microsoft SharePoint:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click **New**. The **New Connector** panel opens.
3. In **SaaS Application**, select **Microsoft SharePoint**.
4. In **Connector Tenant**, select the parent Microsoft 365 connector you created in the previous section.
5. Enter the **Connector Name**.
6. In **Permissions**, select **Read/Write**.
7. Click **Save**. The Cato connector app is created. This can take up to 30 seconds.

![SaaS_Security_API_App_Created.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639992074013.png)
8. Click **Authorize** to authorize the creation of the connector.

![SaaS_Security_API_Authorize.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639989475101.png)
9. In a new browser tab, authenticate to the SharePoint app.
  1. Select the Microsoft account for the SharePoint app.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions for Cato to access the app.

![Sharepoint_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640003986717.png)
  4. The screen shows that you have successfully applied the permissions for the app.

You can close the browser tab and return to the Cato Management Application.

It can take Microsoft SharePoint several seconds to process the request, so if you receive an error, refresh the browser.
10. The SharePoint SaaS application is added to the **Integrated APIs** tab.

### Understanding the Connector Status

The **Status** column on the Connectors Settings screen shows the status of the connection between the Microsoft app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Connection Warning** - Some of the users in the Azure tenant are not configured correctly to support Data Protection API (such as, no email address defined for the user). Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Connection Error** - Connectivity or permissions issue, or rate limiting (Microsoft limitation) with the Microsoft connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).

## Adding SharePoint Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor and manage the actions that your users perform with SharePoint files. For example, sharing files, creating new files, uploading and so on.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).

### Understanding SharePoint Actions

When you create a Data Protection rule, you can define different actions to monitor or remediate the policy violations when the rule is matched. Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/microsoft-sharepoint-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

These are the actions you can set for the Data Protection engine to perform when a rule is matched:

- **Monitor** - Generates an event to let you monitor traffic that matches the rule.
- **Quarantine** - When a user tries to upload a file, the Data Protection API engine moves it to a quarantine folder and then users can no longer access it. The SharePoint admin can access the file in the quarantine folder. For information about configuring quarantine folders, see below [Preparing for File Quarantine](/v1/docs/microsoft-sharepoint-configuring-the-data-protection-api-connector#preparing-for-file-quarantine).

### Preparing for File Quarantine

Configure quarantine folders for Data Protection and Threat Prevention rules, and define the SharePoint admin with permissions to access the folders. You can configure quarantine folders for each SharePoint admin for the tenant. When you configure the folders, you can then create rules with the **Quarantine** action, and define the folder that the file is moved to.

![SaaS_Security_API_Settings_SharePoint.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640018388893.png)

**To configure quarantine folders for a SharePoint admin:**

1. From the navigation pane, select **Security > App & Data API Protection** and select the **Settings** tab.
2. Click **New**. The **Quarantine Folder** panel opens.

![SaaS_Security_API_Settings_Onedrive_Quarantine_Folder.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640033506589.png)
3. Select the **SharePoint** application connector.
4. Select the SharePoint admin to have access to these quarantine folders.
5. Click **Save**.

A Data Protection folder and a Threat Prevention folder are created for the admin, and can be configured in rules with the **Quarantine** action. The folders are named with the admin's email address, and located in the following SharePoint directories:
  - Data Protection folder: Cato_Qarantine/Cato_Qarantine_DataProtection
  - Threat Prevention folder: Cato_Qarantine/Cato_Qarantine_ThreatPrevention

### Configuring SharePoint Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

Create a Data Protection rule to define the traffic that is scanned by Data Protection API. Create separate rules for each SaaS app connector, and then define the criteria which determines which traffic is scanned.

Scanned files also include Team and OneNote files that are shared with SharePoint.

For more information about the SharePoint rule settings, see below [Understanding the SharePoint Rules](/v1/docs/microsoft-sharepoint-configuring-the-data-protection-api-connector#understanding-the-sharepoint-rules).

![SharePoint_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640004127517.png)

**To create a new Data Protection rule for the SharePoint app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the SharePoint app.
4. In the **General** section, enter the settings for the rule.
5. In **Owner**, select one or more SharePoint file owners (default value is **Any**).

When you select multiple owners, there is an OR relationship between them.
6. In **Sharing Options**, select one or more file permission types (default value is **Any**).

When you select multiple options, there is an OR relationship between them.
7. In **Attachments**, define the criteria to specify the files which are scanned (the default setting is to scan all files).
8. In **Content Profile**, select the DLP Content Profile for this rule.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
9. Select an **Action**.

For the **Quarantine** action, select a **Quarantine folder path**. For more about quarantine folders, see above [Preparing for File Quarantine](/v1/docs/microsoft-sharepoint-configuring-the-data-protection-api-connector#preparing-for-file-quarantine).
10. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
11. Click **Save**. The rule is added to the Data Protection policy.

#### Understanding the SharePoint Rules

This section explains how to define the settings for the Data Protection rules to scan the correct SharePoint traffic. Each rule can be defined according to the following criteria:

- Owner - Individual sites, or Azure types of users that are the owners of the relevant SharePoint directories (default value is Any)
- Sharing Options - Select the types of file sharing permissions that match this rule (default value is Any)

For example, to monitor files that are shared with any external users, select **External Link**.
- Attachments - Criteria for attachments that are scanned (default value is all attachments)
  - File Type
  - File Name
  - File Size (maximum file size is 100 MB)
- Content Profile - DLP Content Profile that defines the DLP content inspection (Security > DLP Profiles > DLP Profiles > Content Profile)
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

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640004188445.png)

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
| Collaborators | Email addresses of the users that received the file |
| Connector Name | Name for the connector that is defined for the rule |
| Connector Type | SaaS app that is defined for this connector |
| DLP Profile | DLP Content Profile that generated this event |
| File Name | Name of the attached file |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Parent Connector Type | Parent Microsoft 365 connector |
| Rule | Name of the rule in the Data Protection policy |
| Owner | File owner |
| Severity | Severity defined for the rule |
| Sharing Scope | Sharing Options for the SharePoint file |
