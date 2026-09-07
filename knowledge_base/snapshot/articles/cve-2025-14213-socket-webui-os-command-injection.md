---
title: "CVE-2025-14213 Socket WebUI: OS Command Injection"
slug: "cve-2025-14213-socket-webui-os-command-injection"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cve-2025-14213-socket-webui-os-command-injection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CVE-2025-14213 Socket WebUI: OS Command Injection

## Description

Socket versions lower than v25 contain a command injection vulnerability that allows an authenticated attacker with access to the Socket Web Interface (WebUI) to execute arbitrary operating system commands as the root user on the Socket’s internal system.

## Severity

The CVSSv4 score is 8.3 (High).

## What Changes Do I Need to Make?

From the navigation menu, click **Network** > **Sites**, and check the version of the connected Sockets inside the **Socket Versions** on the right side of the page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33185588578845.png)

## Acknowledgments

Cato Networks thanks the researchers from BugCrowd's bug bounty program for detecting and identifying the issue.

## What is the Impact on the Account?

If you don’t upgrade to Socket version 25, the Socket will remain vulnerable. To the best of our knowledge, none of these issues has been exploited in the wild.
