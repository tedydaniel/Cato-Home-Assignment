---
title: "Redundant VPN Connection to AWS Using BGP"
slug: "redundant-vpn-connection-to-aws-using-bgp"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/redundant-vpn-connection-to-aws-using-bgp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Redundant VPN Connection to AWS Using BGP

Following the original article on [connecting your AWS assets to Cato](/v1/docs/connect-your-aws-assets-to-cato-cloud-with-amazon-virtual-private-gateway), the article below elaborates on the extended BGP functionality. BGP functionality allows having a redundant VPN connection to AWS cloud in order to assure maximum redundancy.

## Configuring BGP with AWS

This procedures explains how to set up an IKEv1 or IKEv2 site that uses BGP to connect to AWS.

1. Ensure you have at least 2 Public IP addresses in the Cato Management Application (**Network > IP Allocation**):

![IP_Allocation.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248068112669.png)
2. In AWS, create a Virtual Private Gateway:

| ![360002046957-blobid0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248076168861.png) |
| --- |
3. Navigate to the **Your VPN Dashboard > Create VPC**. From here create your new VPC:

| ![360002150038-blobid1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248083474077.png) |
| --- |
4. Navigate to the **Customer Gateways**. Create a **2 Customer Gateways** using the new IP address allocated above (in the same AWS region):

a. **Name** - needs to recognizable to you.

b. **IP Address** - these are Public IP address that you have been allocated in the Cato Management Application.

c. **VPC** - for each customer Gateway you will need to ensure you select the same VPC.

| ![360002150078-blobid2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248110309277.png) |
| --- |
5. Navigate to '**Site-To-Site VPN Connections**' and **create 2 VPN Connections** (1 to each of the new Customer Gateways you have just created):

**a.Name Tag -** Descriptive Name

**b. Customer Gateway -** Here select one of the Customer Gateways you created

**c.Routing Option -** Select Dynamic (BGP)

**d.Tunnel Options -** You stipulate the Tunnel IP's if required but if left as default AWS will use 169.x.x.x range.

| ![360002047017-blobid3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248104204061.png) |
| --- |

**Note:** AWS uses the Tunnel IP to create the BGP peer with Cato over the IPsec tunnel.
6. Click on **Download Configuration** for each of the new VPN Connections you have just set up:

| ![360002151218-blobid0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248100633245.png) |
| --- |
7. Within this file get the following information to help set up the Cato Management Application:

**a**. Pre-Shared Key

**b.** BGP Configuration (Private IP Address and ASN)

| ![360002047057-mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248104402205.png) |
| --- |
8. In the Cato Management Application, navigate to the Site you want to set up IPsec/BGP.

**a.** The set up here is exactly the same as you would for a standard IPsec site except you need to add the private IP address's that you have in the AWS configuration you downloaded earlier.

Example of IKEv1 site:

| ![360002150318-blobid7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248104494749.png) |
| --- |

Example of IKEv2 site:

![AWS_IPsec_IKEv2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248084066333.png)

**b.** In the BGP section, enter the following:

**i.** ASN's

**ii.** Private IP's

**iii.** Routing Information

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25133913086109.png)

**Note:** The tunnel with the lower Metric will be the preferred route.
9. To check the status of the BGP connection select **Show BGP Status**.
10. To check in AWS, navigate to **Site-to-Site Connection > Select your VPC connection > Tunnel Details**. From here you can see if the VPN connection is and if BGP routes have been propagated to AWS.

![tunnel_details.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248111011101.png)
11. **Note:** If you want to see what routes have been publish to the AWS site go to **Route Table > Find Your Routing Table > Select Routes**.

| ![360002150458-blobid11.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248104903581.png) |
| --- |

## Testing BGP Failover

Although Amazon does not support failover test within [AWS platform](https://docs.aws.amazon.com/vpc/latest/adminguide/GenericConfig.html), BGP failover test can be done using the Cato Management Application:

1. From behind a Socket site or connecting with the Cato Client, ping a host within the AWS environment.
2. In the Cato Management Application, go to the IPsec site with BGP.
3. Change the IP address to create a failover:

Make sure that you save the original IP address, you need it after the test is completed.
  1. In the **BGP** section, for the primary connection, change the Cato or Neighbor's IP address:
  2. In the **IPsec** section, change the **Private IPs** for **Cato** or **Neighbor** to the same IP address in the previous step.
  3. Click **Save**.
4. The pings start to drop and then the connection fails over and you see that the BGP failover is working correctly.
5. To fail back to the primary link, change the BGP and IPsec IP address back to the original settings, After a few dropped pings the connection falls back to the primary connection.
