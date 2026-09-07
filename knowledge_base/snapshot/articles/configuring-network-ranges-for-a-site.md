---
title: "Configuring Network Ranges for a Site"
slug: "configuring-network-ranges-for-a-site"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/configuring-network-ranges-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Network Ranges for a Site

This article explains how to create and configure network ranges for a site in your account.

## Overview of Network Ranges for a Site

The Native Range for the site is the IP range that you configured for each LAN interface when you created the site. You can configure additional LAN network ranges with their own IP address ranges.

The types of networks that you can add depends on the site's **Connection Type**:

| Connection Type | Direct Range | Routed Range | VLAN |
| --- | --- | --- | --- |
| Socket | ✓ | ✓ | ✓ |
| Azure vSocket | ✓ | ✓ |  |
| ESX vSocket | ✓ | ✓ | ✓ |
| AWS vSocket | ✓ | ✓ |  |
| Cato-initiated IPsec IKEv1 and IKEv2 | ✓ |  |  |
| vSocket VSH (legacy) | ✓ |  |  |
| vSocket VGS (legacy) | ✓ |  |  |

For more information about configuring DHCP settings for a network range, see [Configuring DHCP Settings](/v1/docs/configuring-dhcp-settings).

## Creating a Network Range for a Local Network

Use the **Networks** section to define the network ranges for each LAN interface configured for the site. The IP addresses cannot use /31 or /32 CIDR blocks.

**Best Practice:** All sites in your account use unique network ranges for optimal troubleshooting and avoiding route loops. However, if two or more sites in your account use overlapping IP address ranges, you must enable and configure Static Range Translation. For more information, see, [Configuring System Settings for the Account](/v1/docs/configuring-system-settings-for-the-account).

These are the types of network IP ranges that you can create:

- **Direct** - Network segments directly connected to the Cato Socket or firewall (not via a router), but the IP range is different than the site's native range.
- **Routed** - Network segments that connect to a Socket through a router.
- **VLAN** - When VLANs connect to Cato, the connection is similar to a trunk port. VLAN tags are stripped as the packets enter the Cato Cloud. When a packet enters the LAN again, the VLAN tag is reapplied.
  - You can optionally tag the Native range per LAN interface with a VLAN ID (802.Q). This is considered a best practice to only have tagged networks within your sites. You can either add the tag while creating a site or add it for existing sites.

**Note:** VLAN tags for Native ranges are supported for physical and ESX vSockets only, from Socket version 21.1.18975.

> [!NOTE]
> Note:
> 
> The **Local IP** field isn't relevant for IPsec sites.

For more about configuring DHCP settings for a network range, see [Configuring DHCP Settings](/v1/docs/configuring-dhcp-settings).

### Internet Only IP Ranges

You can configure a network range to only provide access to the Internet without the possibility of communicating with the WAN. Internet Only ranges can be configured in multiple sites with identical IP ranges. This simplifies network management and improves security for guest services, such as guest WiFi.

Internet Only network ranges are not propagated to the global routing table maintained in the Cato Cloud, and are managed locally in the Socket. Hosts within this range can access Internet applications based on the site's Internet firewall settings.

Cato recommends as a best practice for the security of guest WiFi networks to use Internet Only ranges together with the [Cato captive portal](/v1/docs/configuring-the-cato-captive-portal).

Internet-Only ranges require an IPsec site or a Socket site with a physical Socket with version 23 and higher. Internet-Only ranges support the following:

- DHCP configurations
- Local port forwarding
- DNS forwarding
- LAN Firewall configurations
- Bypass rules

The following known limitations apply to Internet Only ranges:

- Route Via settings can’t be used with Internet Only ranges. Hosts on an Internet Only network egress only from the PoP connected to the local Socket.
- Remote Port Forwarding is not supported for internet-only ranges.
- Native ranges cannot be configured as internet-only.

![SecureNetwork_LAN_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27469136988189.png)

**To create an IP address range for a LAN interface:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. Expand the LAN interface.
4. From the LAN interface, click **New** to add a new network segment for the IP range.

The **New Interface IP Range** panel opens.
5. Enter the **Name** for the IP range.
6. From the **Type** drop-down menu, select the type of IP range: **Direct**, **Routed**, or **VLAN**.

**Note:** VLAN ranges are supported only for physical Sockets and ESX vSockets.
7. Enter the **Subnet** and IP settings based on the range type:
  - For Direct and VLAN ranges, enter the **Local IP**. This is the IP address for the Cato LAN port.
  - For Routed ranges, enter the **Gateway**. This is the next hop IP address for the neighboring router.
8. For VLANs, enter the **VLAN** ID for this range.
9. **(Optional)** Configure the DHCP settings for this range, from the **DHCP Range** drop-down menu select one of these options:
  - **Disabled** - DHCP is disabled for this range
  - **Account Default** - this range uses the default DCHP settings for the account
  - **DHCP Range** - Enter the range of IP addresses that the DHCP server assigns for this segment
10. **(Optional)** Configure **Additional Settings** for the range:
  - To configure the range as Internet Only, under **Routing Type**, select **Internet Only**.
  - To enable mDNS on a VLAN, under Multicast, select **mDNS Gateway**. For more information, see [Enabling mDNS Between Subnets](/v1/docs/enabling-mdns-between-subnets).
11. Click **Apply**. The **New Interface IP Range** panel closes.
12. Click **Save**. The IP address range is created.

## Editing a Network Range

Use the **Edit Interface IP range** panel to edit the settings for a network range.

**To edit a network range:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. Expand the LAN interface.

The **Edit IP Range** panel opens.
4. Edit the settings for the network range.
5. Enter the **Name** for the IP range.
6. From the **Type** drop-down menu, select the type of IP range: **Direct**, **Routed**, or **VLAN**.

## Deleting a Network Range

Before you can delete a network range, make sure that it isn't used somewhere else in the Cato Management Application, such as network or firewall rules. In addition, make sure that no hosts are configured for that range (in **Network > Site Settings > Host**).

**To delete a network range:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. Expand the LAN interface.
4. From the network range, click the Delete icon![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/img-cc8e2cca6fcdef2b25cda91a4cf0207c(1).svg).

The network range is removed from the LAN interface.
5. Click **Save**. The network range is deleted.

## Defining Segments for Security Policies

In some cases, you may need to define a special security policy for a segment of IP addresses that are part of a bigger network range. For example, within 10.0.0.0/24, the 10.0.0.0/27 block has different security requirements.

![SecureNetwork.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27469155451293.png)

To support such cases, you can define a network range within a site that is a subset of an existing range in the same site. Then, use the item for that network sub-range in a security policy (such as a firewall rule).

> [!NOTE]
> Note:
> 
> If a rule or group is referencing an IP that is included in two ranges in the same site, the more accurate definition (e.g. 10.0.0.0/27 in the example above) always takes precedence.
