---
title: "Managing Agentic Threat Prevention"
slug: "managing-agentic-threat-prevention"
status: "update"
updated: 2026-09-06T10:18:19Z
published: 2026-09-06T10:18:19Z
canonical: "knowledge.catonetworks.com/managing-agentic-threat-prevention"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Agentic Threat Prevention

## Overview

Agentic Threat Prevention automatically applies controls to hosts to reduce the attack surface and help prevent threats before they impact your environment. For more information, see [What is Agentic Threat Prevention?](/v1/docs/what-is-dynamic-prevention).

For each threat category, define the automatic action: **Block** or **Monitor** and how each action is tracked. These threat categories represent different stages of the attack lifecycle, such as lateral movement or command and control. You can view the enforced rules and the threats they prevent.

### Prerequisites

- TLS is enabled

## Configuring Agentic Threat Prevention

By default, Agentic Threat Prevention is enabled. For each Threat Category, the Action is set to Block, and the tracking is set to create an event. To meet your security requirements, change these configurations.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(89).png)

**To configure Agentic Threat Prevention:**

1. From the navigation menu, click **Security >** **Agentic Threat Prevention.**
2. (Optional) For each **Threat Category**, configure the **Action** and tracking options. For more information, see [Monitoring Agentic Threat Prevention](/v1/docs/managing-dynamic-prevention#monitoring-dynamic-prevention-threat-prevention).
3. Enable the toggle.
4. Click **Save**.

## Monitoring Agentic Threat Prevention

You can monitor Agentic Threat Prevention activity with:

- **The Agentic Threats Page:** View details of the controls applied to hosts and the threats prevented from the **Agentic Threats** page. For more information, see [Monitoring Agentic Threat Prevention](/v1/docs/monitoring-agentic-threat-prevention).
- **Events:** Agentic Threat Prevention generates the following event types:

**Note:** Agentic Threat Prevention Events have the subtype **Agentic Threat Prevention**. For more information, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).
  - **Control Applied**: Generated when a control is applied to a host
  - **Malicious Action Detected** *(optional)*: Generated when a malicious action is detected Configure whether to generate an Event, Notification, or both. If you have an XOps license, an XOps story is also generated

**To enable Events or Notifications:**

1. From the navigation menu, click **Security >** **Agentic Threat Prevention.**
2. For each **Threat Category**, click **Event**.
3. Configure the required tracking options:
  - Subscription Group (For more information, see [Creating Subscription Groups](/v1/docs/creating-subscription-groups))
  - Mailing List (For more information, see [Working with Mailing Lists](/v1/docs/working-with-mailing-lists))
  - Webhook (For more information, see [Sending CMA Notifications via Webhooks](/v1/docs/sending-cma-notifications-via-webhooks))
4. Click **Save.**

## Excluding Hosts From Controls

To prevent specific controls from being applied to a host, add the relevant signature to the **IPS Policy Allowlist**. For more information, see [Allowlisting IPS Signatures](/v1/docs/allowlisting-ips-signatures).

You can allowlist either:

- **Suspicious behavior signatures**: No controls associated with the suspicious behavior are applied to the host
- **Control signatures**: Only the selected control is excluded from the host

### Identifying Signatures for the IPS Policy Allowlist

Identify both suspicious behavior and control signatures from the **Threat Catalog**. For more information, see [Using the Threat Catalog](/v1/docs/using-the-threat-catalog).

#### Identifying Suspicious Behavior Signatures

Suspicious behavior signatures describe behaviors detected by the Agentic Threat Prevention engine. Opening a signature shows a description of the behavior and the controls that are applied when the behavior is detected.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(94).png)

**To identify Suspicious Behavior signatures:**

1. From the navigation menu, click **Resources > Threat Catalog.**
2. In the **Engine** filter, add a filter for **Dynamic Prevention.**
3. In the **Signature** filter, enter **cid_atp_c.** The suspicious behavior signatures are displayed.

#### Identifying Control Signatures

Control signatures represent the individual controls that can be applied when suspicious behavior is detected. Opening a control signature shows a description of the control.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(95).png)

**To identify Control signatures:**

1. From the navigation menu, click **Resources > Threat Catalog.**
2. In the **Engine** filter, add a filter for **Dynamic Prevention.**
3. In the **Signature** filter, enter **cid_atp_r.** The control signatures are displayed.

### Excluding Hosts from the Events Page

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(96).png)

Add suspicious behavior or control signatures to the **IPS Policy Allowlist** directly from the **Events** page.

Click the **Signature ID** link to open a panel with a pre-populated IPS Policy allowlist rule. Review or edit the rule as needed, and then click **Apply** to add it to the allowlist.

### Version Control

| Date | Description |
| --- | --- |
| September 6, 2026 | Updated the name of Agentic Threat Prevention Events |
