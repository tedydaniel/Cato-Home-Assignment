---
title: "Explaining the Cato TCP Acceleration and Best Practices"
slug: "explaining-the-cato-tcp-acceleration-and-best-practices"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/explaining-the-cato-tcp-acceleration-and-best-practices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Explaining the Cato TCP Acceleration and Best Practices

Some TCP connections, especially long-distance ones, often experience high latency that have a negative impact on the user experience. Cato Networks’ TCP acceleration feature accelerates the TCP connections over the WAN and improves the network efficiency and speed for TCP traffic.

This article explains how Cato implements TCP acceleration and lists some best practices to optimize TCP acceleration for specific applications that are based on TCP traffic.

## Explaining TCP Acceleration

Cato accomplishes TCP acceleration by designating the Cato PoPs to act as an intermediate proxy server between the client and the destination server. The proxy eliminates a long-distance connection and instead splits it into three short ones. The advantage is that instead of maintaining a long-distance connection, the Socket maintains a short connection to the closest PoP. The traffic between the PoPs is transferred over the Cato Cloud private backbone that guarantees the cloud speed and low latency. The PoP that is the closest to the destination, sends the traffic to the server.

If there is packet loss, the PoPs are responsible for retransmitting packets, and this allows a quick reaction and reduces the response time. This technique improves TCP performance and reduces the recovery time if a tunnel disconnects. Each short connection has a shorter round-trip time (RTT) per packet as compared to one long-distance connection. The short connections improve performance and guarantee faster data delivery to the destination. A long-distance connection with a high RTT means that packets are traveling for a longer time until they reach the destination. The longer travel time and slow connections can create a poor user experience.

The following diagram shows a connection from client to server where PoP A and PoP B act as proxy servers:

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29278863821469.png)

The proxy splits the long-distance connection between the client and the server to three short connections:

1. First connection is from the Socket to PoP A.
2. Second connection is from PoP A to PoP B, over the Cato Cloud.
3. The third connection is from PoP B to the destination server.

Each PoP maintains its own TCP stack and reduces TCP packets retransmissions of the entire window in the case of packet loss. In some scenarios, for example, with TLS traffic and TLS inspection is enabled or an egress network rule that is evaluated, when the PoP receives SYN messages from the client, it quickly returns ACK responses to the client, instead of waiting for the response from the server. Meanwhile, the Socket continues to send the TCP traffic which makes the connection faster. The PoP allocates a larger TCP stack window size according to the following formula: window size = RTT * bandwidth. For example, for connections with an RTT of 200MS and bandwidth of 20MBS, the TCP window size is 4 MB (0.2 Sec * 20 MB). However, there are other scenarios where the PoP waits for a response from the server before sending ACK responses to the client.

**Note:** TCP acceleration is not supported for Alternative-WAN and Off-Cloud transports.

### TCP Acceleration vs TCP Proxy

From the PoP’s point of view, the behavior explained in the previous section is seen as TCP proxy. TCP Acceleration is the feature that can be enabled or disabled in the Cato Management Application, whereas TCP Proxy is the actual TCP connection split mechanism that takes place on the PoPs. TCP Acceleration triggers TCP proxy when it’s enabled. We make this distinction because in some cases, TCP proxy may still occur even if TCP acceleration is disabled in the Cato Management Application.

### TCP Proxy for WAN Traffic

For WAN traffic over the Cato Cloud, two TCP proxy modes are available:

- Full WAN TCP proxy
- Preserving original WAN TCP negotiation and delaying the TCP proxy

For WAN traffic that uses **Full WAN TCP Proxy** mode, the TCP proxy begins immediately on the first SYN packets for each connection. This mode enforces TCP Proxy on the first SYN when TCP acceleration is enabled in the network rule, and the rule is a [simple rule](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices#working-with-simple-and-complex-network-rules). There are some situations where this mode is not an optimal setting, for example SIP trunk and Off-Cloud traffic.

With **Preserving original WAN TCP negotiation and delaying the TCP Proxy** mode, the TCP proxy is delayed and begins only after the TCP handshake is completed. We recommend this mode for Alt WAN traffic, and Off-Cloud failover, since the PoP preserves the same TCP sequence over the tunnel. However, when using this mode the TCP session parameters such as Window Scaling, MSS, and others, are already set before the TCP proxy starts, and may have different TCP parameters from the Cato PoP.

Starting in November 2023, **Full WAN TCP Proxy** is the default mode for new accounts. For accounts that were created before this date, the **Full WAN TCP Proxy** mode is disabled by default.

You can change the WAN TCP Proxy mode in the **Advanced Configuration** page for both [account-level](/v1/docs/working-with-advanced-configuration-for-the-account) and [site-level](/v1/docs/advanced-configurations-for-a-site).

### Enforcing TCP Proxy

The following sections describe circumstances where TCP Proxy is automatically enabled and overrides the **Active TCP Acceleration** setting.

#### Using an Egress IP in a Network Rule

When choosing an egress IP or location in a network rule, the PoPs act as proxy servers for the connection, and Cato automatically activates the TCP proxy. You can’t disable the TCP acceleration for egress rules in the Cato Management Application. The following screenshot shows an egress network rule where the **Active TCP Acceleration** option is greyed out (Network > Network Rules > Edit Rule).

![TCP_Acceleration.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29278863941277.png)

For more about egress rules, see [How to Configure an Egress Rule](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic).

#### Working with Simple and Complex Network Rules

To understand TCP proxy behavior based on network rule configuration, it's essential to distinguish between simple and complex network rules.

A complex network rule is one that the Socket itself cannot evaluate. In such a case, the Socket needs to forward the traffic to the PoP to choose the correct network rule, which in turn enables TCP Proxy. These are the definitions for simple and complex network rules:

- A complex rule contains one or more of the following objects in the App/Category setting: Applications, Application Categories, Services, Custom Applications, or Domain/FQDN
- A simple rule can be defined only with Port Ranges, Custom Services, or ANY configured in the App/Category setting. Otherwise the rule is a complex rule

Disabling TCP Acceleration in a network rule will not disable TCP proxy when:

- A complex network rule exists above the network rule with TCP Acceleration disabled
- The network rule that has TCP Acceleration disabled is itself a complex rule

The example below shows network rule #2 with TCP Acceleration disabled. Because rule #1 is a complex rule containing Applications, traffic matching network rule #2 will have TCP proxy applied to it. In order to disable TCP proxy in this scenario, network rule #2 must be placed above the complex rule (rule #1).

![tcp_complex_networkRule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29278872686365.png)

### Recovering from PoP Disconnection

In the case that the tunnel from the Socket to the PoP disconnects, the Socket then tries to reconnect to the same PoP. If the Socket manages to reconnect, the connection is recovered since the PoP keeps the tunnel state. In the case that the Socket can’t connect to the same PoP and TCP acceleration is enabled for a network rule, the state of existing connections is lost. Since the PoP acts as the TCP proxy server when the Socket loses connectivity to the PoP, the state of the connection is lost, and the client must initiate a new connection. Therefore, we recommend enabling TCP proxy for applications that can survive momentary disconnections such as web applications and file sharing.

## Best Practices for TCP Acceleration

This section describes best practices for when to enable TCP acceleration for specific types of applications.

### Enabling TCP Acceleration for Web Applications

Commonly, web applications are clientless and use a web browser to connect to a server. Cato’s TCP acceleration engine significantly improves the performance of this traffic. We recommend that you enable TCP acceleration for network rules with web applications.

### Enabling TCP Acceleration for File Sharing Applications

Files sharing applications, such as SMB, can suffer from network latency or retransmissions in the case of packet loss. If you use file sharing between computers in your network (ie. SMB protocol for resource sharing), Cato’s TCP acceleration can significantly improve the file transfer speed. We recommend that you enable the TCP acceleration for these applications’ network rules.

### Disabling TCP Acceleration for Sensitive Applications

There are some applications that are sensitive to network disconnections, and it is difficult for them to recover after a disconnect. These applications are commonly desktop legacy applications in a client-server architecture. After a disconnection, they force the client to initiate a new connection and then lose the connection state. For example, for Citrix clients that already use an optimized protocol, we recommend that you disable the TCP acceleration for network rules with this traffic.

## TCP Proxy and TLS Inspection

The TLS inspection feature decrypts HTTPS traffic for security features such as Anti-Malware and IPS. This feature uses the PoPs as proxy servers to inspect the traffic for malicious files and threats. When you enable TLS Inspection for your account, Cato activates TCP proxy for all TLS traffic. For more about TLS inspection, see [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account).

Enabling or disabling TCP Acceleration is not related to enabling TLS Inspection.

## Fine Tuning TCP Acceleration for Windows OS

This section discusses how to optimize the TCP setting for Windows computers to improve the TCP acceleration for your network rules.

### Enabling TCP Window Scaling Option

Some Windows operating systems are configured to use a default window size of 64KB. This window size is limited and can cause performance issues and latency. Cato PoPs allocate a TCP stack that is larger than the default window size for more efficient data transfer. Therefore, we highly recommend that you enable the TCP window scaling option in your Windows computers.

**Note:** Usually the TCP window scaling option is enabled by default.

### Enabling TCP Timestamp Option

The default setting for Windows operating systems doesn’t support the TCP timestamp option. Enable the TCP timestamp option to improve the packet RTT measurements and help to identify packet loss. This option also assists the TCP stack to adjust the retransmission timer in case of packet loss. We recommend enabling the TCP timestamp in your Windows computers.
