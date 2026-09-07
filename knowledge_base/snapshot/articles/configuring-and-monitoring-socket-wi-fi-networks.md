---
title: "Configuring and Monitoring Socket Wi-Fi Networks"
slug: "configuring-and-monitoring-socket-wi-fi-networks"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/configuring-and-monitoring-socket-wi-fi-networks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring and Monitoring Socket Wi-Fi Networks

This article explains how to configure Wi-Fi networks on supported Sockets and review analytics for the networks.

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

The X1600 and X1600 5G Socket models include an optional integrated Wi-Fi capability that lets you deliver secure wireless access directly from the Socket. By combining SD-WAN, security, and enterprise-grade Wi-Fi in a single device, you can reduce hardware footprint at the site, simplify deployment, and centrally enforce consistent network and security policies for both wired and wireless users.

Integrated Wi-Fi extends the Cato SASE platform to the wireless edge. Wireless traffic is inspected by the same security engines as wired traffic, including Firewall, IPS, Anti-Malware, and additional security services enabled in your account. This ensures consistent policy enforcement, full visibility, and simplified segmentation for corporate, guest, and IoT networks without requiring a separate wireless controller or firewall appliance.

Because Wi-Fi is managed directly from the Cato Management Application (CMA), you can configure SSIDs, authentication methods, encryption standards, and network segmentation for multiple sites from a single console. This centralized management model helps you maintain uniform security standards, streamline site rollouts, and reduce operational overhead.

### HA Configurations for Socket Wi-Fi Networks

These are the supported configurations to provide HA including Wi-Fi connectivity:

- 2 X1600 Sockets with integrated Wi-Fi
- 2 X1600 5G Sockets with integrated Wi-Fi

HA is not supported (for either wired or Wi-Fi connectivity) in a site with one X1600 Socket and one X1600 5G Socket. A site with 2 X1600 Sockets (or 2 X1600 5G Sockets), one with integrated Wi-Fi and one without, supports HA for wired connectivity but not for Wi-Fi.

## Configuring Socket Wi-Fi Networks

For sites with connection type X1600 or X1600 Cellular, with Socket models with integrated Wi-Fi, you can configure up to four Wi-Fi networks.

**To configure a Socket Wi-Fi network**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. In the ports table, under **Default Ports**, click one of the Wi-Fi interfaces (labelled WBR1-WBR4). The **Edit SSID** panel opens.

![Wif_Ports_table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310571523101.png)
4. In the **General** section, enter a name for the network and move the toggle to **Enabled**.

![Wifi_Edit_SSID_panel_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310574042781.png)
5. In the **SSID Setup** section, select whether the SSID name is **Hidden** or **Visible** to users.
6. In the **Network** section:

![Wifi_Edit_SSID_Panel_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310591760285.png)
  - Enter the **Subnet IP** range for the network.
  - Enter the **Local IP** address for the interface.
  - Under **DHCP**:

The DHCP lease time follows the global account setting for DHCP lease time. For more information on setting account DHCP lease time, see [Configuring DHCP Settings](/v1/docs/configuring-dhcp-settings).
    - Enable or disable DHCP for wireless clients on this SSID.
    - When DHCP is enabled, enter the IP **Range** that defines the pool of addresses assigned to clients.
7. In the **Security** section:

![Wifi_Edit_SSID_Panel_Security.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310574082205.png)
  - Select the **Authentication Mode** for the SSID:
    - **PSK** - Users authenticate with a shared password
    - **Open** – Users connect without authentication
  - In **Password**, enter the pre-shared key when PSK is selected.

Click **Generate Strong Password** to automatically create a secure password.
  - Under **Security Protocol**, select the encryption standard.
  - Under **Track**, select **Track authentication events** to generate events for wireless authentication activity.
8. In the **Radio** section, select the **Broadcast Bands** for this SSID. You can enable one or both bands.

## Monitoring Socket Wi-Fi Networks

You can monitor Socket Wi-Fi networks at the interface, SSID, device, and traffic levels from multiple pages in the CMA. This gives you operational visibility into radio status, connected clients, IP assignment, and throughput per Wi-Fi interface.

### Viewing Socket Wi-Fi Network Status

The Networks page provides an overview of the Socket Wi-Fi networks including configured SSIDs and connected devices.

![Wifi_Networks_page.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310582537757.png)

These are the fields shown for each interface:

- **Port** - The identifier for the interface
- **SSID** - The configured name of the Wi-Fi network
- **Status** - Shows whether the SSID is enabled on the interface
- **Connected Devices** - the number of devices connected on each band
- **Network Range** - The configured subnet for the SSID
- **Visibility** - Shows whether users can see the SSID name
- **Auth Mode** - Shows whether users authenticate with a password or connect without authentication
- **Bands** - Shows the broadcast bands configured for the SSID

### Viewing Wi-Fi Interface Status

The Snapshot page shows operational status for the Socket Wi-Fi interfaces. In the **Link State** section, the Wi-Fi interfaces are listed as WBR1 – WBR4.

![Wifi_Snapshot_page.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310562477853.png)

These are the fields shown for each interface:

- **Status** - shows if the link is **Up** or **Down**
- **Media Connected** - Always shows **Yes** for Wi-Fi interfaces as no cable connection is required.
- **Link Speed** - Auto-negotiation, or the maximum speed configured for the link in the Socket WebUI
- **Duplex** - Auto-negotiation, or the duplex configured for the link in the Socket WebUI

### Viewing Connected Wi-Fi Hosts

The Known Hosts page provides device-level visibility for Wi-Fi clients.

![Wifi_Known_Hosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310562515229.png)

These are the fields shown for each host connected to a Wi-Fi network:

- **IP Address**
- **MAC Address**
- **DHCP Range**
- **Network Range**
- **IP Allocation** - Shows how the IP address was allocated to the host:
  - **Dynamic** - hosts with a dynamic IP address allocated by the Cato DHCP server
  - **Reserved** - hosts with a static IP address allocated by the Cato DHCP server
    - Reserved hosts are defined in the Hosts screen for the site (Network > Sites > {site name} > Site Configuration > Static Host Reservations)
  - **N/A** - Hosts that are sending traffic, but the IP address was not allocated by the Cato DHCP server
- **Last Host Activity** - Amount of time that elapsed since this host had network activity
- **Lease Time** - Duration for the DHCP lease

For hosts with **Reserved** IP Allocation, the Lease Time value is **Permanent**.
- **Expires In** - Amount of time remaining for the DHCP lease for this host

For hosts with **Reserved** IP Allocation, the Expires In value is **Never**.
- **Radio** - Shows the broadcast band for the Wi-Fi network the host is connected to
- **SSID**

### Monitoring Wi-Fi Traffic and Throughput

You can analyze Wi-Fi interface traffic from the Network Analytics page.

![Wifi_Network_Analytics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310571766685.png)

In the **Avg. Throughput by Port** widget, select a Wi-Fi interface (for example, WBR1) to view:

- Transmit (Tx) utilization
- Receive (Rx) utilization

This view helps you monitor wireless usage, identify peak utilization periods, and validate throughput on specific Wi-Fi interfaces.
