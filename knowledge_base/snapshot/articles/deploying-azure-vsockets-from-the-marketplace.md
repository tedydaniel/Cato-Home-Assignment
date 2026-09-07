---
title: "Deploying Azure vSockets from the Marketplace"
slug: "deploying-azure-vsockets-from-the-marketplace"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/deploying-azure-vsockets-from-the-marketplace"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying Azure vSockets from the Marketplace

This article explains how to use the Azure Marketplace to automatically deploy a virtual Cato Socket (vSocket) for a site hosted in Microsoft Azure. The Azure vSocket image publicly available in the Marketplace and the Cato wizard guides you through the steps to add the required virtual resources.

For more about manually deploying a vSocket with the Cato installation script, see [Deploying an Azure vSocket Site Manually](/v1/docs/deploying-an-azure-vsocket-site-manually).

For information about migrating an existing deployment to 2 NICs, see [Migrating Azure vSockets to a 2-NIC Solution](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution).

## Prerequisites

- Make sure the environment meets the requirements listed in [Cato Socket Connection Prerequisites](/v1/docs/cato-socket-connection-prerequisites-and-known-limitations).
- In tenants with a Private Azure Marketplace, the Azure Administrator should do the following:

**Note:** For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/marketplace/create-manage-private-azure-marketplace-new).
  1. Go to the **Private plans** screen and make sure you have two Cato offers - Azure Application and Virtual Machine. Make sure to select the **Azure Application** for the procedures outlined in this article.

![Azure-Marketplace-Offering.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247810219293.png)
  2. Go to the **Private marketplace** screen and add the two Cato offers to your desired Collection. Make sure this Collection applies to the relevant tenant in which you would like to install the vSocket.
- The Azure vSocket must have access to a public DNS server. Make sure that the VNet isn't configured to only use a private DNS server.
- Each vSocket instance requires outbound connectivity to these resources:
  - Virtual Network - DNS and HTTP
  - Azure Resource Manager - HTTPS
  - The management interface requires Internet access for public DNS servers (if configured, UDP/53) and management.azure.com (TCP/443)

### Supported Instance Types

- Standard_D2s_v5 - 2-NIC deployments, including up to 1Gbps throughput
- Standard_D8ls_v5 - 3-NIC deployments, including Azure Accelerated Networking and up to 2Gbps throughput

### Known Limitations

- Deploying vSockets from the Azure marketplace is not supported for Azure sites based in China. To deploy a vSocket in China, manually deploy the vSocket with the Cato installation script, see [Deploying an Azure vSocket Site Manually](/v1/docs/deploying-an-azure-vsocket-site-manually).
- When deploying resources with an Availability Zone set, the Public IP Set will not work. To workaround this, deploy the Availability Zone using the marketplace deployment wizard and manually configure the Public IP Set after the deployment wizard is complete.
- The default VM for new deployments is Standard_D8ls_v5. If your environment does not currently support this VM, contact your Azure admin. For existing deployments, you can resize your VM. For more information, see [For Microsoft Azure Sites - Changing Cato vSocket VMs to the Standard D8Is v5 VM Size](/v1/docs/for-microsoft-azure-sites-changing-cato-vsocket-vms-to-standard-d8ls-v5-vm-size).
- Azure extensions and backups are not supported for the vSocket VM

## Overview of the Virtual Resources for the Azure vSocket

When you deploy an Azure vSocket from the Marketplace, the following virtual resources are used by the vSocket:

- VM instance that the vSocket firmware is installed on
- WAN virtual network for traffic that is sent to the Cato Cloud
- LAN virtual network for internal LAN traffic
- MGMT virtual network (for 3 NIC instance types only)
  - For vSocket HA sites, the management communication between the vSocket and the Azure API used for the failover mechanism between the vSockets
  - Single vSocket sites don't require inbound or outbound traffic for the management interface
- 3-NIC vSockets support up to 2Gb throughput with the Azure Accelerated Networking option enabled.
- LAN Routing Table for the vSocket
- WAN and LAN Network Security Groups

## Creating the Azure vSocket Site

In the Cato Management Application, create a new **vSocket Azure** site. All the network segments that you create in the Cato Management Application must be included in the network range of the Azure virtual networks.

The Local IP for the vSocket must be the same as the IP address for the LAN interface on the VM. The first three IP addresses of the subnet are reserved by the VPC.

After you create the site, the Cato Management Application assigns a unique serial number (S/N) to it. We recommend that you copy and paste the serial number in a text file.

**To create the site for the Azure vSocket:**

1. From the Cato Management Application's navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![add_site_vsocket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27865026340893.png)
3. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Select **vSocket Azure** for the **Connection Type**.
  4. Configure the **Country**, **State**, and **Time Zone** to set the time frame for the **Maintenance Window**.
4. Configure the **WAN Interface Settings**, including the **Downstream** and **Upstream** bandwidth according to your ISP bandwidth.
5. Configure the LAN Interface Settings, including the **Native Range** for the Azure site. This setting must be the same as the LAN subnet IP range in Azure.
6. Click **Apply**. The site is added to the **Sites** list.
7. Copy and save the vSocket serial number for the Cato wizard in the Azure Marketplace:
  1. From the **Sites** list, select the new vSocket site.
  2. From the navigation menu, click **Site Configuration > Socket**. Copy the serial number (S/N) and save it.

## Creating an Azure vSocket from the Marketplace

Use the automated Cato wizard in the Azure Marketplace to create the virtual resources for the primary (or single) vSocket and deploy it for the Azure site. The Azure vSocket image is publicly available in the Marketplace.

If you are using a high availability (HA) configuration for the site, you need to run the wizard twice, and select the appropriate options for the second vSocket (see below [Adding a Secondary vSocket for High Availability](/v1/docs/deploying-azure-vsockets-from-the-marketplace#adding-a-secondary-vsocket-for-high-availability)).

**Note:** As of March 2025, you need to use the Standard SKU for public IP addresses that you assign to a VM interface. The Basic SKU for public IP addresses will be [retired on Sept. 30, 2025](https://learn.microsoft.com/en-us/answers/questions/1033456/retirement-announcement-basic-sku-public-ip-addres). For more information on this retirement and migration of existing IPs, see the following notification: [Upgrade Azure vSocket Public IPs from Basic to Standard SKU](/v1/docs/upgrade-azure-vsocket-public-ips-from-basic-to-standard-sku).

### Optional Configurations with the Marketplace Wizard

This section explains the different optional settings that you can choose to define for a vSocket in the **Optional Configurations** window in the Cato wizard.

#### Assigning Public IP Addresses to WAN and MGMT Interfaces

While it's not a requirement, you can choose to define a static public IP address from Azure for the WAN and MGMT interfaces and Virtual Networks. If you configure a public IP address, it must be for both the MGMT and WAN interfaces. The MGMT interface must have a public IP address to access the Socket WebUI over the public Internet.

After configuring public IP address, Cato recommends you add Network Security Groups.

When you connect to the Socket WebUI through the Cato tunnel or Cato Management Application, you do not need a public IP address.

#### Using Network Security Groups

Network Security Groups define which traffic is allowed and helps to manage inbound traffic for a virtual network, defined according to the WAN, LAN, or MGMT interface. You can use an existing Security Group or create a new one for the vSocket.

#### Assigning the vSocket VMs to an Availability Set or Availability Zone

Azure provides these features for cloud resource redundancy:

- Availability Set - secures the Azure services from outages inside individual data centers
- Availability Zone - protects against incidents that impact the entire data center

You can choose to assign the vSockets to a single Availability Set or Availability Zone. Availability Sets are mostly used in a vSocket HA configuration when you want to make sure that the both vSockets are assigned to different Fault and Update domains.

You can't assign an Availability Set to VMs that are using different Availability Zones.

> [!NOTE]
> Note:
> 
> Azure doesn't let you assign a VM to an Availability Set after you create it.

### Deploying the Primary vSocket

Use the Cato vSocket wizard in the Azure Marketplace to define the settings for the virtual resources and deploy the primary vSocket. Then the vSocket automatically connects to the Cato Cloud and is assigned to the Azure site in your account.

For more about deploying the secondary vSocket for HA configurations, see below [Adding the Secondary vSocket to an Azure Site](/v1/docs/deploying-azure-vsockets-from-the-marketplace#adding-the-secondary-vsocket-to-an-azure-site).

**To deploy the primary Azure vSocket from the Marketplace:**

1. From the Azure Marketplace, search for **Cato**, and select the **Cato Networks Virtual Socket**.
2. In the **Overview** screen, select the **Plan** and **Subscription** for the Azure resources, and then click **Create**.

![Marketplace_Overview.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247803838749.png)
3. In the **Basics** screen, define the following settings for the resources and costs:

![Marketplace_Basics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247826927645.png)
  - **Subscription** - Billing account for the Azure resources
  - **Resource group** - Azure resource group that the vSocket resources are associated to
  - **Region** - Azure region for the vSocket resource
  - **Resource prefix** - optional prefix to add to each of the vSocket resources
4. In the **vSocket Deployment** screen, select **Deploy a primary vSocket**.

![Marketplace_deployment_type.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247822536989.png)
5. In the **Networking** screen, first determine if you want to work with 2 or 3 NICs.

![azure-2NIC-3NIC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247804159261.png)

These are the vSocket subnets (minimum subnet address space of /28):
  - 2 NIC deployments use the Standard_D2s_v5 instance type
  - 3 NIC deployments use the Standard_D8ls_v5 instance type

> [!NOTE]
> Note:
> 
> By default, 3 NIC vSockets support up to 2Gb throughput with the Azure Accelerated Networking option enabled.
  - MGMT subnet (3 NIC deployments, only) – Management communication between the vSocket and the Azure API
  - WAN subnet - External WAN traffic for the vSocket (Internet and Cato Cloud)
  - LAN subnet - Internal Azure resources and traffic that are connected to the vSocket

**Note:** Make sure that the IP range of the LAN subnet is the same as the **Native Range** for the vSocket site in the Cato Management Application.
6. In the **Cato vSocket Configuration** screen, define the following settings for the vSocket based on the vSocket site that you created in the Cato Management Application (above [Creating the Azure vSocket Site](/v1/docs/deploying-azure-vsockets-from-the-marketplace#creating-the-azure-vsocket-site)).

![Marketplace_vSocket_Configuration.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247810785693.png)
  - **vSocket Serial Number (S/N)** - Paste the **S/N** that you copied from the **Site Configuration > Socket** page.
  - **vSocket LAN IP** - Enter the **Local IP** for the primary vSocket from the **Site Configuration > Networks** page in the CMA.
  - **vSocket Name** - Enter the name for the VM that hosts the vSocket.

The **vSocket Name** can't include spaces or [Azure restricted characters](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules).
  - **WAN interface IP allocation** – Select a **Dynamic** or **Static** internal IP address for the WAN interface. For Static IP allocation, you can allocate any IP address.
  - **MGMT interface IP allocation** (3 NIC deployments, only) – Select a **Dynamic** or **Static** internal IP address for the MGMT interface. For Static IP allocation, you can allocate any IP address.
7. In the **Optional Configuration** screen, you can choose to define these settings:

![Marketplace_additional_configuration.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247838326557.png)

For more information about these settings, see above [Optional Configurations with the Marketplace Wizard](/v1/docs/deploying-azure-vsockets-from-the-marketplace#optional-configurations-with-the-marketplace-wizard).
  - Public IP addresses for the WAN and/or MGMT (3 NIC deployments, only) interfaces
  - Network Security Groups for the WAN, MGMT (3 NIC deployments, only), and/or LAN interfaces
  - Availability Options for the vSocket:
    - Azure Availability Set - **Create new** or use an existing one

**Note:** The Availability Set must be in the same Resource Group as the vSocket
    - Azure Availability Zone - Select an Availability Zone in the range of 1 - 3
8. In the **Review + create** screen, review the vSocket settings and then click **Create**.

**Note:** You can choose to export the deployment template and use it future vSocket deployments.

The **Deployment is in progress** screen shows real-time status of the vSocket deployment. It can take several minutes to complete deploying all the resources.

After the vSocket resources are deployed, the vSocket automatically connects the site to the Cato Cloud and checks if it's necessary to upgrade to the newest vSocket version. The Cato Management Application notification area shows messages regarding the status of connecting the vSocket.

## Adding a Secondary vSocket for High Availability

To provide redundancy for vSockets within an Azure site, you can deploy two vSockets in the same Azure Virtual Network (VNet), and set them to work in a high availability (HA) configuration. The vSockets operate in active/passive mode and the LAN links are used to send keepalive messages between the vSockets.

The Azure HA configuration uses a Floating IP address which is bound to the LAN interface for the active vSocket. When there is a failover to the passive secondary vSocket, the Floating IP moves to the secondary vSocket LAN interface. The route tables use this Floating IP as the next hop for traffic that is sent over the Cato Cloud.

Where required, you can deploy Azure HA supports vSockets to different Availability Zones. Alternatively, you can use the Availability Sets to make sure that both vSockets are deployed in different Fault and Update domains in Azure.

After deploying the primary vSocket, in the Cato Management Application add the secondary vSocket to the Azure site. Then use the Marketplace wizard to deploy the secondary vSocket.

For more information about Azure HA, see [Configuring High Availability for Azure vSockets](/v1/docs/configuring-ha-for-azure-vsockets).

### Prerequisites for Azure High Availability

- You must be the owner of the Azure Resource Group for the virtual resources
- The Azure vSockets must use the same VNet
- If you used the default virtual network name **vsNet** when deploying the primary Socket, and you encounter a validation error, you must define a Resource Prefix for the secondary vSocket
- If you have a default policy for system-defined identities, you must exempt the Cato vSockets to make sure the transition between the primary and secondary vSockets works. For more information, see the [relevant Azure documentation](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-assign-managed-identity-via-azure-policy).

### Adding the Secondary vSocket to an Azure Site

Use the **Add Secondary Socket** option in the **Network > Sites > Site Settings > Socket** screen to prepare the site for the secondary vSocket. There is a pop-up window where you enter the following settings:

- LAN Interface IP - IP address for the LAN interface of the secondary vSocket
- LAN Floating IP - IP address for the Floating IP that is used for the Azure HA configuration

The Cato Management Application uses the LAN Interface IP address as the management IP address for the secondary vSocket. This LAN interface is also used for the HA keepalive packets.

After you add the secondary vSocket to the site, the Cato Management Application does the following:

- Generates the vSocket serial number for the new vSocket (this serial number is used when you run the Cato script to install the vSocket on the VM)
- Enables the **High Availability Configurations** section for that site
- Modifies the **Networks** section Native Range, the Local IP is replaced with the Floating IP

**To configure an Azure site for HA:**

1. From the navigation menu, select **Network > Sites**, and select the Azure site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click **Add Secondary Socket**. The **Add Secondary vSocket (High Availability)** window opens.
4. Configure the LAN IP settings:
  1. Enter the **LAN Interface IP**. This value is used as the MGMT IP and for keepalive packets.
  2. Enter the **LAN Floating IP**.
5. Click **Apply**. The Floating IP settings are configured and copied to the **Socket > High Availability Configurations** section.
6. Click **Save**.
7. Copy and save the serial number (S/N) for the **Secondary** vSocket.

Use this S/N when you deploy the secondary vSocket from the Azure Marketplace.

#### Changes to the Socket Screen

After you add the secondary vSocket to the site, in the **Socket** screen, the **Destination** for the LAN1 link is automatically set to **LAN & HA**.

### Deploying a Secondary Azure vSocket from the Marketplace

Use the automated Cato wizard in the Azure Marketplace to create the virtual resources for the secondary vSocket and deploy it for the Azure site.

When you configure the settings for the secondary vSocket in the Marketplace wizard, the following settings must be the same settings for the primary and secondary vSockets:

- Networking - You must use the same Virtual Network and MGMT, WAN, and LAN subnets for the primary and secondary vSockets.
- Optional Configuration > Security Groups - if you create a new group for the primary, use it again with the secondary. Otherwise select None for both, or the same existing group.

**To deploy the secondary Azure vSocket from the Marketplace:**

1. From the Azure Marketplace, search for **Cato**, and select the **Cato Networks Virtual Socket**.
2. In the **Overview** screen, select the **Plan** and **Subscription** for the Azure resources, and then click **Create**.
3. In the **Basics** screen, define the same settings that you defined for the primary vSocket:
  - **Subscription** - Billing account for the Azure resources
  - **Resource group** - Azure resource group that the vSocket resources are associated to
  - **Region** - Azure region for the vSocket resource
  - **Resource prefix** - optional prefix to add to each of the vSocket resources

If you used the default virtual network name **vsNet** when deploying the primary Socket, you must define a Resource Prefix for the secondary Socket to avoid any errors.
4. In the **vSocket Deployment** screen, select **Deploy a secondary vSocket**.

![07_deployment_secondary.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247804397853.png)
5. In the **Networking** screen, select the same VNet being used by the primary vSocket

![secondary_azure_vsocket-networking.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247811053085.png)

> [!NOTE]
> Important:
> 
> If you do not select the same resources as the primary vSocket, the HA deployment will fail.
  - For the WAN, MGMT, and LAN subnets, select the same subnets that you used for the primary vSocket
6. In the **Cato vSocket Configuration** screen, define the following settings for the vSocket based on the vSocket site that you created in the Cato Management Application (above [Creating the Azure vSocket Site](/v1/docs/deploying-azure-vsockets-from-the-marketplace#creating-the-azure-vsocket-site)).

![08_config_secondary.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247811162909.png)
  - **Select the Primary vSocket** - The primary vSocket that you previously created
  - **Select the Primary vSocket LAN NIC** – The NIC for the primary vSocket’s LAN subnet that you previously created
  - **Secondary vSocket Serial Number (S/N)** - Copy the **S/N** for the secondary vSocket from the **Site Configuration > Socket** screen in the Cato Management Application.
  - **Secondary vSocket LAN IP** - Enter the **Local IP** for the secondary vSocket from the **Site Configuration > Socket > High Availability Configurations** screen in the Cato Management Application.
  - **Floating IP for the Site** -The same Floating IP is used by both vSockets. The Floating IP is configured in **Site Configuration > Socket > High Availability Configurations** screen in the Cato Management Application.
  - **Name for the Secondary vSocket** - Enter the name for the VM that hosts the secondary vSocket.
  - **WAN interface IP allocation** – Select a **Dynamic** or **Static** internal IP address for the WAN interface. For Static IP allocation, you can allocate any IP address.
  - **MGMT interface IP allocation** (3 NIC deployments, only) – Select a **Dynamic** or **Static** internal IP address for the MGMT interface. For Static IP allocation, you can allocate any IP address.
7. In the **Optional Configuration** screen, define these settings for the secondary vSocket:

![Marketplace_additional_confguration_secondary.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247838703261.png)
  - Make sure to configure the same **Security Groups** and **Availability** configurations as the primary vSocket.
  - **LAN Route Table Update** - Select the same LAN Routing Table as the primary vSocket. The HA Floating IP is automatically used as the next hop.
8. In the **Review + create** screen, review the vSocket settings and then click **Create**.

The **Deployment is in progress** screen shows real-time status of the vSocket deployment. It can take several minutes to complete deploying all the resources.

After the vSocket resources are deployed, the vSocket automatically connects the site to the Cato Cloud and checks if it's necessary to upgrade to the newest vSocket version. The Cato Management Application notification area shows messages regarding the status of connecting the vSocket.

## Troubleshooting Deployment Failures

In some cases, Azure may fail to complete the deployment of your vSocket, for example, if the deployment wizard was not approved by an administrator in a private Azure Marketplace.

You may inspect the deployment error summary or the Azure Activity Log for more information about the failed deployment.

During the deployment process, Azure resources are created automatically regardless of the deployment status. If your deployment failed, make sure to delete the resources before attempting another deployment.

**To delete Azure deployment resources:**

1. In Azure, go to **Resource Groups** and select the resource group you used for this deployment.
2. Under **Resources**, use the filter screen to filter for the prefix of your deployment. All the deployment resources created using this prefix appear.

![Azure_delete_resources.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247804742685.png)
3. Check all resources match the prefix and bulk-select them using the checkbox.
4. Click **Delete**. You can optionally apply force-delete to Virtual machines, if selected.

![Azure_delete_command.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247811477405.png)

When ready, run the deployment wizard again. If you are unable to complete the deployment please contact Cato Support [support@catonetworks.com](mailto:support@catonetworks.com).

## Connecting to the Azure vSocket WebUI

After the vSocket is deployed, we recommend that you connect to the vSocket WebUI and change the password for the VM. The default password for the vSocket is the VM ID for the vSocket VM.

For more information, see [Deploying an Azure vSocket Site Manually](/v1/docs/deploying-an-azure-vsocket-site-manually).

## Additional Resources

Cato offers multiple options for deploying, configuring and troubleshooting Azure vSockets.

- [Deploying an Azure vSocket Site Manually](/v1/docs/deploying-an-azure-vsocket-site-manually) - If you prefer to explore custom (ARM template deployment) or manually creating resources for the vSocket instead of using the Azure marketplace
- [Configuring High Availability for Azure vSockets](/v1/docs/configuring-ha-for-azure-vsockets) - Manually creating the HA configuration for vSockets
- [How to Use a vSocket in Azure Multiple VNets Environment](/v1/docs/how-to-use-a-vsocket-in-azure-multiple-vnets-environment)
- [Azure HA vSocket Troubleshooting](/v1/docs/azure-ha-vsocket-troubleshooting)
