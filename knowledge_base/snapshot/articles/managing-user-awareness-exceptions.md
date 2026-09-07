---
title: "Managing User Awareness Exceptions"
slug: "managing-user-awareness-exceptions"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/managing-user-awareness-exceptions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing User Awareness Exceptions

This article discusses how to create rules to identify users that are temporarily an exception to being identified by User Awareness.

## Creating Rules for Exceptions

You can create temporary exceptions (rules that bind a specific IP and an SDP user) to handle cases where the Cato Cloud could not identify the user or has incorrectly identified a Directory Services user.

The Cato Cloud automatically disables exception rules (without deleting them) when their expiration date is reached. You can configure your account to delete expired exception rules after a certain number of days.

When a rule is disabled, the SDP user is no longer bound to the IP address.

**To create a rule for User Awareness Exceptions:**

1. From the navigation menu, select **Access > User Awareness**.
2. From the **User Awareness Exceptions** section or tab, click **New**.

The **Add** exception panel opens.
3. Click the slider to ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218203301149.png)**Enabled**.
4. In **What**, click ![Domain_plus.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218247971741.png) and enter one or more IP addresses of the user that have an invalid association.
5. In **Statically bind to**, select or search the Directory Service user you want to map the IP address to.
6. In **Expire in**, enter the number of days in which the exception rule expires.
7. Click **Apply** and then click **Save**.

## Configuring a Rule to Delete Automatically

**To automatically delete exception rules when they expire:**

1. From the navigation menu, select **Access > User Awareness**.
2. In **User Awareness Exceptions** section or tab, click **Automatically delete expired exceptions after**.
3. Enter the number of days after expiry that the rule will be deleted.
4. Click **Save**.
