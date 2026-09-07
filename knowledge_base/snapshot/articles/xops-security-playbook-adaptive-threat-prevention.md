---
title: "XOps Security Playbook - Adaptive Threat Prevention"
slug: "xops-security-playbook-adaptive-threat-prevention"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-security-playbook-adaptive-threat-prevention"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Security Playbook - Adaptive Threat Prevention

This playbook describes how to use the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) to investigate stores based on Adaptive Threat Prevention malicious behavior.

## Overview

This playbook outlines a systematic approach for SOC engineers to investigate potential security incidents related to Adaptive Threat Prevention malicious behavior. These indicators block malicious behavior associated with the early stages of suspected lateral movement or data exfiltration attempts. They focus on detecting and blocking the use of critical tools or techniques typically employed by attackers during the second phase of compromise, such as:

- Remote tool execution (e.g., PsExec)
- Unauthorized download tools (e.g., Rclone)

![image-20250727-102958.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424540405917.png)

## Gathering Information About the Threat

Use the Details widgets in the story to gather basic information about the potential threat and make an initial assessment whether further investigation is required. This part of the investigation leads to understanding the preconditions of the triggered activity that led to story creation. Review these key fields:

- **Source Tab**: Device-level data such as IP, OS, hostname, and MAC address.
- **IOA Catalog Entry**: Use the IOA title and description to guide your investigation.

## Analyze the Triggered IPS Event

This stage focuses on understanding the activity that triggered the story creation, what was blocked, and what preconditions this IPS activity requires in order to block the malicious traffic.

- **Target Actions Table**: Review the associated events by clicking on the Related Events. These entries provide deeper insight into the nature of the blocked traffic, including contextual details and threat references that can help identify the type and intent of the threat.

![image-20250701-124511.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424521206173.png)
- **Attack Distribution Graph**: This graph helps assess the nature of the detected traffic, whether it follows a recurring pattern (e.g., periodic or bot-like behavior) or is a one-time event. In the context of these types of stories, recurring traffic is less commonly observed. Multiple occurrences may suggest the activity was part of a test or drill rather than an actual attack attempt. However, each case must be thoroughly investigated to rule out any malicious intent.

![image-20250703-132703.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424540631325.png)
- **Related Events Timeline**: Since UEBA IPS-based stories are triggered only after specific preconditions are met, understanding the sequence of events leading to the block is essential.

![image-20250703-125705.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424507213597.png)
  - Start by filtering events based on the story’s time frame and the user/client IP involved. Next, add the Signature ID as a visible column and apply filters for IPS and Suspicious Activity event types. This makes it easier to pinpoint the exact events that contributed to triggering the UEBA IPS Block.
  - Key indicators outlined in the IOA description help focus the investigation on relevant activity patterns. Once the precondition events are identified, reference the Threat Catalog to gather more context about the techniques involved and better understand the nature of the detected threat.

## Analyze Related Stories

This step provides valuable context by uncovering additional detections tied to the same device or user, which may reveal a broader pattern of suspicious behavior. Be sure to cross-reference timelines, involved IPs, and user identities to spot overlapping indicators and potentially linked intrusion attempts. Reviewing related stories can help you:

- Identify other activities that occurred around the same time on the affected host, which may have triggered separate stories
- Detect similar stories across the organization, helping to assess whether this is an isolated event or part of a larger, coordinated attack attempt
- Evaluate the scope and persistence of the threat by identifying repeated techniques or tool usage across multiple entities

## Conclustion

These are some examples of relevant conclusions:

- Malware
- Exploitation Attempt
- Lateral Movement

## Recommended Actions

1. Run full AV/EPP/EDR scans on the affected host
2. Perform a credential reset for involved user accounts, especially if reconnaissance was extensive
3. If applicable, proactively block tools or services flagged in the detection for the affected host within Cato Firewalls (LAN, WAN, Outbound, and RPF) until full remediation
4. In case the story is a false Positive, you can classify it as Benign/Informational and also add it to a [Mute Stories](/v1/docs/muting-xops-stories) rule. If the story results from a legitimate scan or penetration test it is recommended to add it to a Mute Stories rule for a specific time range.
