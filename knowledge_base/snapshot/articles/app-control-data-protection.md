---
title: "Managing the Application Control Policy"
slug: "managing-the-application-control-policy"
updated: 2026-09-07T11:23:33Z
published: 2026-09-07T11:23:33Z
canonical: "knowledge.catonetworks.com/managing-the-application-control-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing the Application Control Policy

This article explains how to configure the Application Control rulebase as part of Cato's Cloud Access Security Broker (CASB) solution. This rulebase helps to manage how users are allowed to access and work with the pre-defined applications and system categories.

For more information about the Application Control policy in Cato, see [What is the Unified CASB Solution?](/v1/docs/what-is-the-unified-casb-solution).

## Creating the Application Control Policy

The Application Control policy is an extension of the Internet and WAN firewalls for Cloud Applications. Only flows that are allowed by the firewall policies are inspected by the inline Application Control policy. The Application Control policy does not apply to apps with the **Application** type in the [App Catalog](/v1/docs/using-the-app-catalog).

> [!NOTE]
> **Note:** To manage application usage with an Application Control rule, make sure that this application is allowed by the Internet and WAN firewalls.

The Application Control policy is an ordered rulebase that lets you define activities and required criteria for applications and categories. Each rule defines one application or one category. Once a rule matches the traffic, the lower priority rules (below the matching rule) are not applied to the traffic.

The final rule in the rulebase is an implicit ANY ANY allow rule, so if a connection does not match a rule, then it is allowed by the final implicit rule.

### Managing Tenant Restrictions

Tenant Restriction policies limit which SaaS tenants users can access, preventing access to personal or unauthorized accounts and reducing data-leak risks. Cato enforces these controls through two methods: Tenant Awareness, which applies tenant-specific allow or block actions within Application Control, and the Tenant Restriction policy, which injects HTTP headers to direct apps to the correct tenant. Together, these capabilities ensure users access only your organization’s approved tenants.

For more information, see [Managing Tenant Restrictions for SaaS Apps (Tenant Restrictions Policy)](/v1/docs/managing-tenant-restrictions-for-saas-apps-tenant-restrictions-policy) and [Restricting Access to SaaS Application Tenants.](/v1/docs/restricting-access-to-saas-application-tenants).

### Policy Revisions and Concurrent Editing by Multiple Admins

The Application Control Policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Working with the Application Control Configuration Wizard

The Application Control Configuration Wizard autonomously reviews your policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management. For more information, see [Using the Configuration Wizard](/v1/docs/using-the-configuration-wizard).

### Prerequisites for the Application Control Policy

- For application rules, you must enable TLS Inspection to inspect the traffic that matches the rule.
- As a result of a more granular app policy, make sure that the Internet firewall policy has two rules with a high priority (near the top of the rulebase) to block QUIC traffic. It is more secure to only allow standard protocols, and block these items in separate rules:

> [!NOTE]
> **Note:** When you initially enable the Application Control Policy, a rule is automatically added to the top of Internet firewall rulebase that blocks QUIC and GQUIC traffic. This follows Cato’s security best practices.
> 
> If necessary, you can edit this rule based on the requirements of your account.
  - Application - GQuic
  - Service - QUIC
- The Application Control policy is included in the CASB license. For more about purchasing the CASB license, please contact your Cato representative.

## Adding Rules to the Application Control Policy

When you add a rule to the Application Control policy, configure each section in the rule that is required to define the access and permitted actions for that application.

We recommend that when you are implementing the policy for the first time, or adding a new application to an existing policy, that you run the new rules with the Allow action and enable events. Then review the events and see if this rule would block allowed traffic.

![CASB_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29334867441181.png)

### Application Control Rule Settings

An Application Control rule has the following sections:

- General - Name and severity that you choose to assign to the rule. Also lets you enable or disable the rule.
- Application - Predefined application, category, custom application, or Sanctioned App that matches this rule. Only supported apps appear in the list of predefined applications.
- Activities - Define one or more items that define the application behavior, and if there is an AND or OR relationship between the items.

You can select **Any Granular Activity** for the rule to match all activities performed for a granular app, however, only the **Allow** action is available.

If the **Activities** field is not configured and empty, then the rule matches
  - For applications, select the matching activity that the action is applied to.For more information, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service).

> [!NOTE]
> **Note:** For application rules, you must enable TLS Inspection to inspect the traffic that matches the rule.
  - For categories, select the matching activity or criteria that the action is applied to.

> [!NOTE]
> **Note:** For category rules with a defined activity, you must enable TLS Inspection to inspect the traffic that matches the rule.
- Access Methods - Requirements for the user agents on hosts and devices that can connect to your account.
- **Source** - Source of the traffic for this rule.
  - You can set the **Source** to a **Country** to create a rule that enforces traffic originating in that country, based on IP geolocation
  - For information about other **Source** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects)
- Device Posture - Select the [Device Profile](/v1/docs/creating-device-posture-profiles-and-device-checks) that the device must meet for the Action to apply to the device.

For example, a rule with the **Allow** action, and devices must meet the Device Profile for that rule, otherwise the traffic is blocked. For more about using Device Profiles with security rules, see [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules).
- Time - Define the time period when the rule is active.
- Actions - Apply the specified action to traffic that matches the rule. The options are:
  - **Allow**: The action is allowed
  - **Block**: The action is blocked
  - **Notify:** When the action is taken, a Client notification is displayed. Users can dismiss the notification and continue their activity.
- Define the tracking options for events and email notifications.

### Creating New Application Control Rules

Create a new Application Control rule and configure the rule's settings to implement the Application Control policy for your organization.

The **Time** options define the time range that the rule is enabled. You can configure custom options for a rule, or choose the default working hours that are defined for the account.

**To create a new Application Control rule:**

1. From the navigation menu, select **Security > App & Data Inline**.
2. Click **New** and select **App Control Rule**. The **App Control Rule** panel opens.
3. Expand the **General** section and configure these settings:
  1. Enter a **Name** for the rule.
  2. Enable or disable the rule using the slider (green is enabled, grey is disabled).
  3. Select the **Severity**.

The Severity is used in the events and monitoring analytics for this rule.
4. Expand the **Application** section, and select the app or category for the traffic that matches this rule. **Note:** Some apps have more than one Category. To apply a rule to these apps, include all their categories in the rule. You can view an app’s categories in the [App Catalog](/v1/docs/using-the-app-catalog).
5. Expand the **Activities** or **Criteria** section, and configure these settings:
  1. Click **Add Activity** or **Add Criteria** and select the item for the rule.
  2. If necessary, click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29334891148957.png) and configure the settings for this item.
  3. When there are multiple items in the **Activities** or **Criteria** section, in the **Satisfy** drop-down menu, define the relationship between the items:
    - **any (OR)** - If any of the items match the traffic, then the rule is applied
    - **all (AND)** - If all of the items match the traffic, then the rule is applied
6. Expand the **Access Methods** section, and define the user agent requirements.

If there are multiple items, there is an AND relationship between them.
7. Expand the **Source** section and select one or more objects for the traffic source for this rule (or you can enter an IP address).

Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
8. Expand the **Device Posture** section, and select one or more Device Profiles for the rule.

When there are multiple Device Profiles for a rule, there is an OR relationship between them.
9. **(Optional)** Expand the **Time** section, and define when the rule is active.

Select **No time constraint** to set the rule as always active.
10. Expand the **Actions** section, and configure these settings:
  1. Select the **Action** for this rule.
  2. **(Optional)** Configure tracking options to generate **Events** and **Send Notification**. The frequency starts counting after the first notification is sent.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
11. Click **Apply**.

### Using Value Sets in Application Control Rules

**Value Sets** are user defined categories that help you manage Application Control rules for groups of items such as URLs or email addresses. For example, you can:

- Manage access to a group of specific Dropbox folders with one rule, by configuring a Dropbox rule with a **Value Set** defined with the **Full Path URLs** for the folders
- Allow the **Login** activity for only specific users by creating a rule configured with a **Value Set** defined with a list of email addresses

![Value_Sets_Rule_Config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29334867629341.png)

**To use a Value Set in an Application Control rule:**

1. Create a **Value Set** of type **Text Strings**. Value Sets with other types will not work with Application Control Rules.
2. Create a new application control rule as described above.
3. In the **Activities** section, select the **In** operator and then create or select the **Value Set**.

For more about creating **Value Sets** , see [Working with Categories](/v1/docs/working-with-categories).

### Adding an Exception to the Application Control Policy

The Application Control policy is an ordered rulebase, and when you need to create an exception for a rule, you can create a new rules to allow the traffic. Make sure that the new rule is BEFORE the blocking rule.

**To add an exception to a block rule in the Application Control policy:**

1. From the navigation menu, select **Security > App & Data Inline**.
2. On the right of the rule, click ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29334891332509.png) and select **Add Rule Above**.

The **New Cloud App Rule** panel opens.
3. Configure the settings for the Application Control rule.
  - In the **Actions** section, make sure to select **Allow**.
4. Click **Apply**.

The exception is added to the Application Control rulebase.

## Understanding the Application Control Fields

This section describes the fields that are available for rules that require criteria and activities.

### Criteria Based Rules

These are explanations of the fields that you can configure for rules that require specific criteria. The criteria are divided into three sections: Security, General, and Compliance.

| Criteria Field | Explanation |
| --- | --- |
| **Security criteria** |
| Audit Trail | Application supports audit trail for admin changes |
| Encryption Protocol | Based on analysis in the Cato Cloud, define the allowed TLS encryption protocols for the application |
| Encryption at Rest | Data storage for the service is encrypted |
| HTTP Security Headers | Supports HTTP security headers |
| MFA | Supports Multi Factor Authentication |
| RBAC | Supports Rule Based Access Control (RBAC) for the admins |
| Remember Passwords | Allows users to remember the password on the local browser |
| Risk Score | Cato assigns each cloud app a risk score between 0 (no risk) to 10 (very high risk) to help you evaluate if the application meets the requirements of your security policy, see [Using the Cloud Apps Dashboard](https://support.catonetworks.com/document/preview/40340#UUID-c49f955f-102c-469d-ac85-341de87dc2ff) |
| SSO Type | Supports Single Sign-On (SSO) |
| TLS Enforcement | Based on analysis in the Cato Cloud, application only allows TLS encrypted traffic |
| Trusted Certificates | Based on analysis in the Cato Cloud, this application only uses trusted certificates from a registered CA (no self-signed or revoked certificates) |
| **General criteria** |
| Country Code | Country where the company headquarters is physically located (Registered Country of Origin) |
| **Compliance criteria** |
| Compliance Options | See below, *Supported Compliance Requirements*. |

#### Supported Compliance Requirements

These are the compliance requirements that you can add to an Application Control rule. For example, you can only allow an application that is compliant with HIPAA or SOC-2.

- HIPAA
- ISAE 3402
- ISO 27001
- PCI-DSS
- SOC-1
- SOC-2
- SOC-3
- SOX
- SSO

### Activity Based Rules

These are explanations of the fields that you can configure for rules that require specific activities. The table also shows an example of an app that includes the activity field for a rule.

**Note**: If the **Activities** field is left blank, any activity is matched to the rule.

| Activity Field | Explanation | Example App |
| --- | --- | --- |
| Add Attachment | Attach a file to an email | Gmail |
| Chat | Use the chat feature of an app | LinkedIn |
| Continue with Provider | Social/IdP login flows | OpenAI |
| Delete message | Delete a message from a conversation in an app | Slack |
| Download | Download a file from cloud storage | Google Drive |
| Edit | Edit permissions for the app | Salesforce |
| Enterprise SSO Login | Enterprise-based login flows | OpenAI |
| Export | Export data or records from the app | Salesforce |
| Full Path URL | Only app traffic that matches the specific path is allowed or blocked. For example, in **dropbox.com/contact** the Full Path URL must include the path **/contact** | Dropbox |
| Login | Log in to an account | Google |
| Logoff | Log out of an account | Google |
| Post | Post a message or comment to a social media app | Facebook |
| Save report | Save a report from the app to the host or device | Salesforce |
| Send mail | Send email messages | Microsoft Outlook |
| Send message (file) | Send a message that includes a file | Slack |
| Send message (text) | Send a message that only includes text | Slack |
| Sign in | Sign in to the application | Slack |
| Sign out | Sign out of the application | Slack |
| Third Party Login | Third Party SSO login flows | Claude |
| Upload | Upload a file to cloud storage | Box |
| Watch stream | Watch streaming video | YouTube |

## Best Practices for the Application Control Policy

This section contains recommended best practices for implementing the Application Control policy in your account. When indicated, the best practice also applies to adding a new application to the policy.

- When you implement the policy, or add a new application with the Block action:
  - Enable events for the rule.
  - Review the events that the rule generates and make sure that there are no events for traffic that you want to allow (false positive traffic).
  - If there is false positive traffic, you can make these changes:
    - Refine the scope of the rule to exclude the false positive traffic
    - Create a new allow rule before the block rule, and the scope of the new rule is only for the false positive traffic
- The policy supports browser-based apps. Native clients are not supported unless specified explicitly.
- Remember that the Application Control policy is an ordered policy, and the final implicit rule is ANY ANY Accept. Add rules to the policy to block the relevant application traffic, activities and criteria.
- The maximum number of Application Control events for your account is 2.5 million events per hour.

### Sample Application Control Rules

This section contains examples of Application Control rules to enforce the CASB policy in your organization.

#### Enforcing Compliance for Office365

![BestPractice_Office365.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29334834670365.png)

The previous example shows two rules for the **Office Programs and Services** category, which is for Office365 apps and services.

1. Rule 1 allows traffic which meets the compliance requirements for Office365 with the following settings:
  - **Source - Any**. Applies to all traffic sources.
  - **Application - Office Programs and Services**. Applies to the category for Office365.
  - **Criteria - SOC2, Trusted Certificates, SSO** with AND relationship. Applies to traffic that meets all of the compliance items.
  - **Severity - Medium**. The traffic that matches this rule is categorized as **Medium** risk for analytics.
  - **Action - Allow**. Office365 traffic that meets the compliance requirements is allowed.
2. Rule 2 blocks all other Office365 traffic, with the following settings that are different than rule 1:
  - **Criteria** - none. Applies to all Office365 traffic, because rule 1 already matches the allowed traffic.
  - **Action - Block**. Blocks all Office 365 traffic, because rule 1 already allowed all the compliant traffic.
  - **Tracking - Event**. Generate events for all non-compliant Office365 traffic.

## Analyzing Application Control Events

The Events screen shows all the Application Control events for your account. These Security events are the Sub Type, **Apps Security**.

You can learn more about using the Events page [here](/v1/docs/analyzing-events-in-your-network).

These are the fields that uniquely related to Application Control:

| Field Name | Description |
| --- | --- |
| app activity | For events with the block action, shows the activity for the rule (see above, **Activity Based Rules**) |
| app activity category | The general category of the app activity in the event. For more about app activity categories, see below **Understanding App Activity Categories and Types**. |
| app activity type | The type of app activity. For more about app activity types, see below **Understanding App Activity Categories and Types**. |
| application | Name of the application |
| application risk | Cato risk level for this application |
| full path URL | Full path of the URL that the traffic is connecting to |
| is sanctioned app | True means that this application is configured as a sanctioned app |

### Understanding App Activity Categories and Types

These are the possible values for the **App Activity Category** field and the description for each category:

- **Content Operations** - Activities where data (usually files or clear text) is:

For example: Upload, Download, Move
  - Uploaded from the client to the SaaS app
  - Downloaded from the SaaS app to the client
  - Edited in the SaaS app
- **Content Share** - Activities where the access is modified for data that already resides on a SaaS app. For example: Share, Share Anonymous Link
- **Communication & Collaboration** - Activities where information is transferred between users of the SaaS app. For example: Chat, Video, Voice
- **Search & View** - Activities where data on the SaaS app is accessed without the data itself or its permissions being modified. For example: Search, File Accessed
- **Admin Settings** - For example: User creation, Quarantine, Change permissions
- **Login and Authentication** - For example: Login, Logout, Fail login
- **API and Integration** - For example: Query API, Add <App Name> integration
- **Execution** - For example: Execute Flow, Run Report/Dashboard
- **General** - Activities that don't meet the definition of any of the other categories, or activities that haven't yet been assigned a category

These are the possible values for **App Activity Type** and the activities included in each type:

- **File Sharing** - Upload, Download, Remove, Share, Edit, View, Create
- **Source Control** - Pull/Clone, Push
- **Chat** - Send Message, Send Voice Message, Receive Message, Delete Message, Add Reaction
- **Mail** - Send Mail
- **Social Networks** - Post, Comment
- **Admin Apps** - Login, Third Party Login, Logoff, Authorize Third Party, Change Item's Permissions
- **IaaS Platforms** - Access
- **Finance** - Edit, Export, Save Report
- **Streaming Media** -Watch Stream
- **Web Conferencing** - Video Call
- **Knowledge Sharing** - Create, Edit, Share
- **Task Management** - Create Task, Edit Task, Delete Task, Change Task Status, Assign
- **Search Engine** - Search
- **AI Tools** - Conversation

## User Notifications

If an activity matches a rule with a **Notify** action, or is blocked by an Application Control rule, you can configure a notification to be displayed to the User, explaining which app was blocked and why. You can customize the content and branding of a notification to meet your organization's requirements.

This is how the default notification appears on a Windows device:

![Notificationa.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29334880979741.png)

This is how the default notification appears on an iOS device:

![iOS_not.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29334891654301.png)

### Prerequisites for User Notifications

- Supported from:
  - Windows Client v5.10 and higher
  - macOS Client v5.7 and higher
  - iOS Client v5.4 and higher
- User must be connected remotely
- Notifications must be enabled (if notifications are suppressed on the device, for example in a Focus or Do not disturb mode, notifications cannot be displayed)

### Enabling User Notifications

You can enable users to receive system notifications if an activity matches a Notify rule or is blocked by an Application Control rule.

**To enable user notifications:**

1. From the navigation menu, select **Access > Client Access > Security Policy Notifications**.
2. Select the **Enable Security Policy User Notifications** checkbox.
3. Click **Save**.

### Customizing User Notifications

To coach users on why the notification was displayed or an action was blocked, you can create and assign multiple notification templates and assign them to a policy rule. This lets you provide contextual notifications tailored to specific use cases at the point of enforcement. For more information, see [Creating User Notification Templates](/v1/docs/creating-user-notification-templates).
