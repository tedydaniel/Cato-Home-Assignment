---
title: "End of Support (EoS) Policy for Cato vSockets"
slug: "end-of-support-eos-policy-for-cato-vsockets"
tags: ["vSockets"]
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/end-of-support-eos-policy-for-cato-vsockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# End of Support (EoS) Policy for Cato vSockets

## Overview

When the cloud environment hosting the vSocket, such as VMware ESXi or KVM, reaches End of Life (EoL) status by its vendor, Cato evaluates and announces the End of Support (EoS) timeline for vSockets running on those platforms.

When a vSocket version or its hosting environment is EoS:

- Cato no longer supports that version, and you can't open tickets related to the outdated platform
- We strongly recommend that you upgrade to the newest supported cloud environment version or component as soon as possible

**Best Practice:** To avoid disruptions, we recommend that you upgrade your cloud environment before the announced EoS date.

### EoS Notification Timeline

When Cato plans to declare a vSocket version or hosting platform as EoS:

- You receive an email notification three months before the official EoS date
- In case of a critical issue with an older vSocket version, the EoS notification period may be shorter than three months

**Example**

On May 1, Cato announces that ESXi vSphere v6.7 will reach EoS on August 1 and sends notifications to affected accounts. On August 1, ESXi vSphere v6.7 is officially EoS, and you can't open Support tickets for it.

## EoS for ESXi vSphere Versions

These ESXi vSphere versions are announced as EoL by VMware and will be EoS by Cato as follows:

- December 31, 2025
  - vSphere v6.7 - EoL date Oct 2024
  - vSphere v7.0 - EoL date Oct 2025

Existing vSockets on these versions may continue to function, and Support tickets will be addressed if the issue isn't related to an outdated platform.
