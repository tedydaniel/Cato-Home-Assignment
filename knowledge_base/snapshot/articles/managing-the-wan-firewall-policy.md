---
title: "Managing the WAN Firewall Policy"
slug: "managing-the-wan-firewall-policy"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/managing-the-wan-firewall-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing the WAN Firewall Policy

This article explains how to manage the WAN firewall rulebase, including: create new rules, edit rules, enable and disable a rule, search for a rule, and delete rules.

For more information about the WAN firewall policy in Cato, see [What is the Cato WAN Firewall?](/v1/docs/what-is-the-cato-wan-firewall).

## Overview

The WAN firewall in the Cato Cloud controls access to objects and entities in your WAN and lets you create rules to prevent unauthorized access to the network. It uses an ordered rulebase, inspecting the connection and checking each rule sequentially until a rule matches the connection.

The WAN firewall lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings).

## Enabling and Disabling the WAN Firewall

When the WAN firewall is disabled, there is no access control and all WAN resources are accessible to anyone.

![WAN-FW-enabled.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27704386493085.png)

**To enable or disable the WAN firewall:**

1. From the navigation menu, click **Security > WAN Firewall**.
2. At **Firewall Enabled** above the rulebase, click the slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27704397046173.png) to enable (green) or disable (gray) the WAN firewall for the account.
3. Click **Save**.

## Creating New WAN Firewall Rules

Create a new WAN firewall rule and configure the settings for the rule to manage access control for the WAN. Use the **Add Rule Below** option to easily add a rule to the correct place in the rulebase.

For more about **Source**, **Destination**, **App**, and **Category** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects).

The **Time** options define the time range that the rule is enabled. You can configure custom options for a rule, or choose the default working hours that are defined for the account.

**To create a new rule for the WAN firewall:**

1. From the navigation menu, click **Security > WAN Firewall**.

The WAN Firewall page opens to your existing unpublished revision, or to the newest published revision.
2. Click **New**. The **New** panel opens.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider (green is enabled, grey is disabled).
5. Configure the **Position** and **Direction** for the new rule:
  - By default, the rule is applied in one direction, from the source **To** the destination. Click the **Direction** drop-down menu to set the rule to operate in **Both** directions.
  - For more about the rule order options, see [What is the Cato WAN Firewall?](/v1/docs/what-is-the-cato-wan-firewall).
6. Expand the **Source** section and select one or more objects for the traffic source for this rule (or you can enter an IP address).
  1. Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
  2. When needed, select a specific object from the drop-down list for that type.
7. Expand the **Destination** section enter a string or select one or more destination objects for this rule.
  1. Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
  2. When needed, select a specific object from the drop-down list for that type.
8. Expand the **Criteria** section and add the device conditions to the rule. For more information, see [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules). The default values are **Any**.
9. Expand the **App/Category** section and select one or more applications for the rule.

When there is more than one App/Category object in a rule, there is an OR relationship between them. The default value is **Any**.
10. Expand the **Service/Port** section and define the type or types (Service, Port/Protocol, Any) that are applied to this rule.

When there is more than one Service/Ports object in a rule, there is an OR relationship between them. The default value is **Any**.
11. Select the **Action** for this rule. The options are **Allow**, **Block**, **Prompt**.
12. **(Optional)** Configure tracking options to generate **Events** and **Send Notification**. The frequency starts counting after the first notification is sent.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the section [Alerts](/v1/docs/notifications).
13. **(Optional)** Configure the **Time** options that define when this rule is enabled.
14. Click **Apply**. The new rule is added to the rulebase.
15. Click **Save**.

The changes are saved to your unpublished revision, and are available for editing until they are published or discarded.

## Adding Exceptions to the WAN Firewall

You can use exceptions in the WAN firewall rulebase to ignore a specific rule and continue with the lower priority rules. For example, if rule #3 allows VPN access to the RnD subnet, you can create an exception that does not allow VPN access for a small subset of SDP users. When creating an exception for a block rule, the traffic must match an allow rule with a lower priority, otherwise the final implicit ANY ANY block rule blocks the traffic.

The exception for a rule is a sub-set of the rule, and some settings apply to both the rule and the exception:

- When you disable the rule, the exception is also disabled
- When you move the rule and change the priority, the exception is also moved

**To add an exception to a firewall rule:**

1. From the navigation menu, click **Security > WAN Firewall**.
2. On the right of the rule, click ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27362486514077.png) and select **Add Exception**.

The **Add Exception** panel opens.
3. Expand and configure the settings for the rule exception.

The Action for the parent rule is not applied to the rule exception.
4. Click **Apply**. The exception is added below the rule.
5. Click **Save**. The exception is saved to your unpublished revision and is available for editing until it is published or discarded.

**To remove an exception from a firewall rule:**

1. From the navigation menu, click **Security > WAN Firewall**.
2. From the right-hand column of the rule, click ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27362486514077.png) and in the pop-up window select **Delete Exception**.

The exception is removed from the rule.
3. Click **Save**. The exception is deleted from your unpublished revision, and you can publish the revision to remove the exception from the account policy.

## Working with WAN Firewall Rules

Use the WAN Firewall rule search to find the rules you want to work with. The search function finds and shows rules that include the search terms in any of the following fields:

- **Name**
- **Source**
- **Device**
- **Destination**
- **App/Category**
- **Service/Port**

If a rule is part of a section, the results show the rule within the section.

### Editing WAN Rules and the Rulebase

You can edit rules and change the order of the rules in the firewall rulebase.

**To edit a rule:**

1. From the navigation menu, click **Security > WAN Firewall**.
2. Click on the rule. The **Edit** panel opens.
3. Expand any of the sections in the panel to display and edit the current rule settings.
4. Click **Apply** to change the rule settings. The **Edit** panel closes.
5. Click **Save** to save the changes.

The changes are saved to your unpublished revision and are available for editing until they are published or discarded.

### Changing the Order of a Rule

Rule order is defined by setting a rule’s position relative to other rules. For example, set a rule to follow a specific rule, or to be first in a section.

These are the options for defining the rule order:

- **Before Rule** - The rule is positioned immediately before the selected rule
- **After Rule** - The rule positioned immediately after the selected rule
- **First in Section** - The rule is positioned first in the selected section
- **Last in Section** - The rule is positioned last in the selected section
- **First** - The rule is positioned at the top of the rulebase
- **Last** - The rule is positioned at the bottom of the rulebase

**To change the order of the rules:**

1. From the navigation menu, click **Security > WAN Firewall**.
2. Hover at the left end of the rule, and this icon is shown: ![move.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27362462244253.png).
3. Click the icon and drag the rule up or down in the rulebase.
4. Click **Save**.

### Enabling and Disabling a WAN Rule

**To enable or disable a rule:**

1. From the navigation menu, click **Security > WAN Firewall**.
2. On the right of the rule, click the icon ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27362486514077.png) and from the pop-up menu select **Enable** or **Disable**.
3. Click **Save**. The rule is enabled or disabled.

### Deleting WAN Rules

You can delete one or more rules from the firewall rulebase. After you delete the rules, you cannot undo or restore them.

**To delete rules from the firewall rulebase:**

1. From the navigation menu, click **Security > WAN Firewall**.
2. Click the icon ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27362486514077.png) and from the pop-up window select **Delete Rule**.
3. In the confirmation window, click **Delete Rule**. The rule is removed.
4. Click **Save**. The rule is deleted.
