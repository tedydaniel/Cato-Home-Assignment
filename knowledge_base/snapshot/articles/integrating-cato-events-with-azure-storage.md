---
title: "Integrating Cato Events with Azure Storage"
slug: "integrating-cato-events-with-azure-storage"
updated: 2026-08-11T13:44:33Z
published: 2026-08-11T13:44:33Z
canonical: "knowledge.catonetworks.com/integrating-cato-events-with-azure-storage"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato Events with Azure Storage

This article explains how to integrate an Azure Storage account with your Cato account to upload events directly to a storage account.

## Overview of Events Integration

For customers who review and analyze event data in an Azure Storage account, you can configure your Cato account to automatically and continuously upload events to it. This is different from the [eventsFeed API](https://api.catonetworks.com/documentation/#query-eventsFeed), which requires customers to pull the data from Cato and is impacted by issues such as rate-limiting.

The Cato Cloud uploads data to the storage account as follows: every 60 seconds, or when there is more than 10MB of data. Cato uses HTTPS to upload data to the Azure Storage account.

The events are sent in a compressed .gz format, some clients (e.g. certain browsers) may automatically uncompress these files without removing the .gz extension. If this occurs, changing the file extension to .log or .txt will correctly align the file's format with its extension.

### Events Integration Use Case

Sample company is using the [IPS Suspicious Activity Monitoring feature](/v1/docs/monitoring-suspicious-activity-with-ips-sam) which generates a lot of security events. They decide to create an Azure Storage account to store all the event data, which they can then integrate with their SIEM solution. Sample company enables Events Integration and adds the Azure Storage account as an integration to their Cato account so that all the IPS events are automatically uploaded to the Azure Storage.

### Prerequisites

- Please review the prerequisites for all Cato event integrations in [Getting Started with Event Integrations](/v1/docs/getting-started-with-event-integrations)

## High-Level Overview of Azure Event Integration

1. Create new Azure Storage account and container.
2. Azure provides a connection string as follows:
  1. Access keys - connection string is automatically generated.
  2. SAS - configure the recommended permissions and settings, and then the connection string is generated.
3. Create the Azure integration in the Cato Management Application using the connection string from the previous step.

## Configuring the Azure Storage Account

Create a new storage account and container for the Cato event data, we recommend that you don't use an existing storage account for the Event Integration. You can use an Azure connection string from an access key or from a Shared access signature (SAS).

### Using Access Keys for the Connection String

For customers that are using Azure access keys to authenticate the storage account to Cato, copy the connection string. You will paste the access keys connection string in the Cato Management Application when you configure the Azure integration.

**To create a storage account that uses access keys:**

1. Create a new storage account with the appropriate settings.
  1. In the **Instance** details, select **Standard** performance.

![basic_storage_account.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34850872907933.png)
  2. Click **Review** and then click **Create**.
2. Create a new container for the event data (**Data storage > Containers**).

You will enter the container **Name** in the Cato Management Application when you create the integration for the events (below).
3. In the left-hand navigation pane, go to the **Security + networking** section and select **Access keys**.
4. Copy the access keys connection string for the storage account.

![access_key_string.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34850881357853.png)
5. Continue with [Adding Azure Storage Account for Events](/v1/docs/integrating-cato-events-with-azure-storage-account#adding-azure-account-storage-for-events) (below).

### Using SAS for the Connection String

Azure SAS lets you restrict permissions for the storage container, such as allowed IP addresses, and an expiration date for the connection string. For more information about Cato IP addresses, see this [article](/v1/docs/cma-ip-allowlist) (you must be signed in to view it).

The token for the SAS connection string includes an expiration date, which is shown on the Event Integration page. After the expiration date, the token is no longer valid, and Cato can't push events to the storage container. To maintain uninterrupted uploading of events, make sure to generate a new connection string and apply it to the integration before the SAS expiration date.

**To configure a storage account in Azure to receive Cato event data:**

1. Create a new storage account with the appropriate settings.
  1. In the **Instance** details, select **Standard** performance.

![basic_storage_account.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34850872907933.png)
  2. Click **Review** and then click **Create**.
2. Create a new container for the event data (**Data storage > Containers**).

You will enter the container **Name** in the Cato Management Application when you create the integration for the events (below).
3. In the left-hand navigation pane, go to the **Security + networking** section and select **Shared access signature**.
4. Configure the SAS with the following access permissions:

![SAS_settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34850873054877.png)
  - Allowed services - Blob, File
  - Allowed resource types - Container, Object
  - Allowed permissions - Read, Write, List
5. Click **Generate SAS and connection string**.
6. Copy the **Connection string** for the storage account. You will paste this string when you create the integration for the events (below).

![sas_string.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34850927140253.png)

## Adding Azure Storage Account for Events

Create a new integration for the Azure Storage account in the **Integrations** page, and paste the connection string into the integration. This string permits Cato to upload the event data to the storage account. You can't edit the string after creating the integration, instead you can **Reset** the field and then paste the connection string.

After you define and enable the Azure Storage integration, it takes a few minutes for Cato to start uploading events to the storage account.

You can choose to filter the events that are uploaded to the storage account. For example, only upload IPS events for your account to it. The default setting is no filter, and all events are uploaded to the storage account.

**To add an Azure Storage integration to upload events for your account:**

1. From the navigation menu, select **Resources > Integrations > Configured Integrations**.
2. Click **New**. The **New Integration** panel opens.
3. Select the integration type: **Azure Blob Storage.**
4. In **Integration**, select **Azure Storage Account** and enter the **Name** for the integration.
5. Enter these **Connection Details** for the integration based on the settings in Azure:
  - **Connection String** - Paste the connection string that you copied from the storage account
  - **Name** - Identical name of the container in the storage account
  - (Optional) **Folder** - Identical name for the folder path within the container (if necessary)
6. **(Optional)** Define the filter settings for events that are uploaded to the storage account.

When you define multiple filters, there is an AND relationship, and the events that match all filters are uploaded.
7. Click **Apply**. The Azure Storage account is now integrated with your account.

**Note:** You can define up to a total of three Event Integrations for your account.
