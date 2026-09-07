---
title: "Overview of Scouts and Agent Controls"
slug: "overview-of-scouts-and-agent-controls"
updated: 2026-08-27T07:05:51Z
published: 2026-08-27T07:05:51Z
canonical: "knowledge.catonetworks.com/overview-of-scouts-and-agent-controls"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview of Scouts and Agent Controls

## Overview

Together, Scout, Agent Controls, and Agent Policy help security teams move from discovering local AI coding tools, to observing agent activity, to enforcing organizational standards for secure AI-assisted development:

- **Scout** is Cato AI Security’s endpoint discovery solution for local AI coding agents. It answers a key security question: **What AI tools are developers using on their machines?** Scout scans developer workstations to identify locally installed AI-powered development tools and give security teams visibility into AI tool adoption across the organization.
- **Agent Controls** extend this visibility into agent interactions by providing event-triggered integration points for local AI coding agents. When supported agent activity occurs, such as a user message, tool call, tool response, or MCP-related interaction, Agent Controls surface the event to Cato AI Security so it can be evaluated using Agent Policy.
- **Agent Policy** can govern what users are allowed to send to coding agents, which tools or MCPs agents are allowed to use, and what action to take when activity matches a rule.

### Supported OS

- macOS, Windows, and Linux

## Deploying Agent Controls via Scout Settings

Configure Scout Settings before deploying Scout to endpoints. These settings determine whether Agent Controls are deployed with Scout and which users or groups receive their enforcement.

Agent Controls provide event-triggered integration points for local AI coding agents. They allow supported coding-agent activity to be surfaced to Cato AI Security for visibility and Agent Policy evaluation.

When **Enforcement** is enabled, Scout enforces Agent Controls on detected AI coding tools. This allows Cato AI Security to receive supported agent events, so those events can be evaluated using Agent Policy.

The **Enforcement Policy** controls which users or groups receive Hooks enforcement. Select specific users or groups to limit enforcement to those identities. If the enforcement policy is empty, Agnet Controls enforcement applies to everyone.

To deploy Agent Control and configure the enforcement policy:

1. Navigate to the **AI Security > Scout** page and click **Settings**.
2. Click the **Enforcement** toggle to enable enforcement.
3. **Optional:** Define which users and groups the Agent Control enforcement applies to.

## Deploying Scout

Deploying Scout does not require TLS inspection, a network proxy, or a browser extension. Scout operates at the endpoint level and can be deployed through an MDM or endpoint management solution.

Before deploying Scout, configure Scout Settings to determine whether Hooks are deployed and which users or groups receive Hooks enforcement.

To deploy Scout:

1. Navigate to **AI Security > Scout**.
2. Optional: Configure Scout Settings to determine whether Hooks are enforced as part of the Scout deployment.
3. Click **Configure**.
4. Copy the installation script and deploy it to target endpoints using your MDM or endpoint management solution, such as Kandji, Intune, Jamf, or an equivalent tool.
5. In the third-party solution, schedule the script to run periodically. We recommend running it every 6 hours.

Every time the script runs it updates the Scout and pulls new AI usage data.

## Working with Scout

The Scout page provides visibility into Scout deployments across developer endpoints. It helps security teams understand where Scout is installed, which endpoints are actively reporting, and whether those endpoints are configured with inline Hooks for local AI coding-agent interactions.

### Scout Page Widgets

| Widget | Description |
| --- | --- |
| Scout Activity | Shows Scout activity over the last 30 days, including the number of active Scouts. |
| Identified Users | Shows the number of users identified by Scout over the last 30 days. |
| OS Distribution | Shows the distribution of Scout installations by operating system. |
| Daily Scouts Installed | Shows the number of Scout installations detected per day over the last 30 days. |

### Scout Installations Table

| Field | Description |
| --- | --- |
| Scout ID | Unique identifier for the Scout installation. |
| User | User associated with the Scout installation, when available. |
| Hostname | Hostname of the endpoint where Scout is installed. |
| Inline Hooks | Indicates whether inline Hooks are detected or configured for the endpoint. |
| OS | Operating system of the endpoint. |
| First Seen | Date and time when the Scout installation was first detected. |
| Last Seen | Date and time when the Scout installation last reported activity. |

## Uninstalling Scout or Agent Controls

To stop using Scout or Agent Controls on an endpoint, remove the Scout installation files, the recurring installation task, and any Agent Control configuration that was added to supported coding agents.

Disabling Agent Controls enforcement in Scout Settings does not remove Agent Controls that are already configured on endpoints. You must remove the existing Agent Control configuration manually.

### Uninstalling Scout

On macOS endpoints, delete the following items:

- `/etc/aim` directory
- `/usr/local/bin/ai-scout` binary

On Windows endpoints, remove the following items:

- The scheduled task that runs Scout every 6 hours
- `C:\ProgramData\AIM\` directory
- Any Scout-related files from the endpoint

On all platforms, remove the scheduled task or cron job that runs the installation script every 6 hours.

### Uninstalling Agent Controls

Remove Agent Controls from each supported coding agent that was configured with Agent Controls.

For Cursor, delete or remove Agent Controls from the configuration file:

- macOS: `/Library/Application Support/Cursor/hooks.json`
- Linux/WSL: `/etc/cursor/hooks.json`
- Windows: `C:\ProgramData\Cursor\hooks.json`

For Claude Code, remove the Agent Controls configuration:

- macOS/Linux: Delete `/etc/aim/claude-code-hook.sh` and remove AIM entries from the Claude Code `managed-settings.json` file
- Windows: Delete `C:\ProgramData\AIM\claude-code-hook.ps1` and remove AIM entries from the Claude Code configuration

For Codex, delete or remove Agent Controls from the configuration file:

- macOS: `/etc/codex/requirements.toml &nbsp;`
- Windows: `C:\ProgramData\OpenAI\Codex\requirements.toml`

## Supported Coding Agents

The following sections list the coding agents and coding agent controls that can be detected by Cato AI Security.

### Coding Agent Discovery

- Claude Code
- Cursor
- Codex
- OpenClaw
- Claude Cowork
- Google Antigravity
- PyCharm
- IntelliJ IDEA
- Junie
- JetBrains
- Windsurf
- Copilot
- VS Code
- Hermes
- Cline
- Kilo Code
- Warp

### Coding Agent Controls

- Claude Code
- Claude CoWork
- Cursor
- Codex
- Many More to Come
