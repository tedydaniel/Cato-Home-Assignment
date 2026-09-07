---
title: "Socket Site Tunnel Connectivity Troubleshooting"
slug: "socket-site-tunnel-connectivity-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-site-tunnel-connectivity-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Site Tunnel Connectivity Troubleshooting

## Overview

Site connectivity is paramount for hosts behind a socket to have access to the WAN via the Cato cloud. The lack of connectivity of a site can disrupt business function. This playbook looks to provide guidance on troubleshooting this scenario.

## Symptoms

A failure in socket connectivity can manifest in a number of ways. An administrator may note the following symptoms:

- The Site is disconnected in CMA
- Site connecting to unexpected PoP
- Network Analytics shows that the tunnel is unstable

## Possible Causes

The following are possible causes that you can identify while troubleshooting

- No Socket Connectivity
- DTLS traffic one way only
- Poor Underlay Performance
- IP Geolocation Restrictions
- Unsuitable PoP selection config
- SLA configuration at incorrect baselines
- NAT Device Infront of socket

## Troubleshooting the Issue

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

### Troubleshooting Site Disconnected in CMA

#### Gathering Information from Events

Using the **Home** > **Events page** in CMA, an administrator can quickly get a history of connectivity events for sites within an account. Events can be filtered down into relevant events by selecting the 'Sites connectivity status' preset or else by filtering for Event type 'Connectivity' and Sub-type 'Disconnected.' You can further filter for the name of the site in question with the 'Source site' field.

![Monosnap Cato|Liam-lab - Events 🔊 2024-02-22 13-28-40.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16955207476125.png)

Viewing the timestamp of the relevant disconnection event from the site in question can help in focusing the investigation. Were any wider networking events or local power events known to occur at this time stamp? Are there any [audit trail](https://support.catonetworks.com/hc/en-us/articles/4413273463953-Using-the-Admin-Audit-Trail) changes preceding this that may be correlated?

#### Checking Socket Connectivity

Please view [Cato Socket Connection Prerequisites](/v1/docs/cato-socket-connection-prerequisites-and-known-limitations) to understand the requirements of a socket's connection.

The socket's connectivity status can be seen via its local WebUI, see [Logging in to the Socket WebUI Locally.](/v1/docs/accessing-the-socket-webui#logging-in-to-the-socket-webui-locally-for-a-new-or-reimaged-socket) For a socket to be connected, the WAN port that is being used to service the connection to the Cato cloud should show a green status icon. An indicator other than green suggests a connectivity problem. The meaning of different status icon colours is described in [Understanding the Link Status Icons](/v1/docs/accessing-the-socket-webui)

![thumbnail_image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16955175451165.png)

For a red icon, ensure that there is a working physical link between the socket and the ISP device. This includes the cables being connected securely and port LEDs lighting up as expected.

An IP conflict will also be detected by the socket connectivity status. The IP conflict warning will continue to be displayed for a 24-hour period, starting from when the conflict was first detected as explained in [this KB article](/v1/docs/ip-address-conflict-reported-on-socket-ui-even-after-it-s-resolved).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18529219826461.png)

Confirm that the **Force Recovery via Internet Bypass** status under **Tools** is Normal. The 'Force Bypass' button will force all LAN traffic to bypass Cato and will bring down the Cato tunnel, showing the Site as disconnected in CMA. Hence, all remote configuration and access to this device will fail. In an HA setup, if the primary Socket has 'Force Bypass' enabled, the secondary Socket will continue to remain as the backup Socket, and traffic behind the Sockets will be routed directly to the Internet.

The screenshot below shows 'Force Bypass' enabled on the primary Socket, and the secondary Socket remains as Standby.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28642248797725.png)

If the Force Recovery status is Active, exit this state by clicking the **Exit Forced Bypass** button.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22610138722845.png)

In the event of a connectivity problem, we can utilize the **Tools** tab to test further. To connect to Cato, the socket requires L3 access to Cato's public IP addresses. Use the ping tool to ensure that this Socket can reach Cato IP addresses or domains, or well-known IP reachable addresses like 8.8.8.8 over the WAN port directly. If none are reachable, please view the [Resolving No Socket Connectivity](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-no-socket-connectivity) section.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16955207509917.png)

#### Running Packet Capture

A [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) can also be done to ensure that the Socket's request to establish a DTLS tunnel to the PoP is being responded to. When capturing on the WAN port in question, bi-directional packets on UDP/443 to the PoP should be seen. The following screenshot shows a successful DTLS handshake and the exchange of **Application Data** packets.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19742398244637.png)

If only outbound DTLS packets are detected or the DTLS handshake is incomplete, please view [Resolving Incomplete DTLS Handshake](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-incomplete-dtls-handshake).

#### Unable To Establish Tunnel Due to NAT Device Infront of Socket

For Sockets that use multiple WAN links, if there is a NAT device between the Socket and the PoP, then it’s possible that one or more of the WAN links can’t connect to the PoP. This can create connectivity issues, such as the HA status of the site is Not Ready.

The PoP uses the source port of each incoming DTLS connection to connect each WAN link to the same logical tunnel. The NAT device may change the source port, and prevent a WAN link from connecting to the same logical tunnel as the other WAN links.

#### Failing DTLS Connections with LTE/5G providers

As mentioned in this [case study](/v1/docs/socket-site-is-disconnected-with-lte-5g-providers), if LTE/5G providers are being used to connect to Cato, the ISP may interfere with the DTLS handshake on port UDP/443, which can be seen as carrier-specific data (e.g., APN) during the handshake.

Even though there's two-way DTLS communication, the handshake is not completed; hence, the Cato tunnel will not come up.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20255496885661.png)

To resolve this issue, change the DTLS port to UDP/1337, please view [Resolving Incomplete DTLS Handshake](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-incomplete-dtls-handshake).

### Troubleshoot Unexpected PoP Selection

#### Check For the ISP's IP Address and the Current Selected PoP

Under Monitoring, select a Site and open the Site's Overview pane. In the Site Sockets section, click 'View Log' to see all recent connections. Look for the ISP's public IP (Remote IP) that connects to Cato, along with the ISP's Name and location. The 'PoP' column will display the current PoP the Site is connected to.

It is important to verify that the 'Remote IP' and ISP location are as expected and that the ISP is not backhauling the connection through an unexpected location. The ISP location (city) should correspond with or be close to the Country/City specified in the Site's general settings within CMA.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21454560091549.png)

#### Check For PoP Selection Config on CMA

A stale or misconfigured preferred PoP location on a site can force connections to sub-optimal PoPs. PoP selection configuration can be viewed per site via the **Network** > **Site** > **Site Configuration** > **General** page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16958089925533.png)

If a location is configured here that doesn't look to be suitable for optimal connection, or if it is preferred to allow Cato PoP selection mechanism to determine the optimal PoP, please view the [Resolving Unsuitable PoP Selection Config](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-unsuitable-pop-selection-config) section.

#### Check For PoP Selection Config on Socket

Stale or unsuitable PoP selection configuration can also exist in socket configuration. To view if this is the case navigate to the Cloud Connection Settings in the webUI of the socket, see [Using the Socket WebUI.](/v1/docs/accessing-the-socket-webui)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16959394681629.png)

If config exists here and it is preferred to allow Cato PoP selection mechanism to determine the optimal PoP, please view the [Resolving Unsuitable PoP Selection Config](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-unsuitable-pop-selection-config) section.

#### Check PoP Status

Sockets may connect to an unexpected PoP due to the nearest geographical PoP being affected by maintenance or other such issue. Please view the [PoP Status](https://status.catonetworks.com/) page to verify if this is the case.

#### Verify Location Restrictions for Geolocation

As per the Cato MSA, socket sites in some geolocations are restricted from connecting to PoPs in other locations. The MSA is outlined when purchasing Cato services.

Socket sites in some geolocations will be limited to a pool of available PoPs, for example socket sites in China will connect to PoPs within China, and Vietnamese socket sites will connect to a pool of PoPs within Asia.

For more information on this, please refer to the [MSA](https://www.catonetworks.com/msa/).

#### Check for Signs of Socket Moving Between PoPs

The Events page can be used to determine if a socket is likely not on the originally determined optimal PoP due to connectivity issues. Using a selection of fields, a timeline of the socket's connectivity to different PoPs.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16960514306333.png)

By using the 'Site Reconnected' events preset, and further filtering to the site in question and also setting the 'event_message' field value to 'Performance issue detected, reconnected to a different service node in the Cato Cloud', we can see all instances where a socket site has moved PoPs due to tunnel connectivity parameters breaching configured SLA thresholds. If a socket site is breaching SLA thresholds to multiple PoPs, continue the troubleshooting flow to verify Connection SLA Settings.

#### Verify Connection SLA is Not Too Strict

[Connection SLA](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites) plays an important role in ensuring a site is connected to the optimal PoP, especially in dynamic network environments with public underlay like through ISP internet connections. A Connection SLA that is too strict, however, can cause unnecessary reconnections to PoPs other than an admin's preferred location.

Connection SLA configuration per site can be seen under **Network** > **Site** > **Site Configuration** > **Connection SLA**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16960411903517.png)

Using [Network Analytics](/v1/docs/showing-the-site-network-analytics) to build a baseline of last mile performance metrics, consider if the SLA metrics are suitable for this site.

If these parameters are not suitable, please view [Resolving SLA Configuration at Incorrect Baselines](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-sla-configuration-at-incorrect-baselines)

If the parameters are suitable, yet PoP re-optimisation events are still occurring regularly to a number of PoPs, please view the [Resolving Poor Underlay Performance](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-poor-underlay-performance) section.

If the Socket keeps connecting to an unsuitable PoP after following the above steps, please open a [ticket with Support](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#raising-cases-to-cato-support) and highlight the current and expected PoP.

### Troubleshoot Unstable Tunnel

#### Check the Correlation Between Last-Mile and Site Connection Performance

When noting that a given site is experiencing poor performance in its connection to a PoP, it is important to isolate whether this packet loss is likely due to performance on the underlying ISP line.

This can be done by correlating any given performance issues over a timeframe with the performance seen over the last mile within the same time frame and looking for patterns.

The [Network Analytics](/v1/docs/showing-the-site-network-analytics) can be used to do this.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16961296090909.png)

The above example shows upstream packet loss detected on a site tunnel to the PoP. We can see several spikes of ~10% and a constant low level of loss throughout the time period.

When comparing this to the performance for the last mile over the same time period, we can see the following:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16961296096669.png)The last mile can be seen to also see some variation in performance, but it is affected by a constant level of loss between ~10-20%. It is clear from this that packet loss on the tunnel from the socket to the Cato PoP is likely to be a symptom of poor performance on the underlay.

If this is the case when troubleshooting a performance issue, please view [Resolving Poor Underlay Performance](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-poor-underlay-performance)

#### Cross-Referencing Similar Sites

Shared properties between sites can be used to attempt to infer facts about the issue in question. For example, the below site is having connectivity issues. Note that the connected PoP is London:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19376778301213.png)

This information can be used to cross-reference other sites that may be connected to London to see if any issues are shared. This can be seen in the screenshot below:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19376787823261.png)

If cross-referencing suggests the issue is on a Cato PoP, view the section [Check PoP Status](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#check-pop-status).

Cross-referencing is also useful for sites with shared ISPs. This is being done in the below example:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19376778317341.png)

If this cross-referencing implies the ISP is having connectivity issues, view the section [Resolving Poor Underlay Performance](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-poor-underlay-performance).

#### Verify Connection SLA is Not Too Lenient

[Connection SLA](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites) plays an important role in ensuring a site is connected to the optimal PoP, especially in dynamic network environments with public underlay like through ISP internet connections. A Connection SLA that is too lenient, however, can cause sockets to hold onto sub-optimal connections to PoPs for longer than an administrator would want, and so impact sensitive applications.

Connection SLA configuration per site can be seen under Network > Site > Site Configuration > Connection SLA.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16961513519389.png)

Using [Network Analytics](/v1/docs/showing-the-site-network-analytics) to build a baseline of last mile performance metrics, consider if the SLA metrics are suitable for this site.

If these parameters are not suitable, please view [Resolving SLA Configuration at Incorrect Baselines](/v1/docs/socket-site-tunnel-connectivity-troubleshooting#resolving-sla-configuration-at-incorrect-baselines).

## Resolving Discovered Issues

### Resolving No Socket Connectivity

It is important to isolate whether connectivity issues only affect the Socket. If you plug a laptop into the same ISP connection, do you encounter the same issues with resolving DNS or pinging addresses? If so, contact your ISP to progress.

Ensure that the test laptop has IPv6 disabled and, in case of static IP address allocation, assign the same IP as the Socket when testing.

If the connectivity issues are isolated to your Socket, ensure that the IP configuration is correct under the **Network Settings** tab of the WebUI:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16955207519773.png)

### Resolving Incomplete DTLS Handshake

Ensure with your provider that DTLS traffic on UDP port 443 is allowed to egress towards the internet. If necessary this port can be changed to UDP/1337 as described in [Setting a Different Port to Connect to the Cato PoP](/v1/docs/setting-a-different-port-to-connect-to-the-cato-pop).

### Resolving Poor Underlay Performance

Poor underlay performance will impact any tunnel built on that underlay. Whilst underlay is the domain of the ISP there are some tools that can be used to identify where performance issues are being introduced, and also to attempt to mitigate performance issues where possible.

The socket's WebUI has a [traceroute tool](/v1/docs/using-the-socket-webui-tools) that will allow you to ping publicly accessible hosts over the ISP connection. When pinging publicly accessible hostnames it can be determined the hop at which loss or excess delay is introduced on the l3 path between a socket and the service.

![Monosnap Cato Networks - Tools 🔊 2024-02-23 09-52-45.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16982481871517.png)

In the above instance, packet loss is clearly being introduced directly from the L3 boundary provided by the ISP.

Whilst ultimately any underlay issues will have to be taken to the ISP, ensuring the settings in CMA are correct will help to mitigate the impact of performance issues. Ensure that the bandwidth configuration for a socket interface is accurate for the bandwidth provided by the line. Socket WebUI speedtest tools can be performed to benchmark the connection. In addition, [reducing the burstiness parameters](/v1/docs/troubleshooting-socket-site-packet-loss#18-checking-for-microbursts) of a connection can force Cato to engage the [QoS engine](/v1/docs/qos-policies-explained) sooner, and allow your least prioritised traffic to be dropped in favour of more critical applications.

### Resolving Unsuitable PoP Selection Config

To revert any manual PoP selection configuration and allow Cato to select the optimum PoP for a socket connection, first ensure that there is no manual PoP location configuration on CMA, and then do the same for the socket.

In CMA this can be done in **Network** > **Site** > **General** > **Preferred PoP Locations**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16982718414493.png)

Ensure 'Automatic' is selected.

On the socket WebUI navigate to **Cloud Connection Settings**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16982747125917.png)

Ensure that Destination is set to 'Steering'.

### Resolving SLA Configuration at Incorrect Baselines

The first step in ensuring SLA configuration is suitable is to understand what the critical thresholds or requirements for critical applications at use from the site are.

To expand on this consider two examples.

- Application A is tolerant to low levels of packet loss and has good packet re-ordering capabilities, however, the session needs to be maintained for the service to work; breaking and re-creating the flow causes issues within the application.
- Application B is very sensitive to sporadic packet loss. Even low levels of loss can cause data transfers to be interrupted and the transfer would have to be started again from the beginning. That said, the control channel is very resilient to sessions ending and reconnecting.

With the profile of application A, we would create an SLA configuration that allows for low levels of loss even over long time windows; it is a preference to retain the connection to the PoP to maintain the session even if loss is otherwise impacting the service.

Application B, in contrast, requires a stricter SLA configuration. It is preferable to move PoP if even small amounts of packet loss are detected to protect the integrity of the transfers.

Sites obviously use a mix of applications with different profiles and requirements. An Administrator will have to be strategic with balancing these needs for a suitable SLA policy.

## Raising cases to Cato Support

If following this playbook has not resolved the issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). In order to get the most helpful response to a request, an administrator should provide results of troubleshooting steps taken throughout the use of this playbook. Including for example:

- Relevant filters to draw attention to specific events.
- Results of WebUI tests.
- Network Analysis findings.
- SLA configuration requirements.
