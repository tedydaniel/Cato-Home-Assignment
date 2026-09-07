---
title: "Decommissioning a Socket Site"
slug: "decommissioning-a-socket-site"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/decommissioning-a-socket-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Decommissioning a Socket Site

## Overview

This guide provides step-by-step instructions for properly decommissioning a Socket from an existing site. This process is essential when relocating a Socket to a different site or when a site is being decommissioned. Following these procedures ensures a smooth and proper decommissioning process, enabling the Socket to be reassigned or repurposed as needed.

## Environment

Decommissioning a Socket typically occurs in scenarios such as:

- Transferring a Socket from one site to another
- Shutting down a site permanently

**Note:** If a reseller intends to reuse a Socket for a different account, please follow the instructions below and reach out to support for further assistance.

## Procedure for Decommissioning a Socket from a Site

Follow these steps to decommission a Socket from a site:

1. Verify that the Socket appears as **Connected** or **Degraded** in the CMA. If the Socket has already been removed from the site, proceed with the next steps and additionally reset the Socket to default settings once it is powered back on. For more information on resetting a Socket, see [Managing Sockets](/v1/docs/managing-sockets).
2. Before proceeding with decommissioning, remove all dependencies associated with the site:
  1. Remove the site from any relevant groups.
  2. Remove the site from applicable policies, including firewall and network rules.
  3. Clear any other dependencies referencing the site.
3. Unassign the site license:
  1. Navigate to **Network > Site > Site configuration > General > License**.
  2. In the Allocate bandwidth section, set the license to **unassigned**.

![Socket_Unassign.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25354487906077.png)
4. Unassign the Socket from the site:
  1. Go to **Network > Site > Site Configuration > Socket.**
  2. Click on the **Actions** button and select **Unassign**.
  3. If the site is in High Availability, repeat this step for each Socket.

![Socket_Unassign_from_Site.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25354473843101.png)
5. Ensure that the Socket status is updated correctly:
  1. After a few minutes, the Socket should appear as **Installed** under **Account > Sockets & Accessories**. This status confirms that it has been successfully unregistered from the original site and is ready to be assigned to a new site.

![Socket_-_Installed.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25354488136477.png)
  2. If the Socket remains in **Delivered** status, it may need to be manually reset to default settings. For more information on resetting a Socket, see [Managing Sockets](/v1/docs/managing-sockets).
6. Delete the site from CMA to complete the decommissioning process:
  1. Navigate to **Network > Sites**.
  2. Select the site by checking the corresponding box.
  3. Click the **Actions** dropdown and choose **Delete**.
