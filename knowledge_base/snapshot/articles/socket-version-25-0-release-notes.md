---
title: "Socket Version 25.0 Release Notes"
slug: "socket-version-25-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-25-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 25.0 Release Notes

## New Features & Updates

Socket version 25.x includes the firmware for new features, and in the coming weeks, we will update the Cato Cloud and release the following features:

- **SLA-Based Link Selection for Active/Active Socket Links:** You can now define granular SLA thresholds for each Socket link in Active/Active (A/A) configurations to improve link selection and flow quality. Previously, Connection SLA logic was limited to Active/Passive links.
- **Account-Level Socket Bypass Policy for FQDN-Based Applications:** Define account-wide rules to bypass trusted Internet traffic directly from Socket sites, including FQDNs and domains. Define account-wide rules to bypass trusted Internet traffic directly from Socket sites, including FQDNs and domains.
  - Supports FQDNs, domains, IPs, and custom apps as bypass destinations
  - Single, unified policy across sites with full API and event support (previously, Bypass Policy was only available per site)
  - Ideal for Windows Update, cloud backups, guest Wi-Fi, and similar use cases
- **Faster HA Failover for BGP-Connected Socket Sites:** We've enhanced the resilience and responsiveness of Socket HA failover in BGP scenarios to minimize downtime during active traffic.
  - Reduces failover time with optimized BGP timers and BFD support
  - Improves reliability when the primary Socket goes down mid-session
  - Helps maintain session continuity and SLA targets for BGP-routed sites
- **Category for DEM Socket Probes in Network and Security Policies:** For simplified and consistent policy enforcement across all relevant DEM probe types, we added the category **DEM Socket Synthetic Probes**. This category can be configured in Network and Security policies to control probe traffic.
- **Configure Custom Thresholds for Default DEM Probes:** To better fit your requirements, we’re adding the ability to configure thresholds for the following predefined default probes:
  - LAN Gateway
  - Underlay Reachability
  - Underlay Traceroute
- **New X1600 Socket with Built-In 5G:** We added a new Socket model X1600 5G with integrated 5G connectivity to provide sites with faster cellular connectivity and improved resiliency.
  - Use 5G as a primary or backup WAN link
  - Boost performance with higher speed and lower latency
  - Accelerate site deployments without waiting for wired links
  - Manage and monitor 5G links directly from the CMA
- **Socket Next Gen LAN FW Now Enforces DNS over TCP:** The Socket Next Gen LAN Firewall can now identify and enforce DNS traffic over TCP, enhancing visibility and control for DNS flows in firewall policies.
- In addition, this version includes:
  - Stability improvements
  - Security updates
  - Bug fixes

## SSH and SSL Versions for Socket v25

- OpenSSH Version: 10.2p1
- OpenSSL Version: 3.5.4
  - From Socket v25.0.21964: 3.5.5

## Summary of Minor Versions

- v25.0.21964 - includes upgrade to OpenSSL version 3.5.5
- v25.0.22040 - resolved issue 167472
- v25.0.22177 - resolved issues 163551, 168400, 168942, 170114
- v25.0.22236 - internal enhancements
- v25.0.22707 - resolved issues 171359, 174695, 174953, 175114, 176343 and includes the firmware for this new feature:
  - **Automatic SIM Failover for Cellular Sockets:** Enable automatic SIM failover for X1600 LTE and X1600 5G Sockets to improve cellular resilience and maintain connectivity during network issues.

## Known Limitations

| ID | Description | Severity | Issue Found In |
| --- | --- | --- | --- |
| 172721 | For Sockets with BGP peers configured, routes advertised by the peer that has the Socket LAN IP as the next hop causes BGP sessions to disconnect | Critical | v25.0.22177 |

## Resolved Issues

| ID | Description | Severity | Issue Found In | Issue Resolved In |
| --- | --- | --- | --- | --- |
| 47698 | Fixed an OS command injection vulnerability in the Socket WebUI. | Critical | v24.0 | v25.0 |
| 124361 | Fixed an issue where PCAP downloads initiated from the Socket WebUI via CMA failed with HTTP 400 errors, while local access worked correctly. | Critical | v23.0 | v25.0 |
| 131494 | Fixed an issue where BFD reply packets were sourced from an incorrect link-local address instead of the Socket LAN IP, preventing BFD neighbors from establishing sessions. | High | v23.0 | v25.0 |
| 140807 | Fixed an issue on X1500B Sockets where a health check could abort a worker thread during outlet weight updates. | High | v24.0 | v25.0 |
| 142513 | Fixed a TCP stack consistency issue that could trigger internal boundary-check violations under certain traffic conditions. | High | v24.0 | v25.0 |
| 142828 | Fixed an issue where X1600 LTE Sockets experienced repeated service interruptions during upgrades between versions 23.0.19481 and 24.0.19856, impacting LTE connectivity and configuration persistence. | Critical | v23.0.19481 | v25.0 |
| 147975 | Fixed an issue where DNS resolution failures during DEM probe execution caused incorrect Last-Mile ICMP packet-loss reporting. | High | v24.0.2002 | v25.0 |
| 148071 | Resolved an issue causing repeated false CMA upgrade or rollback notifications and intermittent version mismatch indications, despite stable socket operation. | High | v24.0 | v25.0 |
| 148647 | Fixed a routing subsystem issue on X1600-LTE sockets that could cause unexpected socket restarts. | High | v23.0.19481 | v25.0 |
| 150945 | Fixed an issue where Network Analytics continued to display outdated Last-Mile probe paths after probe rule changes, resulting in stale ICMP analytics data. | High | v24.0 | v25.0 |
| 151839 | Resolved an issue on X1500B Sockets in Active/Active deployments where the main Socket process could consume excessive CPU under low-traffic conditions. | High | v24.0.19906 | v25.0 |
| 156902 | Potential memory leak issue. | Critical | v24.0 | v25.0 |
| 158017 | Fixed an issue where off-cloud PF connections could open redundant remote-site tunnels without recognizing existing NAT-punched connections, leading to unnecessary connection attempts. | Medium | v24,0 | v25.0 |
| 162210 | A race condition during startup caused DHCP relay mode to activate, preventing devices on the native subnet using Cato as DHCP from obtaining IP addresses until the Socket was rebooted. | Critical | v24.0 | v25.0 |
| 163551 | After upgrade to v24.0, floating IP is not assigned to any Socket, neither primary nor secondary. | Critical | v24.0 | v25.0.22177 |
| 167472 | After upgrading to Socket v25, some sites experienced DNS lookups intermittently failing or timing out. | Critical | v25.0 | v25.0.22040 |
| 168400 | In some scenarios, Socket X1700/X1700B experiences sustained high CPU utilization on a single core. | Critical | v24.0.20874 | v25.0.22177 |
| 168942 | For X1600 5G Socket, cellular modem won't initiate a connection when using a T-Mobile SIM card. | High | v25.0 | v25.0.22177 |
| 170114 | After upgrading Sockets to v25.0, some traffic stopped working reliably, which caused voice calls to fail and also led to Wi-Fi authentication failures at affected sites. | Critical | v25.0 | v25.0.22177 |
| 171359 | After a Socket upgrade, some BGP routes were not advertised due to an issue where dynamically learned routes were incorrectly removed during initialization. As a result, routes remained missing until the tunnel or Socket was restarted. | Critical | v25.0 | v25.0.22707 |
| 174695 | After a Socket upgrade, X1600 LTE devices experienced unexpected reconnections due to an issue with the LTE modem interface. | Critical | v25.0 | v25.0.22707 |
| 174953 | When switching SIM slots on an X1600 5G Socket, the operator ID may be cleared, which can prevent cellular connectivity from being established. | Critical | v25.0 | v25.0.22707 |
| 175114 | Fixed an issue where, in some cases after upgrading a Socket from v24 to v25, clients at the site did not receive IP addresses from the DHCP server. | High | v24.0 | v25.0.22707 |
| 176343 | Fixed a Socket stability issue that could cause repeated crashes in rare cases during RTT measurement traffic handling. | High | v25.0 | v25.0.22707 |
