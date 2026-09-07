---
title: "Working with the Cato System Range"
slug: "working-with-the-cato-system-range"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/working-with-the-cato-system-range"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with the Cato System Range

By default, Cato reserves the private IP prefix **10.254.254.0/24** as the internal System Range of your account. This range must be allowed within the network, IPs in the System Range allow for Cato's features to work properly in your account.

This article includes mapping of IPs in the System Range and their purpose, refer to this mapping to identify System Range hosts within your network traffic.

If you want to monitor the availability of the default Cato System Range, you can set up a continuous ping with ICMP to 10.254.254.1 (for a customized range, use X.Y.Z.1 such as 192.168.1.1

## Changing The System Range

In case the default reserved **10.254.254.0/24** IP prefix does not fit your environment's network design, you can modify the System Range to a custom range of your choice.

If you need to modify the System Range, please reach out to Cato Support.

## Reserved IPs in The System Range

Reserved IPs of the System Range can be identified in multiple interfaces such as PCAPs, routing tables, the Socket WebUI, the Cato Client, and more.

The following table lists known internal hosts and their functions. When you change the System Range to a custom IP prefix, the mapping of hosts changes as well, this mapping can be found in the **Custom Range IP Address** column below.

Additional private IPs (not included in this table) are used for internal purposes. Please reach out to Cato Support if you have questions on IPs within the System Range that are not listed below.

| Item | Description | Default Range IP Address | Custom Range IP Address |
| --- | --- | --- | --- |
| DNS | Default DNS server | 10.254.254.1 | X.Y.Z.3 **Note:** If the query comes from and is forwarded to the same site the source IP will be x.y.z.1 |
| User Awareness Client | Source for WMI queries sent to Directory Services | 10.254.254.12 | X.Y.Z.9 |

> [!NOTE]
> Note:
> 
> ​After you change the System Range, we recommend that you flush the DHCP cache of connected devices to avoid IP overlapping.
