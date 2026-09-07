---
title: "Salesforce: Configuring the Data Protection API Connector"
slug: "salesforce-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/salesforce-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce: Configuring the Data Protection API Connector

This article explains how to configure the Salesforce connector for the App & Data API Protection policy for your account and create rules that use this connector in the Threat Protection and Data Protection Policy.

The App & Data API Protection policy requires a separate Cato license. Please contact your Cato representative or official reseller for more information.

## Overview of the Salesforce Connector

The Salesforce Data Protection API connector monitors exported reports and scans for sensitive data that you define in the DLP Content Profiles. The connector uses the Salesforce events log API to periodically check for exported reports. When a report is exported, the connector downloads the report and scans to see if it contains sensitive data. When the connector identifies sensitive data in the report, it generates an event with the details. Once the connector completes the scan, the content of the report is deleted from the Cato server, regardless of the outcome of the scan (no impact to the data in the Salesforce account).

Create the connector for the production or sandbox Salesforce account for your organization. Then define rules in the Threat Protection and Data Protection policies that include the Salesforce connector and define the users that are scanned and monitored. You can create a single connector for each Salesforce account.

### Prerequisites

- Active subscription to Salesforce Shield or Salesforce Event Monitoring component
- Read-only user permissions for the following settings:
  - Event Monitoring Analytics Apps (Permission Set License)
  - View Event Log Files
  - API Enabled
  - View Real-Time Event Monitoring Data
  - View Reports in Public Folders
  - Manage All Private Reports and Dashboards
- Verify that these Salesforce licenses are valid: **Analytics Platform** and **Event Monitoring Analytics Apps** (Setup > Settings > Company Information > Company Settings > Permission Set Licenses)
- Verify that storage is enabled for **Report Event** (Events > Event Manager)

### Required Permissions for the API Connectors for Salesforce

To enable the Data Protection API to scan exported Salesforce reports, the connector gives Cato the following permissions and actions with the Salesforce account:

- Access the identity URL service
- Access Analytics REST API resources
- Manage user data via APIs
- Perform requests at any time

## Working with Salesforce Connectors

This section explains how to create the API connector for Salesforce to scan exported reports for sensitive data and threats. Once you create the connector, update the Refresh Token Policy to ensure the Data Protection API has continued access to Salesforce data.

### Creating the Salesforce Connector

Use the Cato Management Application to create the Salesforce connector, and then sign in to the production or sandbox Salesforce account.

The Salesforce connector lets the Cato SaaS API engine scan reports for the content that you define in the Data Protection policy.

**To create the connector for Salesforce:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **SaaS Application** drop down, choose Salesforce.
4. In the **Capability** section, select **Data and Threat Protection**.
5. Enter the **Connector Name**.
6. In **Salesforce Environment**, select if this connector is monitoring the **Production** or **Sandbox** environment.
7. Click **Save**.

The Salesforce login screen opens in a new browser tab.

![SF_login.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640024908701.png)
8. Enter the Salesforce admin **Username** and **Password** for the specific environment.
9. Give permissions for your Cato account to access the Salesforce app.
  1. **Allow** the permissions for Cato to access the Salesforce app.

![Allow_Cato_SF_Access.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640005841693.png)
  2. The screen shows that you have successfully applied the permissions for the tenant.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639994128669.png)
10. You can close the browser tab and return to the Cato Management Application. It can take Salesforce several seconds to process the request, so if you receive an error, refresh the browser.

While Salesforce is processing the request, the Status for the connector is **Pending user consent** (see below *Understanding the Connector Status*).

The Salesforce SaaS application is added to the **Integrated APIs** tab.

### Updating the Refresh Token Policy

The Salesforce Refresh Token defines the length of time the Data Protection API connector has permission to scan Salesforce data. For maximum security, we recommend you configure the Refresh Token Policy to be **Refresh token is valid until revoked**. This ensures the Data Protection API connector has continued access to Salesforce Data.

For more information on how to configure the Refresh Token Policy, see the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.connected_app_manage_oauth.htm&amp;type=5).

#### Providing Re-Consent to the Data Protection API Connector

> [!NOTE]
> Note:
> 
> The recommended configuration for the Refresh token is **Refresh token is valid until revoked**.

If you configure an expiry time for the Refresh Token, you need to proactively provide re-consent for the Data Protection API connector to access Salesforce data before the token expires. Providing re-consent ensures the Data Protection API connector maintains access to Salesforce data. If the token expires without providing re-consent, the Data Protection API connector does not have access to Salesforce data.

**To provide re-consent to the** **Data Protection API** **connector:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click the three dots next to the Salesforce connector.
3. Click **Reconsent**.

### Understanding the Connector Status

The **Status** column on the Installed SaaS Applications page shows the status of the connection between the Salesforce account and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the account and working correctly
- **Connection error** - Connectivity or permissions issue with the Salesforce connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Pending user consent** - The Salesforce connector is created in the Connect Settings page, however you haven't successfully authenticated to Salesforce.

## Adding Salesforce Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor exported Salesforce reports.

### Configuring Salesforce Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

![Slack_Data_Protection_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639994192797.png)

**To create a new Data Protection rule for the Salesforce app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **SaaS Application** drop down, select the Salesforce app.
4. In **Application Connector**, select the Salesforce app.
5. In the **General** section, enter the settings for the rule.
6. In **Users**, define the Salesforce users you are monitoring.
  - **Any**: Monitor reports exported by all Salesforce users
  - **Salesforce User**: Select the specific users from the Salesforce account that their exported reports are monitored
7. In Content Profile, select the DLP Content Profile for this rule.

For more information about Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
8. In **Actions**, select **Monitor**.
9. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](https://support.catonetworks.com/hc/en-us/sections/13908020158237-Alerts) section.
10. Click **Save**. The rule is added to the Data Protection policy.

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

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640006038429.png)

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
| File Name | Name of the file for the exported report |
| Full Path URL | Link for the exported report |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Rule | Name of the rule in the Data Protection policy |
| Owner | Salesforce user that exported the report |
| Severity | Severity defined for the rule |

## Known Limitations

- Due to Salesforce API access restriction, the Salesforce connector is not able to scan private reports
