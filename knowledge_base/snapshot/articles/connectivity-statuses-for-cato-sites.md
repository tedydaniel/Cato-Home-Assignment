---
title: "Connectivity Statuses for Cato Sites"
slug: "connectivity-statuses-for-cato-sites"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/connectivity-statuses-for-cato-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectivity Statuses for Cato Sites

Cato Networks supports the following site types:

- Sockets
- IPsec
- Cloud Interconnect

This article lists the connectivity states for each of these sites and what they mean.

## Socket Site Connectivity Statuses

The following table shows the relevant connectivity statuses for Socket sites and what they mean.

| Status | Description |
| --- | --- |
| Connected | Indicates that the site is connected to the Cato Cloud. |
| Degraded | Indicates that there is an issue with your site. This status is displayed if any of the following issues are detected: - HA is not ready - this is true when - There are incompatible Socket versions between the primary and secondary Sockets - Either of the Sockets are not responding to ICMP keep alive packets - Either of the Sockets is disconnected - Port is disconnected - this is true when: - LAN port is disconnected - Indicates that any of the LAN types are not working properly, including LAN, LAN and VRRP, LAG master, and LAG master *and* VRRP. - One of the LAG members is disconnected - One of the WAN ports, or the ALT WAN port, is disconnected - Tunnel is down - this is true when: - One of the WAN ports is connected but does not have a tunnel You can disable [Degraded status](/v1/docs/configuring-system-settings-for-the-account) for your account from the Administration > System Settings page. |
| Disconnected | Indicates that your site is not connected to the Cato Cloud. |
| Disconnected (Disabled) | Indicates that a site has been MANUALLY disabled. A disabled site cannot connect to the Cato Cloud. However, it still appears in the relevant references and entries in the Cato Management Application, such as security rules. |

## IPsec Site Connectivity Statuses

The following table shows the relevant connectivity statuses for IPsec sites and what they mean.

| Status | Description |
| --- | --- |
| Connected | Indicates that the site is connected to the Cato Cloud. |
| Degraded | Indicates that either the primary or secondary tunnel is down. The site can still connect to the Cato cloud. You can disable [Degraded status](/v1/docs/configuring-system-settings-for-the-account) for your account from the Administration > System Settings page. |
| Disconnected | Indicates that your site is not connected to the Cato Cloud. |
| Disconnected (Disabled) | Indicates that a site has been MANUALLY disabled. A disabled site cannot connect to the Cato Cloud. However, it still appears in the relevant references and entries in the Cato Management Application, such as security rules. |

## Cloud Interconnect Site Connectivity Statuses

The following table shows the relevant connectivity statuses for Cloud Interconnect sites and what they mean. For more information, see the section about Cloud Interconnect site architecture [here](/v1/docs/getting-started-with-cloud-interconnect-sites).

| Status | Description |
| --- | --- |
| Connected | Indicates that the site is connected to the Cato Cloud. A site is considered connected when: - Both the Primary and Secondary BGP peers are established - When either the Primary or Secondary BGP peers is established |
| Degraded | Indicates that either the primary or secondary tunnel is down. The site can still connect to the Cato cloud. You can disable [Degraded status](/v1/docs/configuring-system-settings-for-the-account) for your account from the Administration > System Settings page. |
| Disconnected | Indicates that your site is not connected to the Cato Cloud. This means that both the Primary and Secondary BGP peers are down. |
| Disconnected (Disabled) | Indicates that a site has been MANUALLY disabled. A disabled site cannot connect to the Cato Cloud. However, it still appears in the relevant references and entries in the Cato Management Application, such as security rules. |
