---
title: "Getting Started with XOps"
slug: "getting-started-with-xops"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/getting-started-with-xops"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with XOps

This article describes best practices for investigating threats with the Cato XOps platform.

## Overview

The Cato XOps platform enables both Security operations and Network operations teams to utilize AI and automation to monitor the organization's network for both security threats and network performance issues. XOps transforms unmanageable amounts of raw security and network events into consumable, cross-functional and actionable stories.

This article describes best practices for getting the most out of XOps to significantly enhance your organization's security monitoring and remediation of threats. First, we discuss configuring integrations to expand XOps capabilities, and then we describe an end-to-end workflow for how to investigate a story in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench), including the following steps:

1. [Configuring XOps Integrations](/v1/docs/xops-connectors)
2. [Identifying the most important stories to focus on](/v1/docs/identifying-the-most-important-xops-stories)
3. [Steps for beginning an investigation](/v1/docs/starting-an-xops-investigation)
4. [Setting a verdict and remediating the threat](/v1/docs/remediating-xops-stories)

## Setting Up Integrations for XOps

To maximize the usefulness of the XOps platform, we recommend configuring supported integrations that expand the number and type of producers for XOps stories. We recommend setting up one of the following endpoint security integrations to help you get a more complete picture of potential threats, and conduct investigations in a unified XOps platform extending into both the network and the endpoint. For a full list of XOps producers, see [Welcome to the Cato XOps Service](/v1/docs/welcome-to-the-cato-xops-service).

- **Microsoft Defender for Endpoint connector** - Customers who use Defender for Endpoint can leverage the Microsoft API to integrate Defender alert data and generate XOps stories for endpoint devices. For more about this integration, see [Microsoft Defender for Endpoint Alerts: Configuring the XOps Integration](/v1/docs/microsoft-defender-for-endpoint-alerts-configuring-the-xops-integration).
- **SentinelOne Alerts** - Customers who use SentinelOne can integrate data from SentinelOne EDR to generate stories for endpoint devices. The SentinelOne producer creates a story by correlating data SentinelOne EDR incidents based on the Agent UUID (Device ID) and the threat file Hash within 90 days. These stories include all relevant evidence for the incidents detected by SentinelOne.

For more about integrating SentinelOne Alerts, see [SentinelOne EDR: Configuring the XOps Integration](/v1/docs/sentinelone-edr-configuring-the-xops-integration).
- **CrowdStrike Alerts** - Customers that use CrowdStrike can integrate data from CrowdStrike detections based on the Incident ID. These stories include all relevant evidence for the detection identified by CrowdStrike.

For more about integrating CrowdStrike Alerts, see [CrowdStrike: Configuring the XOps Integration](/v1/docs/crowdstrike-configuring-the-xops-integration).
- **Cato Endpoint Protection** - The Cato EPP solution natively integrates with Cato XOps to generate stories for endpoint devices, with no need to configure a connector. For more about this integration, see [Cato Endpoint Protection (EPP): Configuring the XOps Integration](/v1/docs/cato-endpoint-protection-epp-configuring-the-xops-integration).

## Identifying the Most Important Stories

Selecting the right stories to work on in the Stories Workbench is a crucial first step for effective use of the XOps platform. You can use the tools and information provided in the Workbench to quickly identify the highest-priority stories to investigate. We recommend the following steps:

1. **Group the stories** - The **Group By** options can give you a quick overview of the different types of stories in your account, as well as indicate particular items of interest on the network such as sources or users. These are examples of helpful **Group By** options:

We recommend cycling through the different **Group By** options to get a quick understanding of the stories on your network from different perspectives, which can help you identify particular areas of interest to focus the investigation on.

![Stories_Workbench_Grouping2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28647966739485.png)
  - **Source** and **Source IP** - quickly see the users, devices, and IP addresses involved in stories
  - **Producer** - Quickly review the different types of stories detected. For more about the different types of Producers, see [Welcome to the Cato XOps Service](/v1/docs/welcome-to-the-cato-xops-service).
  - **Indications** - Get an overview of the specific indicators of attack detected
2. **Prioritize by Criticality** - Start by focusing on the stories with the highest Criticality score. These are the potential threats that could have the most significant impact on your network. You can click in the **Criticality** column header to sort the stories by Criticality, or filter the stories for specific Criticality levels. Also, when you use the **Group By** options, each group indicates the number of high Criticality stories for the group.

## Starting an Investigation

Once you’ve selected a story to investigate, you can click on the story to drill-down to the details in the Detection & Response [Story Overview](/v1/docs/drilling-down-and-analyzing-xops-security-stories) page. We recommend taking the following steps to gain an initial understanding of what’s happening in the story:

1. **Generate an AI Summary** - The **Details** widget includes a tool that lets you create a natural language story description generated by AI, which provides rich context and helps you quickly assess the story. Generate the summary by clicking the Generate AI Summary button.

![XDR_Core_Story_Summary.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28647966833693.png)
2. **Check if the Traffic was Blocked** - The **Target Actions** table shows events related to each target involved in the story, including whether the **Block** action was applied to the traffic by one of the Security services such as IPS. If some of the traffic to the targets wasn't blocked, then the story has a higher risk level. Even if all the traffic to the targets was blocked, it is possible that this traffic relates to an ongoing threat that requires further investigation.

![XDR_Core_Target_Actions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28648020985245.png)
3. **Assess the Targets** - The **Targets** table shows data for the potentially malicious sources outside your network site related to the story. We recommend focusing on the following columns when you start your investigation:

![XDR_Core_Targets_table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28647967016349.png)
  - The **Malicious Score** tells you the likelihood that the target is malicious, according to Cato Threat Intelligence machine learning algorithms. Scores range from 0 (benign) to 1 (malicious)
  - The **Target Links** help you understand the target reputation by looking up the target in various external threat intelligence sources
4. **Work with XOps Playbooks** - The Cato XOps Security Playbooks provide a structured approach to investigating specific types of stories. They guide you through the investigation process and help you identify action items. For stories with a relevant playbook, you can find the link to the playbook in the **Details** widget. The XOps Security Playbooks are also available [here](https://support.catonetworks.com/hc/en-us/sections/29395432221085-XOps-Security-Playbooks).
5. **Use Comments** - If the story investigation includes collaboration among team members, use **Comments** to document what work has been done and provide important information and context for the next analyst who looks into the story. For more about using comments, see [Managing XOps Story Investigations](/v1/docs/managing-xops-story-investigations).

## Setting the Verdict and Taking Remediation Steps

The **Story Actions** panel lets you perform crucial actions and record important information as you conclude your investigation. Some analysts make the mistake of closing a story without setting a verdict, and lose much of the benefit of the investigation process. When you set a verdict, you record meaningful information about the story for future reference, and can learn about recommended actions for remediation. This is an example workflow for setting a verdict and performing basic remediation steps after you identify a device has been compromised by an exploitation attempt of a known vulnerability:

1. Click **Actions > Manage Story** to open the Story Actions panel.

![XDR_Comment_buttons.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28647988757661.png)
2. Set the **Analyst Verdict** to **Malicious**.
3. Define the **Severity** of the threat.
4. Define the **Type** as **Exploitation Attempt**, and if possible define a more specific **Classification** for the threat. Use the **Additional Info** field to record details about the investigation process or the results.

![XDR_Core_Example_Verdict.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28647973741085.png)
5. Follow the **Recommended Actions**, including:
  1. Create firewall rules to block malicious targets and sources you identified in the story.
  2. Update device software to remediate the vulnerability and avoid future exploitation attacks.
6. If you identify a compromised user, you can revoke the user's remote session to prevent access to the network. For more about revoking a remote session, see [Revoking a Remote User Session](/v1/docs/revoking-a-remote-user-session).
7. Set the Story **Status** to **Closed**.
