---
title: "Socket Best Practice: VLANs vs. Routed Ranges"
slug: "socket-best-practice-vlans-vs-routed-ranges"
tags: ["Best Practices", "Networking", "Sockets"]
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/socket-best-practice-vlans-vs-routed-ranges"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Best Practice: VLANs vs. Routed Ranges

The following article covers the case where the Cato Socket used both for WAN connectivity and Firewall-as-a-service. In such case, security is a major goal of the deployment. This article is less relevant for situations where Cato Networks used primary for WAN/ global connectivity.

## Introduction

Until recently it was quite common to have a topology of internal L3 switch managing all internal VLANs. The backbone switch would have L3 interface for each VLAN acting as the default gateway. Routing was done internally on the switch, i.e., traffic between VLANs would stay inside the switch. Only traffic to the Internet or WAN would go up to the Firewall. See example below:

![L3Switch.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248124189469.png)

In the topology above, routing between internal VLANs is done on the L3 backbone switch. Only Internet traffic would go up to the Firewall for L4 inspection. It's rare to have of ACL (Access Lists) between the internal VLANs due to the following reasons:

1. Hard to manage - ACLs must be created using CLI, very cumbersome.
2. Review blocked traffic - traffic logs could be mainly reviewed using CLI commands and not with clear GUIs like Firewalls have these days.
3. Enabling L3 ACL would consume CPU power of the switch.
4. Very complicated to have an isolated VLAN that has no corporate access.

Eventually, most networks had unlimited routing and access between internal VLANs. Virus outbreak in one of the VLANs would be very hard (nearly impossible) to contain.

## Moving L3 to a Security Device

As cyber attacks keeps growing and malware grow larger in the wild, network designs began moving to a L3 routing on a security device - Firewall. Similar to the topology above, yet with one main difference - all switches act as a L2 device, while the Firewall device would perform L3 routing between the internal VLANs. See example below:

![L2_Switch_and_Firewall_inter-VLAN_routing.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248139313693.png)

In the topology above, the Firewall acts as Router-on-a-stick. Traffic between VLAN 10 PCs and VLAN 20 PCs would go through the Firewall.

Naturally, this approach provides much more control and security. It is very easy to isolate an infected VLAN from the network. It's also straightforward to have a VLAN with Internet access only (for example guests network).

## Cato Socket: VLANs vs. Routed Ranges

Cato Socket supports (mainly) two configurations:

- VLAN - similar to L3 routing on the Firewall, the Socket has L3 interface for each VLAN and acts like a default gateway.
- Routed range - static route. Used in the first topology in which the Socket has routes via the L3 switch to the internal VLANs.

Although both network designs are supported by Cato, the best practice for a new design would be VLANs. As long as there are no limitations or special requirements, best way to configure a Socket would be similar to L3 on the Firewall topology. See example below:

![L3_switch_catoCloud.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248109738909.png)

## Advantages of having VLANs on the Socket

1. Management - the Socket can act as default gateway for each VLAN + provide DHCP range for each VLAN. All is managed from the Cato Management Application.
2. Control - in case of a virus outbreak in one of the VLANs, this VLAN can be isolated immediately and easily either by a WAN Firewall rule or by even deleting the default gateway for that VLAN.
3. Security - when there's a need create a completely isolated VLAN like Wifi for guests, the Socket can easily block WAN/ corporate access for that network and allow only Internet access.

- Pay attention that by design all WAN traffic goes to the PoP. That included both site-to-site and inter-VLAN traffic. Meaning, that traffic between VLANs in the same office will not be routed in the Socket by default. This point is covered in the next section.

## Common Concerns and Advised Resolutions for L3 Routing on the Socket

1. Create and manage security rules between internal VLANs - it's actually not the most important thing to have hundreds of unique rules allowing inter-VLAN traffic. The more important ability is to have the immediate way to isolate an infected VLAN. Effective security defence will be provided by the Cato's advanced security services like Anti-Malware and IPS. Anti-Malware and IPS will provide genuine L7 inspection for both internal and external traffic.
2. Performance - when it comes to shifting inter-VLAN routing to a security device, immediate concern that arises is the bandwidth capacity. Legacy L3 switches lacked the security, but clearly had high performance. To tackle this point we would like to provide some facts:
  - Besides Data Centers, common offices have few VLANs like Users, Printers and Wifi for guests. When you think about it, there's no actual reason to allow traffic between those VLANs. They mainly need access to corporate resources in the Data Center, or even just access to cloud services like Office 365, Skype and Salesforce.
  - Small volume traffic like users to printers, can work perfectly going to the PoP and back from the Socket. The users won't notice any difference when a printing job has additional 20ms delay, but the IT Admins will have much better security and control.
  - If high-speed 1Gbps routing is still a must, the Cato Socket supports Local Routing capability. Local Routing allows in-Socket routing, i.e., traffic between a pair of VLANs will remain in the Socket. This kind of configuration bypasses Cato's L7 security services (Anti-Malware and IPS). Nevertheless, if there's any infected work station, once it will communicate with an external C&C or malicious proxy, it will be detected and alerted.
