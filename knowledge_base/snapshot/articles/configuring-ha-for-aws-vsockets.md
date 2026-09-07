---
title: "Configuring HA for AWS vSockets"
slug: "configuring-ha-for-aws-vsockets"
updated: 2026-08-18T15:10:05Z
published: 2026-08-18T15:10:05Z
canonical: "knowledge.catonetworks.com/configuring-ha-for-aws-vsockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring HA for AWS vSockets

This article explains how to configure a site in the Amazon Web Services (AWS) cloud with two vSockets to provide high availability (HA).

## Overview of High Availability vSocket in AWS

To provide redundancy for vSockets within an AWS site, deploy two vSockets in a single VPC, and set them to work in a high availability (HA) configuration. The vSockets operate in active/passive mode and the LAN links are used to send keep-alive messages between the vSockets.

You can deploy the vSockets within a single Availability Zone (AZ) or in different AZs within the same VPC. Make sure that you associate both LAN subnets to the same route table.

The high availability solution requires that both vSockets have IAM permissions to use API calls to modify the route tables.

For more about installing a vSocket in AWS, see [Deploying a vSocket Site from the AWS Marketplace](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace). The vSocket image is publicly available in the AWS Marketplace.

### Prerequisites for AWS High Availability

- High availability in AWS is supported for vSockets that are using Socket version 9.1 or higher.
- All of the AWS virtual resources must belong to the same account.​
- The AWS vSockets must have access to a public DNS server, make sure that the VPC isn't configured to only use a private DNS server.
  - The DNS server must be able to resolve internal AWS domains.
- Each EC2 instance for a vSocket must have:
  - IAM permissions that allow the vSocket to modify the route table
  - Separate subnets for each LAN interface
  - Active MGMT interface that makes the API calls to change the routing table during failover
- AWS security rules must allow traffic on UDP port 20480 in both directions between the LAN interfaces for the vSockets.

> [!NOTE]
> Notes:
> 
> - Alt. WAN links are not supported for AWS HA deployments. You must remove any existing Alt. WAN links before you implement the HA solution.
> - BGP isn't supported for AWS vSocket HA (only supported for single AWS vSockets).
> - If you downgrade a vSocket to a version earlier than version 9.1, HA is disabled for the site. The secondary vSocket is removed from the site.
> 
> We recommend that you remove the HA settings from the site before you downgrade a vSocket to an unsupported earlier version.

### AWS vSocket Failover Workflow

This is the failover workflow when the primary active vSocket fails over to the secondary standby one in an AWS site.

1. The primary (active) vSocket goes down, and the HA link state for the LAN ENIs is changed to **down**.
2. The secondary (standby) vSocket sends an announcement that it is the new active (master) vSocket.
3. The secondary vSocket issues an API call to the AWS API gateway to modify the LAN route table and assign the secondary vSocket LAN ENI as the next hop for the 0.0.0.0/0 route.

**Note:** The MGMT interface must be enabled and active to make the API calls to change the routing table during failover.
4. The Gateway IP (next hop) for the Routed ranges (**Sites > Networks**) is automatically updated to the Gateway IP address for the Secondary Socket Native Range.
5. The secondary vSocket is now the active vSocket and passes traffic for the site.
6. When the primary vSocket recovers, it resumes the active role, and the secondary vSocket returns to standby status.

For more about HA and failover behavior, see [What is Socket High Availability (HA)](/v1/docs/what-is-socket-ha).

## Preparing the AWS Environment for High Availability

This section describes the steps that you need to complete to prepare the AWS environment for vSocket HA.

> [!NOTE]
> Note:
> 
> The screenshots and examples in this article are based on the new AWS **EC2 Experience** for EC2 instances.

### Creating a Subnet for the Secondary vSocket LAN Interfaces

The secondary vSocket requires a separate subnet for its LAN interface (ENI) to send the keep-alive packets to the primary vSocket. This requirement is the same for single AZ and dual AZ HA deployments.

In the AWS VPC, create a subnet for the secondary vSocket LAN interface, and associate it to the VPC private route table. Make sure that the new subnet is associated with the same route table as the subnet for the Primary vSocket LAN interface.

> [!NOTE]
> Notes:
> 
> - You must associate all the LAN subnets to the same private route table.
> - If you create the LAN subnet for the secondary vSocket in a different Availability Zone, you must also create separate WAN and MGMT subnets in that Availability Zone.

### Creating the IAM Role for the vSocket

The Identity and Access Management (IAM) role lets the vSocket make AWS API calls to change entries in the route table. Create an IAM role that gives the instance the correct permissions. Later you will attach this role to each vSocket.

#### Creating the Policy for the IAM Role

Use a JSON file to create a new policy for the IAM role that includes AWS read-write permissions for these actions:

- "ec2:CreateRoute"
- "ec2:DescribeRouteTables"
- "ec2:ReplaceRoute"

**JSON File for the vSocket HA Policy**

This is the JSON file for the IAM policy that assigns the necessary permissions for the vSockets to operate in an HA configuration. You can copy and paste the file in the **Create policy** window.

```plaintext
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
                "ec2:CreateRoute",
                "ec2:DescribeRouteTables",
                "ec2:ReplaceRoute"
                ],
            "Resource": "*"
        }
}
```

**To create the IAM policy:**

1. From the AWS Management Console, in **Find Services** search for **IAM**.

![AWS_SearchIAM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247825424157.png)

The **Identity and Access Management (IAM)** dashboard opens.
2. From the navigation menu, select **Access management > Policies**.
3. Click **Create policy**.
4. In the **Create policy** window, click the **JSON** tab.
5. Paste the contents of the JSON file to configure the permissions for the IAM role.

![JSON_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247802806813.png)
6. Click **Review policy**.
7. Enter the **Name** for the policy.
8. Click **Create policy**. The policy is created and added to the IAM policies.

#### Creating a New IAM Role

Create an IAM role that you attach to the EC2 instances for the vSocket HA.

**To create a new IAM role:**

1. From the navigation menu, select **Access management > Roles**.
2. Click **Create role**.
3. In the **Create role > Select type of trusted entity** window, select **AWS service** and click **EC2**.

![IAM_Role_resize.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247836663069.png)
4. Click **Next: Permissions**. The **Attach permissions policies** window opens.
5. In the Search bar, enter the name of the IAM policy you created in the previous section.

![attach_permissions_720x341.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247836741661.png)
6. Click **Next: Tags**. The **Add tags** window opens.
7. **(Optional)** Add tags to the IAM role. Click **Next: Review**. The **Review** window opens.
8. Enter the **Role name** for the IAM vSocket HA role.
9. Click **Create role**. The IAM vSocket HA role is created.

### Locating the Route Table ID

Locate and copy the private Route table ID for the VPC. You need this ID when you add the secondary vSocket to the AWS HA site in the Cato Management Application. The vSockets issue API calls to modify this route table as part of the failover process.

To locate the Route table ID:

1. From the **Virtual Private Cloud** navigation menu, select **Route Tables**.

![RouteTableID.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247836797853.png)
2. Select the route table used for the LAN segment, and copy the **Route Table ID**.

## Deploying vSocket High Availability in AWS

Deploy the vSockets on the EC2 instances as the primary and secondary vSockets for the site.

1. For new sites, create a new site in the Cato Management Application and deploy the primary vSocket. (For existing sites, skip this step.)
2. Attach the IAM role to the EC2 instance for the primary vSocket.
3. Add the secondary vSocket to the site in the Cato Management Application.
4. Deploy the secondary vSocket to the AWS VPC.
5. Attach the IAM role to the EC2 instance for the secondary vSocket.

> [!NOTE]
> Note:
> 
> When you configure the IP settings for the site, make sure that you don't use IP addresses that are reserved by AWS. You can't use the first four IP addresses and the last IP address in a subnet CIDR block.

For more about AWS reserved IP addresses, see [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html).

### Deploying the Primary vSocket in the AWS VPC

Complete these steps to deploy the primary vSocket on the EC2 instance. For a new AWS site, deploy the primary vSocket and attach the IAM role to the instance.

For existing AWS sites, upgrade the primary vSocket to version 9.1 or higher. Then attach the IAM role to the EC2 instance (the primary vSocket) and continue below with [Attaching the IAM Role to a vSocket](/v1/docs/configuring-ha-for-aws-vsockets#attaching-the-iam-role-to-a-vsocket).

To deploy the primary vSocket for a new site:

1. Add a new AWS site to the Cato Management Application.
2. Install the primary vSocket on the EC2 instance.

For more about installing a vSocket in AWS, see [Deploying a vSocket Site from the AWS Marketplace](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace).
3. Attach the IAM role that you created above to the vSocket.

The screenshot above shows the AWS site after the primary vSocket is installed and upgraded to version 9.1 or higher.

> [!NOTE]
> Note:
> 
> For existing AWS sites, the **Add Secondary Socket** button is only shown after you upgrade the vSocket to version 9.1 or higher.

### Attaching the IAM Role to a vSocket

Attach the IAM role that you created above to the vSocket EC2 instance. The IAM role gives permissions to the vSocket to make API calls to modify the routing table for HA functionality.

**To attach the IAM role to the instance:**

1. In AWS, in the **Instances** window, select the vSocket instance.
2. From the **Actions** drop-down menu, select **Security > Modify IAM role**.
3. In the **Modify IAM role** window, select the IAM role.

![Modify_IAM_role.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247825952029.png)
4. Click **Save**. The IAM role is attached to the vSocket instance.

### Adding the Secondary vSocket to an AWS Site

After the Cato Management Application detects that the primary vSocket is connected to the Cato Cloud, the **Add Secondary Socket** option is shown in the **Network > Sites > Site Configuration > Socket** page.

When you add the secondary vSocket to the site, a pop-up window opens where you enter the following settings of the secondary vSocket:

- LAN ENI IP Address
- LAN ENI Subnet
- Route-Table ID

The Cato Management Application uses the LAN ENI IP Address as the management IP address for the secondary vSocket. This LAN ENI is also used to send HA keep-alive packets to the primary vSocket LAN interface.

The secondary vSocket settings in the Cato Management Application must be the same settings used in AWS.

After you add the secondary vSocket to the site, the Cato Management Application does the following:

- Generates the vSocket serial number for the new vSocket (this serial number is used when you install the vSocket on the EC2 instance)
- Enables the **High Availability Configurations** section for that site
- Modifies the **Site Configuration > Networks** page with the new Native Ranges:
  - The LAN ENI IP address is shown as the Local IP of the network range
  - The LAN ENI subnet is shown as the subnet of the network range

For more about network segments in the HA site, see below [Overview of AWS High Availability Network Segments in the Cato Management Application](/v1/docs/configuring-ha-for-aws-vsockets#overview-of-aws-high-availability-network-segments-in-the-cato-management-application).

![AWS_HA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247826029981.png)

**To configure an AWS site for high availability:**

1. From the navigation menu, click **Network > Sites**, and select the AWS site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click **Add Secondary Socket**. The **Add Secondary vSocket (High Availability)** window opens.
4. Configure the settings exactly as the LAN subnet for the Secondary vSocket EC2 instance:
  1. Enter the **LAN Interface IP**. This value is used as the Local IP.
  2. Enter the **LAN ENI Subnet** with the CIDR. This value is used as the Secondary Socket Native Range.
  3. Enter the **Route-Table ID** of the private route table used for LAN ranges.
5. Click **OK**. The settings for the primary and secondary vSockets are configured and copied to the **Site Configuration > Socket** and **Socket Configuration** section.
6. Copy and save the vSocket serial number for the vSocket configuration script:
  1. From the **Sites** list, select the new vSocket site.
  2. From the navigation menu, click **Site Configuration > Socket**. Copy the serial number (S/N) and save it.

Use this serial number when you install the secondary vSocket on the EC2 instance.

#### Changes to the Socket Configuration Window

After you add the secondary vSocket to the site, the **Destination** for the LAN1 link is automatically set to **LAN & HA**.

### Deploying the Secondary vSocket in the AWS VPC

Create and deploy the secondary vSocket in the AWS VPC with the IAM role that you created earlier.

- Create the network interfaces
- Attach the IAM role that you created above to the secondary vSocket (see above [Attaching the IAM Role to a vSocket](/docs/configuring-ha-for-aws-vsockets#UUID-12280c2f-3853-bcd4-6dac-ae3a5e62eaaa_N1637059553385))
- Enter the serial number of the secondary vSocket site that was generated in the Cato Management Application
- Configure the EC2 instance for the vSocket

#### Creating the MGMT, WAN, and LAN Interfaces

Create the MGMT, WAN, and LAN interfaces for the vSocket for the EC2 instance. Use the EC2 dashboard to create the interfaces.

Set the **Custom** IP address for the LAN interface to the same IP address as the **LAN Interface IP** entered in CMA.

You need to disable AWS source/destination checking on the LAN interface to allow the EC2 instance to perform traffic forwarding.

> [!NOTE]
> Note:
> 
> To ensure proper vSocket behavior, define custom DHCP options with a [trusted server](/v1/docs/using-trusted-dns-servers) as the primary DNS server

![04_LAN_NIC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247850650397.png)

**To create the network interface (ENI):**

1. From the EC2 dashboard, in the navigation menu select **Network & Security > Network Interfaces**.
2. Click **Create network interface**.
3. In the **Create network interface** window, select the LAN **Subnet**.
4. **(Optional for the MGMT/WAN interfaces)** In **Private IPv4 address**, click **Custom** and enter the **LAN Interface IP** entered in CMA.
5. In **Security groups**, select the appropriate security group for the interface.
6. Click **Create network interface**. AWS creates the interface.
7. Repeat the previous steps for the **MGMT** and **WAN** interfaces.
8. For the **LAN** interface, disable AWS source/destination tracking:
  1. In the **Network Interfaces** window, right-click the LAN interface and select **Change source/dest. check**.

![05_LAN_INT_source-dest.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247821714973.png)
  2. In the **Change source/destination check** window, uncheck **Enable**.
  3. Click **Save**.

#### Associating Elastic IP Addresses with MGMT and WAN Interfaces

Create and associate Elastic IP addresses with the WAN and MGMT interfaces of the Secondary vSocket. You can use a public IP address that is allocated from Amazon's pool of IPv4 addresses.

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

#### Configuring the EC2 Instance for the vSocket

After you create all the virtual resources for the vSocket, connect these resources to your EC2 instance using the Cato Networks AMI available in the AWS Marketplace.

#### EC2 Supported Instance Types

The following EC2 instance types are certified for vSockets:

- c5.xlarge
- d2.xlarge
- c3.xlarge
- t3.large
- t3.xlarge
- c4.xlarge
- c5d.xlarge
- c5n.xlarge (Suggested for higher performance sites with bandwidth above 2Gbps)

#### Configuring the Cato AMI

After preparing the environment, you can now configure the Cato Networks AMI.

**Configure the AMI:**

1. From the AWS Marketplace, search for Cato Networks Virtual Socket.
2. Click **Continue to Subscribe**.
3. Click **Continue to Configuration**.

![Cato_AMI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247821784861.png)
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

![AWS_vSocket_Cato_AMI_advanced_network_config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247821872157.png)
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

### Confirming the High Availability Status for the AWS Site

This section describes how to test and confirm that the vSockets are configured correctly for HA functionality.

#### Showing the High Availability Status in the Cato Management Application

The **High Availability** section in the Cato Management Application for the site shows the HA status for the vSockets. After you deploy the secondary vSocket, it automatically connects to the site.

For more information, see below [Showing the High Availability Information and Status](/v1/docs/configuring-ha-for-aws-vsockets#showing-the-high-availability-information-and-status).

**To confirm the high availability status for the site:**

1. From the navigation menu, click **Network > Sites**, and select the AWS site.
2. From the navigation menu, click **Site Monitoring > Network Analytics**
3. In **High Availability Status**, verify that the status is **Ready**, and the **Master** is the **Primary** vSocket.

#### Testing High Availability from the Socket WebUI

You can use the Network Tools in the Socket WebUI to test HA functionality for the vSockets. The vSocket performs an API call to the AWS API gateway to verify the HA configuration for these settings:

- IAM permissions for the vSocket are configured correctly
- Route table ID is configured correctly

To complete the test, make sure that the vSocket can resolve the AWS RestAPI domain for the relevant region. For more information, see [AWS documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html).

If the test isn't successful, we recommend that you compare the settings for the route table ID in AWS and in the Cato Management Application.

**To test the HA API calls for an AWS vSocket:**

1. From the navigation menu, select **Site Configuration > Socket**.
2. From the **Actions** drop-down menu for the Primary vSocket, select **Socket WebUI**.

The Socket WebUI opens in a new tab.
3. Click the **Tools** tab.
4. In the Network Tools section, click the **API Test Tool** tab.
5. Click **Run Test**. The window shows if the HA API test succeeds or fails.
6. Repeat steps 2-5 for the Secondary vSocket.

For more about using the Socket WebUI, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

## Working with Network Segments for AWS High Availability Sites

This section explains how to use the **Networks** section to manage network segments for the AWS HA site.

### Overview of AWS High Availability Network Segments in the Cato Management Application

When you add the secondary vSocket to the Cato Management Application, the network segments in the **Networks** section are automatically updated to the following settings:

- Primary Socket Native Range:
  - The Native Range for the primary vSocket is converted to the Primary Socket Native Range
  - The **Local IP** of the Native Range represents the LAN interface IP address for the vSocket. This IP address is also used as the management IP address of the vSocket.
  - The **Gateway** IP address is automatically set as the first IP address of the subnet, which points to the AWS VPC router (based on the AWS reserved IPs)
- Secondary Socket Native Range - These settings are based on the LAN ENI values that you entered when you added the secondary vSocket:
  - The Native Range for the secondary vSocket is the **LAN ENI IP Subnet**
  - The **Local IP** of the secondary Native Range is the **LAN ENI IP Address**. This IP address is also used as the management IP address of the vSocket.
  - The **Gateway** IP address is automatically set as the first IP address of the subnet, which points to the AWS VPC router (based on the AWS reserved IPs)

> [!NOTE]
> Notes:
> 
> - Because the Gateway IP address is automatically calculated for a range, you can't change it.
> - If you need to change the Local IP address of the range, you must change the management IP address of the vSocket (see below, [Changing the Local IP Address](/v1/docs/configuring-ha-for-aws-vsockets#changing-the-local-ip-address)).

### Adding Routed Ranges (Static Routes)

You can add Routed ranges to the AWS HA site. When you add a Routed range, the Gateway for the range is automatically selected based on the active vSocket. The Gateway IP of the active vSocket Native Range is automatically used as the **Gateway** for the Routed range.

For example, when the secondary vSocket is active, then the Gateway IP address for the Secondary Socket Native Range is used for all the Routed ranges in the site. In the example below, the Gateway IP of 10.0.17.1 will be used as the Gateway (next hop) for the 10.0.25.0/24 Routed range.

When the primary vSocket becomes active again, the Gateway IP for the Routed range automatically switches to 10.0.3.1.

![AWS_routed_range.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247850993309.png)

**To add a Routed range to an AWS HA site:**

1. From the navigation menu, click **Network > Sites**, and select the AWS site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. Expand the LAN interface.
4. From the LAN interface, click **New** to add a new network segment for the IP range.

The **New Interface IP Range** panel opens.
5. Enter the **Name** for the IP range.
6. From **Type**, select **Routed**.
7. Enter the **IP Range** for the segment.
8. Click **Apply**.

### Changing the Local IP Address

In vSocket HA configuration, the Local IP address of the Native Range is the same as the vSocket management IP. This IP address is used for the HA keep-alive messages, and also for access to the Socket WebUI. To change the Local IP address of the Native Range, change the management IP address in the **High Availability** section for the relevant vSocket.

For example, to change the Local IP for the primary vSocket Native Range, change the management IP address of the primary vSocket in the **High Availability** section.

**To change the Local IP address:**

1. From the navigation menu, click **Network > Sites**, and select the AWS site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Expand the **High Availability Configurations** section.
4. Enter the new **Primary Management IP** or **Secondary Management IP**.
5. Click **Save**. The **Local IP** for the Primary or Secondary Native Range is updated with the new IP address.

### Changing the Native IP Range for a vSocket in a High Availability Configuration

If you need to change the Primary or Secondary Native IP Range, change the IP range in the **Networks** section, and then update the management IP address in the **High Availability** section.

**To change the IP range of a segment:**

1. From the navigation menu, click **Network > Sites**, and select the AWS site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. For the Primary or Secondary Native IP Range, configure the new IP range:
  1. In the **Type** column, click the network range.

The **Edit IP Range** panel opens.
  2. Configure the **Subnet** for the IP range.
  3. Click **Apply** and then click **Save**.
4. From the navigation menu, select **Site Configuration > Socket**.
5. Expand the **High Availability Configurations** section.
6. Enter the new **Management IP** address for the Primary or Secondary vSocket.

The management IP must be within the subnet you configured in step 2. You can't use an AWS reserved IP address for the management IP.
7. Click **Save**.

## Managing AWS High Availability

This section explains how to manage HA for the AWS site:

- Show the HA status for each vSocket
- Change the route table ID for the site
- Disable HA for the site and remove the secondary vSocket

### Showing the High Availability Information and Status

The **High Availability** section shows the HA status for the primary and secondary vSocket.

| Item | Description |
| --- | --- |
| High Availability Status | The HA status for the site (Ready or Not Ready), only shows ready when each status HA status indicator is OK |
| WAN Connectivity (status indicator) | The status **Ok** indicates that both vSockets have WAN connectivity to the Cato Cloud |
| Keepalive (status indicator) | The status **Ok** indicates that one vSocket is the master and one is the standby (If both vSockets are status master, then there is an HA split brain issue) |
| Socket Version (status indicator) | The status **Ok** indicates that both vSockets are running the same Socket version |
| Master | Shows if the Primary or Secondary vSocket is the active vSocket |
| Connection to Cato - Primary | The connection status for the primary vSocket |
| Connection to Cato - Secondary | The connection status for the secondary vSocket |

### Changing the Route Table ID

You can change the route table ID for the AWS HA site in the Cato Management Application, to match the setting in AWS.

**To change the route table ID for the site:**

1. From the navigation menu, click **Network > Sites**, and select the AWS site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Expand the **High Availability Configurations** section.
4. Enter the new **Route Table ID**.
5. Click **Save**.

### Disabling High Availability for the AWS Site

You can remove the secondary vSocket from an AWS site and disable HA for that site. After you remove the secondary vSocket from the Cato Management Application, the deployed vSocket can no longer connect to the Cato Cloud. The settings for the site are restored to the configuration for a single vSocket:

- The **High Availability** section is disabled and no longer appears in the page
- The layout for the **Networks** section changes to the configuration for a single vSocket
- For **Routed** ranged, the next hop is set to the first IP address of the Native Range

> [!NOTE]
> Note:
> 
> You can't undo the **Unassign Socket** action. The serial number for the secondary vSocket is no longer valid.

If you want to add the secondary vSocket again, you must install a new vSocket on the EC2 instance with the new serial number.

**To disable HA for the AWS site:**

1. From the navigation menu, click **Network > Sites**, and select the AWS site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. From the **Actions** menu of the **Secondary** vSocket, click **Unassign**.
4. In the Warning window, click **OK**. HA is disabled for the site, and the secondary vSocket is removed from it.

## Analyzing High Availability Events

The **Events** screen shows all the HA Connectivity events for your account.

You can learn more about using the Events screen [here](/v1/docs/analyzing-events-in-your-network). You can use the **SaaS Security API Data Protection** preset to filter the events.

### Explaining the High Availability Events Fields

The Events fields and events are the same for Socket HA and for vSocket HA. These are the HA events:

| Field | Description |
| --- | --- |
| Socket role | Shows if the event was generated by the primary or secondary vSocket |
| Event sub type - Socket Fail-Over | The failover process is initiated for the site |

For more about events that are generated as part of the failover process, see [Socket HA Failover Events](/v1/docs/what-is-socket-ha).
