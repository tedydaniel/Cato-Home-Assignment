---
title: "Deploying an AWS vSocket Site Manually"
slug: "deploying-an-aws-vsocket-site-manually"
updated: 2026-07-15T10:54:23Z
published: 2026-07-15T10:54:23Z
canonical: "knowledge.catonetworks.com/deploying-an-aws-vsocket-site-manually"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying an AWS vSocket Site Manually

## Overview of AWS vSockets

You can connect your AWS VPC to Cato using an IPsec tunnel or a virtual Socket (vSocket). This article describes how to deploy a vSocket on an EC2 instance.

The vSocket provides these advantages:

- Bandwidth management control and QoS
- Maximizes connectivity to PoPs in the Cato Cloud
- Support for high availability configurations

For more information about vSocket and IPsec sites, see [Selecting the Connection Type for a Site](/v1/docs/selecting-the-connection-type-for-a-site).

This article assumes that you already have a VPC in your AWS environment.

> [!NOTE]
> Note:
> 
> Due to regulations in China, to deploy an AWS vSocket site in China please contact your Cato representative or Cato [Support](https://catonetworks.zendesk.com/agent/home/tickets).

### Prerequisites

- You must have admin permissions to the AWS dashboard and the Cato Management Application. In addition, you must have the following permissions in AWS:
  - AWS Marketplace
  - Key pair creation
- Make sure the environment meets the requirements listed in [Cato Socket Connection Prerequisites](/v1/docs/cato-socket-connection-prerequisites-and-known-limitations).

### AWS Limitations

AWS doesn't support these networking features:

- VLAN ranges
- DHCP ranges

## High Level Overview of Creating the AWS vSocket

1. In the Cato Management Application, create a new site for the AWS vSocket.
2. Create the AWS virtual resources
3. In the AWS Marketplace, subscribe to the Cato Networks AMI offering to connect the virtual resources to your EC2 instance
4. Launch the vSocket instance
5. Verify that the vSocket is connected to your account.

## Creating the vSocket Site in the Cato Management Application

Create the AWS vSocket site in the Cato Management Application, and the serial number for the vSocket is generated. This serial number is used when you launch the EC2 instance.

The Local IP for the vSocket must be the same as the IP address for the LAN interface on the EC2 instance. The first three IP addresses of the subnet are reserved by the VPC.

After you create the site, the Cato Management Application automatically generates a unique serial number for the new vSocket. You need to enter this serial number when you launch the EC2 instance).

### Creating an AWS Site

**To create the site for the AWS vSocket:**

1. In the Cato Management Application, from the navigation menu select **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![awsSocketsite.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247781858333.png)
3. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Select **vSocket AWS** for the **Connection Type**.
  4. Configure the **Configure the Country, State, and Time Zone to set the time frame for the Maintenance Window. Country**, and **State**.
4. Configure the **WAN Interface Settings**, including the **Downstream** and **Upstream** bandwidth according to your ISP bandwidth.
5. Configure the LAN Interface Settings, including the **Native Range** for the AWS site. This setting must be the same as the LAN subnet IP range in AWS (see below [Creating the MGMT, WAN, and LAN Subnets](/v1/docs/deploying-an-aws-vsocket-site-manually#creating-the-mgmt-wan-and-lan-subnets)).
6. Click **Apply**. The site is added to the **Sites** list.

#### Copying the vSocket Serial Number

The Cato Management Application automatically generates a unique serial number for the new vSocket. You need to enter this serial number (S/N) when you configure the AMI (see below [Configuring the Cato AMI](/v1/docs/deploying-an-aws-vsocket-site-manually#configuring-the-cato-ami)).

**To copy the serial number:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Copy the **S/N** for the vSocket.

You need to enter this serial number when you launch the vSocket instance.

## Creating the AWS Virtual Resources

Once you create the vSocket, you can create the AWS virtual resources and connect them to your EC2 instance using the AMI template in the AWS Marketplace.

### Creating the AWS Virtual Resources Manually

Create these virtual resources for the vSocket instance:

> [!NOTE]
> Note:
> 
> If these resources already exist, you can proceed to [associating the resources with the EC2 instance](/v1/docs/deploying-an-aws-vsocket-site-manually#configuring-the-ec2-instance-for-the-vsocket), below.

- Internet gateway
- Three subnets - WAN, LAN, and MGMT
- Security group(s) to manage inbound and outbound communication
- Three interfaces (ENIs) - WAN, LAN, and MGMT
- Two route tables - Internet and LAN
- Two Elastic IPs (for WAN and MGMT interfaces)

#### Defining the Internet Gateway for the VPC

Use the AWS Virtual Private Cloud (VPC) dashboard to create a new Internet gateway and attach it to your VPC.

![01_VPC_Dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247774459165.png)

**To create the new Internet gateway and attach it to the VPC:**

1. From the VPC dashboard, in the navigation menu select **Virtual Private Cloud > Internet Gateways**.
2. Click **Create internet gateway**.
3. In **Name tag**, enter the name for the Internet gateway.
4. Click **Create internet gateway**. The VPC dashboard shows the details for the Internet gateway.

![01a_Attach_IGW.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247774534301.png)
5. From the **Actions** drop-down menu, select **Attach to VPC**.
6. In the **Attach to VPC** window, in the **Available VPCs** section, select the VPC.
7. Click **Attach internet gateway**. The Internet gateway is attached to your VPC.

#### Creating the MGMT, WAN, and LAN Subnets

Create these subnets in the AWS and then they are automatically attached to the VPC:

- MGMT subnet
- WAN subnet
- LAN subnet - this is the same as the Native Range for the site.

Make sure that all the subnets are in the same AWS Availability Zone.

![02_CreateSubnet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247790974109.png)

**To create the subnet for the AWS vSocket:**

1. From the VPC dashboard, in the navigation menu select **Virtual Private Cloud > Subnets**.
2. Click **Create subnet**.
3. From the **Create subnet** window, in the **VPC** section, select the **VPC ID**.
4. Configure the settings for the subnet:
  1. Enter the **Subnet name**.
  2. Select the **Availability Zone** for the subnet.
  3. Enter the **IPv4 CIDR block** for the subnet. For the LAN subnet - this is the same value as the Native Range for the site.
5. To add additional subnets, click **Add new subnet** and repeat the previous step 4.
6. Click **Create subnet**. AWS creates the subnets and attaches them to the VPC.

#### Configuring the Security Groups

Configure the security group rules for the WAN and MGMT traffic with **Outbound rules** that allow all outbound traffic, so the traffic can reach the Cato Cloud.

#### Creating the WAN and LAN Interfaces

Create the WAN and LAN interfaces for the vSocket for the EC2 instance. Use the EC2 dashboard to create the interfaces.

Set the **Custom** IP address for the LAN interface to the same IP address as the Local IP for the Native Range. Don't use the first 3 IP addresses as they are reserved by AWS.

You need to disable AWS source/destination checking on the LAN interface to allow the EC2 instance to perform traffic forwarding.

> [!NOTE]
> Note:
> 
> To ensure proper vSocket behavior, define custom DHCP options with a [trusted server](/v1/docs/using-trusted-dns-servers) as the primary DNS server

![04_LAN_NIC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247820261789.png)

**To create the network interface (ENI):**

1. From the EC2 dashboard, in the navigation menu select **Network & Security > Network Interfaces**.
2. Click **Create network interface**.
3. In the **Create network interface** window, select the LAN **Subnet**.
4. In **Private IPv4 address**, click **Custom** and enter the Local IP for the Native Range.
5. In **Security groups**, select the appropriate security group for the interface.
6. Click **Create network interface**. AWS creates the interface.
7. Repeat the previous steps for the WAN interface.
8. For the LAN interface, disable AWS source/destination tracking:
  1. In the **Network Interfaces** window, right-click the LAN interface and select **Change source/dest. check**.

![05_LAN_INT_source-dest.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247820365597.png)
  2. In the **Change source/destination check** window, clear **Enable**.
  3. Click **Save**.

#### Creating the Route Tables

Create new or use existing VPC route tables for the vSocket traffic:

- Private route table for the LAN subnets
  - Attach the LAN subnet
  - Define the Socket LAN ENI as the target (next hop) for the default route
- A single Internet route table for the MGMT and WAN subnets. This route table is used to provide connectivity between the vSocket and the Cato Cloud resources.
  - Attach the WAN and MGMT subnets
  - Define the Internet Gateway as the target (next hop) for the default route

**To create the Internet and LAN route tables:**

1. From the VPC dashboard, in the navigation menu select **Virtual Private Cloud > Route Tables**.
2. Click **Create route table**.
3. In **Name tag**, enter the name for the Internet or LAN route table.
4. Select the **VPC** for the vSocket.
5. Click **Create**. The route table is added to the VPC.
6. Associate the WAN and MGMT subnets to the Internet route table, or the LAN subnet to the LAN route table.
  1. Right-click the route table and select **Edit subnet associations**. This is an example of the Internet route table.

![06_Internet_route_table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247791247517.png)
  2. In the **Edit subnet associations** window:
    - For the Internet route table, select the MGMT and WAN subnets
    - For the LAN route table, select the LAN subnet
  3. Click **Save**. The subnets are associated with the route table.
7. Add the default route to each route table (first configure the Internet route table and then the LAN).
  1. Right-click the route table, and select **Edit routes**. The following screenshot shows the Internet route table:

![06_InternetGW_route.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247835928093.png)
  2. Click **Add route**.
  3. Set the **Destination** for the new route to 0.0.0.0/0.
  4. In **Target**, select the next hop for the Internet or LAN route table:

![LAN_RouteTable.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247835995421.png)
    - For the Internet route table, select **Internet Gateway** and choose the Internet gateway for the VPC
    - For the LAN route table, select **Network Interface** and choose the LAN ENI. The following screenshot shows the LAN route table:
  5. Click **Save changes**.
  6. The window shows that the route was successfully created, click **Close**.
8. Repeat the previous steps for the LAN route table.

#### Associating Elastic IP Addresses with an Interface

Create and associate Elastic IP addresses with the WAN and MGMT interfaces. You can use a public IP address that is allocated from Amazon's pool of IPv4 addresses.

> [!NOTE]
> Note:
> 
> The elastic IP for the MGMT interface should be associated with the MGMT interface automatically created by the Cato AMI during the instance creation, and not one created manually.

**To allocate an Elastic IP address:**

1. From the EC2 dashboard, in the navigation menu select **Network & Security > Elastic IPs**.
2. Click **Allocate Elastic IP address**.
3. For the **Public IPv4 address pool**, select **Amazon's pool of IPv4 addresses**.
4. Click **Allocate**. The Elastic IP is allocated.
5. Select the Elastic IP, and select **Actions > Associate Elastic IP address**.

![07_associate_Elastic.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247802274845.png)
6. In the **Associate Elastic IP address** window, in **Resource type**, select **Network interface**.
7. In **Network interface**, select the WAN interface.
8. Click **Associate**. The Elastic IP is associated with the interface.
9. Repeat the previous steps for the MGMT interface.

### Configuring the EC2 Instance for the vSocket

After you create all the virtual resources for the vSocket, connect these resources to your EC2 instance using the Cato Networks AMI available in the AWS Marketplace.

#### EC2 Supported Instances

The following EC2 instance types are certified for vSockets:

- t3.large
- t3.xlarge
- c3.xlarge
- c4.xlarge
- c5.xlarge
- c5d.xlarge
- c5n.xlarge (Suggested for higher performance sites with bandwidth above 2Gbps)
- d2.xlarge
- The following instance types are supported from Socket version 26.0.23517:
  - c7i.xlarge
  - c7i.2xlarge
  - c7i.4xlarge
  - c7i.8xlarge

See [this article](https://aws.amazon.com/ec2/instance-types/) to review the specifications for the instance types to help you choose a type that matches the site requirements.

> [!NOTE]
> Note:
> 
> If the c3.xlarge or c4.xlarge instances are not available in your region, contact AWS customer support.

#### Configuring the Cato AMI

After preparing the environment, you can now configure the Cato Networks AMI.

**Configure the AMI:**

1. From the AWS Marketplace, search for Cato Networks Virtual Socket.
2. Click **Continue to Subscribe**.
3. Click **Continue to Configuration**.

![Cato_AMI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247820800797.png)
  - Under **Fulfillment option**, select **Amazon Machine Image**.
  - Under **Region**, make sure to select the region in which your vSocket is located.
4. Click **Continue to Launch**.
5. In the **Launch this Software** page:
  1. Under **Choose Action**, select **Launch through EC2**.
  2. Under **EC2 Instance Type**, select the EC2 instance.
  3. Under **VPC Settings**, select the VPC to which you are connecting.
  4. Under **Subnet Settings**, select the MGMT network.
  5. Under **Security Group Settings**, select the Security Group that you created for this instance.
  6. Expand **Advanced network configuration** and under **Network Interface** select the MGMT interface that you created.

**Note:** If you don't select an existing interface, a new interface is created.

![AWS_vSocket_Cato_AMI_advanced_network_config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247820868637.png)
  7. Under **Key Pair Settings**, select the key pair that you created.
  8. In the **Advanced details section**, under **User data - optional**, enter the serial number you copied from the vSocket site you created in the Cato Management Application.
6. Click **Launch**.

#### Attaching the Interfaces to the vSocket Instance

After the vSocket instance launches, the MGMT interface is attached to it. Stop the instance and then attach the remaining WAN and LAN interfaces to the instance.

> [!NOTE]
> Note:
> 
> Make sure that the EC2 instance is stopped and that first you attach the WAN interface, and then the LAN interface.

**To attach the interfaces to the vSocket instance:**

1. From the EC2 dashboard, in the navigation menu select **Instances > Instances**.
2. Right-click the vSocket instance and select **Stop instance**.
3. In the confirmation window, click **Stop**. Refresh the window and confirm that the **Instance state** is **Stopped**.
4. In the navigation menu select **Network & Security > Network Interfaces**.
5. Attach the WAN interfaces to the instance:
  1. Right-click the WAN interface, and select **Attach interface**.
  2. In the **Attach network interface** window, in **Instance** select the vSocket instance.
  3. Click **Attach**.
  4. Repeat the previous three steps for the LAN interface.

## Completing the vSocket Installation

After you attach the interfaces to the vSocket, start the instance and confirm that it connects to the Cato Cloud. After the vSocket connects to the Cato Cloud, it automatically updates to the newest Socket version.

**To complete the vSocket installation:**

1. From the EC2 dashboard, in the navigation menu, select **Instances > Instances**.
2. Right-click the vSocket instance and select **Start instance**. If the instance is already running, then restart it.
3. In the Cato Management Application, select **My Network > Topology**.
4. Confirm that the AWS site is connected to the Cato Cloud.

### (Optional) Connecting to the Socket WebUI

We don't recommend connecting to the AWS vSocket WebUI using an Elastic IP address. If you need to log in to the Socket WebUI, use these settings:

- Use the MGMT Elastic IP address as the public IP address for the vSocket
  - Create a Security Rule to allow inbound traffic from a single IP address (the Elastic IP address)
- Username is **admin**
- The default password is the **Instance ID** for the vSocket EC2 instance

## (Optional) Routing Traffic to the EC2 Instances

If your application EC2 instances are associated to a non-Native Range subnet (a subnet which is not the vSocket LAN interface subnet), in the Cato Management Application add a routed range in the **Networks** section for the site.

**To route traffic to the EC2 instance:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Networks**.
3. In the **LAN** section, click **New**. The **New IP range** panel opens.
4. Enter the **Name** for the IP range.
5. Set the **Type** of range to **Routed**.
6. Enter the **Subnet** IP Range.
7. Set the **Gateway** IP to the VPC router, which is the first host IP address of the Native Range subnet.
8. **(Optional)** Configure the **Static NAT** for the range.
9. Click **Apply**. The range is added to the **Networks** screen.

![awsiprange.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247782836893.png)

The screenshot above shows these sample settings for the Routed range:

- Native Range - 10.0.2.0/24
- Routed range - 10.0.26.0/24
- Gateway IP - 10.0.2.1

## (Optional) Configure IMDSv2 for EC2 Instances

IMDS (Instance Metadata Service) provides secure access to retrieve an instance's metadata. Cato uses this service to get the following information:

- Serial number in user data
- Instance ID
- HA-related information
- Key and hostname settings for modifying the routing table

Starting with Socket v20 build 18221, Cato is adding support for IMDSv2.

**To configure your instance to use IMDSv2:**

1. In AWS, select the instance you want to configure.
2. Select **Actions > Instance settings**.
3. In the **Modify instance metadata options** section, under **IMDSv2** select **Required**.
4. Click **Save**.

This change does not cause any downtime. However, if you have an HA deployment, you must configure both the primary and secondary instances to use the same IMDS version.
