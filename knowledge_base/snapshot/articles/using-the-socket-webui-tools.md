---
title: "Using the Socket WebUI Tools"
slug: "using-the-socket-webui-tools"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/using-the-socket-webui-tools"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Socket WebUI Tools

## Overview of Troubleshooting Tools

The Socket WebUI has network tools in the **Tools** and **HW Status** tabs that you can use to troubleshoot the Socket links including:

- Ping
- Traceroute
- Speedtest
- iPerf
- CPU Utilization

For more information about the Socket WebUI, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

## Logging in to the Socket WebUI from the Cato Management Application

Admins with editor permissions can automatically log in to the Socket WebUI from the Cato Management Application.

**To log in to the Socket WebUI from the Cato Management Application:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the socket, select **Socket WebUI**.

The browser opens a new tab and logs in to the Socket WebUI.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248020098205.png) |
| --- |

The Socket WebUI automatically logs out when the window is idle for more than 10 minutes.

## Using the Network Tools

After you log in to the Socket WebUI, select one of the network tools from the **Tools** tab.

> [!NOTE]
> Note:
> 
> The **Force Recovery via Internet Bypass** feature can impact the service for the Socket, use it with caution.

**To show the network tools:**

- From the menu bar, click **Tools**. The Socket WebUI shows the **Network Tools** section.

![Tools_Tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248026937245.png)

### Using the Ping Tool

Choose the Socket link and enter the hostname or IP address that you are pinging.

These are the types of Socket links that you can use as the egress interface:

- LAN - The packets are sent using the internal LAN network for the site.
- ALT WAN - The packets are sent using the Alt. WAN tunnel over the MPLS network.
- WAN via Cato - The packets are sent using a tunnel over the Cato Cloud.
- WAN <ISP> directly - The packets are sent using a tunnel over the Internet directly to the ISP. The Cato Cloud is bypassed.

**​​Note:​​** The ping tool resolves domains using Google Public DNS directly through the Socket WAN interface, which can impact the physical location of the server IP address used for the test.

**To ping the destination from a Socket link:**

1. From the **Network Tools** section, click the **Ping** tab.

![Ping.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248004057757.png)
2. In **Route via**, select the link that is sending the packets.
3. Enter the **Hostname/IP** that is the destination you are pinging.
4. (Optional) Enter the number of packets to send in the **Count** field. You can enter any value between 1-100. If you don't enter any value, the default value of 10 is applied.
5. (Optional) Set the **Interval** for how often each packet is sent. If you don't enter any value, the default value of 1 second is applied.
6. Click **Run**.

> [!NOTE]
> Note:
> 
> The value of **Count** * **Interval** cannot exceed 120. For example, if you set the **Count** to 50 packets, the **Interval** can't be more than 2 seconds.

The window shows the results of the ping test.

### Using the Traceroute Tool

Traceroute is used to identify the routers (hops) between a source and destination. Traceroute works by first sending a packet to the destination IP with a time-to-live (TTL) value of 1. When the packet hits the first router in the path, the router decrements the TTL by 1. Since the new TTL is 0, the router drops the packet and responds with an ICMP time-to-live exceeded message sourced from its own IP address. Traceroute now has the IP address of the first router in the path, so it sends out another packet with the TTL value of 2 (the original TTL incremented by 1), and the second router in the path responds with a TTL exceeded message.

This process is repeated until the traceroute reaches the destination IP address. There is a timer of 60 seconds to complete the traceroute and a maximum of 20 hops.

Choose the Socket link that you are using to run the traceroute and enter the destination hostname or IP address.

These are the types of Socket links that you can run traceroute:

- LAN - The packets are sent using the internal LAN network for the site.
- ALT WAN - The packets are sent using the Alt. WAN tunnel over the MPLS network.
- WAN via Cato - The packets are sent using a tunnel over the Cato Cloud.
- WAN <ISP> directly - The packets are sent using a tunnel over the Internet directly to the ISP. The Cato Cloud is bypassed.

**To run traceroute from a Socket link:**

1. From the **Network Tools** section, click the **Traceroute** tab.

![Traceroute.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248020353437.png)
2. In **Route via**, select the link that is sending the packet.
3. Enter the **Hostname/IP** that is the destination for the traceroute.
4. (Optional) Enter the number of packets to send in the **Count** field. You can enter any value between 1-200. If you don't enter any value, the default value of 5 is applied.
5. (Optional) Set the for how often each packet is sent. If you don't enter any value, the default value of 1 second is applied.
6. Click **Run**.

> [!NOTE]
> Note:
> 
> The value of **Count** * **Interval** cannot exceed 200. For example, if you set the **Count** to 25 packets, the **Interval** can't be more than 8 seconds.

The window shows the results of the traceroute test.

### Using the Speedtest Tool

The Socket WebUI lets you use the Speedtest client that is installed on the Socket to troubleshoot the network performance of the Socket links. The Speedtest tool can be used with a randomly chosen Speedtest server in the public Internet, or with the server running directly on the connected PoP in the Cato Cloud.

These are the types of Socket links that you can run the Speedtest:

- WAN via Cato - The packets are sent using a tunnel over the Cato Cloud.
- WAN <ISP> directly - The packets are sent using a tunnel over the Internet directly to the ISP. The Cato Cloud is bypassed.

**Note:** When the **Server** is set to **Internet**, The Speedtest tool is not supported for the Paris and Marseille PoP locations.

**Best Practices for Accurate Speedtest**

The same Socket CPU is responsible for generating the traffic for the Speedtest and sending the site traffic. These are the recommended link network speeds for accurate Speedtest results:

- X1500 Socket results are accurate for link speeds up to 300 Mbps
- X1700 Socket results are accurate for link speeds up to 2000 Mbps
- Virtual Socket (vSocket) - the accuracy depends on the VM and cloud platform specifications

For the most accurate results, run the Speedtest tool when there is minimal traffic over the link. Other traffic has higher QoS priority than the Speedtest traffic.

**To run Speedtest for a Socket link:**

1. From the **Network Tools** section, click the **Speedtest** tab.

![Speedtest.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248004209181.png)
2. In **Server**, select the server that is running the Speedtest:
  - **Cato Connected PoP** - the Speedtest client is hosted on a PoP in the Cato Cloud
  - **Internet** - the Speedtest client is hosted on a random server in the public Internet
3. In **Route via**, select the WAN link that is sending the traffic for the Speedtest.
4. Click **Run**.

The window shows the results of the Speedtest.

### Using the iPerf Tool

The Socket WebUI lets you use the iPerf tool to troubleshoot last mile performance issues between the Socket and the connected PoP in the Cato Cloud. The Socket that is running the iPerf client performs the test against the iPerf server that is running on the connected PoP. Use the **Direction** option to test the upstream or downstream connectivity performance for a WAN link.

These are the types of Socket links that you can run the iPerf tests:

- WAN via Cato - The packets are sent using a tunnel over the Cato Cloud.
- WAN <ISP> directly - The packets are sent using a tunnel over the Internet directly to the ISP. The Cato Cloud is bypassed.

You can also select TCP or UDP traffic, and the amount of time (seconds) in between each data stream.

For best results, we recommend that you run the iPerf test from a host that is connected to the LAN.

**Known Limitations for iPerf**

The same Socket CPU is responsible for generating the traffic for the iPerf test and sending the site traffic. These are the recommended link network speeds for accurate iPerf results:

- X1500 Socket results are accurate for link speeds up to 300 Mbps

**Note:** iPerf results for X1500 Sockets running version 19.x are accurate for link speeds up to 100 Mbps
- X1700 Socket results are accurate for link speeds up to 2000 Mbps
- Virtual Socket (vSocket) - the accuracy depends on the VM and cloud platform specifications

For the most accurate results, run the iPerf tool when there is minimal traffic over the link. Other traffic has higher QoS priority than the iPerf traffic.

**To run an iPerf test for a Socket link:**

1. From the **Network Tools** section, click the **iPerf** tab.

![iPerf.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248010434333.png)
2. The option for **Server** is **Cato Connected PoP**, the iPerf tool is hosted on a PoP in the Cato Cloud.
3. In **Route via**, select the WAN link that you are using to run iPerf.
4. Select the **Protocol** for the iPerf test, **TCP** or **UDP**.
5. Set the **Direction** of the test traffic, and the **Measurement Interval** between data streams.
6. For TCP protocol, select if this test uses **Parallel flows**.
7. For UDP protocol, enter the **Target rate** (bandwidth) for the UDP traffic.
8. Click **Run**.

The window shows the results of the iPerf test.

## Showing the Socket CPU Usage

The HW Status page shows real-time information about your Socket CPU utilization. You can use this page to monitor CPU changes while troubleshooting the Socket.

The CPU utilization is supported on Socket version 19.0 and higher.

![WebUI_HW_Status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248020609309.png)

**To show the Socket CPU Usage:**

- From the menu bar, click the **HW Status** tab.
