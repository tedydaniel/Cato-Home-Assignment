---
title: "Managing Locations in the Enterprise Directory"
slug: "managing-locations-in-the-enterprise-directory"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/managing-locations-in-the-enterprise-directory"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Locations in the Enterprise Directory

The **Enterprise Directory** provides a central list of your organization’s locations and addresses. This lets you seamlessly manage address information for shipping locations when ordering Sockets and accessories, preventing mistakes and simplifying the management process.

## Overview

The Enterprise Directory displays all defined enterprise locations. Each location record includes key details such as **Name**, **Type**, and **Country**, along with optional address and recipient contact information. Currently, locations are used to manage shipping locations for sockets and hardware.

A **map component** at the top of the page displays all locations visually, providing an at-a-glance view of your organization’s geographic footprint. Admins can create, edit, archive, or import locations in bulk. The directory also supports search and filtering to help you find locations quickly.

After locations are created, they can be selected directly in the Shipping page.

## Creating or Editing an Individual Location

You can add or modify individual locations directly from the **Enterprise Directory** page. For locations in Brazil, a VAT ID is required. When using a location for shipping, all address and recipient fields are required.

1. From the navigation menu, select **Account > Enterprise Directory**.
2. Click **Add Location**.
3. Enter the fields for the location:
  - **Name** – A descriptive name for the location.
  - **Type** – Choose the location type (Branch, Headquarters, Data Center, Cloud Data Center, or Other)
  - **Country** – Select the country from the list.
4. (Optional) Add full address details: street, city, postal code, and region.
5. (Optional) Add recipient contact details (required if this location will be used for shipping).
6. Click **Save**.
7. To edit an existing location, click the location name in the list, make your changes, and click **Save** again.
8. To **archive** a location, click the **three dots (…)** at the end of the row and select **Archive**. Archived locations are hidden from active views but retained for record-keeping.

## Importing Locations in Bulk

You can quickly add multiple locations by importing them from a CSV file. The file must be in UTF-8 format and include the following columns:

- Name
- Type
- Country

If the locations will be used for shipping, include the full address and recipient contact columns as well. For locations in Brazil, a VAT ID is required.

To simplify the process, you can use the export button to download a blank CSV that includes the required columns. You can fill in the details for each location and then import the file back into the Enterprise Directory.

To import locations:

1. From the navigation menu, select **Account > Enterprise Directory**.
2. Click **Import**.
3. Select a properly formatted CSV file and upload it.
