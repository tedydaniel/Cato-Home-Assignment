---
title: "Adding Sections to the WAN and Internet Firewalls"
slug: "adding-sections-to-the-wan-and-internet-firewalls"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/adding-sections-to-the-wan-and-internet-firewalls"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Sections to the WAN and Internet Firewalls

This article discusses how to use sections in your WAN and Internet firewall policies.

## Overview of Firewall Sections

Firewall rulebases with many rules can be hard to navigate and manage. To improve rulebase management, add sections to the firewalls and group together many related rules into a single collapsible section.

You can move a rule within a section, or to a different section. Moving a rule in the firewall rulebase changes the priority of the rule and can have a significant impact on the functionality and performance of that policy. When moving a rule to a new section, make sure the rule has the required priority in that section.

These are the ways to move rules within a firewall rulebase:

- Drag and drop the rule
- Edit the **Rule Order** (priority) settings for the rule

You can also move entire sections in the rulebase using the following methods:

- Drag and drop the section
- Edit the **Move after section** setting for the section

For more about configuring the Cato WAN and Internet firewall rulebases, see the relevant article in [WAN and Internet Firewalls](/v1/docs/cato-firewalls).

## Adding Sections to a Firewall Rulebase

Add sections to the Internet or WAN firewalls to improve usability. When you add a new section, enter a name for the section and select which section it appears after. After the section is created, you can move existing rules to the section, or add new rules to it.

These buttons expand and collapse all the sections:

- Click ![FW_Sections_-_Expand_All.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303140219293.png) to expand all sections
- Click ![FW_Sections_-_Collapse_All.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303140301341.png) to collapse all sections

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303140388381.png)

**To add a new section to a firewall rulebase:**

1. From the navigation menu, select **Security** and then select **Internet Firewall** or **WAN Firewall**.
2. Click **New > New Section**.
3. Enter a **Name** for the section.
4. From the **Create after section** dropdown menu, select the section that the new section follows.
5. Click **Apply**.

The section is added to the rulebase as an empty section, and you can now add rules to the section.

## Working with Firewall Sections

You can move rules within a section, or to a different section, by dragging and dropping them to new positions, or editing their settings.

When you drag and drop a rule, the rule order automatically updates. When you drop a rule into a collapsed section, the rule is automatically assigned a rule order as follows:

- If the rule is moving to a higher section, the rule is assigned the lowest priority in the section
- If the rule is moving to a lower section, the rule is assigned the highest priority in the section

To move an entire section, you can drag and drop the entire section to a new position, or edit the section settings. When you drag and drop a section, the rule orders automatically update.

You can't move the first (default) section in the rulebase.

### Moving Rules

You can move rules within a section or to a different section in the rulebase.

To move a rule to a different section, select the relevant section, and then select the priority for the rule within the section.

**To move a rule:**

1. From the navigation panel, select **Security** and then select **Internet Firewall** or **WAN Firewall**.
2. To move a rule within a section, drag and drop the rule, or change the settings as follows:
  1. Select the rule in the WAN or Internet firewall rulebase.

The **Edit** panel opens.
  2. Enter a number for the new **Rule Order** that is within the range of the section.
3. To move a rule to a different section, drag and drop the rule, or change the settings as follows:
  1. Select the rule in the WAN or Internet firewall rulebase.

The **Edit** panel opens.
  2. In the **General** section, from the **Add to Section** dropdown menu, select the section for the rule.

The **Rule Order** is set by default to the last rule in the section.
  3. To change the default **Rule Order**, enter a number within the range of the selected section.
4. Click **Apply**.

### Moving Sections

You can move entire sections and the rule orders automatically update.

**To move a section:**

1. From the navigation panel, select **Security** and then select **Internet Firewall** or **WAN Firewall**.
2. Drag and drop the section to the new position, or change the settings as follows:
  1. Click the section name. The **Edit** panel opens.
  2. In the **Move after section** dropdown menu, select the section for the moved section to follow.
3. Click **Apply**.

### Removing Sections

When you no longer need a section, you can ungroup the rules from it and then the section is removed from the rulebase. When you ungroup the rules from a section, they are moved to the section immediately above.

You can't ungroup the first (default) section in the rulebase.

**To ungroup the rules from a section and remove the section:**

1. At the end of the section, click ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303140444957.png), and select **Ungroup Section**.
2. Click **Save**.

The section is removed and the rules are moved to the preceding section.
