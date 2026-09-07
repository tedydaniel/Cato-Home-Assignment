---
title: "Working with CMA Advanced Groups and Groups"
slug: "working-with-cma-advanced-groups-and-groups"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/working-with-cma-advanced-groups-and-groups"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with CMA Advanced Groups and Groups

## Overview

Advanced Groups and Groups in the Cato Management Application (CMA) let you manage sets of sites, hosts, subnets, and other entities as a single object in policy configurations.

Grouping objects lets you operate at scale by separating group membership from policy application. This approach streamlines policy management, separates object lifecycle tasks (for example, adding or removing members) from rule definition and enforcement, and clarifies administrative responsibilities. Different admins can manage group membership and policy usage independently

When you're ready to create a group, you can choose between two types:

- Advanced Groups
  - Supports API integration: [mutation APIs](https://api.catonetworks.com/documentation/#mutation-groups.createGroup) to create and configure, and [query APIs](https://api.catonetworks.com/documentation/#query-groups.group)
  - Dynamically validates that members are compatible with the supported policies
  - Offer a transparent and intuitive user experience, making it easy to identify which advanced groups are valid in each policy context
  - Built to support future enhancements, so Cato can easily update advanced groups with different member types and new objects
- Groups - the earlier type that remains supported to continue existing processes and configurations
  - Groups also continue to support customized network options, such as custom DNS and DHCP settings

### Supported Policies for Advanced Groups

Advanced groups are supported in these policies:

- Internet firewall
- WAN firewall
- Socket Next Gen LAN Firewall
- Network Rules

Additional policies will support advanced groups in the future. All policies support groups.

### Using Advanced Groups and Groups in Policies

Fields in a rule (such as Source) show all available groups for selection, including both Groups and Advanced Groups.

- Advanced groups - Only compatible advanced groups are available to add to a rule
- Groups - All groups are available to add to a rule

There is no validation for groups, and if the group includes non-compatible members, then the rule behavior can be inconsistent.

#### What is a Compatible Member of an Advanced Group?

An advanced group is only compatible with a policy if all of its members are supported. Otherwise, the advanced group is not compatible. For example, the Link Health Rules policy only supports sites, so a group that contains sites and hosts would be non-compatible for that rule.

The CMA or API validates members based on the policies and doesn't let you add non-compliant members to an advanced group. Similarly, when an advanced group is assigned to policies, you can add new members who are compatible with all the policies.

### Using IP Ranges in Advanced Groups

IP Ranges lets you define and reuse large sets of IP ranges across multiple policies, helping you reduce manual configuration and ensure consistency at scale. Advanced groups support adding IP Ranges as a member type, providing:

- Manage large sets of global IP Ranges as members of advanced groups in Internet and WAN Firewall policies
- Ensures that any changes you make to an IP Range object are automatically applied across all relevant rules

For more information about creating IP Ranges, see [Using IP Ranges in Policies](/v1/docs/using-ip-ranges-in-policies).

## Managing Advanced Groups

### Adding Advanced Groups

![new_groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30322190935069.png)

**To add a group and define its members:**

1. In the navigation menu, click **Resources > Advanced Groups**.
2. Click **New**. The **Create** panel opens.
3. In the **General** section, enter the group **Name** and **Description**.
4. In the **Members** section, add the items that are members of this group.
5. Click **Save**.

The advanced group is saved and added to the CMA.

## Managing Groups

You can create groups and leverage them (in addition to the pre-defined groups) as global objects across the CMA.

Define the items in the CMA that are members of the group. You can also define special configurations for groups relating to DNS and DHCP Options.

![Groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30322190958621.png)

These are the types of groups:

- **Manual:** Groups that you manually define. Group members can include various network entities (such as **Sites**, **Networks**, **Floating Ranges**, and **Hosts**).
- **System:** Groups that are pre-defined in the CMA. These are dynamic groups that are automatically updated with new members when the appropriate items are added. For example, when a new site is added to your account, the **All Sites** system group is automatically updated with the new site. If this group is used in a security rule, the rule will also apply to the new site.

System groups include:
  - **All Sites:** A group that includes all sites
  - **All Floating Ranges:** A group that includes all floating ranges defined in the system

### Showing Groups and Group Members

![legacy_groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30322226482461.png)

**To show the members of a group:**

1. In the navigation menu, click **Resources > Groups**.
2. In the navigation menu, click **Members**. The group members are displayed.

### Adding Groups

You can define groups and their members. These are the behaviors for System groups:

- Definitions in the **General** pane are defined by the CMA and can't be modified.
- For System groups, definitions in the **Members** pane are defined by the CMA and can't be modified.

**To add a group and define its members:**

1. In the navigation menu, click **Resources > Groups**.
2. Click **New**. The **Create** panel opens.
3. Enter the group **Name** and click **Apply**. The group is added to the screen.
4. Click the group. The **General** screen for the group opens.
5. **(Optional)** Enter a **Description**.
6. Add the items that are members of this group:
  1. In the navigation menu, click **Members**. The group members are displayed.
  2. From the **Add Members** drop-down menu, select the type of member to add (for example, Site, Network Interface, or Host).

Cato recommends that each group contain only one type of member. For example, a group of all of your network interfaces.
    - Network Interface - All traffic on the interface (all networks)
    - Interface Subnet - VLAN, routed, or direct ranges, or a secondary AWS vSocket native range
    - Global Range - Native range on the interface
  3. Select all the items for that type that you are including in the group.

The selected members are added to the Members list.
7. Click **Save**.

The group is saved and added to the CMA.

## Deleting Advanced Groups or Groups

To delete an advanced group or group, you must first remove it from any policy that uses the group. For example, if you don't remove the group from the Internet Firewall policy, then you can't delete the group.

**To delete a group:**

1. In the navigation menu, click **Resources > Advanced Groups** or **Resources > Groups**.
2. Click the Delete icon at the end of the row.

A confirmation window opens.
3. Click **Delete**.

The group is deleted.

## FAQ for Advanced Groups

---

### 

#### Q: Should I use advanced groups or groups?

**A:** Use advanced groups if:

- You will manage them through the API
- You want to use them in these policies: Internet or WAN Firewall
- You don’t require custom DNS or DHCP settings
- Otherwise, you should use groups

#### Q: When do I use containers, and when do I use advanced groups?

**A:**[Containers](/v1/docs/integrating-custom-ioc-lists-with-containers) are designed to support values such as IPs and FQDN, and advanced groups support CMA objects. Here are some guidelines:

- Advanced Groups - Provides stronger management features such as descriptions, search, and managing individual members for CMA objects
- Containers - Scale to millions of items and are typically used for custom IoC (Indicators of Compromise) lists that can be applied to threat intelligence or Internet Firewall rules

#### Q: What is the plan for advanced groups?

**A:** Advanced groups will gradually support more member types until they reach parity with existing groups, and new member types will also be added.

## Known Limitations for Advanced Groups

- Custom DNS and DHCP settings are only supported by groups

Alternative support to apply custom DNS and DHCP settings to advanced groups is on the roadmap

- Only groups support specifying sites for entity-based RBAC
