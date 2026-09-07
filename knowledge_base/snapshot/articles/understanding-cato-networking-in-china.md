---
title: "Understanding Cato Networking in China"
slug: "understanding-cato-networking-in-china"
updated: 2026-07-28T09:15:46Z
published: 2026-07-28T09:15:46Z
canonical: "knowledge.catonetworks.com/understanding-cato-networking-in-china"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Cato Networking in China

This article explains how the Cato Cloud platform works in China, including meeting the China government regulations and restrictions.

Cato account licenses use one of two models. This article applies to the Enforcement Model only and is not relevant to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027). Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

## Overview

All Internet traffic in China is inspected by the government and backhauled through a local gateway. Cato follows all regulations in China, and the Cato SASE service is fully available in China just like in other regions.

**Note:** Since China restricts certain websites from being accessed from within China, egressing certain traffic to bypass the Great Firewall of China to a non-China Cato POP violates the Cato [MSA (Master Service Agreement)](https://www.catonetworks.com/msa/). Refer to the Cato MSA, section 5.2 for questions regarding restrictions in China.

Cato provides optimal user experience within China through its PoPs and allows globally distributed companies with offices in China to have a consistent, secure connection across the Cato backbone. There are multiple Cato PoPs in China, for example, Beijing, Shanghai, Shenzhen, and Urumqi. These PoPs communicate with the Cato Cloud through Hong Kong. Meaning, that Chinese PoPs establish a full mesh between them inside of China, and communication with other PoPs is done via Hong Kong and vice versa.

The Chinese government restricts access to some sites and resources outside of China, which requires foreign companies to adapt to these regulations.

**Note:** The Chinese government can change its restrictions and prohibit access to an application or website at any time. If traffic is blocked, check [this list](https://en.wikipedia.org/wiki/List_of_websites_blocked_in_mainland_China) to see if the destination is unavailable in China.

### Limitations for Sites or Remote Users Located in China

- RPF is not supported in China
- Cato Enterprise Browser, Browser Extension, and Browser Access are not supported in China
- RBI is not supported in China. For more information, see [Configuring the RBI Service for Browsing Sessions](/v1/docs/configuring-the-rbi-service-for-browsing-sessions)

## Socket Maintenance in China

Sockets that are located in China download the Socket upgrade file from a Server in Ali Cloud which improves the file download time and reduces latency, and improves the success rate for Socket upgrades.

## DNS in China

Within China, the most commonly used DNS services are not available. Therefore, Cato uses an internal mechanism to determine the best available DNS server, and the Cato DNS server,10.254.254.1, acts as a proxy.

You should configure your WAN interfaces to use the DNS servers provided by your local ISP, or the public DNS servers available in China, such as 114.114.114.114 or 114.114.115.115.

## Last Mile Monitoring in China

Last mile monitoring predefined web addresses are China web services such as QQ.com, baidu.com, and weibo.com (this is configurable under **Network > Last Mile Monitoring Probes**).

## Egressing Traffic in China

By default, Internet traffic in China egresses from the China PoP you're connected to, and through the local gateway and then to the destination. Meaning that if you attempt to access restricted sites, the Cato PoP would allow the traffic to pass, and then it would be blocked due to local regulations, the Great Firewall of China.

## UDP Port 1337 for China Socket and Client DTLS Traffic

Cato recommends, as a best practice, configuring the alternate UDP port for accounts with Socket sites and Client users located in China. DTLS tunnels using UDP port 443 can experience connectivity issues such as packet loss. Configure UDP port 1337 as a preferred DTLS port for Socket and Client traffic to improve connectivity. For more information, see [Understanding Cato Networking in China](/v1/docs/understanding-cato-networking-in-china).

## Licensing

When purchasing a license for a site in China, customers must determine what percentage of the license bandwidth to allocate to regional traffic and what percentage to global traffic.

- Regional traffic is any traffic sent within the China region, for example, from a site in Shenzhen to a site in Beijing
- Global traffic is any traffic sent outside the region, for example, from a site in Shenzhen to a site in Europe.

> [!NOTE]
> Note:
> 
> Global traffic is inherently more expensive than regional traffic. Make sure to allocate both according to your needs.

When you configure a site in the Cato Management Application, you must assign a license to that site. The site details show the license details that combine the regional and global licenses you purchased.

![china_license.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248186203165.png)

The value that you need to enter in Last-mile Bandwidth for the site configuration is the total regional and global bandwidth for the site. If, for example, you purchased 100 Mbps, 70% for regional and 30% for global, then you need to configure **100 Mbps** for a site located in Shenzhen.

![Last-mile_Bandwidth.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248161693469.png)

## QoS for China Sites

QoS in Cato is controlled by two aspects:

- Bandwidth Management
- Network Rules

For more information, see [Network Rules and QoS](/v1/docs/network-rules-qos).

As the Bandwidth Management mechanism is not aware of any licensing limitations, when you create your profiles, you should take into account what your license allows.

If, for example, you purchased 100 Mbps in total bandwidth, with 70% regional and 30% global, when creating your Bandwidth Management profiles, set limits that align with those values. As a best practice, use percentages and not hard limits of bandwidth values to avoid allocating more than you are allowed to use.

### Video Conferencing using Percentage-based Profiles

Your company has sites in Shenzhen, Shanghai, Beijing, and Europe. You want to ensure that when they have video conferencing (VC) meetings, they are able to communicate without any issues.

You can create the following profile to allocate at least 15% of your resources to P15 traffic.

![Bandwidth_Profiles.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248143233181.png)

You can then create a Network Rule that uses the P15 profile for VC traffic. When the traffic is between the offices within China, for example Shanghai and Beijing, the 15% of the allocated bandwidth will be based on your regional license. If Shenzhen is VCing with the Europe site, it will 15% of the global license. However, since you used percentages and not hard Mbps limits, you do not run the risk of going over your license allowance.

### Video Conferencing using Bandwidth-Based Profiles

Based on the scenario we described above, you can also create two different profiles, one for regional VC and one for global VC, that use hard bandwidth limits. For regional video conferencing, you have a profile that allocates 10 Mbps. And for regional video conferencing a profile that allocates 5 Mbps.

![Bandwidth_Profiles-Mbps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248186414493.png)

In your Network Rules, you then create two separate rules to implement each of the profiles depending on the destination of the VC traffic.

![china_network-rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248161969565.png)
