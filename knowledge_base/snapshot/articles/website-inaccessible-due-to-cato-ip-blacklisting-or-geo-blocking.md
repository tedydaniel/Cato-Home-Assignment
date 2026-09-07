---
title: "Website Inaccessible due to Cato IP Blacklisting or Geo-Blocking"
slug: "website-inaccessible-due-to-cato-ip-blacklisting-or-geo-blocking"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/website-inaccessible-due-to-cato-ip-blacklisting-or-geo-blocking"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Website Inaccessible due to Cato IP Blacklisting or Geo-Blocking

## Issue

When attempting to access a specific website through the Cato Cloud, the page fails to load and eventually times out. However, the same site is accessible when bypassing the Cato Cloud.

This issue can arise due to two primary reasons:

#### 1. Cato IP blacklisted by the Website

Certain websites, such as Hulu, ESPN, or government sites, may not be accessible via Cato due to internal restrictions or categorization that block the Cato public IP address.

Although Cato does not have control over this behavior, there are a few ways to troubleshoot and overcome this issue.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10344626672029.png)

#### 2. Geo-blocked Websites

Some governments and other organizations may only allow access to their websites from IP addresses registered in their own country or jurisdiction. This is known as geo-blocking.

Cato Networks has PoPs deployed all over the world, but the PoP you connect to won't necessarily be in the same country/state you live in. If that's the case, when you visit a website hosted within your country/state, the site would see the connection coming from an IP address registered *outside* your jurisdiction, the external IP address of the PoP.

If the website is using geo-blocking to restrict access to in-country/state IP addresses only, the website will fail to load. In some cases you may see a block page from the web server, but most of the time the website will just time out and browser error will be displayed like the ones below.

Chrome:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19589807066269.png)

Firefox:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19589807086365.png)

Edge:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19589823237405.png)

## Troubleshooting

- Run a local packet capture either on the PC or via [the socket](/v1/docs/how-to-capture-traffic-on-a-socket) to confirm that there are no replies from the website server. You will only see SYN packets going out or a complete 3-way handshake with no application-layer exchange. A RST packet may also come from the website server which would be a clear indication that the Cato IP is being blocked.
- It's also possible that parts of the website won't fully load which may indicate a redirection to another server that blocks Cato IP ranges. Collect a HAR file via the browser's [developer tool](/v1/docs/how-to-collect-har-data) for further analysis.

## Solution

- Contact the Website Administrator and inquire about the reason why Cato IP ranges are being blocked. Request the admin to whitelist the IP ranges listed in [this guide](/v1/docs/production-pop-guide) according to the PoP location.
- If the affected users were determined to be from a specific location, apply a basic network rule, select the [Route via](/v1/docs/configuring-network-rules) routing method, and pick a different location that will have access to the website.

If the above does not resolve the issue, continue with the following steps based on where the affected user is located:

#### Cato SDP Client

- For blacklisted Cato IPs: You can enable [backhaul via a socket](/v1/docs/backhauling-traffic-via-a-socket-s-wan-interface-ip-address) in the network rule and select a site that has access to the website. The pop will still perform security scans and will then route SDP traffic to the selected site so the traffic would egress via the socket's WAN port.
- For Geo-blocked websites: You should be able to access the website while in your own country/state by disconnecting from the VPN client. This will not be possible if [Always-On](/v1/docs/protecting-users-with-always-on-security) is enforced on the client.
- Alternatively, you can create a [split tunnel configuration](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) and exempt the IP address(es) of the website. Any traffic to the exempted IP addresses will not be sent to Cato.

#### Socket

- Define the website in a network rule as a Domain object or Application and enable [backhaul hairpinning](/v1/docs/hairpinning-traffic-to-the-same-site). This allows the traffic that matches the network rule to go to the pop for security scans. The traffic is then routed back to the defined site so the traffic would egress via the local socket's WAN port. Be sure to follow [FW best practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies#best-practices-for-cato-internet-firewall-policy) and block the QUIC protocol to accurately identify the Website/Application.
- As a last resort, you can perform [local bypass](/v1/docs/bypassing-the-cato-cloud-site-level-policy) so the traffic goes out directly via the socket's WAN port to the target website. This is not an ideal solution as it bypasses the Cato PoP infrastructure and no security is applied to this traffic.

#### IPSec Site Connected to Cato

- Define the website in a network rule as a Domain object or Application and enable [backhaul via IPSec](/v1/docs/backhauling-traffic-via-an-ipsec-site). This allows the traffic that matches the network rule to go to the pop for security scans. The traffic is then routed back to the IPSec site so the traffic would egress via the local firewall's WAN port. Routing configuration on the firewall is necessary for this option to work. Be sure to follow [FW best practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies#best-practices-for-cato-internet-firewall-policy) and block the QUIC protocol to accurately identify the Website/Application.
- As a last resort, you can change the routing policy on the local IPsec device so that traffic to the website's IP address(es) will not route through the Cato IPsec tunnel. This is not an ideal solution as it bypasses the Cato PoP infrastructure and no security is applied to this traffic.
