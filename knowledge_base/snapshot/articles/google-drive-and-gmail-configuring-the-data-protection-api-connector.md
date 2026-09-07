---
title: "Google Drive and Gmail: Configuring the Data Protection API Connector"
slug: "google-drive-and-gmail-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/google-drive-and-gmail-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Drive and Gmail: Configuring the Data Protection API Connector

This article explains how to configure the Google Drive and Gmail connectors for the App & Data API Protection policy for your account and create rules that use this connector in the Data Protection Policy.

> [!NOTE]
> Note:
> 
> Please contact [SaaSecAPI@catonetworks.com](mailto:SaaSecAPI@catonetworks.com) or your official Cato reseller for more information about using the App & Data API Protection policy.

## Overview of the Google Drive and Gmail Connectors

Create the connector for the Google tenant for your organization. The connector requires that you configure the Google Cloud and Google Admin consoles to allow and enable the API calls for your Cato account. Then define rules in the Data Protection policy that include the connector and define that files or emails that are scanned and inspected.

### Prerequisites

- Admin permissions for the Google Cloud and Google Admin accounts
- Google Drive connector requires the business license for the Google Admin console
- Gmail connector requires the Gmail enterprise license
- Google Drive and Gmail accounts are enabled
- The connector monitors files, other actions will be supported soon

## Creating the Initial Google Connector

This section explains how to create the initial API connector for Google Drive and Gmail, and to connect your organization's Google tenant to your Cato account.

The Google Drive and Gmail connectors let the Cato SaaS API engine scan files (attachments), folders, and emails for the content that you define in the Data Protection policy. Events are generated for content that matches a rule in the policy.

> [!NOTE]
> Note:
> 
> The first time that you create a Google connector, it's necessary to enable Cato to use APIs to connect to your Google account. If you already created a Google connector, and now you creating an additional one, continue with [Creating Additional Google Connectors](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#creating-additional-google-connectors).

### Overview of Initially Configuring the Cato Google Drive and Gmail Connectors

This is a high-level overview of the process to create the Cato connector for Google Drive and Gmail:

1. In the Cato Management Application, create a new SaaS Application connector for Google Drive or Gmail.
  1. Copy the oAuth scopes for the connector.
2. In the Google Cloud console for your company's account:
  1. Create a new project for the Cato connector.
  2. Enable the required Google APIs and generate the Service account ID.
3. In the Google Admin console, define the Domain-wide Delegation for the Cato connector.
  1. Paste the oAuth scopes from the connector in the Google Admin console.
4. In the Google Cloud console, create the API keys for the Cato connector.
5. In the Cato Management Application, upload the API keys to the SaaS Application connector for Google Drive or Gmail.

### Step 1 - Creating the Google Drive or Gmail SaaS Application

In the Cato Management Application, create the Google Drive or Gmail SaaS application for the connector to your Google account.

![Google_Drive_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640019551261.png)

**To create the connector for Google Drive or Gmail:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the SaaS Application drop down, select **Google Drive** or **Gmail**.
4. In the **Capability** section, select **Data and Threat Protection**.
5. Enter the **Connector Name**.
6. Enter the **Admin Email** for the Google admin account with admin privileges.
7. Click **Copy oAuth Scopes**.

To review the full list of oAuth scopes, see below [oAuth Scopes for Google Drive and Gmail Connectors](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#oauth-scopes-for-google-drive-and-gmail-connectors)
8. Continue below with *Step 2 - Configuring the Project in Google Cloud Console*.

### Step 2 - Configuring the Project in Google Cloud Console

From the console for your Google Cloud Platform, create a new project and enable the Admin SDK API and Cloud Identity for your account. Then create a new Service account, and copy the unique ID (you will need this ID for step 3).

**To configure the project in the Google Cloud console:**

1. Log in to the [Google Cloud console](https://console.cloud.google.com) and select the existing or project or create a **New Project**.
2. Enable the Google APIs for the connector:
  1. Select the project and from the navigation pane, select **API & Services > Library**.
  2. In the **API Library**, search for **Admin SDK API**.

![Google_Admin_SDK_API.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639993449885.png)
  3. Click the **Admin SDK API**, and in the new window click **Enable**.
  4. Go back to the API Library, and click **Google Drive API**.
  5. In the next window, click **Enable**.
3. Create the Service account for the Cato connector:
  1. From the navigation pane, select **API & Services > Credentials**.
  2. From the menu bar, click **Create Credentials > Service Account**.

![Google_Create_Service_Account.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005231517.png)
  3. Enter the **Service account name**.
  4. Click **Create and Continue** and then click **Done**.
4. In the **Service Accounts** window, edit the new account.
5. Copy and save the **Unique ID** for the Service account. You will enter this ID in the Google Admin console (below).
6. Continue below with *Step 3 - Defining the Domain-Wide Delegation in Google Admin Console*.

### Step 3 - Defining the Domain-Wide Delegation in Google Admin Console

Google uses domain-wide delegations to allow apps to access data across the Google Workspace environment. Define a domain-wide delegation with permissions to access the APIs that you enabled in the previous section.

In the Google Admin console, create a new API client and configure it to use the Unique ID for the service account (that you saved from *Step 2 - Configuring the Project in Google Cloud Console* above).

**To define the domain-wide delegation in the Google Admin console:**

1. Log in to the [Google Admin console](https://admin.google.com) for your account.
2. From the navigation pane, select **Security > Access and data control > API controls**.
3. In the **API Controls** window, in the **Domain** wide delegation section at the bottom of the screen, click **Manage Domain Wide Delegation**.
4. In the **API client** section, click **Add new**.

The **Add a new client ID** pop-up window opens.

![Google_Add_Client_ID.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640019727005.png)
5. In **Client ID**, paste the Unique ID that you copied in the previous section.
6. Paste the **OAuth scopes** that the connector is allowed to access.
  - See [Step 1 - Creating the Google Drive or Gmail SaaS Application](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#step-1-creating-the-google-drive-or-gmail-saas-application) above for more information about copying the Oauth scopes in the Cato Management Application.
7. Click **Authorize**.

The domain-wide delegation for the Cato connector is defined to use the Unique ID for the Google APIs.
8. Continue below with *Step 4 - Creating the API Keys File in the Google Cloud Console*.

### Step 4 - Creating the API Keys File in the Google Cloud Console

After you enable Google's domain-wide delegation for the service account for the Cato connector, use the Google Cloud console to create an API key file for the service account.

**To create the API keys file:**

1. In the Google Cloud console, from the navigation pane, select **IAM & Admin > Service Accounts**.
2. Select the service account for the Cato connector, and select **Actions > Manage keys**.

![Google_Manage_Keys.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005336605.png)

The **Keys** tab for the service account opens.
3. Click **Add Key > Create New Key**.
4. In the pop-up window, and select **JSON** and click **OK**.

The browser saves the API key file to the specified folder.
5. Continue below with *Step 5 - Uploading the API Key File to the Cato Management Application*.

### Step 5 - Uploading the API Keys File to the Cato Management Application

Upload the API key file that you created in the previous section to the Google Drive or Gmail connector in the Cato Management Application. Then the connector is configured and ready to start scanning files and folders for your account.

For the Gmail connector, it's necessary to add a rule to the **Third-party email archiving** setting in the Google Admin console.

> [!NOTE]
> Note:
> 
> The API key file contains sensitive data, we recommend that you delete the file after uploading it to the Cato Management Application.

**To upload the API key file to the Cato Management Application:**

1. Open the browser tab for the Cato Management Application where you started configuring the Google Drive or Gmail connector (above [Step 1 - Creating the Google Drive or Gmail SaaS Application](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#step-1-creating-the-google-drive-or-gmail-saas-application)).
2. In the **Upload Key File** section, upload the API key file that you created (above *Step 4 - Creating the API Keys File in the Google Cloud Console*).
3. Click **Save**.
4. The Google Drive or Gmail SaaS application is added to the **Integrated APIs** tab.
5. For the Gmail application, perform these additional steps:
  1. In the completion screen, copy the email address.
  2. Open the Google Admin console.
  3. Go to **Apps > Google Workspace > Gmail > Routing > Third-party email archiving**.
  4. Click **Add Another Rule**.
  5. In the **Add setting** pop-up window, paste the email address from step a (above).
  6. Click **Save**.

#### Understanding the Connector Status

The **Status** column on the Connectors Settings screen shows the status of the connection between the Google Drive connector and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Connection error** - Connectivity or permissions issue with the Google Drive connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).

## Creating Additional Google Connectors

When you are creating an additional Google connector for your account, then your Google account is already configured to use APIs connect to your Cato account. The connectors use the same oAuth scope.

Enable the Google API for the new Google Drive or Gmail API. Then create and download the key file from your Google account and upload it to the connector.

**To create an additional Google connector:**

1. Log in to the [Google Cloud console](https://console.cloud.google.com) for your account.
2. Enable the Google APIs for the connector:
  1. Select the project and from the navigation pane, select **API & Services > Library**.
  2. In the API Library, and search for the new **Google Drive API** or **Gmail API**.
  3. In the next window, click **Enable**.
3. Create and download the key file for your Google account:
  1. In the Google Cloud console, from the navigation pane, select **IAM & Admin > Service Accounts**.
  2. Select the service account for the Cato connector, and select **Actions > Manage keys**.
  3. Click **Add Key > Create New Key**.
  4. In the pop-up window, and select **JSON** and click **OK**.

The browser saves the API key file to the specified folder.
4. Create the new Google connector:
  1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
  2. Click **New**. The **New Connector** panel opens.
  3. Define the settings for the Google Drive or Gmail connector and enter the Google **Admin Email**.
  4. In the **Upload Key File** section, upload the API key file that you created above.
  5. Click **Save**.
5. For the Gmail application, perform these additional steps:
  1. In the completion screen, copy the email address.
  2. Open the Google Admin console.
  3. Go to **Apps > Google Workspace > Gmail > Routing > Third-party email archiving**.
  4. Click **Add Another Rule**.
  5. In the **Add setting** pop-up window, paste the email address from step a (above).
  6. Click **Save**.

## Adding Google Drive or Gmail Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor and manage the files, folders, and emails that are stored in your Google account.

### Understanding Google Drive and Gmail Actions

When you create a Data Protection rule, you can define different actions to monitor or remediate the policy violations when the rule is matched. Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

These are the actions you can set for the Data Protection engine to perform when a rule is matched:

(The **Remove Share** and **Quarantine** actions are available only for Google Drive, rules for Gmail can only be defined with the **Monitor** action.)

- **Monitor** - Generates an event to let you monitor traffic that matches the rule.
- **Remove Share** - When a user tries to share a file, the Data Protection API engine removes the unauthorized sharing permission, and the user who receives a link to the shared file won't have permissions to access the file.
- **Quarantine** - When a user tries to upload a file, the engine moves it to a quarantine folder and then users can no longer access it. The Google admin can access the file in the quarantine folder. For information about configuring quarantine folders, see [Preparing for File Quarantine](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#preparing-for-file-quarantine).

> [!NOTE]
> Note:
> 
> The following known limitations apply for Google Drive actions:
> 
> - The **Remove Share** action can't be applied to a file within a shared folder, share permissions can be removed only for files not located within a shared folder.
> - When the **Remove Share** action is applied, Google Drive lets the user request access to the file from the user who shared the file, and they can grant access for approximately ten minutes.
> - The **Quarantine** action can take up to 10 minutes to be applied to a file.

### Preparing for File Quarantine

Configure quarantine folders for Data Protection and Threat Prevention rules, and define the Google admin with permissions to access the folders. You can configure quarantine folders for each Google admin for the tenant. When you configure the folders, you can then create rules with the **Quarantine** action, and define the folder that the file is moved to.

![SaaS_Security_API_Settings_GoogleDrive2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639993682973.png)

**To configure quarantine folders for a Google admin:**

1. From the navigation pane, select **Security > App & Data API Protection** and select the **Settings** tab.
2. Click **New**. The **Quarantine Folder** panel opens.

![SaaS_Security_API_Settings_Onedrive_Quarantine_Folder.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005454237.png)
3. Select the **Google Drive** application connector.
4. Select the Google admin to have access to these quarantine folders.
5. Click **Save**.

A Data Protection folder and a Threat Prevention folder are created for the admin, and can be configured in rules with the **Quarantine** action. The folders are named with the admin's email address, and located in the following Google Drive directories:
  - Data Protection folder: Cato_Qarantine/Cato_Qarantine_DataProtection
  - Threat Prevention folder: Cato_Qarantine/Cato_Qarantine_ThreatPrevention

### Configuring Google Drive and Gmail Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

Create a Data Protection rule to define the traffic that is scanned by Data Protection API. Create separate rules for each SaaS app connector, and then define the criteria which determines which traffic is scanned.

For more information about the Google Drive and Gmail rule settings, see below [Understanding the Google Connector Rules](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#understanding-the-google-connector-rules).

**To create a new Data Protection rule for the Google Drive or Gmail app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the Google Drive or Gmail app.
4. In the **General** section, enter the settings for the rule.
5. In **Owner** (for Google Drive) or **Sender** (for Gmail), select one or more Google users that you are monitoring (default value is **Any**).

When you select multiple users, there is an OR relationship between them.
6. (For Gmail) In **Recipients**, define the Google users who are receiving the mail (the default setting is **Any**).
7. In **Sharing Options**, select permission level for files and folders that are scanned (default value is **Any**).

When you select multiple options, there is an OR relationship between them.
8. In **File Attributes** (for Google Drive) or **Attachments** (for Gmail), define the criteria to specify the files which are scanned (the default setting is to scan all files).
9. In **Content Profile**, select the DLP Content Profile for this rule.
10. Select an **Action**.

For the **Quarantine** action (for Google Drive), select a **Quarantine folder path**. For more about quarantine folders, see above ???.
11. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
12. Click **Save**. The rule is added to the Data Protection policy.

### Understanding the Google Connector Rules

This section explains how to define the settings for the Data Protection rules to scan the correct Google Drive or Gmail traffic. Each rule can be defined according to the following criteria:

- Owner or Sender - Google users in your workspace (default value is Any)
  - Internal - Owner is any user in your company
  - Google User - Owner is a specific user
- Recipients (for Gmail) - Users that receive the email
  - Internal - Owner is any user in your company
  - External - Defined in your Google account as outside of your company
  - Google User - Owner is a specific user
  - Domain - Enter the domain for the email recipients
- Sharing Options - Select the types of file and folder sharing permissions that match this rule (default value is Any)
  - Private - Only user has access
  - Restricted - TBD
  - Organizational Unit - Any user in the unit defined in your Google Drive user hierarchy
  - External - External users that received an invitation with the link
  - Open - Publicly accessible to anyone with the link
- File Attributes or Attachments - Criteria for attachments that are scanned (default value is all attachments)
  - File Type
  - File Name
  - File Size (maximum file size is 100 MB)
- Content Profile - DLP Content Profile that defines the DLP content inspection

You can create or edit Content Profiles in Security > DLP Profiles > DLP Profiles > Content Profile
- Actions - Select if you want to **Monitor** the rule by generating an event or email notification when the rule is matched. For Google Drive, you can also choose to **Remove Share** permissions, or **Quarantine** files that match the rule. For about Google Drive actions, see [Understanding Google Drive and Gmail Actions](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#understanding-google-drive-and-gmail-actions).

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
- **Quarantine** - When a user tries to upload a file, the engine moves it to a quarantine folder and then users can no longer access it. The Google admin can access the file in the quarantine folder. For information about configuring quarantine folders, see [Preparing for File Quarantine](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#preparing-for-file-quarantine).

> [!NOTE]
> Note:
> 
> The following known limitations apply for Google Drive actions:
> 
> - The **Remove Share** action can't be applied to a file within a shared folder, share permissions can be removed only for files not located within a shared folder.
> - When the **Remove Share** action is applied, Google Drive lets the user request access to the file from the user who shared the file, and they can grant access for approximately ten minutes.
> - The **Quarantine** action can take up to 10 minutes to be applied to a file.

Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see below [Analyzing Data Protection API Events](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

When you create a App & Data API Protection rule, the Anti-Malware engines that are enabled for your account (Security > Anti-Malware) perform malware scans on the files that are sent for that connector application.

The following screenshot shows a Threat Protection rule for the OneDrive connector that scans files sent by Internal users or Guests:

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005503133.png)

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
| Owner | File owner |
| Severity | Severity defined for the rule |
| Sharing Scope | Sharing Options for the Google Drive attachment |

## oAuth Scopes for Google Drive and Gmail Connectors

These are the required oAuth scopes for the different Google connector types:

- Google Drive Read -
  - https://www.googleapis.com/auth/admin.directory.user.readonly
  - https://www.googleapis.com/auth/admin.directory.domain.readonly
  - https://www.googleapis.com/auth/admin.directory.customer.readonly
  - https://www.googleapis.com/auth/admin.reports.audit.readonly
  - https://www.googleapis.com/auth/drive.readonly
  - https://www.googleapis.com/auth/admin.reports.usage.readonly
- Google Drive Write -
  - https://www.googleapis.com/auth/admin.directory.user.readonly
  - https://www.googleapis.com/auth/admin.directory.domain.readonly
  - https://www.googleapis.com/auth/admin.directory.customer.readonly
  - https://www.googleapis.com/auth/admin.reports.audit.readonly
  - https://www.googleapis.com/auth/drive.readonly
  - https://www.googleapis.com/auth/admin.reports.usage.readonly
  - https://www.googleapis.com/auth/drive
  - https://www.googleapis.com/auth/drive.file
- Gmail -
  - https://www.googleapis.com/auth/admin.directory.user.readonly
  - https://www.googleapis.com/auth/admin.directory.domain.readonly
  - https://www.googleapis.com/auth/admin.directory.customer.readonly
  - https://www.googleapis.com/auth/admin.reports.audit.readonly
  - https://www.googleapis.com/auth/drive.readonly
  - https://www.googleapis.com/auth/admin.reports.usage.readonly
