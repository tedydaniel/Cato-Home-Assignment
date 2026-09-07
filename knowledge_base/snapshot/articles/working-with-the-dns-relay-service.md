---
title: "Working with the DNS Relay Service"
slug: "working-with-the-dns-relay-service"
updated: 2026-06-23T13:45:56Z
published: 2026-06-23T13:45:56Z
canonical: "knowledge.catonetworks.com/working-with-the-dns-relay-service"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with the DNS Relay Service

The DNS Relay service is a helper service of the Cato Client, running on the endpoint, and it's automatically installed in the background when you implement a [Split Tunnel policy](/v1/docs/routing-with-the-cato-client-split-tunnel-policy). It lets you control how DNS requests from a device are handled so you can steer traffic through the correct network path. DNS Relay intercepts DNS requests locally and determines whether each request should be resolved using the Cato-configured DNS server, the local device DNS server, or a DNS server reachable through another interface. After the request is resolved, DNS Relay can update the routing table for the destination domain so that subsequent traffic follows the correct route.

![Managed_Device_Coexistence_with_VPN.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34698140180893.png)

Using DNS Relay, you can define a default routing behavior for all traffic and then configure exclusions for specific DNS queries and destination traffic that should bypass that default route. For example, if all traffic is routed to the Cato Cloud by default, DNS Relay can process excluded DNS requests and ensure that traffic for those destinations is sent outside the tunnel to the appropriate location. This approach enables precise, domain-based traffic steering while maintaining consistent routing and policy enforcement.

> [!NOTE]
> Note:
> 
> The DNS Relay service is available for Windows Client v5.20.2 and higher.

## Use Case - Cato Internet Security Coexists with a Third-Party VPN using DNS Relay

ABC Company allows remote employees to access internal resources located in their corporate WAN through a third-party VPN. At the same time, all Internet and SaaS traffic must be routed through the Cato Cloud using the Cato Client. To enforce this policy, the Cato Client is configured as Always-On, while the third-party VPN is enabled only when the user needs access to internal WAN resources.

When the user connects to the third-party VPN, the operating system creates a new network interface and associated routes. The DNS Relay service detects this change and adjusts how DNS requests are handled to ensure traffic continues to follow the correct path.

When the user sends a DNS request for an internal server accessible via the 3rd-party VPN, DNS Relay intercepts the request and determines that the destination should be resolved using the 3rd-party DNS server. The request is forwarded through the VPN interface, and subsequent traffic to the database is routed through the 3rd-party VPN.

When the user sends a DNS request for Salesforce, which is a SaaS web application, DNS Relay determines that the request should be resolved using the Cato-configured DNS server. The DNS request is forwarded through the Cato Client, and traffic to Salesforce is routed through the Cato Cloud.

This configuration allows ABC Company to use the third-party VPN for access to internal WAN resources while ensuring that Internet and SaaS traffic remains secured and inspected by the Cato Cloud.

## Use Case: Securing Only Specific Destinations with the Cato Client

ABC Company allows remote employees to access most Internet destinations directly using their local network connection. However, traffic to certain corporate applications and sensitive SaaS services must be secured and inspected through the Cato Cloud. To enforce this policy, admins configure the Cato Client to secure only specific destinations while allowing all other traffic to use the local Internet connection.

When the user connects to the network, the Cato Client is active, and the DNS Relay service intercepts DNS requests. DNS Relay evaluates each request and determines whether the destination should be resolved using the Cato-configured DNS server or the local device DNS server.

When the user sends a DNS request for a corporate application that must be secured, DNS Relay forwards the request through the Cato Client, and traffic to the destination is routed through the Cato Cloud. For other Internet destinations, DNS Relay uses the local DNS server, and traffic is sent directly through the user's local Internet connection.

This configuration allows ABC Company to secure specific applications through the Cato Cloud while allowing other Internet traffic to bypass the tunnel and go directly to the destination.

## Configure the DNS Relay Service Registry Settings

The following Windows registry keys control how DNS Relay manages DNS requests, selects DNS servers, and responds to network interface changes.

| Registry Key | Description | Values |
| --- | --- | --- |
| DnsRelayUseAllInterfaces | Controls whether DNS Relay collects on-prem DNS servers from all network interfaces on the device | Enabled – Collect DNS servers from all interfaces Disabled – Collect DNS servers only from selected interfaces |
| DnsRelayBindingStrategy | Controls which network interface DNS Relay binds to when forwarding a DNS query to an on-prem DNS server | 0 – Bind to the physical interface used by the tunnel 1 – Bind to the interface where the DNS server is configured 2 – Bind to the interface selected by the best route |
| DnsRelayUpdateOnAdapterChange | Controls whether DNS Relay updates its configuration when a network interface changes This is required when working with 3rd party VPNs that you might turn on and off. | Enabled – Update DNS Relay when an interface changes Disabled – Do not update DNS Relay when interface changes occur |
