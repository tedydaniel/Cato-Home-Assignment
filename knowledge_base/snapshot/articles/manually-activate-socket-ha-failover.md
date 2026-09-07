---
title: "Manually Activate Socket HA Failover"
slug: "manually-activate-socket-ha-failover"
updated: 2026-08-12T18:13:45Z
published: 2026-08-12T18:13:45Z
canonical: "knowledge.catonetworks.com/manually-activate-socket-ha-failover"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manually Activate Socket HA Failover

This article provides information about manually switching the HA roles of your primary and secondary Sockets.

## Overview

Manual high availability (HA) failover lets you test your Socket environment by temporarily failing a site over to the Secondary Socket from within the Cato Management Application (CMA). This can help to validate that HA is correctly configured and responsive to failover events

This capability gives you control over failover timing, allowing for a safer and more predictable validation process. Use the Socket page fail over to the Secondary Socket.

> [!NOTE]
> Important:
> 
> - Ensure that onsite Socket personnel are available before performing a manual HA failover in case any issues require physical access.
> - Do not use the manual HA failover to perform Socket maintenance​ - this can create a split-brain issue for the Sockets

### How Manual Failover Works

Triggering a manual failover from the CMA performs these actions:

- The CMA tells the Primary Socket to stop sending VRRP packets
- The Secondary Socket detects the failure and takes over as the Master Socket
- After approximately 120 seconds, the CMA displays:

This behavior is expected and confirms that the Secondary is now active.
  - Status: **Not Ready (In HA Failover)**
  - Both Sockets will appear as Master (split-brain scenario), indicating the Secondary has taken ownership

### Prerequisites

Before triggering a manual HA failover, make sure:

- Both Sockets are running Socket version 24 or higher
- The HA state is **Ready** in the CMA

### Best Practices

- Do not leave the environment in a manual failover state longer than necessary
- Use this feature only for maintenance or validation scenarios
- Always return HA to a **Ready** state promptly to maintain system resilience

## Activating Manual HA Failover

![manual-HA-failover.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31661536014365.png)

**To trigger the manual failover:**

1. From the navigation menu, select **Socket > Actions > Activate Manual HA Failover**.
2. Wait approximately 120 seconds.
3. Refresh the Socket page to verify the new status.

## Reverting to the Primary Socket

You can return control to the Primary Socket in one of the following ways:

- Option 1: From the navigation menu, select **Socket > Actions > Deactivate Manual HA Failover**
- Option 2: Restart the Primary Socket. The CMA automatically restores the original HA configuration to the site.
