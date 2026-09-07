---
title: "Troubleshooting Routing Issues with Azure vSockets"
slug: "troubleshooting-routing-issues-with-azure-vsockets"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/troubleshooting-routing-issues-with-azure-vsockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Routing Issues with Azure vSockets

## Overview

This article covers routing-related issues involving vSockets deployed in Microsoft Azure Virtual Networks (VNets). It focuses on how Azure's software-defined networking model affects traffic flow between vSocket LAN interfaces, subnets, peered VNets, and external networks. Misunderstanding Azure system routes, effective routes, or IP forwarding behavior can result in asymmetric routing, dropped packets, or unreachable resources.

## Symptoms

Routing issues with Azure vSockets commonly present through the following observable symptoms:

- Traffic does not reach internal VMs either in the same subnet as the LAN or in a different subnet or VNET.
- Outbound traffic from internal resources does not reach its destination.
- High availability (HA) deployments fail to route traffic through the active vSocket.

## Possible Causes

- Azure system routes overriding expected traffic paths.
- User-defined routes missing or misconfigured.
- IP forwarding disabled on the vSocket LAN network interface.
- Incorrect floating IP configuration in HA deployments.
- Network Security Group (NSG) rules blocking inbound or outbound traffic.
- Misinterpretation of Azure's intra-subnet routing behavior.

## Troubleshooting the Issue

> [!NOTE]
> IMPORTANT:
> 
> Before troubleshooting, verify all prerequisites for Azure vSocket deployment. See [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace).

Use the steps below to isolate routing problems by symptom.

### Defining the Internal Topology

To better understand packet flow and routing behavior within Azure, first define the network topology between Azure VNet(s), the vSocket LAN interface, and internal subnets and VMs.

Refer to the topology diagram below for guidance.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34423383942557(1).png)

### Troubleshooting Traffic Not Reaching Internal Resources

1. Verify that the internal subnets are correctly defined in CMA under **Site Configuration > Networks**. Non-native subnets must have the gateway set to the first available IP address of the LAN (native) subnet. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422239462045(1).png)
2. Review the **LAN routing table**:
  - Confirm that a **0.0.0.0/0** route is configured with the next hop set to the LAN IP address, or, in HA deployment, to the Floating IP address. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422267097373(1).png)
  - If **only specific prefixes** should be reachable via the vSocket, define explicit routes for those prefixes with the same next-hop configuration.
  - Verify that all the required internal subnets are present in the routing table. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422239467805(1).png)
  - If routes or subnets are missing, see [Resolving missing or incorrect routes](/docs/troubleshooting-routing-issues-with-azure-vsockets#h_01KJXDH424J21GVFPYY6SZH9HN)
3. Check **Effective routes** for the LAN interface.
  - Select the LAN interface, then navigate to **Help > Effective routes**.
  - Effective routes include both system (default) routes and User-defined routes (UDR).
  - Identify which route has precedence for the destination prefix. Non-preferred routes will show as "invalid". ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422267098397(1).png)
  - If a system (default) route overrides the user-defined route, see [Resolving missing or incorrect routes](/docs/troubleshooting-routing-issues-with-azure-vsockets#h_01KJXDH424J21GVFPYY6SZH9HN)
4. Validate **Network Security Group** rules:
  - Confirm explicit allow rules exist for inbound and outbound traffic.
  - Pay special attention to rule priority and direction.
  - Select the LAN interface and verify the **Effective security rules**. Ensure that all associated NSG rules allow the expected traffic.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34421269046813(1).png)
  - If a NSG rule is blocking traffic, see [Resolving NSG-related traffic blocks](/v1/docs/troubleshooting-routing-issues-with-azure-vsockets#resolving-nsgrelated-traffic-blocks)
5. Check the status of **IP forwarding** on the vSocket LAN network interface. This setting must be **enabled** to allow the vSocket LAN to receive traffic destined to other destinations. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34443764951069(1).png)
6. Run [PCAP captures](/v1/docs/how-to-capture-traffic-on-a-socket) on the LAN via the vSocket WebUI while generating active traffic. Continue with the next steps to analyze them.

### Analyzing Internal PCAP Captures

1. Review the packet captures taken from the vSocket's LAN.
2. Confirm the following Azure routing behavior:
  - When traffic leaves the vSocket LAN interface, the **destination MAC** will be the **Azure virtual router** (12:34:56:78:9a:bc). This occurs because Azure routes all traffic through its internal virtual router, even when devices are in the same subnet. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34421666051229(1).png)
  - Returning packets typically show the **source MAC** of the **internal VM**. Azure removes the router MAC before delivering the packet to the vSocket. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34421666051741(1).png)

Unlike traditional Layer-2 networks, Azure does not allow direct host-to-host communication within a subnet. All traffic passes through the Azure virtual router. This behavior can make packet captures appear asymmetric.

### Troubleshooting Routing to Non-Native Subnets

If traffic cannot reach resources in **non-native subnets**:

1. Follow the steps explained in [Troubleshooting Traffic Not Reaching Internal Resources.](/v1/docs/troubleshooting-routing-issues-with-azure-vsockets#troubleshooting-traffic-not-reaching-internal-resources)
2. Verify that the non-native subnet exists in CMA. Ensure the gateway is set to the first available IP address of the LAN (native) subnet. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422267099677(1).png)
3. Confirm that the non-native subnet appears in the vSocket LAN routing table ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422239469213(1).png)

### Troubleshooting VNet-to-VNet Routing

When routing between **peered VNets**, verify the following:

1. Ensure that VNET peering and the route tables are configured as explained in [How to Use a vSocket in Azure Multiple VNets Environment](/v1/docs/how-to-use-a-vsocket-in-azure-multiple-vnets-environment)
2. Follow the steps explained in [Troubleshooting Traffic Not Reaching Internal Resources.](/v1/docs/troubleshooting-routing-issues-with-azure-vsockets#troubleshooting-traffic-not-reaching-internal-resources)
3. Verify that the destination subnet (in the **spoke VNet**) exists in CMA. Ensure the gateway is set to the first available IP address of the LAN (native) subnet.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422267100829(1).png)
4. Verify the **Effective routes** on the vSocket's **LAN interface**. It must include the destination subnet with the next hop set to the VNET peering.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422239469725(1).png)
5. Verify the **Effective routes** on the **internal VM**'s interface. It must include the native subnet with the next hop set to the VNET peering, as well as a **0.0.0.0/0** route with the next hop set to the LAN IP address, or, in HA deployment, to the Floating IP address. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34422267101597(1).png)

### Troubleshooting HA Routing Issues

In HA deployments, verify the following:

1. Navigate to the **MASTER** vSocket's LAN interface, **Settings > IP configurations**, and confirm that the **floating IP** is configured as a Secondary IP address.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34444242637085(1).png)
2. Ensure that the LAN routing table on the vSocket includes the floating IP as the 0.0.0.0/0 route next hop. If not, see [Resolving HA floating IP issues](/v1/docs/troubleshooting-routing-issues-with-azure-vsockets#resolving-ha-floating-ip-issues)
3. Ensure that during failover, the floating IP is migrated to the new MASTER vSocket as expected during role changes.

For more information about troubleshooting HA environments, see [Azure HA vSocket Troubleshooting](/v1/docs/azure-ha-vsocket-troubleshooting)

## Resolving Discovered Issues

Apply the appropriate resolution based on the root cause identified during troubleshooting.

### Resolving Missing or Incorrect Routes

1. Create or update user-defined routes in the **LAN routing table** to override Azure system routes when required.
2. Associate the route table with the correct subnet.
3. Select the LAN interface, then navigate to **Help > Effective routes**. Revalidate that the expected path is now preferred.

### Resolving NSG-related Traffic Blocks

1. Add **explicit allow rules** for required protocols, ports, and source/destination prefixes.
2. Ensure that allow rules have a higher priority than deny rules.
3. Retest traffic flow after rule updates.
4. Select the LAN interface, then navigate to **Help > Effective security rules**. Revalidate that the expected allow rules are now preferred.

### Resolving HA Floating IP Issues

1. Follow the steps from [Azure HA vSocket Troubleshooting](/v1/docs/azure-ha-vsocket-troubleshooting) to resolve **Floating IP address** assignment to the MASTER vSocket.
2. Update the LAN routing table if necessary to reference the next hop as the Floating IP. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34444228343197(1).png)
3. Perform controlled failover testing to validate behavior.

## Raising Cases to Cato Support

Escalate to [Cato Support](/v1/docs/submitting-a-support-ticket) if routing behavior remains inconsistent after configuration validation. Provide the following information to accelerate root cause analysis.

- Description of the internal topology.
- Screenshots of subnet routing tables.
- Screenshots of effective routes.
- Network Security Group inbound and outbound rules.
- Confirmation of IP forwarding status on the vSocket LAN interface.
- Packet captures from the vSocket and affected VMs.
