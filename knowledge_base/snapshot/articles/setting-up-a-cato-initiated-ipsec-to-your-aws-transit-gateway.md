---
title: "Setting up a Cato-Initiated IPsec to Your AWS Transit Gateway"
slug: "setting-up-a-cato-initiated-ipsec-to-your-aws-transit-gateway"
updated: 2026-07-31T01:48:21Z
published: 2026-07-31T01:48:21Z
canonical: "knowledge.catonetworks.com/setting-up-a-cato-initiated-ipsec-to-your-aws-transit-gateway"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up a Cato-Initiated IPsec to Your AWS Transit Gateway

## Overview

The [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) provides full-mesh VPC interconnectivity and allows you to access all your Virtual Private Clouds (VPCs) with a single or multiple VPN connections.

Cato supports **route-based IPsec tunnels with BGP** to AWS Transit Gateway, providing:

- Dynamic route exchange using BGP
- Automatic failover between tunnels
- High availability across multiple Cato PoPs

![360002843337-image-0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797188122013.png)

Depending on your redundancy requirements, you can deploy one of the following architectures:

| **Deployment** | **Description** |
| --- | --- |
| Single Primary Tunnel | One Customer Gateway with a single active tunnel. Suitable for testing or non-critical environments. |
| Dual Primary (Active-Active) Tunnels | Two active tunnels from the same Customer Gateway (same PoP) for load balancing and AWS-side redundancy. **Note:** To achieve effective load balancing, BGP metrics between tunnels must be the same, and ECMP support must be enabled on the AWS side. |
| Primary + Secondary (Active-Passive) Tunnels | Two Customer Gateways using different Cato PoPs for complete end-to-end redundancy. Recommended for production deployments. |

> [!NOTE]
> **Note:**
> 
> Cato doesn't support policy-based IPsec routing for IKEv1 IPsec sites for AWS Transit Gateways, only route-based IPsec with BGP is supported.

## AWS Components

| **Component** | **Description** |
| --- | --- |
| Transit Gateway (TGW) | Central routing hub that connects multiple VPCs and VPN attachments. |
| Customer Gateway | AWS representation of the remote VPN endpoint. In this deployment, the Cato PoP acts as the Customer Gateway. |
| VPN Attachment | Connects the Transit Gateway to the Customer Gateway using IPsec tunnels. |
| VPC Attachment | Connects one or more VPCs to the Transit Gateway. |
| Transit Gateway Route Table | Stores dynamically learned BGP routes and determines packet forwarding. |

## 

## Creating the Primary Tunnel between the Transit Gateway and your PoP

In the following procedure, we will connect through the Cato Cloud to the AWS Transit Gateway.

**To create a tunnel between the Transit Gateway and your PoP through the Cato Cloud:**

1. In the Cato Management Application, select a Cato allocated IP address for the site.
  1. From the navigation menu, click **Network > IP Allocation**.

![IP_Allocation.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797194415645.png)
  2. Select a location. A unique IP is allocated by Cato Networks.

The number of unique IPs that you can obtain is determined by your license. For additional IPs, contact your reseller or sales@catonetworks.com.
  3. Click **Save**.
2. In the AWS console, create the Transit Gateway.
  1. Open the VPC service, then in the navigation pane, scroll down to **Transit Gateways**
  2. Click **Create Transit Gateway**.
  3. Configure the Transit Gateway settings, including the name and any required options for your environment.
  4. Configure the **VPN ECMP Support** setting based on your deployment model:
    - **Active-Passive (Primary-Secondary):** Disable VPN ECMP support to ensure the Transit Gateway prefers a single VPN attachment.
    - **Active-Active (Dual Primary):** Enable VPN ECMP support to allow upstream (AWS-to-Cato) load balancing across multiple active VPN tunnels.
3. In the AWS console, create the **VPN** Transit Gateway Attachment.
  1. Open the VPC service, then in the navigation pane scroll down to **Transit Gateways** and click **Transit Gateway Attachments**.
  2. Click **Create Transit Gateway Attachment**.
  3. Configure the Transit Gateway Attachment as follows:

    - **Transit Gateway ID:** select the Transit Gateway previously created.
    - **Attachment type**: VPN
    - **Customer Gateway**: New
    - **IP Address:** enter the Cato allocated IP address (from above).
    - **BGP ASN:** 64515
    - **Routing options**: Dynamic (requires BGP)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(102).png)
  4. Click **Create attachment**.
  5. Click **Close**.
4. In the AWS console, create the **VPC** Transit Gateway Attachment.
  1. Open the VPC service, then in the navigation pane scroll down to **Transit Gateways** and click **Transit Gateway Attachments**.
  2. Click **Create Transit Gateway Attachment**.
  3. Configure the Transit Gateway Attachment as follows:

    - **Transit Gateway ID:** select the same Transit Gateway.
    - **Attachment type**: VPC
    - **VPC ID:** Select the VPC that will be attached to the transit gateway
  4. Click **Create attachment**.
  5. Click **Close**.
5. Review the VPN connection and download the configuration file.
  1. In the VPC navigation pane, scroll up to **Virtual Private Network (VPN)** and click **Site-to-Site VPN Connections**.
  2. Select the checkbox of the VPN Connection that was created in the previous step and click **Download Configuration**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(103).png)
  3. Configure the settings as follows:
    - **Vendor:** Generic
    - **Platform:** Generic
    - **Software:** Vendor Agnostic

![360002843397-image-6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797140260637.png)
  4. Click **Download**.
  5. Open the downloaded file and note the following items under the **IPsec Tunnel #1** section:
    - **Pre-Shared Key**

![360002843377-image-7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797181008541.png)
    - **Outside IP Addresses**- Virtual Private Gateway

![360002923678-image-8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797194986013.png)
    - **Inside IP Addresses** - Customer Gateway and Virtual Private Gateway

![360002843417-image-9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797181186333.png)
    - **BGP Configuration Options** - Virtual Private Gateway ASN and Neighbor IP Address

![360002923658-image-10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797189041949.png)
6. In the Cato Management Application, create and configure the IPsec site.
  1. From the navigation menu, click **Network > Sites** and click **New**.

The **Add Site** panel opens,
  2. Configure the site settings as follows:
    - **Name:** AWS TGW (example)
    - **Type:** Cloud Data Center
    - **Connection Type:** IPsec IKEv2
    - **Country:** The country in which the configured site is located.
    - **State:** The state, if the country is the United States.
    - **License:** Select the appropriate license.
    - **Native Range:** Any one of your AWS VPC subnets.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(104).png)
  3. Click **Apply**.
  4. From the **Sites** screen, click the new AWS site.
  5. From the navigation menu, click **Site Configuration > IPsec**.
  6. Expand the **Primary** section, and configure the following settings:
    - **Cato IP (Egress):** the unique IP address allocated in step 1 above.
    - Click the **New** button below.
    - Define the **Role** as **WAN1**.
    - **Public IP:** the Virtual Private Gateway Outside IP Address from the AWS configuration file.
    - **Private IPs**

      - **Site**: the Virtual Private Gateway Inside IP Address from the AWS configuration file.
      - **Cato**: the Customer Gateway Inside IP Address from the AWS configuration file.
    - **Bandwidth** (**Downstream** and **Upstream**): the bandwidth according to the site license.
    - **Set/Change Primary Password**: the Pre-Shared Key from the AWS configuration file

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(105).png)
  7. Click **Apply**.
7. Configure the BGP settings for the site.
  1. From the navigation menu, select **Site Configuration > BGP**.
  2. Click **New**. The **(Add BGP Neighbor)** panel opens.
  3. Configure the **General** settings:
    - **Description:** AWS TWG #1 (example)
    - **ASN Settings**
      - **Peer:** the Virtual Private Gateway ASN from the AWS configuration file
      - **Cato:** ASN for the Cato Cloud
    - **IP > Peer:** The Neighbor IP address from the AWS configuration file
  4. Configure the **Policy** settings for the BGP routes:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(106).png)
    - Select the options for the routes that you want to advertise (**Default route** and/or **All routes**) and the routes that you want to accept (**Dynamic routes**).
  5. Click **Apply**.
8. Confirm the connectivity status of the IPsec tunnel and the BGP routes are **Connected**.
  1. From the navigation pane, select **IPsec** and then click **Connection Status**.
  2. From the navigation pane, select BGP and then click **Show BGP Status**.

> [!NOTE]
> **Note:**
> 
> Cato routes propagate to the AWS Transit Gateway routing table but not the VPC routing tables. Create routes back to your on-premises networks in each VPC using the Transit Gateway as the target as shown in the procedure below
9. In your AWS console, in the Navigation pane scroll to **Virtual Private Cloud** and click **Route Tables**.
10. Select a route table associated with a VPC you want to access through the Transit Gateway, click the **Routes** tab, and then click **Edit Routes**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(107).png)
11. Click **Add route**, and then configure the settings as follows:
  - **Destination:** enter a subnet of your local network. This can be a summary route.
  - **Target**: Select the Transit Gateway.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(108).png)
12. Repeat the previous step to create routes for all your local networks that need access to the VPC.
13. Click **Save routes.**
14. Repeat steps 10 - 13 for each VPC that you need to access through the Transit Gateway.

## Creating a Second Primary Tunnel between the Transit Gateway and the Cato PoP (Active-Active)

When setting up an AWS VPN connection, AWS provides two VPN tunnels per customer Gateway. This provides redundancy on the AWS side. However, both tunnels must be connected to the same PoP.

This setup can be useful to configure **Active-Active** IPsec tunnels for load balancing and partial redundancy. If you want to configure a secondary (passive) tunnel and achieve full redundancy, skip this procedure and continue to [Creating the Secondary Tunnel between the Transit Gateway and the Cato PoP](/v1/docs/setting-up-a-cato-initiated-ipsec-to-your-aws-transit-gateway#creating-the-redundant-tunnel-between-the-transit-gateway-and-the-cato-pop)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(110).png)

The following procedure describes how to configure a second primary tunnel in both AWS Console and the Cato Management Application.

> [!NOTE]
> **Note:**
> 
> This procedure assumes that in the Cato Management Application you already configured one tunnel to the AWS Transit Gateway, as described in [Creating the Primary Tunnel between the Transit Gateway and your POP](/v1/docs/setting-up-a-cato-initiated-ipsec-to-your-aws-transit-gateway#creating-the-primary-tunnel-between-the-transit-gateway-and-your-pop).

**To create a second primary tunnel between the Transit Gateway and your PoP through the Cato Cloud:**

1. Download the configuration file.
  1. In the VPC navigation pane, scroll up to **Virtual Private Network (VPN)** and click **Site-to-Site VPN Connections**.
  2. Select the checkbox of the VPN Connection that was created in the previous section and click **Download Configuration**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(111).png)
  3. Configure the settings as follows:
    - **Vendor:** Generic
    - **Platform:** Generic
    - **Software:** Vendor Agnostic
  4. Click **Download**.
  5. Open the downloaded file and note the following items under the **IPsec Tunnel #2** section:
    - **Pre-Shared Key**
    - **Outside IP Addresses**- Virtual Private Gateway
    - **Inside IP Addresses** - Customer Gateway and Virtual Private Gateway
    - **BGP Configuration Options** - Virtual Private Gateway ASN and Neighbor IP Address
2. In the Cato Management Application, configure the second primary tunnel.
  1. From the navigation menu, click **Network > Sites** and click the AWS Transit Gateway IPsec site.
  2. Expand the **Primary** section and configure the following settings:
    - Click the **New** button below.
    - Define the **Role** as WAN2
    - **Public IP**: the Virtual Private Gateway Outside IP Address from the AWS configuration file (tunnel 2).
    - **Private IPs**
      - **Site**: the Virtual Private Gateway Inside IP Address from the AWS configuration file.
      - **Cato**: the Customer Gateway Inside IP Address from the AWS configuration file.
    - **Bandwidth** (**Downstream** and **Upstream**): the bandwidth according to the site license.
    - **Set/Change the PSK**: the Pre-Shared Key from the AWS configuration file ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(112).png)
    1. Click **Apply**.
3. Configure the BGP settings for the second primary tunnel for the site.
  1. From the navigation menu, select **Site Configuration > BGP**.
  2. Click **New**. The **Add Rule** panel opens.
  3. Configure the **General** settings:
    - **Description:** AWS TWG #2 (example)
    - **ASN Settings**
      - **Peer:** the Virtual Private Gateway ASN from the AWS configuration file
      - **Cato:** ASN for the Cato Cloud
    - **IP > Peer:** The Neighbor IP address from the AWS configuration file
  4. Configure the **Policy** settings for the BGP routes
    - Select the options for the routes that you want to advertise (**Default route** and/or **All routes**) and the routes that you want to accept (**Dynamic routes**).
  5. Click **Apply**, and then click **Save**.
4. Confirm the connectivity status of the IPsec tunnel and the BGP routes are **Connected**.
  1. From the navigation pane, select **IPsec** and then click **Connection Status**.
  2. From the navigation pane, select BGP and then click **Show BGP Status** and check the status of the second primary tunnel.

## Creating the Secondary Tunnel between the Transit Gateway and the Cato PoP **(Active-Passive)**

To provide Active-Passive redundancy for both the Cato Cloud and AWS, you must create two Customer Gateways in AWS, then define one tunnel from one Customer Gateway for the primary tunnel and one tunnel from the other Customer Gateway for the secondary tunnel. This allows you to configure the primary and secondary tunnels on PoPs in different locations.

The following procedure describes how to configure a secondary tunnel in both AWS Console and the Cato Management Application![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(113).png)

> [!NOTE]
> Note:
> 
> This procedure assumes that in the Cato Management Application you already configured one tunnel to the AWS Transit Gateway, as described in [Creating the Primary Tunnel between the Transit Gateway and your POP.](/v1/docs/setting-up-a-cato-initiated-ipsec-to-your-aws-transit-gateway#creating-the-primary-tunnel-between-the-transit-gateway-and-your-pop)

**To create a redundant tunnel between the Transit Gateway and your PoP through the Cato Cloud:**

1. In the Cato Management Application, select a Cato allocated IP address for the site.
  1. From the navigation menu, click **Network > IP Allocation**.

![IP_Allocation.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797194415645.png)
  2. Select a location. A unique IP is allocated by Cato Networks.

The number of unique IPs that you can obtain is determined by your license. For additional IPs, contact your reseller or sales@catonetworks.com.
  3. Click **Save**.
2. In the AWS console, create a **VPN** Transit Gateway Attachment.
  1. Open the VPC service, then in the navigation pane scroll down to **Transit Gateways** and click **Transit Gateway Attachments**.
  2. Click **Create Transit Gateway Attachment**.
  3. Configure the Transit Gateway Attachment as follows:
    - **Transit Gateway ID:** select the Transit Gateway created in the section [Creating the Primary Tunnel between the Transit Gateway and your PoP](/v1/docs/setting-up-a-cato-initiated-ipsec-to-your-aws-transit-gateway#creating-the-primary-tunnel-between-the-transit-gateway-and-your-pop)
    - **Attachment type**: VPN
    - **Customer Gateway**: New
    - **IP Address:** enter the Cato allocated IP address (from above).
    - **BGP ASN:** 64515
    - **Routing options**: Dynamic (requires BGP)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(115).png)
  4. Click **Create attachment**.
  5. Click **Close**.
3. Review the VPN connection and download the configuration file.
  1. In the VPC navigation pane, scroll up to **Virtual Private Network (VPN)** and click **Site-to-Site VPN Connections**.
  2. Select the checkbox of the VPN Connection that was created in the previous step and click **Download Configuration**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(116).png)
  3. Configure the settings as follows:
    - **Vendor:** Generic
    - **Platform:** Generic
    - **Software:** Vendor Agnostic

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(117).png)
  4. Click **Download**.
  5. Open the downloaded file and note the following items under the **IPsec Tunnel #1** section:
    - **Pre-Shared Key**

![360002843377-image-7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797181008541.png)
    - **Outside IP Addresses**- Virtual Private Gateway

![360002923678-image-8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797194986013.png)
    - **Inside IP Addresses** - Customer Gateway and Virtual Private Gateway

![360002843417-image-9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797181186333.png)
    - **BGP Configuration Options** - Virtual Private Gateway ASN and Neighbor IP Address

![360002923658-image-10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25797189041949.png)
4. In the Cato Management Application, configure the AWS Transit Gateway IPsec site for redundant tunnels.
  1. From the navigation menu, click **Network > Sites** and click the AWS Transit Gateway IPsec site.
  2. From the navigation menu, click **Site Configuration > IPsec**.
  3. Expand the **Secondary** section and configure the following settings:

    - **Cato IP (Egress):** the unique IP address allocated in step 1 above.
    - Click the **New** button below.
    - Define the Role as **WAN1**.
    - **Public IP**: the Virtual Private Gateway Outside IP Address from the AWS configuration file.
    - **Private IPs**

      - **Site**: the Virtual Private Gateway Inside IP Address from the AWS configuration file.
      - **Cato**: the Customer Gateway Inside IP Address from the AWS configuration file.
    - Bandwidth (**Downstream** and **Upstream**): the bandwidth according to the site license
    - **Set/Change Primary Password**: the Pre-Shared Key from the AWS configuration file

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(119).png)
  4. Click **Save**.
5. Configure the BGP settings for the redundant tunnel for the site.
  1. From the navigation menu, select **Site Configuration > BGP**.
  2. Click **New**. The **Add Rule** panel opens.
  3. Configure the **General** settings:
    - **Description:** AWS TWG #2 (example)
    - **ASN Settings**
      - **Peer:** the Virtual Private Gateway ASN from the AWS configuration file
      - **Cato:** ASN for the Cato Cloud
    - **IP > Peer:** The Neighbor IP address from the AWS configuration file
  4. Configure the **Policy** settings for the BGP routes:
    - Select the options for the routes that you want to advertise (**Default route** and/or **All routes**) and the routes that you want to accept (**Dynamic routes**).
  5. Click **Apply**, and then click **Save**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(120).png)
6. Confirm the connectivity status of the IPsec tunnel and the BGP routes are **Connected**.
  1. From the navigation pane, select **IPsec** and then click **Connection Status**.
  2. From the navigation pane, select BGP and then click **Show BGP Status** and check the status of the secondary tunnel.

> [!NOTE]
> **Note:**
> 
> Cato routes propagate to the AWS Transit Gateway routing table but not the VPC routing tables. Create routes back to your on-premises networks in each VPC using the Transit Gateway as the target as shown in the first section above
