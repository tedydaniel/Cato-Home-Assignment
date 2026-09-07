---
title: "Using the CMA to Add Sites"
slug: "using-the-cma-to-add-sites"
updated: 2026-07-06T14:40:40Z
published: 2026-07-06T14:40:40Z
canonical: "knowledge.catonetworks.com/using-the-cma-to-add-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the CMA to Add Sites

## Overview of Cato Sites

Each site in your account can be classified as one of these site types:

- Branch
- Headquarters
- Cloud Data Center
- Data Center

The site types are used to determine which icon is used for the site in the My Network - Topology window. You can use them to easily identify the key sites in your account. The different site types are not functionally different in the Cato Management Application (CMA) or your network.

For each office location that you connect to the Cato Socket, you must define a site according to the connection type required for the location.

The site definitions include general configuration information, DNS and Hosts settings.

The following table shows the additional feature configurations that are available for each type of site:

| Connection Type | Multiple Active WAN | Bypass | Local Port Forwarding | Networks |
| --- | --- | --- | --- | --- |
| Sockets X1500, X1600, X1600 LTE, X1700 | Yes | Yes | Yes | Full |
| Azure/AWS/ESX/GCP vSocket | Yes | Yes | Yes | Full |
| Cloud Interconnect | Yes | - | - | Partial |
| IPsec IKEv2 | Yes | - | - | Partial |
| IPSec IKEv1 (Cato-initiated) | No | - | - | Partial |

## Adding a New Site

For each office location you connect to the Cato Management Application, you must define a site according to the connection type at the location. In addition, you can configure advanced settings and features.

All of the settings in this window can be edited at a later time.

The LAN Native Range for the site uses the CIDR for the subnet. /32 CIDR blocks aren't supported.

> [!NOTE]
> Note:
> 
> If two or more sites in your Cato account use identical IP address ranges, you must enable and configure Static Range Translation as described in [Configuring System Settings for the Account](/v1/docs/configuring-system-settings-for-the-account).

**To add a new site:**

1. From the navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![Add_Site.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25831719795613.png)
3. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Select the **Connection Type** for the site.
  4. Configure the **Country**, **State**, **Time Zone**, and **City** to set the time frame for the **Maintenance Window** for Socket upgrades.

If your city is not listed, select the next closest city in the list. This ensures that the closest PoP is automatically selected for best performance.
  5. Select the **Time Zone**.

For Sockets and vSockets, this setting is used to set the time frame for the Maintenance Window for Socket upgrades.
4. In the **WAN Interface Settings** section, configure the settings for the Sockets:
5. If the site uses a link for the secondary ISP connection, select **Enable WAN2**.
6. For Sockets and vSockets, configure the bandwidth limits for the site:
  1. Enter the values (in Mbps) for the **WAN1 Bandwidth** and **WAN2 Bandwidth** for **Downstream** and **Upstream**.
  2. If necessary, repeat the previous step for the **WAN2 Bandwidth**.
7. In the **LAN Interface Settings** section, configure the LAN **Native Range** for the site.
8. Select the appropriate **License** based on the region.
9. Click **Apply**.

The new site is added to the account.

## Controlling the Bandwidth for a Site

> [!NOTE]
> Note:
> 
> Cato account licenses use one of two models. This section applies to the Enforcement Model only and is not relevant to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027). Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

You can use the Cato Management Application to control the maximum upstream and downstream bandwidth from the Cato Cloud to each site.

Configure the bandwidth setting according to the terms of the Cato site license. For example, if the site license is for 100 Mbps, configure each link (upstream and downstream) as 100 Mbps. If the Cato site license has a higher bandwidth value than the ISP link bandwidth, set each link’s bandwidth according to the ISP bandwidth.

You can set values as whole numbers or include up to one decimal.

For Socket sites with multiple WAN links, the license is for the aggregated bandwidth of all the WAN links. For example, for a site license of 500 Mbps, we recommend setting each WAN link to 250 Mbps. However, there are situations where one ISP has a lower bandwidth, so WAN1 would be set to 400 Mbps and WAN 2 would be set to 100 Mbps.

For links that are dedicated to off-cloud or Alt WAN traffic, this is not part of the site bandwidth license, and set the link to the actual last-mile bandwidth.

You can configure the settings as follows:

Socket sites - Network > {site} > Site Configuration > Socket

IPsec sites - Network > {site} > Site Configuration > IPsec > Primary and Secondary tunnels
