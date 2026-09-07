---
title: "What are the Cato Bandwidth Management Profiles"
slug: "what-are-the-cato-bandwidth-management-profiles"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/what-are-the-cato-bandwidth-management-profiles"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What are the Cato Bandwidth Management Profiles

This article provides background information about using QoS and Bandwidth Management profiles with network rules in your account.

## Overview of QoS and Bandwidth Management with the Cato Cloud

You can define and manage your bandwidth from a centralized location with as much granularity as required by:

- Configuring your organization's QoS policies through Bandwidth Management profiles. These profiles define priorities and limit upstream/downstream bandwidth to either a fixed speed or a percentage of the total bandwidth.
- Analyzing QoS in real-time or viewing historical data.

For more information about working with Bandwidth Management profiles, see:

- [Configuring Bandwidth Management Profiles](/v1/docs/configuring-bandwidth-management-profiles)
- [Overriding Bandwidth Management Profiles for a Site](/v1/docs/overriding-bandwidth-management-profiles-for-a-site)

## Overview of Policy-Based Routing (PBR)

You can define and manage PBR from a centralized location with as much granularity as required.

The PBR comprises the following main functions:

- Transport Selection: you can define through which transport (such as Cato or Alt. WAN) to transfer specific traffic. For example, if a site has Alt. WAN (MPLS) as well as an internet link, you can define a PBR where certain WAN traffic is directed over MPLS while the remaining traffic and internet is directed over the Cato Socket.
- NIC Selection: you can define through which NIC to transfer specific traffic. For example, if a site has multiple internet lines, you can define a PBR where one NIC is used for all business apps, while another NIC is used for non-business apps.

> [!NOTE]
> Note:
> 
> NIC selection is only applicable assuming the selected transport is Cato.
- Egressing or NAT from the Cato Socket: you can select via which PoP(s) or IP(s) should specific traffic be egressed from the Cato Socket, as explained in the following examples:
  - Egressing from a specific location (**Route via**): If you want to optimize specific internet traffic to egress from the Cato Socket closer to the target location, or to egress specific locations for localization purposes.
  - **NAT** with a specific IP: If you need to egress with a specific IP to gain secure access to applicable SaaS applications (for example, egressing Salesforce traffic with a specific IP from Cato Socket and populating that IP in Salesforce's whitelist increases overall security, and forces users to access Salesforce from the Cato Socket, benefiting from the Cato Socket Security Services Stack).

> [!NOTE]
> Note:
> 
> A specific IP address is associated with your account only, and is not be shared with any other Cato Networks customers. To egress with a specific IP, you must first get an IP allocation form Cato.

### How Does Cato’s PBR Work?

Cato’s PBR is closely associated with Cato’s QoS engine and Network Rules.

The QoS engine dynamically monitors each link's quality matrix (congestion, packet loss, jitter, latency).

When defining Network Rules, you can define the PBR's functionality as follows:

- Explicit transport/NIC selection - although Cato Socket is the default transport, you can select a different transport as primary, and select which secondary transport to use if the primary transport is unavailable (due to a fault or QoS engine quality matrix).

> [!NOTE]
> Note:
> 
> If you select explicit transports/NICs, the QoS engine monitors packet loss, jitter and latency. if congestion occurs, packets are dropped.
- Automatic - you can define network rules to dynamically select the best available link over which to send the traffic, based on Cato Socket's QoS engine link quality matrix. If a link’s quality doesn’t meet these the quality thresholds, it is considered as unavailable and the other link will be used.

> [!NOTE]
> Note:
> 
> If you select automatic transports, the QoS engine monitors congestion, packet loss, jitter and latency.
- None - you can set the secondary transport/NIC to none. For example, at a site with two links, one is used for business traffic, while the other for non-business traffic. If the non-business traffic link fails, you do not necessarily want to transfer this traffic to the business link.

![bwEditConfig.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247992844701.png)

You define your PBR when you configure the actions for a Network Rule, as described in [Configuring Network Rules](/v1/docs/configuring-network-rules).

You can monitor the PBR in real-time or view historical data, presenting you with a better understanding of how your traffic is being routed and enabling you to adjust the PBR accordingly.

## How Does the Cato QoS Engine Work?

When you configure a site, you also define the upstream/downstream bandwidth capacity for the site. In this way, the Cato Socket is aware of the capacity of each link, and can further leverage it in the QoS engine. As part of the QoS engine, Cato continuously monitors each link’s quality matrix based on these factors: congestion, packet loss, jitter, and latency.

The Socket dynamically decides how to send the traffic over the best available link according to the configuration in the PBR.

You can also configure Health Rules to set alerts based on the link quality thresholds that you can configure in **Network > Link Health Rules**.

In addition, Cato uses Weighted Random Early Drop (WRED). Prior to discarding a packet (due to lack of capacity), Cato buffers a minimum threshold of 250 packets and an upper threshold of 500 packets. You can use analytics to drill-down and get more information about discarded packets.

For each Bandwidth Management profile, you assign a number defining its priority. When you assign these prioritized profiles to the Network Rules, you effectively implement traffic prioritization which includes, when links are congested, throttling of traffic as per defined limits in the Bandwidth Management profile.

For more information on Network Rules, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

Cato provides a set of predefined priorities assigned to the predefined network rules as follows:

| Priority | Predefined Purpose |
| --- | --- |
| P10 | Prioritizing Voice & Video traffic across WAN and Internet. |
| P20 | Prioritizing RDP traffic across WAN and Internet. |
| P30 | Prioritizing SMB traffic across WAN and Internet. |
| P40 | Prioritizing the rest of the WAN traffic. |
| Default | Prioritizing the rest of the Internet traffic and used as default priority when a Networking Rule doesn’t have a QoS context (meaning no specific priority should be assigned to it) |
