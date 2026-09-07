---
title: "Performance Troubleshooting: Socket Behind a Third-Party Firewall"
slug: "performance-troubleshooting-socket-behind-a-third-party-firewall"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/performance-troubleshooting-socket-behind-a-third-party-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance Troubleshooting: Socket Behind a Third-Party Firewall

## Challenge

If you notice that there is a reduced throughput for a Cato Socket or VPN Client, one possible cause is a third-party firewall with UDP Flooding protection. This protection can limit traffic that is sent over the Cato DTLS tunnels and passes through the firewall. Often the UDP Flooding protection is enabled by default on many firewalls.

## Solution

In these kind of cases, Cato Networks recommends disabling the UDP Flooding protection in your firewall. You can run a speed test and compare the impact of this protection on your network throughput.
