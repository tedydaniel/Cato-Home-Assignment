---
title: "Product Update - Sept. 18th, 2023"
slug: "product-update-sept-18th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-sept-18th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Sept. 18th, 2023

## New Features & Enhancements

- **Authenticate SDP Users Automatically with Windows Credentials:** Over the next few weeks**,** SDP users can authenticate to the Client [with their Windows credentials](/v1/docs/authenticate-users-automatically-with-windows-credentials) for an improved user experience. You can configure the Client to add a user, launch, authenticate, and connect without any user action.
  - Available from Windows Client version 5.8 and higher
  - Supported with Azure SSO on devices that are:
    - Running Windows 10 or higher
    - Azure AD joined
- **Disable Always-On in Designated Trusted Networks:** Over the next few weeks**,** to provide access to an office network that is protected by a third-party solution, admins can define conditions that classify it as a [Trusted Network](/v1/docs/working-with-managed-networks)**.** Once the Client identifies a Trusted Network**,** Always-On is disabled. This optimizes network performance for users connecting to the Trusted Network.
  - Available from Windows Client version 5.8 and higher
  - You can classify a Trusted Network based on:
    - HTTPS resource request
    - DNS query
    - Ping to IP address or a URL
- **Socket WebUI Now Shows Socket CPU Usage:** We added the new **Socket HW Status** tab to the Socket WebUI that lets you monitor the real-time Socket CPU usage. This can help with different troubleshooting scenarios, for example - if a site has performance issues, you can ensure that the Socket CPU isn’t the source of the problem.
  - Requires Socket v19.0
- **Upcoming Deprecation to Health Field in timeseriesMetricType:** On December 17th, 2023, we will deprecate the **health** field of the [TimeseriesMetricType](https://api.catonetworks.com/documentation/#definition-TimeseriesMetricType) used in the [accountMetrics](https://api.catonetworks.com/documentation/#query-accountMetrics) API. After this date, the **health** field in the accountMetrics API will not be available.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
