---
title: "Configuring DHCP Settings"
slug: "configuring-dhcp-settings"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/configuring-dhcp-settings"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring DHCP Settings

This article discusses how to use the Cato Cloud as the DHCP server for network ranges and how to configure DHCP options for the entire account and groups.

## Overview of DHCP in Cato Networks

After you define the DHCP ranges in the Cato Management Application, the Cato's DHCP server in the Cato Cloud assigns IP addresses to clients. You can also choose to use Cato as the DHCP relay agent for a local DHCP server in your organization.

You can configure the following DHCP settings for the network segments in a site: DHCP range, DHCP lease time, DHCP relay, and disabling DHCP. For example, to configure a specific DHCP range that is only used for a Guest WiFi VLAN in the corporate HQ. You can also define a default DHCP setting for the entire account and then apply it to the network ranges.

## Configuring the Cato Cloud as the DHCP Server

When you configure a network range to use the Cato Cloud as the DHCP server for your account, each PoP assigns IP addresses and network parameters to the clients and hosts that use it to connect to the Cato Cloud.

The hosts behind the site, receive their IP addresses from the DHCP IP range for the network segment in that site. Make sure that the Gateway IP address isn’t included in the DHCP range.

For hosts that require a static IP address, such as a network printer, you can assign the static IP address in two ways:

1. Manually configure the static IP address on the host. Make sure that the configured IP address isn't within the DHCP range for the network segment.
2. Use the Cato DHCP server to allocate a static IP address for the host. With this option, the Cato DHCP server reserves the IP address for the hosts and allocates this IP address with an infinite DHCP lease time. Make sure that this IP address is within the DHCP IP address range for that network segment.

For more about configuring a static IP and DHCP reservation for a host, see [Defining Hosts for a Site](/v1/docs/defining-hosts-for-a-site).

You can define one of the following DHCP server settings for each Native Range and VLAN Range within a site:

- Account Default - the network uses the settings for the account that are configured in the **DHCP Relay** section. If this section isn't configured, then Cato does NOT provide DHCP services for this network range.
- DHCP Range - enter an IP range that is assigned by the Cato DHCP server. Use this option when you want to use Cato as the DHCP server.
- DHCP Relay - select the DHCP relay group that you previously defined.

The DHCP Relay option is only available for Cato Sockets, and ESX vSockets.

For more about DHCP relays and Cato, see [Configuring Cato as the DHCP Relay](/v1/docs/configuring-cato-as-the-dhcp-relay).

### Configuring the DHCP Range for a Network Segment

For each network range, define the DHCP IP address range for the network segments in that site in one of the following formats:

- Range of IP addresses - 192.0.2.10-192.0.2.20
- Subnet (CIDR) - 192.0.2.0/24

For a Native Range, you can configure multiple DHCP ranges. Up to 20 total DHCP ranges are supported for a Native Range.

You can customize the DHCP lease time for a network segment. For more information about DHCP lease time, see below: [Configuring the DHCP Lease Time For the Account](/v1/docs/configuring-dhcp-settings#configuring-the-dhcp-lease-time-for-the-account).

**To define the DHCP range for a network segment:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. In the **DHCP Settings** column, click the network range.

The **Edit IP Range** panel opens.

![DHCP_Lease_Network_Range.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247972757917.png)
4. Configure the DHCP range for the network range:
  1. From the **DHCP Range Type** drop-down menu, select **DHCP Range**.
  2. Enter the **DHCP Range** of IP addresses that the Cato DHCP server can assign.

You can either use CIDR or the first and last IP address of the range with a dash. For example, 10.11.1.0/28 or 10.11.1.5-10.11.1.10
5. **(Optional)** For Native Ranges, under **Additional DHCP Ranges**, click the plus icon to configure multiple DHCP ranges.
6. **(Optional)** Customize the DHCP lease time for this network range:
  1. In the **DHCP Lease Time** section, select **Override Account Settings**.
  2. Configure the custom **Lease Time**.
7. Click **Apply**. The **Edit IP Range** panel closes.
8. Click **Save**. The changes to the network range are saved.

### Configuring the DHCP Lease Time For the Account

By default, Cato DHCP Server allocates IP addresses to DHCP clients with a lease time of 72 hours. You can overwrite the default lease time for IP allocations for the entire account (and also for specific site network ranges). The DHCP lease time for a network range takes priority over the lease time for the account.

![DHCP_Lease_Account.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247997213213.png)

**To configure the DHCP lease time for the account:**

1. From the navigation menu, click **Network > DHCP**.
2. Select or expand the **DHCP Lease** tab or section.
3. Set the **DHCP Lease Time** that the allocated IP addresses are valid for.
4. Click **Save**.

#### Cato DHCP Lease Timers

The following table shows details about lease times for the Cato DHCP server.

| Description | Time Value |
| --- | --- |
| The default DHCP lease time. After the lease expires, the IP address returns to the pool, regardless of the host activity. There's no grace period after the lease expires. Halfway through the lease time, the client may extend its lease which will reset the lease expiration timer. | 72 hours |
| Amount of time that a static IP address reported via DHCPINFORM is reserved. | 48 hours + 6 hour grace time |
| For cases where the host is inactive and the IP address was not originally allocated by the Cato DHCP server. The IP address remains reserved as long as the host is active and it goes back to the pool after 6 hours of inactivity. | 6 hours |
| Amount of time that an offered IP address is reserved. | 30 seconds |

## Configuring DHCP Options for the Account and Groups

DHCP options lets you define custom DHCP host configuration parameters for your DHCP clients. You can configure DHCP options for groups (highest precedence) or for the entire account (lowest precedence). The options are applied according to [RFC 2132](https://tools.ietf.org/html/rfc2132) and other relevant RFCs.

> [!NOTE]
> Notes:
> 
> - If you use the Cato Cloud as a DHCP relay instead of the DHCP server:
>   - For network ranges with **DHCP Range** option, then the DHCP options configured in the Cato Management Application are applied
>   - For network ranges with **Account Default** option, then the DHCP relay settings are used and the DHCP options configured in the Cato Management Application are ignored
>   - For groups, the DHCP options configured in the Cato Management Application are ignored
> - The DHCP options aren't applied to Cato SDP Clients.

**To configure the DHCP options:**

1. Edit the DHCP options for a specific group, or for the entire account:
  - For groups - From the navigation menu, click **Resources > Groups** and select the group. Then, from the navigation menu, select **DHCP Option**.
  - For the entire account - From the navigation menu, click **Network > DHCP** and then select the **DHCP Options** tab.
2. Click the **New** button.

The **New DHCP Option** panel opens.
3. Enter a **Name**, and the DHCP **Option Number**.
4. Configure the specific settings for the DHCP option:
  1. Select the **Type** of data for the option: **ASCII**, **HEX**, or **IP** address.
  2. Enter the **Data** value.

For multiple **Data** values, you can enter several values separated by commas.
5. Click **Apply**. The **New DHCP Option** panel closes and the option is added to the screen.
6. Click **Save**. The DHCP option is applied to the group or the account.

### Working with Hierarchy for DHCP Options

You can configure the DHCP options on different objects in the Cato Management Application, for example, settings for the entire account and for specific groups. When there is a conflict between these objects, the precedence is for the most specific object:

1. Groups - most specific and highest precedence
2. Account - less specific and lowest precedence

In other words, if there are different DHCP settings for a group and the account, the DHCP settings for the group are used because the group is higher precedence than the account. However, you can't configure DHCP options for sites, so they are not relevant to this hierarchy.

**​​Note:**​​ We recommend that ​you do not configure the same site as a member for multiple groups with different DHCP options. Doing so can create unpredictable behavior for how the DCHP options are applied to the site.
