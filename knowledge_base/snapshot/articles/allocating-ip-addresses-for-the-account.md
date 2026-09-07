---
title: "Allocating IP Addresses for the Account"
slug: "allocating-ip-addresses-for-the-account"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/allocating-ip-addresses-for-the-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Allocating IP Addresses for the Account

## Obtaining IP Addresses for Specific Requirements

In some cases, you need to obtain IP addresses from Cato Networks for use as part of network configurations (for example, NAT and Routing). These IP addresses are only associated to your account and aren't shared with any other Cato Networks customers.

Using **IP Allocation**, you can specify multiple locations from which Cato Networks can allocate unique IP(s).

- If you require more than one IP address per location, select that location as many times as required. A different IP address is allocated for each selection.
- The number of unique IP addresses that you can obtain is determined by your license. For additional IPs, contact your reseller or [sales@catonetworks.com](mailto:sales@catonetworks.com).

**To obtain unique IP addresses for your account:**

1. From the navigation menu, click **Network > IP Allocation**.
2. Select the location where you are allocating a unique IP address.
3. Click **Save**.

**To remove an allocated IP address:**

1. For the specific IP address, click the **Delete** icon.
2. Click **Save**. The allocated IP address is removed from the account.

### Using NAT to Assign the Allocated IP as a Fixed IP

When you define a network rule to egress traffic to an allocated IP address, by default the Internet traffic undergoes Network Address Translation (NAT) with the egress (public) IP addresses of the connected PoP in the Cato Cloud. These egress IP addresses can change from time to time. If you want your Internet traffic to use a fixed public IP address to egress from the POP, use the **IP Allocation** window to allocate a fixed public IP address to your account. Once allocated, you can bind that IP address to one of the network rules NAT settings (**Network > Network Rules**).

## Related Resources

- [Configuring Network Rules](/v1/docs/configuring-network-rules)
- [How to Configure an Egress Rule](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic)
