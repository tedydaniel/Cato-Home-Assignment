---
title: "Azure vSocket is disconnected after a version upgrade"
slug: "azure-vsocket-is-disconnected-after-a-version-upgrade"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/azure-vsocket-is-disconnected-after-a-version-upgrade"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure vSocket is disconnected after a version upgrade

## Overview

This article explains the steps to take in case the Azure VM is stuck on reboot during an upgrade to Socket v21 and v20 whilst upgrading from Socket v19 or below.

## Symptoms

- While performing an upgrade that requires a reboot, you may encounter a situation in which the VM is stuck in the reboot phase.
- How to identify such issue: This issue can be identified if an upgrade was triggered, failed, and the vSocket is still disconnected after the upgrade failure alert and event were sent. In this case you can act upon the suggested solution.

## Solution

To resolve the issue, please power cycle your instance by clicking on the VM and select Stop (wait for the process to end) and then start. The vSocket will boot into the new version.

This issue was fixed in v20 and v21 thus once the vSocket upgraded we will not encounter this issue in future versions.
