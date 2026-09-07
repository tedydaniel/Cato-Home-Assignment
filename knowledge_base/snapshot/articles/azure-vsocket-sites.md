---
title: "Deploying an Azure vSocket Site Manually"
slug: "deploying-an-azure-vsocket-site-manually"
updated: 2026-07-21T07:17:03Z
published: 2026-07-21T07:17:03Z
canonical: "knowledge.catonetworks.com/deploying-an-azure-vsocket-site-manually"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying an Azure vSocket Site Manually

This article explains how to use the Cato script to manually deploy a virtual Cato Socket (vSocket) for a site hosted in Microsoft Azure.

## Overview

For sites that are hosted in Azure, you can deploy a vSocket on an Azure virtual machine (VM) and benefit from many of the same features as a physical Socket. This article explains how to use the Cato script to manually deploy a vSocket, as opposed to using the Azure marketplace. For example, when a site is located in China where the marketplace is unavailable.

You can choose to assign a vSocket VM to an Availability Set for resiliency purposes, for example with vSocket High Availability.

### Additional Deployment Options for the Azure vSocket

Cato provides multiple options to deploy the vSocket for Azure sites for running the Cato script.

These are other Azure vSocket deployment options:

- [Configuring High Availability for Azure vSockets](/v1/docs/configuring-ha-for-azure-vsockets) - For more about how to use the Cato script for deploying vSockets in a HA configuration
- [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace) - For more about deploying a single or HA vSockets by using the Cato wizard that is available on the Azure Marketplace

### Copying the vSocket Image and Configuration Script

Cato provides a VHD image and a configuration script for the Azure vSocket. Use Azure PowerShell to copy the vSocket image from Cato to your Azure storage container, and download the script file from the Cato public repository.

For more about the Azure vSocket image and a configuration script, see [Copying the Azure vSocket VHD Image with SAS](/v1/docs/copying-the-azure-vsocket-vhd-image-with-sas).

### General Prerequisites

You can run the vSocket configuration script directly from the [Azure Cloud Shell](https://azure.microsoft.com/en-gb/features/cloud-shell/) or from the macOS and Linux Ubuntu operating systems. Windows Bash shells, including the Windows Subsystem for Linux (WSL), are NOT supported to run the Azure vSocket script.

> [!NOTE]
> Note:
> 
> The Azure vSocket must have access to a public DNS server. Make sure that the VNet isn't configured to only use a private DNS server.

- For High Availability (HA) configurations, the vSocket requires a static IP address for the MGMT interface
- (Optional) If access to the vSocket WebUI is required over the Internet:
  - Assign a public IP to the MGMT interface and create a security rule to allow TCP/443 inbound traffic
  - Cato recommends only temporarily exposing the WebUI to the Internet for as long as needed, and in addition, restrict access by source IP (if possible)
- Make sure the environment meets the requirements listed in [Cato Socket Connection Prerequisites](%%LINK:360000891085%%).
- The vSocket configuration script supports the following instance types:

For information about migrating your vSocket to an instance with 2 network interfaces, see [this article](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution).
  - 2 NICs - Standard_D2s_v5
  - 3 NICs - Standard_D8s_v3
  - 3 NICs - Standard_D8ls_v5

Microsoft requires accelerated networking on the D2s_v5 and D8ls_v5 sizes, and it can’t be disabled.

#### OS Prerequisites for the Configuration Script

These are the prerequisites to run the script for both Linux and macOS operating systems:

- Bash shell and typical binutils package.
- Lightweight JSON processor jq ([https://stedolan.github.io/jq/](https://stedolan.github.io/jq/)), for Ubuntu OS install the processor as `apt update &amp;&amp; apt install jq`.
- Azure CLI utility - for more about installing the Azure CLI, see the documentation for [Microsoft Azure](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

### Known Limitations

These are known limitations with the Azure vSocket:

- For Socket versions earlier than v14.0, the primary vSocket LAN IP is used for BGP peering. This does not survive failover to the secondary vSocket.
  - Starting with v14.0, in vSocket HA configurations, the Floating IP is used for BGP peering. Make sure to define the Floating IP in the neighboring BGP router.
- Cato supports accelerated networking only on vSocket instance types using 3 NICs.
- Using Azure [Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-support-matrix#replicated-machine-operating-systems) for vSocket VM replication is not supported.
- The default VM for new deployments is Standard_D8ls_v5. If your environment does not currently support this VM, contact your Azure admin. For existing deployments, you can resize your VM. For more information, see [For Microsoft Azure Sites - Changing Cato vSocket VMs to the Standard D8Is v5 VM Size](/v1/docs/for-microsoft-azure-sites-changing-cato-vsocket-vms-to-standard-d8ls-v5-vm-size).
- Azure extensions and backups are not supported for the vSocket VM

## High Level Overview of Creating the Azure vSocket

1. In the Cato Management Application, create a new site for the Azure vSocket.
2. In Azure, create the following virtual resources for the vSocket VM:
  - Virtual Network (VNet) for the vSocket
  - WAN, LAN and Management subnets
  - WAN, LAN and Management interfaces
  - Routing tables for each of the vSocket's subnets
  - WAN, LAN and Management network security groups
3. Run the vSocket configuration script.

## Creating the Azure vSocket Site

In the Cato Management Application, create a new **vSocket Azure** site. All the network segments that you create in the Cato Management Application must be included in the network range of the Azure virtual networks.

The Local IP for the vSocket must be the same as the IP address for the LAN network interface that you will create in Azure.

The first three IP addresses of the subnet are reserved by the VPC.

After you create the site, the Cato Management Application assigns a unique serial number (S/N) to it. We recommend that you copy and paste the serial number in a text file.

You need to enter this serial number when you run the vSocket configuration script.

**To create the site for the Azure vSocket:**

1. From the Cato Management Application's navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![add_site_vsocket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27865096856093(1).png)
3. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Select **vSocket Azure** for the **Connection Type**.
  4. Configure the **Country**, **State**, and **Time Zone** to set the time frame for the **Maintenance Window**.
4. Configure the **WAN Interface Settings**, including the **Downstream** and **Upstream** bandwidth according to your ISP bandwidth.
5. Configure the **LAN Interface Settings**, including the **Native Range** for the Azure site.

This setting must be the same as the LAN subnet IP range in Azure.
6. Click **Apply**. The site is added to the **Sites** list.
7. Copy and save the vSocket serial number for the vSocket configuration script:

![vSocket_Socket_tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247852614301(1).png)
  1. From the **Network > Sites** page, select the new vSocket site.
  2. From the navigation menu, click **Site Configuration > Socket**. Copy the serial number (S/N) and save it.

## Creating the Azure Virtual Resources

This section explains how to create the virtual resources in Azure for the vSocket. Depending on your deployment, you may be able to use some existing Azure virtual resources instead of creating new ones.

Make sure that you have the correct permissions to create virtual resources in Azure.

### Creating the Virtual Network

Create the virtual network address space in Azure for the vSocket. The address space contains the subnets for the Azure vSocket. When you create the virtual network, you also create the subnets used for the Management, LAN, and WAN links.

The vSocket subnets have a minimum subnet address space of /28.

**To create the virtual network:**

1. From the Microsoft Azure homepage, create a new virtual network: click **Virtual networks > Create**. If you decide to use an existing virtual network, you must select existing subnets that correspond to that virtual network.
2. In the **Create virtual network** window, configure the settings for the virtual network:
  1. In the **Basics** tab select the **Subscription**, **Resource Group**, **Virtual Network** name and **Region**.

**Note:** Make sure that the virtual network and the rest of the vSocket resources are deployed in the same region.
  2. In the **IP addresses** tab configure the following settings:

![virtual_network_creation.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247852688541(1).png)
    1. Create the **Address space** for the Virtual Network.
    2. Within the address space click **Add a subnet** and create each of these subnets for the vSocket: LAN, WAN and Management.

**Notes:**
      - IPv6 address spaces are NOT supported
      - The LAN subnet must correlate with the **Native Range** that you configured for this site in the Cato management Application
      - The address range for each of the subnets must be within the address space of the virtual network.
3. Click **Review + create**. The Virtual Network is deployed to the Azure account.

### Configuring the LAN Resources

These are the required LAN resources for the vSocket: subnet, network interface and routing table. The LAN subnet refers to LAN traffic that is sent to the internal Azure resources. The network interface is configured to use the LAN subnet. This section explains how to create a network interface and attach it to the LAN subnet.

> [!NOTE]
> Note:
> 
> For Azure HA configurations, during failover there is an API call that automatically adds the Floating IP to the LAN interface of the standby vSocket and deletes settings configured on the LAN interface (including the LAN NSG).

Don't manually configure the Floating IP on the LAN interface of a vSocket. The Cato HA script assigns the Floating IP to the primary vSocket LAN interface and then reboots the vSockets.

#### Creating the LAN Interface

Use the Azure wizard to define the settings for the network interface that will be used as the LAN interface for the vSocket.

1. From the Microsoft Azure homepage, go to **Network Interfaces**.
2. Click **Create**.

The **Create network interface** page opens.

![network_interface.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247811880221(1).png)
3. Configure the settings for the network interface:
  1. **Subscription** - Subscription ID of your Azure account.
  2. **Resource Group** - Select the resource group for the network interface.
  3. **Name** - Give the interface a meaningful name.
  4. **Region** - Select the same region as the rest of the vSocket resources.
  5. **Virtual network** - Select the virtual network that you configured for the vSocket (in the previous section).
  6. **Subnet** - Select the LAN subnet.
  7. **IP Version** - Select **IPv4**.
  8. **Private IP address assignment** - Select **Static** and enter the private IP address for the network interface. This IP address is the same as the **Local IP** configured for the Native Range in the Cato Management Application.
4. Click **Review + create**. The network interface is deployed to the Azure account.
5. Enable IP forwarding for the interface:
  1. From the Microsoft Azure homepage, go to **Network Interfaces**.
  2. Select the LAN network interface.
  3. From the **Settings** section, click **IP configurations**.
  4. Select **Enable IP forwarding**.
  5. Click **Save**. The network interface is configured for IP forwarding.

#### Configuring the LAN Route Table

Create and configure the route table for the Azure site and vSocket. You need the following settings to configure the LAN route table:

- If **ALL TRAFFIC** from your Azure account is routed through the vSocket, then you can use 0.0.0.0/0 for the LAN subnet.
- However, if only some of the traffic is routed through the vSocket, then configure the LAN subnet for the IP range of the relevant traffic.
- In case you are using Windows KMS and the default route (0.0.0.0/0) is within the route table, make sure to add an exception for 23.102.135.246/32. Read more [here](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/custom-routes-enable-kms-activation) on Microsoft's documentation center.

After you configure the LAN route, then you assign the LAN subnet to the route table.

**To configure the LAN route table settings:**

1. Create the LAN route table:

![route-table-creation.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247852870301(1).png)
  1. From the search bar, search for **route tables**.
  2. From the **Route tables** page, click **Create**.
  3. From the **Create route table** pane, enter the **Name** and configure the other settings.
  4. Click **Create**. The route table is deployed to the Azure account.
2. Configure the LAN routes for the vSocket:
  1. From the **Route tables** page, click the new route table.
  2. In the left-hand pane, from the **Settings** section, click **Routes**.
  3. Create a route for the LAN traffic:
    1. Click **Add**.
    2. From the **Add route** pane, enter the **Route name**.
    3. In **Destination type**, enter the LAN IP address range for the LAN.
    4. In **Next hop type**, select **Virtual appliance**.
    5. In **Next hop address**, enter the private IP address for the vSocket VM.
    6. Click **Add**. The LAN to Internet route is added to the route table.
3. To associate the LAN subnet to the route table:
  1. In the left-hand pane of the **Route table** page, from the **Settings** section, click **Subnets**.
  2. Click **Associate**.
  3. From the **Associate subnet** pane, in the **Virtual network** drop-down menu select the virtual network.

![09_AssociateSubnet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247805347741(1).png)
  4. From the **Subnet** drop-down menu, select the LAN subnet.
  5. Click **OK**. The LAN subnet is added to the route table.

### Configuring the WAN Resources

These are the required resources for the WAN subnet of the vSocket: subnet, network interface and routing table.

This is the virtual interface in Azure for the WAN traffic that is sent to the Cato Cloud. The interface is configured to use the WAN subnet. After you create the interface, you need to enable it to support IP forwarding

#### Creating the WAN Interface

Use the Azure wizard to define the settings for the network interface that will be used as the WAN interface for the vSocket.

1. From the Microsoft Azure homepage, go to **Network Interfaces**.
2. Click **Create**.

The **Create network interface** page opens.

![network_interface.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247811880221(1).png)
3. Configure the settings for the network interface:
  1. **Subscription** - Subscription ID of your Azure account.
  2. **Resource Group** - Select the resource group for the network interface.
  3. **Name** - Give the interface a meaningful name.
  4. **Region** - Select the same region as the rest of the vSocket resources.
  5. **Subnet** - Select the WAN subnet.
  6. **IP Version** - Select **IPv4**.
  7. **Private IP address assignment** - Select **Static** and assign a private IP address for the WAN network interface.
4. Click **Review + create**. The WAN interface is deployed to the Azure account
5. Enable IP forwarding for the WAN interface:
  1. From the Microsoft Azure homepage, go to **Network Interfaces**.
  2. Select the WAN network interface
  3. From the **Settings** section, click **IP configurations**.
  4. Select **Enable IP forwarding**.
  5. Click **Save**. The network interface is configured for IP forwarding.
6. Add a public IP address to the WAN interface:
  1. From the **Settings** section of the network interface, click **IP configurations**
  2. Select the IP address. The **Edit IP Configuration** pane opens.
  3. Select **Associate public IP address** and click **Save**.

#### Configuring the WAN Route Table

The WAN network interface connects the WAN subnet to Cato over the internet. The following route table is used for BOTH the WAN interface and the Management interface, since both require the same outbound routing policy.

After you configure and associate the WAN route table with the WAN network interface, you will associate the management network interface with the WAN route table as well.

**To configure the WAN route table:**

1. Create the WAN route table:
  1. From the search bar, search for **route tables**.
  2. From the **Route tables** page, click **Create**.
  3. From the **Create route table** pane, configure the settings.
  4. Click **Create**. The route table is deployed to the Azure account.
2. Configure the WAN route table:
  1. From the **Route tables** page, click the new route table.
  2. In the left-hand pane, from the **Settings** section, click **Routes**.
  3. Create a route for outbound traffic:
    1. Click **Add**.
    2. From the **Add route** pane, enter the **Route name**.
    3. In **Destination type**, enter **0.0.0.0/0**.
    4. In **Next hop type**, select **Internet**.
    5. Click **Add**
3. Associate the WAN subnet to the route table:
  1. In the left-hand pane of the **Route table** page, from the **Settings** section, click **Subnets**.
  2. Click **Associate**.
  3. From the **Associate subnet** pane, in the **Virtual network** drop-down menu select the virtual network.
  4. From the **Subnet** drop-down menu, select the WAN subnet.
  5. Click **OK**. The WAN subnet is added to the route table.

### Configuring the Management Resources

The Management Interface is the virtual interface in Azure for the management communication between the vSocket and the Azure API. This interface is also used to access the vSocket WebUI.

- Inbound access to the management interface is a potential security risk, make sure to configure the Azure network security group to restrict access to this interface only to necessary admins.
- A single vSocket does not require inbound or outbound traffic for the management interface - Outbound Internet traffic is only required for Azure HA configurations.
- Inbound internet connections on TCP/443 must be allowed to access the vSocket WebUI using the public management IP (if assigned)

#### Creating the Management Interface

Use the Azure wizard to define the settings for the network interface that will be used as the Management interface for the vSocket.

1. From the Microsoft Azure homepage, go to **Network Interfaces**.
2. Click **Create**. The **Create network interface** page opens.
3. Configure the settings for the MGMT network interface:
  1. **Subscription** - Subscription ID of your Azure account.
  2. **Resource Group** - Select the resource group for the network interface.
  3. **Name** - Give the interface a meaningful name.
  4. **Region** - Select the same region as the rest of the vSocket resources.
  5. **Virtual network** - Make sure the virtual network is the one you previously configured for the vSocket.
  6. **Subnet** - Select the Management subnet.
  7. **IP Version** - Select **IPv4**.
  8. **Private IP address assignment** - Select **Static** and assign a private IP address for the Management network interface. This IP can be used locally to access the vSocket WebUI.
4. Click **Review + create**. The MGMT network interface is deployed to the Azure account.
5. Enable IP forwarding for the interface:
  1. From the Microsoft Azure homepage, go to **Network Interfaces**.
  2. Select the Management network interface.
  3. From the **Settings** section, click **IP configurations**.
  4. Select **Enable IP forwarding**.
  5. Click **Save**. The network interface is configured for IP forwarding.
6. **(Optional)** Assign a public IP address to the Management interface if access to the vSocket WebUI is required over the Internet. (you can also access the WebUI via the private IP of the network interface)
  1. From the Microsoft Azure homepage, go to **Network Interfaces**.
  2. Select the Management network interface.
  3. From the **Settings** section, click **IP configuration**.
  4. Select the IP address. The **Edit IP Configuration** pane opens.
  5. Select **Associate public IP address** and click **Save**.

#### Associating the Management Subnet to the Route Table

Use the same routing table previously created for the WAN interface for the Management interface. Both network interfaces require the same routing policy for outbound connections to the internet.

**Associate the Management subnet to the route table:**

1. In the left-hand pane of the **Route table** page, from the **Settings** section, click **Subnets**.
2. Click **Associate**.
3. From the **Associate subnet** pane, in the **Virtual network** drop-down menu select the virtual network.
4. From the **Subnet** drop-down menu, select the Management subnet.
5. Click **Ok**. The route table is now associated with the Management subnet.

### Creating a Network Security Group

Create a network security group that defines which traffic is allowed. After you create the vSocket VM, you can apply this security group to help manage inbound traffic for the network interfaces.

> [!NOTE]
> Note:
> 
> You can use an existing security group instead of creating a new one for the vSocket. Skip this section if you are using an existing security group.

**To create the network security group:**

1. From the Microsoft Azure homepage, go to **Network Security Groups**.
2. From the **Network security group** page, click **Create**.

![nsg-creation.png](https://support.catonetworks.com/hc/article_attachments/24247839637917)

The **Create network security group** page opens and shows the **Basics** tab.
  1. Select the **Resource group**.
  2. Enter the **Name** for the network security group.
  3. Select the **Region** for the security group.
3. Click **Review + create**. The network security group is now ready to be used.

#### Configuring the WAN and LAN Security Rules

Configure the inbound security rules for the network security group to define the traffic that is allowed to connect to the vSocket. We recommend that you configure the WAN network security group to deny all inbound traffic and allow all outbound traffic. Use the Cato firewall to control the inbound LAN traffic, so you can allow all traffic in both directions for the LAN network security group.

![nsg-settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247853230493(1).png)

**To configure the inbound and outbound security rules:**

1. From the Microsoft Azure homepage, go to **Network Security Groups**.
2. Select the Network security group you created in the previous section.
3. From the **Settings** section, click **Inbound security rules**.
4. Click **Add** to open the **Add inbound security rule** pane and configure the inbound WAN rule.
5. From the **Settings** section, click **Outbound security rules**.
6. Click **Add** to open the **Add outbound security rule** pane and configure the outbound WAN rule.
7. Repeat the previous steps for the LAN network security group.
8. To assign the network security group, go to the Virtual Network resource you previously created:

![network_security_group_assign.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247824218013(1).png)
  1. From the **Settings** section, click **Subnets** and select the subnet you are assigning the network security group to.
  2. Select the network security group from the dropdown menu.
  3. Click **Save**.

The following table shows sample inbound security rules.

| Name | Source > IP Addresses | Source port ranges | Destination | Dest port ranges | Protocol | Action | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WAN_inbound | 0.0.0.0/0 | * (any) | Any | 0-65535 | * (any) | Deny | 100 |
| WAN_outbound | 0.0.0.0/0 | * (any) | Any | 0-65535 | * (any) | Allow | 100 |
| LAN_inbound | 0.0.0.0/0 | * (any) | Any | 0-65535 | * (any) | Allow | 100 |
| LAN_outbound | 0.0.0.0/0 | * (any) | Any | 0-65535 | * (any) | Allow | 100 |

## Running the Azure Configuration Script

The Cato Networks configuration script helps you to create the Azure vSocket. The script automatically creates the VM for the vSocket, and then asks you for the necessary settings to configure it for your account.

You can also create a custom executable file with the settings for the vSocket, and run the script in non-interactive mode.

> [!NOTE]
> Notes:
> 
> - The default password for the vSocket WebUI is the **VM ID** for the vSocket VM. The VM ID is shown at the end of the vSocket script. We recommend you save the VM ID in a text file after the deployment is complete. For more about finding the VM ID, see below [Connecting to the Azure vSocket WebUI](/v1/docs/deploying-an-azure-vsocket-site-manually#h_01JHFPDKAFESEB6T21WDT5VMB5).
> - Make sure that all the virtual resources are in the same region before your run the configuration script.

Make sure that the vSocket image is uploaded to the Azure container, and that you have the configuration script. For more information, see [Copying the Azure vSocket VHD Image with SAS](/v1/docs/copying-the-azure-vsocket-vhd-image-with-sas).

### Assigning the vSocket VMs to an Availability Set (Optional)

The Cato vSocket script (`create_vm_from_vhd.sh`) lets you assign the vSockets to an Availability Set. This option is mostly used in a vSocket HA configuration when you want to make sure that the both vSockets are assigned to different Fault and Update domains. You must create the Availability Set BEFORE you run the Cato vSocket script.

You can't assign an Availability Set to VMs that are using different Availability Zones.

> [!NOTE]
> Note:
> 
> Azure doesn't allow you to assign a VM to an Availability Set after you create it.

Create a new Availability Set and configure the settings as follows:

- Assign it to the same resource group as the VM.
- Set the **Fault domains** and **Update domains** to **2**.

The following screenshot shows an example of a vSocket Availability Set:

![Availability Set Configuration.png](https://support.catonetworks.com/hc/article_attachments/24247812674333)

### Azure Information for the Script

The vSocket configuration script asks for the following information to configure the vSocket settings correctly:

- Azure account subscription and login details
  - Make sure that you only enter the resource IDs. Entering the resource names can cause the script to fail.
- Resource group
- Storage account
- Storage container
- Storage blob
- Storage type
  - Select the Standard_LRS storage option for non-accelerated instance Standard_D8ls_v5.
- Availability Set or Availability Zone
- Interface names on the VM
- Enter a name for the vSocket VM
- S/N for the vSocket from the Cato Management Application
- Azure VM instance type

### Running the Script

Run the configuration script in interactive mode to create and configure the Azure vSocket. As part of the script, you configure the name for the vSocket VM. You can't change this name at a later time.

Part of the script is choosing a SSD for the vSocket VM. In general, you can use the standard SSD for the VM.

For more information about the vSocket script, run `./create_vm_from_vhd.sh --help`.

#### Running the Script from the Azure Cloud Shell

You can use the Azure Cloud Shell in the Azure environment to run the Cato vSocket script.

**To use the Azure Cloud Shell to run the vSocket configuration script:**

1. From the top of the Microsoft Azure window, click Cloud Shell ![CloudSHell.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247805910429(1).png).
2. The **Welcome to Cloud Shell** panel opens in the bottom of the window, click **Bash**.
3. Go to the home directory in Azure and upload the script file manually or via CLI:
  1. **Manually** - Click **Upload** and select the script file you previously downloaded in [Copying the vSocket Image and Configuration Script](/v1/docs/deploying-an-azure-vsocket-site-manually#h_01JHFPDKAEBFXF9H6GP7756ZRW).
  2. **CLI** - download the file using the wget command - `wget https://catonetworks.hosted-by-files.com/CatoNetworks-Support/Public/Azure%20vSocket/create_vm_from_vhd.sh` .
4. Give executable permissions to the script, run `chmod u+x create_vm_from_vhd.sh`.
5. Run the Cato vSocket script, `./create_vm_from_vhd.sh --login`.
6. You will be prompted to authenticate with a dedicated code.
7. Once authenticated, the interactive mode is executed and you will be prompted to enter the vSocket settings.

The script creates and deploys the vSocket VM.

![azure_welcome_script_.png](https://support.catonetworks.com/hc/article_attachments/24247829161885)

#### Running the Script from macOS or Linux:

> [!NOTE]
> Note:
> 
> Before you run the script, make sure you are in the same directory as the script file.

**To run the vSocket configuration script from macOS or Linux:**

1. Give executable permissions to the script, run `chmod u+x create_vm_from_vhd.sh`.
2. Start the script and from the CLI run `./create_vm_from_vhd.sh --login`.
3. Select interactive mode and enter the vSocket settings.

The script creates and deploys the vSocket VM.

### Running the Script in Non-Interactive Mode

You can create a custom executable file that runs the vSocket script and automatically passes the environment variables. This means that you enter all the vSocket data for the script in the custom file and then the Cato script configures the vSocket in non-interactive mode.

The following sections describe the custom executable file and show a sample file.

> [!NOTE]
> Notes:
> 
> - Before you run the custom file, make sure you are in the same directory as the script file.
> - Make sure jq is installed on your operating system.

**To run the vSocket script in non-interactive mode:**

1. Create a new executable file that contains the environment variables for the Cato vSocket script.
2. Give executable permissions to the file. For example, run `chmod a+x &lt;file_name&gt;.sh`.
3. Run the file. The file passes the environment variables to the Cato script and creates the vSocket.

#### Explaining the vSocket Environment Variables

This section explains the environment variables that you configure in the custom executable file to create a vSocket in non-interactive mode. At the end of the list of variables is the command to run the Cato script.

AZ_VS_SUBSCRIPTION - Azure subscription name or ID

AZ_VS_RESOURCE_GROUP - Resource group name

AZ_VS_STORAGE_ACOUNT - Storage account name

AZ_VS_STORAGE_CONTAINER - Storage container name

AZ_VS_STORAGE_BLOB - VHD disk image blob name (inside of storage container)

AZ_VS_STORAGE_SKU - storage disk type SKU - **Standard_LRS**

AZ_VS_LAN_NIC - Name of management virtual NIC

AZ_VS_WAN_NIC - Name of WAN virtual NIC

AZ_VS_MNG_NIC - Name of LAN virtual NIC

AZ_VS_SERIAL_ID - Serial ID number of Cato vSocket for Azure site

AZ_VS_VM_NAME - Unique name for Azure vSocket VM

AZ_VS_VM_SIZE - Specifications for for Azure vSocket VM - **Standard_D8Is_v5**

./create_vm_from_vhd.sh - Runs the Cato script to create the vSocket VM.

#### Sample Custom File with Environment Variables

This section shows a sample file with the environment variables to create a vSocket in non-interactive mode.

export AZ_VS_SUBSCRIPTION=38a5bc1d-e3f6-4g50-h34i-kj01k23456789

export AZ_VS_RESOURCE_GROUP=CatoNetworks-Resource_Group

export AZ_VS_STORAGE_ACOUNT=catonetowksstorageinwe

export AZ_VS_STORAGE_CONTAINER=vhds

export AZ_VS_STORAGE_BLOB=vsocket-7.0-rel.vhd

export AZ_VS_STORAGE_SKU=Standard_LRS

export AZ_VS_LAN_NIC=vm-custom-data-mark-1VMNic

export AZ_VS_WAN_NIC=vm-custom-data-mark-2VMNic

export AZ_VS_MNG_NIC=vm-custom-data-mark-3VMNic

export AZ_VS_SERIAL_ID=ZZ-11-77-99-55-66

export AZ_VS_VM_NAME=vsocket-vm

export AZ_VS_VM_SIZE=Standard_D8Is_v5

./create_vm_from_vhd.sh

## Connecting to the Azure vSocket WebUI

After the vSocket is deployed, we recommend that you connect to the vSocket WebUI and change the password for the VM. The default password for the vSocket is the **VM ID** for the vSocket VM. The VM ID is shown at the end of the vSocket script.

**To connect to the vSocket WebUI and change the default password:**

1. Open a Web browser and connect to the vSocket, enter `https://&lt;vSocket management interface ip&gt;` .
  1. If connected behind Cato (site or SDP User) you can use the private IP of the management interface.
  2. If connected over the internet you can use the public IP of the management interface.
2. Log in to the WebUI with these credentials:
  - Username: admin
  - Password: VM ID

**To find the VM ID:**
    1. In the page for the Azure virtual machine, click **Overview**.
    2. Click to open the JSON and locate the VM ID in the JSON.

![Azure_VM_ID.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247840374429(1).png)
3. Change the password as prompted.
