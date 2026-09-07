---
title: "Connecting a Socket to a Switch with VLANs (802.1q)"
slug: "connecting-a-socket-to-a-switch-with-vlans-802-1q"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/connecting-a-socket-to-a-switch-with-vlans-802-1q"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting a Socket to a Switch with VLANs (802.1q)

When configuring VLANs on the site level, it means that the Socket sends tagged packets with the VLAN ID (VID) attached to it.

On the switch, the configuration is straightforward - any layer 2 switch that supports VLAN tagging/ 802.1q can work with such a configuration. VLAN support does not require a layer 3 switch.

When configuring VLANs on the switch, the VLAN IDs (VIDs) must match between the Socket and the switch.

The Native Range of LAN01 can be configured with a specific VLAN ID, in this configuration:

- Traffic in this Native Range is expected to be **tagged with the configured VLAN ID**.
- Traffic arriving **untagged or with a different VLAN ID** will be **dropped** by the Socket.

The Socket can provide a **DHCP range for the Native Range**, which will be tagged with its configured VLAN ID. This can be useful for providing an IP address for the switch management interface on this VLAN.
