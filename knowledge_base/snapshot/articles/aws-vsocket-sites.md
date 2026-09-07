---
title: "Deploying a vSocket Site from the AWS Marketplace"
slug: "deploying-a-vsocket-site-from-the-aws-marketplace"
updated: 2026-07-15T10:58:28Z
published: 2026-07-15T10:58:28Z
canonical: "knowledge.catonetworks.com/deploying-a-vsocket-site-from-the-aws-marketplace"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying a vSocket Site from the AWS Marketplace

## Overview of AWS vSockets

You can connect your AWS VPC to Cato using an IPsec tunnel or a virtual Socket (vSocket). This article describes how to deploy a vSocket on an EC2 instance.

The vSocket provides these advantages:

- Bandwidth management control and QoS
- Maximizes connectivity to PoPs in the Cato Cloud
- Support for high availability configurations

For more information about vSocket and IPsec sites, see [Selecting the Connection Type for a Site](/v1/docs/selecting-the-connection-type-for-a-site).

This article assumes that you already have a VPC in your AWS environment.

### Prerequisites

- You must have admin permissions to the AWS dashboard and the Cato Management Application. In addition, you must have the following permissions in AWS:
  - AWS Marketplace
  - Cloud Formation
  - IAM role creation
  - Key pair creation
- Make sure the environment meets the requirements listed in [Cato Socket Connection Prerequisites and Known Limitations](/v1/docs/cato-socket-connection-prerequisites-and-known-limitations).

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

### AWS Limitations

AWS doesn't support these networking features:

- VLAN ranges
- DHCP ranges

## High Level Overview of Creating the AWS vSocket

1. In the Cato Management Application, create a new site for the AWS vSocket
2. Deploy the Cato Networks AWS offering
3. Verify that the vSocket is connected to your account

## Creating the vSocket Site in the Cato Management Application

Create the AWS vSocket site in the Cato Management Application, and the serial number for the vSocket is generated. This serial number is used when you launch the EC2 instance.

The Local IP for the vSocket must be the same as the IP address for the LAN interface on the EC2 instance. The first three IP addresses of the subnet are reserved by the VPC.

After you create the site, the Cato Management Application automatically generates a unique serial number for the new vSocket. You need to enter this serial number when you deploy the EC2 instance (see below [Deploying the AWS vSocket](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace#deploying-the-aws-vsocket)).

### Creating a New AWS Site

**To create the site for the AWS vSocket:**

1. In the Cato Management Application, from the navigation menu select **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![awsSocketsite.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32000509163165.png)
3. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Under **Connection Type**, select **vSocket AWS** .
  4. Configure the **Country**, **State**, **City**, and **Time Zone** to set the time frame for the Maintenance Window.
4. Configure the **WAN Interface Settings**, including the **Downstream** and **Upstream** bandwidth according to your ISP bandwidth.
5. Configure the **LAN Interface Settings**, including the **Native Range** for the AWS site.

The Native Range must be the same as the LAN subnet IP range in the EC2 instance.
6. Click **Apply**. The site is added to the **Sites** list.

#### Copying the vSocket Serial Number

The Cato Management Application automatically generates a unique serial number for the new vSocket. You need to enter this serial number (S/N) is used during when you launch the EC2 instance.

**To copy the serial number:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Copy the **S/N** for the vSocket.

### Deploying the AWS vSocket

This procedure enables you to automatically deploy all aspects of the AWS environment using a predefined template. Before you begin, make you have:

- Necessary permissions to download and run the template from the AWS Marketplace
- Created a key pair for encrypted communication
- Copied the serial number from the vSocket you created in the Cato Management Application.

**To deploy AWS resources using the Cato offering:**

1. From the AWS Marketplace, under **Discover products**, search for **Cato Networks Virtual Socket** and click on the search result.
2. Click **View purchase options** and then **Subscribe**.
3. Click **Launch your software**.
4. Under **Setup> Service**, select **AWS CloudFormation**.
5. Under **Region**, make sure to select the region in which your vSocket is located.
6. After reviewing the configuration information, click **Launch with CloudFormation**.
7. In the **Create stack** page, click **Next** to use the template as is, or click **View in Infrastructure Composer** to make changes relevant to your environment.
8. In the **Specify stack details** page, enter a **Stack name** and the **Network Configuration** parameters for your virtual resources:
  - **NewVPC** - enter the network range of the VPC to which you are connecting. Make sure it does not conflict with your WAN.
  - **NewMGMTSubnet**, **NewWANSubnet**, and **NewLANSubnet** - enter the range, within the VPC, to use as the respective subnets.
9. Enter the Instance Configuration parameters for your virtual resources:
  - **NewMGMTENI** - An IP address within the MGMT subnet for the MGMT interface. The first three IP addresses of the subnet are reserved by the VPC.
  - **NewWANENI** - An IP address within the WAN subnet for the WAN interface. The first three IP addresses of the subnet are reserved by the VPC.
  - **NewLANENI** - An IP address within the LAN subnet for the LAN interface. The first three IP addresses of the subnet are reserved by the VPC.
  - **MyKeyPair** - Select the key pair that you created to encrypt this connection.
  - **SerialNumber** - The S/N you copied when creating the vSocket in the Cato Management Application.
  - **SecurityGroupIngress** - Enter the IP address or range that can initiate a connection to these virtual resources. We recommend limiting this to the smallest group possible to maintain good security posture.
  - **InstanceType** - Select the required instance type.
10. Click **Next**.
11. (Optional) If required, configure stack options.
12. Click **Next**.
13. On the **Review and create** page, review the settings and then click **Submit**.
14. Once the stack is built and the EC2 instance is running, reboot the VM to finalize the vSocket deployment.

> [!NOTE]
> Note:
> 
> Rebooting the VM is required for the vSocket to establish a connection to the Cato Cloud.

The new configuration is deployed and within several minutes, the vSocket should display a **Connected** status.

### (Optional) Connecting to the Socket WebUI

If you need to log in to the Socket WebUI, use these settings:

- Use the MGMT Elastic IP address as the public IP address for the vSocket
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

![awsiprange.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32000509192989.png)

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
