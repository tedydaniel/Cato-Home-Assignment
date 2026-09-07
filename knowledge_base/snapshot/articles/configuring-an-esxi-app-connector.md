---
title: "Configuring an ESXi App Connector"
slug: "configuring-an-esxi-app-connector"
updated: 2026-08-09T07:58:51Z
published: 2026-08-09T07:58:51Z
canonical: "knowledge.catonetworks.com/configuring-an-esxi-app-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring an ESXi App Connector

This article describes how to deploy an App Connector for a data center or universal CPE (uCPE) running VMware ESXi.

## Preparing to Provision the ESXi App Connector

These are the prerequisites to prepare to create the VMware ESXi App Connector and connect it to the Cato Cloud:

- Download the OVA image for the ESXi vSocket and App Connector from the Cato Networks repository, see [Socket and vSocket Image Files](/v1/docs/socket-and-vsocket-image-files)
- Internet connectivity for the WAN1 interface on the App Connector VM
- Public DNS service must be available for the LAN interfaces on the App Connector VM
- Only attach 3 network interfaces (NICs) to the VM. Attaching more than 3 NICs may result in issues for the App Connector

## Create an App Connector

When you create an App Connector, you can choose the behavior for connecting to a preferred PoP in the Cato Cloud:

- Disabled - the App Connector automatically connects to the best available PoP (default)
- Enabled - Select the PoPs to which the connector attempts to connect to

When Preferred PoP is enabled, you can restrict an App Connector to only connect to the Preferred PoP Locations that you configure. In this case, the connector doesn't connect to a non-preferred PoP location despite any connectivity or performance issues that it is experiencing. When you use this option, you must define a primary and secondary PoP location for the App Connector.

Once the App Connector is created in the CMA, copy the serial number, as you will need to provide it when deploying the App Connector in your cloud environment.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/new app connector.png)

**To create an App Connector in the CMA:**

1. From the navigation menu, click **Access > App Connector**, and then click **New**.
2. Enter the information in the **General** section, such as **Connector** **Name** and **Country**.
3. Under **Type**, click **Virtual**.
4. In the **Connector Group** section, select an existing App Connector group from the list or enter a name to create a new group.
5. Under **Preferred PoPs**, select the behavior
  1. **Disabled** - the App Connector tries to connect to the best available PoP
  2. **Enabled** - Select the **Primary** and **Secondary** PoP locations that the connector tries to connect to
  3. **Enabled** and **Only connect to the preferred PoPs** - Only connect to the **Primary** or **Secondary** PoP location
6. Click **Apply**.

## Best Practices for Deploying an ESXi App Connector

- When you deploy an ESXi App Connector, we recommend creating the VM directly from the OVA file in vSphere, instead of creating a VM first and then attaching the OVA file to it. Deploying directly from the OVA file ensures that all necessary hardware settings are correctly applied and helps avoid potential hardware compatibility issues.

If you have already deployed and need to add memory, you can do so without having to redeploy your App Connector.
- Make sure to meet the VM App Connector minimum requirements for both vSphere and VM resources, as documented [below](/v1/docs/configuring-an-esxi-app-connector#minimum-requirements-for-the-vsocket).

## Deploying the VM in ESXi

In vSphere, deploy a new VM for the App Connector based on the Cato OVA template. The performance of the ESXi App Connector depends on the hardware configuration of the ESXi host.

### Minimum Requirements for the App Connector

These are the minimum requirements for the VM App Connector:

- vSphere requirements:
  - Minimum ESXi version - ESXi 8.0
  - Image format - OVA
- Required VM resources:
  - 2 vCPUs
  - 4 GB RAM
  - At least 7 GB HDD

### Deploying the VM

Deploy the ESXi template to a VM in vSphere and configure the settings for the App Connector interfaces.

**To deploy the App Connector to a VM:**

1. Right-click the ESXi host or folder and select **Deploy OVF Template**.
2. In the **Select an OVF template window**, select **Local file** and click **Choose Files**.
3. Select the OVA file with the App Connector image. Click **Next**.
4. In the **Select a name and folder** window, enter a VM name and select the location. Click **Next**.
5. In **Select a compute resource**, select the host for the VM. Click **Next**.

vSphere validates the settings for the OVF template.
6. In the **Review details** window, click **Next**.
7. In the **Select storage** window, select the virtual disk. Click **Next**.
8. In the **Select networks** window, configure each **Destination Network** according to the following Socket **Source Networks**:
  1. LAN interface
  2. Management interface
  3. WAN interface Click **Next**.
9. In the **Customize template** window, enter the serial number for the App Connector in the Cato Management Application.

You need to enter the exact serial number (including dashes).
10. Click **Next**.
11. In the **Ready to complete** window, click **Finish**. vSphere deploys the App Connector VM.
12. If necessary, click **Edit Settings** and change the resources and networks for the VM.

##
