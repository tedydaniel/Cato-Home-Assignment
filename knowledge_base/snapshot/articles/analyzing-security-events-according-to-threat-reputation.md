---
title: "Analyzing Security Events According to Threat Reputation"
slug: "analyzing-security-events-according-to-threat-reputation"
updated: 2026-08-03T10:38:45Z
published: 2026-08-03T10:38:45Z
canonical: "knowledge.catonetworks.com/analyzing-security-events-according-to-threat-reputation"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyzing Security Events According to Threat Reputation

## Overview

The Security research team in Cato Networks has developed analytical engines to tag malicious IP addresses, URLs, and domain names with a bad reputation. This reputation indicates that we discovered that the specific IP address, URL, or domain initiated suspicious or malicious activity. For example, malware C&C, network scanners, phishing activity, and so on.

The IPS engine in the Cato Cloud blocks network traffic that is tagged with a bad reputation and generates a reputation-based security event with the threat type **Reputation**.

The following screenshot shows an example of a security event with the Reputation threat type from Event Discovery:

![ThreatEvent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303256617629.png)

## Reasons for Blocked Traffic

When Cato's IPS engine identifies potentially malicious traffic and blocks it based on the threat reputation, the **threat name** field explains the reason why the traffic was blocked.

Values for the **threat name** field include, but are not limited to:

- Domain reputation based signature - Phishing
- Reputation IP based signature - Botnet
- IP reputation based signature - Malicious IP
- Domain reputation based signature - Malicious Domain
- IP reputation based signature - Abuse
- URL reputation based signature - Malicious URL

## What are the different Threat Types?

Each Security Event generated within the Cato Management Application is categorised by a field called **threat type**. This field displays a high-level overview of the type of threat that Cato has protected you against, and provides you with an indication of any potential malicious activity.

The **threat types** which may be displayed in a Security Event include:

- Spam
- Brute Force
- Scanner
- Phishing
- Policy Violation
- Crypto Mining
- Anonymizer
- DoS
- Network Scan
- Vulnerability Scan
- Information Disclosure
- Privilege Escalation
- Reputation
- Remote Code Execution
- PuP
- Web Application Attack
- Malware
- Malicious Browser Extension

## Sample Threat Reputation Security Event Workflow

1. The Security research team identifies that a domain is potentially a source of malicious attacks.
2. The domain is tagged with a bad reputation and the IPS engine is updated.
3. An end-user tries to access the domain, and IPS blocks the connection and generates a Security event with the threat type **Reputation**.

## What's the Size of Cato's Threat Database?

The Threat Database at Cato Networks is constantly evolving in line with the ever-changing threat landscape. We continuously improve the size and scope of our threat detections to ensure maximum protection for our end customers. Cato ingests 100s of different threat intelligence sources containing some 20 million IOCs. For more information, see [Managed Threat Intelligence in the Cato Cloud](/v1/docs/managed-threat-intelligence-in-the-cato-cloud).
