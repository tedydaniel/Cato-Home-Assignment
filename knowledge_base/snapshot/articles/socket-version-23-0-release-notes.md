---
title: "Socket Version 23.0 Release Notes"
slug: "socket-version-23-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-23-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 23.0 Release Notes

## New Features & Updates

Socket version 23.x includes the firmware for new features, and in the coming weeks, we will update the Cato Cloud and release the following features:

- **Identical Internet-Only IP Ranges:** To simplify network management and improve security for guest traffic, you can now configure identical IP ranges in multiple sites to be used for Internet-only traffic. These ranges are not propagated to the global routing table, preventing communication with the WAN.
  - We recommend as a guest WiFi best practice for using the Internet-only ranges together with the [Cato captive portal](/v1/docs/configuring-the-cato-captive-portal)
  - Supported for physical Sockets only
- **WAN Recovery Enhancements:** For enhanced resiliency of our [WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery) feature, we introduced the following improvements:
  - **Cached IP Addresses for More Reliable Tunnel Establishment:** We've implemented a Socket caching mechanism that retains the last known IP addresses of remote sockets. This improves the reliability of WAN recovery tunnel establishment.
  - **Enhanced Recovery Event Logging:** Recovery events are now cached within the socket during periods of connectivity loss. Once the tunnel is re-established, these events are sent to the CMA, ensuring admins have a complete and accurate log of recovery events.

## Summary of Minor Versions

- v23.0.19481 - limitation 132324
  - Fixes for minor bugs related to the upgrade process from Socket versions lower than v23.0.
    - These updates are not relevant for Sockets that were already upgraded to v23.0.
- v23.0.19599 - resolution 132169
- v23.0.19786 - resolution 133135
- v.23.0.20122 - resolution 144181

## Known Limitations

Socket version 23.x has the following known limitations:

| **ID** | **Description** | **Severity** | **Issue Found In** |
| --- | --- | --- | --- |
| 132324 | For X1600 LTE Sockets, eSIMs are not supported. It is possible that an eSIM functioned in previous Socket versions because those versions didn’t identify the card as an eSIM. | Critical | v23.0.19481 |
| 136115 | Sometimes when there is low throughput on a link, the Cato Management Application falsely reports packet loss (about 4-5%). PCAPs can correctly confirm that there is no actual packet loss. | Low | v23.0 |

## Resolved Issues

Socket v23.x resolved the following issues:

| **ID** | **Description** | **Severity** | **Issue Found In** | **Issue Resolved In** |
| --- | --- | --- | --- | --- |
| 123666 | After upgrading X1700 Sockets in HA configuration with add-on cards, created a split-brain condition. | Critical | v22.0.19219 | v23.0 |
| 124297 | Changing the WAN interface speed/duplex settings in the Socket WebUI from a manual value to **Auto** led to an issue where the Socket was frozen and required a full reset. | Critical | v22.0 | v23.0 |
| 126869 | For Azure vSocket HA configuration, after upgrading to the new version, vSocket did not receive the floating IP configuration from the Azure API. | Critical | v22.0 | v23.0 |
| 127743 | X1700 Socket site did not reconnect to the optimal PoP after scheduled maintenance. | High | v22.0.19344 | v23.0 |
| 132169 | In some scenarios, after a Socket HA site upgrade, traffic to Azure was disrupted because a floating IP range was unexpectedly assigned to the secondary Socket instead of the primary. | Critical | v.23.0.19445 | v23.0.19599 |
| 133135 | In some scenarios, after the upgrade of an AWS vSocket HA site, the Sockets couldn't connect until one of the Sockets was rebooted. | Critical | v23.0.19445 | v23.0.19786 |
| 144181 | After applying a hub and spoke configuration to the Socket site infrastructure, this could cause degraded network states and Socket disconnects and restarts. | Critical | v23.0 | v.23.0.20122 |
