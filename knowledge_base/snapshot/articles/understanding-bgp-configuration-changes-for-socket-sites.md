---
title: "Understanding BGP Configuration Changes for Socket Sites"
slug: "understanding-bgp-configuration-changes-for-socket-sites"
status: "update"
updated: 2026-09-07T07:54:25Z
published: 2026-09-07T07:54:25Z
canonical: "knowledge.catonetworks.com/understanding-bgp-configuration-changes-for-socket-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding BGP Configuration Changes for Socket Sites

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

## Overview

Cato reduces the impact of many BGP configuration changes for Socket sites by updating BGP routing information without resetting the BGP session. Cato uses BGP soft reset mechanisms when possible to apply supported route policy and advertisement changes without tearing down the BGP session. This helps preserve traffic continuity when you edit supported BGP settings, because the Socket can refresh or update routes while the peer session remains established. For changes that can’t be applied with a soft reset, or when the peer doesn’t support the required BGP capability, Cato performs a hard reset, which disconnects and re-establishes the BGP session.

This article explains how Cato handles different BGP configuration changes for Socket sites, including which changes use soft reset mechanisms and which changes require a hard reset.

## Supported Sites

BGP soft reset behavior is supported for Socket sites.

## Understanding BGP Reset Behavior

When you save BGP configuration changes for a Socket site, the Socket evaluates the type of change and uses the least disruptive supported mechanism for the relevant BGP peer.

The Socket can handle BGP changes in the following ways:

| Mechanism | Description | Typical Impact |
| --- | --- | --- |
| Route Refresh | The Socket requests the BGP peer to resend all routes it advertises to the Socket so the Socket can apply the updated inbound policy. | The BGP session remains established |
| Enhanced Route Refresh | The Socket sends the peer a refreshed outbound routing table using the Enhanced Route Refresh mechanism. This mechanism marks the beginning and end of the route refresh so the peer can identify stale routes and remove routes that are no longer advertised. | The BGP session remains established |
| Specific UPDATE messages | For some outbound changes, the Socket does not need to refresh the full outbound route table. Instead, it sends targeted BGP UPDATE messages to advertise or withdraw only the affected routes. | The BGP session remains established |
| Hard reset | The Socket tears down and re-establishes the BGP session | The BGP session flaps |

### Route Refresh

Route Refresh is used for BGP configuration changes that affect routes the Socket accepts from the peer. For example, when you change BGP filtering or accepted route behavior, the Socket can request the peer to send the relevant routes again.

The Socket then re-evaluates the received routes according to the updated configuration. The BGP session remains established if the peer supports Route Refresh.

### Enhanced Route Refresh

Enhanced Route Refresh is used for more complex outbound route advertisement changes. These changes affect the routing information the Socket advertises to the peer.

With Enhanced Route Refresh, the Socket sends markers that indicate the start and end of the refreshed route table. The peer can mark the previously received routes as stale, process the refreshed route table, and remove routes that are no longer advertised.

The BGP session remains established if the peer supports Enhanced Route Refresh.

### Specific UPDATE Messages

For some outbound changes, the Socket does not need to refresh the full outbound route table. Instead, it sends specific BGP UPDATE or withdraw messages for the affected routes.

This mechanism is used for changes that can be represented as targeted route updates, such as changes to the default route advertisement or metric.

### Hard Resets

Some BGP configuration changes still require a hard reset. A hard reset occurs when the change is not supported by one of the soft reset mechanisms, or when the peer does not support the required BGP capability.

If you save multiple BGP changes together and one of them requires a hard reset, Cato performs a hard reset and does not also perform a soft reset action.

## BGP Reset Behavior by Configuration Change

The following table maps BGP configuration changes to the mechanism Cato uses when the change is saved for a Socket site.

| Configuration Change | Mechanism |
| --- | --- |
| Accept default route from the peer | Route Refresh |
| Accept dynamic routes from the peer | Route Refresh |
| BGP filtering rule for accepted subnets | Route Refresh |
| Enable or disable summary routes | Enhanced Route Refresh |
| Change summary route configuration | Enhanced Route Refresh |
| Perform NAT for BGP-advertised traffic | Enhanced Route Refresh |
| Advertise all routes | Enhanced Route Refresh |
| Advertise default route | Specific UPDATE messages |
| Enable or disable custom BGP ranges | Specific UPDATE messages |
| Change custom BGP range configuration | Specific UPDATE messages |
| Change the BGP metric | Specific UPDATE messages |
| Other BGP configuration change | Hard reset |

## Fallback Behavior for Unsupported Peer Capabilities

Soft reset behavior depends on the capabilities negotiated by the BGP peer during session establishment.

If the peer does not support the capability required for the configuration change, Cato falls back to a hard reset:

| Required Capability | Used For | Fallback Behavior |
| --- | --- | --- |
| Route Refresh | Changes that affect accepted routes | Hard reset if the peer does not support Route Refresh |
| Enhanced Route Refresh | Complex outbound advertisement changes | Hard reset if the peer does not support Enhanced Route Refresh |

Specific UPDATE messages do not require Enhanced Route Refresh capability because the Socket sends targeted BGP updates for the affected routes.

## Multiple Changes Saved Together

When you save multiple BGP configuration changes at the same time, Cato applies precedence logic to determine which mechanism to use.

| Combination of Changes | Result |
| --- | --- |
| Enhanced Route Refresh change and Specific UPDATE change | Only Enhanced Route Refresh is performed |
| Soft reset change and hard reset change | Hard reset is performed |
| Multiple soft reset changes that use the same mechanism | The relevant soft reset mechanism is performed |

## Multiple BGP Peers

For sites with multiple BGP peers, Cato evaluates the change for the relevant peer sessions. A change that affects one peer does not require resetting or refreshing unrelated peer sessions.

If a saved configuration affects multiple peers differently, Cato applies the relevant mechanism for each peer. For example, one peer can require a hard reset while another peer uses a soft reset mechanism.

## Related Articles

- [Configuring BGP Neighbors for a Cato Socket](https://chatgpt.com/v1/docs/configuring-bgp-neighbors-for-a-cato-socket)
- [Using BGP in the Cato Cloud](https://chatgpt.com/v1/docs/using-bgp-in-the-cato-cloud)
- [Working with BGP Filtering](https://chatgpt.com/v1/docs/working-with-bgp-filtering)
- [Working with BGP Summary Routes](https://chatgpt.com/v1/docs/working-with-bgp-summary-routes)
