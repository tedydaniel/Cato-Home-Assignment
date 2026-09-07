---
title: "Setting up a Cato IPsec Tunnel to Your Azure Virtual Network Gateway"
slug: "setting-up-a-cato-ipsec-tunnel-to-your-azure-virtual-network-gateway"
updated: 2026-07-31T02:20:50Z
published: 2026-07-31T02:20:50Z
canonical: "knowledge.catonetworks.com/setting-up-a-cato-ipsec-tunnel-to-your-azure-virtual-network-gateway"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up a Cato IPsec Tunnel to Your Azure Virtual Network Gateway

## Overview

This article describes how to connect Azure resources to the Cato Cloud with Azure Virtual Network Gateway using a single or multiple VPN connections.

Cato supports route-based IPsec tunnels with BGP to Azure Virtual Network Gateway, providing:

- Dynamic route exchange using BGP
- Automatic failover between tunnels
- High availability across multiple Cato PoPs

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(124).png)

Depending on your redundancy requirements, you can deploy one of the following architectures:

| **Deployment** | **Description** |
| --- | --- |
| Single Primary Tunnel | One Local Network Gateway with a single active tunnel. Suitable for testing or non-critical environments. |
| Dual Primary (Active-Active) Tunnels | Two active tunnels from the same Local Network Gateway (same PoP) for load balancing and Azure-side redundancy. **Note:** To achieve effective load balancing, BGP metrics between tunnels must be the same. |
| Primary + Secondary (Active-Passive) Tunnels | Two Local Network Gateways using different Cato PoPs for complete end-to-end redundancy. Recommended for production deployments. |

## Azure Components

| **Component** | **Description** |
| --- | --- |
| Virtual Network Gateway | Primary Azure endpoint where the IPSec tunnel terminates and runs BGP. |
| Local Network Gateway | Azure representation of the remote VPN endpoint. In this deployment, the Cato PoP acts as the Local Network Gateway. |
| VPN Connection | The IPSec/BGP relationship between the Virtual Network Gateway and the Local Network Gateway (PoP) |
| Virtual Network (VNet) | Provides Azure address space and contains the Gateway Subnet which is required for the Virtual Network Gateway |
| Virtual Network Router | Routes traffic based on the dynamically learned BGP routes. |

## Creating a Single Tunnel between the Virtual Network Gateway and your PoP

This section describes how to configure a single route-based IPsec tunnel between a Cato site and an Azure Virtual Network Gateway.

**To create a tunnel between the Virtual Network Gateway and your PoP through the Cato Cloud:**

1. In the Cato Management Application, select a Cato allocated IP address for the site.
  1. From the navigation menu, click **Network > IP Allocation**.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444344792.png)
  2. Select a location. A unique IP is allocated by Cato Networks.

The number of unique IPs that you can obtain is determined by your license. For additional IPs, contact your reseller or sales@catonetworks.com.
  3. Click **Save**.

1. In the Azure console, create a Virtual Network (VNet).
  1. From the Azure Marketplace, create a new Virtual Network and associate it with a resource group.
  2. Create two subnets:
    - A Virtual Network Gateway subnet to be used with the Virtual Network Gateway
    - A Workload subnet to be used with Azure Virtual Machines

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444344794.png)

1. In the Azure console, create the Virtual Network Gateway.
  1. From the Azure Marketplace, create a new Virtual Network Gateway
  2. Configure the Virtual Network Gateway settings, including the subscription, name and region.
  3. Configure the next settings as follows:
    - **Gateway type:** VPN
    - **SKU:** VpnGw2AZ (Select based on the desired capacity and performance)
    - **Virtual Network:** Select the VNet previously created
    - **Public IP address:** Create new and add a name
    - **Enable active-active mode:** Disabled
    - **Configure BGP**: Enabled
    - **Autonomous system number (ASN):** 65515. This is the Azure ASN.
    - **Custom Azure APIPA BGP IP address:** 169.254.21.1![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444344796.png)
  4. Click **Review + create**.
  5. The deployment can take around **30 minutes.**
  6. Once the deployment is complete, open the Virtual Network Gateway and under Configuration, gather **BGP** and **public IP address** information.

1. In the Azure console, create the Local Network Gateway.
  1. From the Azure Marketplace, create a new Local Network Gateway
  2. Configure the Local Network Gateway settings, including the subscription, resource group, region, name and the IP address allocated from CMA in step 1.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444346084.png)
  3. Click **Next** and under **Advanced settings** configure:
    - **Configure BGP settings:** Yes
    - **Autonomous system number (ASN):** 65512. This is the Cato ASN.
    - **BGP Peer IP address:** 169.254.21.3. This is the Cato BGP Peer IP address.
  4. Click **Review + create**.
2. In the Azure console, create the VPN Connection.
  1. Open the Virtual Network Gateway previously created.
  2. Under **Settings > Connections**, click **Add**
  3. Configure the new connection settings, including the subscription, resource group, connection type (**Site-to-Site**), name, and region.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(125).png)
  4. Click **Next** and under **Settings,** configure:
    - **Virtual Network Gateway:** Select the Virtual Network Gateway configured in step 3.
    - **Local Network Gateway**: Select the Local Network Gateway configured in step 4.
    - **Authentication Method**: Shared Key (PSK)
    - **IKE Protocol**: IKEv2
    - **Enable BGP**: Enable
    - **Enable Custom BGP Addresses**: Enable ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444346749.png)
  5. Leave remaining settings as default and click **Review + create**.
3. In the Cato Management Application, create and configure the IPsec site.
  1. From the navigation menu, click **Network > Sites** and click **New**.

The **Add Site** panel opens,
  2. Configure the site settings as follows:
    - **Name:** Azure IPSec (example)
    - **Type:** Cloud Data Center
    - **Connection Type:** IPsec IKEv2
    - **Country:** The country in which the configured site is located.
    - **State:** The state, if the country is the United States.
    - **License:** Select the appropriate license.
    - **Native Range:** Any one of your Azure workload VNet subnets.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444347793.png)
  3. Click **Apply**.
  4. From the **Sites** screen, click the new Azure IPSec site.
  5. From the navigation menu, click **Site Configuration > IPsec**
  6. Expand the **Primary** section and configure the following settings:
    - **Cato IP (Egress)**: the unique IP address allocated in step 1 above.
    - Click the **New** button below and configure the PRIMARY1 tunnel.
    - Define the **Role** as **WAN1**.
    - **Public IP**: the Public IP Address from the Virtual Network Gateway configuration.
    - **Private IPs**
      - **Cato**: 169.254.21.3
      - **Site**: 169.254.21.1
    - **Bandwidth** (**Downstream** and **Upstream**): the bandwidth according to the site license.
    - **Set/Change the PSK**: the Pre-Shared Key configured in step 5![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444347993.png)
  1. Click **Apply**.
4. Under **Init Message Parameters,** ensure that the algorithms selected are **Automatic** and the Diffie-Hellman Group is **2 (1024-bit).**
5. Configure the BGP settings for the site.
  1. From the navigation menu, select **Site Configuration > BGP**.
  2. Click **New**. The **(Add BGP Neighbor)** panel opens.
  3. Configure the **General** settings:
    - **Description:** Azure Peer 1 (example)
    - **ASN Settings**
      - **Peer:** 65515
      - **Cato:** 65512
    - **IP > Peer:** 169.254.21.1
  4. Configure the **Policy** settings for the BGP routes:
    - Select the options for the routes that you want to advertise (**Default route** and/or **All routes**) and the routes that you want to accept (**Dynamic routes**).![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444348569.png)
  1. Click **Apply**.
6. Confirm the connectivity status of the IPsec tunnel and the BGP routes are **Connected**.
  1. From the navigation pane, select **IPsec** and then click **Connection Status**.
  2. From the navigation pane, select BGP and then click **Show BGP Status**.

> [!NOTE]
> **Note:**
> 
> Cato routes propagate to the Azure Virtual Network Gateway and to the VNet default routing table.

1. To view the dynamically learned routes via BGP, open the **Virtual Network Gateway** and click **Monitoring BGP Peers**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444348608.png)

1. Dynamic routes can also be viewed from an internal VM’s **network interface**, under **Help > Effective routes**.
2. You may propagate dynamic routes to other VNets via VNet peering in a Hub-and-Spoke topology.

## Creating Active-Active Tunnels between the Virtual Network Gateway and the Cato PoP

In the following procedure, we will deploy two **Active-Active** tunnels between a single Azure Virtual Network Gateway and a **single Cato PoP**.

This setup can be useful for load balancing and partial Azure-side redundancy.

> [!NOTE]
> **Note:**
> 
> Active-active tunnels do not protect against a Cato PoP outage because both tunnels terminate on the same PoP.

If you want to configure a secondary (passive) tunnel and achieve full redundancy, skip this procedure and continue to [Creating the Secondary (Passive) Tunnel between the Virtual Network Gateway and the Cato PoP](/v1/docs/setting-up-a-cato-ipsec-tunnel-to-your-azure-virtual-network-gateway#creating-the-secondary-passive-tunnel-between-the-virtual-network-gateway-and-the-cato-pop)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444349219.png)

**To create Active-Active tunnels between the Virtual Network Gateway and your PoP through the Cato Cloud:**

1. In the Cato Management Application, select a Cato allocated IP address for the site.
  1. From the navigation menu, click **Network > IP Allocation**.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444349534.png)
  2. Select a location. A unique IP is allocated by Cato Networks.

The number of unique IPs that you can obtain is determined by your license. For additional IPs, contact your reseller or sales@catonetworks.com.
  3. Click **Save**.

1. In the Azure console, create a Virtual Network (VNet).
  1. From the Azure Marketplace, create a new Virtual Network and associate it with a resource group.
  2. Create two subnets:
    1. A Virtual Network Gateway subnet to be used with the Virtual Network Gateway
    2. A Workload subnet to be used with Azure Virtual Machines

1. In the Azure console, create the Virtual Network Gateway.
  1. From the Azure Marketplace, create a new Virtual Network Gateway
  2. Configure the Virtual Network Gateway settings, including the subscription, name and region.
  3. Configure the next settings as follows:
    - **Gateway type:** VPN
    - **SKU:** VpnGw2AZ (Select based on the desired capacity and performance)
    - **Virtual Network:** Select the VNet previously created
    - **Public IP address:** Create new and add a name
    - **Enable active-active mode:** Enabled
    - **Second Public IP address :** Create new and add a name
    - **Configure BGP**: Enabled
    - **Autonomous system number (ASN):** 65515. This is the Azure ASN.
    - **Custom Azure APIPA BGP IP address:** 169.254.21.1
    - **Second Custom Azure APIPA BGP IP address:** 169.254.21.2![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444350107.png)
  4. Click **Review + create**.
  5. The deployment can take around **30 minutes.**
  6. Once the deployment is complete, open the Virtual Network Gateway and under Configuration, gather **BGP** and **public IP address** information.
2. In the Azure console, create the Local Network Gateway.
  1. From the Azure Marketplace, create a new Local Network Gateway
  2. Configure the Local Network Gateway settings, including the subscription, resource group, region, name, and the IP address allocated from CMA in step 1.
  3. Click **Next** and under **Advanced settings,** configure:
    - **Configure BGP settings:** Yes
    - **Autonomous system number (ASN):** 65512. This is the Cato ASN.
    - **BGP Peer IP address:** 169.254.21.3. This is the Cato BGP Peer IP address. Azure only allows one Peer IP address for a single local network gateway. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444346172.png)
  4. Click **Review + create**.
3. In the Azure console, create the VPN Connection.
  1. Open the Virtual Network Gateway previously created.
  2. Under **Settings > Connections**, click **Add**
  3. Configure the new connection settings, including the subscription, resource group, connection type (**Site-to-Site**), name, and region.
  4. Click **Next** and under **Settings** configure:
    - **Virtual Network Gateway:** Select the Virtual Network Gateway configured in step 3.
    - **Local Network Gateway**: Select the Local Network Gateway configured in step 4.
    - **Authentication Method**: Shared Key (PSK)
    - **IKE Protocol**: IKEv2
    - **Enable BGP**: Enable
    - **Enable Custom BGP Addresses**: Enable and select primary and secondary BGP addresses.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444350905.png)
  5. Leave the remaining settings as the default and click **Review + create**.
4. In the Cato Management Application, create and configure the IPsec site.
  1. From the navigation menu, click **Network > Sites** and click **New**.

The **Add Site** panel opens,
  2. Configure the site settings as follows:
    - **Name:** Azure IPSec (example)
    - **Type:** Cloud Data Center
    - **Connection Type:** IPsec IKEv2
    - **Country:** The country in which the configured site is located.
    - **State:** The state, if the country is the United States.
    - **License:** Select the appropriate license.
    - **Native Range:** Any one of your Azure workload VNet subnets.
  3. Click **Apply**.
  4. From the **Sites** screen, click the new Azure IPSec site.
  5. From the navigation menu, click **Site Configuration > IPsec**
  6. Expand the **Primary** section and configure the following settings:
    - **Cato IP (Egress)**: the unique IP address allocated in step 1 above.
    - Click the **New** button below and configure the PRIMARY1 tunnel.
    - Define the **Role** as **WAN1**.
    - **Public IP**: the Public IP Address from the Virtual Network Gateway configuration.
    - **Private IPs**
      - **Cato**: 169.254.21.3
      - **Site**: 169.254.21.1
    - **Bandwidth** (**Downstream** and **Upstream**): the bandwidth according to the site license.
    - **Set/Change the PSK**: the Pre-Shared Key configured in step 5![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444351822.png)
  7. In the same **Primary** section, click **New** and configure the PRIMARY2 tunnel:
    - Define the **Role** as **WAN2**.
    - **Public IP**: the Second Public IP Address from the Virtual Network Gateway configuration.
    - **Private IPs**
      - **Cato**: 169.254.21.3
      - **Site**: 169.254.21.2
    - **Bandwidth** (**Downstream** and **Upstream**): the bandwidth according to the site license.
    - **Set/Change the PSK**: the Pre-Shared Key configured in step 5![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444352030.png)
  8. Click **Apply**.
5. Under **Init Message Parameters,** ensure that the algorithms selected are **Automatic** and the Diffie-Hellman Group is **2 (1024-bit).**
6. Configure the BGP settings for the site.
  1. From the navigation menu, select **Site Configuration > BGP**.
  2. Click **New**. The **(Add BGP Neighbor)** panel opens.
  3. Configure the **General** settings:
    - **Description:** Azure Peer 1 (example)
    - **ASN Settings**
      - **Peer:** 65515
      - **Cato:** 65512
    - **IP > Peer:** 169.254.21.1
  4. Configure the **Policy** settings for the BGP routes:
    - Select the options for the routes that you want to advertise (**Default route** and/or **All routes**) and the routes that you want to accept (**Dynamic routes**).![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444352350.png)
  5. Click **Apply**.
  6. On the same **BGP** page, create a second BGP peer
  7. Click **New**. The **(Add BGP Neighbor)** panel opens.
  8. Configure the **General** settings:
    - **Description:** Azure Peer 2 (example)
    - **ASN Settings**
      - **Peer:** 65515
      - **Cato:** 65512
    - **IP > Peer:** 169.254.21.2
  9. Configure the **Policy** settings for the BGP routes:
    - Select the options for the routes that you want to advertise (**Default route** and/or **All routes**) and the routes that you want to accept (**Dynamic routes**).
  10. Click **Apply**.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444352634.png)
7. Confirm the connectivity status of the IPsec tunnel and the BGP routes are **Connected**.
  1. From the navigation pane, select **IPsec** and then click **Connection Status**.
  2. From the navigation pane, select BGP and then click **Show BGP Status**.

> [!NOTE]
> Note:
> 
> Cato routes propagate to the Azure Virtual Network Gateway and to the VNet default routing table.

1. To view the dynamically learned routes via BGP, open the **Virtual Network Gateway** and click **Monitoring BGP Peers**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444352937.png)

1. Dynamic routes can also be viewed from an internal VM’s **network interface**, under **Help > Effective routes**.
2. You may propagate dynamic routes to other VNets via VNet peering in a Hub-and-Spoke topology.

## Creating the Secondary Tunnel between the Virtual Network Gateway and the Cato PoP (Active-Passive)

To provide **Active-Passive** redundancy for both the Cato Cloud and Azure, Azure requires:

- One Virtual Network Gateway
- Two Local Network Gateways
- Two VPN Connections
- Two independent BGP sessions.

The primary tunnel remains active under normal operation, while the secondary tunnel is used automatically if the primary path becomes unavailable.

The following procedure describes how to configure a secondary tunnel in both Azure Console and the Cato Management Application.

> [!NOTE]
> **Note:** This procedure assumes that you have completed the steps described in [Creating a Single Tunnel between the Virtual Network Gateway and your PoP](/v1/docs/setting-up-a-cato-ipsec-tunnel-to-your-azure-virtual-network-gateway#creating-a-single-tunnel-between-the-virtual-network-gateway-and-your-pop) and that the primary tunnel and BGP sessions are operational.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444353152.jpg)

**To create a redundant tunnel between the Virtual Network Gateway and your PoP through the Cato Cloud:**

1. In the Cato Management Application, select a second Cato allocated IP address for the site.
  1. From the navigation menu, click **Network > IP Allocation**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444353443.png)
  2. Select a location. A unique IP is allocated by Cato Networks.

The number of unique IPs that you can obtain is determined by your license. For additional IPs, contact your reseller or sales@catonetworks.com.
  3. Click **Save**.
2. In the Azure console, edit the existing Virtual Network Gateway.
  1. In the existing Virtual Network Gateway, go to **Settings > Configuration**
  2. Configure a second BGP IP address as: 169.254.22.1![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444353809.png)
3. In the Azure console, create a second Local Network Gateway.
  1. From the Azure Marketplace, create a new Local Network Gateway
  2. Configure the Local Network Gateway settings, including the subscription, resource group, region, name and the IP address allocated from CMA in step 1.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444354372.png)
  3. Click **Next** and under **Advanced settings** configure:
    - **Configure BGP settings:** Yes
    - **Autonomous system number (ASN):** 65512. This is the Cato ASN.
    - **BGP Peer IP address:** 169.254.22.3. This is the Cato BGP Peer IP address.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(126).png)
  4. Click **Review + create**.
4. In the Azure console, create a second VPN Connection.
  1. Open the existing Virtual Network Gateway.
  2. Under **Settings > Connections**, click **Add**
  3. Configure the new connection settings, including the subscription, resource group, connection type (**Site-to-Site**), name, and region.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444354701.png)
  4. Click **Next** and under **Settings** configure:
    - **Virtual Network Gateway:** Select the existing Virtual Network Gateway
    - **Local Network Gateway**: Select the Local Network Gateway configured in step 3.
    - **Authentication Method**: Shared Key (PSK)
    - **IKE Protocol**: IKEv2
    - **Enable BGP**: Enable
    - **Enable Custom BGP Addresses**: Enable
    - **Primary Custom BGP address**: 169.254.22.1

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(128).png)
  5. Leave the remaining settings as the default and click **Review + create**.
5. In the Cato Management Application, create and configure the Secondary tunnel.
  1. From the navigation menu, click **Site Configuration > IPsec**
  2. Expand the **Secondary** section and configure the following settings:
    - **Cato IP (Egress)**: the unique IP address allocated in step 1 above.
    - Click the **New** button below and configure the SECONDARY1 tunnel.
    - Define the **Role** as **WAN1**.
    - **Public IP**: the Public IP Address from the Virtual Network Gateway configuration. This is the same public IP as the Primary tunnel.
    - **Private IPs**
      - **Cato**: 169.254.22.3
      - **Site**: 169.254.22.1
    - **Bandwidth** (**Downstream** and **Upstream**): the bandwidth according to the site license.
    - **Set/Change the PSK**: the Pre-Shared Key configured in step 4![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444355598.png)
  3. Click **Apply**.
6. Configure the second BGP peer settings for the site.
  1. From the navigation menu, select **Site Configuration > BGP**.
  2. Click **New**. The **(Add BGP Neighbor)** panel opens.
  3. Configure the **General** settings:
    - **Description:** Azure Peer 2 (example)
    - **ASN Settings**
      - **Peer:** 65515
      - **Cato:** 65512
    - **IP > Peer:** 169.254.22.1
  4. Configure the **Policy** settings for the BGP routes: Select the options for the routes that you want to advertise (**Default route** and/or **All routes**) and the routes that you want to accept (**Dynamic routes**).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(131).png)
  5. Click **Apply**.
7. Confirm the connectivity status of the IPsec tunnel and the BGP routes are **Connected**.
  1. From the navigation pane, select **IPsec** and then click **Connection Status**.
  2. From the navigation pane, select BGP and then click **Show BGP Status**.

> [!NOTE]
> **Note:** Cato routes propagate to the Azure Virtual Network Gateway and to the VNet default routing table.

1. To view the dynamically learned routes via BGP, open the **Virtual Network Gateway** and click **Monitoring BGP Peers**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1785444355923.png)

1. Dynamic routes can also be viewed from an internal VM’s **network interface**, under **Help > Effective routes**.
2. You may propagate dynamic routes to other VNets via VNet peering in a Hub-and-Spoke topology.
