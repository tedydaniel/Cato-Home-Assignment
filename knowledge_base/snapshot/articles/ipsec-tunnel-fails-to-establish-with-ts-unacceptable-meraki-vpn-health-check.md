---
title: "IPsec Tunnel Fails to Establish with TS_UNACCEPTABLE When Meraki VPN Health Check Is Enabled"
slug: "ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check"
updated: 2026-08-10T10:58:33Z
published: 2026-08-10T10:58:33Z
canonical: "knowledge.catonetworks.com/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IPsec Tunnel Fails to Establish with TS_UNACCEPTABLE When Meraki VPN Health Check Is Enabled

## Issue

When connecting a Cisco Meraki MX appliance to Cato using a route-based (0.0.0.0/0) IPsec VPN configuration, the tunnel may fail to establish when Meraki's VPN **health check feature** is enabled.

With VPN health check active, the Meraki MX injects multiple traffic selector, including the health check probe 192.0.2.3 which Cato rejects with TS_UNACCEPTABLE. Cato expects a single Traffic Selector pair of 0.0.0.0/0 ↔ 0.0.0.0/0 for route-based tunnels and rejects the SA with a TS_UNACCEPTABLE notification when it receives multiple Traffic Selectors. As a result, the tunnel fails to come up.

## Environment

- Cisco Meraki MX with VPN health check enabled
- IKEv2

## Troubleshooting

- In the Meraki Dashboard, validate if VPN health check is enabled.
- In the CMA, navigate to the IPsec site and check the Timeline. Look for tunnel events showing TS_UNACCEPTABLE as the disconnect reason.
- If enabled, temporarily disable VPN health check and check if the IPsec tunnel establishes successfully. If it does, this confirms the issue.

## Solution

There are two options:

1. **Switch to policy-based IPsec**: Reconfigure the IPsec tunnel on both the Cato side and the Meraki MX to use policy-based VPN instead of route-based. With policy-based configuration, specific network ranges are defined as Traffic Selectors on both sides, and the health-check probe IP no longer causes a mismatch. This is the recommended self-service workaround.
2. **Contact Cato Support**: If switching to policy-based is not feasible, contact Cato Support. Support can apply a backend configuration specifically for this limitation.
