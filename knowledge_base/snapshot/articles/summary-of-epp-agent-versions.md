---
title: "Summary of EPP Agent Versions"
slug: "summary-of-epp-agent-versions"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/summary-of-epp-agent-versions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Summary of EPP Agent Versions

This article summarizes the features and enhancements of the Cato EPP Agent.

For information on how to download and install the EPP Agent, see [Installing the Cato EPP Solution](/v1/docs/installing-the-cato-epp-solution).

## Endpoint Protection Agent v1.6.2

Starting the week of May 04, 2026, we are rolling out EPP Agent version 1.6.2. This version includes bug fixes and enhancements.

## Endpoint Protection Agent v1.6

Starting the week of Feb 15, 2026, we are rolling out EPP Agent version 1.6. This version includes bug fixes and enhancements.

## Endpoint Protection Agent v1.5

From Aug 17, 2025, we are starting the rollout of Endpoint Protection (EPP) Agent version 1.5. This version includes bug fixes and enhancements.

## Endpoint Protection Agent v1.4.2

From June 23, 2025, we are starting the rollout of Endpoint Protection (EPP) Agent version 1.4.2. This version fixes an issue where the EPP Agent service might not start.

## Endpoint Protection Agent v1.3

From January 12, 2025, we are starting the rollout of Endpoint Protection (EPP) Agent version 1.3. This version includes:

- Self-Healing: If the Agent encounters an error, in some cases, it will try to resolve the issue on its own. For example, if the driver is out-of-date, the Agent will attempt to download the driver.
- Bug fixes and enhancements, including:
  - Improved error messages

## Endpoint Protection Agent v1.2

From October 27, 2024, we started the rollout of Endpoint Protection (EPP) Agent version 1.2. This version includes:

- Support for Windows Servers 2022, 2019, and 2016
- Bug fixes and enhancements, including:
  - Improved error messages
  - In the agent, the **Full system scan** button is enabled only with an EPP license

## Endpoint Protection Agent v1.1.7

From September 22, 2024, we started the rollout of Endpoint Protection (EPP) Agent version 1.1.7, which includes this enhancement:

- We improved the validations that the Agent runs when upgrading to a newer version

## Endpoint Protection Agent v1.1

From May 05, 2024, we started the rollout of EPP Agent version 1.1. This version contains:

- **Protection Against Threats That Take Advantage of Software Vulnerabilities**: The new Anti Exploit engine uses machine learning to protect against threats that attack software vulnerabilities. Examples of attack techniques that are protected against include:
  - Privilege escalation
  - Process introspection
  - LSASS credential dumping
- **Automated Check for Other Anti-Virus Solutions**: Cato's EPP Agent cannot effectively protect an endpoint if another Anti-Virus solution is running on it. During the installation process, the Agent checks if another Anti-Virus is installed on the endpoint and displays an error message if a solution is identified.
- **Uninstall and Delete the Agent in One Action:** You can now uninstall the Agent from an endpoint and delete it from your account in one action.
  - Previously, uninstalling the Agent and deleting the Agent had to be done separately
  - If required, you can still uninstall the Agent from an endpoint without deleting it from your account

## Endpoint Protection Agent v1.1.6

From August 4, 2024, we started the rollout EPP Agent version 1.1.6 which includes this enhancement:

- File Paths added to the [Allow List](/v1/docs/configuring-endpoint-protection) are now excluded from Behavioral Analysis detections as well as Anti-Malware detections
