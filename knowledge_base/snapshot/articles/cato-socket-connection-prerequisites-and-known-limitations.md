---
title: "Cato Socket Connection Prerequisites and Known Limitations"
slug: "cato-socket-connection-prerequisites-and-known-limitations"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/cato-socket-connection-prerequisites-and-known-limitations"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Socket Connection Prerequisites and Known Limitations

> [!NOTE]
> Note:
> 
> The Cato Cloud only supports IPv4 addresses.

This article describes the prerequisites for Sockets to connect to the Cato Cloud and known limitations for Sockets.

## Socket Connection Prerequisites

To securely connect and access resources on your private network behind the Cato Cloud, please ensure that your networking devices and firewalls meet these requirements:

- These ports are open on firewalls:
  - UDP port 53
  - UDP port 443
  - TCP port 443
- Devices can resolve these URLs:
  - vpn.catonetworks.net
  - cc2.us1.catonetworks.com
  - cc2.in1.catonetworks.com
  - cc2.jp1.catonetworks.com
  - cc2.catonetworks.com

**Note:** If this URL is unreachable, then use the actual IP address, see [CMA IP Allowlist](https://support.catonetworks.com/hc/en-us/articles/20511945810589-Source-IP-Address-for-the-Cato-Management-Application) (you must be logged in to the Cato Knowledge Base to view this article).
  - steering.catonetworks.com
  - For Sockets running firmware v11.x and earlier, they must be able to resolve these domains:
    - c-me.catonetworks.net
    - d-me.catonetworks.net
- TLS inspection and security checks are disabled for the Socket IP
- Sockets use ICMP packets for Last Mile Monitoring data
- NTP is used for time synchronization

## MTBF Specifications

These are the mean time between failures (MTBF) specifications for Sockets:

- X1500: 808,959 Hrs
- X1600: 143,940 Hrs
- X1700: 157,565 Hrs

The RMA for Sockets is less than 0.5%.

## Socket Known Limitations

### All Sockets

- For Sockets that use multiple WAN links, if there is a NAT device between the Socket and the PoP, then it’s possible that one or more of the WAN links can’t connect to the PoP. This can create connectivity issues, such as the HA status of the site is **Not Ready**.

The PoP uses the source port of each incoming DTLS connection to connect each WAN link to the same logical tunnel. The NAT device may change the source port and prevent a WAN link from connecting to the same logical tunnel as the other WAN links.
- When multiple Socket sites are connected to the same PoP location, sometimes you can't use the Socket WebUI to ping another Socket site connected to the same PoP.
- Starting Socket v25.0, when configuring NAT policy for a site, the socket LAN IP cannot be used as the Translated Source IP. **Note:​​** Starting with Socket v25.0.22177, there are legacy configurations that we continue to support using the Socket LAN IP as the Translated Source IP. However, this is only available for those legacy configurations.

#### Socket Ping Behavior

When testing connectivity with ping requests, Sockets only respond to specific IP addresses based on the source:

- From devices behind the Socket site: Ping replies are only received when targeting the gateway IP in the same subnet as the source device
- From remote users (via the Client): Ping replies are only received when targeting the local IP address of the native range
- For Azure vSockets in HA mode: The floating IP responds to all ping requests

### Socket X1600 and Socket X1600 LTE

- Devices with NIC model Intel® Ethernet Connection I219-LM can't connect directly to the Socket MGMT port using the NIC's default settings. This NIC is common in Dell and HP laptops.
  - Workarounds: There are two ways to connect to the Socket MGMT port with this NIC:
    - Connect directly by changing the NIC settings as follows:

**Note:** After configuring these settings, the NIC can connect directly to the Socket, however, the Socket will recognize the connection as 100 Mbps half-duplex and not full-duplex.
      - Set **Speed/Duplex** to **100 Full**
      - Set **Legacy Switch Compatibility** to **Enabled**
    - Connect through a third-party device, such as a switch. The device and Socket must be in the same subnet.
- X1600 LTE Sockets can't ping the **Local IP** address of the Native range of a different Socket site.
- X1600 LTE Sockets are not supported for sites located in China. Please contact your authorized Cato representative for more information.
- X1600 LTE Sockets do not currently support automatic failover between SIM cards. For information on performing a manual failover if necessary, see [LTE Connectivity Troubleshooting](/v1/docs/x1600-cellular-connectivity-troubleshooting#resolving-discovered-issues).
