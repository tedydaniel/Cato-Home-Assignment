---
title: "How to Implement Cato vSocket in AWS Multiple VPCs Environment"
slug: "how-to-implement-cato-vsocket-in-aws-multiple-vpcs-environment"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-implement-cato-vsocket-in-aws-multiple-vpcs-environment"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Implement Cato vSocket in AWS Multiple VPCs Environment

## Implementing Cato vSocket in AWS Multiple VPC Environment

This article describes how to deploy the Cato vSocket in an Amazon AWS multiple VPC environment. It introduces a cost-efficient solution where you can deploy a single vSocket instance for multiple VPCs rather than deploying multiple vSocket instances in your AWS environment. The solution allows you to add additional VPCs to your AWS environment without deploying any additional EC2 instances for the vSockets. It simplifies the management of the network topology and you can manage the multiple VPCs as a single site in the Cato Management Application.

### Solution Overview

The solution to implement the Cato vSocket in a multiple VPC environment, is to deploy the vSocket on a single VPC and connect all your VPCs using an AWS transit gateway. The transit gateway allows you to route the traffic between the attached VPCs. Therefore, you must attach the transit gateway to each VPC that you want to connect. The transit gateway propagates the route tables of the attached VPCs and allows connectivity between the different CIDRs in different VPCs.

### Architecture

The architecture is based on a hub and spokes model. The VPC with the vSocket acts as a central hub and all other VPCs act as spokes. The hub VPC manages and centralizes the outbound traffic from the AWS environment to the Cato Cloud. The following diagram shows an example of a multiple VPCs environment in AWS with one vSocket connected to the Cato Cloud.

![blobid0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248075669149.png)

This diagram introduces an AWS environment with 3 VPCs: VPC 1 is the (central hub) VPC with the Cato vSocket), and VPC 2 and VPC 3 are the spokes. Each one of the VPCs has a route table with a different subnet. When attaching the VPCs to the transit gateway, it propagates all the VPC route tables to route the traffic between the different VPCs.

### Implementing Cato vSocket and Connecting Multiple VPCs

First you must deploy a vSocket in a VPC. Then, create an AWS transit gateway and transit gateway attachments for the VPCs. To implement Cato vSocket in a multiple VPC environment:

1. Deploy the vSocket in AWS hub VPC
2. Create a transit gateway
3. Create transit gateway attachments for VPCs
4. Create a transit gateway route table
5. Configure network routed ranges in the Cato Management Application

#### 1. Deploying a vSocket in AWS

Deploy a Cato vSocket to provide the connectivity to the Cato Cloud and to the Internet. For more information, see [Deploying an AWS vSocket Site Manually](/v1/docs/deploying-an-aws-vsocket-site-manually).

When you connect the spoke VPCs to the hub VPC, deploy a transit gateway and attach them to it. The transit gateway then creates a VPN connection between the different VPCs.

#### 2. Creating a Transit Gateway

Once you’ve deployed a vSocket, create an AWS transit gateway. The transit gateway is a cloud-based router that centralizes the VPN connections between the attached VPCs. The following screenshot shows an example of an AWS transit gateway configuration:

![blobid1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248092891805.png)

#### 3. Attaching the VPCs to the Transit Gateway

Create transit gateway attachments for each VPC. The transit gateway attachments connect the VPC to the transit gateway. The attachment must be associated with a route table and allows connectivity between the attached VPCs. When creating a transit gateway attachment for the hub VPC, you must select the vSocket LAN subnet. The following screenshot shows three transit gateway attachments, one for each VPC:

![blobid2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248067885469.png)

Note: You can add a transit gateway attachment for different regions but not for different accounts in the same region.

#### 4. Configuring Routes Between the Transit Gateway and the VPCs

Create a transit gateway route table for the transit gateway and configure the routes for each transit gateway attachment. The transit gateway propagates the VPCs’ route tables and allows connectivity between the attached VPCs. The following screenshot shows an example of a transit gateway route table with the propagations of the attached VPCs:

![blobid4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248075894557.png)

#### 5. Configuring the Network Ranges for the VPCs

Configure the LAN ranges of the VPCs in the Cato Management Application (Configuration>AWS Site>Networks>LAN) and add a **Routed** range for each VPC that is attached. Use the first IP address of the IP range for the gateway. The gateway IP address is the next hop for the spoke VPC IP range. The following screenshot shows an example of a routed IP ranges configuration for the two spoke VPCs.

![blobid5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248093176733.png)

**Note**: Make sure you configure network rules that route traffic to the AWS vSocket site. For more about network rules, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

After you complete the deployment, you can verify that hosts in the spoke VPC have internet access and can communicate with other sites in your account.
