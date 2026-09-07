---
title: "Socket Version 21.1 Release Notes"
slug: "socket-version-21-1-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-21-1-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 21.1 Release Notes

## New Features and Enhancements

Socket version 21.1 includes the firmware for new features, and in the coming weeks we will update the Cato Cloud and release the following features.

- **DEM Enhanced Underlay Performance Monitoring in Socket Last Mile**: To identify and diagnose out-of-tunnel issues that could impact last-mile performance, we enhanced Experience Monitoring (DEM) and the Socket will now periodically send probes to the connected PoP IP directly over the Internet.
- **Enhanced Troubleshooting Tools for Socket WebUI:** To provide precise control over test durations for Ping and Traceroute tools, the Socket WebUI now includes **"Count"** and **"Interval"** options. These enhancements allow users to run longer, customizable tests to better identify intermittent issues and monitor network performance over time.
- **BGP Ingress Route Filters:** BGP Ingress Route Filters let you control inbound routes with granular match options like prefix lists and communities. This helps ensure only valid and relevant routes are accepted, enhancing network agility, security, and stability. Filter out unnecessary or unauthorized routes for improved routing control and optimized network performance. You can also better control the gradual migration of routes towards Cato.
- In addition, this version includes:
  - Stability improvements
  - Security updates
  - Bug fixes

This version will not be rolled out to all accounts automatically and will only be available using the [Upgrade Now](/v1/docs/manually-upgrading-a-socket) feature.
