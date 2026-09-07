---
title: "Microsoft Exchange: Configuring the Data Protection API Connector"
slug: "microsoft-exchange-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/microsoft-exchange-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Exchange: Configuring the Data Protection API Connector

This article explains how to configure the Microsoft 365 and Microsoft Exchange connectors for the App & Data API Protection policy for your account.

The App & Data API Protection policy requires a separate license from Cato. Please contact your Cato representative or official reseller for more information.

> [!NOTE]
> Note:
> 
> Please contact [SaaSecAPI@catonetworks.com](mailto:SaaSecAPI@catonetworks.com) or your official Cato reseller for more information about using the App & Data API Protection policy.

## Overview of Microsoft Exchange Connectors

The first step for the Data Protection API solution is to create the connectors for the Microsoft SaaS apps, Microsoft 365 and Exchange. For accounts with multiple Azure AD tenants, you can create multiple Microsoft 365 connectors. In addition, you can create multiple Exchange connectors for each Microsoft 365 parent connector.

Each Microsoft Exchange app and Azure tenant (according to the 365 app) are subject the Microsoft's rate limiting. For more information, see the [Microsoft documentation](https://docs.microsoft.com/en-us/graph/throttling#pattern).

### Prerequisites

- The Microsoft 365 connector requires an admin with the global admin role to give permissions to the Data Protection API
- The connector monitors files, other actions will be supported soon

### Required Permissions for the API Connectors for Microsoft Exchange

To enable the Data Protection API to scan assets and content for Exchange emails, the connector gives Cato the following permissions and actions with the Exchange app:

- Grant access to the app using Oauth2
- Receive a token from the app to establish and maintain a secure connection
- Connect to the Microsoft APIs and fetch data and scan emails according to the App & Data API Protection policy

## Working with Microsoft Exchange Connectors

To enable the Data Protection API to scan assets and content for Microsoft Exchange, first you need to configure the Microsoft 365 connector as the parent app to give read permissions for the Exchange connector. The parent app only has permissions to manage the Microsoft connectors. You can easily create the app in the Cato Management Application, it's not necessary to configure settings in Microsoft Azure. Afterwards create a separate Microsoft 365 connector for each Azure tenant.

### Step 1: Creating the Microsoft 365 Connector

Use the Cato Management Application to create the Microsoft 365 SaaS application connector for the Azure tenant for the Microsoft Exchange app that your are scanning with the Data Protection API. You must have the correct credentials to authenticate to the Microsoft Exchange app to add it to your Cato account.

Before you can create and configure the connector settings, first you need to enable the Data Protection API for your account.

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

![Create_API_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639989834013.png)

**To create the Microsoft 365 parent connector:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **Microsoft 365** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640004288925.png)
4. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
5. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640018759069.png)

You can close the browser tab and return to the CMA.
6. The Microsoft 365 SaaS application is added to the **Integrated APIs** tab.

### Step 2: Creating the Microsoft Exchange Connector

After the Microsoft 365 connector is connected to your Cato account, you can create the required Exchange connectors. The Exchange connector lets the Cato SaaS API engine scan emails for the content that you define in the Data Protection policy. Events are generated for any email that matches a rule in the policy.

> [!NOTE]
> Note:
> 
> When you create an API connector for a Microsoft 365 app, the connector creates an authentication certificate that is valid for 3 months, and renews the certificate 7 days before expiration.

**To create the connector for Microsoft Exchange:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click **New**. The **New Connector** panel opens.
3. Create a new **Exchange SaaS Application**, for the **Connector Parent** you created in the previous step.

Currently, only **Read** permissions and actions are supported for the Exchange app. However, **Read/Write** permissions and actions will be supported soon.
4. Click **Authorize and Save**.
5. In a new browser tab, authenticate to the Exchange app.
  1. Select the Microsoft account for the Exchange app and log in.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions for Cato to access the Exchange app.
  4. The screen shows that you have successfully applied the permissions for the app.

You can close the browser tab and return to the Cato Management Application.

It can take Microsoft Azure several seconds to process the request, so if you receive an error, refresh the browser.
6. The Exchange SaaS application is added to the **Integrated APIs** tab.

## Adding Exchange Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor and manage the messages and attachments that your users send with Microsoft Exchange.

### Configuring Exchange Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

For more information about the Exchange rule settings, see below [Understanding the Exchange Rules](/v1/docs/microsoft-exchange-configuring-the-data-protection-api-connector#understanding-the-exchange-rules).

![SaaS_API_Data_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640033826461.png)

**To create a new Data Protection rule for the Exchange app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the Exchange app.
4. In the **General** section, enter the settings for the rule.
5. In **Sender**, define the Azure AD users who are sending the mail (the default setting is Any).
6. In **Recipients**, define the Azure AD users who are receiving the mail (the default setting is Any).
7. In **Attachments**, define the criteria to specify the email attachments which are scanned (the default setting is to scan all attachments).
8. In **Content Profile**, select the DLP Content Profile for this rule.

You can enter keywords in **Email Subject**, to limit the scans to only emails that contain those keywords.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
9. In **Actions**, select **Monitor**.
10. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
11. Click **Save**. The rule is added to the Data Protection policy.

#### Understanding the Exchange Rules

This section explains how to define the settings for the Data Protection rules to scan the correct Exchange traffic.

- Sender - individual users, or Azure types of users that are sending the email (default value is Any)
- Recipients - individual users, Azure types of users, or email domains that are receiving the email (default value is Any)
- Attachments - Criteria for attachments that are scanned (default value is all attachments)
  - File Type
  - File Name
  - File Size (maximum file size is 100 MB)
- Content Profile - DLP Content Profile that defines the DLP content inspection (Security > DLP Profiles > DLP Profiles > Content Profile)

#### Working with Senders and Recipients

You can define specific **Senders** and **Recipients** for each rule in the Data Protection policy. The Cato Management Application connects to the Azure AD for the tenant defined in the Office 365 Connector. The individual users that are shown for a rule are based on this Azure AD, and are NOT related to the users defined for your Cato account.

If you don't see the required user, make sure that the user is defined correctly in the Azure AD tenant, and then configure the Data Protection rule.

Azure AD defines these types of users:

- Internal
- External
- User

For the **Recipients** for a rule, you can also define email address domains.

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

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640023589277.png)

## Creating an Exception for a File

Sometimes there is file blocked by Cato's Data Protection API engines that you know is safe, and you need to allow it in the network. Anti-Malware Exceptions in the File Hash policy also apply to the App & Data API Protection. For more information on adding files to the File Hash Policy, see [Managing Anti-Malware Exceptions](/v1/docs/managing-anti-malware-exceptions).

## Analyzing Data Protection API Events

The Home > Events page shows all the Data Protection API events for your account. The powerful search tools let you drill-down and identify the few events that contain the relevant data that you need.

Data Protection API events can be identified by the following fields:

- Event Type - Security
- Sub-Type - SaaS Security API Data Protection and SaaS Security API Anti Malware

You can learn more about using the Events page [here](/v1/docs/analyzing-events-in-your-network).
