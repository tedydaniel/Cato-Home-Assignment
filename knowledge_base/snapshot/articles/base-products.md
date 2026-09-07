---
title: "Base Products"
slug: "base-products"
updated: 2026-06-25T14:09:09Z
published: 2026-07-02T07:05:10Z
canonical: "knowledge.catonetworks.com/base-products"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Base Products

Base Products define how sites and users connect to the Cato Cloud and provide the foundation for all networking and access capabilities.

Sites are licensed based on bandwidth and support all site types, including physical sites (Sockets), IPsec, Cloud Interconnect, and App Connector deployments. Users are licensed as ZTNA users and provide secure remote access to the platform.

Base Products can be combined to support different deployment models across the organization. The following sections describe each component, its scope, and how it is licensed.

## Bandwidth Pool

Bandwidth Pool provides secure, optimized, and resilient connectivity between sites, users, and private resources through the Cato Cloud. It enables site-to-site, site-to-cloud, and private application connectivity, forming a unified network fabric across the organization.

Bandwidth Pool supports connectivity across all Cato site types, including Socket, IPsec, Cloud Interconnect, and App Connector deployments.

The Bandwidth Pool is designed for network connectivity use cases and provides reliable transport, performance optimization, and integrated security for traffic between sites and private environments.

### Capabilities

- SD-WAN with QoS, SLA, and high availability across Cato Cloud
- Internet Firewall with URL filtering
- WAN Firewall for site-to-site and private application traffic inspection and policy enforcement
- LAN Firewall for Socket sites
- Private access policy for zero trust access to App Connector
- Enforcement and visibility for on-site users in all firewall policies

### Supported Connectivity

- All Cato site types, including Socket, IPsec, and Cloud Interconnect
- App Connector deployments for private application access, with no limitation on the number of App Connectors or published applications

### Licensing

Bandwidth Pool is licensed by bandwidth, in units of 1 Mbps, and evaluated per region group.

The licensed bandwidth represents the total capacity of traffic sent and received through sites over the Cato Cloud. Bandwidth is purchased as a pooled capacity and shared across all sites in the applicable region group.

The Bandwidth Pool includes traffic that traverses the Cato Cloud, including site-to-site, user-to-site, internet-bound, and private application traffic (via App Connector).

Traffic that is locally bypassed or does not traverse the Cato Cloud (off-cloud traffic) is not measured against the Bandwidth Pool.

There is no minimum quantity requirement for Bandwidth Pool.

### Bursting and Over-Usage

Bandwidth Pool supports a bursting model, allowing customers to utilize available bandwidth beyond their licensed capacity when required. Customers can leverage the full capacity of their underlying connectivity across the pool, without being constrained by fixed limits.

Usage is measured against the licensed capacity using P95, and any excess is considered overusage. Additional details on measurement, enforcement behavior, and over-usage handling are provided in the Bandwidth Measurement and Over-Usage section.

## ZTNA User

ZTNA User enables secure remote connectivity to the Cato Cloud, providing authenticated access to Internet, SaaS, and internal resources. ZTNA User support connectivity using the Cato Client, clientless access portal, and browser-based access methods. Access is enforced based on identity-aware policies, enabling Zero Trust access to resources through the Cato Cloud. ZTNA Users apply only to users connecting remotely and do not apply to users connected through a Cato site.

### Capabilities

- Secure, authenticated remote user connectivity to the Cato Cloud.
- Access to Internet, SaaS, and internal resources is enforced using identity-aware Zero Trust policies.
- Connectivity using the Cato Client, clientless access portal, and browser-based access methods.

### Licensing

ZTNA Users are licensed per user and evaluated per region group.

Each license represents one distinct authenticated user who is allowed to connect remotely to the Cato Cloud.

By default, each account is allocated 5 ZTNA users free of charge.

There is no minimum quantity requirement for ZTNA users.

### Bursting and Over-Usage

ZTNA Users support a bursting model, allowing the number of active users to exceed the licensed capacity when required.

Usage is measured based on the number of distinct authenticated users during the evaluation period, and any excess beyond the licensed capacity is considered over-usage.

Additional details on measurement and over-usage handling are provided in the Over-Usage section of this guide.
