---
title: "Configure User Risk Score with Entra ID"
slug: "configure-user-risk-score-with-entra-id"
status: "update"
updated: 2026-09-06T13:26:08Z
published: 2026-09-06T13:26:08Z
canonical: "knowledge.catonetworks.com/configure-user-risk-score-with-entra-id"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure User Risk Score with Entra ID

## Overview

Cato lets you use Microsoft Entra ID risk levels to enforce adaptive, risk-based access policies. Select Microsoft Entra ID as the User Risk Score source to use the risk level managed in your Entra tenant instead of the Cato-native score.

:::(Info) (Note)
Using Cato and Microsoft Entra ID as User Risk Score sources at the same time isn't supported. Select one active source for the account.
:::


Cato maps Entra risk levels to the Cato risk-level scale. Your existing policies continue to enforce rules without changes. User risk-level updates are automatically reflected in Cato within a few minutes.

## Prerequisites

* Ensure that you have the required permissions to integrate Microsoft Entra ID with Cato.
* An Entra ID P2 license is required 

## Understanding the Risk-Level Mapping

When Microsoft Entra ID is the active User Risk Score source, Cato maps Entra risk levels to Cato risk levels:

| Microsoft Entra ID Risk Level | Cato Risk Level |
| ----------------------------- | --------------- |
| None                          | Low             |
| Low                           | Medium          |
| Medium                        | High            |
| High                          | Critical        |

The mapping is automatic and cannot be configured.

## Connecting Microsoft Entra ID

Before selecting Microsoft Entra ID as the User Risk Score source, connect the Microsoft 365 and Microsoft Entra ID integrations.

To connect Microsoft Entra ID:

1. From the navigation menu, select **Resources > Integrations**
2. On the **Configured Integrations** tab, add a **Microsoft 365 (New Tenant)** integration if one is not already configured
3. For the integration capability, select **MS Integration Setup**, complete the required Microsoft consent, and save the integration
4. Add a **Microsoft Entra ID** integration
5. For the capability, select **Entra ID Risky Users**
6. Complete the required fields and save the integration

The Entra ID Risky Users capability retrieves risky-user and risk-detection signals from Microsoft Graph Identity Protection. It is associated with the Microsoft 365 integration as its parent.

## Selecting Microsoft Entra ID as the User Risk Score Source

To use Microsoft Entra ID risk levels in Cato:

1. From the navigation menu, select **Access > User Risk Score**
2. Confirm that **Microsoft Entra ID** shows the **Connected** status
3. Select **Microsoft Entra ID**
4. Click **Save**

Cato starts using the mapped Entra risk levels for user records and policy enforcement.

If Microsoft Entra ID isn't connected, the page shows **Connect** instead of the connected status. Click **Connect** to open the Integrations page and configure the required integration.

## Viewing Entra User Risk Levels

When Microsoft Entra ID is the active source, the **Risk Level** column on the Users pages displays the Microsoft logo. The displayed values use the Cato risk-level scale.

Click the external-link icon next to a risk level to open the Microsoft Entra ID **Risky Users** page and investigate the user in Entra.

The Cato User Risk Score Dashboard is unavailable while Microsoft Entra ID is the active source. Cato continues to collect security data. If you later select Cato as the User Risk Score source, Cato uses the collected data to calculate user risk levels.

## Using Risk Levels in Policies

You can use the mapped risk level in existing Internet Firewall and WAN Firewall rules. No policy changes are required when you change the User Risk Score source.

For instructions on creating risk-based firewall rules, see [Define User Risk Level Policies](https://knowledge.catonetworks.com/docs/understanding-the-user-risk-level#DefineUserRiskLevelPolicies).

## Monitoring User Risk-Level Changes

Cato audits changes to the User Risk Score source. When a user’s risk level changes, Cato generates a User Risk Event that includes the score source.

When a risk level is reset in Microsoft Entra ID, Cato generates an event and an audit-log entry.
