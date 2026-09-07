---
title: "How Cato Threat Protection Protects Your Network"
slug: "how-cato-threat-protection-protects-your-network"
updated: 2026-08-27T11:26:57Z
published: 2026-08-27T11:26:57Z
canonical: "knowledge.catonetworks.com/how-cato-threat-protection-protects-your-network"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How Cato Threat Protection Protects Your Network

## Overview

Cato Threat Prevention is a cloud-native security service that inspects WAN and Internet traffic in the Cato Cloud to detect and block malicious files, malware, network-based attacks, and other security threats. Threat Prevention helps secure your traffic by preventing malware, blocking malicious domains and destinations, detecting exploit attempts and other attack activity, and stopping threats before they can impact users or resources. You can extend this protection with Advanced Threat Prevention services such as Remote Browser Isolation (RBI), which isolates web sessions from the user’s device, and Sandbox, which scans suspicious files in an isolated environment for deeper analysis.

### Shared Context for Stronger Threat Protection

Cato's security engines work together in a single cloud-native service to deliver more accurate detections, more consistent enforcement, and stronger protection across the full threat lifecycle. Rather than making isolated decisions, the engines inspect the same traffic and build on shared analysis across multiple protection layers. This unified architecture improves coordination between security controls and helps stop threats before they can spread or cause damage.

#### Related Articles

- [Understanding Packet Flow with Cato SPACE Architecture](/v1/docs/understanding-packet-flow-with-cato-space-architecture)

### AI and Machine Learning in Threat Prevention

Cato Threat Prevention also uses AI and machine learning as part of the service infrastructure to improve threat intelligence and strengthen detection quality. This includes AI-based IOC classification, machine learning analysis of traffic metadata, machine learning protections in IPS for threats, and Agentic Threat Prevention. Together, these capabilities strengthen detection across protection engines and help Cato identify both known and unknown threats more effectively.

## TLS Inspection

Complete threat inspection requires TLS Inspection, so encrypted traffic can also be analyzed.

Cato decrypts, inspects, and re-encrypts traffic in-line so Threat Prevention and Advanced Threat Prevention services can analyze encrypted traffic, including Anti-Malware, IPS, and Sandbox. This extends threat inspection to encrypted sessions and allows more traffic to be evaluated by the full set of protection layers. Granular Inspect and Bypass rules help you maintain security coverage while excluding traffic that should not be inspected.

Because TLS Inspection can impact user experience for legitimate sites, Cato provides a TLS Inspection configuration wizard that helps you deploy recommended Inspect and Bypass rules more quickly while customizing the policy for your environment.

### Traffic Bypassing the Cato Cloud

Threat Prevention engines run in the PoPs in the Cato Cloud and only inspect traffic that passes through them. Traffic that bypasses the Cato Cloud, such as MPLS traffic or traffic from sites and Clients that egress directly to the public Internet, is not inspected by Threat Prevention or Advanced Threat Prevention services. This traffic is outside the scope of Cato’s inline threat inspection.

### Related Articles

- [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account)
- [Best Practices for TLS Inspection](/v1/docs/best-practices-for-tls-inspection)

## Threat Protection Services

These services work together to deliver layered protection, combining signature-based detection, behavioral analysis, and machine learning to identify both known and unknown threats. As they all operate in the Cato Cloud as part of a single security architecture, each layer adds to a broader and more coordinated view of threat activity. Centralized management in the CMA lets you easily configure policies, monitor events, and maintain visibility across all protected traffic.

### Intrusion Prevention System (IPS)

Cato IPS inspects inbound, outbound, and WAN traffic to protect applications, devices, and network services against known vulnerabilities, bots, malicious traffic, and other network-based attacks. The service includes multiple protection layers such as reputation analysis, known vulnerability protections, anti-bot detection, network behavioral analysis, protocol validation, geo restriction, and tunneling attack detection.

IPS signatures are continuously updated by Cato security research, and IPS policies are designed to balance security coverage with operational stability. IPS can enforce protections in block mode or monitor traffic without blocking, and it helps prevent exploitation of known vulnerabilities across traffic that passes through the Cato Cloud.

#### Related Articles

- [Configuring the IPS Policy](/v1/docs/configuring-the-ips-policy)

### DNS Protection

The IPS service includes DNS Protection to enforce DNS security for traffic in your account. DNS Protection blocks DNS requests to malicious domains before a connection is established to the destination, which helps stop threats such as phishing, malware delivery, and command-and-control communication earlier in the attack flow. By blocking malicious requests at the DNS layer, DNS Protection helps stop attacks before payload delivery and provides visibility that supports broader threat investigation.

You can enable or disable specific DNS protections and define actions such as Allow, Block, or Sinkhole for each protection. The Sinkhole action redirects DNS requests for malicious domains to a sinkhole server instead of the original destination. This also helps identify the originating endpoint for the request, including in environments that use internal DNS proxies, and supports detection of potentially infected devices.

#### Related Articles

- [Customizing the DNS Protections for IPS](/v1/docs/customizing-the-dns-protections-for-ips)

### Suspicious Activity Monitoring (SAM)

Suspicious Activity Monitoring expands IPS visibility for suspicious network activity that is not monitored by standard IPS signatures. SAM identifies activity that can indicate a compromise or breach, but because the traffic is not definitively malicious, it monitors the traffic without blocking it.

By correlating events over time, SAM reduces noise and gives security teams better visibility into early-stage attack activity. This helps you identify threats that are not detected by IPS signature-based controls. This adds investigative context for activity that may not trigger direct prevention and helps identify threats that signature-based controls alone might miss.

#### Related Articles

- [Monitoring Suspicious Activity with IPS (SAM)](/v1/docs/monitoring-suspicious-activity-with-ips-sam)

### Anti-Malware and NG Anti-Malware

Cato Anti-Malware and NG Anti-Malware provide two layers of protection to prevent malicious files from entering your network. Both layers simultaneously scan files from WAN and Internet traffic.

Anti-Malware uses known file signatures and heuristic analysis to detect malicious files. NG Anti-Malware uses machine learning and predictive models to classify files as benign, suspicious, or malicious and detect unknown and zero-day malware. This layered approach blocks ransomware, trojans, and other commodity malware without impacting user experience.

#### Related Articles

- [What is the Cato Anti-Malware Policy?](/v1/docs/what-is-the-cato-anti-malware-policy)
- [Configuring the Anti-Malware Policy](/v1/docs/configuring-the-anti-malware-policy)

## Advanced Threat Prevention

Advanced Threat Prevention services provide additional protection against sophisticated threats that may bypass standard Threat Prevention controls. These services extend Cato’s protection with isolated browsing, advanced file analysis, and behavior-based prevention to help detect and stop sophisticated attack techniques.

### Remote Browser Isolation (RBI)

RBI is part of the Internet Firewall policy and protects users from web and browser-based threats without blocking Internet access. Instead of rendering web content on the user’s device, RBI runs the browsing session in an isolated environment in the Cato Cloud and streams a safe visual representation to the browser. This helps protect against threats such as ransomware, malware, phishing, malicious ads, and cross-site scripting (XSS), while letting users safely access risky or unknown websites. RBI extends protection to risky browsing activity without forcing users to bypass security controls.

#### Related Articles

- [Securing Browsing Sessions Through RBI](/v1/docs/securing-browsing-sessions-through-rbi)
- [Configuring the RBI Service for Browsing Sessions](/v1/docs/configuring-the-rbi-service-for-browsing-sessions)

### Agentic Threat Prevention

Agentic Threat Prevention uses AI agents to identify and prevent emerging threats based on behavior and context across your environment. The service analyzes account telemetry over time to identify suspicious behavior and predict potential next steps in an attack. It then applies targeted restrictions to prevent those actions before they can cause damage.

Agentic Threat Prevention complements other security engines by using broader context and multiple signals to identify threats that single-flow analysis may miss. Restrictions are continuously adapted based on observed behavior, helping reduce the attack surface while minimizing impact on legitimate activity.

#### Related Articles

- [What is Agentic Threat Prevention?](/v1/docs/what-is-dynamic-prevention)
- [Managing Agentic Threat Prevention](/v1/docs/managing-dynamic-prevention)
- [Monitoring Agentic Threat Prevention](/v1/docs/managing-agentic-threat-prevention)

### Sandbox

Sandbox is an isolated and secure environment where potentially malicious or suspicious files are executed and analyzed without risk to your network. This adds in-depth analysis for malware investigation to detect unknown and evasive threats. Files identified by the Anti-Malware policy as malicious or suspicious are automatically scanned in the Sandbox, and you can also upload specific files for analysis.

#### Related Articles

[Scanning Files in the Sandbox](/v1/docs/scanning-files-in-the-sandbox)

## MITRE ATT&CK® Dashboard

The MITRE ATT&CK framework is a knowledge base of adversary tactics and techniques that helps security teams classify and investigate attack activity. The Cato MITRE ATT&CK Dashboard provides visibility into attack activity in your network using the MITRE ATT&CK framework. It maps threats detected by Cato security services to ATT&CK tactics and techniques, helping security teams understand how attacks progress across the kill chain. The dashboard includes analytics and visualizations such as tactic summaries, technique breakdowns, event timelines, and affected devices. You can drill down into specific techniques or sources to investigate security events and analyze attack patterns in your environment. This helps connect individual detections to the broader attack story and gives security teams a clearer view of how threats unfold across the environment.

### Related Articles

[Using the MITRE ATT&CK® Dashboard](/v1/docs/using-the-mitre-att-ck-dashboard)
