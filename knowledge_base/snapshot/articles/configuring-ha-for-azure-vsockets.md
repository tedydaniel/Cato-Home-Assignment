---
title: "Configuring HA for Azure vSockets"
slug: "configuring-ha-for-azure-vsockets"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/configuring-ha-for-azure-vsockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring HA for Azure vSockets

This article explains how to configure a site with two vSockets that provide high availability (HA) for a site in the Microsoft Azure cloud.

## Overview of High Availability vSocket in Azure

To provide redundancy for vSockets within an Azure site, deploy two vSockets in the same Azure virtual network (VNet), and set them to work in a high availability configuration. The vSockets operate in active/passive mode, and the LAN links are used to send keepalive messages between the vSockets.

The Azure HA configuration uses a Floating IP address, which is bound to the LAN interface for the active vSocket. When there is a failover, the Floating IP moves to the secondary vSocket LAN interface. The route tables use this Floating IP as the next hop for traffic that is sent over the Cato Cloud.

Azure HA supports multiple Availability Zones. Alternatively, you can use the Availability Sets to make sure that both vSockets are deployed in different Fault and Update domains in Azure.

### Sample Diagram of Azure HA Virtual Network

The following network diagram shows a sample HA vSockets configuration for an Azure site.

![Azure_HA_Deployment.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864615094941.png)

The primary and secondary vSockets are in the same VNet. The LAN interfaces are 10.102.2.10 (primary) and 10.102.2.11 (secondary). The Floating IP is 10.102.2.200 and is configured as the next hop for the LAN route table.

The normal traffic flow for this network is:

1. VM1 sends traffic to the Internet.
2. According to the LAN route table, the next hop for the traffic is 10.102.2.200, which is configured as the secondary IP address for the LAN interface of the primary vSocket.
3. The primary vSocket is active and sends the traffic over the WAN interface to the Internet.

### Azure vSocket Failover Workflow

This is the workflow when the primary active vSocket fails over to the secondary standby one in an Azure site. The following diagram illustrates the failover, the numbers correspond to the items in the steps below:

![Azure_HA_Failover_Callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864586016285.png)

1. In normal operation, the primary vSocket has the active role, and the secondary vSocket has the standby role.
  1. The Floating IP (secondary IP address on the LAN interface) is attached to the primary vSocket (item 1a).
  2. The LAN route table prefixes use the Floating IP as the next hop (item 1b).
2. The primary (active) vSocket goes down (item 2).
  1. The secondary (standby) vSocket stops receiving keepalive packets from the primary vSocket (item 2a).
3. The secondary vSocket issues an API call to the Azure API gateway to make the following changes to the LAN interfaces on each vSocket:
  1. Remove the Floating IP (the secondary IP address) from the LAN interface on the primary vSocket (item 3a).
  2. Add the Floating IP as the secondary IP address for the LAN interface on the secondary vSocket (item 3b).
4. The secondary vSocket is now the active vSocket and passes traffic for the site in both directions (item 4).
5. When the primary vSocket recovers, it resumes the active role, and the secondary vSocket returns to standby status. (The primary vSocket issues an API call to move the Floating IP back as a secondary IP address for its LAN interface.)

> [!NOTE]
> Note:
> 
> Due to reasons related to the Azure infrastructure, the Network Interface configuration update can take up to 120 seconds and may cause a delay in the HA failover.

### Prerequisites for Azure High Availability

- High availability in Azure is supported for vSockets that are using Socket version 11.0 or higher
- Download the Azure HA configuration script from the Cato repository, see [Copying the Azure vSocket VHD Image with SAS](/v1/docs/copying-the-azure-vsocket-vhd-image-with-sas)
- Both vSockets must be the same Azure VM instance type (for example, D2s v4)
- The Azure vSockets must have access to a public DNS server. Make sure that the VNet isn't configured to only use a private DNS server **Note:** The vSocket VM must be restarted after any DNS changes made to the VNETs used by the vSocket.
- If you are using separate resource groups for the VNet and the vSocket VMs, make sure that the storage container blob is in the resource group as the VMs and the VHD image
- Each vSocket requires outbound connectivity to the following resources:
  - VirtualNetwork - DNS and HTTP
  - Azure Resource Manager - HTTPS
  - The management interface requires Internet access for public DNS servers (if configured, UDP/53) and management.azure.com (TCP/443)

#### Setting Admin Permissions to Configure High Availability

This section explains the correct Cato and Azure permissions for the admin to configure vSocket HA. If you don't have the correct permissions, then it's possible the Cato HA script can't create an HA configuration between the vSockets.

- Must have admin permissions for the Cato Management Application and [owner permissions](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) for Azure
- If you are using Privileged Identity Management (PIM) or any identity token mechanism in Azure, [assign the maximum privilege](https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-resource-roles-assign-roles) to the necessary resource group before you run the HA script
- If there are multiple Azure resource groups, then you must have owner permissions for both resource groups

### Using Availability Zones for Azure High Availability Configurations

You can choose to assign each VM to a different Azure Availability Zone as part of the HA configuration script to protect your applications and data from Azure data center failures. Create the Availability Zones before you run the HA script.

You can't assign VMs to different Availability Zones that are using different Availability Sets.

> [!NOTE]
> Note:
> 
> Azure only supports standard SKU public IP addresses for Availability Zones (and other zone redundant configurations). Before you deploy the vSocket HA configuration, make sure that you configure the proper SKU for the IP addresses.

The following network diagram shows a sample HA vSockets configuration with different Availability Zones for an Azure site.

![Azure-HA - availability Zones (KB).png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864583409309.png)

### Known Limitations

- For Socket versions earlier than v14.0, the primary vSocket LAN IP is used for BGP peering. This does not survive failover to the secondary vSocket.
  - Starting with v14.0, in vSocket HA configurations, the Floating IP is used for BGP peering. Make sure to define the Floating IP in the neighboring BGP router.

Due to reasons related to the Azure infrastructure, the Network Interface configuration update can take up to 120 seconds and may cause a delay in the HA failover.
- For existing configurations, to assign a VM to an Availability Zone, you must create new VMs and redeploy the vSockets (see [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace))

## Deploying vSocket High Availability in Azure

Deploy the vSockets on the Azure virtual machines (VMs) as the primary and secondary vSockets for the site.

For Azure HA configurations, during failover there is an API call that automatically adds the Floating IP to the LAN interface of the standby vSocket and deletes settings configured on the LAN interface (including the LAN NSG). Don't manually configure the Floating IP on the LAN interface of a vSocket. The Cato HA script assigns the Floating IP to the primary vSocket LAN interface and then reboots the vSockets (see step 7 and 8 below).

This is a high-level workflow of the process to deploy a vSocket HA configuration.

1. For new sites, create a new site in the Cato Management Application and run the Cato Azure vSocket script to deploy the primary vSocket. (For existing sites, skip this step.)
2. After you create the site, the Cato Management Application assigns a unique serial number (S/N) to it. We recommend that you copy and paste the serial number in a text file.
3. Verify that the primary vSocket is running Socket version 11.0 or higher.
4. Add the secondary vSocket to the site in the Cato Management Application.
5. Deploy the secondary vSocket with the Cato Azure vSocket script. Both vSockets must be in the same VNet.

The only virtual resources that you need to create for the secondary vSocket are new network interfaces for the WAN, LAN, and MGMT subnets.
6. Verify that both the primary and secondary vSockets have connectivity to the Cato Cloud.
7. Run the Cato HA script to apply the HA configuration to the vSockets.
8. Restart both the primary and secondary vSockets.
9. Update the Azure route table to use the Floating IP as the next hop.
10. Confirm that the HA status for the vSockets and run the API test from the Socket WebUI.

> [!NOTE]
> Note:
> 
> When you configure the IP settings for the site, make sure that you don't use IP addresses that are reserved by Azure. You can't use the first four IP addresses and the last IP address in a subnet CIDR block.

For more about Azure reserved IP addresses, see [Azure documentation](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-faq#configuration).

### Deploying the Primary vSocket in Azure

Complete these steps to deploy the primary vSocket on a VM. For existing Azure sites, upgrade the primary vSocket to version 11.0 or higher. If you want to assign the vSocket to an Availability Set, see below [Assigning the vSocket VMs to an Availability Set (Optional)](/v1/docs/configuring-ha-for-azure-vsockets#assigning-the-vsocket-vms-to-an-availability-set-optional).

Then continue below with [Adding the Secondary vSocket to an Azure Site](/docs/configuring-ha-for-azure-vsockets#UUID-15159dec-7ed5-b701-faa9-991b06a310e9_N1625145201753).

**To deploy the primary vSocket for a new site:**

1. Add a new Azure site to the Cato Management Application.
2. Install the primary vSocket on the VM.
  - Remember to use the same resource group for both vSocket VMs.
  - If necessary, create the Availability Set for the vSocket VMs.

For more about installing a vSocket in Azure, see [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace).

#### Assigning the vSocket VMs to an Availability Set (Optional)

The vSocket script (`create_vm_from_vhd.sh`) lets you assign the vSockets to an Availability Set. This option is mostly used in a vSocket HA configuration when you want to make sure that both vSockets are assigned to different Fault and Update domains. You must create the Availability Set BEFORE you run the CatovSocket script.

> [!NOTE]
> Notes:
> 
> - Azure doesn't allow you to assign a VM to an Availability Set after you create it
> - You can't assign an Availability Set to VMs that are using different Availability Zones

Create a new Availability Set and configure the settings as follows:

- Assign it to the same resource group as the VM
- Set the **Fault domains** and **Update domains** to **2**

The following screenshot shows an example of a vSocket Availability Set:

![AvailabilitySet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864566996125.png)

### Adding the Secondary vSocket to an Azure Site

After the Cato Management Application detects that the primary vSocket is upgraded to version 11.0 or higher, the **Add Secondary Socket** option is shown in the **Network > Sites > Site Configuration > Socket** page.

When you add the secondary vSocket to the site, a pop-up window opens where you enter the following settings:

- LAN Interface IP - IP address for the LAN interface of the secondary vSocket
- LAN Floating IP - IP address for the Floating IP that is used for the Azure HA configuration

The Cato Management Application uses the LAN Interface IP address as the management IP address for the secondary vSocket. This LAN interface is also used for the HA keepalive packets.

After you add the secondary vSocket to the site, the Cato Management Application does the following:

- Generates the vSocket serial number for the new vSocket (this serial number is used when you run the Cato script to install the vSocket on the VM)
- Enables the **High Availability Configurations** section for that site
- Modifies the **Networks** section Native Range, the Local IP is replaced with the Floating IP

For more about network segments in the HA site, see below [Overview of Azure High Availability Network Segments in the Cato Management Application](/v1/docs/configuring-ha-for-azure-vsockets#overview-of-azure-high-availability-network-segments-in-the-cato-management-application).

![Azure_vSocket_HA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864615660573.png)

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

Use this S/N when you install the secondary vSocket on the VM.

#### Changes to the Socket Page

After you add the secondary vSocket to the site, in the **Socket** page, the **Destination** for the LAN1 link is automatically set to **LAN & HA**.

### Deploying the Secondary vSocket in Azure

Create and deploy the secondary vSocket in the same Azure VNet as the primary vSocket.

1. Make sure that all of the virtual resources for the site are in the same Azure resource group.
  - Based on your organizational requirements, you can assign the VNET to one resource group and the other virtual resources to a different resource group.
  - If necessary, create the Availability Set for the vSocket VMs.
2. Use the same subnets for the primary and secondary vSockets.
3. Create new virtual interfaces for each subnet.
4. Verify that both the primary and secondary vSockets have connectivity to the Cato Cloud.
5. Run the Cato Azure vSocket script:
  1. Select the resources for the secondary vSocket.
  2. Use the serial number for the secondary vSocket in Azure that was generated by the Cato Management Application.

For more about installing a vSocket in Azure, see [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace).

#### Using Different Resource Groups for the VNET and the VMs

The Cato HA script (`create_ha_settings.sh`) lets you assign the VNET to one resource group and use a different resource group for the other virtual resources (NICs, vSocket, storage container, route tables, and so on). When you are running the Cato HA script, there are separate questions that ask you to assign the VNET resource group and the VM resource group.

If you are using the same resource group for the VNET and the VMs, make sure that you select the same resource group for both options in the Cato HA script.

> [!NOTE]
> Note:
> 
> Make sure that the VHD image is in the storage container blob that is in the VM resource group.

### Running the Cato High Availability Script

After you deploy the secondary vSocket to the VNet, both vSockets have the Master role (split-brain). Run the Cato HA script **create_ha_settings.sh** to apply the HA configuration to the vSockets. For more information about downloading the file with the Cato HA script, see [Socket and vSocket Image Files](https://support.catonetworks.com/hc/en-us/articles/11503595325085-Socket-and-vSocket-Image-Files#h_01HPEVA883H8GCW15MWARHD5Z2) (you must be signed in to view this article).

The Cato HA script creates a Managed Identity, which is the identity created and later assigned, with the role of Contributor to the VMs (both members of the HA). In addition, the Cato HA script creates two custom scripts, one for each member of the HA group, that create a configuration file with all of the information required by the VM in the event of failover. This includes the subscription_id names of the NICs, location of the VMs, and more.

> [!NOTE]
> Important:
> 
> Before you run the Cato HA script:
> 
> - The primary and secondary vSockets must have connectivity to the Cato Cloud
> - Make sure that you have the correct Azure admin permissions, see above [Setting Admin Permissions to Configure High Availability](/v1/docs/configuring-ha-for-azure-vsockets#setting-admin-permissions-to-configure-high-availability)

**To run the Cato HA script:**

1. In the **High Availability** section, confirm that the primary and secondary vSockets have connectivity to the Cato Cloud:
  - The **Connection toCato Cloud** status for each vSocket shows **Connected**
  - See below, [Showing the High Availability Status in the Cato Management Application](/v1/docs/configuring-ha-for-azure-vsockets#showing-the-high-availability-status-in-the-cato-management-application)
2. Run the Cato HA script **create_ha_settings.sh** to apply the HA configuration to the vSockets.
3. Restart the VMs with the primary and secondary vSockets.
4. Update the relevant route table entries in Azure to use the Floating IP as the next hop.

### Confirming the Azure vSockets for High Availability Status

After you successfully run the HA script, verify that the vSockets are configured correctly for HA functionality:

- Verify the HA status in the **High Availability** section
- From the Socket WebUI, ping the Floating IP and test the HA API calls

For help with problems related to deploying the HA configuration, see [Troubleshooting Azure HA Deployment](/v1/docs/azure-ha-vsocket-troubleshooting).

#### Showing the High Availability Status in the Cato Management Application

The **High Availability** section for the site shows the HA status for the vSockets. After you deploy the secondary vSocket, it automatically connects to the site.

**To confirm the high availability status for the site:**

1. From the Cato Management Application's navigation menu, click **Network > Sites**.
2. From the navigation menu, click **Site Monitoring > Network Analytics**.
3. From the top of the page, verify the status of the following items:
  - **Status** is **Connected**
  - **HA Status** is **Ready**
  - **Master** is **Primary**
  - **Socket** is **vSocket Azure**

![Azure_HA_Status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864597986461.png)

For more about HA and failover behavior, see [Socket High-Availability (HA): Background and Failover Conditions](/v1/docs/what-is-socket-ha).

#### Testing High Availability from the Socket WebUI

You can use the Network Tools in the Socket WebUI to test HA functionality for the vSockets. You can ping the Floating IP for the HA configuration to verify that it is configured correctly. The **High Availability** section shows the LAN Floating IP. You need to run the test for both the primary and secondary vSocket.

The vSocket performs an API call to the Azure API proxy to verify that the role and identity settings were configured correctly by the HA script. It also verifies that the vSocket can successfully communicate with the API proxy.

For more about using the Socket WebUI, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

**To test the Azure HA configuration:**

1. From the navigation menu, select **Site Configuration > Socket**.
2. From the **Actions** drop-down menu for the Primary vSocket, select **Socket WebUI**.

The Socket WebUI opens in a new tab.
3. Click the **Tools** tab.
4. In the **Network Tools** section, click the **Ping** tab.
5. Ping the Floating IP:
  1. In **Route via**, select **LAN1**.
  2. In **Hostname/IP**, enter the Floating IP.
  3. Click **Run**. The window shows if the ping succeeds or fails.
6. In the **Network Tools** section, click the **API Test Tool** tab.
7. Click **Run Test**. The window shows if the HA API test succeeds or fails.
8. Repeat steps 2-7 for the secondary vSocket.

#### Troubleshooting a Failed Azure API Test

If the Azure API test fails, an error message is displayed to help you troubleshoot the issue.

| API Test Error Message | Suggested Troubleshooting Steps |
| --- | --- |
| Azure API test failed – can’t authenticate to the API proxy. Make sure that Azure access control (IAM) settings are correct. | The Azure admin doesn't have sufficient permissions to make changes to the virtual resources. See above, [Setting Admin Permissions to Configure High Availability](/v1/docs/configuring-ha-for-azure-vsockets#setting-admin-permissions-to-configure-high-availability). |
| Azure API test failed. Verify that the NIC settings on the vSocket VM instance are correct. | - Check that the NICs, subnets, and VMs belong to the same resource group. See above [Using Different Resource Groups for the VNET and the VMs](/v1/docs/configuring-ha-for-azure-vsockets#using-different-resource-groups-for-the-vnet-and-the-vms). - Make sure that the Azure admin has permissions to create a role and apply it to the NICs, subnets, and VMs. - Make sure that the Azure admin has permissions to change NIC properties. |

## Working with Network Segments for Azure High Availability Sites

This section explains how to use the **Networks** section to manage network segments for the Azure HA site.

### Overview of Azure High Availability Network Segments in the Cato Management Application

When you add the secondary vSocket to the Cato Management Application, the network segments in the **Networks** section are automatically updated to include the settings for the Floating IP. The Floating IP replaces the Local IP for the Native Range for the site.

### Adding Routed Ranges (Static Routes)

You can add Routed ranges to the Azure HA site in the same way as for a physical Socket site.

- The IP address for the default Azure router (VNet router) is the first host IP address of the Native Range subnet
- If you are using a third-party virtual appliance (for example, a firewall) in your Azure environment, make sure that the IP address is within the Native Range for the site
- You can configure the Floating IP address in the Cato Management Application in the **Site Configuration > Sockets > High Availability Configuration** for the site

## Managing Azure High Availability

This section explains how to manage HA for the Azure site:

- Show the HA status for each vSocket
- Change the Floating IP for the site
- Change the management IP addresses for the vSockets
- Disable HA for the site and remove the secondary vSocket

### Showing the High Availability Information and Status

The **Network > Sites > Socket** page for the site shows the HA status for the primary and secondary vSockets.

| Item | Description |
| --- | --- |
| HA Status | The High Availability status for the site (**Ready** or **Not Ready**), only shows Ready when each HA status indicator is OK |
| **Connected** (status indicator) | The status ![allow.svg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864598066205.svg-xml) indicates that both vSockets have WAN connectivity to the Cato Cloud |
| **Keepalive** (status indicator) | The status ![allow.svg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864598066205.svg-xml) indicates that one vSocket is the master and one is the standby (If both vSockets are status master, then there is an HA split brain issue) |
| **Same Version** (status indicator) | The status ![allow.svg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26864598066205.svg-xml) indicates that both vSockets are running the same Socket version |

### Changing the IP Settings for the Site

If you change the IP address settings for the vSockets in Azure, you need to update the same settings in the Cato Management Application. These are the settings that you can configure:

- Native Range subnet - Use the **Networks** section for the site
- Floating IP - Use the **Networks** or **High Availability** section for the site (the new value is automatically updated to the other section)
- Management IP - Use the **High Availability** section for the site

#### Changing the Native Range Subnet

Use the **Networks** section to change the Native Range subnet.

**To change the Native Range subnet for the site:**

1. From the navigation menu, click **Network > Sites** and select the Azure site.
2. From the navigation menu, select **Site Configuration > Networks**.
3. Edit the **Native** range, enter a new value for the **Subnet**.
4. Click **Apply**. The **Edit IP range** panel closes.
5. Click **Save**.

#### Changing the Floating IP and Management IP

Use the **High Availability** section to change the Floating IP and the Management IP. You can also change the Floating IP in the Networks section.

**To change the Floating or Management IP for a site:**

1. From the navigation menu, click **Network > Sites** and select the Azure site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. Expand the **High Availability Configurations** section.
4. Enter the new **Primary Management IP**.
5. Enter the new **Secondary Management IP**.
6. Enter the new **LAN Floating IP**.
7. Click **Save**.

### Disabling High Availability for the Azure Site

You can remove the secondary vSocket from an Azure site and disable HA for that site. After you remove the secondary vSocket from the Cato Management Application, the deployed vSocket can no longer connect to the Cato Cloud. The settings for the site are restored to the configuration for a single vSocket:

- The **High Availability** section is disabled and no longer appears on the page
- In the **Networks** section, the Local IP replaces the Floating IP

> [!NOTE]
> Note:
> 
> You can't undo the **Unassign Socket** action. The serial number for the secondary vSocket is no longer valid.

If you want to add the secondary vSocket again, you must install a new vSocket on the VM with the new serial number.

**To disable HA for the Azure site:**

1. From the navigation menu, click **Network > Sites** and select the Azure site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the **Secondary** vSocket, click **Unassign**.
4. In the Warning window, click **OK**. HA is disabled for the site, and the secondary vSocket is removed from it.

## Analyzing High Availability Events

The [Events page](/v1/docs/analyzing-events-in-your-network) shows all the HA Connectivity events for your account.

### Explaining the High Availability Events Fields

The Events fields and events are the same for Socket HA and for vSocket HA. These are the HA events:

| Field | Description |
| --- | --- |
| Socket role | Shows if the event was generated by the primary or secondary vSocket |
| Event subtype - Socket Fail-Over | The failover process is initiated for the site |

For more about events that are generated as part of the failover process, see [Socket HA Failover Events](/v1/docs/what-is-socket-ha).
