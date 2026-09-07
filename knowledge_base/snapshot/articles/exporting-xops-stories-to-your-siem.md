---
title: "Exporting XOps Stories to Your SIEM"
slug: "exporting-xops-stories-to-your-siem"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/exporting-xops-stories-to-your-siem"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting XOps Stories to Your SIEM

## Overview

XOps stories transform unmanageable amounts of raw security and network events into consumable, cross-functional and actionable stories. To integrate XOps stories into your existing workflows and increase visibility, you can export XOps stories into your SIEM. Cato supports two types of SIEM integrations: CMA turnkey integrations that are configured from the **Integrations** page or an integration managed from a third-party.

## Configuring XOps Stories to be Exported to Your SIEM

To export XOps stories to your SIEM, you need to:

1. Create a Response Policy rule that creates events for stories
2. Create an event integration

### Step 1: Creating a Response Policy Rule

![Xops_response.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356144041373.png)

The Response Policy helps you monitor XOps stories by defining when notification actions or events are generated for the stories. For more information, see [Creating the Response Policy for XOps Stories](/v1/docs/creating-the-response-policy-for-xops-stories).

The event type for XOps stories is Detection and Response.

![Event_Type.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356121653149.png)

**To create a response policy rule:**

1. From the navigation menu, click **Home > Detection & Response Policy**.
2. Select the **Response Policy** tab.
3. Click **New**. The **Add to Response Policy** panel opens.
4. Enter a **Name** for the rule.
5. Select the **Source** of the events you want to export to your SIEM.
6. **(Optional)** Define **Criteria** that specify the characteristics a story must have to match the rule.
7. Select the **Trigger** for the rule. You can configure whether the trigger should be when a story is created, updated or both.
8. In the **Response** section, select **Event**.
9. Click **Save**. The rule is added to the policy.

### Step 2: Creating an Event Integration

You can also integrate events for XOps stories with your existing third-party services and workflows.

- For a list of vendor-supported integrations for Cato events, see [Cato Data: Third-Party Supported Integrations](/v1/docs/cato-data-third-party-supported-integrations)
- For a turnkey integration with your SIEM, see the relevant configuration articles. The supported SIEMs are:
  - [Splunk](/v1/docs/integrating-cato-data-with-splunk)
  - [Microsoft Sentinel](/v1/docs/integrating-cato-events-with-microsoft-sentinel)
