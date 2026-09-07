---
title: "Product Update - September 23, 2024"
slug: "product-update-september-23-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-september-23-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - September 23, 2024

- **Improved Throughput for Azure vSockets:** Cato’s [Azure vSocket](/v1/docs/deploying-azure-vsockets-from-the-marketplace) now supports up to 2 Gbps of network throughput, with the following requirements:
  - Azure accelerated networking enabled
  - Standard_D8ls_v5 instance type
  - Socket v21.0.18517 and higher (requires a [manual upgrade](/v1/docs/manually-upgrading-a-socket))
- **XDR - Improve Your Security Posture and Stay Ahead of Emerging Threats:** XDR Security stories provide the context and details of suspicious traffic to help investigate threats detected by Cato’s real-time security services such as IPS and Anti-Malware. Use the [XDR Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) to analyze the stories and determine if there is a threat that requires mitigation.
  - XDR Core is available at no extra charge for customers with a Threat Prevention license
  - See our new XDR guides:
    - [Getting Started with Cato XDR](/v1/docs/welcome-to-the-cato-xops-service)
    - [Best Practices for XDR Core](/v1/docs/getting-started-with-xops)
  - The XDR platform’s complete set of detection capabilities - including zero-day detection and [UEBA stories](/v1/docs/analyzing-xops-ueba-stories-for-usage-and-events-anomalies) - are available with an XDR Pro or MXDR license
- **iOS Client v5.4:** iOS Client version 5.4 is available to download for testing [here](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3Db089421e67%26e%3Da04538e456&amp;data=05%7C02%7Cyaron.libman%40catonetworks.com%7C463ed205b30548008ec808dcdb1d4478%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638626165953644946%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&amp;sdata=5bYj%2F%2B9UHPmQweB%2FcSgVU69REXIzYQBOxOf038%2FdT2Q%3D&amp;reserved=0) and will be gradually rolled out in the App Store from the week of September 30. The version contains:
  - **IPv6 Support for Last Mile Connections:** Users can connect remotely over ISPs that provide last mile [IPv6-only](/v1/docs/cato-client-last-mile-support-for-ipv6) connections. Both IPv6 and IPv4 connections are now supported.
  - **User Notifications for CASB and DLP:** The device displays a notification to the user when their activity is blocked by [App Control](/v1/docs/managing-the-application-control-policy) or [Data Control](/v1/docs/creating-the-data-control-policy) rules. This educates the user about which app was blocked and why.
  - Bug fixes and stability improvements
- **New EPP Agent v1.1.7:** From September 22, 2024, we are starting to roll out Endpoint Protection (EPP) Agent version 1.1.7 which includes this enhancement:
  - We improved the validations the Agent runs when upgrading to a newer version
- **New Access Best Practices:** To provide recommendations for optimal performance and security for remote users, we added two new Access [Best Practices](/v1/docs/reviewing-posture-checks-for-your-account):
  - [Internet Recovery](/v1/docs/protecting-users-with-always-on-security) is enabled for all Always-on users
  - All Signing Certificates are Valid
- **Always-On Policy Enhancement**: [Internet Recovery](/v1/docs/protecting-users-with-always-on-security) mode allows remote users to access the Internet directly in rare cases where a connection to the Cato Cloud is temporarily unavailable. This is now enabled by default for new rules. While in Recovery Mode, the Client continuously attempts to re-establish its connection to the Cato Cloud until successful.
- **Enriched Event Fields Supported for API and Integrations:** Over the next few weeks we're gradually rolling out the ability to use the API to export all the new fields we added to enrich Security events with full context. These fields were recently introduced, and could previously only be viewed in the Events page.
  - New fields include: network_rule, congestion_algorithm, tcp_acceleration, tls_inspection, public_ip, egress_site_name, egress_pop_name, qos_priority
  - This API enhancement is backwards compatible since the fields are included in existing event sub-types
  - Read more in the [Cato API Reference](https://api.catonetworks.com/documentation/#definition-EventFieldName) portal
- **New Dublin PoP Site for Cloud Interconnect:** We added a new [PoP for Cloud Interconnect](/v1/docs/cloud-interconnect-availability) in Dublin, Ireland, expanding connectivity and access in the region.
- **CMA Enhancement - Improved User Experience for DLP Configuration:** We redesigned the [DLP Configuration page](/v1/docs/creating-dlp-content-profiles) for more intuitive and user-friendly navigation to the different profile configurations and settings.
  - There is no impact on existing DLP profiles

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
