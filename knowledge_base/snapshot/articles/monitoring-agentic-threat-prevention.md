---
title: "Monitoring Agentic Threat Prevention"
slug: "monitoring-agentic-threat-prevention"
updated: 2026-08-10T08:01:59Z
published: 2026-08-10T08:01:59Z
canonical: "knowledge.catonetworks.com/monitoring-agentic-threat-prevention"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Agentic Threat Prevention

## Overview

Agentic Threat Prevention defends against autonomous, AI-driven attack mutations at machine speed. It uses AI agents to identify attacks and apply and adapt protections before any impact occurs. This reduces your attack surface and stops frontier AI threats without waiting for manual intervention. For more information on Agentic Threat Prevention, see [What is Agentic Threat Prevention?](/v1/docs/what-is-dynamic-prevention)

The **Agentic Threats** page lets you monitor activity at each stage of the prevention flow. The page summarizes suspicious behaviors, applied controls, and mitigated threats per host across your environment. Its widgets help you understand what the agent detected, why it responded, and which protections were enforced.

From this page you can:

- Review suspicious behaviors the AI agents identified, and the reasoning and context behind each detection, including an AI summary of activity on each host
- Track the dynamic controls currently enforced and those that were adjusted or removed as behavior changed
- Understand the threats that were mitigated and their potential impact on your environment

#### Understanding How Agentic Threat Prevention Works

Agentic Threat Prevention continuously analyzes activity across your environment to identify and stop suspicious behavior using the following five-step prevention flow:

1. **Build an Entity Baseline**: Agentic Threat Prevention’s AI agents monitor network activity over time to establish normal behavior across your network.
2. **Detect Deviations**: Agents collect real-time signals from multiple security engines, including services such as Anti-Malware, IPS, Firewall and SAM. It also analyzes long-term insights from the Cato data lake, which aggregates all security events. AI agents reasoning identifies suspicious behavioral patterns compared against the behavioral baseline to identify abnormal activity. Even actions that appear benign can be flagged if they significantly deviate from normal behavior.
3. **Dynamic Controls**: When suspicious behavior is detected, to reduce the attack surface, the agent predicts the next stage of the attack and applies customized controls to prevent it from progressing. Multiple controls can be applied for a single suspicious behavior.
4. **Block Malicious Action**: If a malicious action is taken, it is blocked in real time to prevent threats.
5. **Adapt Dynamic Controls**: Agents continuously reevaluate entity behavior and dynamically adjust or expire the applied controls as the risk level changes.

## Getting Started with the Agentic Threats Page

The **Agentic Threats** page lets you monitor activity at each stage of the prevention flow. It consists of three key components:

- **Animation and Summary Table:** The animation illustrates each stage of the prevention flow and shows the number of actions and affected hosts at that stage. Clicking each stage of the prevention flow filters the summary table to data specific to that stage. The table then displays an overview of the suspicious behavior or actions taken by Agentic Threat Prevention.
- **Details Panel:** Select an entity in the Summary Table to open the details panel. The panel provides additional information about the entity, including an AI-generated summary of the activity detected on the host.
- **Sankey Diagram:** Shows how hosts progress through each stage of the prevention flow. The diagram provides context for each host by showing the preceding detection or control and the resulting outcome.

### Use Case - Understanding a Fully Mitigated Attack in Minutes, Without Manual Investigation

Company ABC’s security team notices mitigated threat activity on the **Agentic Threats** page. An analyst uses the prevention flow animation to see how Agentic Threat Prevention identified suspicious behavior, applied controls, and blocked the threat before it could progress.

The analyst selects the affected host to open the Details panel. The AI-generated summary explains the suspicious activity, the reasoning behind the detection, the controls applied, and the threat that was mitigated. The timeline helps the administrator review the sequence of events and understand how the activity developed.

To investigate further, the analyst uses the Sankey diagram to trace the host through each stage of the prevention flow. This provides a complete view of the relationship between the suspicious behavior, the activated controls, and the final outcome. Within minutes, the analyst understands what the agent detected, why it responded, which protections were enforced, and whether the threat was neutralized. This reduces investigation time while preserving the context and audit trail required for administrative review.

### Accessing the Agentic Threats Page

To access the **Agentic Threats** page, navigate to **Security > Agentic Threats**.

### Understanding the Animation and Summary Table

The animation provides an illustration of the actions taken by Agentic Threat Prevention across your network. Use the animation to understand where activity appears in the prevention flow

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(90).png)

- **AI Findings:** This section displays the reasoning for the AI agent as it monitors behaviors on hosts in your network
- **Prevention Flow:** Displays the volume of activity and the number of hosts affected at each stage of the prevention flow
  - **Suspicious Behavior:** The number of times AI agents identified suspicious activity based on user behavior and signals from multiple security engines
  - **Activated Controls:** The number of times automatic controls have been applied to restrict risky actions on hosts to prevent an attack from progressing. The host count reflects only hosts with active controls.
  - **Mitigated Threats:** The number of times a risky action was taken and blocked in real time to mitigate threats.
- **Block/Monitor:** Based on your configuration, the number of times an action was blocked or monitored. For more information, see [Managing Agentic Threat Prevention](/v1/docs/managing-dynamic-prevention).

In the example above, the AI agent identified four suspicious behaviors across 15 hosts. It activated 24 controls on those hosts, with three controls still active. Among the hosts with active controls, the agent mitigated three threats across two hosts, while one host remains protected with no threat detected yet.

Clicking each stage of the prevention flow filters the summary table to data specific to that stage. The table then displays an overview of the suspicious behavior or actions taken by Agentic Threat Prevention. Use the summary table to review affected behaviors, controls, threats, and hosts

#### Summary Table - Suspicious Behavior

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(91).png)

- **Suspicious Behavior Tab:** Displays the behaviors the agent considered suspicious
- **Hosts With Suspicious Behavior Tab:** Displays the hosts the suspicious behavior was detected on. Clicking on a host opens the panel

#### Summary Table - Activated Controls

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(92).png)

- **Controls Tab:** Displays the controls that the agent has applied, the suspicious behavior the control prevented, and the current status of the controls. Clicking a suspicious behavior or host control status opens the panel. In the example above, the Rclone Download control was applied to prevent 2 suspicious behaviors across 15 hosts. That control expired on 14 of those hosts and is still active on 1
- **Hosts With Active Controls Tab:** Displays the hosts that have active controls applied to them. Clicking on a host opens the panel

#### Summary Table - Mitigated Threats

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(93).png)

- **Threats Tab:** Lists the mitigated threats and shows how many hosts were affected by each threat
- **Hosts with Mitigated Threats Tab:** Lists the hosts where Agentic Threat Prevention mitigated one or more threats

### Understanding the Details Panel

Selecting a link in a Summary table opens the Details panel with related information. From the **Suspicious Behavior** table, you can review the controls applied in response. From the **Activated Controls** table, you can review the suspicious behavior that triggered each control.

The Details panel is primarily used to investigate hosts. Select a host in a Summary table to open the panel, which contains three tabs:

#### Host Details

A high-level summary of the host, including an AI-generated summary. This is a natural language description with rich context of what Agentic Threat Prevention identified, which controls it applied, and, when relevant, which threats it mitigated:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(97).png)

#### Timeline

The timeline of activity on the host:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(98).png)

#### Agentic Threat Prevention

Shows how the host progressed through each stage of the prevention flow. Select a stage to update the table with the corresponding information.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(137).png)

Clicking on the **Activated Controls** stage displays the controls that are currently applied to a host. By hovering over the **Control Status**, you can view the date and time the control will expire. The active window varies by control type. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(138).png)

### Understanding the Sankey Diagram

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(136).png)

Use the Sankey diagram to trace progression through the prevention flow, from suspicious behavior through activated controls to the final outcome. The connecting paths show how each stage relates to the next. Select a stage to view the corresponding details in the table.

This data can also be viewed in table form with links that open the Details Panel.
