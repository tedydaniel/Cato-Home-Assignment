---
title: "Copying the Azure vSocket VHD Image with SAS"
slug: "copying-the-azure-vsocket-vhd-image-with-sas"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/copying-the-azure-vsocket-vhd-image-with-sas"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Copying the Azure vSocket VHD Image with SAS

This article explains how to get the vSocket image and scripts to deploy a single and high availability (HA) vSocket.

For more information about Azure vSockets, see:

- [Deploying an Azure vSocket Site Manually](/v1/docs/deploying-an-azure-vsocket-site-manually)
- [Configuring HA for Azure vSockets](/v1/docs/configuring-ha-for-azure-vsockets)

## Creating the Azure Blob Storage and Container

You can copy the vSocket VHD image to an existing Azure blob storage and container. Otherwise, create a new one for the VHD file. For more about creating a blob and container, see the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/).

> [!NOTE]
> Note:
> 
> Make sure that the blob storage is in the same resource group where you are deploying the vSocket VM.

## Copying the Azure vSocket Image with Azure SAS Using PowerShell

You can use Azure PowerShell to copy the vSocket image from Cato to your Azure storage container. We provide a URI with an Azure Shared Access Signature (SAS) to share the image.

Generate an SAS for your storage container, and then use Azure PowerShell to copy the vSocket image to your storage container. Use the region that is physically closest to your storage container:

- **North Europe:** [https://catoeuimagestorage.blob.core.windows.net/vsocket/socket_AZ1500_19605_production_socket_v23.0_20250220_2025_05_13.vhd?sp=racwdyti&amp;st=2025-06-12[...]sig=RliFKdF92bW8PWDquG6IwFj2YPCaKkvmxzo1Qs8Jz9c%3D](https://catoeuimagestorage.blob.core.windows.net/vsocket/socket_AZ1500_19605_production_socket_v23.0_20250220_2025_05_13.vhd?sp=racwdyti&amp;st=2025-06-12T08:21:11Z&amp;se=2030-06-12T16:21:11Z&amp;spr=https&amp;sv=2024-11-04&amp;sr=b&amp;sig=RliFKdF92bW8PWDquG6IwFj2YPCaKkvmxzo1Qs8Jz9c%3D)
- **United States:** [https://catostorageaimage.blob.core.windows.net/vsocket/socket_AZ1500_19605_production_socket_v23.0_20250220_2025_05_13.vhd?sp=racwdyti&amp;st=2025-06-12[...]sig=s0dEos5oplYj81XcJ0pCaPoMR2bpiao0u4BadDym%2FFU%3D](https://catostorageaimage.blob.core.windows.net/vsocket/socket_AZ1500_19605_production_socket_v23.0_20250220_2025_05_13.vhd?sp=racwdyti&amp;st=2025-06-12T08:20:05Z&amp;se=2030-06-12T16:20:05Z&amp;spr=https&amp;sv=2024-11-04&amp;sr=b&amp;sig=s0dEos5oplYj81XcJ0pCaPoMR2bpiao0u4BadDym%2FFU%3D)

You can access these SAS URIs from any region, except from China.

**To copy the Azure vSocket image:**

1. Create the Azure storage container, or use an existing container, for the vSocket image.

The storage container must be in the same resource group as the vSocket virtual machine (VM).
2. Open the container, and from the **Settings** section in the navigation pane, click **Shared access signature**.
3. Assign the correct permissions for the SAS, in the **Permissions** section, select the following items: **Read**, **Add**, **Create**, and **Write**.

![SAS_container.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28076507608605(1).png)
4. Make sure that **Allowed protocols** is set to **HTTPS only**.
5. Click **Generate SAS token and URL**.
6. Copy the **Blob SAS URL**. The URL concatenates both the container address and the SAS token.
7. Open Azure Cloud Shell and select **PowerShell**.
8. Run the azcopy command: `azcopy copy '&lt;Cato blob sas url&gt;' '&lt;customer blob sas container url&gt;'`

> [!NOTE]
> Note:
> 
> Make sure that you use single quotation marks in the command.

For example, the following command copies the image from the Cato EU blob:

`azcopy copy 'https://catoeuimagestorage.blob.core.windows.net/vsocket/socket_AZ1500_19605_production_socket_v23.0_20250220_2025_05_13.vhd' 'https://storagecatoexample.blob.core.windows.net/storagecatocontainernonaccel?sp=racw&amp;st=2025-6-02T11:44:51Z&amp;se=2025-6-02T19:44:51Z&amp;spr=https&amp;sv=2025-6-02&amp;sr=c&amp;sig=ABcdefGhIJklMnop2q%3Rs45T678%9Uv0xYZ1aBcdEFghiJ%2K'`

In the example above, replace the second URI (storagecatoexample.blob), with the Blob SAS URL that you generated.

### Troubleshooting Copying the vSocket with SAS

If there is an issue with copying the image to your account, check and make sure that the container is set with all of these permissions:

- Read
- Add
- Create
- Write

## Downloading the vSocket Scripts

Cato provides the following scripts to configure the virtual resources for Azure vSockets:

- create_vm_from_vhd.sh - should be used when deploying Azure vSocket v19 and above
- create_vm_from_vhd_U19.sh - should be used when deploying Azure vSocket below v19
- create_ha_settings.sh - HA script that configures high availability (HA) for two deployed vSockets

For more information about getting the vSocket files, see [Socket and vSocket Image Files](%%LINK:11503595325085%%).

> [!NOTE]
> Note:
> 
> After you successfully copy the image and download the scripts, continue the vSocket deployment with [Deploying an Azure vSocket Site Manually](/v1/docs/deploying-an-azure-vsocket-site-manually).

## Manually Adding the vSocket Image to Your Azure Account

For situations where you're unable to copy the image with Azure SAS, you manually download the file, untar it, and then upload it to your Azure container.

### Downloading and Extracting the Image from a TAR File

Download the Azure vSocket image as a TAR file from the public Cato repository. Then extract the vSocket image from the TAR file.

**To download and extract the image:**

1. Go to the Cato repository, from the [Socket and vSocket Image Files](%%LINK:11503595325085%%) article.
2. Download the TAR file for the VHD image, for example `socket_AZ1500_19605_production_socket_v23.0_20250220_2025_05_13.vhd.tar`
3. Untar the file.

### Uploading the VHD Image to Azure

Upload the VHD file for the vSocket image to the Azure storage blob.

**To upload the VHD file to the storage blob:**

1. Open the **Storage accounts** window and click the storage account, or create a new one.
2. From the Storage account navigation menu, scroll down to the **Blob service** section and click **Containers**.
3. Click the container, or create a new one.
4. In the Container window, click **Upload**.
5. From the right-hand **Upload blob** pane, select the VHD file and click **Upload**.
