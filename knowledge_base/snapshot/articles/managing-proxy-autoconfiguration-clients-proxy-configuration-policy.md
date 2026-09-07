---
title: "Managing Proxy Auto-Configuration for Clients (Proxy Configuration Policy)"
slug: "managing-proxy-autoconfiguration-clients-proxy-configuration-policy"
updated: 2026-08-23T12:37:11Z
published: 2026-08-23T12:37:11Z
canonical: "knowledge.catonetworks.com/managing-proxy-autoconfiguration-clients-proxy-configuration-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Proxy Auto-Configuration for Clients (Proxy Configuration Policy)

This article explains how to manage the Proxy Configuration Policy for users and user groups in your account.

## Overview

If your network architecture contains proxy servers that you manage, then hosts in your network require a PAC file to know which proxies to send relevant traffic to. The Proxy Configuration Policy defines a URL where a PAC file is located so that it can be downloaded by a browser. You can configure different URLs for different users or User groups.

### Policy Revisions and Concurrent Editing by Multiple Admins

The Proxy Configuration Policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Prerequisites

- The Proxy Configuration Policy is supported for Clients installed on the following operating systems:
  - Windows
  - macOS
  - iOS

## Configuring the Proxy Configuration Policy

The Proxy Configuration Policy is an ordered rule base that sequentially checks if a rule is met. When a user meets a rule, the PAC file is made available for their browser to download. If no rule is met, the user traffic is routed directly to the Cato Cloud without using a proxy server.

![PCP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218253717405.png)

**To configure the Proxy Configuration Policy:**

1. From the navigation menu, click **Access > Proxy Configuration Policy**.
2. Click **New**.

The new rule panel opens.
3. Enter a **Name** for the rule.
4. Define the **Users/Groups**, **Platforms**, and enter the **PAC file URL**.
5. Repeat steps 2-4 for each rule in the Proxy Configuration Policy.
6. Enable the **Proxy Configuration Policy** and then click **Save**.

The slider is green when the rule is enabled, and gray when the rule is disabled.
