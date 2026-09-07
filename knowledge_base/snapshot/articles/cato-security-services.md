---
title: "Cato Security Services"
slug: "cato-security-services"
updated: 2026-08-27T11:28:27Z
published: 2026-08-27T11:28:27Z
canonical: "knowledge.catonetworks.com/cato-security-services"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Security Services

## Introduction

Enterprise security can no longer rely on static controls operating in isolation. Modern attacks increasingly span identities, networks, SaaS applications, endpoints, and data at the same time. Attackers blend techniques across these domains to evade detection, abuse trusted applications, and move laterally with speed. In this environment, the challenge is no longer a lack of tools. It is a lack of shared context.

That is the foundation of Cato Networks’ security approach. Cato delivers a unified, cloud-native security platform built to apply protection using real-time context across users, devices, applications, data, location, and behavior. Rather than stitching together separate point products, Cato converges security and networking on the same cloud-native architecture so policies, telemetry, and enforcement work together. This enables more accurate decisions, fewer blind spots, and faster response.

A core advantage of the Cato platform is its context-aware, single-pass design. Because traffic is processed once in a shared engine, Cato can apply multiple layers of inspection and enforcement consistently and efficiently across the Internet, WAN, cloud, SaaS, and remote access traffic. This shared-context model strengthens threat prevention, improves zero-trust access decisions, enhances data protection, and simplifies operations through a single management experience.

Cato’s security platform is built for hybrid work, cloud-first applications, unmanaged devices, SaaS sprawl, Shadow IT, Shadow AI, and increasingly dynamic threats. Its protections are automated by default, multi-layered by design, and cloud-delivered at global scale. The result is a security architecture that helps enterprises reduce attack surface, contain threats earlier, and maintain consistent policy enforcement across all users and environments.

The graphic below illustrates the high-level architecture of the Cato platform, showing how security capabilities operate as a unified, context-aware service delivered from a single cloud-native architecture.

![image1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35484064809373(1).png)

### Executive Summary

| Focus Area | Positioning Summary |
| --- | --- |
| **Architecture** | Single cloud-native platform with single-pass inspection and shared context across networking and security. |
| **Security model** | Context-aware, automated, multi-layered protection spanning users, devices, apps, data, and network activity. |
| **Core controls** | FWaaS, SWG, IPS, Malware Prevention, DNS Security, RBI, CASB, DLP, ZTNA, IoT/OT Security, XOps, and MDR. |
| **Operating model** | One management application, one data lake, and one policy framework for prevention, investigation, and response. |

## Security Platform Capabilities

### SSE 360: Security as a Service

Cato SASE Cloud Platform includes a cloud-native security stack, SSE 360, that converges network segmentation and zero trust, threat prevention, application protection, and data protection into a single service. It brings together FWaaS, SWG, IPS, Malware Prevention, DNS Security, RBI, CASB, DLP, and ZTNA under one platform and one management experience.

Unlike legacy architectures that depend on separate appliances and point products, Cato is designed to decrypt and inspect enterprise traffic at scale without sizing, patching, or upgrading hardware. This allows organizations to apply security consistently across sites, users, cloud resources, and SaaS access while centrally managing policies, analytics, and events through the Cato Management Application.

### Network Segmentation and Zero Trust

Firewall as a Service is the foundational enforcement layer of the Cato security platform. It controls traffic across WAN, internet, and internal environments, and supports segmentation based on both network constructs and logical business context, such as identity, organizational unit, application, service, and device posture.

This approach helps customers move beyond simple network-based controls toward true zero-trust principles. Access can be governed using who the user is, what they are trying to access, how they are connecting, from where, and under what risk conditions. Continuous inspection combined with segmentation reduces lateral movement and sustains a least-privilege posture.

### Multi-Layer Threat Prevention

Cato applies defense in depth across the platform. Its threat prevention stack includes SWG, IPS, Malware Prevention, DNS Security, and RBI, all operating within the same cloud-native inspection framework. This layered approach matters because modern attacks do not rely on a single vector. They often involve phishing, malicious domains, payload delivery, account abuse, lateral movement, and data exfiltration in sequence.

Cato’s context-aware architecture strengthens this model by allowing threat prevention to use signals from identity, network, application, device, and data activity. That improves efficacy against both known and emerging threats while reducing false positives and operational overhead.

### IoT/OT Security

Cato extends platform protection to IoT and OT environments through native device discovery, classification, policy enforcement, and threat prevention. AI and ML fingerprint connected devices to identify type, manufacturer, and version, enabling organizations to eliminate blind spots and apply granular access controls to previously unmanaged assets.

Because IoT/OT Security is native to the platform, customers do not need to deploy separate products or build complex integrations. IoT and OT protections benefit from the same management, visibility, and prevention architecture used across the rest of the enterprise.

### Application and Data Protection

Cato protects application access and sensitive data across inline and API-based channels. CASB provides visibility into sanctioned and unsanctioned cloud applications, supports granular access policies, and extends control to SaaS usage and tenant restrictions. DLP identifies and governs sensitive data movement across web, SaaS, and private application traffic.

This protection is reinforced by shared context. Cato can make decisions based not only on the content being accessed or moved, but also on user identity, device trust, application risk, connection method, and behavioral indicators. That enables more adaptive and precise enforcement than isolated DLP or CASB tools.

### Cato Client for Endpoints

Cato extends secure access and endpoint protection to user devices through the Cato Client, available across major operating systems. The client supports granular traffic steering, always-on connectivity, and continuous protection for corporate endpoints. It also serves as a key enforcement point for user identity, posture validation, secure remote access, and endpoint telemetry.

### Hybrid and Remote Work

Cato’s Universal ZTNA capability ensures that access policy follows the user everywhere: in the office, at home, or on the road. Users are continuously evaluated based on identity, posture, and risk before and during access sessions. Once connected, all traffic is inspected by the same SSE 360 stack used for branch and site traffic, ensuring consistent threat prevention and data protection for remote users.

### Endpoint Protection, Detection, and Response

The Cato EPP Agent for Cato EDR includes endpoint protection, detection, and response capabilities, adding next-generation anti-malware and suspicious activity correlation directly on the device. Endpoint telemetry is combined with network and security context in the Cato data lake, allowing XOps to present more accurate incidents and improve investigation and remediation.

### Incident Life Cycle Management

Cato supports the full Threat Detection, Investigation, and Response lifecycle using AI-assisted incident handling. Incidents are enriched with human-readable narratives, correlated evidence, investigation guidance, and timeline-based analysis within the analyst workbench. For organizations that prefer external support, Cato and partners also provide MDR services for timely detection, guided remediation, and optional preventive action.

### Cato Management Application

All Cato capabilities are administered through the Cato Management Application (CMA). It provides unified policy management, analytics, event investigation, monitoring, and troubleshooting across networking and security. This single management layer is critical to the platform value proposition: current and future capabilities are managed consistently, which simplifies adoption and reduces operational complexity.

### Cato Universal API and Third-Party Integration

[Cato provides an API](/v1/docs/what-is-the-cato-api) for automation, integration, and data sharing. Customers can automate provisioning, policy creation, and object management, and export selected data for external workflows, analytics, or reporting. Formal integrations with third-party systems further support operational alignment with broader security and IT processes.

## Security Platform Products and Features

### 

### Firewall Security

#### Firewall-as-a-Service (FWaaS)

[Cato FWaaS](/v1/docs/what-is-the-cato-firewall) delivers cloud-native firewall protection across the Internet, WAN, and LAN traffic without the constraints of physical or virtual firewalls. It inspects all traffic across ports, protocols, and encrypted sessions, eliminating the blind spots and fragmented enforcement common in legacy architectures.

Because FWaaS is part of the Cato platform, it benefits from shared context and unified policy. Rules can use rich objects such as user identity, device, organization, host, application, protocol, location, network, and VLAN. This supports granular segmentation and zero-trust enforcement across the enterprise. Cato further extends firewall administration with Autonomous Policies for FWaaS, using AI-driven analysis to identify misconfigurations, optimize rulesets, and support continuous zero-trust enforcement. The result is stronger control, fewer manual errors, and policy management that scales with enterprise complexity.

Additional strengths include full logging and monitoring, centralized audit trails, cloud-scale performance, support for microsegmentation, and DPI-based visibility into applications and users from the first packet.

#### Secure Web Gateway (SWG)

[Cato SWG](/v1/docs/what-is-the-cato-internet-firewall) protects users against risky and malicious web destinations while enforcing enterprise browsing policies based on content category and risk. It includes pre-defined policies and more than 80 built-in website categories, enabling rapid deployment and immediate enforcement of best-practice controls.

Cato SWG also strengthens protection against phishing and malware delivery sites by maintaining current intelligence on malicious, compromised, phishing, and parked domains. It helps prevent policy circumvention through support for Safe Search and YouTube restriction controls, and improves user experience with customizable block and prompt pages. All activity is logged into the Cato data lake, giving administrators strong visibility for auditing, reporting, and policy tuning.

Within the broader platform, SWG is one layer in a multi-layer threat prevention model. It works alongside IPS, DNS Security, RBI, CASB, and DLP to reduce exposure and improve overall resilience.

### Threat Prevention

#### 

#### Intrusion Prevention System (IPS)

[Cato IPS](/v1/docs/configuring-the-ips-policy) provides real-time protection across Internet, WAN, and cloud traffic to stop ransomware, lateral movement, malicious communications, and exploit activity. It combines signatures, threat intelligence, heuristics, and inline AI/ML to prevent attacks across both known and unknown techniques.

Cato IPS also supports phishing and malware protection using AI/ML, virtual patching for fast mitigation of emerging CVEs, cloud-scale TLS inspection, geofencing for attack surface reduction, and a heuristics language designed to use platform context such as app ID, URL category, user identity, target risk, and device fingerprint. Automated threat intelligence management based on 250+ feeds helps keep protections current with near-zero customer effort.

#### Agentic Threat Prevention

[Agentic Threat Prevention](/v1/docs/what-is-agent-threat-prevention) uses AI agents to identify and prevent emerging threats based on behavior and context across your environment. The service analyzes account telemetry over time to identify suspicious behavior and predict potential next steps in an attack. It then applies targeted restrictions to prevent those actions before they can cause damage.

Agentic Threat Prevention complements other security engines by using broader context and multiple signals to identify threats that single-flow analysis may miss. Restrictions are continuously adapted based on observed behavior, helping reduce the attack surface while minimizing impact on legitimate activity.

#### Malware Prevention

Cato Malware Prevention combines [next-generation anti-malware](/v1/docs/what-is-the-cato-anti-malware-policy) with [sandbox analysis](/v1/docs/scanning-files-in-the-sandbox) to deliver layered malware defense. The platform detects known, unknown, zero-day, and polymorphic malware in real time, while suspicious files can be detonated in a sandbox to produce behavioral analysis and forensic insights.

Because it runs in the Cato Cloud, malware inspection can be applied broadly, including on TLS-encrypted traffic, without appliance sizing constraints. Policies are simple to manage and can be tuned by source, destination, application, and traffic type. Support for nested archives and encrypted file handling further reduces common evasion paths. The result is comprehensive malware prevention at scale, supported by up-to-date signatures, heuristics, and deep behavioral analysis.

#### DNS Security

[Cato DNS Security](/v1/docs/customizing-the-dns-protections-for-ips) inspects DNS traffic to block phishing sites, malicious domains, command-and-control communications, DNS tunneling, and crypto-mining activity before a connection is established. It serves as an important early prevention layer because many attacks begin with DNS resolution.

Cato uses AI and ML to identify domain squatting, impersonation attempts, suspicious patterns, and tunneling behavior. Its optimized threat intelligence helps block malicious domains and C2 sites in real time, while centralized logging and visibility enable security teams to investigate DNS-based threats through the same management interface used for all other protections.

Although DNS Security is part of Cato’s broader threat prevention architecture and closely aligned with IPS, it is presented here as a distinct capability due to its dedicated DNS-layer controls, visibility, and policy enforcement.

#### Remote Browser Isolation (RBI)

[Cato RBI](/v1/docs/securing-browsing-sessions-through-rbi) enables safe access to uncategorized or risky websites by isolating browsing sessions in a remote, containerized environment. Instead of executing website code on the endpoint, RBI streams only a visual representation to the user's browser. This reduces the risk of malware delivery, credential theft, and browser-based compromise.

Because RBI is instantly available from the cloud, organizations can deploy it quickly without new infrastructure. It provides a practical middle ground between allowing and blocking risky sites outright, preserving productivity while reducing exposure. Integrated logging and policy controls help administrators understand usage patterns and adjust enforcement as needed.

RBI complements Cato’s SWG and broader Internet security controls, but is presented here as a distinct capability because it adds a dedicated isolation-based protection layer for risky web access.

#### IoT/OT Threat Prevention

[Cato IoT/OT Threat Prevention](/v1/docs/what-is-device-inventory) extends visibility, access control, and threat prevention to connected operational and embedded devices. Native AI/ML-based discovery and fingerprinting identify devices by type, manufacturer, and model, giving teams the visibility needed to secure a critical and often under-managed attack surface.

Granular policies can restrict device access to internal or external resources, while the broader threat prevention stack protects IoT and OT devices from known and zero-day threats. Because the capability is fully integrated into the Cato platform and management interface, it reduces sprawl and eliminates the integration burden typically associated with separate IoT/OT tools.

### Data and Application Protection

#### Cloud Access Security Broker (CASB)

[Cato CASB](/v1/docs/what-is-the-unified-casb-solution) gives organizations visibility and control over cloud application usage across both inline and API-based channels, including sanctioned applications, Shadow IT, and Shadow AI. It continuously monitors internet traffic to identify cloud app usage, classify applications, assess risk, and help IT teams distinguish approved from unapproved services.

CASB is especially important for modern SaaS-heavy environments. Cato uses ML-based application risk analysis to build detailed cloud app profiles with relevant security and compliance context. It also enables granular inline and API-based controls over user actions such as login, view, upload, and download. This lets organizations govern what users do inside cloud applications, not just whether they can access them.

Cato CASB also supports SaaS tenant restriction to reduce the risk of employees moving sensitive data into personal accounts within otherwise sanctioned applications. Together, these capabilities support adaptive SaaS access decisions based on user risk, device trust, and application posture.

Cato CASB also includes API-based capabilities that provide out-of-band visibility into sanctioned SaaS applications, including:

- Extended monitoring and governance for user activity, even when traffic does not traverse the Cato Cloud.
- Visibility for direct-to-cloud access.
- Coverage for unmanaged devices.
- Visibility in environments where TLS inspection is not enabled.

Through App Activities integrations, Cato captures granular audit events across connected SaaS applications and presents them in a unified view, enabling security teams to monitor actions such as logins, downloads, permission changes, sharing activity, administrative actions, and other sensitive operations.

API-based CASB also strengthens governance by improving visibility into application ecosystems, including interconnected SaaS applications, extensions, and plugins. This helps organizations better understand how sanctioned SaaS platforms are being used, what third-party integrations may introduce risk, and where suspicious or non-compliant activity may require investigation or policy response.

Together, Cato’s inline and API-based CASB capabilities provide more complete SaaS security coverage across managed, unmanaged, and direct-access scenarios.

#### Data Loss Prevention (DLP)

[Cato DLP](/v1/docs/what-is-the-cato-dlp-service) provides consistent data protection across users, locations, web traffic, SaaS applications, and private applications. It is designed to help organizations protect intellectual property, reduce accidental and malicious data leaks, and support regulatory requirements such as GDPR, PCI DSS, and HIPAA.

A major strength is its broad classification capability. Cato includes more than 350 pre-defined data types, along with support for custom data types, Exact Data Match, keywords, regex, labels such as Microsoft Information Protection, and OCR for image-based content. This enables organizations to identify sensitive data in many real-world business formats and scenarios.

Cato applies DLP both inline and through API-based inspection. Inline controls provide real-time governance over data in motion across web, SaaS, and private application traffic. API-based Data Protection extends this coverage with out-of-band content inspection for sanctioned cloud applications, allowing organizations to monitor and react to sensitive data exposure even when traffic does not traverse the Cato Cloud. This is particularly valuable for BYOD scenarios, unmanaged devices, remote users connecting directly to SaaS applications, and cases where the Cato Client is not operating in always-on mode.

API-based DLP also improves coverage for applications and sessions that are difficult to inspect inline, including scenarios where TLS inspection is disabled or where certificate pinning limits inline inspection. Using the same underlying data classification engines as inline DLP, Cato enables consistent detection across both channels while adding near real-time visibility into cloud content, sharing activity, and misconfigurations. Together, inline and API-based DLP provide broader and more resilient protection for sensitive data across managed and unmanaged access scenarios.

#### Universal Zero Trust Network Access (ZTNA)

Cato Universal ZTNA allows organizations to define a single risk-based access policy and enforce it consistently across office, home, remote, and hybrid users. Instead of granting broad network access, Cato applies per-user and per-application decisions based on identity, device posture, geography, application sensitivity, and other contextual risk signals.

[Continuous posture evaluation](/v1/docs/implementing-adaptive-access-with-cato) is central to this model. Cato checks device compliance at connection and throughout the session, and can block or terminate access when posture degrades. This reduces the likelihood of compromised or non-compliant devices becoming a path to sensitive applications or data.

Cato extends this model to unmanaged devices and third parties through browser-based access and the Cato Browser Extension. It also improves user experience by leveraging the Cato global private backbone and optimization capabilities, reducing the performance issues often associated with legacy remote access and backhauled inspection.

All session traffic is continuously inspected by the Cato security stack, which means ZTNA is not isolated from the rest of the platform. Access, threat prevention, and data protection work together within one policy and one architecture.

#### Cato Enterprise Browser

[Cato Enterprise Browser](/v1/docs/what-is-the-cato-enterprise-browser) provides secure, policy-controlled access to public SaaS and private WAN applications from unmanaged devices without requiring installation of the Cato Client. It is designed for contractors, partners, guest users, and BYOD scenarios where organizations need to extend secure access without relying on full endpoint management.

Because it is fully integrated into the Cato platform, Enterprise Browser traffic is routed through Cato’s globally distributed PoPs and inspected by the same Single Pass Cloud Engine (SPACE). This allows organizations to apply the same Internet Firewall, CASB, and Data Protection policies used for managed devices, ensuring consistent enforcement across different user types and access methods.

Cato Enterprise Browser also enables browser-level controls such as restricting copy and paste, file downloads, printing, and unauthorized browser extensions. This helps reduce the risk of data leakage and browser-based threats while maintaining a controlled and productive user experience.

#### Cato Browser Extension

[The Cato Browser Extension](/v1/docs/what-is-the-cato-browser-extension) extends secure browser-based access to unmanaged and BYOD users such as contractors, partners, and temporary workers. It gives organizations a practical way to apply zero trust access and full-stack inspection to users who cannot or should not install a full client.

Because the extension is part of the same platform, it applies the same centrally managed policies and inspection logic used for client-based and site-based access. This delivers operational consistency without separate products or consoles. It also improves onboarding speed and user experience by allowing secure access from the existing browser, with traffic still benefiting from the Cato backbone and security inspection stack.

### Detection and Response

#### XOps

[Cato XOps](/v1/docs/welcome-to-the-cato-xops-service) is the AI layer that helps customers quickly detect and resolve security and network issues by transforming millions of raw events into correlated, consumable incident stories. It spans both security and network operations, automatically processing events from licensed Cato capabilities, add-ons, and connected third-party tools.

Its value comes from correlation and shared context. Instead of forcing analysts to manually stitch together data from separate products, XOps presents incidents across users, devices, applications, and locations with relevant context and risk-based prioritization. This helps NOC and SOC teams collaborate more effectively, reduce alert fatigue, and respond faster.

#### Cato Detection & Response as Part of XOps

[Cato Detection & Response](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench), as part of XOps, is a SASE-based detection and response capability that uses the platform’s native sensors and massive data lake to improve detection, investigation, and remediation. It aggregates prevention events into meaningful incidents, helping teams see through alert volume and focus on likely compromise.

Threat hunting incidents are created by AI/ML models that scan for anomalous indicators of threats that bypassed prevention layers. Cato also applies behavior analytics to identify suspicious user and entity activity, with risk scoring to help teams prioritize investigation.

To accelerate triage, Cato uses GenAI to generate human-readable incident narratives and maps activity to MITRE ATT&CK techniques. This helps teams understand what happened, how far an attack progressed, and what response steps are needed. Because XDR is native to the platform, remediation actions such as containment firewall rules or endpoint scans can be triggered within the same interface.

An additional advantage is the breadth of native sensor data. Cato XDR draws from FWaaS, SWG, IPS, NGAM, DNS Security, CASB, DLP, RBI, endpoint telemetry, and more, all collected into a single data lake. This produces richer incidents and more accurate analytics than tools dependent on reduced or disconnected telemetry. External data from third-party EDR tools can also be incorporated, supporting an open architecture.

#### CMA as a Unified Console for Threat Detection, Investigation, and Response

Cato supports the full incident lifecycle from detection through investigation, response, and follow-up within the CMA. Analysts can review incident stories, inspect timelines, collaborate around findings, and take remediation steps without pivoting across multiple consoles from different providers.

This unified operating model is particularly valuable for phishing investigations and other cross-domain threats. Events from internet security, DNS protection, RBI, CASB, and ZTNA can be correlated into one story, allowing analysts to trace attacks across services and adjust policies from the same console.

#### MDR

For organizations that want expert support, Cato and its partners provide MDR services. These services include timely threat detection, remediation guidance, and optional preventive measures. MDR helps reduce dwell time, lowers the burden on internal teams, and extends the value of the platform’s detection and response capabilities.

## Why the Cato Platform Architecture Matters

Cato’s product capabilities are important, but the real differentiator is how they work together. The platform is designed around shared context and single-pass inspection, not around loosely connected point products.

That matters because security decisions are only as effective as the context behind them. In the Cato platform, networking and security share the same data plane, so signals from identity, device posture, application behavior, network flows, and data activity can inform both prevention and response. Context is not stitched together after the fact. It flows across the platform by design.

This architecture also enables operational simplicity. Policies are managed centrally and enforced consistently across Cato’s globally distributed PoP architecture, while traffic is inspected once in the cloud through Cato’s single-pass model. Events are stored in a common data lake for analytics and response. Organizations gain consistent enforcement, correlated detection, fewer blind spots, and reduced infrastructure burden. That is especially important in cloud-first, SaaS-heavy, hybrid-work environments where complexity itself becomes a risk factor.

In practical terms, Cato helps enterprises move from fragmented and reactive security toward security that is context-aware, automated, multi-layered, and cloud-delivered by design.

## Conclusion

Cato Networks provides a unified security platform built to address how enterprises operate today and how threats evolve now. Its capabilities span network segmentation, zero trust access, web and threat prevention, SaaS governance, data protection, endpoint security, and AI-assisted detection and response. But more importantly, these are not isolated products. They operate as one platform with one architecture, one management layer, and one shared context model.
