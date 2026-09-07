---
title: "Using Windows Client 5.0 on Windows Server"
slug: "using-windows-client-5-0-on-windows-server"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/using-windows-client-5-0-on-windows-server"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Windows Client 5.0 on Windows Server

## Issue

Automatic Upgrade for the Windows Client version 5.0 is disabled for hosts that use the Windows Server operating system. The Trusted Browsing feature on the Windows Server blocks the Client from authenticating.

## Solution

To use Windows Client v5.0 on a Windows Server you can use one of the following solutions and then install or upgrade the new Client version:

- Whitelist the domains for your IdP for Trusted Browsing
- Disable the Trusted Browsing feature

You can download the installation file from the [Cato Networks User Portal](https://myvpn.catonetworks.com/login).
