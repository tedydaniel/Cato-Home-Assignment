---
title: "Drilling-Down and Analyzing XOps Account Operations Stories"
slug: "drilling-down-and-analyzing-xops-account-operations-stories"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/drilling-down-and-analyzing-xops-account-operations-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Drilling-Down and Analyzing XOps Account Operations Stories

This article discusses how you can use the Stories Workbench to review Site Operations stories for connectivity and performance issues on your network.

> [!NOTE]
> Note:
> 
> XOps is Cato’s unified analytics layer for security and operations, offering insights and guided remediation. XOps has replaced XDR, for more information, see [XOps FAQ](/v1/docs/xops-faq).

## Overview

XOps Account Operations stories highlight operational issues that impact the health and configuration of your account as a whole. The Account Operations producer detects account-level conditions such as directory sync failures, license exhaustion, expired certificates, connector issues, and other scenarios that can impact users, sites, and services. The generated stories help you identify systemic risks, understand their scope and impact, and follow guided remediation workflows to restore normal operation.

The Stories Workbench page shows the details of each story to help you understand and analyze the issues. You can sort and filter the stories to find the most important incidents, and then drill-down on a story to further investigate the details to resolve the issue.

### Account Operations Story Indications

These are the indications of account-level operational issues that are detected by the Account Operations producer to generate stories:

| Indication | Description |
| --- | --- |
| **BGP Prefix Exhaustion** | The BGP routing table reached the maximum allowed number of learned IP prefixes, causing additional prefixes to be ignored. This may lead to routing instability or suboptimal traffic paths. |
| **DC Connectivity Failure (WMI)** | Directory Services synchronization failed due to a WMI query failure, preventing directory data from being retrieved from the domain controller. |
| **LAN IP Conflict** | An IP address conflict was detected on the LAN, where multiple hosts attempted to use the same IP address, potentially causing intermittent connectivity issues. |
| **LDAP Active Directory Sync Failed** | Directory Services synchronization failed due to a previous error, preventing Active Directory data from being synchronized successfully. |
| **IPsec Phase 2 Failure** | IPsec Phase 2 negotiation failed, preventing the tunnel from being fully established and potentially disrupting encrypted traffic between tunnel endpoints. |
| **SaaS Apps Connector Down** | A SaaS application connector is experiencing a connectivity error and is not retrieving data from the application. |
| **SCIM Provisioning Failed** | SCIM provisioning operations failed, preventing user or group changes from being synchronized with the target application. |

## Showing the Stories Workbench Page

The Stories Workbench page shows a summary of the XOps stories for your account.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

## Drilling-Down and Analyzing Stories

You can click on a story in the Stories Workbench to drill-down and investigate the details in a different page. This page contains a number of widgets that help you evaluate the issue identified by the Account Operations producer.

![XOps Account Operations story.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310959122717.png)

### Understanding the Story Drill-Down Widgets

These are the story drill-down widgets:

| Name | Description |
| --- | --- |
| **Story summary** | At the top of the page there is a summary of basic information about the story, including: - The story type (indication) - The producer that generated the story - The story's criticality - The number of times the issue occurred - The story duration - The story's current status |
| **Story timeline** | Shows a timeline of changes in the story status |
| **Details** | Basic information for analyzing the story, including the time of the first signal for the story, when the story was created, the story ID number, a summary of the story impact, and other relevant information. For example, for an **LDAP Active Directory Sync Failed** story, the domain name is shown. |
| **Related Events** | A timeline of events related to the story. Click **View All** to open the [Events](/v1/docs/analyzing-events-in-your-network) page prefiltered to show events related to the story. |
| **Incident Timeline** | A list of the detected incidents for issues and resolutions in the story. For each incident, the timeline shows when the incident occurred, when it was validated, a brief description, and a link to show the [Events](/v1/docs/analyzing-events-in-your-network) page pre-filtered for the incident. |
| **Playbook Workflow** | A step-by-step troubleshooting guide tailored to the specific issue detected in the story. This helps you quickly identify root causes and resolve the problem using clear, actionable plays. Includes links to relevant documentation. |
