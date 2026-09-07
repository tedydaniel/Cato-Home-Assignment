---
title: "How to Configure a Network Rule to Egress Traffic"
slug: "how-to-configure-a-network-rule-to-egress-traffic"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-configure-a-network-rule-to-egress-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Configure a Network Rule to Egress Traffic

## Overview

Internet resources and business partners may use egress public IPs for access control lists (ACLs) to allow access to Internet hosted resources.

When connected to a PoP, Internet traffic may use any of the PoP's external IP addresses for NAT. A static public IP address is required when a customer needs to egress from a PoP with a specific public IP to be used in an ACL. Define the routing options for a Network Rule to NAT specific traffic with a static public IP address. The IP address is available for your account only and does not change (unless you change it yourself).

## Configuring a Network Rule to Egress Traffic

Use the Network Rules policy to define outbound NAT behavior. A rule that uses the **NAT Routing** method lets you translate traffic to one or more static public IP addresses allocated to your account. These IPs provide stable egress identities for services that require allowlisting.

Before creating the rule, make sure that the required public IP addresses are allocated on the IP Allocation page, and (if needed) that the relevant hosts are defined for the site.

When you configure a Network Rule with multiple allocated IPs, the PoP selects the egress IP address based on availability and routing conditions.

### Allocating IPs for your Account

Select the [Cato-allocated public IP address](/v1/docs/allocating-ip-addresses-for-the-account) you want to translate with NAT in the egress rule. The default license for each account includes 3 unique IPs that can be used by any PoP. If you need additional IP addresses, contact your partner or Sales Engineer.

**To allocate an IP for egressing traffic:**

1. From the navigation menu, click **Network > IP Allocation**.
2. From the drop-down menu, select the PoP location to which you are allocating an IP address. The IP address is automatically added to your account.
3. Click **Save**.

### Egressing Traffic for Static Hosts (Optional)

When you are egressing traffic for a specific number of devices, [configure the static hosts](/v1/docs/defining-hosts-for-a-site) behind the relevant site. Then add the hosts as the **Source** in a Network Rule.

For accounts that use the Cato DHCP server, you need to enter the MAC address for the host to reserve the IP.

**Note:** If you are not using Cato DHCP, make sure the source device has a static IP or a DHCP reservation in the local DHCP server. If the IP address of the device changes, the Network Rule will not use the Cato IP address to egress traffic for the device.

**Translated IP** shows the IP address that the PoP translates for the internal host IP address. When **Static Range Translation** (**Administration > System Settings**) is enabled for the account, you can define the translated IP range in the **Networks** screen.

**To create a static host for egressing traffic:**

1. From the navigation menu, click **Network > Sites > {site name} > Site Configuration > Static Host Reservations.**
2. Click **New**.
3. Enter the **Name** for the device.
4. Enter the **IP address** of the device.
5. If you are using Cato for DHCP, enter the **MAC** address. This creates a DHCP reservation to assign a static IP for this host.

![new_static_host_reservation.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27867156330909.jpeg)
6. Click **Apply**, and then click **Save**.
7. For a new or existing Network Rule, add the static hosts as the **Source**.

### Configuring a Network Rule to Egress Traffic to a Static IP

Create a network rule to define the traffic that you are egressing to the Cato public IP address.

When a Network Rule is configured with multiple egress IPs/Route Via PoPs is configured, the Cato Cloud identifies the PoP to which the egress IP belongs and builds a list of candidate PoPs around it. Then it searches for the nearest PoP and uses it to egress the traffic. If both IPs belong to the same PoP, the first IP in the list is used.

#### **To create a Network Rule that egresses to an allocated IP:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click **New > New Rule**. The **Add Network Rule** panel opens.
3. From the **General** section, configure the following settings for the rule:
  1. Enter the **Name** for the rule.
  2. Enable or disable the rule using the slider (green is enabled, grey is disabled).
  3. Select the **Position** for the new rule.
  4. Under the **Rule Type** drop-down, select **Internet**.
4. In the **Source** section, select the source of the traffic the egress rule applies to.

If necessary, add hosts that you defined above in [Egressing Traffic for Static Hosts (Optional)](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic#to-create-a-network-rule-that-egresses-to-an-allocated-ip).
5. Expand the **App/Category** section and select one or more applications for the rule.
6. In the **Configuration** section, under **Routing Method**, select **NAT**.
7. Under **Allocated IPs**, select the IP address(es) to egress the traffic to.
8. Click **Save**. The panel closes, and the settings are updated in the rulebase.

The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
9. Click **Publish**. A confirmation window opens, click **Publish**.

## Best Practices for Egressing Traffic

We recommend these best practices when you configure Network Rules that egress traffic with the following **Routing Methods**:

- NAT traffic via IPs:

![nat_egress.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27867204454941.png)
  - Use at least two egress IP addresses from 2 different PoP locations in the Network Rule to provide failover in case the destination isn’t reachable from the first IP **Note:** For Network Rules that only route traffic with sensitive applications, such as VoIP, configure one egress IP address (see below [Using Egress IPs for VoIP Traffic](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic#using-egress-ips-for-voip-traffic))
- Route traffic via a PoP location:

![route_via_egress.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27867204528029.png)
  - Use two different PoP locations in the Network Rule to provide failover in case the destination isn’t reachable from the first PoP

### Multiple Egress IPs

When a Network Rule is configured with multiple egress IPs/Route Via PoPs is configured, the Cato Cloud identifies the PoP to which the egress IP belongs and builds a list of candidate PoPs around it. Then it searches for the nearest PoP and uses it to egress the traffic. If both IPs belong to the same PoP, the first IP in the list is used.

![egress_rule_nat.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27867186280989.png)

### Using Egress IPs for VoIP Traffic

For network rules that only route traffic with sensitive applications, such as VoIP or ERP, we recommend that you configure these settings:

- Only ONE egress IP address
- Enable the [Preferred IP for SIP Traffic advanced setting](/v1/docs/working-with-advanced-configuration-for-the-account) to always use the same egress IP address

These settings force the PoP to only use the egress IP. If that IP isn't available, it waits until the egress IP address is reachable again and makes sure that the connection state is maintained.

## Troubleshooting Egressing Traffic with Network Rules

Some applications might block access if the same NAT IP is used by many users or sites at once. Cato recommends that if there is no need for a specific NAT IP for a specific domain, you should use **Route Via**, which will route the traffic using dynamic PoP IPs for the connections.

## FAQ for Egressing Traffic

Question: When there is a Network Rule configured with an egress NAT IP, is there a limit of 64K concurrent flows for each egress IP address (assuming that each flow consumes a single TCP/UDP port)?

Answer: No. For each egress IP address, the PoP creates a unique NAT translation entry for every four-tuple hash (SRC IP, SRC port, DEST IP, and DEST port). This means that the 64K concurrent flows limit applies to each pair (ie. source IP, destination IP). For example, if two LAN hosts communicate with two public destinations using destination port TCP/443, the PoP can allocate up to 128K ports to support the concurrent flows (64K ports for each SRC/DST IP and SRC/DST port).
