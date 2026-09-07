---
title: "What is the Cato Firewall"
slug: "what-is-the-cato-firewall"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/what-is-the-cato-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Cato Firewall

## Overview

Cato’s Next-Generation Firewall (NGFW) provides consistent inspection and enforcement across WAN, Internet, and LAN traffic using multiple policies tailored to each traffic type. This lets you apply precise controls at every network boundary and benefit from unified enforcement.

Cato’s global PoPs act as the enforcement point for FWaaS, where the security stack inspects and protects WAN and Internet traffic at the network edge.

All firewall policies operate on a shared traffic context that feeds into the data and analytics for your account. You configure and monitor these policies in the Cato Management Application (CMA), a unified console that simplifies policy management and enables detailed analysis of enforcement data across WAN, Internet, and LAN traffic.

The Socket LAN Firewall addresses east-west traffic behind a site. By inspecting inter-VLAN and host-to-host communications directly on the Socket appliance, you can prevent unauthorized lateral movement, enforce microsegmentation, and eliminate the need for third-party LAN firewall hardware. This extends NGFW protection to local traffic while maintaining centralized policy control in the CMA.

## CMA Firewall Policies

Cato provides three distinct firewall policies in the CMA that align with different traffic types and security requirements. Instead of a single generalized rulebase, each policy is optimized for Internet traffic, WAN traffic, or internal LAN segmentation. This separation improves clarity, reduces policy complexity, and ensures that security controls match the context of the traffic being inspected.

- WAN Firewall: Provides Zero Trust enforcement for site-to-site and user-to-site traffic over the WAN. In the CMA, admins define explicit allow rules that ensure only authorized applications, services, and identities are allowed to communicate over the Cato backbone
- Internet Firewall: Enforces granular controls for outbound Internet traffic. Admins define rules in the CMA that match traffic based on application, user identity, and destination domain or category. Features like URL Filtering and application awareness provide deep traffic visibility to support accurate rule enforcement
- Next-Gen LAN Firewall: Provides layer-7 east-west traffic inspection between VLANs and hosts within a site. The LAN Firewall enforces segmentation and microsegmentation policies defined in the CMA, without requiring third-party appliances

| Traffic Type | Description | How the Traffic is Processed | Policy Configuration |
| --- | --- | --- | --- |
| Internet | Traffic to external Internet destinations | The PoP receives the traffic from the site or remote user and applies the Internet Firewall policy | [Internet Firewall](/v1/docs/internet-firewall) |
| WAN | Traffic from sites or remote ZTNA users to other Cato Cloud destinations | The PoP receives the traffic from the site or remote user and applies the WAN Firewall policy | [WAN Firewall](/v1/docs/wan-firewall) |
| LAN | Traffic between hosts (e.g., VLANs) behind the same Socket - both the source and the destination IP addresses of a flow belong to the same Socket site. | The Socket applies the LAN Firewall policy The traffic remains local and isn’t sent to the PoP | [LAN Firewall](/v1/docs/lan-firewall) |

## Zero Touch Deployment for WAN and Internet FW

Cato enforces WAN and Internet Firewall policies without requiring on-site installation, manual setup, or hardware maintenance. All policy creation and distribution are handled centrally in the CMA, and enforcement is applied automatically across Cato’s global PoPs. This approach accelerates the onboarding of new sites and users and maintains consistent enforcement with minimal administrative effort.

- Centralized policy definition in the CMA with automatic distribution to all PoPs
- Global policy propagation that applies changes in real time across WAN and Internet firewalls
- No appliance lifecycle tasks such as patching, upgrading, or replacing hardware

## Analytics and Integrations

Firewall analytics in the CMA provide deep visibility into traffic behavior, rule performance, and policy effectiveness. Admins can monitor data, view firewall events, track rule usage, and correlate activity across the security stack. These insights help validate policies, troubleshoot issues, and support audit or compliance efforts.

Capabilities include:

- Events and Reporting: Admins can configure rules in the CMA to generate traffic events, which are logged for visibility into rule activity, policy enforcement, and anomalies
- App Analytics: Display traffic trends and application usage across the network. Security teams can identify top applications, monitor unusual behavior, and inform policy decisions based on observed traffic
- Customized Notifications: Generate real-time notifications for firewall rules that can be delivered to admin-defined subscription groups, or integrated with third-party systems through webhooks. Notifications can also be distributed via email to ensure timely visibility across security and operations teams
- SIEM Integration: Export firewall logs and event data to third-party SIEM platforms for advanced analysis, threat correlation, and compliance reporting

**Related Articles**

- [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network)
- [Understanding App Analytics](/v1/docs/understanding-app-analytics)
- [Sending CMA Notifications via Webhooks](/v1/docs/sending-cma-notifications-via-webhooks)
- [Cato Data: Third-Party Supported Integrations](/v1/docs/cato-data-third-party-supported-integrations)

## Firewall Features

### Core Features

Cato's core platform license includes firewall capabilities that consistently inspect traffic across WAN, Internet, and LAN networks. These features are delivered from Cato’s global PoPs and centrally managed in the CMA, giving admins unified control across all network segments. The platform follows SASE design principles: cloud-native architecture, identity-based policy enforcement, and a single-pass security stack at the edge.

Capabilities include:

- Application awareness: Identifies applications across all ports and protocols using Layer 7 inspection in Cato PoPs
  - Cato uses AI/ML models to collect new application indicators directly from our cloud traffic stream (650+ Gbps) across thousands of customers. Our research team assigns and scores them as part of the semi-automated process of discovering new applications and integrating them into the Cato platform
  - The App Catalog in the CMA ensures you always have access to the latest information on thousands of apps and services, including Cato-specific metadata such as risk scores and CASB activities
- User awareness: Enables rules that match traffic based on user and group identity, integrating with enterprise identity providers
- URL filtering: Categorizes domains and URLs to allow or block access based on destination content and risk
- Device posture: Supports conditional access by evaluating device posture attributes defined in Device Posture Profiles
- Autonomous Firewall Insights: Uses AI-based analysis to identify unused, overly permissive, or conflicting rules and provides optimization suggestions
- Socket LAN Firewall: Inspects inter-VLAN and host-to-host traffic at the site level, enabling segmentation and microsegmentation without additional LAN appliances
- API support: Provides full API access for configuring and monitoring firewall policies, enabling automation and integration with external management and security systems

**Related Articles**

- [Using the App Catalog](/v1/docs/using-the-app-catalog)
- [User Awareness](/v1/docs/user-awareness)
- [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules)
- [What is the Cato API](/v1/docs/what-is-the-cato-api)

### Add-On Features

Cato offers additional firewall capabilities as licensed services to extend inspection and control across more traffic types and device categories. These services integrate with the CMA and the Cato Cloud to enhance threat protection and asset visibility.

- Remote Browser Isolation (RBI): Streams visual web content from a remote browser hosted in the cloud. Web code executes in isolation and never reaches the user’s device, protecting against browser-based threats such as phishing, malware, and malicious scripts. Requires the Advanced Threat Prevention license
  - You can define RBI as the action for Internet Firewall rules
- IoT/OT security: Uses the Device Inventory engine to detect, classify, and monitor connected IoT and OT devices. The Cato Cloud passively identifies devices by analyzing WAN-bound and outbound traffic, no agents or special setup required. Requires the IoT/OT Security license
  - You can use IoT **Device Attributes** as conditions in WAN and Internet Firewall rules

**Related Articles**

- [Securing Browsing Sessions Through RBI](/v1/docs/securing-browsing-sessions-through-rbi)
- [What is Device Inventory?](/v1/docs/what-is-device-inventory)

### Related Security Services

Cato’s security services extend NGFW functionality with advanced threat prevention, SaaS visibility, and data protection for compliance.

- Intrusion Prevention System (IPS): Detects and blocks exploits and network-based attacks through signature-based and heuristic analysis. Requires the Threat Prevention license
- CASB and DLP: Adds SaaS app visibility and policy enforcement, and data protection to prevent data leakage and meet compliance requirements. Requires CASB or DLP licenses

**Related Articles**

- [Configuring the IPS Policy](/v1/docs/configuring-the-ips-policy)
- [What is the Unified CASB Solution?](/v1/docs/what-is-the-unified-casb-solution)
- [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service)
- [What is the Data Protection API?](/v1/docs/what-is-the-data-protection-api)
