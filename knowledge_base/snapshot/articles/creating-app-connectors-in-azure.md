---
title: "Creating App Connectors in Azure"
slug: "creating-app-connectors-in-azure"
updated: 2026-08-23T13:52:57Z
published: 2026-08-23T13:52:57Z
canonical: "knowledge.catonetworks.com/creating-app-connectors-in-azure"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating App Connectors in Azure

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

You can deploy an app connector in Azure to provide secure access to private applications in your cloud environment. The app connector establishes a connection between your cloud environment and Cato, and once connected, you assign it in the CMA and associate it to the relevant app connector group.

## Understanding the App Connector in Azure Workflow

The following is a high-level workflow for deploying an app connector in Azure:

- You create the App Connector object in the CMA
- Deploy the Cato App Connector from Azure Marketplace
- Assign apps to the connector

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

## Deploy the App Connector in Azure

Use the automated Cato wizard in the Azure Marketplace to create the virtual resources for the app connector and deploy it to Azure. The Azure app connector image is publicly available in the Marketplace.

**To deploy an app connector in Azure**

1. From the Azure Marketplace, search for Cato, and select the **Cato App Connector**.
2. In the **Overview** screen, select the **Plan** and **Subscription** for the Azure resources, and then click **Create**.
3. In the **Basics** screen, define the following settings for the resources and costs:
  - **Subscription** - Billing account for the Azure resources
  - **Resource group** - Azure resource group that the app connector resources are associated to
  - **Region** - Azure region for the app connector resource
  - **Resource prefix** - optional prefix to add to each of the app connector resources
4. In the **Networking** screen, first determine if you want to work with 2 or 3 NICs.

![azure-2NIC-3NIC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809663331357.png)

These are the app connector subnets (minimum subnet address space of /28):
  - 2 NIC deployments use the Standard_D2s_v5 instance type
  - 3 NIC deployments use the Standard_D8ls_v5 instance type

> [!NOTE]
> Note:
> 
> By default, 3 NIC vSockets support up to 2Gb throughput with the Azure Accelerated Networking option enabled.
  - MGMT subnet (3 NIC deployments, only) – Management communication between the app connector and the Azure API
  - WAN subnet - External WAN traffic for the app connector (Internet and Cato Cloud)
  - LAN subnet - Internal Azure resources and traffic that are connected to the app connector
5. In the **Cato AppConnector Configuration** screen, define the following settings for the app connector based on the app connector that you created in the [Cato Management Application](/v1/docs/creating-app-connectors-in-azure#create-an-app-connector), above.

![Marketplace_vSocket_Configuration.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809671464093.png)
  - **AppConnector Serial Number (S/N)** - Paste the **S/N** that you copied from the **Access > App Connectors** page.
  - **AppConnector Name** - Enter the name for the VM that hosts the app connector.

The **AppConnector Name** can't include spaces or [Azure-restricted characters](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules).
  - **WAN interface IP allocation** – Select a **Dynamic** or **Static** internal IP address for the WAN interface. For Static IP allocation, you can allocate any IP address.
  - **MGMT interface IP allocation** (3 NIC deployments, only) – Select a **Dynamic** or **Static** internal IP address for the MGMT interface. For Static IP allocation, you can allocate any IP address.
6. In the **Optional Configuration** screen, you can choose to define these settings:

![Marketplace_additional_configuration.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809648186653.png)

For more information about these settings, see above ???.
  - Public IP addresses for the WAN and/or MGMT (3 NIC deployments, only) interfaces
  - Network Security Groups for the WAN, MGMT (3 NIC deployments, only), and/or LAN interfaces
  - Availability Options for the app connector:
    - Azure Availability Set - **Create new** or use an existing one

**Note:** The Availability Set must be in the same Resource Group as the app connector
    - Azure Availability Zone - Select an Availability Zone in the range of 1 - 3
7. In the **Review + create** screen, review the app connector settings and then click **Create**.

After the app connector resources are deployed, it automatically connects to the Cato Cloud and checks if it's necessary to upgrade to the newest version. The Cato Management Application notification area shows messages regarding the status of connecting the app connector.

You can see your app connectors in the Access > App Connectors page.

## Assign Apps to the Connector

You assign apps to your connectors either from the Private Apps page or from App Connectors page, using the **Assign App** link.
