---
title: "Product Update - July 29, 2024"
slug: "product-update-july-29-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-29-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 29, 2024

- **Improved Initial Upgrade for Sockets:** When you connect a Socket to the network, it immediately attempts to upgrade to the newest Socket version. We improved the upgrade mechanism to detect issues during the upgrade process and if there’s an issue, then it automatically restarts the upgrade.
  - Previously, after a failed upgrade you couldn’t assign the Socket and you had to contact Support to proceed with the upgrade
- **New Labels for Beta APIs:** We are starting to mark new APIs in the [API Reference portal](https://api.catonetworks.com/documentation/#introduction) with a **Beta** label to indicate that the API schema may change frequently and with notice a short time in advance.
  - APIs not labeled **Beta** are GA (General Availability). There are rarely breaking schema changes for APIs in GA and we will announce them months in advance
- **Enriched Events for Inline and Out-of-Band App Activity Traffic:** The inline [Application Control](/v1/docs/managing-the-application-control-policy) policy and out-of-band [SaaS Security API](/v1/docs/what-is-the-data-protection-api) policy help you secure traffic to your organization’s sanctioned cloud apps. For easier analysis of the activities your users perform in these apps, we added new event fields for general categories of app activities instead of only specific ones. For example, filter the Events page for the **Communication & Collaboration** category to show all the events for the **Chat**, **Video**, and **Voice** activities, instead of viewing one activity at a time.
  - New fields include **App Activity Category** and **App Activity Type**
  - The fields appear in events of subtypes **Apps Security** and **Apps Security API**
- **Configure Default Block Action for DLP Scans that Don’t Complete:** We're adding the option to configure a fail-closed mode that blocks the traffic if Cato’s [DLP](/v1/docs/what-is-the-cato-dlp-service) can't complete the scan. For example, if a file is too large to scan or if the scan times out.
  - By default, the [Data Control policy](/v1/docs/creating-the-data-control-policy) fails open and allows traffic for uncompleted scans
  - There is no change to the current behavior
- **New Cato Icons and Visio Stencils:** To help you with network diagrams and Cato-related presentations, we created new and improved [Cato icons (SVG files)](/v1/docs/cato-networks-stencils-and-icons).
  - The icons are also available in a Visio stencil

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
