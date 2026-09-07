---
title: "Integrating Cato with Azure vWAN"
slug: "integrating-cato-with-azure-vwan"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/integrating-cato-with-azure-vwan"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato with Azure vWAN

This article provides information about Azure vWAN and how to integrate Azure virtual resources and topology with your Cato account using Terraform.

> [!NOTE]
> Note:
> 
> Issues concerning vWAN and API integration are subject to the guidelines outlined in [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## What is Azure Virtual WAN

Azure Virtual WAN (vWAN) is a unified networking service that combines various networking, security, and routing features into a single operational interface. It supports branch connectivity via SD-WAN or VPN, site-to-site and remote user VPN connections, private connectivity through ExpressRoute, and intra-cloud connectivity for virtual networks. Utilizing a hub-and-spoke architecture, it enables global transit network capabilities with Azure regions acting as interconnected hubs, facilitating seamless any-to-any connectivity. This design simplifies network management and enhances performance and scalability for distributed environments.

## Architectural Overview

Cato uses IPsec to connect your Azure vWAN environment to the Cato Cloud and then Terraform can automatically integrate Azure vWAN with your account.

![vWAN_Diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25806937764893.png)

In the sample configuration above, the Cato Cloud uses two IPsec connections to each of the Azure Hubs. This provides redundancy in the event that one of the connections is unavailable, so you can still access your assets in Azure.

These are the components in the sample configuration above:

- **vWAN:** The Virtual WAN (vWAN) resource is a virtual overlay of the Azure network, comprising multiple resources. It includes links to all the hubs within the vWAN. Each vWAN resource is isolated and cannot share a common hub. Additionally, hubs within different vWANs do not communicate with each other.
- **Hub:** A virtual hub is a Microsoft-managed virtual network (VNet) that contains various service endpoints to enable connectivity from your on-premises network (VPN site). When you create a virtual WAN hub from the portal, it generates a VNet and a VPN gateway. Each Azure region can have only one hub.
- **Hub-to-hub connection:** In a Virtual WAN, all hubs are interconnected. This means that a site, remote user, or assets behind a VNet connected to a local hub can communicate with another site or VNet through the full mesh architecture of the connected hubs.
- **Sites:** A site can be the HQ/DC or Branch as in the diagram above, or it can be a virtual entity located within the Azure vWAN. Sites connect to the Cato Cloud through various connection types supported by Cato, for example, Sockets.
- **IPsec connection:** This is used to connect the Azure vWAN to your account in Cato.

## Prerequisites

- The information in this article is based on the assumption that you already created a Virtual WAN and Virtual Hubs in the Azure Portal. For more information about creating the necessary resources in Azure:
  - [Virtual WAN](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#openvwan)
  - [Virtual Hub](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#hub)
- Terraform is already set up to have access to your Azure environment. For more information, refer to the [Terraform documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret).

## Using Terraform to Create the Integration

Cato Networks uses Terraform to create the resources required for integrating with Azure vWAN, including:

- Creating the VPN Gateway Connection in your Azure account
- Creating a site in your Cato account. You need to create a separate site for each Azure Hub to which you want to connect
- Creating the Primary and Secondary IPsec connections (to different PoPs) between the new site and the Azure Hub
- Defining and configuring the BGP peers in the new site

### Retrieving the Terraform Module

The Cato module for integrating with Azure vWAN is available from Cato's Terraform registry at: [https://registry.terraform.io/modules/catonetworks/azure-vwan/cato/latest](https://registry.terraform.io/modules/catonetworks/azure-vwan/cato/latest)

Download the relevant module and ensure you have the following files:

- `main.tf` includes the API calls that the Terraform runs, for example, connecting to the providers, associating allocated IP addresses with the site, and more
- `variables.tf` all of the parameters for both the Azure and Cato resources, for example, the Cato API token, Cato account ID, the name of the IPsec site, and more
- `version.tf` specifies the required providers for both Azure and Cato, and their respective versions

### Modifying the variables.tf File

The `variables.tf` file contains all of the parameters that you will need to get information from your Azure and Cato accounts, as well as the parameters you need to provide to create the resources that you will need in your account.

**To modify the variables.tf file:**

1. Open the file in a text editor.
2. Provide the required information as outlined in the table, below.
3. Save the file.

| Parameter | Description |
| --- | --- |
| cato_baseurl | The location of the Cato API The default value is: [https://api.catonetworks.com/api/v1/graphql2](https://api.catonetworks.com/api/v1/graphql2) |
| azure_subscription_id | The Azure subscription you are integrating with. This value can be found in your Azure account under Home > Subscriptions. |
| azure_vwan_hub_id | The Azure Hub to which you want the Cato IPsec site to connect. The Hub ID can be found in your Azure account under Home > vWANs > <vWanName> > Hubs. Click **JSON view** and copy the contents of the id field. |
| cato_token | The [Cato API token](/v1/docs/generating-api-keys-for-the-cato-api) |
| cato_account_id | The ID associated with your Cato Networks account. This is located in the CMA under **Administration > General Info**. |
| site_name | The name of the IPsec site you are creating in the CMA |
| cato_site_address_cidrs | The local ranges of the sites in CMA that Azure will be communicating with If you have multiple ranges, enter them as a comma-separated list in CIDR format |
| connection_bandwidth | Define how much bandwidth to allocate for the Azure VPN connection (in Mbps) |
| vpn_site_primary_link_name | The name of the primary IPsec connection between the site in the CMA and Azure, as it will appear in Azure |
| vpn_site_secondary_link_name | The name of the secondary IPsec connection between the site in the CMA and Azure, as it will appear in Azure |
| site_description | A description of the IPsec site in the CMA |
| site_location | Enter the location parameters for the IPsec site in the CMA. This includes the following information: - City - Country Code - State Code - Timezone |
| cato_primary_public_ip | Cato primary public IP (already [allocated to your account](/v1/docs/allocating-ip-addresses-for-the-account), available in Network > IP Allocations) |
| cato_secondary_public_ip | Cato secondary public IP (already allocated to your account, available in Network > IP Allocations) |
| bgp_enabled | Determines if BGP should be enabled for the IPsec site. Cato recommends that you enable BGP peering |
| cato_asn | The Cato ASN |
| cato_primary_peering_address | The primary Cato peering address |
| cato_secondary_peering_address | The secondary Cato peering address |
| vpn_gateway_connection_name | In Azure, the name of the VPN gateway connection |
| vpn_gateway_name | In Azure, the name of the VPN gateway |
| vpn_site_name | The Cato IPsec site name as it appears in Azure |

### Running the Terraform Module

Once you set up the `variables.tf` file and make any modifications that you want to `main.tf`, you can run the Terraform module.

> [!NOTE]
> Notes:
> 
> - The module takes approximately 30 minutes to complete
> - If you need to run the module more than once to create additional sites, wait until the first module execution completes before starting another one

**To run the Terraform module:**

1. Navigate to the folder in which all of the Terraform files are located.
2. Run the following command: `terraform apply`
3. Terraform will present you with a confirmation request explaining that 4 resources are going to be created. Approve the request to start the process.

The following resources are created:

- Azure VPN Gateway Connection
- Cato IPsec site
- Primary and Secondary IPsec connections between the new site and the Azure Hub
- BGP peers in the new site

### Verify the Integration

Once the Terraform module is completed, you can verify that the integration was successful.

**To verify the integration was successful:**

1. In the CMA, navigate to **Network > Sites** and look for the IPsec site you defined.
2. Click on the site and navigate to **Site Configuration > IPsec**.
3. Under the **Primary** and **Secondary** sections, you should see the new connections that were created.

If the **Status** of the connections is still **Disconnected**, wait a few minutes and refresh the page.
  - Check the values of the **Private IPs** and **Authentication Identifier**
4. Navigate to **Site Configuration > BGP**.
5. Verify that the BGP peers were created, and click **Show BGP Status** to verify that there is a connection.

If the **Status** of the connections is still **Disconnected**, wait a few minutes and refresh the page.
