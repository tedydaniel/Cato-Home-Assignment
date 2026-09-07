---
title: "App Connector Reference Architecture"
slug: "app-connector-reference-architecture"
updated: 2026-07-28T08:05:33Z
published: 2026-07-28T08:05:33Z
canonical: "knowledge.catonetworks.com/app-connector-reference-architecture"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# App Connector Reference Architecture

This article explains the role of [App Connectors](/v1/docs/working-with-app-connectors) in the Cato Private Access architecture and the end-to-end traffic flow for accessing Private Applications. It describes how DNS resolution, CGNAT, App Connector Groups, load balancing, and high-availability mechanisms work together to securely broker user connections to internal applications.

## Overview

When an admin publishes a [Private Application](/v1/docs/configuring-private-applications) in the Cato Management Application (CMA), the application is associated with an App Connector Group and defined by its published application domain, internal destination, and permitted ports and protocols. The Cato PoP is the ZTNA Broker that registers the published application in the Private Access control plane and assigns a synthetic IP address to the published application domain. This IP address represents the application within the Cato brokered architecture and prevents users from learning or connecting directly to the application's internal IP address.

All access to published Private Applications is user-initiated and brokered by the Cato Cloud.

- The control plane validates the user identity, evaluates the Private Access Policy, and determines whether the requested application, port, and protocol are authorized
- The data plane transports sanctioned traffic through the Cato Cloud and the selected App Connector to the internal application server

Unauthorized application requests are denied before a session to the application environment is established.

## Traffic Flow

1. The user connects to the Cato SASE Cloud using the Cato Client, or another supported access method.
2. The user attempts to access a published Private Application by sending a DNS request for the published application domain to the Cato DNS service.
3. The Cato PoP (ZTNA broker):
  - Identifies the Private Application associated with the requested domain
  - Evaluates the [Private Access Policy](/v1/docs/configuring-the-private-access-policy) to determine whether the authenticated user is authorized to access an application published with that domain
4. Cato DNS handles the request based on the authorization result:
  - If the user is authorized, Cato DNS returns the synthetic (CGNAT) IP address assigned to the published application domain
  - If the user is not authorized, Cato DNS denies the request The domain does not resolve, and no session to the application environment is established
    1. The user initiates a connection to the returned synthetic IP address. The Cato Cloud sanctions the session.
    2. Selects the optimal App Connector from the associated App Connector Group.
    3. Stitches the authorized user session to the internal application through the outbound DTLS tunnel established by that App Connector.
5. The App Connector resolves the configured internal application destination when internal DNS resolution is required, and forwards the traffic over the local network to the internal application server.

Throughout the flow, identity validation, DNS authorization, port and protocol enforcement, and session brokering are performed by the Cato Cloud. The user communicates with the synthetic IP address assigned to the published application domain and does not receive direct network reachability to the application environment.

## DNS and App Connectors

DNS binds authorized users to published Private Applications without exposing internal application addressing. User devices must use the Cato DNS service at 10.254.254.1 so that queries for published application domains are processed by the PoP.

The App Connector uses a separate DNS path for internal application resolution. By default, it uses DHCP to obtain its LAN IP address, default gateway, and internal DNS server. When an internal application is identified by an FQDN, the App Connector uses the internal DNS server to resolve the application over the local network.

**Coming Soon:** Support for static LAN IP and DNS configuration in environments without DHCP.

## CGNAT and IP Abstraction

When a Private Application is published through an App Connector Group, the PoP registers it in the Private Access control plane and assigns it a unique synthetic IP address from the account’s Private Application CGNAT range. This synthetic IP represents the application within the Cato Cloud and keeps its internal IP address hidden from users.

These ranges must not overlap with customer network ranges or other Cato service ranges and can be customized when required.

Users access the application through its published domain and synthetic IP representation rather than its internal address.

This abstraction is especially useful in environments with overlapping address spaces, such as mergers and acquisitions, because applications can be published without readdressing the underlying networks.

**Known Limitation:** Synthetic IP addresses are generated automatically by Cato and are not exposed for direct reference in Network Policy rules.

### App Connector Groups

An App Connector Group is the logical connectivity layer between the Cato Cloud and a set of Private Applications. Private Applications are associated with a group rather than with an individual App Connector, and each application can be published through one App Connector Group at a time.

**Note:** An App Connector Group can include up to 10 App Connectors.

The PoP continuously probes the connectors in the group and evaluates their availability and performance. For each sanctioned session, the PoP selects the optimal connector and stitches the session through that connector to the internal application.

Multiple App Connector Groups can be used to represent separate environments, regions, or security zones, such as production, disaster recovery, cloud, or on-premises networks. The group associated with a Private Application must contain at least one connector that can reach the application over the LAN. Each application can only be published to one App Connector Group at a time.

**Best Practice:** Deploy and connect the App Connectors before publishing Private Applications through the group. If no connector in the group is connected, the Private Application is unavailable and appears as disabled.

## Auto-Failover

Auto-failover maintains access to Private Applications when an App Connector becomes unavailable. The PoP continuously probes the connectors in an App Connector Group and evaluates their availability and performance.

If a connector becomes unreachable, the PoP stops selecting it for new sessions and routes subsequent sanctioned sessions through the next best available connector in the group. Existing sessions may need to be re-established through the newly selected connector.

Failover occurs automatically within the App Connector Group and does not require administrator intervention. Private Applications remain available as long as at least one connector in the group is connected and has LAN reachability to the internal application server.

To maintain availability across regions or cloud environments, deploy App Connectors in each environment that hosts the application. The connectors must belong to an App Connector Group associated with the corresponding Private Application and must have LAN reachability to that application instance.

## High Availability

High availability is achieved by deploying multiple App Connectors in the same App Connector Group. Because Private Applications are associated with the group rather than with an individual connector, application access can continue as long as at least one connector remains connected and has LAN reachability to the internal application server.

Deploy at least two App Connectors per group and ensure that each connector can reach the same application destinations. The PoP continuously evaluates connector health and performance and distributes sanctioned sessions across the available connectors.

For cloud deployments, place connectors in separate availability zones or regions to reduce dependency on a single infrastructure location. For physical deployments, place connectors in separate racks, power domains, or failure zones.

App Connector failover is designed to restore application access within 30 seconds. Session continuity depends on the application protocol and session state, and some active sessions may need to be re-established.

**Coming Soon:** Support for redundant physical App Connector Cato Sockets in an HA pair.
