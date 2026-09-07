---
title: "Azure Blob Storage: Configuring the Forensic Storage Connector"
slug: "azure-blob-storage-configuring-the-forensic-storage-connector"
updated: 2026-07-26T11:34:15Z
published: 2026-07-26T11:34:15Z
canonical: "knowledge.catonetworks.com/azure-blob-storage-configuring-the-forensic-storage-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Blob Storage: Configuring the Forensic Storage Connector

## Overview

To minimize data exposure and ensure compliance with regulatory requirements, you can create an integration with a third party for the storage of the evidence files.

This is supported for storing data from DLP policy violations. For more information, see [Investigating DLP Violations with Forensic Evidence](/v1/docs/investigating-dlp-violations-with-forensic-evidence).

To configure the integration, you need to:

1. Configure the integration storage application
2. Create the API connector in the CMA

## Configuring the Azure Blob Storage Integration

To configure the Azure Blob Storage integration, create the required configurations in your Azure account, then configure the connector within the CMA.

### Step 1: Configure the Integration in Azure

To configure the Azure Blob Storage integration, create a storage account and container.

**To configure the integration in Azure:**

1. In your [Azure portal](https://portal.azure.com/), navigate to **Storage accounts**.
2. To integrate forensic evidence with an existing Storage account, click on that account and go to step 4. To create a new Storage account, click **Create**.
3. Create a Storage account. For more information, see the [Microsoft Documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create).
4. In the navigation pane for the storage account, navigate to **Data storage > Containers**.
5. Click **+ Container**.
6. Create the Container. For more information, see the [Microsoft Documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/blob-containers-portal).
7. Copy and save the Container name so it can be entered into the CMA.
8. In the Storage Account, navigate to **Security + networking > Access keys.**
9. Copy and save the **Connection string** so it can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. In the **SaaS Application** dropdown, select **Azure Blob Storage**.
5. Choose **Forensics Evidence** and in the **Auth** drop-down, choose **API key**.
6. Add these configurations:
  - **Name:** Choose a name for the integration
  - **API Key**: The **Connection string**
  - **Container Name:** The name of the container you created in Step 1
  - **Folder Path:** Choose a folder path, the folder is automatically created
  - **Permissions:** Read/Write
  - Choose whether you want to track errors by creating an event
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.
