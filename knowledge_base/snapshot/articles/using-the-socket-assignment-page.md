---
title: "Using the Socket Assignment Page"
slug: "using-the-socket-assignment-page"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/using-the-socket-assignment-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Socket Assignment Page

This article discusses the Socket Assignment tab in the Sockets & Accessories page, which shows information about all the Sockets ordered for and connected to your account.

## View Sockets in your Account

The Socket Assignment tab shows information about Sockets that you ordered, or already connected to your account.

**To show the Sockets Assignment tab:**

- From the navigation panel, click **Account > Sockets & Accessories** and click the **Socket Assignment** tab.

![Socket_accessories.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35403676815901(1).png)

## Understanding the Socket Assignment Page

The summary bar at the top of the page shows the Socket types and hardware models in your account. For example, you can see how many X1700 Sockets you have, and how many of each hardware model, such as X1700A and X1700B. This helps you quickly review your Socket inventory and understand whether any hardware requires a [refresh](/v1/docs/cato-socket-hardware-refresh-policy).

These are the explanations of the columns in the Sockets & Accessories page:

- **Status** - Status of the Socket as follows:
  - **Ordered** - Cato received the order for the Socket
  - **Shipped** - Cato shipped the order to the physical site
  - **Delivered** - Socket was successfully delivered to the physical site
  - **Installed** - Socket is installed and connected to the Cato Cloud, but is not yet assigned to a site
  - **Connected** - Socket is connected to the site
- **Sites** - Site name or **Assign to a Site** if the Socket is not yet assigned to a site
- **Type** - Socket model (for example, X1500)
- **Hardware Version** - The Socket model, including the specific hardware version (for example, X1500B or X1500A)
- **Version** - Socket OS version installed on the Socket
- **Serial Number** - Socket serial number (S/N)
- **MAC Address** - Socket MAC address (only for X1500 Sockets)
- **Shipping Date** - Date that Cato shipped the Socket
- **Carrier** - Shipping carrier that is transporting the Socket (for example, FedEx or DHL)
- **Delivery Form Site Name** - Office name on the delivery form for the Socket

This column is hidden by default
- **Description** - Displays the socket description you define in the Site > Site Configuration > Socket page in the Socket Configuration field

This column is hidden by default

## Unassigning Sockets from Sites

On the Sockets & Accessories page, you can unassign Sockets to sites.

After you unassign a Socket, we recommend that you wait at least 5 minutes before disconnecting the Socket or its connections to the network. This lets the Socket complete the unassign process.

**To unassign a Socket from a site:**

1. From the navigation menu, click **Account > Sockets & Accessories**.
2. Click the three dots to the right of any Socket.
3. Select one of the following options:
  - **Unassign:** Unassign a Socket from a site

## Managing Socket Automatic Upgrade

By default, Sockets are [automatically upgraded](/v1/docs/understanding-cato-s-managed-socket-upgrade-service) to the newest version as part of the Cato platform. However, in some scenarios, you might want to skip an upgrade. For your convenience, you can quickly pause or resume upgrades on a Socket directly on the Sockets & Accessories page. You can also manage this setting as follows:

- For a single Socket: Network > Sites > [site name] > Site Configuration > Socket
- For multiple Sockets (bulk upgrade): Network > Sites

After [manually upgrading](/v1/docs/manually-upgrading-a-socket) to the newest version, the Socket resumes the automatic upgrade process.

**To pause or resume upgrades for a Socket from a site:**

1. From the navigation menu, click **Account > Sockets & Accessories**.
2. Click the three dots to the right of any Socket.
3. Select one of the following options:
  - **Upgrade:** For a Socket that was paused, manually upgrade to the newest version right now
  - **Pause Automatic Upgrades:** Exclude this Socket from automatically upgrading to the newest version
