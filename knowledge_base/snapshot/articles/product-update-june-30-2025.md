---
title: "Product Update - June 30, 2025"
slug: "product-update-june-30-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-june-30-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 30, 2025

## New Features & Enhancements

- **Explore SASE with CatoLabs:** Spin up a self-guided lab environment to learn more about the Cato platform - no setup, no impact on production. Ideal for training, testing, and hands-on practice. [We rolled out the initial lab units](https://academy.catonetworks.com/page/labs) (such as GenAI Security), and more will be coming soon.
  - CatoLabs is currently in beta and may change as we gather feedback and make improvements
  - Please share your feedback with us at [labs@catonetworks.com](mailto:labs@catonetworks.com)
- **DEM Enhancements for Zoom and Teams Integrations:** To better indicate end-user experience issues with UCaaS apps, we made the following adjustments to metrics shown on the [Experience Monitoring page](/v1/docs/using-the-experience-monitoring-page):
  - For Zoom, we improved the meeting quality score calculation to provide a more accurate reflection of the worst user experiences during the session
  - For [Zoom and Microsoft Teams](/v1/docs/experience-monitoring-connectors), the page now shows both the **Maximum** and **Average** experience scores in the call summary. This highlights brief performance issues that may have impacted the user experience
    - Previously, only the **Average** was shown
- **New Release for Windows Client v5.16:** Starting July 1, 2025, we are rolling out the new Client version 5.16 for Windows. This version includes:
  - Updates the Client embedded browser to Chromium version 135.0.220
  - Bug fixes and performance enhancements
- **Edit App Activities API Integration Configuration:** You can now edit and update existing [App Activities integration settings](/v1/docs/application-control-via-api-with-app-activities) from the Resources > Integrations page on the Integrated Apps tab. This lets you modify parameters such as the expired integration secret, ensuring continued integration without disruption.
- **Reminder for July 1 - Automatic Migration to the Layer 7 Socket LAN Firewall:** The [Next Gen Layer 7 LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall) provides L7 enforcement and account-level configurations, enabling seamless LAN segmentation without sending the traffic over the last mile to the PoP. Starting on July 1, 2025, we are automatically migrating rules from your current site-level LAN Firewall policy to the new unified Next Gen LAN Firewall policy.
  - Each site-level rule will automatically be configured in the policy as a LAN Network rule to specify the routing, and a Firewall rule to allow or block the traffic
  - The rules for each site will be added as a separate section in the rulebase, and the site name is used for the section
  - Next Gen LAN Firewall is supported from Socket v22 and higher
  - Click [here](https://academy.catonetworks.com/next-generation-lan-firewall-migration) to watch a video recording of this feature
- **EPP Agent v1.4.2:** On June 24, 2025, we started rolling out [EPP Agent version 1.4.2](/v1/docs/summary-of-epp-agent-versions). This version includes the following bug fix:
  - EPP Agent service might not start following a reboot in some cases

## PoP Announcements

- New ranges are available for these PoP locations:
  - **Marseille, FR:** 159.117.225.0/24
  - **Paris, FR:** 159.117.224.0/24

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
