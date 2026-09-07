---
title: "Including and Excluding Traffic for the Split Tunnel Policy"
slug: "including-and-excluding-traffic-for-the-split-tunnel-policy"
updated: 2026-07-12T12:39:56Z
published: 2026-07-12T12:39:56Z
canonical: "knowledge.catonetworks.com/including-and-excluding-traffic-for-the-split-tunnel-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Including and Excluding Traffic for the Split Tunnel Policy

For more information about routing traffic for remote users, see [Routing with the Cato Client (Split Tunnel Policy)](/v1/docs/routing-with-the-cato-client-split-tunnel-policy).

## Overview

For remote users connected with the Cato Client, the Split Tunnel policy controls which traffic is routed through the Cato Cloud and which traffic bypasses the tunnel. Use include and exclude rules to define the specific destinations that are routed through the Client tunnel.

When users are behind a Cato site, the Split Tunnel policy only applies if they are connected with the Client and are not in Office Mode. In Office Mode, users are not treated as remote users, and the Split Tunnel policy does not apply to their traffic.

## Destination-Based Split Tunnel Routing

The Split Tunnel policy supports these routing options:

- Route all traffic through the Cato Cloud and exclude specific destinations (such as trusted SaaS services)
- Route most traffic directly to the Internet and include only selected destinations for inspection

Destination-based rules support applications, [IP ranges](/v1/docs/using-ip-ranges-in-policies), domains, and FQDNs, giving you precise control over which traffic is secured by the Cato Cloud and which traffic bypasses the tunnel.

### Domains and FQDN as Destinations

When you use the domain and FQDN to define traffic for remote users connected with the Client, that is included or excluded from the Cato Cloud:

- **Domain** - Use Domain objects to match a domain and all its subdomains (for example, `example.com` matches `app.example.com` and `login.example.com`)
- **FQDN** - Use FQDN objects to target specific hosts (for example, only `app.example.com`)

### Apps as Destinations

For destination-based Split Tunnel rules with **All Ports and Protocols**, you can use predefined applications as destinations. There are FQDN-based applications and IP-based applications.

For FQDN-based applications, Cato dynamically maintains the application domains and updates the routing definitions when those domains change. This reduces policy maintenance and lets the Cato Client route matching application traffic through the tunnel to the Cato Cloud or directly to the Internet, according to the Include or Exclude rule. The apps indicate which are FQDN-based and which are IP-based only.

You can also choose to include FQDNs in a rule with OR based logic, if necessary.

### Prerequisites

- DNS Relay must be enabled on the devices
- Supported from Windows Client v6.2 or higher
  - Recommended for Windows Client v6.4 and higher (see below [Known Limitation](/v1/docs/including-and-excluding-traffic-for-the-split-tunnel-policy#h_01KTTW64AWQBWSPEPMSJJ2ZQY3))
- Apps as Destination is supported from Windows Client v6.4 or higher

## Customize which Traffic is Excluded from Cato

For configurations where you route all the remote user traffic to the Cato Cloud, you can define exceptions to bypass the Cato Cloud tunnel and connect directly to the destination. This lets you maintain security inspection in the Cato Cloud while optimizing access to trusted services.

For example, you may want traffic to a SaaS service such as **office.com** to bypass the tunnel for performance reasons. DNS queries for the domain are still inspected by the Cato Cloud. After the domain is resolved, the traffic connects directly to the destination.

Split Tunnel exceptions include the following options:

- **DNS Exclusions** – Define domains that are resolved by a local DNS server instead of through the Cato Cloud, such as internal applications that you want to access directly
- **Destination Exclusions** – Define applications, domains, FQDNs (EA), or IP ranges that bypass the tunnel, such as applications or services that users will access by bypassing the tunnel

**Note:** When creating a rule with an exclusion, you must explicitly specify the operating system as Windows

![Routing_Exceptions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34724175647005.png)

The following procedure outlines how to configure a rule to send all of your traffic to Cato while excluding local DNS traffic and destination using an FQDN.

**To customize the traffic that is excluded from the Cato Cloud:**

1. From the navigation menu, click **Access > Split Tunnel Policy**.
2. Create a new rule and configure the settings for: General, Users/Groups, Platforms, Source Network, and Countries.

For more information, see [Routing with the Cato Client (Split Tunnel Policy)](/v1/docs/routing-with-the-cato-client-split-tunnel-policy).
3. In the **Configuration** section, under **Select Connection Mode**, select **All Ports & Protocols**.
4. Under **Routing Policy**, select **Route all to Cato**.
5. In the **Define Routing Exceptions** section, define the traffic that bypasses the tunnel:
  1. Under **DNS Exclusions**, enter one or more domains to be resolved by your local DNS server.
  2. Under **Destination Exclusions**, configure one or more destinations and types that go directly to the destination.

Traffic to these domains will go directly to their destination and not through Cato
6. Click **Save**.

## Secure Only Specific (Included) Destinations

When creating a Split Tunnel rule, you can determine the routing policy so that, by default, traffic is not routed to Cato. Then, define only the specific traffic that is routed to Cato for inspection. For example, when most of your network traffic goes to a third-party solution, but you want to route specific traffic to a remote data center through Cato.

Currently, with **Route only selected to Cato**, all traffic is resolved using Cato DNS.

**Note:** When creating a rule to include traffic, you must explicitly specify the operating system as Windows.

The following procedure outlines how to configure a rule to send only specific traffic destinations to the Cato Cloud, and the rest is routed to your third-party solution.

![routing_include.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34724161599005.png)

**To customize which traffic is routed to Cato:**

1. From the navigation menu, click **Access > Split Tunnel Policy**.
2. Create a new rule and configure the settings for: General, Users/Groups, Platforms, Source Network, and Countries.

For more information, see [Routing with the Cato Client (Split Tunnel Policy)](/v1/docs/routing-with-the-cato-client-split-tunnel-policy).
3. In the **Configuration** section, under **Select Connection Mode**, select **All Ports & Protocols** or **Web Only**.
4. Under **Choose Routing Policy**, select **Route only selected to Cato**.
5. In the Define Routing Selections section, under **Destination Inclusions**, add the items that are routed to Cato for additional security checks.
6. Click **Save**.

## Known Limitation

- For Windows Client v6.4 and higher, you can define up to 100,000 Domain and FQDN items for a single rule
- For Windows Client v6.2 - 6.3, you can define up to about 100 Domain and FQDN items for a single rule (total number of characters is less than 3.5 KB)
