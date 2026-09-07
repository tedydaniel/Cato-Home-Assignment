---
title: "Creating File Control Rules in the Application Control Policy"
slug: "creating-file-control-rules-in-the-application-control-policy"
updated: 2026-08-27T07:37:00Z
published: 2026-08-27T07:37:00Z
canonical: "knowledge.catonetworks.com/creating-file-control-rules-in-the-application-control-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating File Control Rules in the Application Control Policy

This article discusses how to use the Application Control page to configure the File Control rules for your account.

## Overview

File Control lets you define rules that identify and control the transfer of granularly defined file types within and outside of your organization. This lets you tailor security policies for scenarios such as unauthorized source code transfers or access to Microsoft Office document types. The App & Data Inline Protection page supports three types of rules: CASB App Control, DLP Data Control, and File Control. The File Control rules contain additional settings for defining file types, including the following File Attributes:

- Content Type - Supports hundreds of file types in a variety of categories including: Microsoft Office, executables, source code, and more. You can granularly refine the rule to only match specific file types within each category.
  - A full list of supported file types is available in the Cato Management Application when configuring the Content Type for a rule. For more information about configuring the Content Type, see below [Configuring File Control Rules](/v1/docs/creating-file-control-rules-in-the-application-control-policy#configuring-file-control-rules)
- Content Size - Define the rule to apply to custom defined file sizes.

The Application Control policy is an ordered rulebase that lets you define activities and required criteria for applications and categories. Each rule defines one application or one category. Once a rule matches the traffic, the lower priority rules (below the matching rule) are not applied to the traffic.

The final rule in the rulebase is an implicit ANY ANY allow rule, so if a connection does not match a rule, then it is allowed by the final implicit rule.

### Prerequisites

- File Control rules require that TLS Inspection is enabled to identify the files.
  - Cato's granular [TLS Inspection policy](/v1/docs/configuring-tls-inspection-policy-for-the-account) lets you create rules that will only inspect the traffic that is relevant for a File Control rule.
  - File Control rules are included in the CASB license. For more about purchasing the license, please contact your Cato representative.

## Understanding File Control in the Application Control Rulebase

Create File Control rules in the App & Data Inline Protection page to define the files that are blocked by the security stack in the Cato Cloud. This section describes the fields and settings that are specific to File Control rules. For more information about rules and settings that are also relevant to App Control rules, see [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy).

![Data_Control_Rules_-_Callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24899363087005.png)

| Item | Description |
| --- | --- |
| 1 | Enable or disable the App Control and File Control rules in the policy |
| 2 | Enable or disable the Data Control rules in the policy |
| 3 | Create a new App Control, Data Control, or File Control rule |
| 4 | Icon that shows the type of rule: - ![Data_Control_Icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24899349112989.png) Data Control rule - ![App_Control_Icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24899349181981.png) App Control rule - ![File_control_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24899300305437.png) File Control rule |
| 5 | **Criteria** column shows the **Activities**, **File Attributes**, DLP Content **Profiles** and other criteria that match this rule The DLP Content Profiles are configured in Security > Data Types & Profiles **Note:** Not all activities are supported for all apps. For example, Upload and Download are only supported for specific apps. |

### File Control Rule Settings

A File Control rule has the following sections:

- General - Name and severity that you choose to assign to the rule. Also lets you enable or disable the rule.
- Application - Predefined application, category, custom application, or Sanctioned App that matches this rule. Only supported apps appear in the list of predefined applications.
- Activities - Select if the rule is for upstream and/or downstream traffic.

You must define an activity for each rule.

**Note:** For rules using Activities conditions, you must enable TLS Inspection to inspect the traffic that matches the rule.
- File Attributes - Define the file types and file size for the data that matches this rule, and if there is an AND or OR relationship between the attributes.
  - Content Type - The drop-down menu shows all the supported file Content Types. Select a Content Type and then configure the specific file types to include in the rule. For example, select Microsoft Office Documents and configure only Excel and PowerPoint files.
  - Content Size - Define the size of the file and operator (**Greater than** or **At most**) for the file to match the rule. File size can be defined in KB or MB.
    - For rules configured with Content Size, only the **Monitor** action is supported.
- Access Methods - Requirements for the user agents on hosts and devices that can connect to your account.
- **Source** - Source of the traffic for this rule.
  - You can set the **Source** to a **Country** to create a rule that enforces traffic originating in that country, based on IP geolocation
  - For information about other **Source** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects)
- Time - Define the time period when the rule is active.
- Actions - Apply the specified action to traffic that matches the rule. Also define the tracking options for events and email notifications.

## Configuring File Control Rules

Create a new File Control rule and configure the rule's settings to implement the file transfer policy for your organization.

The **Time** options define the time range that the rule is enabled. You can configure custom options for a rule, or choose the default working hours that are defined for the account.

**To create a new File Control rule:**

1. From the navigation menu, select **Security > App & Data Inline**.
2. Make sure that **App Control** is enabled (green is enabled, grey is disabled).
3. Click **New > File Control Rule**.

The **File Control Rule** panel opens.
4. Expand the **General** section and configure these settings:
  1. Enter a **Name** for the rule.
  2. Enable or disable the rule using the slider (green is enabled, grey is disabled).
  3. Select the **Severity**.

The Severity is used in the events and monitoring analytics for this rule.
5. In the **Application** section, select **Any Cloud Application**, or you can choose to limit the content inspection to a specific application or category.
6. Expand the **Activities** section, and configure these settings:
  1. Click **Add Activity** and select the item for the rule.
  2. When there are multiple items in the **Activities** section, in the **Satisfy** drop-down menu, define the relationship between the items:
    - **any (OR)** - If any of the items match the traffic, then the rule is applied
    - **all (AND)** - If all of the items match the traffic, then the rule is applied
7. In the **File Attributes** section, select the specific file types and file size to match the rule.
  1. Click **Add File Attribute** and select **Content Type** or **Content Size**.
  2. Define the settings for the File Attribute item.
  3. For multiple items, define the relationship between the items (see above 6b).
8. Expand the **Access Methods** section, and define the user agent requirements.

If there are multiple items, there is an AND relationship between them.
9. Expand the **Source** section and select one or more objects for the traffic source for this rule (or you can enter an IP address).

Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
10. **(Optional)** Expand the **Time** section, and define when the rule is active.

Select **No time constraint** to set the rule as always active.
11. Expand the **Actions** section, and configure these settings:
  1. Select the **Action** for this rule.
  2. **(Optional)** Configure tracking options to generate **Events** and **Send Notification**.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and [Alert](https://support.catonetworks.com/hc/en-us/sections/13908020158237-Alerts) Integrations in the Alerts section.
12. Click **Apply**.

## Analyzing File Control Events

The Events screen shows all the File Control events for your account. These Security events are the Sub Type, **Apps Security**.

You can learn more about using the Events screen [here](/v1/docs/analyzing-events-in-your-network).

These are the fields that are related to File Control:

| Field Name | Description |
| --- | --- |
| File Name | Name of the file that was scanned by the File Control engine |
| File Size | Size of the file (in bytes) that was scanned by the File Control engine |
| File Type | File content type (such as Archive or Microsoft Office) **Note:** form_data is a generic representation of data submitted through a web form, commonly used in HTTP requests (e.g., multipart form submissions). It doesn't indicate a distinct file type. |
