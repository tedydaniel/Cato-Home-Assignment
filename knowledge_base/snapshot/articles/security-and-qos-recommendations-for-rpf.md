---
title: "Security and QoS Recommendations for RPF"
slug: "security-and-qos-recommendations-for-rpf"
updated: 2026-07-05T09:24:58Z
published: 2026-07-05T09:24:58Z
canonical: "knowledge.catonetworks.com/security-and-qos-recommendations-for-rpf"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Security and QoS Recommendations for RPF

Remote Port Forwarding (RPF) helps to open inbound connections from the Internet. It directs TCP/UDP traffic from the Internet to specific internal resources in your organization through the Cato Cloud. Remote Port Forwarding allows the defined external IP addresses to access the internal resources.

Use the Cato Management Application (Network > Remote Port Forwarding) to configure remote port forwarding rules for your account. When you create a remote port forwarding rule, select to allocate an IP address for this rule. And then define the internal IP address and port of the resource, and the allowed remote IPs. You can also use the **Tracking** option to generate email notifications for forwarded traffic.

Since these rules allow inbound traffic from the Internet, we strongly recommend that you configure an IP address (or IP range) for the **Allowed Remote IPs**. Using the setting **0.0.0.0/0** allows ANY inbound traffic and is a significant security risk. Therefore, if there is a requirement to expose a resource, Cato recommends deploying a [DDoS service](/v1/docs/how-to-integrate-third-party-ddos-services-for-internet-facing-rpf-traffic) in front of that resource.

The following screenshot shows an example of a rule that enables connectivity for all inbound traffic to an FTP server:

![ftp1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24448367633693.png)

This screenshot shows the same rule that has been made secure and only allows access from the IP address 66.249.66.61 to the FTP server:

![ftp2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24448343391133.png)

Cato Networks lets you manage the network bandwidth and QoS by assigning priority for different types of traffic. If you configure a Remote Port Forwarding (RPF) for your account, the RPF traffic is assigned automatically with the default QoS priority which is the lowest - 255. The reason that RPF is assigned the default priority is to let you easily assign higher priority to other types of traffic. You can't change the default priority for the RPF rule. For more details about bandwidth Management, see [What are the Cato Bandwidth Management Profiles](/v1/docs/what-are-the-cato-bandwidth-management-profiles).

For more information about remote port forwarding, see [Configuring Remote Port Forwarding for the Account](/v1/docs/configuring-remote-port-forwarding-for-the-account).

> [!NOTE]
> Note:
> 
> Remote Port Forwarding isn't supported for PoPs that are located in China. You can choose to use allocated IPs in China to egress traffic in network rules or for IPsec sites.
