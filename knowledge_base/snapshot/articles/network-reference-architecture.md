---
title: "What is Cato LAN Segmentation"
slug: "what-is-cato-lan-segmentation"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/what-is-cato-lan-segmentation"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Cato LAN Segmentation

## Overview

As organizations adopt hybrid architectures, cloud applications, and distributed work models, internal network traffic increasingly carries sensitive data and critical operational flows that must be protected with the same rigor as WAN and Internet traffic. LAN segmentation is a key architectural component to reduce risk and improve operational control within modern enterprise networks.

This section describes how Cato approaches LAN segmentation as part of its broader SASE and Universal Zero Trust Network Architecture (UZTNA).

### LAN Segmentation in Modern Enterprise Networks

The primary goal of LAN segmentation is to limit implicit trust within the local network. By dividing the LAN into segments with explicit access controls, organizations can reduce lateral movement, contain compromised systems, and enforce least-privilege communication between devices, applications, and services.

LAN segmentation also improves operational clarity by making access paths intentional and reviewable. Instead of relying on flat networks and broad connectivity, admins define which systems are allowed to communicate and under what conditions.

### LAN Traffic as a Security and Visibility Gap

In hybrid and cloud-first environments, security controls are often concentrated at the network edge, protecting traffic entering or leaving the organization. As a result, east–west LAN traffic may receive less inspection and enforcement, creating a blind spot for lateral threats.

Without segmentation, a single compromised endpoint can access a wide range of internal resources. LAN segmentation closes this gap by applying consistent inspection and policy enforcement to internal traffic flows, improving both security posture and visibility within the local network.

### Relationship between LAN segmentation, Zero Trust, and SASE

LAN segmentation is a practical extension of Zero Trust principles into the local network. Zero Trust assumes no implicit trust based on network location and requires explicit policy evaluation for each access attempt.

Within the Cato SASE Cloud Platform, LAN segmentation applies these principles locally by enforcing policy-driven controls on the Socket. This lets organizations extend Zero Trust consistently across LAN, WAN, and Internet traffic using a single management plane.

### Components of the Cato LAN Segmentation Solution

Cato LAN segmentation is implemented through the following core components:

- Sockets - Enforce LAN segmentation locally at each site by inspecting and controlling east–west traffic.
- LAN Firewall - Defines and enforces segmentation policies for traffic between segments, including Layer 7 enforcement capabilities.
- Microsegmentation - Isolates hosts within the same VLAN using /32 addressing and forces intra-VLAN traffic through the Socket for inspection.
- Cato Management Application (CMA) and the Cato Cloud - Provide a single console to define and manage policies and settings that implement LAN segmentation. Policies are consistently deployed across the Cato Cloud global backbone.

## Defining LAN Segmentation in the Cato Platform

Cato implements LAN segmentation as a policy-driven security control that governs east–west traffic behind a Socket site. Local traffic segmentation is enforced through a combination of LAN firewall policies and microsegmentation controls that define which users, devices, applications, and services are allowed to communicate within the LAN. The Socket locally segments and secures LAN traffic at the physical site to control east–west communication with minimal latency.

### Logical Segmentation Versus Physical Segmentation

Cato LAN segmentation is implemented as logical segmentation enforced by the Socket. It does not rely on physically separate networks or dedicated segmentation hardware.

VLANs and IP ranges can be used to define segmentation scope, but they do not enforce isolation by themselves. In the Cato platform, these network attributes are used as matching criteria within LAN firewall and microsegmentation policies, while the Socket performs the actual enforcement. This approach allows administrators to adapt segmentation as the environment changes without redesigning network topology or introducing additional hardware.

### Using Sockets and the CMA to Enforce Segmentation

Segmentation policies are defined centrally in the CMA and enforced locally on the Socket at each site. The Socket acts as the enforcement point for all LAN traffic that crosses a defined trust boundary. This model provides centralized control with local enforcement, ensuring consistent policy behavior across Socket sites while maintaining local traffic inspection even if cloud connectivity is temporarily unavailable.

Once segmentation policies are in place, you can further enhance LAN security by enabling IPS enforcement on the Socket. The Socket can inspect east–west traffic for threats as it is evaluated against LAN Firewall rules.

## LAN Segmentation Architecture

This section describes the architecture of LAN segmentation in Cato.

### Role of the Socket in Local Enforcement

The Socket is the enforcement point for LAN segmentation at each site. All LAN traffic that crosses a segmentation boundary is inspected and controlled directly on the Socket, including traffic between VLANs. In addition, when you enable microsegmentation, traffic between hosts within the same VLAN is also inspected.

By enforcing segmentation locally, the Socket ensures that east–west traffic is evaluated with minimal latency and does not depend on round trips to PoPs in the Cato Cloud. This is especially important for latency-sensitive applications and environments where uninterrupted local connectivity is required.

### Centralized Policy Definition and Distribution via the CMA

Segmentation policies are defined once in the CMA and automatically distributed to all relevant Sockets. Administrators manage segmentation using a single policy framework that easily scales to large numbers of sites and supports gradual onboarding of sites to the Cato platform.

This centralized model simplifies change management and auditing. Policy updates are applied consistently across the environment, reducing configuration drift and eliminating the need for site-specific firewall rule settings.

## Socket Next Gen LAN Firewall as the Segmentation Control Plane

Cato uses the Socket Next Gen LAN Firewall as the control plane for enforcing segmentation within the local network. The Socket LAN Firewall evaluates east–west traffic against security policy, providing a consistent inspection and enforcement mechanism for LAN traffic without sending traffic to the cloud.

### Layer 7 Inspection for East-West LAN Traffic

The Socket LAN Firewall performs Layer 7 inspection on LAN traffic that crosses a policy-defined trust boundary. Rather than relying solely on IP addresses, ports, or VLAN identifiers, the firewall identifies applications and protocols within the traffic stream and evaluates them against policy.

Applying segmentation decisions based on application identity and traffic attributes allows administrators to enforce least-privilege access between systems while maintaining simple network designs. Segmentation decisions are expressed in security terms and enforced consistently at the Socket, reducing reliance on complex ACLs and minimizing the risk of over-permissive lateral access.

### Device and User Context

The Socket LAN Firewall also supports segmentation using device and user context. You can define rules based on device attributes such as OS version, manufacturer, or device type (for example, security cameras or printers), and restrict access accordingly. In addition, LAN Firewall rules can include user-based conditions, such as user identity or attributes like risk score, to enforce access policies based on who is initiating the traffic. This allows segmentation policies to combine network, device, and user context for more precise control over east–west traffic.

## Microsegmentation Within the LAN

Cato extends LAN segmentation with an agentless microsegmentation model that enforces isolation at the individual host level. Microsegmentation reduces the attack surface within a segment by preventing implicit trust between devices, limiting lateral movement even when systems share the same VLAN or IP subnet.

Microsegmentation forces intra-VLAN traffic to traverse the Socket for inspection and enforcement. East–west traffic between hosts is evaluated by the Socket LAN Firewall using the same policy framework applied to inter-VLAN traffic.

### Agentless Solution

Cato microsegmentation is implemented without deploying agents on endpoints or introducing dedicated segmentation appliances. Enforcement is performed by the Socket, using policy-defined controls rather than host-based software or complex network redesign.

This agentless approach allows microsegmentation to be applied uniformly across managed, unmanaged, and non-user devices, including servers, IoT, and OT systems. It also simplifies operations by avoiding endpoint lifecycle management and compatibility constraints.

### Host-Level Isolation Using /32 Addressing

When microsegmentation is enabled, hosts within a VLAN are logically isolated using /32 addressing. Each device is treated as its own isolated endpoint, removing default peer-to-peer reachability within the subnet.

This model ensures that devices cannot communicate directly with one another unless explicitly permitted by policy. Any lateral communication attempt must be evaluated and allowed by the Socket, enforcing least-privilege access at the host level.

## Segmentation Use Cases

The following sample use cases show how to limit unnecessary trust within the LAN while preserving required business connectivity.

### LDAP and Active Directory Segmentation

Restrict access to LDAP and Active Directory servers to only an IT admin user group. Enforce this on the Socket by allowing traffic to the LDAP/AD servers only from designated IT admin users or devices, and block all other access. This is an example set of LAN Firewall rules that to allow LDAP/AD access to IT admins while blocking acces for other sources:

![LAN_Segmentation_Restrict_LDAP_Server.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35000714149149(1).png)

### OT and IoT Isolation

Operational technology (OT) and IoT devices often lack built-in security controls and cannot support endpoint agents. Cato enables isolation of these devices by enforcing LAN firewall and microsegmentation policies directly on the Socket, allowing OT and IoT assets to be placed into dedicated segments with tightly controlled communication paths.

For example, configure microsegmentation for the security camera VLAN, and create a LAN Firewall rule that restricts access to the IP camera device type to only security personnel.

The following image shows a VLAN for security cameras configured with microsegmentation.

![LAN_Segmentation_Camera_Microsegmentation.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35000692517917(1).png)

### Protection of a Payment Server

Segmentation is used to restrict access to critical servers and workloads that host sensitive data or business-critical applications. Cato enables this by enforcing LAN firewall and microsegmentation policies on the Socket, allowing access to be defined using application-based controls where applicable and IP-based controls at the host level.

For example, restrict access to a payment processing server to only application servers that require it. Enforce this on the Socket by allowing traffic to the payment server only from designated application server IPs or segments, and block all other access.

This is an example set of LAN Firewall rules that allow access to the payment server from a designated application server while blocking access for other sources:

![LAN_Segmentation_Restrict_payment_Server.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35000692575133(1).png)
