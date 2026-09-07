---
title: "RDP Session Established but the Remote Desktop Isn't Loading"
slug: "rdp-session-established-but-the-remote-desktop-isn-t-loading"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/rdp-session-established-but-the-remote-desktop-isn-t-loading"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# RDP Session Established but the Remote Desktop Isn't Loading

## Issue

When attempting to connect with RDP to a physical server or appliance, the session is established properly but the screen freezes or only shows black (as seen below):

![image__6_.png](https://support.catonetworks.com/hc/article_attachments/360016662738/image__6_.png)

## Environment

The problem occurs for Windows users that are using the default utility for RDP, mainly Windows 10 users, while using the RDP protocol to destinations in the network (not hosted in the cloud).

## Troubleshooting

The first step is to check if following issues exist, then you can continue to the solution (below):

1. First, make sure that none of the **WAN Firewall** rules that block RDP traffic.
2. Try to access a local resource using RDP (any device connected to your WAN that is NOT cloud based) and confirm that the screen freezes.

## Solution

Cato has a known issue with Windows 10 and its default older RDP utility, some of the TCP traffic isn't 100% transmitted through Cato's DTLS tunnel.

We recommend as a best practice to use the most up-to-date RDP application from the Microsoft store. (this solves the issue)

![5151651651561561.png](https://support.catonetworks.com/hc/article_attachments/360016551897/5151651651561561.png)
