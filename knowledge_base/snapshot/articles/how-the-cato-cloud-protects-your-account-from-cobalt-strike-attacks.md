---
title: "How the Cato Cloud Protects your Account from Cobalt Strike Attacks"
slug: "how-the-cato-cloud-protects-your-account-from-cobalt-strike-attacks"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/how-the-cato-cloud-protects-your-account-from-cobalt-strike-attacks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How the Cato Cloud Protects your Account from Cobalt Strike Attacks

This article explains how the IPS security service in the Cato Cloud security stack protects your network from malware attacks using Cobalt Strike.

## Overview

Cobalt Strike is a well-known adversary simulation tool used by both threat actors and security professionals for various purposes. In this article, we outline techniques that the Cato Cloud employs to protect against attacks based on the malicious use of Cobalt Strike.

## Protection Techniques Against Cobalt Strike Attacks

This section describes techniques used by the IPS service to identify and defend against Cobalt Strike attacks.

### PowerShell Detection and Blocking

Cobalt Strike often leverages PowerShell for downloading malware onto a system. To counter this, the IPS engine is configured to block any suspicious PowerShell activities associated with Cobalt Strike, thereby preventing the introduction of malicious payloads.

### Identifying and Blocking Unique HTTP Identifiers

Cobalt Strike uses distinct HTTP identifiers for communication with its Command and Control (C2) servers. Cato's IPS identifies and blocks these unique identifiers, rendering the C2 communication ineffective and protecting your network from potential threats.

### Privilege Escalation Prevention

Cobalt Strike offers options for privilege escalation, which can be exploited by attackers. To mitigate this risk, IPS actively blocks any attempt by the C2 server to execute privilege escalation on target systems, thus preventing unauthorized access to higher-level privileges.

### Post-Exploitation Command Blocking

Cobalt Strike relies on predefined post-exploitation commands to control compromised systems. IPS detects and blocks the execution of these commands issued by the C2 server, ensuring that any attempts to manipulate the compromised host are thwarted.

### Lateral Movement Detection and Prevention

Cobalt Strike employs various techniques and tools for lateral movement within a network, including PSexec, SSH, SMB, and WinRM. To counteract these tactics, IPS together with [Suspicious Activity Monitoring](/v1/docs/monitoring-suspicious-activity-with-ips-sam) (SAM) can efficiently detect and block these protocols and techniques. This prevents the lateral spread of the threat within your network.

### Malleable C2 Profile Detection

Cobalt Strike often employs Malleable C2 profiles to mimic popular services, such as Gmail, Bing, and Pandora, in an attempt to evade detection. To counter this sophisticated evasion technique, IPS employs detection methods specifically designed to identify and block Cobalt Strike's use of Malleable C2 profiles. This proactive measure ensures that even attempts to disguise malicious traffic as benign services are effectively intercepted, enhancing your network's security.

### Identifying and Blocking Tools for Randomizing Malleable C2 Profiles

To further complicate detection, there are tools available to randomize the identifiers in Malleable C2 profiles, making them harder to spot. IPS is equipped to recognize the identifiers of these tools and proactively block them.
