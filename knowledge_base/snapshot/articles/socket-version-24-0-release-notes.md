---
title: "Socket Version 24.0 Release Notes"
slug: "socket-version-24-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-24-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 24.0 Release Notes

## New Features & Updates

Socket version 24.x includes the firmware for new features, and in the coming weeks, we will update the Cato Cloud and release the following features:

- **WAN Recovery Site-to-Site Tunnels Status in CMA:** To proactively address connectivity issues and ensure WAN Recovery readiness at all times, the Site-to-Site Tunnels feature enables recovery of WAN traffic in case of an unlikely failure, such as a complete Cato Cloud outage. To enhance operational visibility, we have added a new status that indicates whether sites are fully ready, partially ready, or not ready for WAN Recovery. The status is displayed at both the site level and the WAN interface level.
  - Available in the following pages: Topology, Sites, Site Configuration > Socket
  - API Support: Each site and port can be viewed in wanRecoveryStatus in the accountsnapshot API
- **Export Quality SLA Test Results to Easily Open Tickets with ISPs:** Network Stories now supports exporting ICMP and Traceroute results to make it easier to provide the data to your ISP when you open a ticket.
  - ILMM customers are required to upgrade their Sockets to Socket v24 to fully migrate the ILMM service to the CMA
- **DEM Synthetic Probes Adhere to Network and Security Policies:** To provide a more accurate simulation of user-generated traffic, Experience Monitoring probes sent from a Socket now operate in compliance with the configured Network and Security policies.
  - This change may increase the number of events generated for your account
  - Probe traffic can be blocked by policy rules
- **X1700B Socket Supports Higher Port Density for Data Center and Campus Sites:** We added the option to use two add-on port cards, allowing a total of eight 10Gbps fiber ports.
  - Use the Site Configuration > Socket page in the CMA or the **addSocketAddOnCard** API to enable the second card
  - Previously, only a single add-on card was supported
- **Next Gen LAN Firewall Improvements:**
  - Send a notification when traffic matches a LAN Firewall rule
  - New event fields for LAN Firewall events:
    - **Domain Name** - Shows internal LAN apps
    - **HTTP Method** - Specifies the action a client intends to perform on a resource when communicating with a server
  - Identifies the WebDAV app
- **Reminder for Azure vSocket Sites:** Cato identified a new Microsoft validation that impacts Azure vSockets with the **Standard_D2s_v4 VM** size.
  - All impacted customers were sent a dedicated email, you can see the full details [here](/v1/docs/for-microsoft-azure-sites-changing-cato-vsocket-vms-to-standard-d8ls-v5-vm-size).
  - For Azure vSocket sites with the **Standard_D2s_v4 VM** size, it is required to resize the vSocket VM from **Standard_D2s_v4** to **Standard_D8ls_v5**. For more information, see [Resizing VMs for Azure vSockets](/v1/docs/changing-azure-vsockets-to-a-different-vm-size).
  - The vSockets will continue to function normally as long as the VM instance doesn’t power off, so plan your Azure resizing accordingly to prevent future issues.
- In addition, this version includes:
  - Stability improvements
  - Security updates
  - Bug fixes

## SSH and SSL Versions for Socket v24

- OpenSSH Version: 9.9p2
- OpenSSL Version: 3.5.0
  - From Socket v24.0.21914: 3.5.5

## Summary of Minor Versions

- v24.0.19980 - limitation 147300
- v24.0.20639 - bug fixes and internal enhancements
- v24.0.21282 - resolved issues 158066, 151321
- v24.0.21363 - resolved issue 151321
- v24.0.21499 - resolved issue 158765
- v24.0.21570 - includes the firmware for this new feature:
  - **Microsegmentation Support for Third-Party DHCP Servers:** You can now apply DHCP-based microsegmentation to site subnets that use third-party DHCP servers through DHCP relay. This lets you enforce zero-trust east-west controls without changing your existing DHCP infrastructure.
- v24.0.21914 - Includes upgrade to OpenSSL version 3.5.5
- v24.0.22145 - resolved issue 168400

## Known Limitations

| ID | Description | Severity | Issue Found In |
| --- | --- | --- | --- |
| 136115 | Sometimes when there is low throughput on a link, the CMA falsely reports downstream packet loss (about 4-5%). PCAPs can correctly confirm that there is no actual downstream packet loss. **Note:** The limitation for upstream packet loss was resolved in Socket v24.0.20639 | Low | v23.0.19481 |
| 147300 | For X1700B Sockets that have two add-on cards installed, and are running Socket v23.x or lower, upgrading to v24.x can cause ports in the active add-on card to be remapped to the inactive add-on card. This creates a risk of ports going down and no longer passing traffic Make sure that there is only one add-on card in the X1700B Socket before upgrading to Socket v24.x | Critical | v24.0.19980 |

## Resolved Issues

| ID | Description | Severity | Issue Found In | Issue Resolved In |
| --- | --- | --- | --- | --- |
| 100463 | Socket experienced a WAN link flapping issue when there was high RTT. | Critical | v20.0.18453 | v24.0 |
| 127040 | When a Socket site changed PoP location and then was disconnected, it did not reconnect to the optimal PoP. | High | v22.0.19344 | v24.0 |
| 130458 | In a scenario where a router behind a Socket experienced a bug and duplicated packets, the Socket couldn't establish a tunnel from its second WAN interface to the PoP. | Critical | v20.0.18453 | v24.0 |
| 132324 | For X1600 LTE Sockets, eSIMs are not supported. It is possible that an eSIM functioned in previous Socket versions because those versions didn’t identify the card as an eSIM, and then stopped functioning when the version was upgraded. | Critical | v23.0.19481 | v24.0 |
| 136115 | Sometimes when there is low throughput on a link, the CMA falsely reports upstream packet loss (about 4-5%). PCAPs can correctly confirm that there is no actual upstream packet loss. **Note:** There is still a limitation for downstream packet loss | Low | v23.0.19481 | 24.0.20639 |
| 151321 | In some scenarios, a Socket stopped sending the configured PPPoE service name after several connection attempts, which caused connectivity issues with the ISP. | Critical | v24.0.20230 | v24.0.21282 v24.0.21363 |
| 156902 | Potential memory leak issue. | Critical | v24.0 | v24.0.21705 |
| 158066 | Fixed an issue where a missing VFIO configuration reduced vSocket performance on some AWS instances. | High | v20.0 | v24.0.21282 |
| 158765 | Under high flow volumes, a site may experience increased RTT when there is bursty traffic from a single source. | High | v21.0 | v24.0.21499 |
| 168400 | In some scenarios, Socket X1700/X1700B experiences sustained high CPU utilization on a single core. | Critical | v24.0.20874 | v24.0.22145 |
