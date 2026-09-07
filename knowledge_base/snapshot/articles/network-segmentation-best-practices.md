---
title: "Network Segmentation - Best Practices"
slug: "network-segmentation-best-practices"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/network-segmentation-best-practices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Segmentation - Best Practices

## Overview

Network segmentation helps to improve the security and makes it easier to manage by dividing the corporate network into smaller network segments. This article focuses on using the Cato Management Application to use the VLAN network segments and minimize the impact of a possible network intrusion. If there is a network intrusion, the infected VLAN is isolated and can’t spread to the entire network. VLANs also can provide granular access control, you can create firewall rules to define access control based on the users role in the organization.

## Network Segmentation with Cato Networks

The Cato Management Application lets you easily define the VLANs for a site that uses the Cato Socket. Use the **Network** section for a site to define the network segments with the **Range Type** of **VLAN**. See the following screenshot for an example of VLAN network segments (**Network > Sites > {Site Name} > Site Configuration > Networks**):

![Sites_Network.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248147518749.png)

You can then use these network segments to increase security for the site. For example, you can create a separate VLAN for the corporate Finance department and use it in a WAN firewall rule. Since traffic between VLANs is routed over the Cato Cloud, it's possible that there’s an impact on the network performance for this traffic. This is true even if the VLANs are in the same physical location.

### Segmenting Servers to Increase Security

Servers that contain essential and sensitive data often require extra layers of security. You can isolate these servers in a separate VLAN and limit the access to these servers. For example, you can use a separate VLAN for the database servers in your corporate headquarters.

On the other hand, application servers often have inbound access from the public Internet and can be a potential security risk. We recommend that you assign these servers to a separate VLAN and prevent attackers from accessing internal and sensitive servers. You can use this VLAN as a DMZ (demilitarized zone) for publicly accessed servers.

### Using VLANs to Protect Servers and Workstations

Corporate workstations and servers can be a security risk for your network because if a workstation is compromised, then it can quickly spread throughout the entire network. However, when the workstations are in a separate VLAN, you can isolate the VLAN and block connectivity to the network. To allow communication between the networks, you must configure a gateway IP address for each of the VLAN networks. The following screenshot shows an example of separate VLANs for servers and workstations:

![servers_and_work.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248147604637.png)

Create a WAN firewall rule that allows connectivity between these VLANs. If one of the workstations in your network becomes infected, you can easily disable this rule and prevent the infection from spreading to the servers. After you remediate the infected workstations, you can enable the rule again to allow connectivity between the workstations and application server.

### Separating Networks for Different Types of Users

Network segmentation lets you define different access levels for the different groups of users in your organization. For example, define separate VLANs for management, regular users, and guests.

If you want to provide WiFi or network access for guests, this is can be a potential security risk. Segment the guest network in a separate VLAN which only allows access to the Internet, and they can’t access the internal resources. The following screenshot shows a VLAN for the guest WiFi users:

![vlans1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248162183837.png)

Then create a rule in the Internet firewall that allows this VLAN to access the Internet. The following screenshot shows an Internet firewall rule that allows the Guest WiFi VLAN to access the Internet:

![GuestWiFi_Internet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248177418525.png)

### Restricting Traffic with Security Risks

In addition to segmenting the network to improve network security, you can also restrict the traffic types that are potential security risks. For example, RDP (remote desktop) and SMB (file sharing) protocols are often used by intruders to gain access to sensitive information or to spread ransomware that causes damage to corporate data.

We recommend that you configure the WAN firewall to limit access to these protocols by default and only allowing this traffic when necessary. For more about configuring WAN firewall rules and best practices, see [Internet and WAN Firewall Policies Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies).
