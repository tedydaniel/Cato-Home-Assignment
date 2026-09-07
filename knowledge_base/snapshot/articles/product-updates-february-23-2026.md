---
title: "Product Updates - February 23, 2026"
slug: "product-updates-february-23-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-february-23-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - February 23, 2026

## New Features & Enhancements

- **New X1600 Cellular Socket with 5G Support:** We are introducing a new [X1600 Socket model](/v1/docs/cato-socket-deployment-guides-and-data-sheets) with embedded 5G connectivity. You can use the cellular link as a backup or for active WAN connectivity in rural areas.
  - The 5G links support the following: 1 Gbps upstream and downstream throughput, dual SIM standby
  - The X1600 5G Socket supports the same wired throughput as the X1600 base model
  - Socket v25 is the minimum version
- **Windows Client v6.0:** During the week of February 22, 2026, we will start rolling out the new [Windows Client version 6.0](/v1/docs/summary-of-cato-windows-client-releases). This version includes:
  - An indicator if the Client has connectivity issues that impact the user experience
  - Support for ARM architecture, such as Windows Surface devices
  - Stability improvements, security updates, and bug fixes
- **Cato Supports Deploying GCP vSockets from the Marketplace:** We added the Cato virtual Socket (vSocket) for the GCP public cloud to the [Google Cloud Marketplace](/v1/docs/deploying-a-gcp-vsocket-from-the-marketplace). This enhancement significantly simplifies the deployment process of the vSocket.
- **Automated Response for XOps Stories:** Automate the [Revoke User Session mitigation action](/v1/docs/configuring-automatic-responses-to-xops-stories) in the XOps Response Policy to shorten time to response and ensure consistent handling of high-risk stories.
  - For each rule, you can define criteria based on story attributes, such as criticality, user, or target, together with the automated action
  - When a story matches the rule, the remote user's session is revoked automatically
  - XOps license required
- **Application Control via API Support for Docusign:** Connecting SaaS apps to Cato lets you understand who is accessing each app and identify suspicious activities or trends even when users are not connected to the Cato Cloud. You can now connect your [Docusign account](/v1/docs/docusign-configuring-the-app-activities-integration) to provide visibility into user activities.
  - The Docusign connector is available from the **Integrations Catalog**, under **App Activities**
  - CASB license required
- **Near Real-Time XOps Stories for SentinelOne and CrowdStrike:** To improve response times for critical threats from EDR alerts, [SentinelOne](/v1/docs/sentinelone-edr-configuring-the-xops-integration) and [CrowdStrike](/v1/docs/crowdstrike-configuring-the-xops-integration) XOps stories are now created shortly after the original alert is generated.
  - Supported for MDR customers or customers with an XOps license
- **Intune Compliance for Device Posture:** Create [Device Posture checks](/v1/docs/creating-device-posture-profiles-and-device-checks) based on compliance statuses reported by [Microsoft Intune](/v1/docs/configuring-intune-mdm-compliance-checks-for-device-posture) via a Cato connector. This lets you enforce access policies based on your organization's MDM compliance posture.
  - Use Intune-reported compliance signals as posture checks in Access policies
  - Applies to all devices, no additional license required
- **End of Support for Cato Socket X1500A and X1700A Models:** Cato announces that the X1500A and X1700A Socket hardware models will reach End of Support (EOS) on July 1, 2030. This lifecycle milestone is part of Cato’s standard [hardware refresh](/v1/docs/cato-socket-hardware-refresh-policy) process to ensure you continue to benefit from secure, high-performance, and fully supported platforms.
  - EOS announcement date: February 22, 2026
  - EOS date: July 1, 2030
  - For more information, see [this article](/v1/docs/product-lifecycle-notice-end-of-support-for-cato-socket-hardware)

## PoP Announcements

- New ranges are now available for these PoP locations:
  - **Atlanta, US:** 199.27.48.0/24
  - **Osaka, JP:** 113.30.131.0/24
- **Upcoming New Localized IP Range for Kazakhstan:** The following localized IP range for Kazakhstan (serviced through the Helsinki PoP location) will soon be available:
  - **KZ:** 159.117.235.0/27

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
