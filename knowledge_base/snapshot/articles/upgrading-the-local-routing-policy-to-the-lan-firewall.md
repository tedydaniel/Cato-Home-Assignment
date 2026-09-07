---
title: "Upgrading the Local Routing Policy to the LAN Firewall"
slug: "upgrading-the-local-routing-policy-to-the-lan-firewall"
updated: 2026-07-23T15:21:57Z
published: 2026-07-23T15:21:57Z
canonical: "knowledge.catonetworks.com/upgrading-the-local-routing-policy-to-the-lan-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrading the Local Routing Policy to the LAN Firewall

This article describes how to use the automatic migration tool to migrate the Local Routing rules for a site to the LAN Firewall policy.

## Overview

The LAN Firewall policy enhances the existing Local Routing capabilities that control the LAN communication between hosts and networks behind a Socket site. As part of the process to upgrade the Local Routing policy to the LAN Firewall, Cato automatically migrates the existing Local Routing rules to the LAN Firewall policy format. All the Local Routing functionality and settings are maintained after the migration without any further actions. For more about the LAN Firewall, see [Configuring the Socket LAN Firewall Policy](/v1/docs/configuring-the-socket-lan-firewall-policy).

No impact is expected during the migration process, however as a standard precaution, we recommend that you upgrade the policy during a maintenance window.

### Prerequisites

You can only use the migration tool for sites that meet the following requirements for the LAN Firewall:

- All Sockets in the site are running Socket version 18.0 or higher

The upgrade option is only available for sites that meet the prerequisites.

## Upgrading Local Routing Policy to the LAN Firewall Policy

When you start the process to upgrade Local Routing policy to the LAN firewall, the Cato Management Application automatically migrates all the rules to the new LAN Firewall format. When the migration is complete, the rules appear as follows:

- The **Local Routing** screen is now called **LAN Firewall**
- Rules keep the same priority, order, and rule name
- The **Protocols** and **Ports** for Local Routing rules are migrated to a single entity in the **Service/Port** in the LAN Firewall
- Local Routing rules with no defined **Protocol**, are assigned the value **Any** in the LAN Firewall
- The action is set to **Allow locally**

The following screenshot shows an example of the Local Routing policy (before the migration):

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247954492317.png)

This screenshot shows the LAN Firewall policy after the migration is completed:

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247954589853.png)

**To migrate the Local Routing rules to the LAN Firewall:**

1. From the navigation pane, select **Configuration > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Local Routing**.
3. Click **Upgrade to LAN FW**.
4. In the confirmation window, click **Confirm**. The rules are migrated to the LAN Firewall policy.

---

### FAQ

#### Q: Can the LAN Firewall policy be reverted to the Local Routing policy?

A: Yes. Please contact Support to revert back to the Local Routing Policy. You can only revert rules with the Allow locally action.
