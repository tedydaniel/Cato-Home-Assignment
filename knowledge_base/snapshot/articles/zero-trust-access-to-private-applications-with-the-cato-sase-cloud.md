---
title: "Zero Trust Access to Private Applications with the Cato SASE Cloud"
slug: "zero-trust-access-to-private-applications-with-the-cato-sase-cloud"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/zero-trust-access-to-private-applications-with-the-cato-sase-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zero Trust Access to Private Applications with the Cato SASE Cloud

## Overview

As organizations modernize their IT infrastructure, securing access to private applications becomes critical. Traditional network-based approaches expose direct access to internal networks and extend unnecessary trust to users and devices. In distributed environments where users, workloads, and applications span branches, data centers, and cloud platforms, security must be enforced at the application level.

The Cato SASE Cloud delivers Zero Trust Network Access (ZTNA) to private applications by ensuring that only authenticated and authorized users can access published applications. Applications are never exposed to the non-authorized users and are only reachable through policy-driven access controlled in the Cato Cloud.

This article provides a high-level architectural overview of how the Cato Cloud functions as a ZTNA security broker and describes two deployment models for enabling secure access to private applications via Cato sites or App Connectors.

![app_connector_topology.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34326609119901.png)

The diagram above shows an example of users connecting to private applications in different environments via a physical Cato Socket or App Connectors. In this diagram, there are:

- Independent routing domains for each private network
- No requirement for unique IP spaces
- The Cato PoPs act as the ZTNA broker for access to the applications

## The Cato Zero Trust Model

At the core of Cato’s architecture is the global network of Points of Presence (PoPs) that form the Cato SASE Cloud. Each PoP functions as a ZTNA security broker between users and private applications.

![app_zero_trust.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34386676091421.png)

### User to Broker

Cato offers multiple methods for users to access private applications. While this article focuses on remote access using managed or unmanaged devices, the same principles apply to Cato’s Universal ZTNA (UZTNA) approach for users connecting from behind a site.

Users access private applications by first connecting to the Cato Cloud using the [Cato Client](/v1/docs/understanding-the-capabilities-of-the-cato-client) or secure [browser-based access](/v1/docs/browser-access). This establishes a secure session to the nearest PoP.

Regardless of the method, the core Zero Trust principles, Security engines, and policy enforcement remain consistent across all access scenarios.

#### Authentication and Authorization

1. Users initiate a secure connection to the Cato ZTNA Broker and undergo authentication using methods such as SSO or multi-factor authentication (MFA) via the IdP.
2. By default, no applications are visible or accessible. Once authenticated, the user and device are evaluated against the Private Access policy, role, device posture, location, behavior, and risk level.
3. In each session request, all policy criteria (the user’s device posture, behavior, risk, and more) are continuously evaluated.

#### PoP as the ZTNA Security Broker

The PoP enforces identity-driven access control and securely brokers connections between users and applications.

Once authentication and authorization are complete, the PoP brokers the connection to the permitted application through the appropriate access model (App Connector or Socket).

Applications are never exposed directly to users. By default, all application access is denied until explicitly permitted by Cato's ZTNA broker and the Private Access policy.

Once access is granted, all traffic is subject to Cato’s full security stack, including Threat Prevention and CASB/DLP inspection.

This brokered model ensures application-level access control, identity-based authorization, continuous posture and risk evaluation, and centralized policy enforcement.

### Private Access via App Connectors

In this model, private applications are published through App Connectors deployed within the application environment.

![app_connector_Architecture.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310215654685.png)

An App Connector is deployed in the same network environment as the protected application, whether in a physical data center or a public cloud VPC. This represents a network-neutral access model, where application access is enforced in the Cato Cloud rather than being dependent on underlying network topology. The connector establishes a secure connection to the Cato Cloud and publishes the applications via an App Connector Group.

When a user is authorized to access a private application, the PoP brokers the session to the best available App Connector associated with that application. The connector forwards only authorized sessions to the application.

Multiple connectors can be grouped together in an App Connector Group. This enables resiliency and load distribution. If a specific connector becomes unavailable, the application can automatically use another available connector within the same group. For more information, see [What Is Cato Private Access?](/v1/docs/what-is-cato-private-access)

### Private Access via Sites

In this model, the site type (Socket, vSocket, or IPsec) provides secure access to private applications located behind that site. The site connects to the Cato Cloud and extends the ZTNA architecture to applications within that environment. The PoP remains the ZTNA security broker, authenticating users and enforcing policy before brokering access to applications hosted behind the site.

A Socket or vSocket serves as the secure edge device for the entire site. Private applications within the site can be published and accessed based on ZTNA policy, without exposing internal network resources.

### Private Applications and the Cato ZTNA Broker

The Cato ZTNA Broker (implemented as part of the Cato SASE Cloud) acts as a broker between the user and the private application, securely stitching their outbound tunnels based on policy. By default, all application access is blocked, and only explicitly defined ZTNA policies can grant access.

Administrators can create granular policies that specify which users or groups can access which applications, supporting both HTTP/S as well as any protocol and port (including TCP/IP and UDP), in either direction. Once access is granted, all application traffic is subject to inspection by all security engines ([Threat Prevention](/v1/docs/threat-prevention), [CASB/DLP](/v1/docs/app-control-data-protection)) and policy enforcement.

- Access is granted per application rather than per network
- Authorization is identity-based and policy-driven
- Applications remain hidden unless explicitly permitted
- All permitted sessions are inspected by Cato’s security engines

By decoupling application access from network exposure, Cato enables organizations to adopt Zero Trust principles across data centers, branches, and cloud environments without redesigning their infrastructure.
