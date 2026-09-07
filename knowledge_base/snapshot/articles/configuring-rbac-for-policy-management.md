---
title: "Configuring RBAC for Policy Management"
slug: "configuring-rbac-for-policy-management"
updated: 2026-08-23T12:47:27Z
published: 2026-08-23T12:47:27Z
canonical: "knowledge.catonetworks.com/configuring-rbac-for-policy-management"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring RBAC for Policy Management

## Overview

Cato Management Application (CMA) roles implement [RBAC](/v1/docs/what-are-admins-and-role-based-access-control-rbac) to define view and edit permissions for CMA pages. Sub-policies let you assign RBAC for a set of rules to give admins autonomy over the areas they’re responsible for, while preserving centralized control and security boundaries.

Create **sub-policies** for specific rules and define which admins have view or edit access to those sub-policies.

### Use Case

Sample company has 2 SOC teams, one for EMEA and one for APJ. There are 50 rules in the Internet Firewall policy: 20 apply to all regions, 10 are only related to EMEA traffic, and 20 are only for APJ traffic. Before sub-policies, the SOC teams had permissions to view and edit all the rules in the Internet Firewall policy, which did not meet the company's compliance regulations.

Sample company used sub-policies to restrict access, so each SOC team only had access to rules that manage traffic for their region. They created an EMEA sub-policy for the 10 rules for EMEA traffic, and an APJ one for the 20 rules for APJ traffic. Now, the SOC teams can only edit the rules for their regional traffic, and the company is fully compliant with the regulations.

## Working with Sub-policies

- The parent rule of the sub-policy is a scoping rule that defines when the rules in the sub-policy are applied to the traffic
- The sub-policy rules are also ordered rules, and the action of the first matching rule is applied to the traffic
- You can add sections for rules in the sub-policies
- By default, an optional ANY ANY cleanup rule is added at the end of the sub-policy. This rule is only applied to:

**Note:** Rules inside a sub-policy that have ANY conditions are only applied to the traffic that also matches the scoping rule of the sub-policy. That means that a rule with ANY ANY Block, doesn't impact traffic that does NOT match the scoping rule.
  - Traffic that matches the scoping rule for the sub-policy
  - Doesn't match any other rule in that sub-policy
- Sub-policies cannot contain other sub-policies (no nesting)

Any rules not included in a sub-policy are part of the **main** sub-policy when defining admin permissions.

You can define which admins can view/edit each sub-policy.

## Creating a Sub-policy and Defining Admin Permissions

First, create sub-policies and then define admin permissions for who is allowed to view or edit the rules.

Rule numbers stay consistent across the entire policy, even when some admins cannot view certain sub-policies. As a result, admins without view permissions for specific sub-policies may see gaps in the rule numbering.

![sub-policy_settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32724684645405.png)

### Creating a Sub-policy

You can create a sub-policy in any of the supported policies. The conditions of the sub-policy define when traffic will be applied to the rules inside a sub-policy.

**Note:** Make sure you define rules and permissions before you enable the sub-policy.

**To create a sub-policy:**

1. In the relevant policy, click **New > Sub-Policy**.
2. Define the name, position, and conditions for the sub-policy and click **Save**.

### Defining Admin Permissions for Sub-Policies

By default, admins have permissions to view and edit all sub-policies on every page that they have permissions for. Remove permissions for the entity for all the sub-policies and add it back for the new individual sub-policy.

![sub-policy-assign.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32724714811677.png)

**To define admin permissions on a sub-policy:**

1. From the navigation menu, select **Administration > Admins**.
2. Select an admin, and go to the **Access Permissions for Entities** area.
3. In the table, locate the line for the policy (e.g., **All Internet Firewall Policies**) and remove view and edit permissions.
4. In the drop-down, select the sub-policy category for your page (e.g., **Internet Firewall Sub-Policies**).
5. In the second drop-down, select the target sub-policy. The sub-policy is added to the table.
6. In the table, give the admin **Edit** or **View Only** permissions for the sub-policy.
7. Repeat this process for every admin.
8. After the admin permissions are defined, they can start configuring rules for the sub-policy.

### Enabling Sub-Policies

After rules have been defined in the sub-policy, you can enable it.

![sub-policy-enable.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32724714938269.png)

**To enable a sub-policy:**

1. In the target policy, click the sub-policy.
2. Expand the **General** section and use the toggle to **enable** it.

## Limitations

- The following policies support sub-policies and RBAC for policy management:
  - Internet Firewall
  - WAN Firewall
  - LAN Firewall
  - TLS Inspection
