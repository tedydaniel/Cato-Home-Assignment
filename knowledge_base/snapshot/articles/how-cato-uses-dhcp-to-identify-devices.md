---
title: "How Cato Uses DHCP to Identify Devices"
slug: "how-cato-uses-dhcp-to-identify-devices"
updated: 2026-08-17T12:30:39Z
published: 2026-08-17T12:30:39Z
canonical: "knowledge.catonetworks.com/how-cato-uses-dhcp-to-identify-devices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How Cato Uses DHCP to Identify Devices

This article explains how Cato uses DHCP messages to identify and classify devices in your network, and how your DHCP deployment choice affects the device data shown on the Device Inventory page and available in firewall rules.

## Overview

The Device Inventory engine analyzes WANbound and outbound traffic to discover, identify, and classify the devices in your network. For more about the IoT/OT Security service and how to use Device Inventory in the Cato Management Application (CMA), see [What is Device Inventory?](https://knowledge.catonetworks.com/docs/what-is-device-inventory).

The engine uses various identifier protocols, including DHCP, HTTP, MAC, TCP/IP, and FTP. However, DHCP is the most valuable for obtaining device data. In a DHCP exchange, a device announces its own MAC address, often its host name, and hints about its operating system. This occurs on a predictable schedule, when the device joins the network or renews its lease. Cato uses this data to populate device attributes such as **MAC Address**, **Manufacturer**, **Device name**, and **Device IP**, which then become available as **Device Attribute** conditions in your firewall rules. For more about using device data in firewall rules, see [Adding Device Conditions to Firewall Rules](https://knowledge.catonetworks.com/docs/adding-device-conditions-to-firewall-rules).

For Cato to access DHCP data, Cato must be on the DHCP message path. When Cato is either the DHCP server or a DHCP relay for a network range, the Cato Cloud reads the DHCP messages it processes and feeds the extracted identifiers into the Device Inventory engine.
> **Note:**
>
> - Firewall rules that use **Device Attribute** conditions are enforced only for devices whose MAC address was detected. In practice, this means devices seen through DHCP. Cato recommends configuring your sites to use the Cato DHCP service to help ensure MAC address detection.
> - The MAC address stored in **Device Inventory** is taken from the DHCP message payload (`chaddr`), not from the Ethernet header of the frame. Intermediate DHCP relays, routers, and Sockets do not overwrite this value.

### How the DHCP Message Path Impacts Retrieval of Device Data

When a client on a site network range needs an IP address, it sends a DHCP `DISCOVER` message. What Cato sees when this happens depends on how DHCP is configured for that range:

- **Cato Cloud as the DHCP server** - When a range is configured in CMA with the **DHCP Range** setting, the Cato PoP is the DHCP server. Every `DISCOVER`, `REQUEST`, `RENEW`, and `RELEASE` from every client on the range is delivered to the PoP, which assigns the IP address and parses the payload. This mode produces the most complete and freshest device data.
- **Cato as a DHCP relay** - When a range is configured with the **DHCP Relay** setting, your DHCP server, for example a Microsoft DHCP server in a data center, assigns the leases. The Cato Socket relays the DHCP messages between the client and your server and reads the payload while it does so.
**Note:** Cato can also extract DHCP identifiers from DHCP relay messages that pass through the Cato Cloud, even when the Cato Socket is not the DHCP relay agent. This applies when the relay traffic is routed through Cato to reach the DHCP server.
- **DHCP served locally on the LAN** - A third-party DHCP server, such as a local router, a third-party access point, or a Windows Server, responds to clients on the same broadcast domain without Cato relaying. These DHCP messages never leave the LAN and Cato does not see them. Devices on this range may still appear in the Device Inventory through their WANbound traffic, but typically with limited data (no MAC address, manufacturer, or host name) and firewall rules with **Device Attribute** conditions do not apply to them.

For each DHCP message it processes, Cato extracts identifiers from the following fields and uses them to populate the device profile:

| DHCP Field | Device Inventory Attribute |
|---|---|
| Client hardware address (`chaddr`) | **MAC Address** — the anchor for the device record and the prerequisite for **Device Attribute** firewall rules. |
| MAC OUI (first 24 bits) | Initial **Manufacturer**, derived from the IEEE OUI registry. |
| Assigned or requested IP address | **Device IP**, and the IP-to-MAC binding used to attribute later traffic to the device. |
| Option 12 (Host Name) | **Device name**, when the client advertises one. |
| Option 55 (Parameter Request List) | Contributes to **OS** and **OS Version** identification. |
| Option 60 (Vendor Class Identifier) | Refines **Type**, **Manufacturer**, and **Model** for devices that advertise a vendor class, such as IoT and OT devices, printers, VoIP phones, and cameras. |

Cato combines these DHCP-derived attributes with signals from other protocols and from behavioral analysis of WANbound traffic to refine the classification.

## Configuring DHCP for Device Identification

To make sure the Device Inventory engine can identify devices at each site, configure DHCP so that Cato is on the DHCP message path for every network range you want to monitor. You can use one of two modes.

### Using Cato as Your DHCP Server (Recommended)

In this mode, the Cato Cloud assigns IP addresses to clients on the network range and reads every DHCP message directly.
> **Note:**
>
> Cato recommends this mode for both device identification coverage and operational simplicity. For more information, see [Recommendations for DHCP](https://knowledge.catonetworks.com/docs/recommendations-for-dhcp).
***
For more about using Cato as the DHCP server, see [Configuring DHCP Settings](https://knowledge.catonetworks.com/docs/configuring-dhcp-settings).

### Using Cato as a DHCP Relay

Use this mode when you want to keep your own DHCP server (for example, a centralized Microsoft DHCP server) but still let Cato see the DHCP messages.
For more about using Cato as a DHCP relay, see [Configuring Cato as the DHCP Relay](https://knowledge.catonetworks.com/docs/configuring-cato-as-the-dhcp-relay).

## Where DHCP-Based Device Data Appears

Cato uses DHCP-derived identifiers in the following CMA pages:

- **Device Inventory** - The **MAC Address**, **Manufacturer**, **Device name**, and **Device IP** columns are populated from the DHCP fields listed above. Open a device's **Quick View** to see the MAC address and the full attribute list. For more information, see [Using the Device Inventory Page](https://knowledge.catonetworks.com/docs/using-the-device-inventory-page).
- **WAN, Internet, and LAN firewall rulebases** — The values identified by the Device Inventory engine become selectable values in the **Device Attribute** condition of a rule. Rules with **Device Attribute** conditions apply only to devices whose MAC address was detected.

## Known Limitations

In addition to the limitations described in [Using the Device Inventory Page](https://knowledge.catonetworks.com/docs/using-the-device-inventory-page) (3-day aging, multi-ID split, shared-ID collision), DHCP-based identification has the following limitations:

- **Static-IP devices produce no DHCP signal.** A device with a static IP address does not send DHCP messages, so it has no MAC address in **Device Inventory** and is not matched by firewall rules that use **Device Attribute** conditions.
- **Locally served DHCP is invisible to Cato.** If DHCP is served by a device on the LAN that does not send its DHCP messages through the Cato Cloud (as server or as relay), Cato cannot extract device identity from those messages.
- **MAC randomization.** Modern operating systems (recent versions of iOS, Android, Windows 11, and macOS) can present a randomized MAC address per network. A randomized MAC address has an OUI that maps to no real manufacturer, and the same physical device may appear under different MAC addresses on different networks.
- **DHCP snooping or Option 82 rewriting.** If a device between the client and the Cato Socket modifies DHCP messages (for example, by adding Option 82 or rewriting `chaddr`), the identifiers stored in **Device Inventory** reflect that modification.

## Related Articles

- [What is Device Inventory?](https://knowledge.catonetworks.com/docs/what-is-device-inventory)
- [Using the Device Inventory Page](https://knowledge.catonetworks.com/docs/using-the-device-inventory-page)
- [Configuring DHCP Settings](https://knowledge.catonetworks.com/docs/configuring-dhcp-settings)
- [Configuring Cato as the DHCP Relay](https://knowledge.catonetworks.com/docs/configuring-cato-as-the-dhcp-relay)
- [Recommendations for DHCP](https://knowledge.catonetworks.com/docs/recommendations-for-dhcp)
- [Adding Device Conditions to Firewall Rules](https://knowledge.catonetworks.com/docs/adding-device-conditions-to-firewall-rules)
