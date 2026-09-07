---
title: "Creating the Data Control Policy"
slug: "creating-the-data-control-policy"
updated: 2026-08-26T09:40:14Z
published: 2026-08-26T09:40:14Z
canonical: "knowledge.catonetworks.com/creating-the-data-control-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating the Data Control Policy

This article discusses how to use the Application Control page to configure the Data Loss Prevention (DLP) Data Control policy for your account.

## Overview of the Data Control Policy

The Data Control policy lets you define rules to inspect how data and content is transferred and moved within and outside of your organization. The Application Control page supports three types of rules: CASB App Control, File Type Control, and DLP Data Control. The Data Control rules contain additional settings for content inspection, including:

- File Attributes - Supports over 40 different file types in a variety of categories including: Microsoft Office, executables, and source code. In addition, you can refine the rule to only match a specific range of file sizes, or configure the rule to match encrypted files.
- [DLP Content Profiles](/v1/docs/creating-dlp-content-profiles) - These profiles can define content inspection based on over 350 data types in over 30 countries and languages, including: PII, financial, and medical data

The Application Control policy is an ordered rulebase that lets you define activities and required criteria for applications and categories. Each rule defines one application or one category. Once a rule matches the traffic, the lower priority rules (below the matching rule) are not applied to the traffic.

The final rule in the rulebase is an implicit ANY ANY allow rule, so if a connection does not match a rule, then it is allowed by the final implicit rule.

### DLP Protection for Encrypted Files

The DLP engine has the ability to identify and block files encrypted with a password. This can help secure your information by preventing users from uploading or downloading sensitive data hidden in password-protected files. The DLP engine doesn't scan the contents of the encrypted file, but identifies it as encrypted and applies the relevant rule action. Since the engine doesn't scan the file content, the rule action is applied to all encrypted files regardless of any content profiles configured in the rule. You can define rules to allow or block encrypted files, according to the needs of your organization.

The encrypted files detected by the DLP engine include password-protected files of the following types: Word, Excel, PowerPoint, ZIP, and PDF

### Policy Revisions and Concurrent Editing by Multiple Admins

The Data Control Policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Prerequisites

- Data Control rules require that TLS Inspection is enabled to inspect the content.
  - Cato's granular [TLS Inspection policy](/v1/docs/configuring-tls-inspection-policy-for-the-account) lets you create rules that will only inspect the traffic that is relevant for a Data Control rule.
- The Application Control policy is included in the CASB license. Enabling Data Control rules in the Application Control policy also requires the DLP license.

For more about purchasing the above licenses, please contact your Cato representative.

### Known Limitations

- For information on the file requirements, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service)
- The DLP engine bypasses a file if inspection takes longer than 10 seconds.
- When using Microsoft Copilot, DLP only supports file uploads, and not prompts
- These apps aren't supported for content inspection with Data Control rules:
  - Bitbucket
  - GitHub
  - WhatsApp
- When the file attribute is set to **Content Size**, the **Block** action is not supported. Only non-blocking actions (such as **Allow/Notify**) can be used with this attribute. Attempting to configure a Block action with Content Size will result in an error in the Cato Management Application. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(88).png)

## Understanding DLP in the App & Data Inline Protection Rulebase

Use Data Control rules in the Application Control page to implement your company's DLP policy and define the content that is blocked by the security stack in the Cato Cloud. This section describes the fields and settings that are specific to Data Control rules. For more information about rules and settings that are also relevant to App Control rules, see [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy).

![Data_Control_Rules_-_Callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982705697821.png)

| Item | Description |
| --- | --- |
| 1 | Enable or disable the App Control rules in the policy |
| 2 | Enable or disable the Data Control rules in the policy |
| 3 | Create a new App Control or Data Control rule |
| 4 | Icon that shows the type of rule: - ![Data_Control_Icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982681939485.png) Data Control rule - ![App_Control_Icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982696967837.png) App Control rule |
| 5 | **Criteria** column shows the DLP Content **Profiles** that match this rule The DLP Content Profiles are configured in Security > DLP Profiles |

### Data Control Rule Settings

A Data Control rule has the following sections:

- General - Name and severity that you choose to assign to the rule. Also lets you enable or disable the rule.
- Application - Predefined application, category, custom application, or Sanctioned App that matches this rule. Only supported apps appear in the list of predefined applications.
- Activities - For Data Control rules, the activities are simplified to make it easier to implement the DLP policy. Select if the rule is for upstream and/or downstream traffic.

You must define an activity for each rule.
  - For applications, select the matching activity that the action is applied to.For more information, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service).

> [!NOTE]
> Note:
> 
> For application rules, you must enable TLS Inspection to inspect the traffic that matches the rule.
  - For categories, select the matching activity or criteria that the action is applied to.
- File Attributes - Define the type of content and file size for the data that matches this rule, and if there is an AND or OR relationship between the items.
  - Content Type - The drop-down menu shows all the supported file Content Types with file extensions and examples
  - Content Size - For more information, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service)
  - Content Encrypted - The rule action is applied to all encrypted files. The content of encrypted files can't be scanned by the DLP engine.
- DLP Profiles - The DLP engine can identify over 350 data types, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles). You can configure the profile with an AND or OR relationship between the data types.
- Access Methods - Requirements for the user agents on hosts and devices that can connect to your account.
- **Source** - Source of the traffic for this rule.
  - You can set the **Source** to a **Country** to create a rule that enforces traffic originating in that country, based on IP geolocation
  - For information about other **Source** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects)
- Time - Define the time period when the rule is active.
- Actions - Apply the specified action to traffic that matches the rule. The options are:
  - **Allow**: The action is allowed
  - **Block**: The action is blocked
  - **Notify:** When the action is taken, a Client notification is displayed. Users can dismiss the notification and continue their activity.
- Define the tracking options for events and email notifications.

## Configuring Data Control Rules

Create a new Data Control rule and configure the rule's settings to implement the DLP Data Control policy for your organization.

The **Time** options define the time range that the rule is enabled. You can configure custom options for a rule, or choose the default working hours that are defined for the account.

**To create a new Data Control rule:**

1. From the navigation menu, select **Security > App & Data Inline**.
2. Make sure that the **Data Control** is enabled (green is enabled, grey is disabled).
3. Click **New > Data Control Rule**.

The **Data Control Rule** panel opens.
4. Expand the **General** section and configure these settings:
  1. Enter a **Name** for the rule.
  2. Enable or disable the rule using the slider (green is enabled, grey is disabled).
  3. Select the **Severity**.

The Severity is used in the events and monitoring analytics for this rule.
5. In the **Application** section, select **Any Application**, or you can choose to limit the content inspection to a specific application or category.
  - When you select Any Application for a rule, the rule is enforced for all HTTP/S application traffic including both Internet and WAN traffic.When you select Any Application for a rule, the rule is enforced for both cloud applications and application traffic over the WAN.
6. Expand the **Activities** section, and configure these settings:
  1. Click **Add Activity** and select the item for the rule.
  2. When there are multiple items in the **Activities** section, in the **Satisfy** drop-down menu, define the relationship between the items:
    - **any (OR)** - If any of the items match the traffic, then the rule is applied
    - **all (AND)** - If all of the items match the traffic, then the rule is applied
7. In the **File Attributes** section, you can choose to only inspect content for specific file types and file sizes.

If you don't configure any **File Attribute** settings, then all supported file types and sizes are inspected.
  1. Click **Add File Attribute** and select **Content Type**, **Content Size**, or **Content Encrypted**.
  2. Define the settings for the File Attribute item.
  3. For multiple items, define the relationship between the items (see above 6b).
8. In the **DLP Profiles** section, you can add existing Content Inspection profiles and define the data types that match this rule.

If there are multiple DLP Profiles for a rule, there is an AND relationship between them.
9. Expand the **Access Methods** section, and define the user agent requirements.

If there are multiple items, there is an AND relationship between them.
10. Expand the **Source** section and select one or more objects for the traffic source for this rule (or you can enter an IP address).

Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
11. **(Optional)** Expand the **Time** section, and define when the rule is active.

Select **No time constraint** to set the rule as always active.
12. Expand the **Actions** section, and configure these settings:
  1. Select the **Action** for this rule. The options are **Allow**, and **Block**.
  2. **(Optional)** Configure tracking options to generate **Events** and **Send Notification**. The frequency starts counting after the first notification is sent.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](https://support.catonetworks.com/hc/en-us/sections/13908020158237-Alerts) section.
13. Click **Apply**.

## Setting the DLP Fail Mode

Enable or disable the DLP Fail Close setting. When enabled, the Data Control policy enforces a default Block action when a file scan times out or can't be completed due to other issues. By default, the DLP Fail Close setting is disabled. For more about DLP Fail mode, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service).

![DLP_Fail_Mode.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982738271261.png)

**To set the DLP Fail mode:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and in the **Settings** tab select **General**.
2. Click ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982713049117.png) to enable (green) the **DLP Fail Close** setting for the account.
3. Click **Save**. The **DLP Fail Close** setting is applied to the account.

## Analyzing Data Control Events

The Events page shows all the Data Control events for your account. These Security events are the Sub Type, **Apps Security**.

You can learn more about using the Events page [here](/v1/docs/analyzing-events-in-your-network).

These are the fields that are uniquely related to Application Control:

| Field Name | Description |
| --- | --- |
| DLP Profiles | DLP Content Profiles that matched this connection |
| File Name | Name of the file that was scanned by the DLP engine |
| File Size | Size of the file (in bytes) that was scanned by the DLP engine |
| File Type | File content type (such as Archive or Microsoft Office) |

## User Notifications

If an activity matches a rule with a **Notify** action, or is blocked by an Data Control rule, you can configure a notification to be displayed to the User, explaining which app was blocked and why. You can customize the content and branding of a notification to meet your organization's requirements.

This is how the default notification appears on a Windows device:

![Notificationa.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982697023645.png)

This is how the default notification appears on an iOS device:

![iOS_not.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982722637213.png)

### Prerequisites for User Notifications

- Supported from:
  - Windows Client v5.10 and higher
  - macOS Client v5.7 and higher
  - iOS Client v5.4 and higher
- User must be connected remotely
- Notifications must be enabled (if notifications are suppressed on the device, for example in a Focus or Do not disturb mode, notifications cannot be displayed)

### Enabling User Notifications

You can enable users to receive system notifications if an activity matches a Notify rule or is blocked by an Data Control rule.

**To enable user notifications:**

1. From the navigation menu, select **Access > Client Access > Security Policy Notifications**.
2. Select the **Enable Security Policy User Notifications** checkbox.
3. Click **Save**.

### Customizing User Notifications

To coach users on why the notification was displayed or an action was blocked, you can create and assign multiple notification templates and assign them to a policy rule. This lets you provide contextual notifications tailored to specific use cases at the point of enforcement. For more information, see [Creating User Notification Templates](/v1/docs/creating-user-notification-templates).
