---
title: "Premium Security"
slug: "premium-security"
updated: 2026-08-31T13:15:01Z
published: 2026-08-31T13:15:01Z
canonical: "knowledge.catonetworks.com/premium-security"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Premium Security

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/premium_security.png)

Premium Security extends the connectivity and security capabilities provided by the Base Products with additional advanced security capabilities.

Premium Security capabilities can be purchased as predefined packages for simplified licensing and broader security coverage, or as individual licenses based on the customer’s requirements.

## Licensing and Measurement

Premium Security licenses are either aligned to Base Products or licensed independently, depending on the capability.

Licenses tied to Base Products are sized according to the customer’s protected Base Product scope. This includes the applicable Bandwidth Pool capacity and/or ZTNA Users, with the licensed quantity following the corresponding Base Product measurement unit.

Other capabilities are licensed independently of Base Products according to their own licensing unit and measurement method. These include AI Security for Users, AI Security for Applications, Assets Security, and EPP.

The licensing and measurement requirements for each Premium Security capability are detailed in the corresponding sections of this article.

## Advanced Threat Prevention

Advanced Threat Prevention (ATP) is a bundled security package that includes Threat Prevention (TP) and additional capabilities such as Remote Browser Isolation (RBI) and Sandbox. It provides enhanced protection against advanced, unknown, and evasive threats for traffic across the Cato Cloud, including traffic from sites, users, and cloud resources.

### Capabilities

- Includes all Threat Prevention (TP) capabilities.
- Sandbox - Performs deep inspection and analysis of suspicious and unknown files in a controlled environment to detect zero-day and advanced malware before it reaches users or systems.
- Remote Browser Isolation (RBI) - Isolates web browsing sessions in a remote environment, preventing malicious content from reaching user devices and reducing exposure to web-based threats such as phishing and drive-by downloads.

### Licensing

ATP is licensed based on Bandwidth Pool (sites) and ZTNA Users.

The licensed quantity must cover the total Bandwidth Pool and ZTNA Users across all region groups.

Threat Prevention can be licensed independently. RBI and Sandbox are included only as part of the ATP package.

Usage and fair use follow the measurement of the underlying Base Products.

## Threat Prevention

Threat Prevention provides real-time, inline security inspection and enforcement for traffic across the Cato Cloud, including traffic from sites, remote users, and cloud resources. It enables detection and prevention of known, unknown, and evasive threats for traffic to internet, SaaS, and internal resources.

Threat Prevention includes multiple security engines, such as malware prevention, intrusion prevention (IPS), DNS security, threat intelligence, and AI/ML-based anti-phishing.

Threat Prevention applies to traffic that traverses the Cato Cloud.

### Capabilities

- Inspects traffic across sites, users, and cloud resources
- Multiple security engines inspect for malicious content and threats, including:
  - Malware prevention
  - Intrusion prevention (IPS), including LAN IPS for Socket sites
  - DNS security
  - Threat intelligence
  - AI/ML-based anti-phishing

### Licensing

TP is licensed based on Bandwidth Pool (sites) and ZTNA Users.

The licensed quantity must cover the total bandwidth and ZTNA Users across all region groups.

Usage and fair use follow the measurement of the underlying Base Products.

## Agentic Threat Prevention

Agentic Threat Prevention provides proactive protection against advanced and AI-assisted attacks by using AI agents to anticipate potential attack paths, identify customer-specific exposure, and dynamically adapt protections as threats evolve.

### Capabilities

- Attack path prediction to anticipate how attackers may chain techniques and exploit security gaps.
- Customer-specific protection tailored to the unique exposure and risk profile of each environment.
- Proactive attack prevention that deploys protections before AI-assisted attacks can advance.
- Dynamic protection adaptation that continuously evolves protections as threats and attacker behavior change.

### Licensing

Agentic Threat Prevention is licensed based on Bandwidth Pool and ZTNA Users and requires TP or ATP.

The licensed Bandwidth Pool quantity must cover the total Bandwidth Pool capacity across all region groups, and the licensed ZTNA User quantity must cover the total number of ZTNA Users across the account.

Usage and fair use are determined based on the measurement of the underlying Base Products.

## App & Data Security

App & Data Security provides application visibility and data protection across the Cato Cloud. It enables customers to monitor application usage and prevent unauthorized exposure of sensitive data across the internet, SaaS, and internal resources.

### Capabilities

- Cloud Access Security Broker (CASB) for application visibility and control, including inline and out-of-band inspection
- Data Loss Prevention (DLP) for detection and prevention of sensitive data exposure, including inline and out-of-band inspection

### Licensing

App & Data Security is licensed based on Bandwidth Pool (sites) and ZTNA Users.

The licensed quantity must cover the total bandwidth and ZTNA Users across all region groups.

CASB and DLP can be licensed individually or as part of the App & Data Security package.

Usage and fair use follow the measurement of the underlying Base Products.

## CASB

Cloud Access Security Broker (CASB) provides visibility and control over the use of cloud and SaaS applications for Internet and SaaS traffic protected by Internet Security. It enables organizations to discover application usage, assess risk, and enforce policies to govern access and data usage.

### Capabilities

- Inline CASB for real-time visibility and policy enforcement
- Out-of-band CASB using supported third-party integrations
- Discover and classify cloud and SaaS applications
- Policy enforcement for application usage and access control

### Licensing

CASB is licensed based on Bandwidth Pool (sites) and ZTNA Users.

The licensed quantity must cover the total bandwidth and ZTNA Users across all region groups.

CASB can be licensed individually or as part of App & Data Security.

Usage and fair use follow the measurement of the underlying Base Products.

## DLP

Data Loss Prevention (DLP) provides controls to detect and prevent unauthorized exposure of sensitive data across the Cato Cloud. It enables organizations to identify, monitor, and control the movement of sensitive data across applications and destinations.

### Capabilities

- Inline DLP for real-time inspection and enforcement
- Out-of-band DLP using supported third-party integrations
- Detect and control of sensitive data movement across the internet, SaaS, and internal resources

### Licensing

DLP is licensed based on Bandwidth Pool (Mbps) and ZTNA Users.

The licensed quantity must cover the total bandwidth and ZTNA Users across all region groups.

DLP must be purchased with CASB at the same quantity or as part of App & Data Security.

Usage and fair use follow the measurement of the underlying Base Products.

## AI Security for Users

AI Security for Users provides visibility, governance, and runtime protection for how users interact with public AI services and local AI agents. It enables organizations to discover AI usage, enforce acceptable-use and data protection policies, and secure user interactions with AI tools and agents.

### Capabilities

- User-to-AI visibility, including Shadow AI discovery, AI services accessed, and data shared.
- Runtime policy enforcement to control acceptable use, prevent data exposure, and block policy violations.
- AI Security Posture Management (AI-SPM) for local agents, including visibility into configuration, skills, and MCP server security.
- Runtime safeguards for local AI agents, including controls for prompts and tools.
- AI Security for Users can protect users connecting through the Browser Plugin, Cato Client, Cato Enterprise Browser, and SSE Cloud Proxy Chaining, as well as users located behind a Cato Socket.

### Licensing

AI Security for Users is licensed per user. Users represent the total number of users protected with AI Security.

AI Security for Users can be purchased independently and does not require Bandwidth Pool or ZTNA Users.

## AI Security for Applications

AI Security for Applications provides runtime protection, posture management, governance, and compliance for homegrown AI applications and managed agents across cloud, on-premises, and private-cloud environments.

### Capabilities

- Runtime protection for homegrown AI applications and agents across cloud, on-premises, and private-cloud environments.
- AI Security Posture Management (AI-SPM) for managed agents, providing posture management and visibility into AI agents and their configurations.
- AI Security for Applications supports deployment and integration through Cato AI Gateway, AI Gateway integrations, custom APIs, and agent platform APIs.

### Licensing

AI Security for Applications is licensed based on the total number of employees in the organization, typically aligned with the number of business SaaS users.

The licensed quantity must be equal to or greater than the licensed quantity of AI Security for Users.

AI Security for Applications can be purchased independently and does not require Bandwidth Pool or ZTNA Users.

## Assets Security

Assets Security provides visibility and security insights for connected devices across the Cato Cloud. It enables the identification and classification of devices and applies device-level context to enforce policies across WAN, Internet, and LAN environments. It also supports micro-segmentation to enforce granular access controls between devices and resources within LAN environments (via Sockets).

### Capabilities

- Device visibility and discovery, including device identification
- Device classification and enforcement within policy rules
- Enforce device-aware rules across all existing WAN, LAN, and Internet Firewall policies
- Enforce LAN micro-segmentation for Socket sites
- Integrate with third-party device management and discovery systems

### Licensing

Assets Security is licensed by device blocks. Devices represent the total number of unique identified devices that send or receive traffic through the Cato Cloud or the local LAN environment.

Device measurement includes devices identified through inline traffic as well as devices discovered through supported out-of-band third-party providers that forward traffic through the Cato Cloud.

Assets Security is licensed independently of Bandwidth Pool and ZTNA Users.

## 

## EPP

Endpoint Protection Platform (EPP) provides endpoint-level threat prevention and malware protection for user devices. EPP extends security coverage beyond network traffic by protecting endpoints directly and centralizing endpoint security management within the Cato Management Application.

EPP protects endpoints independently of network connectivity and does not require the Cato Client for network access. Endpoint security policies, alerts, and events are managed centrally alongside network, access, and security policies.

### Capabilities

- Endpoint malware prevention and threat detection
- Policy-based endpoint protection using centrally managed profiles
- Behavioral analysis and signature-based threat detection
- Centralized visibility and alerting integrated with network and security events
- Unified management of endpoint, user, and network security from a single platform

### Licensing

EPP is licensed by users. Users represent the total number of users protected by EPP across the customer environment.

The licensed user quantity is typically aligned with the number of business SaaS users in the organization (for example, Microsoft 365 users).

EPP can be licensed independently and does not require Base Products. EPP protection applies directly to endpoints and operates independently of network connectivity.

Due to regional restrictions, devices located in China cannot register with the Cato EPP service.

## Premium Security Licensing Summary

| **Security License** | **Licensed by** |
| --- | --- |
| Threat Prevention | Bandwidth Pool and ZTNA Users |
| Advanced Threat Prevention | Bandwidth Pool and ZTNA Users |
| Agentic Threat Prevention | Bandwidth Pool and ZTNA Users |
| App & Data Security | Bandwidth Pool and ZTNA Users |
| CASB | Bandwidth Pool and ZTNA Users |
| DLP | Bandwidth Pool and ZTNA Users |
| Assets Security | Device Blocks |
| EPP | Users |
| AI Security for Users | Users |
| AI Security for Applications | Employees |
