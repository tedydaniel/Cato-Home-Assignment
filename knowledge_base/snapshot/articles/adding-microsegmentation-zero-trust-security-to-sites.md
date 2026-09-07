---
title: "Adding Microsegmentation Zero-Trust Security to Sites"
slug: "adding-microsegmentation-zero-trust-security-to-sites"
updated: 2026-08-31T08:29:31Z
published: 2026-08-31T08:29:31Z
canonical: "knowledge.catonetworks.com/adding-microsegmentation-zero-trust-security-to-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Microsegmentation Zero-Trust Security to Sites

## Overview

Microsegmentation (host‐level segmentation) secures traffic within the same broadcast domain (e.g., a VLAN) by adding access control for lateral movement between hosts. Traditional network firewalls often operate at Layer 3, where they don’t always inspect or block intra-VLAN (Layer 2) traffic.

When you enable microsegmentation for a Socket site in Cato, the subnet mask of the range is broken into multiple /32 addresses. All host‐to‐host traffic in that VLAN is forced to be sent to the default gateway (Socket), where the relevant Cato firewall engine evaluates the traffic before it reaches the destination host. This forces "east‐west" traffic between hosts that share a VLAN to pass through the firewall for inspection and policy enforcement.

We recommend that you use the [Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall) for microsegmentation to provide the optimal on-prem security for the devices.

### Why You Need It

- Reduce risk by preventing unauthorized traffic between hosts in the same LAN
- Gain visibility into Layer 2 traffic so that all host‐to‐host communication is subject to your zero-trust policies
- Simplify segmentation - instead of creating numerous VLANs, you can apply policy rules at the host level

### Microsegmentation and DHCP Configuration

Microsegmentation relies on DHCP to enforce host-level isolation by assigning each device a /32 address and forcing all east-west traffic through the Socket for policy evaluation. You can enable microsegmentation using either Cato as the DHCP server or a third-party DHCP server that is integrated through Cato’s DHCP relay.

These are descriptions of the DHCP configuration options for microsegmentation:

- **Cato as the DHCP server** - Cato assigns IP addresses directly to hosts in the network range. When microsegmentation is enabled, Cato automatically applies /32 addressing to each DHCP allocation and enforces east-west inspection through the Socket.
- **Third-party DHCP server using DHCP relay** - Enables microsegmentation for network ranges that use an external DHCP server, with Cato configured as a DHCP relay. In this configuration, the external server assigns the IP address, and Cato transparently enforces the same /32 host routing and east-west traffic inspection as with Cato-managed DHCP. This lets you apply zero-trust segmentation without changing your existing DHCP infrastructure.

> [!NOTE]
> Note:
> 
> Microsegmentation support for DHCP relay requires a physical Socket site running Socket version 24.0.21570 or higher.

### License

Microsegmentation requires an Assets Security license.

### Prerequisites

- Physical Sockets with Socket v22.x or higher
- Supported for the Native range and VLAN network ranges
- Based on your security requirements, configure the LAN or WAN Firewall policy to allow the relevant traffic for the devices covered by microsegmentation

### Verified OS for Microsegmentation

The following operating systems are verified by Cato to support microsegmentation. Before applying microsegmentation for devices using a different OS, we recommend that you check that the OS functions correctly in your environment.

- Android Samsung Galaxy A24 SM-A245F/DSN
- BusyBox DHCP Client (based on Linux 18.04.6 LTS Ubuntu Debian OS)
- iOS 18.3.1
- Linux 18.04.6 LTS Ubuntu Debian (Bionic Beaver)
- macOS Apple M4 Pro 15.3.2 (24D81)
- Printer HP LaserJet Pro MFP M428fdn
- Printer Brother Model MFC-L2700DW
- Windows 11
- Windows 10 ESX VM: Windows 10 Enterprise, 22H2 19045.5608 (64-bit operating system, x64-based processor)
- Windows Server 2022 ESX VM Datacenter, AMD EPYC 7413 24-Core Processor 2.65 GHz (64-bit operating system, x64-based processor)
- Windows Server 2019 ESX VM standard AMD EPYC 7413 24-Core Processor 2.65 GHz (64-bit operating system, x64-based processor)
- Yealink IP Phone SIP-T23G & SIP-T40G

## Recommendations for Deploying Microsegmentation

Deploying microsegmentation can potentially disrupt legitimate traffic while you are ensuring precise enforcement of security policies that limit lateral movement within the network. Follow these recommendations to successfully deploy microsegmentation in your network.

1. Gradually enable microsegmentation in your account, starting with a single range.
2. Since microsegmentation only takes effect after the current DHCP lease time ends, and the devices request a new DHCP IP, you should:
  1. Override the account settings for the [DHCP lease time](/v1/docs/configuring-dhcp-settings) and reduce the DHCP Lease time for the network range, the minimum value is 1 minute.
  2. When you are enabling microsegmentation for the entire account, temporarily reduce the account-level DHCP lease time. After you confirm that microsegmentation is functioning correctly, you can change the DHCP lease time back to the previous setting.

**Note:** The default DHCP lease time is 72 hours (3 days).
3. Monitor the impact on devices in the network range:
  1. Verify that the devices can communicate with the allowed entities in your account based on the firewall policy.
  2. Verify that the devices have full connectivity to Internet resources.

Microsegmentation is for east-west Intra-VLAN traffic, and there should be no impact on Internet traffic
4. Avoid asymmetric routing to ensure that intra-VLAN traffic is routed through the Socket in a symmetric way. We recommend that the devices protected by microsegmentation use Cato as the DHCP server.

For example, a printer with a static IP that is accidentally not configured with the Cato /32 assigned subnet mask will not be able to communicate with other devices behind the site.

## Enabling Microsegmentation for a Network Range

Configure the new or existing network ranges for microsegmentation. This configuration imposes an automatic /32 subnet mask assignment for each host in the site. Then review the Socket LAN or WAN Firewall policy to confirm that the segmented traffic is allowed.

![DHCP_Microsegmentation.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35974447113629.png)

**To enable microsegmentation for a network range behind a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. Click **New**, or in the **DHCP Settings** column, click the network range.

The IP Range panel opens.
4. Set the network **Type** to the supported range.
5. Enter the other network range settings, such as: **VLAN**, **Subnet**, etc...
6. Define the DHCP configuration:
  - To use Cato as the DHCP server:
    - Set **DHCP Type** to **DHCP Range** and enter the IP address range for hosts in this **DHCP Range**.
  - To configure a third-party DHCP server using DHCP relay:
    1. Set **DHCP Type** to **DHCP Relay**.
    2. In **DHCP Relay Group**, select the DHCP Relay group for this network.

For more about DHCP Relay Groups and configuring Cato as the DHCP relay, see [Configuring Cato as the DHCP Relay](/v1/docs/configuring-cato-as-the-dhcp-relay).
7. Select **DHCP Based Microsegmentation**.
8. Click **Apply**, and then click **Save**.

## Recommendations for Rolling Back Microsegmentation

If you need to roll back and undo microsegmentation that has been deployed in your network, follow these recommendations to minimize the impact on your network.

1. Gradually disable microsegmentation in your account, starting with a single range.
2. Since disabling microsegmentation only takes effect after the current DHCP lease time ends, and the devices request a new DHCP IP, you should:
  1. Override the account settings for the [DHCP lease time](/v1/docs/configuring-dhcp-settings) and reduce the DHCP Lease time for the network range, the minimum value is 1 minute.
  2. When you are disabling microsegmentation for the entire account, temporarily reduce the account-level DHCP lease time. After you confirm that microsegmentation is functioning correctly, you can change the DHCP lease time back to the previous setting.

**Note:** The default DHCP lease time is 72 hours (3 days).

## Known Limitations

- For Linux-based systems, enabling micro-segmentation does not create a route entry for the default gateway when there are already two default routes connected to two routers.

For more information about a workaround, see this [article](/v1/docs/traffic-fails-to-reach-socket-when-micro-segmentation-enabled-linux-hosts).
