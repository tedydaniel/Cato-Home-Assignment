---
title: "Users and User Groups Can No Longer be Included as a Source in Connectivity Health Rules"
slug: "users-user-groups-can-no-longer-be-included-as-source-in-connectivity-health-rul"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/users-user-groups-can-no-longer-be-included-as-source-in-connectivity-health-rul"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Users and User Groups Can No Longer be Included as a Source in Connectivity Health Rules

**Note:** This article has been updated on April 10, 2025 - see Comments for more details

## Overview

From May 5, 2025, users and user groups can no longer be included as a **Source** in [Connectivity Health Rules](/v1/docs/working-with-link-health-rules) (Network > Link Health Rules).

Users regularly connect and disconnect from a network. When you include users or user groups in a Connectivity Health Rule, it generates many email notifications that are unrelated to link connectivity or quality. Including users or user groups in a Connectivity Health Rule does not provide the intended functionality of the Connectivity Health Rules feature.

The sources that can no longer be used are:

- User Groups
- Users
- System Group: All SDP Users
- System Group: All Users

## What is the Impact on My Account?

- If you have Connectivity Health Rules that include users or user groups, after May 5, 2025, no Health Alerts will be sent for rules that include users or user groups as the source.
- If you have Connectivity Health Rules that include **Any** as the source, they will exclude alerts for user or user group related events after May 5, 2025.

## What Changes Do We Need to Make?

Review your Connectivity Health Rules and remove all Users and User Groups from the Connectivity Health Rules where they are the **Source** so that those rules are not deleted by Cato.

## What if We Want to Continue to Use this Functionality after May 5, 2025?

If you want to continue to use Connectivity Rules for users and user groups after May 5, 2025, contact your account representative and we will coordinate an alternative solution.

## Who do I Talk to If I have Questions?

Please contact Support or your account representative.
