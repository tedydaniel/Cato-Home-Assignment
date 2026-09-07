---
title: "GitHub: Configuring the Data Protection API Connector"
slug: "github-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/github-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub: Configuring the Data Protection API Connector

This article explains how to configure the GitHub connector for the App & Data API Protection policy for your account and create rules that use this connector in the Threat Protection and Data Protection Policy.

The App & Data API Protection policy requires a separate Cato license. Please contact your Cato representative or official reseller for more information.

Binary files are not supported for the GitHub connector.

## Overview

The GitHub Data Protection API connector monitors content in commits that users push to repositories, and scans for sensitive data that you define in the DLP Content Profiles. When the connector identifies sensitive data in a commit, it generates an event with the details. For example, you can scan commits for API tokens, SSH keys, database credentials, and more.

To monitor content in commits, create the connector for the GitHub organization, then configure rules in the Threat Protection and Data Protection policies that define the users and repositories that are scanned and monitored.

### Prerequisites

- Administrator permissions for your organization's GitHub account

### Required Permissions for the API Connectors for GitHub

To enable the Data Protection API to scan GitHub commits, the connector gives Cato the following permissions in the GitHub account:

- Read access to code, members, and metadata

## Working with GitHub Connectors

This section explains how to create API connectors for GitHub to scan commits for sensitive data and threats.

### Creating the GitHub Connector

Use the Cato Management Application to create the GitHub connector, and then sign in to your GitHub account. Select the organization to install the connector in, and then select the repositories the connector can access. You can select all repositories for the organization or only specific ones.

You can create a single connector for each GitHub organization. For multiple organizations, a separate connector is required for each one.

The GitHub connector lets the Data Protection API engine scan the content that you define in the Data Protection policy.

> [!NOTE]
> Note:
> 
> - You can't install more than one connector for an organization. Attempting to install a second connector for the same organization may impact functionality, and the organization may no longer be monitored.
> - Changing settings for an existing connector in the GitHub management console can impact functionality, and the organization may no longer be monitored.

**To create the connector for GitHub:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated APIs** tab.
2. Click **New**. The **New Connector** panel opens.
3. In **SaaS Application** drop down, select **GitHub**.
4. In the **Capability** section, select **Data and Threat Protection**.
5. Enter the **Connector Name**.
6. Click **Authorize and Save**. You're redirected to GitHub.
7. Install the app in GitHub:
  1. In GitHub, sign in as an administrator. If you're already signed in to GitHub, verify you're signed in as an administrator.
  2. Select the organization for the connector.

![GitHub_Select_Org.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640006091805.png)
  3. If necessary, sign in to the organization.
  4. Select the repositories the connector has permission to access, and click **Install**. You can select all the repositories in the organization or specific ones.

![GitHub_Select_repos.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640020538013.png)
  5. The screen shows that you have successfully applied the permissions for the tenant.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640035397917.png)
  6. The GitHub connector is created and added to the **Integrated APIs** tab.

### Understanding the Connector Status

The **Status** column on the Installed SaaS Applications page shows the status of the connection between your GitHub account and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the account and working correctly
- **Connection error** - Connectivity or permissions issue with the GitHub connector. Please open a ticket with [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Pending user consent** - The GitHub connector is created in the Connect Settings page, however you haven't successfully authenticated to GitHub. It can take several seconds to process the authentication, so if you receive this status, refresh the browser.

## Adding GitHub Rules to the Data Protection Policy

This section explains how to use the Data Protection policy to monitor GitHub commits for sensitive data. When a user pushes a commit to a repository, the Data Protection engine scans the new content contained in the commit to detect the sensitive data defined in Content Profiles. Content that was previously pushed to the repository isn't scanned, only the new content that is different in the commit.

### Understanding the GitHub Rule Settings

This section explains how to define the settings for the Data Protection rules to scan GitHub commits. Each rule can be defined with the following settings:

- **Users** - Define the GitHub users to monitor. Select **Any** or define one or more specific users.
- **Objects** - Define which GitHub repositories are scanned. Select **Any** or define one or more specific repositories.
  - The repositories available for scanning include the ones the connector has permission to access, as defined when the connector was created. See above [Creating the GitHub Connector](/v1/docs/github-configuring-the-data-protection-api-connector#creating-the-github-connector).
- **File Attributes** - Exclude files from the scan based on **File Name** and **File Type**. Files that meet the defined attributes are not scanned for sensitive content.
- **Content Profile** - DLP Content Profile that defines the DLP content inspection

You can create or edit Content Profiles in Security > DLP Profiles > DLP Profiles > Content Profile
- **Actions** - Select if you want to generate an event or send a notification when the rule is matched

### Configuring GitHub Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

![Slack_Data_Protection_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640035510429.png)

**To create a new Data Protection rule for the GitHub app:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the GitHub app.
4. In the **General** section, enter the settings for the rule.
5. In **Users**, define the GitHub users that you are monitoring:
  - **Any** - Monitor all GitHub users in the organization (default value)
  - **GitHub User** - Select the specific organization users to monitor
6. In **Objects**, define the GitHub repositories that are scanned. Default value is **Any**.
7. In **File Attributes**, define the criteria to specify the files which are scanned (the default setting is to scan all files).
8. In **Content Profile**, select the DLP Content Profile for this rule.

For more about DLP Content Profiles, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
9. In **Actions**, select **Monitor**.
10. **(Optional)** Configure tracking options to generate **Events** and Send Notifications.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
11. Click **Save**. The rule is added to the Data Protection policy.

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

![CAS_Threat_Protection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32640008335133.png)

## Creating an Exception for a File

Sometimes there is file blocked by Cato's Data Protection API engines that you know is safe, and you need to allow it in the network. Anti-Malware Exceptions in the File Hash policy also apply to the App & Data API Protection. For more information on adding files to the File Hash Policy, see [Managing Anti-Malware Exceptions](/v1/docs/managing-anti-malware-exceptions).

## Analyzing Data Protection API Events

The Home > Events page shows all the Data Protection API events for your account. The powerful search tools let you drill-down and identify the few events that contain the relevant data that you need.

Data Protection API events can be identified by the following fields:

- Event Type - Security
- Sub-Type - SaaS Security API Data Protection and SaaS Security API Anti Malware

You can learn more about using the Events page [here](/v1/docs/analyzing-events-in-your-network).

This is a sample SaaS Security API GitHub connector event:

![GitHub_Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32639994726301.png)

### Explaining the Data Protection API Events Fields

| Field Name | Description |
| --- | --- |
| Application Activity | Push |
| Connector Name | Name for the connector that is defined for the rule |
| Connector Type | SaaS app that is defined for this connector |
| DLP Profile | DLP Content Profile that generated this event |
| Full Path URL | Link to the diff comparison for the commit |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Rule | Name of the rule in the Data Protection policy |
| Object Name | Name of the repository the commit was pushed to |
| Object Type | The type of object scanned |
| Owner | Email address of the user that pushed the commit |
| Severity | Severity defined for the rule |
