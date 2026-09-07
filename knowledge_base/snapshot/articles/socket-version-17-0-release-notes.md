---
title: "Socket Version 17.0 Release Notes"
slug: "socket-version-17-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-17-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 17.0 Release Notes

Socket version 17.0 includes the following content:

- Security updates
- Performance and stability enhancements.
- **BGP Behavior Optimization**: Previously, when a Socket was disconnected from the Cato Cloud, sometimes it would only withdraw ranges for remote Socket sites, while ranges for other remote site types, like IPSec, were not withdrawn.
  - Now the Socket no longer advertises any remote ranges when it is not connected to the Cato Cloud.

- **Socket WebUI Traffic Capture Enhancements**:
  - Capturing traffic from multiple Socket interfaces at the same time.
  - Implementing packet filtering syntax during traffic recording.
