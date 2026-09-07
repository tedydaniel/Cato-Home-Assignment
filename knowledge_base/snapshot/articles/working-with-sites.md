---
title: "Working with Sites"
slug: "working-with-sites"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/working-with-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Sites

This article explains how to work with the **Network > Sites** page. This page includes two sections:

- Sites Overview
- Reviewing Site Data

## Understanding the Sites Overview

![sites_overview_widget.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247778015517.png)

The Sites Overview includes three widgets with the following information:

- **Site Connectivity Status** – the total number of sites and the statuses (connected, disconnected, degraded, and disabled)
- **Connection Types** – shows the distribution of site connection types in your account (e.g., Socket X1500, IPSec IKEv2, vSocket AWS)
- **Socket versions** – shows the distribution of the Socket versions running in the account. This widget presents information only for Sockets and Virtual Sockets sites

## Reviewing Site Data

![sites-table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247798225693.png)

You can use the Sites page to manage the sites in your account and it summarizes a variety of real-time information about the sites. In addition, you can add new sites, edit or delete sites, and other actions.

**Filtering the Sites Page**

You can filter sites based on their **Connectivity Status**, **Connection Types** or **Socket Version**. To apply filters, you can select applicable filters from the drop-down options or by hovering the Sites Overview and selecting the filter ![filtericon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247766323741.png) icon. Filters are then applied to both the Sites Overview and Sites Table.

Click the X remove icon to clear a filter.

These are the default columns that are shown for sites:

- **Site** - Name of the site
- **Connection Type** – The connection type of the site (e.g., Socket X1500, IPSec IKEv2, vSocket AWS)
- **License Status** – Shows the license status for the site
- **Connectivity Status** – Connected, Degraded, Disconnected, Disabled
- **PoP** – Shows the name of the PoP that the site is connected to. If the site is disconnected, the field will show the name of the last connected PoP for the site. If the site was never connected before to a PoP, the field remains empty
- **HA Status** – Shows the High-Availability status of the site
- **Version** – Socket version
- **Country** – Configured country for the site
- **ALT. WAN** – Shows the connectivity status of the Alt WAN links
- **Public Site IP Address** - For IPsec sites, shows the public IP address for the primary and secondary tunnel

## Understanding the Actions

- **New** – Add new site
- **Export** – Export the Site table’s content to a CSV file
- **Actions** drop-down menu – You can apply an action to one or more sites. Select one or more sites, click **Actions**, and select one of the following options:
  - **Reconnect to Preferred PoP** – When the site fails to meet the acceptable SLA thresholds with the currently connected PoP, it can move to a different PoP location. You can use the Reconnect to Preferred PoP action to force the site to move back (reconnect) to the original preferred PoP
  - **Connect to Primary/Secondary Socket** - Connect to the primary or secondary Socket WebUI
  - **Enable** – Enable a disabled site
  - **Disable** – Disable an enabled site. A disabled site cannot connect to the Cato Cloud. However, it still appears in the relevant references and entries in the Cato Management Application, such as security rules

**Note:** After you disable a site in the Cato Management Application, it takes a few minutes for the PoPs in the Cato Cloud to disable the tunnels to the site. After you disable the site, wait until the Cato Management Application shows that the status of the site is disabled before configuring any other settings for the site.
  - **Delete** – Delete an existing site. You must clear the dependencies before deleting a site (e.g. remove the site from relevant groups or policies)
