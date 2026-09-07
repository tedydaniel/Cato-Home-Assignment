---
title: "Configure Attribute-based Dynamic User Groups"
slug: "configure-attribute-based-dynamic-user-groups"
status: "update"
updated: 2026-09-06T13:09:27Z
published: 2026-09-06T13:09:27Z
canonical: "knowledge.catonetworks.com/configure-attribute-based-dynamic-user-groups"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Attribute-based Dynamic User Groups

## Overview

Dynamic User Groups let you apply policies to users based on their directory attributes, without manually creating and maintaining user groups. When you enable a supported user attribute, Cato automatically creates a dynamic user group for each attribute value and keeps the membership up to date as user attributes change.

Currently, Cato supports dynamic user groups based on the **Department** attribute.

If a new Department value is assigned to at least one user in your identity provider (IdP), Cato detects it during the next user provisioning sync and automatically creates the corresponding Dynamic User Group.

### Use Case

Your organization needs separate access policies for the Engineering and Finance departments. Enable **Department** for Dynamic User Groups. Cato creates `Engineering (Dynamic)` and `Finance (Dynamic)` and adds the users with the corresponding department value.

When a user joins a department or changes departments, Cato updates the dynamic group membership. You can use the groups as user group criteria in supported policies without maintaining groups in your IdP.

## Understanding Dynamic User Groups

Cato creates a dynamic user group for every non-empty department value it discovers. Dynamic groups are shown on the User Groups page with the type `Dynamic`.

- The group name is `&lt;Department&gt; (Dynamic)`. For example, users in the Engineering department are added to `Engineering (Dynamic)`
- Dynamic groups are read-only. You cannot add or remove members manually
- Cato updates group membership during the applicable user provisioning sync
- Users with no department value aren't added to a dynamic group
- You can't disable an individual dynamic group. Disable **Department** to remove all department-based dynamic groups

## Configuring Dynamic User Groups

When you enable **Department**, Cato scans the existing users and creates a dynamic user group for each department value. For accounts with many department values, allow several minutes for the initial synchronization to complete.

To configure dynamic user groups:

1. From the navigation menu, select **Access > User Groups**.
2. Select the **Settings** tab.
3. Select **Department**.
4. Click **Save**.

## Understanding Group Lifecycle

When the last member leaves a department, Cato deletes the corresponding dynamic group. The deleted group remains visible in policy rules as deleted.

If a user receives the same department value within 10 days, Cato revives the group with the same identity and existing policy references continue to work. After the 10-day grace period, Cato creates a new group if that department value returns. Policies that referenced the old group don't automatically reference the new group.

## Using Dynamic User Groups in Policies

Dynamic user groups work like other user groups when you configure a policy. In a policy that supports user groups, select the required dynamic group as the user group criterion. For example, in an Internet Firewall rule, select a dynamic group under **Source**.

## Auditing and Events

Cato generates an audit entry when you enable or disable **Department** for Dynamic User Groups. Cato also generates events for dynamic group membership changes and group deletion.

#### Related Articles

- [Working with User and System Groups](https://knowledge.catonetworks.com/docs/working-with-user-and-system-groups)
- [LDAP Query Filters and Dynamic Groups](https://knowledge.catonetworks.com/docs/ldap-query-filters-and-dynamic-groups#configure-dynamic-groups)
