---
title: "Tracking the Status of Policy Changes"
slug: "visibility-for-publishing-cma-policies"
updated: 2026-07-22T06:21:07Z
published: 2026-07-22T06:21:07Z
canonical: "knowledge.catonetworks.com/visibility-for-publishing-cma-policies"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tracking the Status of Policy Changes

## Overview

When you publish a policy in the Cato Management Application (CMA), the updated configuration propagates gradually across the Cato Cloud. The **My Policy Changes** tab in the **Notifications** panel lets you track that propagation, confirming whether changes are still in progress or have been successfully applied to the relevant PoPs. You can also review changes from the past 30 days and jump directly to related Audit Trail records.

The tab only shows your policy changes, not those of other admins in the account.

This feature is only available for [policies](/v1/docs/working-with-policy-revisions) that you **Publish**, such as Internet Firewall. CMA pages that you **Save**, such as Access > MAC Authentication, are not shown in **My Policy Changes**.

### Understanding Policy Propagation

After you publish a policy, the updated configuration is distributed across the PoPs in the Cato Cloud. During the propagation and validation processes, different PoPs can receive and enforce the new policy at slightly different times.

A policy change is considered complete only after the updated configuration has reached all the PoPs your sites and users connect to.

On average, policy changes are propagated in less than 1 minute.

**Note:** The **My Policy Changes** page shows an approximate deployment time, and occasional delays in the displayed status don't necessarily reflect actual propagation delays.

## Monitoring Your Policy Changes

The **My Policy Changes** tab displays only your policy changes. Each entry includes information such as:

- Policy name
- Publication time
- Current propagation status
- Completion percentage
- Link to the related Audit Trail records

When your publishing is in progress, an animation appears on the notifications icon ![notification_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32185544095517.png) at the top of every page in the CMA. Clicking the notifications (bell) icon and going to the **My Policy Changes** tab shows the status of the policy propagation that is in progress.

![my_policy_changes.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32184609538717.png)

For the detailed log information about a specific policy change, click the [Audit Trail](/v1/docs/using-the-audit-trail) link. The **Audit Trail** page automatically opens with filters applied to show your changes to the selected policy.

**To view the status of your recent policy changes:**

1. From the top of the CMA, click **Notifications** (bell icon). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(13).png)
2. Select **My Policy Changes**.
