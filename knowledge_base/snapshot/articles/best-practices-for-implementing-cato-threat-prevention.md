---
title: "Best Practices for Implementing Cato Threat Prevention"
slug: "best-practices-for-implementing-cato-threat-prevention"
tags: ["Best Practices", "Internet Security"]
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/best-practices-for-implementing-cato-threat-prevention"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices for Implementing Cato Threat Prevention

## Overview of Cato's Security Services

The Cato Cloud contains powerful security services that are easy to configure and help to keep your network safe. This article explains the recommendations and best practices for the different Threat Prevention services.

The Cato Cloud has these two layers of protection for your account:

- Access layer - includes firewalls for WAN and Internet traffic
- Security layer - includes the Cato Threat Prevention services: Anti-Malware, NG Anti-Malware, and IPS

The Cato Cloud applies the rules in the firewalls to determine if the traffic is allowed or blocked. In addition, the Threat Prevention services analyze the traffic for malware, network-based vulnerabilities, malicious network activity and more.

### Access Layer

Each network flow is inspected by the WAN and Internet firewall. The WAN firewall lets you allow or block traffic between organizational entities such as sites, users, hosts, subnets and more. The Internet firewall lets you control access to websites and web-based applications.

By default, Cato’s WAN firewall uses whitelisting approach, and only allows traffic that is explicitly defined by a firewall rule and blocks all unidentified traffic. The Internet firewall controls outgoing traffic to the Internet and uses a blacklisting approach. The final Internet firewall rule is an implicit any-any allow rule, so you must define rules to explicitly block connections to the Internet.

Out of the box, Cato has many pre-defined categories that contain dozens of services and applications to help manage network traffic. These categories are regularly updated by the Cato Security team.

By default, the Internet firewall includes a rule that blocks potentially dangerous categories of traffic. We strongly recommend that you don't disable this rule and provide the best security for your network.

### Security Layer

The Cato security layer has multiple engines that analyze WAN and Internet traffic for malware and security risks.

1. Anti-Malware is an anti-virus gateway in the cloud and includes the following:
  - Deep packet inspection of the traffic payload for clear and encrypted traffic (if TLS Inspection is enabled).
  - True filetype detection identifies the actual type of a file going over the network regardless of its file extension or the content-type header.
  - Malware detection using signature and heuristics database that is kept up-to-date at all times based on global threat intelligence databases to protect against current known threats. **Cato does NOT share any files or data with cloud-based repositories to ensure customer data remains confidential.**
2. NG Anti-Malware implements the SentinelOne engine that uses an AI model to detect threats in portable executable files, PDFs, and Office documents. The AI model is developed by extracting features from millions of malware samples in the malware repository. Then Supervised Machine Learning is used to identify and correlate different features of benign and malicious files. NG Anti-Malware can predict and prevent unknown malware and viruses.
3. IPS - Cato’s cloud-based network Intrusion Prevention System (IPS) inspects inbound, outbound and WAN traffic, including TLS traffic (if TLS Inspection is enabled). IPS can also operate in monitor mode (IDS) and doesn't block traffic. In IDS mode, all traffic is evaluated, and security events are generated.

## Best Practices for Enabling Threat Prevention

We highly recommend that you enable the Threat Prevention services for your account. End users experience **no delay** due to anti-malware and IPS processing. When a malicious file is detected, user access is blocked, and the user is redirected to a block page.

Cato's security team keeps the Threat Prevention database up-to-date at all times based on global threat intelligence databases to ensure effective protection against current threats.

The following workflow is the best practice for enabling the Threat Prevention services:

1. Enable Threat Prevention policies in **Monitor** mode for both all traffic. In **Monitor** mode, malicious traffic is only logged and isn't blocked.
2. If necessary, you can configure the tracking option to send an email alert if malware is detected (in Monitor mode, there are no alerts for blocked traffic).
3. After a few days, review the Threat Prevention events and gradually switch the policies to Block mode.
4. Enable TLS inspection to let the Threat Prevention engines to analyze encrypted traffic.

> [!NOTE]
> Note:
> 
> For maximum detection results, TLS inspection must be enabled. TLS inspection allows the security engines to analyze encrypted traffic which might contain malicious files or code. Enabling TLS inspection is the final step in enabling AM and IPS.

## Related Articles

- [Internet and WAN Firewall Policies – Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies)
- [Best Practices for TLS Inspection](/v1/docs/best-practices-for-tls-inspection)
- [Testing TLS Inspection in the Cato Cloud](/v1/docs/testing-tls-inspection-in-the-cato-cloud)
- [Installing the Root Certificate for TLS Inspection](/v1/docs/installing-the-root-certificate-for-tls-inspection)
- [What is the Cato Anti-Malware Policy?](/v1/docs/what-is-the-cato-anti-malware-policy)
- [Configuring the Anti-Malware Policy](/v1/docs/configuring-the-anti-malware-policy)
- [Configuring the IPS Policy](/v1/docs/configuring-the-ips-policy)
