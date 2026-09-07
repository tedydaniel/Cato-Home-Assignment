---
title: "Socket VLAN Tagging Troubleshooting"
slug: "socket-vlan-tagging-troubleshooting"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/socket-vlan-tagging-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket VLAN Tagging Troubleshooting

## Overview

Cato Sockets support VLAN tagging based on the IEEE 802.1Q standard across both LAN and WAN interfaces. VLAN tagging enables logical network segmentation, traffic isolation, and scalable network design by allowing multiple VLANs to traverse a single interface. For more information, see [Network Segmentation - Best Practices](/v1/docs/network-segmentation-best-practices).

In Cato environments, VLAN tagging applies to:

- **Physical Cato Sockets** and **ESX vSockets** only.
- **VLAN-enabled ranges:** Cato inserts 802.1Q tags into Ethernet frames for configured [VLAN ranges](/v1/docs/configuring-network-ranges-for-a-site).
- **Native range traffic:** Cato supports VLAN tagging behavior for traffic associated with the [native range](/v1/docs/configuring-sites-with-cato-sockets#configuring-the-native-range), depending on the switch's trunk configuration.
- **WAN uplinks:** VLAN tagging on WAN interfaces is configurable through the [Socket WebUI](/v1/docs/accessing-the-socket-webui) for service-provider or carrier-specific requirements.

This article describes common VLAN tagging issues observed with Cato Sockets, their root causes, and structured troubleshooting steps to help customers validate and resolve connectivity problems.

## Symptoms

VLAN tagging issues typically present as one or more of the following symptoms:

- Devices on VLAN-enabled ranges cannot communicate with the network.
- ARP or DHCP requests do not receive replies.
- Packet captures show missing or incorrect 802.1Q VLAN tags.
- Inter-VLAN traffic is routed to the Cato Cloud instead of locally.
- BGP neighbors fail to establish over VLAN-backed interfaces.
- Endpoints receive incorrect IP address ranges or no IP address at all.

## Understanding VLAN Trunk Scenarios

The following diagram illustrates two common trunk configurations between a Cato Socket and a switch:

- In Scenario 1, no VLAN is configured for the native range in CMA. Untagged frames on the trunk (e.g., native VLAN 1 on the switch) are mapped to the native range on the Socket.
- In Scenario 2, VLAN 5 is configured for the native range in CMA. Frames tagged with VLAN 5 are mapped to the native range on the Socket.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36260004729757.png)

## Troubleshooting the Issue

Use the following troubleshooting sections to isolate issues based on the observed symptom. Packet captures collected from the Socket WebUI and analyzed in Wireshark are critical for validating VLAN tags and frame structure.

### Troubleshooting VLAN Ranges Issues

1. Verify the switch port connected to the Socket is configured as a trunk and allows all required VLAN IDs, including the VLAN configured for the native range (if configured).
2. Confirm that the native VLAN behavior on both the switch and the Socket (tagged vs. untagged) is consistent with the above VLAN Trunk scenarios.
3. In the CMA, review the VLAN-enabled ranges and ensure the configured VLAN IDs match the switch configuration.
4. Collect a PCAP from the relevant Socket LAN interface using the WebUI.
5. Open the capture in Wireshark and inspect the Ethernet header for the presence of an 802.1Q tag and the expected VLAN ID. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36237223807133.png) ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29469836626973.png)

**Note:** A successful ARP request on a VLAN-enabled range includes an 802.1Q header with the correct VLAN ID. Frames missing the VLAN tag are typically discarded by downstream trunk ports.

### Troubleshooting Inter-VLAN Routing Problems

1. Analyze CMA events related to the affected Inter-VLAN traffic.
2. Confirm whether the LAN firewall is enabled on the Socket.
3. Review [LAN firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall) rules to ensure inter-VLAN traffic is explicitly allowed.
  - Note that if a **LAN network rule** is configured for inter-vlan traffic and no **LAN firewall rule** allows it, it is blocked by default.
  - If [microsegmentation](/v1/docs/adding-microsegmentation-zero-trust-security-to-sites) is enabled on the VLAN network range, ensure that the LAN firewall allows **intra-VLAN** traffic.
4. If the LAN firewall isn't enabled, check the WAN firewall rules to confirm they are not unintentionally blocking routed VLAN traffic.
5. Collect a PCAP from the relevant Socket LAN interface using the WebUI. Ensure that frames contain the correct VLAN tag as configured in CMA and the switch trunk port.

### Troubleshooting BGP Failure Over VLAN Ranges

1. Verify that the VLAN-enabled range used for the BGP peer has the correct VLAN ID configured.
2. Confirm that the connected switch or router expects BGP traffic on the same VLAN.
3. Capture traffic on the Socket interface and validate that BGP packets are tagged with the correct VLAN.
4. Check for asymmetric routing caused by mismatched VLAN tagging on ingress and egress paths.

### Troubleshooting DHCP and IP Assignment Issues

1. Confirm that the downstream switch trunk allows the VLAN associated with the DHCP scope.
2. Verify that DHCP requests from endpoints are tagged with the expected VLAN ID.
3. Use a PCAP on the Socket to validate that DHCP Discover and Offer messages are visible and correctly tagged.
4. Ensure that no overlapping or conflicting VLAN configurations exist on intermediate switches.

## Raising Cases to Cato Support

If the issue persists after completing the troubleshooting and resolution steps, escalate the case to Cato Support with sufficient diagnostic data.

- Description of the affected VLAN IDs and ranges.
- Relevant switch or hypervisor configuration details.
- PCAP files collected from the Socket interfaces.
- Issue timeframe and whether it is intermittent or persistent.
- Any recent configuration changes related to VLANs, routing, or firewall rules.
