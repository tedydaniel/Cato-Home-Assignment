---
title: "Creating Subscription Groups"
slug: "creating-subscription-groups"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/creating-subscription-groups"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Subscription Groups

Subscription Groups are logical entities that you can use as the destinations for alerts and notifications that you enable in the Cato Management Application. This article discusses how to create Subscription Groups that contain members for Mailing Lists and integrations (such as Webhooks or ServiceNow).

## Overview

Subscription Groups can be re-used in different alerts and notifications based on the requirements of your organization. After you define Mailing Lists and Webhooks, you can add them as members to a Subscription Group. When you edit the members of a Subscription Group, the relevant alerts are automatically updated to send the alerts to the members in the Subscription Group.

## Creating Subscription Groups

Use the Subscription Groups tab in the Subscription page to create new Subscription Groups and manage them.

![subscription_groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24198360371869.png)

**To create a new Subscription Group:**

1. From the navigation menu, click **Account > Subscriptions** and select the **Subscription Groups** tab.
2. Click **New**. The **New Subscription Group** panel opens.
3. Enter the **Name** of the Subscription Group.
4. Define the members of the Subscription Group:
  1. In **Select members from**, select **Mailing List** or **Webhook**.
  2. In the **Mailing List** or **Webhook** drop-down menu, select the item your are adding to the Subscription Group.
  3. Repeat the previous two steps for all the members of the Subscription Group.
5. Click **Save**. The Subscription Group is added to the page.

## Defining Policy Notifications with Subscription Groups

Cato Security policies let you send notifications when a rule is matched. You can configure the **Track** settings to send notifications to a Subscription Group that contains the Mailing Lists and other integrations.

**To define a Subscription Group notification for a rule:**

1. In the relevant policy, edit the rule and expand the **Actions** section.
2. Select **Send Notification**.
3. Define the **Frequency** for how often the alert is sent.
4. In **Send notification to**, select **Subscription Group** and select the relevant item.
5. Click **Apply**.
