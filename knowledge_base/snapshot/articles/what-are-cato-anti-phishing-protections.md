---
title: "What are Cato Anti-Phishing Protections?"
slug: "what-are-cato-anti-phishing-protections"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/what-are-cato-anti-phishing-protections"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What are Cato Anti-Phishing Protections?

## Overview

Phishing remains a leading cause of credential theft and malware delivery, even in organizations that deploy advanced email and browser protections. Attackers continue to evolve their techniques to bypass security controls and exploit user trust.

Cato provides comprehensive layers of security services, including web, cloud, and Zero Trust Network Access (ZTNA) protections, to detect and block phishing attempts, minimize user exposure, and help you identify and remediate attacks quickly.

You manage and visualize all phishing-related detections, policies, and events in the Cato Management Application (CMA). The unified interface correlates data from services such as Internet Firewall, IPS, DNS Protection, Remote Browser Isolation (RBI), Cloud Access Security Broker (CASB), and ZTNA. This consolidated view simplifies phishing investigation and response, allowing you to review incidents, analyze activity, and update policies without switching between tools.

For example, if IPS or DNS Protection blocks a phishing domain, XOps immediately displays the correlated event as part of a phishing story. You can then trace the attack across services and apply updated policies, all within the CMA.

### What are Phishing Attacks?

Phishing attacks are one of the most effective methods for compromising users and infiltrating organizations. Attackers use deceptive domains, fake login pages, and social engineering to harvest credentials or deliver malware, often impersonating trusted brands or cloud services. These campaigns frequently include fake emails or fraudulent websites designed to look like legitimate companies such as Microsoft, AWS, or Apple, tricking users into entering their login details or approving malicious requests.

Modern phishing campaigns increasingly exploit cloud-based and collaboration platforms, making it harder for traditional security tools to detect and block malicious activity. Threat actors adapt quickly, using automation and encryption to evade detection and disguise communication with command-and-control infrastructure.

### Challenges of Detecting Phishing

Phishing campaigns continue to evolve, exploiting trusted brands and cloud services. Common detection challenges include:

- Newly Registered Domains (NRDs): Attackers rapidly register and discard domains to evade reputation systems
- SaaS Abuse: Malicious content hosted on legitimate collaboration or storage services
- TLS Encryption: Hides phishing payloads and URLs in encrypted traffic
- Fragmented Visibility: Separate point products make it difficult to correlate detections and understand the full attack flow

## Detect and Prevent Phishing

Cato inspects all WAN, Internet, and remote-access traffic in-line within each PoP. Phishing detection and blocking occur through converged security services that operate in parallel within the unified stack.

Core protections are included with the regular Cato service. Threat Protection, Advanced Threat Protection, CASB, and XOps each require a separate license.

### Core Protections

- **Internet Firewall:** Uses category, and reputation-based URL filtering, continuously updated by multiple threat intelligence feeds, to block access to known or suspected phishing domains. You can define and import custom Indicators of Compromise (IoCs) to enhance detection coverage for targeted or emerging phishing campaigns
- **ZTNA (Zero Trust Network Access):** Enforces least-privilege access to internal and cloud applications through identity-based controls. ZTNA features include identity verification, device compliance checks, and Always-On connectivity that ensures all sessions are authenticated and inspected in real time
- **TLS Inspection:** Decrypts and re-encrypts HTTPS sessions at the PoP, enabling inspection of encrypted URLs, forms, and scripts to identify and block phishing pages hidden within TLS traffic

Related Articles:

- [What is the Cato Internet Firewall?](/v1/docs/what-is-the-cato-internet-firewall)
- [Protecting Users with Always-On Security](/v1/docs/protecting-users-with-always-on-security)
- [What is the Client Connectivity Policy?](/v1/docs/what-is-the-client-connectivity-policy)
- [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account)

### Threat Prevention

- **IPS and DNS Protection:** Detect and block phishing campaigns using IoCs, heuristic analysis, and AI/ML models that identify risky or deceptive domains and cloned login pages. DNS Protection blocks DNS requests before a connection is established with the malicious server—preventing any TCP or UDP handshake

Related Articles:

- [Configuring the IPS Policy](/v1/docs/configuring-the-ips-policy)
- [How IPS Protects Against Phishing Attacks](/v1/docs/how-ips-protects-against-phishing-attacks)
- [Customizing the DNS Protections for IPS](/v1/docs/customizing-the-dns-protections-for-ips)

#### Examples: Cybersquatting and Phishing Kits

- **Cybersquatting:** Cato protects against domains intentionally created to resemble legitimate brands or services (for example, micros0ft-login.com), which deceive users into entering their credentials. Learn more in this blog: [Cato Networks Adds Protection from the Perils of Cybersquatting](https://www.catonetworks.com/blog/cato-networks-adds-protection-from-the-perils-of-cybersquatting/)
- **Phishing Kits:** IPS also identifies activity related to phishing kits—pre-packaged toolsets used by attackers to automate the creation of fake login pages and credential theft infrastructure. Learn more in this blog: [Evasive Phishing Kits Exposed: Cato Networks In-Depth Analysis and Real-Time Defense](https://www.catonetworks.com/blog/evasive-phishing-kits-exposed-cato-networks-in-depth-analysis-and-real-time-defense/)

### Advanced Threat Prevention (ATP)

- **RBI (Remote Browser Isolation):** Executes browsing sessions for untrusted or unknown sites in a secure cloud container. Prevents credential submission and script execution, protecting users who visit suspicious sites that evade other detection layers

Related Articles:

- [Configuring the RBI Service for Browsing Sessions](/v1/docs/configuring-the-rbi-service-for-browsing-sessions)

### CASB - App Control

Cato’s Cloud Access Security Broker (CASB) provides visibility and control over SaaS and cloud applications, helping you identify phishing risks and prevent account compromise.

- **App Control:** Uses inline controls to enforce policies for sanctioned SaaS applications and monitors unsanctioned app activity through API integrations. CASB helps detect phishing-related risks such as fake file shares, malicious links, or unauthorized OAuth permissions within cloud collaboration tools
- **App Control via API:** Provides visibility and governance for out-of-band traffic, monitoring user activities in sanctioned SaaS applications even when traffic does not pass through the Cato Cloud

Related Articles:

- [Application Control with Inline Inspection](/v1/docs/application-control-with-inline-inspection)
- [Application Control via API with Audit Activities](/v1/docs/application-control-via-api-with-app-activities)

#### Example: Living off the Cloud

Cato’s CASB helps protect against phishing campaigns that result in malware communicating with command-and-control (C2) servers hosted on legitimate cloud platforms like Google Drive or Trello, a technique known as Living Off the Cloud. These services are often allowed by default in many organizations and can evade traditional phishing defenses that rely on URL filtering or IP reputation.

- Tenant Restrictions: Apply tenant restrictions to block access to unsanctioned or personal instances of cloud apps, ensuring that only corporate-approved accounts are accessible
- Activity-Level Controls: Enforce controls to block high-risk actions, such as uploading files or accessing cloud services via unauthorized clients, preventing attackers from leveraging trusted cloud services to exfiltrate data or issue remote commands to compromised systems
- For more information, watch this [video](https://www.youtube.com/watch?v=NEUT7KU3p5E)

### XOps

XOps is Cato’s advanced analytics and incident correlation service. It combines data from all security engines to identify, prioritize, and contextualize phishing-related incidents. By presenting these insights as correlated stories and behavioral analytics, XOps lets you detect, investigate, and remediate phishing activity more effectively in the CMA.

- **Security Stories:** Correlate phishing detections into unified narratives for analysis

You can also take steps to directly mitigate a phishing threat from within a story, such as revoking the session for remote users or adding the target to a container that is blocked by a firewall rule
- **UEBA:** Detects abnormal login patterns or lateral movement following a phishing attempt, helping you identify compromised accounts and contain post-attack activity

Related Articles:

- [Welcome to the Cato XOps Service](/v1/docs/welcome-to-the-cato-xops-service)
- [Mitigating Threats in XOps Stories](/v1/docs/mitigating-threats-in-xops-stories)
- [Analyzing XOps UEBA Stories for Usage and Events Anomalies](/v1/docs/analyzing-xops-ueba-stories-for-usage-and-events-anomalies)

## Identity and Behavior Protections

Cato’s identity and behavior capabilities strengthen phishing resilience by limiting exposure and reducing the impact of credential theft. These features enforce user verification, device compliance, and least-privilege access to ensure that only authenticated, secure users can connect to corporate resources.

### User Awareness

Cato’s User Awareness framework associates all activity across the platform with verified user identities. Identity-based access policies and visibility in the CMA let you trace phishing-related activity to specific accounts and enforce targeted segmentation for containment.

For more information, see [User Awareness](/v1/docs/user-awareness)

### Authentication and Access Controls

Phishing attacks often rely on stolen credentials. Cato mitigates this risk through integrations with enterprise identity providers for Single Sign-On (SSO) and Multi-Factor Authentication (MFA). Access policies are dynamically enforced at the PoP based on user identity, device posture, and context to prevent credential reuse and lateral movement.

For more information, see [IdP Single Sign-On](/v1/docs/identity-providers-and-authentication)

### Device Compliance and Posture Validation

Cato verifies that only compliant, managed devices can connect to corporate resources. Before access is granted, the platform checks device posture (security software, OS, configuration) and blocks non-compliant endpoints to ensure that potentially compromised devices cannot be leveraged in phishing campaigns.

For more information, see [Client Connectivity Policy (Device Posture)](/v1/docs/client-connectivity-policy).

## Investigate Phishing Activity

The CMA provides unified visibility of phishing-related activity by aggregating detections from all Cato security engines, including Internet Firewall, IPS, DNS Protection, RBI, remote access, and Suspicious Activity Monitoring (SAM). The CMA leverages Cato’s cloud-scale intelligence to continuously improve phishing detection accuracy and identify emerging attack behaviors.

### Event Investigation

You can investigate phishing-related events in the CMA using contextual filters such as user, application, and site to identify related detections. Natural-language search and drill-down reports provide fast access to phishing events.

Key dashboards and reports include the Security Dashboard, Applications Dashboard, User Activity Reports, and Threat Reports, which highlight phishing domains, repeated credential submissions, and risky user activity.

### Investigation with XOps

XOps provides advanced correlation and incident analytics that simplify phishing investigations. It aggregates detections from multiple security engines, including IPS, DNS Protection, RBI, and SAM, correlating them into unified Security Stories that show the full phishing sequence. Similar Stories highlight related attacks, and AI-generated summaries accelerate triage. Integration with tools such as SentinelOne, Microsoft Defender, and CrowdStrike extends context to endpoints for unified investigation. For more information, see [XOps Security Playbook - Phishing Website Attack](/v1/docs/xops-security-playbook-phishing-website-attack).

### Suspicious Activity Monitoring (SAM)

SAM enhances phishing detection and investigation by identifying network behaviors that may indicate emerging threats or misuse related to phishing campaigns. It detects traffic patterns that match signatures created by the Cato Security Research team, identifying activity that deviates from expected user or application behavior. For example, SAM can flag repeated credential submissions to unknown domains, suspicious outbound requests following a phishing attempt, or traffic consistent with command-and-control communication.

For more information, see [Monitoring Suspicious Activity with IPS (SAM)](/v1/docs/monitoring-suspicious-activity-with-ips-sam).

## Mitigate Phishing Across the Attack Lifecycle

Cato mitigates phishing attacks across every stage of the attack lifecycle—from initial access attempts to post-compromise activity—by correlating detections across its security engines. This lifecycle approach ensures that threats are blocked in real time and tracked, contextualized, and contained through integrated visibility and automation in the CMA and XOps.

### Block Access

Cato’s inline inspection engines proactively prevent users from connecting to phishing infrastructure, reducing exposure before a session is established.

- Internet Firewall and DNS Protection: Blocks access to risky or suspicious domains
- IPS: Blocks access to known phishing sites and credential-harvesting infrastructure

### Block Credential Submission

Cato prevents users from submitting credentials to phishing sites that bypass domain or URL reputation filters.

- IPS: Detects credential input patterns and phishing page structures in real time
- RBI: Isolates web sessions in a secure container, preventing data entry or interaction with phishing forms and scripts

### Detect Post-Compromise Activity

Cato provides visibility into unusual activity that may indicate successful phishing or credential misuse, helping you identify and contain potential compromises quickly.

- SAM generates events when it observes repeated credential submissions, anomalous outbound connections, or behavior consistent with command-and-control communication

For example, if a sophisticated phishing attack eluded other protections, monitoring SAM events can help identify an infected host.

### Correlate Phishing Events with XOps

The XOps service unifies phishing-related data from multiple security engines into a single investigative view.

- **Security Stories:** Connect events from IPS, DNS Protection, RBI, and SAM into a chronological attack narrative
- **AI-Driven Analysis:** Highlights root causes, affected users, and follow-up actions
- **Similar Stories:** Identify recurring campaigns targeting the same organization or users

## Manage Phishing Response and Operations

Cato simplifies phishing response and operational workflows by centralizing investigation, containment, and coordination across security engines in the CMA with XOps. This unified approach lets you manage incidents efficiently, accelerate remediation, and reduce the overall impact of phishing attacks.

### Response Actions

You can contain phishing incidents directly from the CMA to reduce response time and minimize the impact of credential misuse or compromised accounts.

- **User and Session Controls:** Isolate affected users and block further access
  - **Remote Users:** Revoke credentials for users connected through the Cato Client to prevent ongoing access from compromised accounts
  - **Users Behind a Site:** Disable affected users and create WAN and Internet Firewall rules that block the specific user as the traffic source (requires User Awareness)
- **Policy Enforcement:** Update WAN and Internet Firewall policies in real time to block communication to newly identified phishing domains or IP addresses
- **Cross-Platform Integration:** Integrate with endpoint protection tools such as SentinelOne, Microsoft Defender, CrowdStrike, and Cato Endpoint Protection (EPP)
  - Data from these EPP tools is included in the CMA event context, letting you view endpoint detections alongside Cato network security events
- **XOps Correlation:** XOps security stories include endpoint detection and response (EDR) data, providing correlated visibility across network and endpoint layers

Related Articles:

- [Creating the Response Policy for XOps Stories](/v1/docs/creating-the-response-policy-for-xops-stories)
- [XOPs Connectors](/v1/docs/sase-detection-response-xops-1)

### Operational Workflows

The CMA streamlines security operations by automating alert management, investigation, and reporting tasks.

- **Centralized Alerts:** View, filter, and prioritize phishing-related alerts from all security engines in one place
- **Notification Integrations:** Send automated alerts to collaboration platforms such as Slack, ServiceNow, or email to accelerate escalation and tracking
- **Event Reviews:** Review phishing events, including SAM and IPS detections, to identify trends and improve accuracy
- **Reports Including Phishing Data:** Generate reports that summarize phishing-related activity, such as the Security Events Report, XOps Investigations Report, and XOps Detections Report, to support operational visibility and executive reporting

Related Articles:

- [Alerts](/v1/docs/notifications)
- [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network)
- [Cato Reports](/v1/docs/cato-reports)

## Complementary Protections

Cato’s complementary protections work alongside phishing defenses to provide complete security across data, endpoints, and connected devices. These services protect against data loss, malware infection, and IoT exploitation that can occur during or after a phishing attack. Each protection requires a separate license.

- **DLP:** Helps prevent data exfiltration attempts that may follow a phishing attack
- **Cato EPP:** Detects and blocks malware or other payloads delivered through phishing vectors
- **IoT Security:** Protects managed IoT assets and identifies unmanaged devices that could be exploited following a phishing compromise

### DLP

Cato’s DLP engine protects sensitive information from being exfiltrated after a phishing attempt. For more information, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service).

- **Inline DLP Enforcement:** Inspects all traffic for sensitive information and blocks unauthorized transfers outside the organization
- **Out-of-Band Monitoring:** Uses API-based connectors to monitor data activity and sharing within sanctioned SaaS applications, even when traffic does not pass through the Cato Cloud
- **Visibility:** Provides event data in the CMA for reviewing and auditing data-handling policy violations

### Cato EPP

Cato Endpoint Protection (EPP) secures endpoints by detecting and blocking malware and phishing-delivered payloads without relying on PoP traffic inspection. This ensures continuous protection, even when devices operate outside the Cato Cloud. For more information, see [Getting Started with Cato's Endpoint Protection (EPP)](/v1/docs/getting-started-with-cato-s-endpoint-protection-epp).

- **Local Threat Prevention:** Detects and blocks malicious files, scripts, and payloads before they execute
- **Behavioral Analysis:** Identifies suspicious processes and ransomware-like activity originating from phishing attacks
- **CMA Integration:** Sends endpoint alerts and telemetry to the CMA for centralized visibility, letting you investigate phishing-related malware alongside network and identity data

### IoT and OT Security

- **Device Discovery:** Automatically identifies all IoT and OT devices connected to the network
- **Behavioral Monitoring:** Detects abnormal communication patterns, such as devices attempting to contact phishing-controlled or command-and-control domains
