---
title: "Configuring BGP Neighbors for a Cato Socket"
slug: "configuring-bgp-neighbors-for-a-cato-socket"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/configuring-bgp-neighbors-for-a-cato-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring BGP Neighbors for a Cato Socket

## Overview

> [!NOTE]
> Note:
> 
> Sites that use a Cato Socket can support multiple BGP neighbors

When you configure a BGP neighbor for a Socket, define the IP address of the BGP neighbor to establish a BGP session. Remember to make sure that this IP address is reachable for this Socket. For example, if you are defining a BGP neighbor that is located in a VLAN range, then the BGP server for the Socket is within the gateway address of that range.

BGP filtering can be used to gradually migrate your environment to Cato by limiting the routes that you are accepting. In addition, you can use BGP filtering to block routes that are known to be used by malicious actors.

For more information, see [Working with BGP Filtering](/v1/docs/working-with-bgp-filtering).

### Advanced BGP Settings

The **Additional** section for a BGP neighbor contains these advanced BGP settings:

- Metric
- Hold Time
- Keep-alive Interval

The Metric defines the priority for this BGP route. The lower this value, the higher the priority given to the metric (for example, 10 is a higher priority than 100). The default Metric is 100.

The Hold Time is the number of seconds that the site waits until it defines that the BGP neighbor is down. For example, if the Hold Time is 90, then if the site does not receive a BGP message for 90 seconds, it stops sending traffic to that neighbor and disconnects. After disconnecting from the BGP neighbor, the site attempts to re-connect to it.

- The default setting for a Cato site is 60.
- A Hold Time value of 1 or 2 isn't valid.
- If the neighbors have different Hold Time values, then the smallest value is used for the pair. Both neighbors always use the same Hold Time value.
- If the Hold Time value for both neighbors is 0, then the site never disconnects.

The keep-alive Interval is the number of seconds that the site sends keep-alive messages to the BGP neighbor to keep the session alive. We recommend that the value of the keep-alive Interval is 1/3 the Hold Time value.

- The default keep-alive Interval for a Cato site is 20.
- When the BGP neighbor has a smaller Hold Time value, both members use that value. If the keep-alive Interval value is smaller than the Hold Time value for the BGP neighbor, then a new keep-alive Interval that is 1/3 the Hold Time value for the BGP neighbor is used.

For example, Cato site A has a Hold Time of 120 and a keep-alive interval of 40, and neighbor B has a Hold Time of 30. Then both neighbors use the Hold Time value of 30, and site A has a new keep-alive interval of 10.

## Defining a BGP Neighbor

Define and configure the BGP neighbor pair for sites that use a Socket.

For each peer, we recommend configuring BGP neighbor status change notifications. Notifications are sent upon a BGP peer connection state change to a subscription group, email list, or third-party integration. This is the frequency at which the notifications are sent:

- **Immediate** - Notification sent to recipients for every occurrence
- **Hourly** - Send notification with the first occurrence. Do not send additional emails if there are more occurrences within an hour.
- **Daily** - Send notification with the first occurrence. Do not send additional ones if there are more occurrences within a day.
- **Weekly** - Send notification with the first occurrence. Do not send additional ones if there are more occurrences within a week.

![bgp_neighbor_policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31125563813149.png)

**To define a BGP neighbor for an AWS vSocket in an HA deployment:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Settings > BGP**.
3. Click **New**. The **Add BGP Neighbor** panel opens.
4. In the **General** section, enter the **Name** for this rule that defines the BGP neighbor.
5. In the **ASN Settings** section, configure the BGP **Peer** ASN and **Cato's** ASN.

For more about changing the default ASN for Cato (see [Using BGP in the Cato Cloud](/v1/docs/using-bgp-in-the-cato-cloud)).
6. In the **IPs** section, enter the BGP **Peer** IP address.
7. In the **Policy** section, define the BGP routing behavior for your network:
  1. The **Advertise** options let you configure how the site advertises the BGP routes for this neighbor.

**Note:** For Socket sites, if you do not select any of these options, meaning you are not advertising any routes, make sure you also create a matching configuration on the BGP peer to NOT accept any route advertisements.
    - **Default route** - The site advertises a default route (0/0) to BGP neighbors. The neighbors can send all traffic to this default route, even if it is not in the routing table. Select this option for deployments that use the Cato Socket as the Internet Gateway for that router.
    - **All routes** - The site advertises the internal routing table for the entire account to the BGP neighbor. These routes include static and floating ranges, in addition to routes that are learned from other peers in this site and across your network. This option is often enabled to send the WAN traffic to the BGP neighbor.

**Note:** The entire range of SDP users is advertised to the BGP peer as a single route.
    - **Summary routes** - The site advertising a summary route instead of multiple unique routes, BGP peers can simplify their forwarding decisions and minimize the computational resources required for route lookup. See, [Working with BGP Summary Routes](/v1/docs/working-with-bgp-summary-routes).
  2. In the **Accept** section, select whether the site accepts or drops the dynamic IP addresses that are published by this neighbor. When you select a Drop option, you are limiting the dynamic propagation from this BGP neighbor. For more information about lists of BGP routes, see [Working with BGP Filtering](/v1/docs/working-with-bgp-filtering).

For example, in deployments that use AWS Direct Connect, BGP is required but you do not want to accept the AWS dynamic addresses. In these deployments, we recommend that you select **Drop All**.
  3. In the **NAT** section, select **Perform Hide SNAT** for the site to perform SNAT to all IPs and the traffic is translated to the LAN IP address.
8. To authenticate BGP MD5 using a pre-shared secret, in the **Additional**: section, select **MD5 Auth**.

**Note:** BGP MD5 authentication is supported according to RFC 2385.
9. In the **Additional** section, you can configure advanced settings for the BGP neighbor:
  1. To change the **Metric** for this route, enter the new priority.

The lower this value, the higher the priority given to the metric (for example, 10 is a higher priority than 100).
  2. To change how long the BGP session is kept open, enter the new **Hold time** (in seconds).
  3. To change the frequency of the **Keepalive interval**, enter the new value (in seconds) between keep-alive messages.
10. To receive notifications based on changes to the status of the BGP neighbor:
  1. Select **Send Notification**.
  2. In **Send notification to**, select the **Subscription Group** , **Mailing List** or **Integration** and select the relevant item.
11. Click **Apply**. The new rule is added to the rulebase.
12. Repeat these steps to configure additional rules for BGP neighbors.
13. Click **Save**. The BGP neighbor is configured for the Socket.

## Showing the Status of the BGP Neighbor

After you configure the BGP neighbor for the connection, we recommend that you use the Show BGP Status feature to test the status of the neighbor and make sure that this dynamic route is working.

> [!NOTE]
> Note:
> 
> You can only show the BGP status after you save the configuration for the BGP neighbor and it is sent to the site.

**To show the status of the BGP neighbor:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Settings > BGP**.
3. Click **Show BGP Status**.

An HTTP query is sent to the relevant PoP. The pop-up window shows the status of each BGP neighbor and data about the current routes.
4. Click **OK** to close the window.
