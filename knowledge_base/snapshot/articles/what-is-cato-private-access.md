---
title: "What Is Cato Private Access?"
slug: "what-is-cato-private-access"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/what-is-cato-private-access"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What Is Cato Private Access?

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Cato Private Access lets you provide secure, identity-based access to private applications without extending your network to users. Instead of granting direct network-level connectivity like a traditional VPN, you enforce least-privileged, application-specific access based on user identity and context.

Applications remain hidden and unreachable unless explicitly authorized. Users connect to the Cato Cloud, and authorized sessions are securely brokered to the application through outbound-only App Connectors. This architecture reduces attack surface, limits lateral movement, and removes the need for inbound firewall rules, route advertisements, or network redesign.

Private Access is designed for rapid deployment and incremental adoption. You can onboard applications without modifying WAN topology or IP addressing.

### Scope of Private Access Architecture

Cato Private Access provides user-to-application access through a brokered architecture. Users do not directly connect to the network that hosts the application. Instead, access is established only to applications that are explicitly defined and exposed through App Connectors.

Private Access supports user-initiated access only. Applications do not initiate connections toward users, and server-initiated or bidirectional communication patterns are not supported. This design enforces strict isolation between users and application environments and eliminates the need to expose internal networks or advertise routes.

Scenarios that require server-initiated or bidirectional communication fall outside the scope of Private Access and are supported by the full Cato networking architecture of IPsec and Socket sites.

For more information, see [Zero Trust Access to Private Applications with the Cato SASE Cloud](/v1/docs/zero-trust-access-to-private-applications-with-the-cato-sase-cloud).

### Licensing for Private Access

The Private Access service is licensed by users per region group. For more information, please contact your Cato representative or official reseller.

## How Cato Private Access Works

1. A user connects to the Cato Cloud using the Cato Client or clientless access.
2. The PoP authenticates the user and evaluates the Private Access Policy.
3. If the user is authorized, the session is brokered through an outbound DTLS tunnel to an App Connector.
4. The App Connector forwards the traffic locally to the application.

Applications never accept inbound connections and are not exposed to user networks. Access is always user-initiated and policy-driven.

## Core Components

### Private Applications

![private_apps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35813226170269(1).png)

Private Applications represent the internal apps you publish through Cato.

For each application, you publish internal resources securely by defining how users access the application and which Connector Group provides authorized connectivity. Applications are abstracted from internal IP addressing, and users access the published domain rather than the internal network.

### App Connectors

![App_Connectors.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35813259615773(1).png)

You deploy App Connectors in the same environment as the protected application (data center, cloud VPC, or LAN) to securely connect that environment to the Cato Cloud. Each connector establishes an outbound-only DTLS tunnel and forwards only sessions that were explicitly authorized by policy. Because connectors do not accept inbound connections and do not require routing changes, you can introduce Private Access without redesigning the application network. You can deploy multiple connectors to increase resiliency and scale.

### App Connector Groups

![app_connector_groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35813214185885(1).png)

App Connector Groups logically group connectors to provide high availability, load distribution, and operational separation. Private applications are attached to a Connector Group rather than to a specific connector. This means that if a specific connector experiences an issue, the application can automatically use another available connector in the group.

### Private Access Policy

![private_access_policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35813222934173(1).png)

You use the Private Access Policy to control who can access which private applications and under what conditions. The policy lets you grant application-level access based on user identity and context while maintaining a default-deny posture. Authorization is evaluated at the PoP before any session is established to the application environment, ensuring that only explicitly permitted connections are brokered to the application.

## Use Cases

### Secure Access to Private Applications Without Network Changes

Securely expose internal applications without modifying routing, advertising subnets, or changing WAN architecture.

Private Access requires no inbound firewall rules, uses outbound-only tunnels from the application environment, does not require IP readdressing, and does not require site on-ramping. This makes it ideal for fast onboarding of private applications while preserving the existing network design.

### Mergers and Acquisitions with Overlapping IP Environments

In M&A scenarios, overlapping IP ranges often delay integration.

Private Access publishes applications without requiring IP readdressing, abstracts internal addressing using CGNAT and DNS mapping, and allows user access without routing-domain integration. This supports rapid, non-disruptive onboarding of acquired environments.

If bidirectional or server-initiated connectivity is required later, you can onboard the environment as a full Cato site.
