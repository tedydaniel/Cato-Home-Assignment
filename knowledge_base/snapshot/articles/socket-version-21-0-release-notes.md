---
title: "Socket Version 21.0 Release Notes"
slug: "socket-version-21-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-21-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 21.0 Release Notes

Socket version 21 includes the following features and enhancements:

- **Unified Account Synthetic Probe Policy for Socket Sites and Users:** We are enhancing Cato’s monitoring capabilities with a Synthetic Monitoring policy that lets you configure probes for all sites, per site, and sites by country. In addition, you can configure probes for Cato Client users. This lets you define specific rules for probes and provides a more granular and accurate understanding with Experience Monitoring.
  - **Additional supported probing options:** Send probes using DNS, HTTP/s, and TCP packets in addition to the already supported ICMP packets.
- **Additional Troubleshooting Statuses:**
  - **Internet Connectivity Status per Port:** Added a new status in the Topology page site preview, to easily identify the Internet connectivity status. This enables you to identify issues related to the ISP’s connectivity and distinguish them from tunnel issues.
    - Previously we only supported Physical status and Tunnel status
    - This field is also accessible via accountSnapshot API as internetUp
  - **Socket Physical Uptime:** Added the uptime to reflect the Socket’s physical uptime, to let you identify site down issues that are related to power outages.
    - This field is also accessible via accountSnapshot API as deviceUptime
- **DHCP Enhancements:**
  - **Socket WAN DHCP Improvement:** The Socket's WAN interface does not assign an IP address when it identifies a conflict and requests a new IP address.
    - Previously, the Socket WAN interface would have accepted the IP address even if it would detect that there was a conflict.
  - **Enhanced DHCP Resiliency for Socket Sites:** We improved the DHCP server on the Sockets to apply CMA configurations when allocating IP addresses. For example, if there is a host with a statically allocated IP address, it will be enforced even if the tunnel is down and the Socket serves as the DHCP server for the site.
    - Previously, if the Cato Cloud was unavailable, the Socket was unaware of the host's static IP.
    - The Socket acts as the DHCP server only when there is no connection to the Cato Cloud.
- **Bandwidth Management Improvements:** We made changes to the bandwidth management algorithm to remove tunnel overhead so that only the actual link capacity is taken into account. This improves bandwidth management accuracy, which can be seenin the Real Time page.

In addition, Socket version 21 includes the following:

- Stability improvements
- Security updates
- Bug fixes
