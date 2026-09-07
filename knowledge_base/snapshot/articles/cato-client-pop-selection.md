---
title: "Cato Client PoP Selection"
slug: "cato-client-pop-selection"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/cato-client-pop-selection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Client PoP Selection

## Overview

For remote access, the Cato Client connects users to the Cato Cloud through one of Cato’s PoPs, which are distributed globally to provide secure connectivity and optimized performance. By default, the Client automatically connects to the optimal PoP based on geolocation and connectivity metrics, which indicate the overall connection quality.

This behavior improves the user experience by helping users connect through the most suitable PoP without manual intervention. For special use cases, the Client can be configured to connect only to a specific PoP instead of automatically connecting to the optimal one.

### Why Connecting to the Optimal PoP Matters

The PoP that the Client uses directly impacts the quality and reliability of the user connection to the Cato Cloud. When the Client connects to the optimal PoP, users can benefit from better performance and lower latency.

This behavior is designed to adapt to the user’s current environment. A user’s physical location and Internet path quality can change over time. By evaluating these factors, the Client helps maintain the best connection path to the Cato Cloud.

## Client Connection Modes

The following table summarizes the modes that the Client connects to PoPs in the Cato Cloud.

| Mode | Behavior | Recommended User |
| --- | --- | --- |
| Automatic | The Client automatically connects to the optimal PoP based on current conditions | Most users and environments |
| Specific PoP | The Client always connects only to the defined PoP | Compliance, testing, and other special cases |

## Automatically Connecting to the Optimal PoP

When the user connects, the Client evaluates available PoPs and chooses the one that best matches the user’s location and current connectivity conditions. This process happens transparently in the background. The user does not need to manually review PoP options or test performance.

### What the Client Evaluates

The Client evaluates two main factors when it connects to a PoP:

- Geolocation - The geographic location of the user or device
- Connectivity metrics - Real-time performance measurements such as latency, packet loss, and connection quality

Geolocation helps the Client identify PoPs that are likely to provide efficient network paths and determines localization for web content. Connectivity metrics help the Client determine which of those PoPs currently provides the best actual performance.

By combining these factors, the Client can connect to a PoP based not only on physical proximity, but also on the quality of the available connection.

### Connection Resiliency and Failover

The Client connection logic is designed to support a resilient connection experience. If network conditions change, the automatic connection logic helps the Client use an alternative PoP that provides a better connection.

This behavior helps improve availability and maintain user connectivity to the Cato Cloud. Instead of relying only on the closest PoP, the Client considers real-time network conditions so that users can connect through the PoP that is most suitable at that time.

## Connecting to a Specific PoP

In addition to automatically connecting to the optimal PoP, the Client can be configured to connect only to a specific PoP. This overrides the default behavior and directs the Client to use the configured PoP instead of automatic PoP selection.

### When Connecting to a Specific PoP Is Useful

For most environments, automatically connecting to the optimal PoP is the recommended option. However, connecting only to a specific PoP can be useful for some business and technical requirements, such as:

- Regulatory or compliance requirements
- Testing and troubleshooting

In addition, you can define Network Rules to [egress traffic from a specific PoP location](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic).

### Considerations for Connecting to a Specific PoP

When the Client is configured to connect only to a specific PoP, it does not use the default logic to connect to the best-performing PoP for the current network conditions. For example, when a PoP is down during the maintenance window, the Client disconnects from the network and doesn't try to connect to a different PoP.

## Related Articles

- [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client)
- Connecting to a specific PoP, see:
  - [Getting Started with the Windows Client](/v1/docs/getting-started-with-the-windows-client)
  - [Getting Started with the macOS Client](/v1/docs/getting-started-with-the-macos-client)
