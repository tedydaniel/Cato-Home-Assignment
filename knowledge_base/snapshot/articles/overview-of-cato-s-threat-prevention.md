---
title: "Overview of Cato's Threat Prevention"
slug: "overview-of-cato-s-threat-prevention"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/overview-of-cato-s-threat-prevention"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview of Cato's Threat Prevention

## Threat Prevention in the Cato Cloud

The Cato Cloud contains Threat Prevention engines that can inspect WAN and Internet traffic for malicious files and malware attacks. Traffic that is sent over MPLS or bypasses the Cato Cloud is not inspected by these engines. One Threat Prevention policy is applied to all sites in the account.

> [!NOTE]
> IMPORTANT!
> 
> We strongly recommend that you enable TLS inspection so that the Threat Prevention services provide the maximum protection for your network.

### Cato Networks Threat Prevention Engines

These are the Threat Prevention engines that inspect traffic in the Cato Cloud:

- Anti-Malware - Protects against malicious files based on known file signatures and from a heuristic analysis
- NG Anti-Malware - Protects against unknown and zero-day malicious files based on machine learning and predictive models
- Intrusion Protection System (IPS) - Protects against known vulnerabilities, bots, and other malicious attacks

## Related Resources

- [What is the Cato Anti-Malware Policy?](/v1/docs/what-is-the-cato-anti-malware-policy)
- [Configuring the Anti-Malware Policy](/v1/docs/configuring-the-anti-malware-policy)
- [Configuring the IPS Policy](/v1/docs/configuring-the-ips-policy)
