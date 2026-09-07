---
title: "Socket Version 26.0 Release Notes"
slug: "socket-version-26-0-release-notes"
updated: 2026-08-31T06:00:23Z
published: 2026-08-31T06:00:23Z
canonical: "knowledge.catonetworks.com/socket-version-26-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 26.0 Release Notes

## New Features & Updates

Socket version 26.x includes the firmware for new features, and in the coming weeks, we will update the Cato Cloud and release the following features:

- **20 Gbps Throughput with the X1700C Socket:** We are introducing the new X1700C Socket as an additional hardware model for X1700 Socket sites.
  - The X1700C supports two optional add-ons: dual-100G (2×100G) and dual-25G (2×25G) modules
  - For supported configurations, the platform reaches up to 20 Gbps aggregate throughput
  - Pricing remains the same for all X1700 Socket models
  - Cato will continue to provide support for all X1700 Socket models, subject to the [EOS policy](/v1/docs/product-lifecycle-notice-end-of-support-for-cato-socket-hardware)
- **Updated X1600 Socket Hardware for Wi-Fi Support:** We are introducing integrated Wi-Fi support for the X1600 Socket family. The models X1600 and X1600 5G are available with the option for built-in Wi-Fi 6, eliminating the need for an external access point.
  - Dual-band 2.4/5 GHz, up to 4 SSIDs, and PSK authentication option
  - Full WLAN configuration and analytics in the CMA - SSID settings and visibility for connected hosts, signal quality, and real-time utilization
- **LAN IPS Enforcement on Cato Sockets:** Protect LAN traffic behind your sites by enforcing IPS directly on Sockets. This extends Threat Prevention to LAN traffic, enabling immediate, local enforcement without sending traffic to the Cato Cloud, and helps maintain low latency for internal communications.
  - Enable LAN IPS at the account level and define which sites enforce it
  - Configure per-site enforcement modes:
    - Block to actively prevent malicious traffic
    - Monitor to detect and log threats without blocking
- **Automatic SIM Failover for Cellular Sockets:** Enable automatic SIM failover for X1600 LTE and X1600 5G Sockets to improve cellular resilience and maintain connectivity during network issues.
- **Device-based Criteria for Next Gen LAN Firewall Rules:** Apply the same device-based Criteria conditions available in Internet and WAN Firewall rules to [Next Gen LAN Firewall rules](/v1/docs/managing-the-socket-next-gen-lan-firewall-policy), letting you control routing and connectivity decisions based on device identity, posture, and context.
  - Apply device attributes such as OS, platform, manufacturer, and model
  - Use Device Posture Profiles to route traffic only for compliant devices (for example, encrypted disks or approved Cato Client versions)
  - Differentiate Next Gen LAN Firewall rules based on device location, origin (remote or behind a site), or device category (such as IoT/OT)
- **Updated DTLS Port for China Socket Connectivity:** To improve connectivity and avoid misclassification of DTLS traffic, Cato now supports using UDP port 1337 for DTLS tunnels for Sockets in China.
  - Account-level configuration
  - Available only for Socket sites in China
- **Enhanced vSocket Performance with Support for AWS c7i.2xlarge Instance:** You can now deploy vSockets on AWS using the c7i.2xlarge instance type, providing additional deployment flexibility for larger or more demanding environments.
- **Expanded Support for DHCP Relay Servers:** Configure up to 10 DHCP relay servers per site, providing greater flexibility for environments with more complex network designs that require multiple DHCP servers.
  - Enables greater compatibility for Socket sites using microsegmentation deployments
  - Previously, up to 3 DHCP relay servers were supported
- In addition, this version includes:
  - Stability improvements
  - Security updates
  - Bug fixes

## SSH and SSL Versions for Socket v26

- OpenSSH Version: 10.2p1
- OpenSSL Version: 3.5.5

## Summary of Minor Versions

- v26.0.23517 - resolved issues 174376, 175537, 178865, 186247, 186389, 188017, 193108
- v26.0.24087 - resolved issue 189423, 194730, 200498, 204056, 207354

## Known Limitations

| ID | Description | Severity | Issue Found In |
| --- | --- | --- | --- |
| 199566 | Sockets that use network ranges with public IP addresses and matching Bypass Rules may experience DHCP failures when Cato is used as the DHCP server | Critical | v26.0.23517 |

## Resolved Issues

| ID | Description | Severity | Issue Found In | Issue Resolved In |
| --- | --- | --- | --- | --- |
| 136115 | Sometimes when there is low throughput on a link, the CMA falsely reports packet loss (about 4-5%). PCAPs can correctly confirm that there is no actual packet loss. | High | v23.0.19481 | v26.0 |
| 163595 | Fixed an issue where, in rare cases after a reboot or upgrade, a network interface could fail to initialize correctly, causing the Socket to become unavailable until it was rebooted again. | High | v24.0.20874 | v26.0 |
| 165183 | Fixed an issue where security scanners could flag the Socket web UI password field because it allowed browser autocomplete. | Medium | v24.0.20874 | v26.0 |
| 174376 | In a Hub & Spoke topology, WAN Recovery (Off-Cloud) connections failed to establish for multiple spoke sites, requiring a manual disable and re-enable to reconnect. | High | v24.0.21705 | v26.0.23517 |
| 175537 | The account-level bypass policy did not apply to traffic destined for private IP addresses. | Critical | v25.0 | v26.0.23517 |
| 178865 | Azure vSockets could lose High Availability (HA) connectivity when DNS-based DDoS protection was triggered, causing a split-brain scenario. | Critical | v25.0.22236 | v26.0.23517 |
| 186247 | Excessive Socket log entries were generated for invalid ENC_CIO packets. | Medium | v24.0 | v26.0.23517 |
| 186389 | Experience Monitoring (DEM) probes reported a constant 50% packet loss for remote targets across tunnels. | High | v25.0.22177 | v26.0.23517 |
| 188017 | A Socket upgrade to v26 prevented BGP session establishment due to an invalid next hop attribute. | Critical | v26.0 | v26.0.23517 |
| 189423 | In some cases, Socket traffic could use a lower MTU than expected and not automatically recover to the correct value. This could affect application connectivity until the Socket was restarted or traffic moved to another Socket. | Critical | v25.0 | v26.0.24087 |
| 193108 | Bypassed traffic experienced connection resets after migrating to the account-level bypass policy. | Critical | v25.0.22707 | v26.0.23517 |
| 194730 | In some cases, WAN interface updates on a Socket could be delayed, causing the Socket to use outdated WAN settings after a connectivity loss. This could require admins to manually restore the WAN configuration. | Critical | v26.0.22806 | v26.0.24087 |
| 200498 | In some cases, devices on bypassed networks did not receive DHCP leases after a Socket upgrade. This could prevent those devices from connecting to the Internet. | Critical | v26.0.23517 | v26.0.24087 |
| 204056 | On Socket v26, LTE connectivity was unavailable after a cellular modem reboot, until the Socket was restarted. | Critical | v26.0.23517 | v26.0.24087 |
| 207354 | Frequent LAN Firewall updates interfered with the Socket's configuration stabilization process, preventing the Socket from saving a confirmed stable configuration. This could cause frequent writes to the Socket's flash storage, potentially accelerating hardware wear. | Medium | v.26.0 | v26.0.24087 |
