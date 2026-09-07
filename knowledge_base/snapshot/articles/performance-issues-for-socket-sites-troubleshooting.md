---
title: "Performance Issues for Socket Sites Troubleshooting"
slug: "performance-issues-for-socket-sites-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/performance-issues-for-socket-sites-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance Issues for Socket Sites Troubleshooting

## Overview

Customers may experience performance issues with their applications while connected to Cato. Performance issues are a broad topic, and they can occur across different OSI layers, spanning from the physical layer to the application layer. This playbook will primarily focus on performance issues up to the TCP layer. Performance issues related to applicative layers will be discussed in other playbooks:

- For reachability issues to Internet Resources, refer to [Internet Service Reachability Troubleshooting](/v1/docs/internet-service-reachability-troubleshooting)
- For performance issues related to Slow Internet Browser refer to [Troubleshooting Long Webpage Loading Time and Rendering Problems](/v1/docs/troubleshooting-long-webpage-loading-time-and-rendering-problems)
- For issues related to accessing Internal Resources, refer to [Access to Internal Resources Troubleshooting](/v1/docs/access-to-internal-resources-troubleshooting)
- For VoIP and Video related issues, refer to [VoIP Troubleshooting](/v1/docs/voip-troubleshooting)

## Symptoms

- Slow file transfer, reduced throughput
  - When connected to Cato Cloud, customers may experience sluggish download and upload speeds.
- Delayed response times in applications
  - This could be more evident in interactive applications like remote desktops.

## Possible Causes

- Misconfiguration (Qos, License, TCP Acceleration, Window Scaling)
- Network Congestion
- Packet Loss (ISP, last mile)
- Non Optimal PoP
- High Socket CPU
- Added Cloud Latency
- Hardware Limitations

## Troubleshooting the Issue

Before you go into more troubleshooting, isolating if this is related to Cato Cloud is essential. To do that, we can bypass the connection to Cato and verify if the issue is present. [Bypassing-the-Cato-Cloud](/v1/docs/bypassing-the-cato-cloud-site-level-policy) provides detailed steps on how to achieve that.

If the issue persists despite bypassing the connection, it indicates that Cato does not cause the problem. However, if the issue is resolved after bypassing the connection to Cato Cloud, then follow the following steps below for further troubleshooting and isolation.

### Licensing and Bandwidth Configuration

**Note:** The WAN bandwidth allocation is based on the site license and bandwidth configuration of the interface. If both have different values, the lower one will be applied to the WAN link.

- Validate that the allocated license for the site is correct. Go to Network > Sites > Site Configurations > General ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18227822402461.png)
- Validate that the configured Bandwidth of the WAN interface is correct. Go to Network > Sites > Site Configurations > Socket > Edit the WAN interface.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20402462802589.png)
- For China and Vietnam sites, the licensing is different. The license will be split into Global and Regional licenses. The Global license is for connections to global sites while the regional license is for connections within the Country.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18227837240733.png)
- For more information about managing site licenses, refer to [Managing-Site-Bandwidth-Licenses](/v1/docs/managing-site-bandwidth-in-licenses).

### Packet Loss

Packet loss can occur within the Cato infrastructure or with the Internet Service Provider (ISP). The following steps aim to isolate the source of the packet loss.

- Check for packet loss (upstream/downstream) in Network Analytics. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17677367894429.png)
- If this coincides with last-mile packet loss, it indicates a potential hardware issue with the cable connecting to the WAN port of the Socket or a problem with the Internet Service Provider (ISP). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17677383572509.png)
- Refer to the [Resolving Packet Loss](/v1/docs/performance-issues-for-socket-sites-troubleshooting#resolving-packet-loss) section for suggestions on resolving packet loss issues.

### Packet Discards (Bandwidth Management)

If you see many packet discards on the Network Analytics page, packets are discarded due to bandwidth management (QoS). To determine if your application is affected by this:

- Navigate to *Network > Priority Analyzer* to validate which class is discarding packets and if your application is allocated to the same class.
- If this is the case, consider allocating more bandwidth for this class.
- Alternatively, if the affected application is critical, move it to a higher priority class to improve performance. Refer to [Resolving Packet Discards (QoS)](/v1/docs/performance-issues-for-socket-sites-troubleshooting#resolving-packet-discards-qos) for instructions on configuring classes.
- One other reason for packet discard is micro-burst. Refer to [checking for micro-bursts](/v1/docs/troubleshooting-socket-site-packet-loss#18-checking-for-microbursts) on what it means, how to identify one, and finally, what steps to take to resolve it.

### Socket Resources Limitations

Performance degradation can happen when the Socket reaches its resource limitation.

#### 1. Maximum Supported Throughput

- Navigate to *Network > Site > Network Analytics* and verify if the throughput for the site is within the supported limit.
- Below are the Support Maximum Tunnel Throughput of our Socket models:

| **Socket Model** | **Maximum Tunnel Throughput** |
| --- | --- |
| X1500 | 500Mbps |
| X1600 | 1Gbps |
| X1600 LTE | 1Gbps |
| X1700 | 3Gbps |
| X1700B | 10Gbps |
- Refer to [Cato-Socket-Deployment-Guides](/v1/docs/cato-socket-deployment-guides-and-data-sheets) on the respective Data-Sheet for more details.
- If you exceed the listed limitations, refer to [Resolving Exceeding Supported Throughput](/v1/docs/performance-issues-for-socket-sites-troubleshooting#resolving-exceeding-supported-throughput).

#### 2. High Socket CPU Utilization

- Overutilization of Socket resources will also result in performance degradation.
- From the Socket WebUI, select the HW Status tab. This will show the current CPU % usage for each core. Consistent high CPU utilization will directly impact Socket performance and cause packet loss.
- If you notice consistently high CPU usage concurrent with network packet loss, please [contact Support](/v1/docs/submitting-a-support-ticket) for assistance.
- Starting with Physical Sockets version 21.1 and virtual Sockets version 22, CPU metrics for the Socket are now visible in CMA. Go to Network Analytics in CMA and select Hardware tab. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26280173001629.png)
- Additionally, CPU metrics are also available from the Socket UI, under the HW Status tab. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17682851010589.png)

### Performance Consideration: Active/Active WAN Throughput

In Active/Active WAN environments, application throughput may be limited when all data flows temporarily aggregate onto a single WAN link instead of distributing evenly across all available links. When this occurs, total throughput is capped by the bandwidth of one link, rather than utilizing the combined bandwidth of multiple links.

This behavior can affect performance expectations, particularly for protocols like SMB that rely on multiple concurrent flows. Flow distribution is influenced by dynamic network conditions and internal algorithms, which may not always guarantee balanced usage across links.

**Note:** If you observe throughput that does not align with the expected performance across multiple WAN links, please [contact Cato Support](/v1/docs/submitting-a-support-ticket) for further investigation and assistance.

### Sub-Optimal PoP

When using the Cato cloud, customers may notice slower application performance or reduced download/upload speeds.

- To validate, perform a PING test on the affected service.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17793680360477.jpeg)
- If the RTT returned is higher than expected, validate that the site is connected to an optimal PoP by navigating to Monitoring > Topology and clicking on the site.
- A right window pane will appear. Click on the "View Log" at the bottom of the window pane
- Another window will pop up. Validate that the ISP is close to the connected PoP.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17682794796957.png)
- To resolve this, refer to [Resolving Optimal PoP](/v1/docs/performance-issues-for-socket-sites-troubleshooting#resolving-connected-to-suboptimal-pop).

### Network Rule Validation

- Verify that the affected connection hits the correct network rule.
- If the affected application is a file-sharing or web application, create a network rule with TCP acceleration enabled and place the rule at the top of the list for isolation. Refer to [Best Practices for TCP Acceleration](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices) for more details.

### Added Cloud Latency

- Applications, such as SQL services, that are sensitive to changes in latency may experience increased time to complete tasks when being migrated over the Cato Cloud.
- The additional latency introduced by performing those queries over the WAN, even if only a few milliseconds, really adds up when considering the number of queries.
- To reduce the latency between Sites, it is recommended that you consider implementing Cato solutions such as [TCP Acceleration](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices), [Off-Cloud](/v1/docs/routing-traffic-to-an-off-cloud-link). or [Alt-WAN](/v1/docs/integrating-cato-with-an-alt-wan-network).
- Services hosted in public Cloud environments, such as Azure or AWS, can leverage [Cloud Interconnect](/v1/docs/getting-started-with-cloud-interconnect-sites) to significantly reduce latency between Sites.
- Alternatively, SQL queries can be modified to perform better over the Cato Cloud.

### Window Scaling for Windows Devices

- Window scaling in TCP/IP allows for a larger window size to be negotiated, enabling more data to be sent in each packet and improving performance.
- It should be enabled by default. To validate this, open the Command Prompt on the Windows device and run the command `netsh interface tcp show global`.
- Look for the "**Receive Window Auto-Tuning Level**" setting, which should be set to "normal".
- Refer to [Enabling TCP Window Scaling Option](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices) for more details. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22443113557917.png)

### TCP Timestamp Option for Windows Devices

- The default setting for Windows operating systems doesn’t support the TCP timestamp option. Enable the TCP timestamp option to improve packet RTT measurements, which can better help identify packet loss.
- This option also assists the TCP stack in adjusting the retransmission timer in case of packet loss.
- We recommend enabling the TCP timestamp on your Windows computers by following these steps:
  - Open the registry editor on Windows.
  - Navigate to the following key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters`
  - Look for a key named **Tcp1323Opts**. If it doesn’t exist, you’ll need to create it as a DWORD (32-bit) value, and name it **Tcp1323Opts**. Set the value to **2**.
  - Restart your system.
- To verify the status of TCP timestamps run ` netsh int tcp show global` from the command prompt. RFC1323 timestamps should be enabled. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22443144188061.png)

### iPerf Testing

- Another troubleshooting tool that helps to isolate the issue would be iPerf. iPerf testing can be used to measure the maximum achievable throughput in the network. This is included in the Socket Web UI as part of network and connectivity testing and is accessible under the Tools tab. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18079716878877.png)
- Refer to [Testing the link with iPerf](/v1/docs/troubleshooting-socket-site-packet-loss#14-testing-the-link-with-iperf) for more information on conducting iPerf testing in Socket Web UI. **Note:** For more accurate results, using UDP as the testing protocol is recommended because it doesn't consider congestion control. Keep in mind that this test aims to determine the maximum achievable throughput of the link.

### (Optional) Experience Monitoring Last Mile

- Customers with Experience Monitoring license can check Last Mile and Application Performance tabs for possible packet loss and packet discards. the data can be correlated with the findings in the site network analytics tab to better understand from where the issue originates.

### Off-Cloud

- For testing purposes, consider configuring an off-cloud setup between the two sites. This approach will allow us to compare the performance between on-cloud and off-cloud.
- If the performance is better in off-cloud, this could be the permanent solution to the performance issue.
- However, one thing to note is that the Cato Threat Protection engines do not inspect off-cloud traffic.
- For details in configuration, refer to [Routing-Traffic-to-an-Off-Cloud-Link](/v1/docs/routing-traffic-to-an-off-cloud-link).

## Resolving Discovered Issues

### Resolving Misconfiguration

#### Resolving Packet loss

- If Last Mile Packet Loss is present, replace the cable connected to the WAN port of the Socket.
- If feasible, connect to a different WAN port on the Socket and upstream device. If that didn't improve the last mile packet loss issue, contact your Internet Provider to isolate the problem further.
- If high packet loss is observed, consider enabling Packet Loss Mitigation for VoIP traffic. Refer to [Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic) for the details. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17799723288733.png)
- Refer to [How-to-Troubleshoot-Socket-Site-Packet-Loss](/v1/docs/troubleshooting-socket-site-packet-loss) for detailed troubleshooting on packet loss.

#### Resolving Packet Discards (QoS)

- To allocate more bandwidth to the class, navigate to Network > Bandwidth Management, select the affected class, and change the Limits accordingly. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17789909938717.png)
- To move the affected application to a higher priority class, either edit the existing Network Rule of the affected application and change the BW priority to a lower value (the lower the value, the higher the priority). Alternatively, create a new Network Rule and assign the BW priority to a lower value. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17798217277469.png)
- For a detailed guide on Bandwidth Management, refer to [Configuring-Bandwidth-Management-Profiles](/v1/docs/configuring-bandwidth-management-profiles).

#### Resolving Connected to Sub-Optimal PoP

- If the device is not connected to an optimal PoP, verify if the "Preferred POP locations" setting is configured. To do this, navigate to *Network > Site > Site Configurations > General > Preferred POP locations*. If the setting was set incorrectly, select the optimal location.
- The Socket will automatically reconnect to the newly defined preferred PoP as configured in *Network > Sites > Connection SLA.* However, the reconnection can also be triggered manually by using the action **Reconnect to Preferred PoP,** as explained in [Manually Reconnecting to a Preferred PoP Location](/v1/docs/defining-a-preferred-pop-for-a-site).

#### Resolving Exceeding Supported Throughput

- Reach out to your respective Account Manager or Customer Service Manager to upgrade to a bigger Socket. If you are unsure about who they are, [contact Support](/v1/docs/submitting-a-support-ticket).

## Raising cases to Cato Support

If the above steps did not help isolate and resolve the issue, please open a case with [Cato Support](/v1/docs/submitting-a-support-ticket). When opening a case, consider the following questions and provide the corresponding answers:

1. Does the issue affect all applications or specific applications?
2. If it affects specific application(s), are these new application(s)?
3. For new application(s), please provide the details, including application name, version, etc.
4. What has changed for existing application(s), leading to the issue?
5. Does this issue affect all sites or specific sites (s)? If specific site(s), please list down the affected sites
6. where is the server located if this affects all sites?

### Data Collection

Please collect the Support Self-Service ([SSS](/v1/docs/support-self-service-supportme-portal)) while replicating the issue. Additionally, install Wireshark on the device and capture two sets of packet data:

- The first set of packet captures (PCAP) should capture the performance issue. This can be done concurrently while collecting the SSS.
- The second set of PCAP should be collected when the connection bypasses the Cato cloud, i.e., when the performance issue is not present. This set of data will serve as a benchmark for Support when reviewing the collected logs and SSS.
