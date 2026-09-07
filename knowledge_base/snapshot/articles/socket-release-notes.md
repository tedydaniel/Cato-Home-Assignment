---
title: "Socket Version 27.0 Release Notes"
slug: "socket-version-27-0-release-notes"
updated: 2026-08-31T06:01:35Z
published: 2026-08-31T06:01:35Z
canonical: "knowledge.catonetworks.com/socket-version-27-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 27.0 Release Notes

## New Features & Updates

Socket version 27.x includes the firmware for new features, and in the coming weeks, we will update the Cato Cloud and release the following features:

- **Multiple DHCP Ranges for Site VLANs**: Configure multiple DHCP ranges on any site VLAN to support more flexible IP allocation across segmented networks.
  - Previously supported only for native ranges

- **Device Labels and Groups for Policies and Visibility:** Classify devices with labels and use them in groups to simplify traffic visibility and apply policies consistently across LAN, WAN, and Internet firewall rules. This helps admins manage device-based access at scale.

- **Azure vSocket Support for v6 and Newer Instances**: Deploy Azure vSockets on certified v6 and newer Azure instances to increase throughput and support regions where v5 instances are unavailable, such as East US.

- **Enhanced X1600 Wi-Fi Capabilities:** Manage X1600 Wi-Fi deployments with expanded configuration and monitoring capabilities, including network analytics over time, advanced radio settings, and Socket LED indications.

- **Flexible High-Capacity Add-On Connectivity for X1700C Sockets**: Install different add-on module types on the same X1700C Socket, including the new 2x25G and 2x100G modules, to support higher-throughput site designs.

- **Large-Scale WAN Recovery with X1700C Socket Hubs:** We added support for up to 24,000 Off-Cloud tunnels on an X1700C Socket hub, helping large hub-and-spoke deployments maintain critical site connectivity in the rare case of a Cato Cloud availability event.

- **BGP Configuration Updates Without Session Reset**: Apply supported BGP routing changes, including summary route and advertisement settings, while keeping the BGP session established. This helps reduce traffic disruption during configuration updates.

- **Socket Static WAN Configuration Visibility:** The Sockets & Accessories page shows which Sockets use static WAN settings, helping admins review site connectivity configuration and plan network changes with more confidence.

- **Expanded Socket and Hardware Metric Visibility:** Gain deeper insight into Socket performance in the Network Analytics and Experience Monitoring pages with new hardware, port, and flow metrics.
  - New data includes memory usage, flow counts and rates, per-port packet rates, and Socket uptime

- **TCP-Based Socket Traceroute in Experience Monitoring:** The Path Analysis section in Socket site drill-down pages shows periodic traceroute (MTR) results for paths in and out of the tunnel. This helps admins investigate connectivity issues between the Socket, PoP and applications.
  - Requires configuration of TCP probes
  - DEM license required

- **Dynamic Link Aggregation for Sockets:** Use Link Aggregation Control Protocol (LACP) to dynamically establish LAG connections between Socket LAN ports and neighboring switches, helping improve link resiliency and aggregate capacity for site connectivity.

- **vSocket Deployment on KVM:** Customers can deploy vSockets in KVM-based virtualization environments, providing greater flexibility for virtual site connectivity beyond VMware-based deployments.
- In addition, this version includes:
  - Stability improvements
  - Security updates
  - Bug fixes

## SSH and SSL Versions for Socket v27

- OpenSSH Version: 10.2p1
- OpenSSL Version: 3.5.5

## Summary of Minor Versions

- v27.0.23945 - resolved issues 204056, 204759
- v27.0.24031 - resolved issues 194730, 205977, 207354

## Resolved Issues

| ID | Description | Severity | Issue Found In | Issue Resolved In |
| --- | --- | --- | --- | --- |
| 136448 | The X1500B Socket incorrectly advertised 10 Mb/s half duplex on the WAN interface when the link was configured for 1 Gbps. | High | v23.19600 | v27.0 |
| 161015 | An AWS vSocket could crash when running high-bandwidth throughput tests (iPerf). | Critical | v24.0.21499 | v27.0 |
| 162234 | On AWS vSocket HA sites, an upgrade or failover could cause routing problems that disrupted access to AWS network segments. | Critical | v24.0.20874 | v27.0 |
| 177654 | On X1500 Sockets, users were unable to change the WAN1 configuration from PPPoE to DHCP via the Socket WebUI. | High | v24.0.21705 | v27.0 |
| 182509 | The Socket WebUI was unable to resolve and ping certain Cato hostnames (e.g., steering.catonetworks.com). | Medium | v25.0.22236 | v27.0 |
| 194730 | In some cases, WAN interface updates on a Socket could be delayed, causing the Socket to use outdated WAN settings after a connectivity loss. This could require admins to manually restore the WAN configuration. | Critical | v26.0.22806 | v27.0.24031 |
| 204056 | On Socket v26, LTE connectivity was unavailable after a cellular modem reboot, until the Socket was restarted. | Critical | v26.0.23517 | v27.0.23945 |
| 204759 | Application-based and FQDN-based Bypass rules were not applied as expected for certain traffic (e.g., Netflix, Roku), causing flows to be routed to the Cato PoP instead of bypassing it directly. | Critical | v27.0 | v27.0.23945 |
| 205977 | Socket diagnostic files were not generated for some Socket errors, even when diagnostics collection was enabled. This could make troubleshooting harder for Cato Support. | High | v.v26.0.23517 | v27.0.24031 |
| 207354 | Frequent LAN Firewall updates interfered with the Socket's configuration stabilization process, preventing the Socket from saving a confirmed stable configuration. This could cause frequent writes to the Socket's flash storage, potentially accelerating hardware wear. | Medium | v.26.0 | v27.0.24031 |
