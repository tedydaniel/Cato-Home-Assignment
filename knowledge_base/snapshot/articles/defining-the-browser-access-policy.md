---
title: "Defining the Browser Access Policy"
slug: "defining-the-browser-access-policy"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/defining-the-browser-access-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining the Browser Access Policy

## Overview of Browser Access Policy

The Browser Access policy gives you granular control over which users in your account can access the different Browser Access applications. The Browser Access policy isn't ordered, and all the rules are applied for the traffic.

After you create the Browser Access applications, create the access rules to allow the users to connect to them. For example, the screenshot below shows a rule that only allows the finance department to access the SAP database.

![Browser_Access_Applications.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218293018781.png)

## Creating a Browser Access Policy Rule

Create a new access rule for the Browser Access Portal and define the users that can access the specific applications in that rule. These are the users and groups you can define for a rule:

- **System Group** and **Group** - Any system or manual group that you created in **Assets > Groups**
- **User** - LDAP groups and users that are added to your account from an AD server in **Access > Directory Services**
- **SDP Users** - Individual users that are connecting to the portal with the email address in **Access > Users >** <user name> **> General**

**To create a new access rule for the Browser Access Portal:**

1. From the navigation menu, click **Access > Applications Portal**.
2. From the **Access Policy** tab or section, click **New**.

The **Add Access Policy Rule** panel opens.
3. In **Rule Name**, enter a name for the access rule.
4. Add the users and groups that can access the applications in this rule:
  1. Expand the **Users/Groups** section.
  2. From the drop-down menu, select the individual users or groups that can access the applications.
  3. Repeat the previous step for additional users or groups for this rule.
5. Select one or more applications for this rule:
  1. Expand **Remote Access Applications**.
  2. In the drop-down menu, select the application.
  3. Repeat the previous step for additional applications.
  4. Click **Apply**.
6. The right-most column ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218293093021.png) lets you enable or disable an SDP access rule.

When a rule is disabled, it is grayed out.
7. Click **Save**. The Browser Access rule is added to the access policy.

## Deleting an Browser Access Rule

Delete an access rule that is no longer being used. You can't undo deleting a rule.

**To delete a Browser Access rule:**

1. From the right-hand column for a rule, click the more icon ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218293093021.png) and select **Delete**.
2. Click **Save**.

The Browser Access policy rule is deleted.
