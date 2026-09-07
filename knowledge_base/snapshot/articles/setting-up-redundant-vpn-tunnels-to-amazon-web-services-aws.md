---
title: "Setting Up Redundant VPN Tunnels to Amazon Web Services (AWS)"
slug: "setting-up-redundant-vpn-tunnels-to-amazon-web-services-aws"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/setting-up-redundant-vpn-tunnels-to-amazon-web-services-aws"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Up Redundant VPN Tunnels to Amazon Web Services (AWS)

When setting up an AWS VPN connection, AWS provides two VPN tunnels per Customer Gateway. While this provides redundancy on the AWS side, it does not provide redundancy on the Cato side, since both tunnels must be connected to the same PoP.

In order to provide redundancy for both Cato and AWS, we recommend creating two Customer Gateways in AWS. Use one tunnel from one Customer Gateway for the primary tunnel and one tunnel from the other Customer Gateway for the secondary tunnel. This allows you to configure the primary and secondary tunnels on PoPs in different locations.

The steps below will show you how to configure this in both AWS and the Cato Management Application.

**Note:** this guide assumes that you have already configured at least one AWS tunnel in the Cato Management Application. If you have not, please see [Connect your AWS assets to Cato Cloud with Amazon Virtual Private Gateway](/v1/docs/connect-your-aws-assets-to-cato-cloud-with-amazon-virtual-private-gateway) for help setting up the first tunnel.

## Step 1

In the Cato Management Application, navigate to **Configuration** > **Global Settings** < **IP Allocation**. In the Select locations box, use the drop-down menu to select a different PoP location than the one that already exists. The IP that is allocated will appear on the right side. Take note of the IP address - you'll need to enter it in the AWS configuration.

![360000575349-mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248109819677.png)

## Step 2

In AWS, navigate to the **VPC Dashboard** > **Customer Gateways.** Create a second Customer Gateway using the new IP address allocated above.

![360000570665-mceclip2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248156371485.png)You should now see the new Customer Gateway with no VPC assigned.

![360000575369-mceclip3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248124644125.png)

## Step 3

Navigate to **VPC Dashboard** > **VPN Connections**. Create a new VPN Connection with the following parameters:

- **Virtual Private Gateway**: select the same one as the existing VPN Connection.
- **Customer Gateway**: select Existing and choose the one you just created.
- **Routing Options**: Static
- **Static IP Prefixes**: 0.0.0.0/0 (if all traffic from your VPC is routed through Cato)
- (Optional) **Pre-Shared Key for Tunnel 1**: Enter the string for the pre-shared key. If nothing is entered, Amazon will automatically create one.

![360000570705-mceclip4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248124747037.png)

You should now have two VPN Connections, with the new one in the pending state.

![360000570725-mceclip5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248116396445.png)

## Step 4

Highlight the new VPN Connection and click the "Download Configuration" button. Select "Generic" for the Vendor.

![360000575389-mceclip6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248156726045.png)

## Step 5

Open the configuration file and find the configuration for IPsec Tunnel #1. Copy and save the Pre-Shared Key as well as the Virtual Private Gateway IP Address. You'll need this to configure the tunnel in the Cato Management Application.

![360000575409-mceclip7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248116517021.png)![360000575449-mceclip9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248144061341.png)

## Step 6

Go back to the Cato Management Application and enter your AWS site configuration. Leave the primary tunnel as is, but add or change the secondary tunnel with the following values:

- **Secondary Source (Egress) IP**: select the IP address allocated in step 1 above.
- **Secondary Destination IP**: Enter the Virtual Private Gateway Outside IP Address from the AWS configuration file.
- **Set/Change Secondary Password**: Enter the Pre-Shared Key that you specified or the one provided in the AWS configuration file.

![360000575429-mceclip8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248156971293.png)

## Step 7

Shortly after saving the configuration in the Cato Management Application, you should see an UP status for one of the two tunnels in each AWS VPN connection.

![360000570765-mceclip10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248133105565.png)

If you check the AWS's sites Analtyics in the Cato Management Application, you should see both the primary and the secondary VPN tunnels connected to the two different PoPs you configured.

![360000575469-mceclip11.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248133183773.png)
