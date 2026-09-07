---
title: "What is Agentic Threat Prevention?"
slug: "what-is-agent-threat-prevention"
updated: 2026-08-13T17:41:07Z
published: 2026-08-13T17:41:07Z
canonical: "knowledge.catonetworks.com/what-is-agent-threat-prevention"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Agentic Threat Prevention?

## Overview

Agentic Threat Prevention defends against autonomous, AI-driven attack mutations at machine speed. It uses AI agents to identify attacks and apply and adapt protections before any impact occurs. This reduces your attack surface and stops frontier AI threats without waiting for manual intervention.

### Understanding the Threat of Frontier AI

Frontier AI attacks are not driven or limited by humans. AI agents can now plan, execute, and adapt multi-stage attack chains autonomously, accelerating vulnerability discovery, personalizing tactics in real time to evade defenses, and running attacks at increasing speed, scale, and sophistication.

Protection from frontier AI attacks is beyond the limits of traditional protections. Static rules and signatures are built for known attacks, while frontier AI attackers continuously mutate their behavior to bypass them. Effective protection must operate at machine speed and use continuous, environment-specific context to identify and block emerging attack paths.

### How Agentic Threat Prevention Protects Your Network

Agentic Threat Prevention uses AI agents powered by the Opus 4.6 large language model. The agents analyze network-wide traffic and security signals every four hours. Each analysis reviews activity from the previous 24 hours across users, hosts, sites, applications, and other entities. This rolling window provides account-specific context about typical usage patterns and expected activity.

Using this context, the agents reason over suspicious behavioral patterns. At machine speed, they correlate activity sequences, timing, first-seen events, and signals from multiple security engines. This reasoning connects individual signals and compares them with established behavior and broader network context. It can reveal emerging attacks, including attacks that use previously unseen paths. For example, downloading a binary file may be normal for an IT administrator. The same action may indicate risk when performed by a user with no history of that behavior.

When activity indicates elevated risk, the agent predicts the next step of the attack and determines the appropriate response by automatically applying temporary, dynamic controls. These controls block access to exposed services, actions, or access paths, enforcing mitigation based on thorough analysis and research into numerous breach scenarios by Cato's research team.

The agents continuously reevaluate behavior over time and adjust or remove controls as conditions change. This reduces the attack surface, limits manual intervention, and preserves administrative visibility and control. To monitor how Agentic Threat Prevention protects your network, see [Monitoring Agentic Threat Prevention](/v1/docs/monitoring-agentic-threat-prevention).

To provide a more complete view of risky user behavior, block events triggered by Agentic Threat Prevention’s security engine are incorporated into the user’s risk score. For more information, see [Understanding the User Risk Level.](/v1/docs/understanding-the-user-risk-level)

Agentic Threat Prevention enables you to:

- **Stay ahead of frontier attacks** by adapting environment-specific protections at machine speed as attacker behavior changes
- **Automate threat prevention** by automatically applying dynamic controls that stop attacks before they can advance
- **Enforce controls everywhere** across users, sites, and applications

### License Requirements

- For customers with an active Advanced Threat Protection license as of Aug 2026, this license also includes Agentic Threat Prevention
- For other customers, Agentic Threat Prevention requires an Agentic Threat Prevention license (this requires a Threat Prevention or an Advanced Threat Prevention license)

### Use Case – Blocking Agentic AI Attack Before Command-and-Control Establishment

An employee at Company ABC interacted with a malicious AI agent disguised as a legitimate productivity assistant. After gaining the employee's trust, the agent attempted to execute a multi-step attack by enumerating local resources, identifying sensitive applications, and preparing the endpoint for persistent remote access. The sequence of actions was atypical for the user and had not previously occurred on the device.

Agentic Threat Prevention analyzed the chain of events, recognized the coordinated reasoning and planning characteristic of an autonomous AI-driven attack, and determined that the activity represented malicious reconnaissance preceding command-and-control establishment.

Based on this assessment, Agentic Threat Prevention applied preemptive controls before the attack could progress. It blocked the download and execution of AnyDesk, preventing the AI agent from establishing remote access and maintaining command-and-control. This disrupted the attack before additional tools, payloads, or instructions could be delivered, significantly reducing the risk of credential theft, privilege escalation, and lateral movement.

By autonomously detecting the intent behind the activity rather than relying on individual indicators, Agentic Threat Prevention contained the AI-driven attack without requiring manual intervention.

## Understanding How Agentic Threat Prevention Works

Agentic Threat Prevention continuously analyzes activity across your environment to identify and stop suspicious behavior using the following five-step process:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(86).png)

1. **Build an Entity Baseline**: Agentic Threat Prevention’s AI agents monitor network activity over time to establish normal behavior across your network.
2. **Detect Deviations**: Agents collect real-time signals from multiple security engines, including services such as Anti-Malware, IPS, Firewall and SAM. It also analyzes long-term insights from the Cato data lake, which aggregates all security events. AI agents reasoning identifies suspicious behavioral patterns compared against the behavioral baseline to identify abnormal activity. Even actions that appear benign can be flagged if they significantly deviate from normal behavior.
3. **Dynamic Controls**: When suspicious behavior is detected, to reduce the attack surface, the agent predicts the next stage of the attack and applies customized controls to prevent it from progressing. Multiple controls can be applied for a single suspicious behavior.
4. **Block Malicious Action**: If a malicious action is taken, it is blocked in real time to prevent threats.
5. **Adapt Dynamic Controls**: Agents continuously reevaluate entity behavior and dynamically adjust or expire the applied controls as the risk level changes.

## How Agentic Threat Prevention Complements Existing Security Engines

Agentic attacks introduce three challenges that traditional security models provide limited protection against:

- **Machine speed**: Attacks execute and progress faster than human-driven response workflows can react
- **Adaptive**: AI-driven attackers iterate continuously, changing tactics after each failed attempt until they find a path that succeeds
- **Autonomous**: Attack chains plan and execute without a human in the loop, so they never pause, wait, or lose focus

Existing Cato security engines provide precise protection against known threats and policy violations. They effectively enforce policy and block attacks at specific stages of the lifecycle. However, they depend on detections defined in advance, signatures and rules created by security researchers based on known attack techniques.

Agentic attackers can continuously modify their techniques until they find an available attack path faster than new detections can be researched, written, and deployed. Agentic Threat Prevention matches the attacker's model of operation with an autonomous reasoning layer. It continuously analyzes account-specific context from traffic, security events, threat intelligence, and entity behavior. Unlike the attacker, the agent has continuous visibility into the environment and immediate access to enforcement controls. This context advantage helps the agent identify suspicious behavioral patterns and emerging attack paths.

The agent detects suspicious behavior without waiting for researchers to create new signatures. It selects the appropriate response based on the context and risk of each detection. Agentic Threat Prevention then applies dynamic controls through Cato’s existing enforcement engines at machine speed.

The agent continuously reevaluates activity and adjusts or removes controls as the risk changes. This provides proactive prevention without requiring a human in the loop.

Existing security engines enforce precise controls, while Agentic Threat Prevention autonomously reasons over context and orchestrates the response. Together, they stop agentic attacks before they can progress, without adding policy complexity or operational overhead.
