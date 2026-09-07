---
title: "Working with Mailing Lists"
slug: "working-with-mailing-lists"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/working-with-mailing-lists"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Mailing Lists

This article discusses how to manage the mailing lists that determine who receives email notifications from the Cato Management Application.

## Overview of Mailing Lists

You can create email alerts and notifications in a variety of screens in the Cato Management Application, for example for firewall rules, or block actions with the Anti-Malware services. The mailing list determines who receives the alert or notification that the Cato Management Application sends out.

In the **Mailing Lists** screen, you can create new mailing lists to define the recipients of these alerts or notifications. There is a predefined list that contains all admins defined in the Cato Management Application. In addition, you can create new mailing lists with specific admins and/or external email addresses.

> [!NOTE]
> Note:
> 
> By default, all emails are sent with recipients in **bcc**. This means that all email addresses in the BCC field are hidden from recipients, including their own. If your organization requires recipients to appear in the ​**To**​ field instead, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new)​​.

![MailingLists.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24198370629661.png)

## Creating a New Mailing List

You can create new mailing lists on the **Mailing List** page. In addition, you can also create new mailing lists on other pages where you configure alerts and notifications.

**To create a new mailing list:**

1. From the navigation pane, click **Account > Subscriptions > Mailing Lists**.
2. Click **New**. The **Create List** panel opens.
3. Enter the **Name** for the mailing list.
4. Add the **Members** of this mailing list.
  1. To add admins for the Cato Management Application:
    1. In the **Edit Members** window, in the **Admins** tab select the Cato Management Application Admins you are adding to this mailing list.
    2. From the drop-down menu, select **Administrator**.
    3. Enter or select the Cato Management Application admins for this list.
  2. To add external users to this email list:
    1. From the drop-down menu, select **Non Admin Email**.
    2. Enter the email address for the external user.
    3. Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24198378500381.png) (Add).
    4. Repeat the previous two steps for each user.
5. Click **Apply**. The mailing list is added to the window.
6. Click **Save**.
