---
title: "Integrating Custom IoC Lists with Containers"
slug: "integrating-custom-ioc-lists-with-containers"
updated: 2026-06-30T08:49:42Z
published: 2026-06-30T08:49:42Z
canonical: "knowledge.catonetworks.com/integrating-custom-ioc-lists-with-containers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Custom IoC Lists with Containers

This article discusses how to use Container objects to integrate custom lists of IoCs with Cato Security services.

## Overview

You can add custom IoC lists to the threat intelligence for your Cato account to meet specific requirements for your organization's industry or location. The IoC lists are configured using Containers, which are user-defined categories that help you manage groups of items such as IP addresses or FQDNs. For example, create a Container that includes a list of malicious IP addresses identified by your organization's SOC or provided by a third-party threat intelligence service.

You can configure Containers with IoC lists directly in the Cato Management Application or through automated API processes, and then include the Containers in Internet Firewall rules. For more information about the API for Containers, see the [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/#definition-Container).

There are different types of Containers, and each type can include only a single type of data. These are the Container types:

- IP - Can include single IP addresses, subnet masks (in dot-decimal or CIDR notation), and IP ranges
- FQDN - Fully qualified domain names, for example: www.shop.example.com

This is an example workflow for integrating custom IoCs using a Container:

1. Configure a Container including the IPs identified as IoCs.
2. Create Internet Firewall rules with the Container configured in the **App/Category** field, and set the rule with the **Block** action.
3. Keep the Container updated by uploading a new list of IoCs to the Container. When you update the container, the firewall rule automatically enforces the new IoCs.

## Working with Containers

You can create a Container on the **Categories** page by:

- Syncing a file from a URL
- Uploading a source file with the data for the Container
- Adding an item manually

After you create a Container, it appears in the table in the Containers tab. You can edit a Container in the table manually or upload a new source file to update the values in the Container.

### Syncing IoCs from a URL

![Ioc.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32702399043357.png)

IoCs can be uploaded directly from a URL, allowing you to automatically ingest external threat feeds or frequently updated indicator lists. This enables faster threat response times with regular automated updates and ensures accuracy with reduced human error. You can configure how often these IoCs sync using either hourly or daily intervals.

If a sync fails, it is automatically retried three times within 15 minutes before a notification is sent. It then continues attempting to sync up to seven additional times over the next hour. You can view the current sync status using the indicator shown in the **Containers** table in the **Members** column.

![Sync_sucessful.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32702399060381.png)

You can also manually trigger a sync from the URL on the **Container** table by selecting the three dots next to the relevant Container and clicking **Sync Now**.

### Uploading IoCs from a File

![Container_-_New.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32702425207453.png)

IoCs can be uploaded from a file allowing you to create a Container of IoCs in bulk. The Container can be of type FQDN or IP. An IP Container can include a list of single IP addresses, subnet masks (in dot-decimal or CIDR notation), or IP ranges.

**Requirements for Container Source Files**

- Source files for Containers must be in one of the following formats:
  - TXT files with values separated by one of the following delimiters:
    - Comma
    - Space
    - Line break
  - CSV files with values listed in column A with no header
  - STIX format JSON files
- Source files must contain a minimum of 1 value and a maximum of 1 million values
- For FQDN Containers, only alphabetic or numeric characters are supported, special characters are not supported

#### Creating a Container

Create a container that contains IoC from a file, URL, or manually.

**To create a Container:**

1. From the navigation panel, select **Resources > Categories** and expand the **Containers** tab.
2. Click **New**. The **New Container** panel opens.
3. Enter the **Display Name** for the Container.
4. Select the container **Type**. Possible values: **FQDN**, **IP**.
5. Enter a **Description** for the Container.
6. Choose the **Source** for the Container by either:
  - Uploading a file
    - Choose the File type (CSV or STIX) and add the file by either dragging and dropping it into the File Uploader or clicking Browse **Note:** To upload a TXT file, select the CSV option.
  - Syncing a file from a URL
    - Choose the File type (CSV or STIX), add the URL, and choose the intervals for the file to sync.

**Note**: Click **Test Container** before saving the Container
  - Adding items manually
7. Choose tracking options. For more information, see [Alerts](/v1/docs/notifications).
8. Click **Save**. The Container is created and visible in the Containers table.

### Updating Containers

Update the values in a Container by uploading a new source file or making manual updates. When you upload a new source file, it replaces the existing file and only the values in the new source file are included in the Container.

**To update a Container:**

1. From the navigation panel, select **Resources > Categories** and expand the **Containers** tab.
2. Click ![edit_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32702413898269.png) in the row of a container. The **Edit Container** panel opens.
3. Under **Source**, drag and drop or browse to upload a file with the values to include in the Container or make manual changes.
4. Click **Save**. The Container is updated and contains the values in the new source file.

## Using Containers in Internet Firewall Rules

Configure Containers in the **App/Category** field in an Internet Firewall rule. Select the Container type and then select the specific containers to include in the rule. You can configure multiple Containers of the same type in a rule.

![Container_-_FW_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32702413915421.png)

**To configure a Container in an Internet Firewall rule:**

1. From the navigation menu, select **Security > Internet Firewall**.

The Internet Firewall page opens to your existing unpublished revision, or to the newest published revision.
2. Click **New**.
3. Under App/Category select either **FQDN Container** or **IP Container**.
4. Select one or more containers from the drop-down menu.
5. Configure the other fields of the rule and save the rule. For more information about configuring Internet Firewall rules, see [Managing the Internet Firewall Policy](/v1/docs/managing-the-internet-firewall-policy).
