---
title: "Working with Policy Revisions"
slug: "working-with-policy-revisions"
updated: 2026-07-13T16:41:37Z
published: 2026-07-13T16:41:37Z
canonical: "knowledge.catonetworks.com/working-with-policy-revisions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Policy Revisions

This article explains how to edit and publish policies that use revisions, and also how multiple admins can edit a policy in parallel.

## Overview

Many Cato features are managed through policies that consist of granular rules. Policies support unpublished revisions, allowing admins to work on changes without affecting the published policy until the changes are published.

Some policies support **multiple unpublished revisions per admin**. Each admin can maintain multiple independent drafts of the same policy. This allows multiple policy efforts to be conducted in parallel, with full control over when to publish each change.

Some policies have legacy restrictions: they support only one unpublished revision, and when working on an unpublished revision, an admin cannot view the active policy. When a draft exists, admins edit the draft rather than the published version. If no draft exists, admins see the published version.

You can edit a policy and save the changes in your own private unpublished revision. This revision is saved even if you log out of the Cato Management Application, and you can continue editing the policy in your next session. Once all the changes have been made, the policy can be published to your account (becoming the published revision).

## Creating a New Policy Revision

There are two ways to create a new policy revision: with the Create new revision button or by editing an active policy.

**To create a new revision using the Create New Revision button:**

1. From the dropdown list at the top of the page, select **Create New Revision**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(56).png)

The new revision pane opens. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(58).png)
2. Enter the relevant details and select **Apply**.

A banner appears confirming the new revision has been created, and the unpublished revision is opened for editing: ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(59).png)
3. Make any edits required and publish as necessary to make this the active policy.

**To create a new revision by editing the active policy:**

1. Edit any aspect of an active policy (for example, add/delete/move a rule or subsection) and select **Create new revision**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(60).png)

The new unpublished revision will be created and given a default name.
2. Optionally, rename the revision and enter a description for it (see [Customising Names and Descriptions of Unpublished Revisions](/v1/docs/working-with-policy-revisions#customising-names-and-descriptions-of-unpublished-revisions), below).

## Customising Names and Descriptions of Unpublished Revisions

For clarity when working on multiple unpublished revisions, it’s helpful to name them appropriately and include descriptions of each.

The revisions menu offers a three-dot context menu for renaming and adding descriptions to your unpublished revisions.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(61).png)

## Policy Revisions and Concurrent Editing by Multiple Admins

Different admins can edit the published revision in parallel however no other admin can access your unpublished revision. Rules saved in an unpublished revision are locked for editing by other admins until the revision is published or discarded.

Until changes are published, they have no impact on the account policy and remain available for you to edit. For example:

- Admin A edits and saves rule 1 to their unpublished revision
- Admin B edits and publishes rule 2 (rule 1 is locked)
- The changes made by admin A to rule 1 are not published until admin A publishes them

For a detailed explanation of how to configure rules for each policy, see the documentation for that policy.

### Understanding Unpublished Revisions

An unpublished revision is a version of a policy that has been saved, but not published.

![Unpublished_Revision.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468560051613.png)

When you save changes to an unpublished revision, the following indicators appear on the page:

- For the admin editing the revision, the ![Edit_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468572648989.png) icon indicates the rules that are currently being edited, and the changes are part of an unpublished revision
- The ![Lock_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468567558941.png) icon indicates rules that are locked for editing by a different admin
  - When editing a rule is defined with a rule order (**Position**) relative to a different rule, then both rules are locked for other admins. For example, if you assign a rule position to be before rule 5, then rules 4 and rule 5 are locked for other admins. For more about locked rules, see [Overriding the Lock for a Rule](/v1/docs/working-with-policy-revisions#overriding-the-lock-for-a-rule).
- The label **Unpublished Revision** appears above the rulebase
- The number of rules with changes appears on the **Publish** button

After saving changes to rules, you can **Discard** or **Publish** your unpublished revision. This is what happens for each of these actions:

- **Discard** - All changes are discarded, and the unpublished revision is no longer accessible

> [!NOTE]
> Note:
> 
> The **Discard** action can't be undone.
- **Publish** - All changes in the unpublished revision are applied to the account policy and appear in the published revision, as well as in the unpublished revisions of other admins

> [!NOTE]
> Note:
> 
> The **Publish** action can't be undone.

Additionally, after you **Discard** or **Publish** a revision:

- Rules are no longer locked for other admins
- The page shows the published revision of the policy

### Locked Rules

When you save changes to rules in an unpublished revision, those rules are locked to prevent editing by other admins. If you are required to edit a locked rule, you can hover over the lock to see which admin locked the rule, and contact them so they can discard or publish their revision and unlock the rule. In cases where the admin can't be contacted, it's possible to override the lock and then edit the rule. When you override the lock, you discard the other admin's entire unpublished revision, including changes for all rules, and those changes can't be retrieved. The other admin sees the published revision the next time they log in.

> [!NOTE]
> Note:
> 
> You can only override a lock on a rule from your unpublished revision, not from the published revision. This means at least one other change has to be saved to your revision before you can override the lock on a rule.

## Editing Policy Revisions

This section describes workflows for editing a policy in the following use cases:

- When the policy isn't being edited by any other admin and no rules are locked
- When another admin is concurrently editing rules, and they are locked

### Editing a Policy with No Locked Rules

When no other admin has saved changes to their private revision, you can edit rules with no restrictions, save the changes to your private revision, and then publish them to the account policy (the published revision).

The example below is from the Internet Firewall policy.

![Internet_Firewall_Revisions_no_lock.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468567597981.png)

**To edit a policy with no locked rules:**

1. From the navigation menu, navigate to the policy page.

The policy page opens to your existing unpublished revision, or to the newest published revision.
2. Edit a rule.
3. Click **Apply**. The new rule is added to the rulebase.
4. Click **Save** then **Publish**.
5. In the **Publish Revision** confirmation window, click **Publish**. Your revision is applied to the account policy.

### Editing a Policy that Includes Locked Rules

When you are required to edit a policy including making changes to locked rules, you can override locks to edit the rules, save the changes to your private revision, and then publish them to the account policy.

![Internet_Firewall_Revisions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468560235421.png)

**To edit a policy including locked rules:**

1. From the navigation menu, navigate to the policy page.

The policy page opens to your existing unpublished revision, or to the newest published revision.
2. Create or edit rules. For more information, see the documentation for the policy.
  - For a locked rule, see [Overriding the Lock for a Rule](/v1/docs/working-with-policy-revisions#overriding-the-lock-for-a-rule) below.
3. Click **Apply**. The new rule is added to the rulebase.
4. Click **Save**.

The changes are saved to your unpublished revision.
5. Click **Publish**.
6. In the **Publish Revision** confirmation window, click **Publish**. Your revision is applied to the account policy.

#### Overriding the Lock for a Rule

Hovering over a locked rule displays the name of the admin who locked the rule and the length of time the rule has been locked. Before overriding a locked rule, we recommend coordinating your changes with the admin who locked the rule.

You can only override a lock on a rule from your unpublished revision, not from the published revision. This means at least one other change has to be saved to your revision before you can override the lock on a rule. Overriding the lock for a rule discards the other admin's entire unpublished revision, and can't be undone.

**Note:** Overriding the lock for a rule discards the other admin's entire unpublished revision, and can't be undone.

**To override the lock for a rule:**

1. Hover the mouse over the lock icon in the row of the rule you want to edit. A window shows the information about the rule's edit history.
2. Click **Override Lock**.

**Note:** Overriding the lock for a rule discards the other admin's entire unpublished revision, and can't be undone.
3. In the confirmation window, click **Override and Discard**. The other admin's unpublished revision is discarded, and the rule is unlocked for editing.

## Publishing Unpublished Revisions

Publish your unpublished revision, and apply the changes to the policy.

**To publish an unpublished revision:**

1. From the navigation menu, navigate to the policy page.

The policy page opens to your existing unpublished revision.
2. Click **Publish**.
3. In the **Publish Revision** confirmation window, click **Publish**. Your revision is applied to the account policy.

## Discarding an Unpublished Revision

Discard your unpublished changes and revert to showing the published account policy.

**To discard your unpublished revision:**

1. From the navigation menu, navigate to the policy page.

The policy page opens to your existing unpublished revision.
2. Click **Discard**.
3. In the **Discard Revision** confirmation window, click **Discard**. Your revision is discarded, and the page shows the published policy.
