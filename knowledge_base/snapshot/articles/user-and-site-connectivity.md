---
title: "Troubleshooting Socket Site Packet Loss"
slug: "troubleshooting-socket-site-packet-loss"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/troubleshooting-socket-site-packet-loss"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Socket Site Packet Loss

## Issue

Determining the source of packet loss and why it is occurring is not always easy. Packets pass through multiple networks owned by different ISPs and organizations over the Internet, and you don’t have access to every router in the path to check things like the link state and CPU load. In addition, packet loss can occur at any point along the network path.

## Possible Causes

There are numerous reasons that packets can be dropped along the way. A few common ones are:

- ISP peering issues
- Link congestion
- Misconfiguration (bandwidth settings or NIC speed and duplex)
- Hardware failures
- High CPU on a network device
- Micro-burst handling

## Understanding Packet Loss at Cato

A good way to identify packet loss at Cato is to use the [Analytics screen](/v1/docs/showing-the-site-network-analytics) in the Cato Management Application. The **Packet Loss** and **Discarded** graphs show packet loss over time and let you focus on specific timeframes. These graphs are useful to identify if packet loss is occurring and when it occurred in the past.

> [!NOTE]
> Note:
> 
> The smallest data bucket sample size in the Analytics graphs is 5 seconds. As a result, a micro-burst within 5ms will get normalized within the averages displayed and is not shown as a peak in the analytics graph.

### **1. Provider loss**

Occurs between the Socket and the PoP. Although most provider packet loss is caused by network connectivity issues on the last mile outside of Cato’s control, it doesn’t necessarily exclude a Cato-related problem.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331688785181.png)

**How Cato Measures Provider Loss**

Provider loss is measured by comparing the count of packets sent and received over a given link on both the Socket and the PoP.

- **Downstream packet loss** is the difference between the number of packets sent by the PoP and the number of packets received by the Socket, expressed as a percentage.

**Formula:**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331510191773.png)
- **Upstream packet loss** is the difference between the number of packets sent by the Socket and the number of packets received by the PoP, expressed as a percentage.

**Formula:**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331524124189.png)

The way that Cato calculates provider packet loss means that, as easy as it may be, you can’t put all the blame on the ISP right away. It's possible that you have equipment between the Socket and the ISP router that contributes to packet loss, or there may be problems with the network path closer to the PoP that is beyond the control of the ISP.

### **2. Cato discarded**

Occurs when [Cato QoS](/v1/docs/part-3-the-socket-traffic-prioritization-and-qos) intentionally drops packets. The QoS engine starts to discard low-priority packets when:

- Congestion occurs when the total throughput over a link matches the configured bandwidth for the link.
- Cato also discards packets if a BW management priority is configured with a hard throughput limit and traffic matching the priority hits the limit.
- During bursts (even high-priority queues may drop packets).

Cato discarded packet loss is expected behavior and not necessarily a sign of a problem.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331722157085.png)

Any issues related to Cato discard packet loss are likely caused by a misconfiguration. Critical applications, like VoIP, should be given the highest bandwidth management priority. If congestion occurs, Cato drops low-priority traffic, but it does not drop high-priority traffic. Always make sure that appropriate [bandwidth management priorities](/v1/docs/configuring-bandwidth-management-profiles) are assigned to traffic.

Analytics provide a broad view of packet loss. However, unless you’re dealing with Cato's discarded packet loss, analytics alone can’t tell you what is causing the packet loss or where the packet loss is occurring.

## How to Troubleshoot Packet Loss

### 1. Determining the Scope of Packet Loss

When you start, it’s really important to find out who or what is experiencing the packet loss.

- Is every user experiencing packet loss at a site, or is it isolated to a single endpoint?
- Does the packet loss occur over the Internet or over the WAN?
- Are multiple sites affected by packet loss, or just one?
- Is all traffic affected, or is it just a certain application?
- Is the packet loss constant, or does it only occur intermittently?

Knowing the answers to the questions above can help you identify related [CMA events](/v1/docs/analyzing-events-in-your-network) and save you time during the troubleshooting process. The more details you know ahead of time, the more focused your troubleshooting can be.

### 2. Checking Site Analytics - Packet Loss Graph

Is packet loss showing on the site’s Analytics packet loss graph? We have different recommendations based on Analytical graphs that may show packet loss and discarded packets.

**No Packet Loss**

It’s possible for packet loss to exist without any packet loss being displayed in the Analytics screen. There could be an issue on the local network, or it could be a PoP-related issue. Using the UI network tool to ping a LAN side IP from the Socket can be a good way to identify the root cause.

**Packet Loss**

If packet loss is shown on the graph, it may be caused by a BW misconfiguration. Please have a look at the configured bandwidth as outlined below in [Checking Bandwidth Configuration](/v1/docs/troubleshooting-socket-site-packet-loss#7-checking-bandwidth-configuration).

For Provider packet loss, check if the drops are present only when traffic spikes (bursts) occur. If that's the case, identify the traffic causing the bursts using the [Application Analytics](/v1/docs/understanding-app-analytics) page. You can limit the application traffic by assigning it to a restrictive [BW management profile](/v1/docs/configuring-bandwidth-management-profiles).

Often, we will see cases where throughput is generally low, but burst spikes cause packet loss. We have to take into account that the ISP has its own traffic shaping policy, and in such a case, it is likely that the ISP policy and Cato's traffic shaping policy have different burstiness policies. For more information about burstiness, see below [Checking for micro-bursts](/v1/docs/troubleshooting-socket-site-packet-loss#18-checking-for-microbursts)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331579975709.png)

### 3. Checking Site Analytics - Discarded Packets Graph

For Cato discarded packets, you should also investigate the bandwidth priorities. Check the [Priority Analyzer](/v1/docs/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer) under the site’s Analytics screen to see what priority is being dropped. You can expand the priority section to show the top applications in that priority. If packet loss only affects a specific application, you may need to raise the priority of that application in the [Network Rules](/v1/docs/configuring-network-rules). Remember, Cato QoS is designed to drop low-priority packets when congestion occurs, so Cato discarded packet loss is not always a problem.

Cato QoS can also discard any packets, regardless of priority, due to bursts in that queue. This behavior is also expected due to the nature of burst management. The Priority Analyzer page can be used to identify whether traffic bursts occur at the same time as when the packets were discarded. For more information, see [Socket Traffic Prioritization and QoS](/v1/docs/part-3-the-socket-traffic-prioritization-and-qos).

![Use_as_placeholder_for_now.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/5946687083421.png)![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23143004561437.png)

The **Priority Analyzer** in the Analytics screen shows packet loss in the upstream and downstream directions for each QoS priority.

### 4. Checking Site Analytics - Last Mile Packet Loss

To assess if the ISP is experiencing issues, use the [Last Mile tab in the Analytics](/v1/docs/last-mile-monitoring-probes-and-connectivity) screen to check for any latency changes or packet loss that appear on the WAN link. Unlike provider packet loss, last-mile data is based on ICMP tests to popular websites. As a recommendation, additional service IPs that are ping-able can be added to the [Last Mile monitoring](/v1/docs/last-mile-monitoring-probes-and-connectivity) page. For example, if there are VoIP-related issues, the SIP server IP can be set as one of the IPs.

If ISP-related packet loss is suspected, ask your ISP the following questions:

1. Are you applying QoS on UDP/443 or UDP/1337 (DTLS) traffic?
2. Do you apply any DoS protection on UDP traffic that may be causing packet loss to the PoP IP?
3. Is there congestion or high CPU on your router(s) in the path to the PoP IP?
4. Do you allow bursting over the subscribed line rate?

### 5. (Optional) Experience Monitoring Last Mile

Customers with [Experience Monitoring](/v1/docs/using-the-experience-monitoring-page) license can check Last Mile and Application Performance tabs for possible packet loss and packet discards. The data can be correlated with the findings in the site network analytics page to better understand where the issue originates.

### 6. Change DTLS Port UDP/443

Some ISPs may apply traffic shaping or QoS specifically on UDP/443. This can introduce packet loss even when the link is otherwise stable.

- In the Socket configuration, [change the DTLS tunnel port](/v1/docs/setting-a-different-port-to-connect-to-the-cato-pop) from **443** to **1337**.
- After applying the change, monitor packet loss and latency in the Analytics screen.
- If packet loss improves, this confirms that the ISP is shaping UDP/443 traffic. In that case, keep the tunnel on 1337 or escalate the issue with the ISP.

### 7. Checking Bandwidth Configuration

Packet loss can be caused by link congestion, and it’s important that the bandwidth for each WAN link is configured correctly in the Cato Management Application. Make sure that the configured bandwidth matches what the ISP provides in the [site configuration](/v1/docs/updating-the-socket-wan-interface-bandwidth). Configure the Socket WAN interface bandwidth setting according to the terms of the Cato site license.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331568529053.png)

Azure/AWS environments don't have traditional bandwidth limitations. Instead, the configured site bandwidth should never exceed the supported bandwidth for the vSocket. For Azure, as of version 21, the Standard_D8ls_v5 VM size supports up to 2Gbps. In AWS, the c5n.xlarge instance size provides bandwidth exceeding 2Gbps. It's important to ensure that the site's configured bandwidth stays within the supported limits for optimal performance.

If the configured bandwidth is lower than what the ISP provides, Cato’s QoS engine can start dropping packets when the configured bandwidth limit is exceeded. If this is the case, there is a flatline across a site’s Analytics throughput graph equal to the site’s configured bandwidth along with Cato discarded packets.

This same behavior can occur if the bandwidth is configured correctly, but the ISP link is congested. Although this behavior does not guarantee a problem, it is a good practice to confirm that the bandwidth is configured correctly in this situation.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331767621917.png)

If the configured bandwidth is higher than what the ISP provides, Cato’s QoS engine does not kick in when the ISP’s bandwidth limit is exceeded, and therefore, the ISP may start dropping packets randomly. If this is the case, you see a flatline across the site Analytics throughput graph below the level of the configured bandwidth along with provider packet loss.

Socket throughput and capacity information per each Socket model are available in the Socket datasheet, see this article: [X1700, X1600 & X1500 Socket Guides](/v1/docs/cato-socket-deployment-guides-and-data-sheets).

### 8. Check Socket CPU performance

From **Network Analytics** in CMA, select the [Hardware](/v1/docs/showing-the-site-network-analytics) tab. This section displays **historical** CPU percentage usage for each core.

Consistent CPU utilization above 90% can negatively impact Socket performance and may cause packet loss and high latency. If constant high CPU utilization is observed, contact your account representative to evaluate a potential hardware replacement (e.g., from X1500 to X1600).

For further troubleshooting, [contact Support](/v1/docs/submitting-a-support-ticket)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25255875205277.png)

**Real-time** Socket CPU usage can be seen from the socket WebUI, under the [HW Status](/v1/docs/using-the-socket-webui-tools) tab. Compare active usage with historical data to identify performance trends.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13663434067997.png)

### 9. Ruling Out Site Reconnects

Site reconnects to the Cato Cloud are a source of packet loss. Check **Home > Events** to see if the packet loss correlates with reconnect events. Filter events as sub-type = 'reconnected'.

Reconnect events will show a message explaining the reason for the disconnections. See [Understanding Reconnected Events](/v1/docs/understanding-socket-connectivity-event-message-fields)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331791699357.png)

### 10. Bypassing Cato

For packet loss over the Internet, set up a source or destination [bypass](/v1/docs/bypassing-the-cato-cloud-site-level-policy) to quickly rule out an issue with the Cato Cloud. The easiest way to do this is to set up a source bypass for a single user’s IP address in the site configuration and see if the packet loss continues. If the packet loss continues, the problem might be on the LAN, the Socket, or the ISP, but the problem would not be related to a PoP.

![3._Bypassing_Cato_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/5946686944541.png)

### 11. Running Ping Tests

Start a continuous ping between a source and destination IP address that is affected by packet loss. Pings are easier to trace and can be analyzed in packet captures. When some of the ping requests do not arrive at their destination, then you are probably experiencing packet loss and it will be shown as request timeout.

**Note:** Packet captures are CPU intensive and may cause performance degradation. Please ensure packet captures are disabled unless actively troubleshooting.

The Socket UI also allows you to ping by hostname or IP with the [ping tool](/v1/docs/using-the-socket-webui-tools). You can select the interface that you want to send the ping over, either via Cato or directly via the WAN link. Look for any inconsistency in the ping results, such as **packet loss** or **high latency**. If packet loss is present both with and without Cato, it may indicate an ISP issue. Also, if one of the links is **4G/LTE,** you need to remember that those links are more sensitive to packet loss.

The UI only sends 10 ping requests, so if you need more pings you will need to click the **Ping** button again.

**Note:** Ping tests are good for checking basic network health, but no ping drops do not necessarily indicate a clean line.

![Ping.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/5946693721501.png)

### 12. Running Traceroute Tests

Traceroute is used to identify the routers (hops) between a source and destination. It will display packet loss and latency for each of the hops.

Traceroute can be run from the Socket UI with the [Traceroute tool](/v1/docs/using-the-socket-webui-tools). Run Traceroute to find any packet loss or unexpected high latency on any of the hops over the WAN link between the socket and the destination. It's recommended to set the maximum count (200) with the lowest interval (0.1) when running the test and validating packet loss.

**Traceroute result analysis**

Be aware that packet loss shown at any single hop is not necessarily a sign of a problem. A single hop could show 100% packet loss simply because ICMP is not enabled on the router. A hop can also show less than 100% packet loss without there being a problem due to ICMP rate limiting. If you see some packet loss on one hop and 0% packet loss on the next hop, you’re likely witnessing ICMP rate limiting.

If there is an actual problem with packet loss, it will start at one hop and continue for multiple hops, with each hop showing packet loss. It’s also possible that multiple routers on a path are contributing to packet loss, so the amount of packet loss can vary at each hop. For example, there are eight hops in the route, and traceroute shows packet loss for hops 3-7.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30761329628061.png)

### 13. Testing the Link with Speedtest

The [Real-Time](/v1/docs/analyzing-data-for-a-site-in-real-time) screen can help spot any current throughput changes to identify immediate packet loss and discarded packets. While troubleshooting, use the Socket's [speedtest tool](/v1/docs/using-the-socket-webui-tools) to simulate high load and reproduce packet loss due to high demand.

Socket Speedtest results via Cato are expected to be close to the bandwidth configured for the link in the Cato Management Application. However, DTLS tunnel overhead (117 bytes) can slightly reduce throughput.

The test will saturate the link and show any ISP-related packet loss on the [Network Analytics](/v1/docs/showing-the-site-network-analytics) screen. Discarded packets are expected when running the test if the configured link bandwidth is lower than the ISP-provided bandwidth.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331879501597.png)

**Direct Speedtest**

When running the Speedtest directly via the WAN port, the upstream result should be close to the configured bandwidth license in the Cato Management Application. The Socket will still use QoS for the upstream Direct Speedtest as per the site's [bandwidth license](/v1/docs/managing-site-bandwidth-in-licenses). On the other hand, the downstream result will show the full capacity of the local ISP.

### 14. Testing the Link with iPerf

The Socket WebUI lets you use the [iPerf tool](/v1/docs/using-the-socket-webui-tools) to troubleshoot last-mile performance issues between the Socket and the connected PoP in the Cato Cloud. The Socket running the iPerf client performs the test against the iPerf server running on the connected PoP.

Run the iPerf test via Cato and directly over the WAN from the socket UI's tools page. Select UDP as the protocol (to rule out TCP flow control), set the direction (upstream or downstream), and target rate as the configured bandwidth. This tool can better confirm that the throughput over Cato and over the WAN is as expected. Be aware that DTLS tunnel overhead (117 bytes) can slightly reduce throughput.

In the example below we're setting 45Mbps as the target rate (which is the same BW configured in the Cato Management Application) and the received rate is lower than expected with a packet loss of 3.7%

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11102392309789.png)

### 15. Checking Link Aggregation (LAG) Links

Packet loss and high latency may be caused by Link Aggregation (LAG) misconfiguration between the Socket and an internal switch. This particular issue cannot be detected in Network Analytics, but rather, it needs to be troubleshot within the LAN. Cato only supports static LAG and the LAG peer must support the same mode. LAG configuration mismatches will lead to packet loss.

For more troubleshooting information see [Link Aggregation (LAG) Link Experiencing High Latency and Packet Loss](/v1/docs/link-aggregation-lag-link-experiencing-high-latency-and-packet-loss)

### 16. Checking the Socket’s Link Speed

One possible cause of provider loss is that a Socket link is running at half-duplex. This means that packets can only travel in one direction (outbound or inbound) at a time, which drastically reduces throughput and results in packet loss. All Socket links should always be at full-duplex without exception.

Also, make sure that both WAN and LAN link speeds are equal to or above the bandwidth configured for a site. The link speed can be the limiting factor for throughput. For instance, if a site’s configured bandwidth is 200 Mbps but the LAN link has only negotiated to 100 Mbps full-duplex, a computer connected to the Socket can’t achieve higher than 100 Mbps throughput.

To check the link state, log in to the Socket UI and view the **Link** status on the **Monitor** page. The example below shows the WAN1 link at 100 Mbps half-duplex.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331828841117.png)

If you notice a link at half-duplex or set to the wrong speed, check the port settings on the device that the Socket’s link is connected to. Make sure it is set to **auto-negotiate** or that it matches the Socket’s speed settings. All Socket links default to auto-negotiate, but you can force the speed under the **Network Settings** page.

![_7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/5946686900509.png)

If the port settings are correct on the other device, the Ethernet cable could be damaged. Replace the cable with a known good one and see if the duplex or speed changes. If that doesn’t work, connect a laptop computer or other device to the Socket’s port and check the link status. Do the same on the other device. If the Socket’s link comes up at the expected speed and full-duplex but the other device’s link does not, you’ll know the problem is with the other device.

### 17. Checking for Duplicate IPs

Another issue at the Socket level that can cause packet loss is duplicate IPs in the network. The Socket can usually detect IP conflicts with its configured interface IP addresses. An IP conflict exists when two devices on the same network are assigned the same IP address. If this happens, you will see the following error on the Socket UI's Monitor page.

The duplicate IP may fail to be detected when a static IP address is configured on the WAN interface, as the Socket only passively monitors for an IP conflict. It will only detect an IP conflict if the Socket receives an ARP from the device with the conflicting IP.

Once the conflicting IP issue is resolved, it can take up to 24 hours for the warning to disappear from the WebUI. See [IP Address Conflict Reported on Socket UI Even After It's Resolved](/v1/docs/ip-address-conflict-reported-on-socket-ui-even-after-it-s-resolved)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10331853343133.png)

### 18. Checking for Micro-bursts

Another potential cause of packet loss is micro-bursts (burstiness). Micro-bursts are characterized by a sudden surge of packets or data frames that occur within a very short time frame, typically lasting **only** a few microseconds to milliseconds. In situations where micro-bursts occur and exceed the link's rate limit, the Last-Mile Provider (ISP) may drop excessive traffic, resulting in packet loss.

In the graph below, you can see an example of typical packet loss caused by micro-bursts and the improvement after adjusting the burstiness value settings.

![Inserting image...](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12247688429597.png)

In the example above the burstiness level value was modified from the default value of 0.2 to 0.01 which means that the Socket and the PoP apply more aggressive shaping on the traffic, thus solving the packet loss issue.

#### **Adjusting burstiness level settings to mitigate the packet loss**

The default burstiness value applied for the upstream and downstream directions is 0.2. With this value, the Socket and the PoP serialize the packets to the media as fast as possible, allowing more bytes to be sent in the first microseconds of the time period bucket. This setting optimizes performance by reducing the serialization delay and the overall latency.

As part of this troubleshooting step, you need to gradually reduce the burstiness level until the packet loss is mitigated. As you reduce the burstiness level value, the Socket and the PoP apply more aggressive shaping on the traffic thus smoothing the micro-bursts. The lowest value you can configure is 0.001.

The best practice to adjust the burstiness level is to gradually reduce the value (for example, from 0.2 to 0.18). After reducing the value, monitor the impact by analyzing the packet loss in the Site Monitoring **Real Time** or **Network Analytics** screens. Keep in mind that the site metrics usually take a few minutes to be updated. Continue reducing the burstiness value until the packet loss is mitigated.

If the packet loss is not resolved by this procedure, it means that it is caused by a different reason than micro-bursts. In this case, restore the default burstiness value of 0.2 and [Contact Support](/v1/docs/submitting-a-support-ticket) for further assistance.

#### **Modifying the Burstiness level**

The burstiness level can be adjusted per the upstream and downstream directions. This setting affects all of the site’s WAN links.

The configuration is applied on a site-level or an account-level. The site-level configuration takes precedence over the account-level.

**To configure the Burstiness level**:

1. From the navigation menu, select **Resources** > **Advanced Configuration** for account-level or **Site Configuration** > **Advanced Configuration** for site-level setting. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12247694270493.png)
2. Select **Burstiness downstream value** or **Burstiness upstream value**.
3. Enable the setting and adjust the value between the range of 0.001 - 0.2. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12247737676189.png)
4. Click **Apply**
5. Click **Save**

**Notes:**

- If burstiness was previously adjusted by Cato Support, the adjusted value will be shown instead of the default value of 0.2
- Burstiness values can be adjusted only for Socket sites
- The smallest data bucket in the Cato Management Application is 5 seconds, microbursts are normalized within the smallest data buckets and are usually hard to identify.
- Setting the burstiness value to 0.001 for sites with a bandwidth of 10 Mbps and below is not recommended, as it can cause connectivity issues for the site.
