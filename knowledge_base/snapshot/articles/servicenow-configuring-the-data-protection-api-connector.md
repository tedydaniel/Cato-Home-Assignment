---
title: "ServiceNow: Configuring the Data Protection API Connector"
slug: "servicenow-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/servicenow-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ServiceNow: Configuring the Data Protection API Connector

This article explains how to configure the ServiceNow connector for the App & Data API Protection policy for your account and create rules that use this connector in the Threat Protection and Data Protection Policy.

The App & Data API Protection policy requires a separate Cato license. Please contact your Cato representative or official reseller for more information.

## Overview of the ServiceNow Connector

Create the connector for the ServiceNow instance for your organization. Then define rules in the App & Data API Protection policies that include the ServiceNow connector and define the objects that are scanned and inspected. You can create a single ServiceNow connector for each instance.

### Prerequisites

- The ServiceNow connector requires an admin with the global admin role to give permissions to the Data Protection API
- The Application scope is set to global

### Required Permissions for the API Connectors for ServiceNow

To enable the Data Protection API to scan table records and attachments in your ServiceNow account, the connector gives Cato the following permissions and actions with the ServiceNow app:

- Grant access to the app using OAuth2
- Receive a token from the app to establish and maintain a secure connection
- Connect to the ServiceNow APIs and scan data and tables according to the App & Data API Protection policy

## Working with ServiceNow Connectors

This section explains how to set the correct ServiceNow permissions, create API connectors for ServiceNow, and to connect your organization's ServiceNow instance to your Cato account.

> [!NOTE]
> Note:
> 
> Make sure that you don't have ACL, IP ACL, business rules, or data policies that impact the ability of Cato to connect to your ServiceNow instance.

### Required ServiceNow Tables and Roles

When the ServiceNow admin creates the Cato connector, the admin account needs to have the correct permissions for the tables and roles. The table below lists the ServiceNow tables that Cato requires permissions to access.

The minimum required permission is the **ITIL** role, but we recommend that you define the tables with the **admin** role.

| change_phase | sn_hr_core_beneficiary | sn_hr_core_op_report_type |
| --- | --- | --- |
| change_request | sn_hr_core_benefit | sn_hr_core_op_system |
| change_request_imac | sn_hr_core_benefit_provider | sn_hr_core_op_system_to_report_type |
| change_task | sn_hr_core_benefit_type | sn_hr_core_profile_bank_account |
| cmdb | sn_hr_core_bonus | sn_hr_core_retirement_benefit |
| incident | sn_hr_core_case | sn_hr_core_task |
| incident_task | sn_hr_core_case_operations | sn_hr_core_tuition_reimbursement |
| kb_knowledge | sn_hr_core_case_payroll | sn_si_incident |
| kb_submission | sn_hr_core_case_relations | sn_si_request |
| problem | sn_hr_core_case_talent_management | sn_si_task |
| problem_task | sn_hr_core_case_total_rewards | sys_attachment |
| release_phase | sn_hr_core_case_workforce_admin | sysapproval_group |
| release_task | sn_hr_core_direct_deposit | sysevent |
| sc_req_item | sn_hr_core_op_report | task |
| sc_request | sn_hr_core_op_report_frequency | ticket |
| sc_task |  |  |

### Setting Permissions for ServiceNow Tables

Set the table permissions in your ServiceNow instance to allow the Cato connector to monitor tables and data.

**To set the ServiceNow table permissions:**

1. Log in to the ServiceNow console, and from the navigation menu search for **System Definition** and select **Tables**.
2. Search for the **Name** of one of the tables, and click the table in the search result.

This is an example of searching for the **problem** table.

![ServNow_Table_Search.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640006585245.png)
3. In the table settings, click the **Application Access** tab and make sure that **Allow access to this table via web services** is selected.

![Allow_access.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640025725469.png)
4. Click **Update**.
5. Repeat steps 2-4 for all the tables listed above in [Required ServiceNow Tables and Roles](/v1/docs/servicenow-configuring-the-data-protection-api-connector#required-servicenow-tables-and-roles).

### Creating the ServiceNow Connector

When you create the ServiceNow connector, copy the base URL for your ServiceNow instance, and paste it in the new Cato connector.

> [!NOTE]
> Note:
> 
> The base URL is the protocol, instance ID, and domain name, without the path. For example, `https://sample.service-now.com` is the base URL for `https://sample.service-now.com/now/nav.ui.classic.params`

Then in the ServiceNow console, create a new OAuth application, and paste the **Cato Redirect URL**. You can also add the Cato logo to the application.

The **Refresh Token Lifespan** defines the length of time the Data Protection APIconnector has permission to scan ServiceNow data. For maximum security, we recommend you update this value from the default 8,640,000 seconds (100 days), to 31,536,000 seconds (1 year). This ensures the Data Protection API connector has continued access to ServiceNow data. Within 14 days of the expiration of the **Refresh Token Lifespan** a warning is displayed in the Cato Management Application, on the **Resources > Integrations** page. To ensure the Data Protection API connector has continued access to the ServiceNow data, provide [re-consent](/v1/docs/servicenow-configuring-the-data-protection-api-connector#providing-reconsent-to-the-data-protection-api-connector).

After the new OAuth application is created, copy the ServiceNow **Client ID** and **Client Secret** and paste these values in the connector. Finally, save the ServiceNow connector in the Cato Management Application and Cato is now ready to monitor ServiceNow objects and tables.

> [!NOTE]
> Note:
> 
> The Cato connector creates several ServiceNow Business Rules that are used to monitor the tables. Don't delete any Business Rule with the prefix **cato**. For more information, see [ServiceNow documentation](https://www.servicenow.com/docs/bundle/vancouver-api-reference/page/script/business-rules/concept/c_BusinessRules.html).

**To create the connector for ServiceNow:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **SaaS Application** drop down select **ServiceNow**.
4. In the **Capability** section, select **Data and Threat Protection**.
5. Configure these connector settings:
  1. Enter the **Connector Name**.

![02_baseURL.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640021070109.png)
  2. From the ServiceNow console, copy the base URL, and paste it in **ServiceNow base URL**.
6. For step 3, configure the new ServiceNow OAuth application:

![step3_oauth.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640021117341.png)
  1. Log in to the ServiceNow console.
  2. Navigate to **System OAuth > Application Registry**, and click **New**.

![01_SN_oauth_app.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640025863069.png)
  3. Click **Create an OAuth API endpoint for external clients**.

The new Oauth application opens.

![New_oauth_app.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639995118237.png)
  4. Enter the **Name** for the application.
  5. Make sure that the **Public Client** option is cleared.
  6. In the Cato Management Application **New Connector** panel, click ![copy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640025951901.png) to copy the Cato redirect URL.
  7. In the ServiceNow application, in **Redirect URL**, paste the URL.
  8. **(Optional)** In **Logo URL**, enter `https://www.catonetworks.com/wp-content/uploads/2022/03/cato-logo.svg` to show the Cato logo for the application.

**Note:** It is not necessary to configure the settings for any of the other fields in the new ServiceNow application.

![ServiceNow_URLs.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640026015645.png)
  9. **(Recommended)** Update the **Refresh Token Lifespan** to 31,536,000 seconds.
  10. Click **Submit**. The ServiceNow OAuth application is created.
7. For step 4, in the Service Now console, click the new OAuth application to open it.
  1. Copy and paste the following OAuth application fields to the Cato connector in the Cato Management Application:
    - **Client ID**
    - **Client Secret**
8. In the Cato Management Application, click **Save**.

A ServiceNow permissions screen opens in a new browser tab.
9. Give permissions for your Cato account to access the ServiceNow app.
  1. Click **Allow** to allow Cato to access the ServiceNow app.
  2. The screen shows that you have successfully applied the permissions for the instance.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639995292189.png)

You can close the browser tab and return to the Cato Management Application. It can take ServiceNow several seconds to process the request, so if you receive an error, refresh the browser.

While ServiceNow is processing the request, the Status for the connector is **Pending user consent** (see below [Understanding the Connector Status](/v1/docs/servicenow-configuring-the-data-protection-api-connector#understanding-the-connector-status)).
10. The ServiceNow SaaS application is added to the **Integrated APIs** tab.

#### Providing Re-Consent to the Data Protection API Connector

You need to proactively provide re-consent for the Data Protection API connector to access ServiceNow data before the token expires. If the token expires without providing re-consent, the Data Protection API connector does not have access to ServiceNow data until you provide re-consent in the Cato Management Application.

**To provide re-consent to the** **Data Protection API** **connector:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click the three dots next to the ServiceNow connector.
3. Click **Reconsent**.

### Understanding the Connector Status

The **Status** column on the **Installed SaaS Applications** page shows the status of the connection between the ServiceNow app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Connection warning** - There is a temporary issue related to polling data from the ServiceNow instance. This could be because the Refresh Token is expiring in 14 days or less. To resolve this issue, provide re-consent for the Data Protection API connector to access ServiceNow data. If this does not solve the issue, please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Connection error** - Connectivity or permissions issue with the ServiceNow connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Pending user consent** - The ServiceNow connector is created in the Connect Settings screen, however, you haven't completed the process to authorize Cato to connect to your ServiceNow account.

## Adding ServiceNow Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor cases managed by ServiceNow.

### Configuring ServiceNow Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

Create a Data Protection rule to define the traffic that is scanned by Data Protection API. Create separate rules for each SaaS app connector, and then define the criteria which determines which traffic is scanned.

You can choose to monitor the content of fields and/or attachments in the ServiceNow instance.

For more information about the ServiceNow rule settings, see below [Understanding the ServiceNow Rules](/v1/docs/servicenow-configuring-the-data-protection-api-connector#understanding-the-servicenow-rules).

![Slack_Data_Protection_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639995362845.png)

**To create a new Data Protection rule for the ServiceNow app connector:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In the **Application Connector** section, select the ServiceNow app connector.
4. In the **General** section, enter the settings for the rule.
5. In the **Objects** section, define the ServiceNow tables that are monitored (default value is **Any**).

When you select multiple objects, there is an OR relationship between them.
6. In **Content Profile**, select the DLP Content Profile for this rule.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
7. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](https://support.catonetworks.com/hc/en-us/sections/13908020158237-Alerts) section.
8. Click **Save**. The rule is added to the Data Protection policy.

#### Understanding the ServiceNow Rules

This section explains how to define the settings for the Data Protection rules to scan the ServiceNow attachments or tables. Each rule can be defined according to the following criteria:

- **Objects** - Select one or more of the following ServiceNow tables that the rule monitors
  - SC task
  - Change phase
  - Change request
  - Change task
  - Release tasks
  - Sysapproval group
  - Change request imac
  - Incident
  - Incident task
  - KB submission
  - KB knowledge
  - Problem
  - Problem task
  - Release phase
  - SC request
  - SC REQ item
  - Task
  - Ticket
- **Content Profile** - DLP Content Profile that defines the DLP content inspection

You can create or edit Content Profiles in Security > DLP Profiles > DLP Profiles > Content Profile
- **Actions** - Select if you want to generate an event or send a notification when the rule is matched

#### Working with Ordered Data Protection Rules

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

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639995451549.png)

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
| Full Path URL | Full URL of the file, table record, or attachment that generated this event |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Object Name | Data for the ServiceNow object that generated the event: - For tables, in the format <table name>/<item number> - For attachments, shows the name of the relevant table record |
| Object Type | Table record |
| Owner | Owner username |
| Rule | Name of the rule in the Data Protection policy |
| Severity | Severity defined for the rule |

## Known Limitations - Supported ServiceNow Tables

This section lists which ServiceNow tables are currently supported for the connector. Unsupported tables aren't monitored for sensitive data.

- Comments and work notes aren't supported
