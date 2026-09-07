---
title: "Managing the Internet Firewall Policy"
slug: "managing-the-internet-firewall-policy"
updated: 2026-09-07T11:22:17Z
published: 2026-09-07T11:22:17Z
canonical: "knowledge.catonetworks.com/managing-the-internet-firewall-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing the Internet Firewall Policy

This article explains how to manage the Internet firewall policy to control Internet access for your organization.

For more information about the Internet firewall policy in Cato, see [What is the Cato Internet Firewall?](/v1/docs/what-is-the-cato-internet-firewall).

## Overview

The Internet firewall inspects traffic between the WAN and the Internet and lets you create rules to control this traffic. Similar to the WAN firewall, the Internet firewall uses an ordered rulebase, starting from the first rule, connections are inspected according to each rule.

The Internet Firewall lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings).

The Internet Firewall Configuration [Wizard](/v1/docs/using-the-internet-firewall-configuration-wizard) autonomously reviews your policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management.

## Configuring the Internet Firewall Policy

This section explains the procedures for creating Internet firewall rules, overriding locks to edit rules, and publishing or discarding an unpublished revision.

![InternetFW.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27930213821085.png)

#### Enabling the Ordered Internet Firewall

The Internet firewall in the Cato Cloud lets you control Internet access for your corporate network. Easily create an Internet security policy that allows users to access business-related web content and blocks inappropriate websites, applications, and so on.

**To enable or disable the Internet firewall:**

1. From the navigation menu, click **Security > Internet Firewall**.
2. At **Firewall Enabled** above the rulebase, click the slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27930250369437.png) to enable (green) or disable (gray) the Internet firewall for the account.
3. Click **Save**.

### Creating New Internet Firewall Rules

Create Internet Firewall rules and save the changes to your unpublished revision.

For more about **Source**, **App**, and **Category** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects).

The **Time** options define the time range that the rule is enabled. You can configure custom options for a rule, or choose the default working hours that are defined for the account.

**To create a new rule for the Internet firewall:**

1. From the navigation menu, select **Security > Internet Firewall**.

The Internet Firewall page opens to your existing unpublished revision, or to the newest published revision.
2. Click **New**.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider (green is enabled, grey is disabled).
5. Configure the **Rule Order** for this rule.

For more about the rule order options, see [What is the Cato Internet Firewall?](/v1/docs/what-is-the-cato-internet-firewall).
6. Expand **Source** and select the source type.
  - Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
  - When needed, select a specific object from the drop-down list for that type.
7. Expand the **Criteria** section and add the device conditions to the rule. For more information, see [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules). The default values are **Any**.
8. Expand the **App/Category** section and select one or more applications for the rule.

When there is more than one App/Category object in a rule, there is an OR relationship between them. The default value is **Any**. **Note:** Some apps have more than one Category. To apply a rule to these apps, include all their categories in the rule. You can view an app’s categories in the [App Catalog](/v1/docs/using-the-app-catalog).
9. Expand the **Service/Port** section and define the type or types (Service, Port/Protocol, Custom Service, or Any) that are applied to this rule.

When there is more than one Service/Ports object in a rule, there is an OR relationship between them. The default value is **Any**.
10. Select the **Action** for this rule. The options are **Allow**, **Block**, **Prompt**.
11. **(Optional)** Configure tracking options to generate **Events** and **Send Notification**. The frequency starts counting after the first notification is sent.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the section.
12. **(Optional)** Configure the **Time** options that define when this rule is enabled.
13. Click **Apply**. The new rule is added to the rulebase.
14. Click **Save**.

The changes are saved to your unpublished revision, and are available for editing until they are published or discarded.

### Using Exceptions to Allow Internet Connections

You can use exceptions in the Internet firewall rulebase to ignore a specific rule and continue with the lower priority rules. Remember to make sure that a lower priority rule doesn't match and block the traffic. The final implicit ANY ANY Allow rule allows all traffic. For example, if rule #3 blocks access to the Hiring category, you can create an exception that does not block access for the Human Resources (HR) department.

The exception for a rule is a sub-set of the rule, and some settings apply to both the rule and the exception:

- When you disable the rule, the exception is also disabled
- When you move the rule and change the priority, the exception is also moved

**To add an exception to a firewall rule:**

1. From the navigation menu, select **Security > Internet Firewall**.
2. On the right of the rule, click ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27930213886365.png) and select **Add Exception**.

The **Add Exception** panel opens.
3. Expand and configure the settings for the rule exception.

The Action for the parent rule is not applied to the rule exception.
4. Click **Apply**. The exception is added below the rule.
5. Click **Save**. The exception is saved to your unpublished revision and is available for editing until it is published or discarded.

**To remove an exception from a firewall rule:**

1. From the navigation menu, select **Security > Internet Firewall**.
2. From the right-hand column of the rule, click ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27930213886365.png) and in the pop-up window select **Delete Exception**.

The exception is removed from the rule.
3. Click **Save**. The exception is deleted from your unpublished revision, and you can publish the revision to remove the exception from the account policy.

## Understanding Entities Within the Internet Firewall Rule

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(200).png)

You can learn more about any entity within a Firewall rule by clicking on it to open Ask AI prompts about the entity. Clicking on the prompts opens the Ask AI draw with a pre-populated prompt to provide information. You can learn more about what the entity is, find other rules that contain it, and see additional Internet Firewall checks that could be applied to the entity.

## Known Limitations

- For the Facebook Messenger app, it's not possible to use the Internet Firewall to block the Messenger app and allow the Facebook app because Messenger shares the same domain as Facebook to load resources. You can use the [CASB Application Control policy](/v1/docs/managing-the-application-control-policy) to manage access to these apps.
