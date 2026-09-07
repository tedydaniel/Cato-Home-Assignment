---
title: "How to Capture Traffic on a Socket"
slug: "how-to-capture-traffic-on-a-socket"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/how-to-capture-traffic-on-a-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Capture Traffic on a Socket

## Overview

Cato Networks provides a PCAP (Packet Capture) utility that is built-in into the Socket WebUI, so anyone with the login credentials can diagnose network issues.

For more about the Socket WebUI, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

## Using the Socket WebUI to Take a PCAP

This section is the following step by step explanation of how to use the Socket PCAP utility to analyze issues in your network.

**Note:** If you are connected directly to the LAN of the Socket, the management IP of the Socket can be used to access the WebUI internally as well.

1. Log in to the Socket WebUI from the Cato Management Application.
2. Start the PCAP.
3. Reproduce the problem.
4. Download the PCAP file.
5. Analyze the results in the file.

### Logging in to the Socket WebUI from the Cato Management Application

Admins with editor permissions can automatically log in to the Socket WebUI from the Cato Management Application.

**To log in to the Socket WebUI from the Cato Management Application:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the socket, select **Socket WebUI**.

The browser opens a new tab and logs in to the Socket WebUI.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247819075229.png) |
| --- |

The Socket WebUI automatically logs out when the window is idle for more than 10 minutes.

### Running a PCAP (Socket v17.0 and Higher)

Starting with Socket version 17.0, you can use the **Traffic Capture** tab in the Socket WebUI.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247800678173.png)

The **Traffic Capture** tab allows for advanced capturing traffic on multiple **Active** interfaces/tunnels/SDWAN tunnels simultaneously.

Simply select the relevant options for each interface and hit the **Start** button to begin packet capturing. The maximum time frame for a packet capture is 60 minutes, otherwise the capture times out and you can't download the file.

The advanced Traffic Capture includes the following options:

- **Side 1 subnet and port** - Filtering based on IP and port.
- **Side 2 subnet and port** - Filtering based on IP and port.
  - **Note:** Both Side 1 and Side 2 can be the source or destination. If needed, use the **Packet Syntax Rule** to filter for the source and destination IPs using the **srcip/dstip** fields with the correct operators. More on the syntax can be found below.
- **IP Protocol** - Filter protocol-specific packets:
  - '*' - No IP Protocol filtering
  - ICMP
  - TCP
  - UDP
- **MAC Address** - Filter based on a MAC address.
- **Packet Syntax Rule**

**Note:** The packet syntax is **not** based on Wireshark's capture filter syntax.
  - Allows filtering packets based on a configurable smart syntax rule.
  - **Show Possible Fields** This link opens up a JSON file containing all possible fields with their available operators that can be applied to this rule.

The file is attached to this article and you can download it for reference.
  - **Show Example** is a clickable example of how to use the syntax rule.
- **Limit Packet size (Bytes)** - Filter to set a limit to the packet size recorded.
- **File Suffix** - Allows adding a suffix to the end of the file.
  - If you choose to add a suffix, the file naming will be structured as follows: {site_name}.{account_name}.{time}.{**suffix**}.pcapng

After you **Start** recording packets, you may choose **Stop**, **Download** or **Download & Stop** to stop packet recording.

The PCAP utility saves the file to the download directory configured for your browser with this format: *<site_name>.<account_name>.<interface>.<timestame>.pcapng*

#### Interface Filtering

The downloaded PCAP file includes traffic recorded on multiple interfaces. In order to search for traffic recorded on a **specific** interface:

- Open the PCAP file, and under **Frame,** search for the '**interface id**':
- Right-click on the interface ID, select **Apply As Filter** and then click on **Selected**
  - **Note that each interface has two IDs, one for TX** (Transmit) **and one for RX** (Receive) **. In the following example, it can be seen that the filter is applied to the WAN1 TX side.**

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247780935581.png)
- It is also possible to filter manually by applying the filter below, while X represents the ID of the interface.

```plaintext
frame.interface_id == X
```

**Note:** If the Socket has LAN LAG configured, then the aggregation interface will appear in the list of interfaces.

### Running a PCAP (Socket v16.x and earlier)

Configure the PCAP settings for the specific interface to start the PCAP.

**Best Practice:** For troubleshooting most network issues we recommend that you to take a packet capture on the LAN interface. WAN packet captures can be useful if the Socket can't connect to a PoP, but once connected, all traffic over the WAN interface is **encrypted and encapsulated** in DTLS. It is difficult to analyze a PCAP with encrypted traffic.

**To start the PCAP:**

1. In the **Monitor** page, click the **PCAP** column. The column expands to show the PCAP options.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247819330589.png)
2. Enter the settings for the PCAP. You can select specific settings for Source, Destination and ports.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247834767261.png)

These optional settings limit the traffic that is captured, without them the PCAP can accumulate a lot of data in a short time.
3. To start the capture, select the checkbox in the PCAP column.

![pcap3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247801008285.png)

## Reproducing the Problem

While the PCAP utility is running, reproduce the network problem that you’re troubleshooting.

## Analyzing the Packets

We recommend that you use Wireshark or a similar program to open the capture file and analyze the packets. Wireshark is a free program for Windows, Mac, and Linux that can be downloaded from [https://www.wireshark.org/.](https://www.wireshark.org/.)

[catalog_socket_packet_fields.json](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/catalog_socket_packet_fields.json)
