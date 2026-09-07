---
title: "Cato SDP Client Performance Troubleshooting"
slug: "cato-sdp-client-performance-troubleshooting"
updated: 2026-08-06T20:58:22Z
published: 2026-08-06T20:58:22Z
canonical: "knowledge.catonetworks.com/cato-sdp-client-performance-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato SDP Client Performance Troubleshooting

## Overview

Users may experience performance issues while using the Cato SDP Client. This article outlines essential troubleshooting steps to help identify and resolve such issues effectively.

## Possible Causes

Several factors can contribute to degraded performance, making it important to perform initial diagnostics before identifying a root cause. Common contributors include:

- Local network misconfiguration
- ISP-related bandwidth or routing issues
- Instability or latency with the connected PoP
- Unintended connection to a geographically distant PoP
- High system resource usage or third-party software interference

## Troubleshooting

An SDP client depends on the speed of the user's local connection to the Internet. Whatever the speed of the connection is, the SDP client cannot be faster.

Depending on the region, Cato Client connections may have a maximum throughput. See [Supported Throughput for Cato SDP Clients](https://support.catonetworks.com/hc/en-us/articles/360001054077-Supported-Throughput-for-Cato-VPN-Clients).

The following steps are recommended to isolate and resolve performance issues with the Cato SDP Client:

### 1. Compare Performance On and Off Cato

Start by determining if the issue lies with the general internet connection or the SDP tunnel:

1. Run a Speed Test While Connected to Cato:
  - Use a web speed test tool, preferably Ookla. It's **highly recommended** that you download the [Ookla Speed Test Application](https://www.speedtest.net/apps) instead of using the browser, as browsers can be limited by process CPU and efficiency mode.
  - Make sure the device is plugged into a power source (not running on battery).
  - Configure a network rule (at the top of the ruleset) for the **speed test** website with a high [bandwidth priority](/v1/docs/configuring-bandwidth-management-profiles). Ensure TCP acceleration is disabled.
  - Run the **speed test** and note the results.
2. Run a Speed Test While Disconnected from Cato:
  - Disconnect from the SDP Client. If the user is configured with Always-On, the administrator can configure a 15-minute [bypass code via CMA](/v1/docs/protecting-users-with-always-on-security).
  - Run a **speed test** once again to determine the Internet speed. Ensure that the speed test is run against the same server as in the previous step.
3. Run a Speed Test In Split Tunnel While Connected to Cato:
  - Configure [Split Tunnel](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) to route traffic from the affected application out of the tunnel.
  - Run a **speed test** once again to determine the Internet speed. Ensure that the speed test is run against the same server as in the previous step.
4. Interpret the Results:
  - If the SpeedTest results without Cato Client are bad, try restarting the Internet modem or switching to a different network, such as a mobile hotspot or an ethernet connection.
  - If the SpeedTest results are poor only with Cato, continue with the next steps below.

> [!NOTE]
> Note:
> 
> Speedtest can run either in multi-connection or single-connection mode. File transfers, like SMB, use a single connection. Hence, you'll probably need to run the speed test with a single connection to get accurate results when troubleshooting bad file transfer performance.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12338417750557.png)

### 2. Check Network Analytics

While the SDP Client is connected to Cato, use the [Network Analytics page](/v1/docs/showing-the-site-network-analytics) in the CMA to review:

- Distance to the connected PoP
- Packet loss levels

High distance or packet loss often indicates underlying ISP issues or suboptimal routing, both of which can significantly degrade performance.

### 3. Verify Connected PoP

While connected to the SDP Client, check which [PoP location](/v1/docs/production-pop-guide) you are connected to by navigating to the Stats section in the Client.

The Name of the PoP indicates its geographic location. For example:

- **montcatodxx** indicates the Montreal PoP
- **nycatodxx** would indicate New York, and so on.

Ensuring the client is connected to the nearest PoP can improve performance. Unexpected connection to a distant PoP may result in higher latency and reduced throughput and should be reported to Cato Support.

### 4. Disable Third-Party Solutions

Temporarily disable any antivirus, firewall, or endpoint security tools. These solutions may inspect or throttle encrypted traffic, which can adversely affect SDP performance. This step helps isolate security software as a potential bottleneck.

### 5. Remove conflicting OEM software (bloatware):

OEM utilities on Windows devices, such as Intel Connectivity Performance Suite, Lenovo Vantage Service, and Dell Optimizer, have been observed to interfere with SDP traffic processing.

- Review the `sc.log` file from the Windows Client log bundle for services:
  - `Intel Connectivity Network Service` or `Intel Dynamic Bandwidth Management`
  - `LenovoVantageService`
  - `Dell Optimizer`
- Uninstall identified interfering software using official vendor methods.
  - Intel Connectivity Performance Suite - [Uninstall instructions](https://www.intel.com/content/www/us/en/support/articles/000093451/wireless/wireless-software.html#primary-content).
  - Dell Optimizer - [Uninstall instructions](https://www.dell.com/support/manuals/en-ca/dell-optimizer/dell-optimizer-4.1.3_ug/uninstall-dell-optimizer?guid=guid-2d2a223a-e547-42ca-a9b5-f453dc1b3bb1&amp;lang=en-us).
- Advise the customer to document post-uninstall performance for Support records.
- If a rollback is needed, consult the vendor's documentation for reinstallation instructions.

### 6. Monitor Local System Resource Usage

High CPU or memory usage can affect Client performance.

- Check Task Manager or relevant system monitoring tools to identify any heavy resource usage.
- Pay attention while running speed tests or replicating the issue.
- Consider adjusting the priority of the `winvpnclient.cli.exe` process manually or via registry key, as explained in [Windows SDP Client Hangs Due To High CPU Utilization](/v1/docs/windows-sdp-client-hangs-due-to-high-cpu-utilization)

### 7. Check the Wireless Connection

If connecting via Wi-Fi, check for poor signal strength and potential interference:

- Check the wireless signal strength. Windows users can run the command ***netsh wlan show interfaces*** to display wireless parameters.
- Run a continuous ping to the default gateway to detect packet loss, jitter, or high latency.
- If possible, switch to a wired connection to rule out interference or weak signals.

### 8. Switch the DTLS Port

By default, the Cato SDP Client uses DTLS over **UDP/443** to connect to Cato. If it fails to connect, it will attempt to use DTLS over **UDP/1337** and, as a last resort, TLS over **TCP/443**.

Due to the nature of TCP and UDP, the Cato Client generally provides better performance when using UDP. In the Client UI’s Stats page, the "Type" field allows you to identify whether the client is using UDP or TCP.

If the default UDP port is **blocked** or **experiences performance issues** caused by a local firewall or ISP, you can [configure a different UDP port](/v1/docs/configuring-a-different-udp-port-for-the-cato-client) to manually switch to **UDP/1337** and bypass any imposed limitations on port **UDP/443**.

### 9. Verify DNS Configuration

For optimal performance, the SDP Client's DNS server should be:

- The default Cato DNS Server (recommended)
- Located in the same country as the SDP Client.

Distant DNS servers can harm performance due to slow response to DNS queries and might provide a server IP that isn't in the SDP client region. For more information, see [Improving Network Performance for Internal DNS Servers](/v1/docs/best-practices-for-dns-and-your-cato-account)

- For internal DNS server IPs, use [the CMA routing table](/v1/docs/showing-the-routing-table-for-your-account) to identify their location.
- For public DNS server IPs, use [ip2location.](https://www.ip2location.com/)

### 10. Use Experience Monitoring (Optional)

For customers with an [Experience Monitoring](/v1/docs/experience-monitoring-connection-details) license, we recommend reviewing the specific user performance under the Remote Users or Office Users tab. Look for indicators that may impact connectivity and overall performance:

- High CPU or memory usage
- Weak Wi-Fi signal
- Packet loss or jitter.
- High latency to the user gateway.

## Raising Cases to Cato Support

Submit a Support ticket with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the experienced issue and overall impact on users.
- Speedtest results with the Client connected and disconnected from Cato.
- Timestamps of when the issue occurred. If possible, collect a screen recording that includes timestamps.
- [Record the issue](/v1/docs/recording-issues-using-the-cato-client) while replicating poor performance and upload the logs to Cato Support. Include the reference ID in the Support ticket.
- Run a PCAP capture on both the physical and the Cato adapter using [Wireshark](https://wiki.wireshark.org/CaptureSetup) while replicating the problem. Include the PCAP file in the ticket.
