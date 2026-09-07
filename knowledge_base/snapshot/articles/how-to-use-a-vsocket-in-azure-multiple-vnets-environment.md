---
title: "How to Use a vSocket in Azure Multiple VNets Environment"
slug: "how-to-use-a-vsocket-in-azure-multiple-vnets-environment"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-use-a-vsocket-in-azure-multiple-vnets-environment"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Use a vSocket in Azure Multiple VNets Environment

## Implementing Cato vSocket in Azure Multiple VNets Environment

This article describes how to deploy the Cato vSocket on a Microsoft Azure environment with multiple Virtual Networks (VNets). It introduces a cost-efficient solution of one vSocket deployment on a single VNet and connects multiple VNets together. The solution allows you to add additional VNets to your Azure environment without deploying any additional instances for the vSockets. It simplifies the management of the network topology, and you can manage the multiple VNets as a single site in the Cato Management Application.

### Solution Overview

The solution of implementing the Cato vSocket in a multi VNets environment, is connecting different VNets using the Azure virtual network peering. The VNet peering allows resources from different VNets to communicate with private IP ranges as if there are in the same network.

### Architecture

The architecture is based on a hub and spokes model. The VNet with the vSocket acts as a central hub, and all other VNets act as spokes. The hub and spokes VNets are connected with an Azure virtual network peering. This peering allows resources from different VNets to communicate with private IP ranges as if they’re in the same network.

The following diagram shows an example of 3 VNets environment: VNet1 is the hub VNet, and VNets 2 and 3 are the spokes VNets. The spoke VNets are connected to the hub VNet with VNet peering.

| ![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26623529870749.png) |
| --- |

### Implementing Cato vSocket and connecting Multiple VNets

To implement a vSocket in a multi VNet environment, you must complete the following steps:

1. Deploy the Azure vSocket to the hub VPC
2. Add a virtual network peering between the spoke VNets and the hub VNet
3. Create the route tables for the spokes VPC
4. Add routes to the route table for the spokes VNets
5. Associate the route table to the spoke VNets subnets
6. Configure the network routed ranges in the Cato Management Application

#### 1. Deploying the Azure vSocket

Create the Azure vSocket site in the Cato Management Application and deploy the Azure vSocket in the hub VNet. For more information, see [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace).

#### 2. Adding a Virtual Network Peering

Create a new VNet peering between each spoke VNet that connects to the vSocket hub VNet. This peering provides connectivity between the hub and the spoke VNets and allows them to send traffic from one peering side to another. The peering must be created for both directions (For example, VNet1 to VNet2 and VNet2 to VNet1). You must enable the **Allow forwarded traffic** option for both directions. The following screenshot shows a sample of VNet peering configuration between VNet2 (spoke) and VNet1 (hub):

![Add_Peering.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26623789351325.png)

#### 3. Creating a Route Table

Create a route table for each one of the spokes VNets that allows you to route traffic between them. The following screenshot shows a sample route table configuration for the spoke VNet2.

![CreateRoute.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26623484776605.png)

#### 4. Adding Route to the Route Table

Add routes to each VNet route table to allow the spoke VNets to route the traffic to the hub VNet. Set the **Next hop type** to Virtual appliance and set the **Next hop address** to the IP address of the vSocket LAN interface.

The following screenshot shows a sample route configuration from a spoke VNet to the vSocket LAN IP address of the hub VNet.

![Add_route.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26623596689437.png)

#### 5. Associating the Route Table to a Subnet

Associate the route table to the VNet subnet. Azure allows you to route traffic only if the route table is associated with the VNet route table. The following screenshot shows the spoke VNet route table associated with the subnet.

![RouteTable_Subnets.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26623506675869.png)

#### 6. Configuring the Network Ranges for the VNets

Configure the LAN ranges of the VNets in the Cato Management Application (Configuration>Azure Site>Networks<LAN) and add a **Routed** range for each VNet that is connected to the virtual network peering. Use the first IP address of the vSocket LAN native range for the gateway. The following screenshot shows a sample configuration of two spoke VNets with different routed IP ranges. Each range is configured with the gateway IP address of the LAN native range.

![blobid5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26623530238237.png)

**Note:** Make sure you configure network rules that route traffic to the Azure vSocket site. For more about network rules, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

After you complete the deployment, you can verify that hosts in the spoke VNet have internet access and can communicate with other sites in your account.
