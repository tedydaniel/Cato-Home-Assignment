---
title: "Access to Internal Resources Troubleshooting"
slug: "access-to-internal-resources-troubleshooting"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/access-to-internal-resources-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Access to Internal Resources Troubleshooting

## Overview

Ensuring seamless access to internal resources is critical for maintaining productivity and security in the network. However, various factors can disrupt access, leading to bad user experience and hampered workflow. This playbook aims to provide a comprehensive guide for troubleshooting WAN access issues to internal resources within the Cato Cloud.

## Symptoms

A failure to access internal resources can manifest in several ways. An administrator may note the following symptoms:

- The internal server domain name cannot be resolved
- The internal server cannot be reached
- WAN firewall rule mismatch
- SDP Clients are unable to reach Internal Resources
- Remote Port Forwarding (RPF) resource cannot be reached
- The LAN monitoring host is unreachable

## Possible Causes

- Routing issues
- DNS forwarding misconfiguration
- WAN firewall misconfiguration
- Overlapping with the SDP Client's Network
- Security Intervention
- Destination host connectivity issues

## Initial Assessment

> [!NOTE]
> Note:
> 
> Make sure you have a WAN Firewall Rule (even temporarily created for troubleshooting purposes) with **event tracking enabled**.
> 
> For issues related to reaching internal servers via Browser Access, see [Troubleshooting Browser Access Issues](/v1/docs/browser-access-portal-troubleshooting)

Review WAN firewall, IPS, and Anti-malware events by selecting the respective preset in CMA. Set filters to narrow down the interesting traffic and check whether the flow was blocked by the WAN firewall or the IPS/AM engines. The **rule** field will show the respective rule that matches the traffic.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17173684051613.png)

Make sure to review the appropriate troubleshooting section by following these initial assessment steps:

- Check if the Server domain name is resolvable by running the *nslookup* or *dig* commands from the command line. If no DNS response is received, go to [Troubleshooting Server Domain Name Resolution Issues](/v1/docs/access-to-internal-resources-troubleshooting#troubleshooting-server-domain-name-resolution-issues)
- Check if the Server IP address can be reached by running the *ping* command. Make sure that ICMP is allowed by the WAN firewall rule before performing this test. If no ping response is received, go to [Troubleshooting Unreachable Internal Server](/v1/docs/access-to-internal-resources-troubleshooting#troubleshooting-unreachable-internal-server)
- If IPS or Anti-malware events show that any of these engines are blocking access to the internal server, go to [Resolving False Positive IPS/Anti-Malware blocks](/v1/docs/access-to-internal-resources-troubleshooting#resolving-false-positive-ipsantimalware-blocks)
- Check if the matching rule in the WAN firewall event is the expected one. If it's not, continue with [Troubleshooting Firewall Rule Mismatch](/v1/docs/access-to-internal-resources-troubleshooting#troubleshooting-wan-firewall-rule-mismatch)
- If only SDP Clients are being affected and not users behind Sites, go to [Troubleshooting SDP Client Not Reaching Internal Resources](/v1/docs/access-to-internal-resources-troubleshooting#troubleshooting-sdp-client-not-reaching-internal-resources)
- If the affected internal resource is accessed via Remote Port Forwarding, go to [Troubleshooting RPF Internal Resources](/v1/docs/access-to-internal-resources-troubleshooting#troubleshooting-rpf-internal-resources)
- If the affected server is monitored by LAN monitoring, check [Troubleshooting Unreachable LAN Monitoring Host](/v1/docs/access-to-internal-resources-troubleshooting#troubleshooting-rpf-internal-resources)

## Troubleshooting the Issue

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

#### Checking Audit Trail Logs

Check [Audit Trail](/v1/docs/using-the-audit-trail) for any **modified** logs that may have impacted access to the internal resources. This includes WAN firewall rules, AM/IPS settings, and TLS inspection.

### Troubleshooting Server Domain Name Resolution Issues

#### Checking DNS Resolution

If the internal resource is to be reachable using its domain name, confirm whether the internal server's domain name can be resolved, by using the *nslookup* or *dig* commands from the command line.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17229662328861.png)

There could be two scenarios for internal DNS resolution in your account:

- If a private DNS server IP address is used in the organization, confirm whether the affected users can reach the DNS server internally. If not, troubleshoot connectivity to the DNS server, similar to [Troubleshooting Unreachable Internal Server](/v1/docs/access-to-internal-resources-troubleshooting#troubleshooting-unreachable-internal-server)
- If the default Cato DNS server 10.254.254.1, account-defined DNS server, or well-known public DNS (8.8.8.8, 1.1.1.1, or 9.9.9.9) are used in the account, troubleshoot DNS forwarding in the next step.

#### Verifying DNS forwarding

Traffic flows that rely on internal domain names (e.g. *pc1.domain.net*) must have [DNS forwarding](/v1/docs/defining-dns-forwarding-rules) correctly configured in CMA. It is also crucial that Cato intercepts DNS flows to be able to resolve Domain Names correctly.

DNS forwarding can only work if DNS queries are destined to specific DNS servers as explained in [Resolving DNS forwarding Issues](/v1/docs/access-to-internal-resources-troubleshooting#resolving-dns-forwarding-issues).

### Troubleshooting Unreachable Internal Server

#### Checking the Cato Routing Table

The routing table can be used to verify route availability, metrics, and more:

- Search for the resource IP address in the search string and confirm that there is an existing matching route via the correct Site.
- If no route is found, this means that Cato is not aware of this route, hence, it cannot route to this destination. To solve this issue see [Resolving Routing issues](/v1/docs/access-to-internal-resources-troubleshooting#resolving-routing-issues)
- If there are routes to the same destination, verify that BGP dynamic ranges do not overlap with other static routes. Routes with lower metric are preferred. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17170685440925.png)
- BGP may also advertise redundant routes from different sites. The route with the lower metric including Weight, AS length, or MED is preferred. See [Understanding the Routing Table Fields](/v1/docs/showing-the-routing-table-for-your-account).
- To resolve metric issues, see [Resolving Routing issues](/v1/docs/access-to-internal-resources-troubleshooting#resolving-routing-issues)

#### Checking IPSec Policy-Based Routing

If the internal resource is reachable via IPSec, confirm that the correct ranges are defined in the Site's IPSec and Networks sections as explained in [IPSEC Troubleshooting Playbook](https://support.catonetworks.com/knowledge/editor/01HMH6A9H1WFWKE88MRDP4AQWS/en-us?brand_id=1168669).

If policy-based routing is configured, all traffic selectors must match on both Cato and the IPSec firewall/router to ensure connectivity to internal resources.

#### Checking the Aliveness of the Internal Resource

If the internal resource is located behind a socket or vSocket, check the **Last Host Activity** value from the **Know Hosts** page on the site. See [Showing Known Hosts for a Site](/v1/docs/showing-known-hosts-for-a-site)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17173713914525.png)

Hosts that have not been seen recently by the Site might be powered off or not connected to the network.

Run a [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) from the WebUI and identify any possible issues within the LAN.

#### Checking for TLS flows

If the interesting traffic is TLS and you have checked that the previous steps allow the traffic. Check if the traffic flow is being TLS inspected by Cato. This can be found in the FW rule with the **TLS inspection** field set to 1.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17174181913117.png)

If so, the Cato root certificate must be installed on the source device as explained in [Configuring the TLS Inspection Policy](/v1/docs/configuring-tls-inspection-policy-for-the-account). Otherwise, bypass TLS inspection to prevent any certificate errors and potential access issues to the resource.

### Troubleshooting WAN Firewall Rule Mismatch

When configuring a firewall rule, it may be possible that the traffic is evaluated against the wrong rule. This section covers all the possible mismatching scenarios and how to troubleshoot this issue.

#### Verifying Custom Application

If the interesting traffic is expected to match a custom application and the **Application** field found in the FW event does not match it, confirm that the custom app is correctly configured. Keep in mind that when overlapping custom apps exist, Cato **only** identifies traffic as **one of the custom apps**.

To prevent this issue, please view the [Resolving Overlapping Custom Application](/v1/docs/access-to-internal-resources-troubleshooting#resolving-overlapping-custom-application) section.

#### Verifying Built-in Application/Service

If the interesting traffic is expected to match a built-in Application or Service and traffic is matching the wrong firewall rule, check the following:

- What applications or services are configured in the 'wrong' matching firewall rule.
- Whether any of these applications/services are listed in the **Related Apps** field from the FW event.

App/Service identification is a multi-step process that starts with identifying the protocol and then all the possible matchable Applications that are included in the **Related Apps** field. Any 'related app' application identified in a flow regardless of the final app (**Application** field) decision will match a firewall rule.

In the example below, SMB traffic matches Rule #1 instead of Rule #2. This is because Rule #1 includes the *TCP* service (included in **Related Apps**) even though the final app (**Application** field) is *SMB*.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17173713919133.png)![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227402106653.png)

To resolve this expected behavior see [Firewall Rule Ordering](/v1/docs/access-to-internal-resources-troubleshooting#firewall-rule-ordering)

#### Verifying the Configured Domain Name

If a Firewall Rule contains a Domain or FQDN object, check what the **Domain Name** field is in the FW event. The Domain/FQDN object in the firewall rule must be the same as this field.

Bear in mind that an **FQDN** is an exact match of the fully qualified domain. For example, the FQDN *example.com* only matches *example.com.*

On the other hand, a **Domain** is a top-level (TLD) or second-level domain (SLD) that matches all subdomains. For example, the Domain *example.com* matches www.*example.com* and *host.example.com*.

There could be cases where Cato cannot determine the correct Domain Name from HTTP, TLS, or DNS flows. To resolve these types of issues see [Resolving Domain Name Mismatching Issues](/v1/docs/access-to-internal-resources-troubleshooting#resolving-domain-name-mismatching-issues)

### Troubleshooting SDP Client Not Reaching Internal Resources

This section addresses issues exclusive to SDP Clients not reaching internal resources.

#### Checking User's Home Network Subnet Overlap

If the SDP Client cannot connect to internal resources, including pinging the server, check if there is an IP address overlap between the user's home network and the site with the internal resources. If that's the case, the client's routing table will point at the local NIC when trying to connect to the internal server located behind the remote Cato site, resulting in a connection failure.

Remote sites with an IP range of 192.168.0.0/24, 192.168.1.0/24 or 10.0.0.0/24, can easily overlap with the IP range for home wireless routers, which often use this IP range as the default DHCP setting.

To solve this issue, follow the steps described in [SDP Client Can't Connect to Remote WAN Resources](/v1/docs/sdp-client-fails-to-connect-to-remote-wan-resources).

#### macOS and iOS Users Not Resolving Internal Domains

As explained in [macOS Ventura and iOS Users Unable to Reach Internal Resources Via Cato](/v1/docs/macos-ventura-and-ios-users-unable-to-reach-internal-resources-via-cato), if the SDP Client cannot connect to internal resources using its domain name but they are able to reach it using its IP address, it is possible that DNS forwarding is failing due to **DoH** (DNS over HTTPS) or **DoT** (DNS over TLS) being used by the endpoint. Cato currently does not support DoH/DoT.

To resolve this issue, see [Resolving DNS forwarding Issues](/v1/docs/access-to-internal-resources-troubleshooting#resolving-dns-forwarding-issues). Alternatively, Cato DNS Server (10.254.254.1) can be defined in CMA as the only DNS server for the endpoint.

#### Android Users Not Resolving Internal Domains

As explained in [Android Devices Unable to Reach Internal Resources Via Cato](/v1/docs/android-devices-unable-to-reach-internal-resources-via-cato), if the SDP Client cannot connect to internal resources using its domain name but they are able to reach it using its IP address, it is possible that DNS forwarding is failing due to **Automatic Private DNS** used by the device (default behavior) which enforces DoH/DoT for DNS resolution. This is currently not supported by Cato.

To resolve this issue, see [Resolving DNS forwarding Issues](/v1/docs/access-to-internal-resources-troubleshooting#resolving-dns-forwarding-issues). Alternatively, Private DNS may be disabled on the device.

### Troubleshooting RPF Internal Resources

#### RPF Event Analysis

Review RPF events by selecting the **RPF** preset in CMA. Confirm that the event is generated which will confirm that the external Cato IP is available. Note that the destination IP address is the external public IP configured in the RPF rule.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17229957627293.png)

> [!NOTE]
> Note:
> 
> Inbound RPF events may sometimes display a **User Display Name**, even though the traffic is not user-initiated. This is **expected behavior**.

Event fields in the Cato platform pull metadata from the **tunnel**, **host**, and **user agent**, not just traffic flow. So, if a user is mapped on an device behind socket or tunnel, their name may appear in the event—even for inbound traffic.

This differs from how firewall or routing policies interpret traffic (which are direction-aware), but is normal for **event correlation**.

#### Geo Block Event Analysis

Review any events destined for the internal IP address of the internal server. Confirm that no Geo Blocking restriction is preventing the connection to the internal server. If so, edit the [Geo Restriction policy](/v1/docs/configuring-ips-and-geo-restriction) for the inbound direction to allow the source country.

#### Checking the Aliveness of the Internal Resource

Check the **Last Known Activity** value from the **Know Hosts** page on the site. See [Showing Known Hosts for a Site](/v1/docs/showing-known-hosts-for-a-site)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17173713914525.png)

Hosts that have not been seen recently by the Site might be powered off or not connected to the network.

Run a [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) from the WebUI and identify any possible issues within the LAN.

### Troubleshooting Unreachable LAN Monitoring Host

#### Connectivity Event Analysis

Review Connectivity events by selecting the **LAN hosts unreachable** preset in CMA. **Host Unreachable** events will be generated when the defined LAN host is no longer reachable.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17197290725021.png)

#### Checking Local Host Reachability

Confirm that the defined local host can be pinged from the [Socket WebUI](/v1/docs/accessing-the-socket-webui). If the ping is successful, check the following:

- The [LAN monitoring](/v1/docs/configuring-lan-monitoring-for-a-site) probes are ICMP packets sourced from 10.254.254.1, so it's important to confirm that the monitored host has a route back to the Socket LAN gateway to be able to reply.
- If the device is running a local firewall, ICMP must be allowed from the 10.254.254.1 IP address.

Run a [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) from the WebUI and identify any possible issues within the LAN.

## Resolving Discovered Issues

### Resolving Routing issues

If the route to the internal resource isn't found in the routing table, check and resolve the following:

- If BGP is configured for the site, verify that the routes are advertised by the neighbor. See [Showing BGP Status](/v1/docs/configuring-bgp-neighbors-for-a-cato-socket). It is important to review the BGP prefixes that the local router advertises and confirm that Cato is receiving them.
- If the BGP session is down, troubleshoot the disconnect issue. See [BGP Session is Disconnected](/v1/docs/xops-network-playbook-bgp-session-disconnected)
- Make sure that the site hosting the range is available. See [Troubleshooting Site Connectivity](https://support.catonetworks.com/knowledge/editor/01HNCRM5BBJFDYEHPQNEHPY527/en-us?brand_id=1168669)

If the route metric seen in the routing table is causing wrong routing decisions, check and resolve the following:

- Tunnel metric values are usually set by Cato. Redundant routes should have the same tunnel metric as long as they originate from the same type of site, e.g. IPSec or Socket Site.
- The weight value can be configured in CMA, **Network > Site > Site Configuration > BGP**. The metric value configured on this page will be seen as weight in the routing table. Changing the metric for the site will fix wrong routing decisions for redundant routes.
- The AS length and Metric Discriminatory metric values are received from the external router. They must be modified on this device if needed.

### Resolving False Positive IPS/Anti-Malware blocks

If the interesting traffic is blocked by IPS/AM, you can add allow lists with scope **WAN** to both IPS and Antimalware settings.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17174211153181.png)

### Resolving Overlapping Custom Application

Make sure that the custom application includes the correct IP addresses, Domain, Port, and Protocol. There is no logic to what custom app is chosen for identification, so the custom app must be uniquely defined to avoid overlapping with another custom app. For more information, see [Working with Custom Applications](/v1/docs/working-with-custom-apps)

### Firewall Rule Ordering

Keep in mind that Firewall Rules are evaluated according to their order, so it's important to define more specific rules above more general rules. For example, Firewall Rules that define a custom application, built-in application, domain, FQDN, or custom service should be placed above Firewall Rules containing categories, custom categories, or services.

In the screenshot below, Rule #1 contains a custom service that includes IP ranges for twitter.com and is placed above Rule #2 which contains Application Categories. Rule #1 is more specific than Rule #2 and will be a better match for traffic destined to *twitter.com.* This will additionally disable TCP acceleration and solve any Off-Cloud or Alt-WAN routing issues given that Rule #1 is a simple rule.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17173684058013.png)

### Resolving Domain Name Mismatching Issues

Firewall Rule matching issues based on Domain/FQDN can be resolved as follows:

- For protocols like HTTP/S, Cato can determine the destination domain using the following sources:
  - **HTTP Hostname header** (when TLS inspection is enabled)
  - **SNI** field during the TLS handshake
  - **DNS resolution**, where the domain name is learned from DNS queries and responses
- It is important to ensure that the domain specified in the Firewall Rule is consistent across all of these sources. Note that only the best-matched domain name (evaluated from top to bottom) is displayed as **Domain Name** in Firewall events.
- For other protocols, such as SSH or SMB, that don't send a domain in plain text, Cato relies exclusively on **DNS interception** to associate traffic with a domain or FQDN. This is particularly critical when using a private DNS as we need to ensure that DNS queries/responses go through Cato. See [Best Practices for DNS and Your Cato Account](/v1/docs/best-practices-for-dns-and-your-cato-account)
- DoH (DNS over HTTPS) and DNS over TLS aren't supported for Domain Name/Application matching, hence, they must be blocked in the Firewall rules to force moving DNS queries to UDP/53.

### Resolving DNS Forwarding Issues

You can only use DNS forwarding when DNS queries are destined to the following DNS servers:

- Cato's default DNS server 10.254.254.1
- Account-level DNS servers, configured under **Network > DNS settings**
- Well-known DNS servers such as 8.8.8.8, 1.1.1.1, and 9.9.9.9. The list of well-known DNS servers can vary between PoPs. For example, China and Sydney.

DoH (DNS over HTTPS) and DNS over TLS aren't supported for DNS forwarding, hence, they must be blocked in the Firewall rules to force moving DNS queries to UDP/53. This solution applies especially to macOS, iOS, and Android SDP Clients.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17176311655325.png)

## Raising Cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the experienced issue and overall impact on users.
- Related Firewall events and Firewall Rule configuration.
- Reproduce the issue and run the [Support Self Service](/v1/docs/support-self-service-supportme-portal). Include the ticket number generated by the Tool.
- If the affected user connects to Cato using the SDP Client, please [Record the Issue Using the SDP Client](/v1/docs/recording-issues-using-the-cato-client)
