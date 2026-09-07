---
title: "Showing Known Hosts for a Site"
slug: "showing-known-hosts-for-a-site"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/showing-known-hosts-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Showing Known Hosts for a Site

Use the Known Hosts screen to show data and information about the hosts that are connected and transmitting data to a specific Socket site in your account. This information can include: hostname, IP address, MAC address, DHCP lease information, last host activity and more.

![Known_Hosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247949798813.png)

You can choose to filter the hosts according to these options:

- **All Hosts** - Shows all known hosts for the site, this can include hosts with IP addresses that are within the configured DHCP ranges, and host that are not within those ranges. This can include any host on the site that is transmitting traffic through the Socket. This is the default view.
- **Hosts in DHCP Ranges** - The screen only shows hosts with IP addresses that are within the configured DHCP ranges

**To show the known hosts for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Monitoring > Known Hosts**.
3. From the drop-down menu in the upper-right corner, select the hosts that are shown:
  - **Hosts in DHCP ranges** - Only shows hosts with an IP address that is within the DHCP network ranges for this site
  - **All Hosts** - Show all the hosts that are behind the site
4. Click **Reload** to refresh the data on the screen (the data isn't automatically updated).

> [!NOTE]
> You can save any discovered known host as a [static host](/v1/docs/defining-hosts-for-a-site) by clicking on the More![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247949869853.png) icon and selecting **Save as static host**. This action opens the **Add Host** configuration menu with the host's information automatically pre-populated, including the name, IP address, and MAC address information.
> 
> ![Known_Hosts_Save_Host.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247949971101.png)

## Understanding the Known Hosts Fields

This section explains the columns and fields in the Known Hosts screen.

- Name - Name of the host. Value is **N/A** when the hostname is unknown.

Click ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247990311325.png)to select one of these options:
  - View Analytics - Show the **Application Analytics** screen pre-filtered for this host
  - Events - Show the Events screen pre-filtered for **Events** related to this host
- IP address - IP address for the host.
- MAC Address - MAC address for the host. Value is **N/A** when the MAC address is unknown.
- DHCP Range - DHCP IP range that the host belongs to.
- Network Range - Shows the **Name** and the **Subnet** range for the network range for the site.
- IP Allocation - Shows how the IP address was allocated to the host:
  - Dynamic - hosts with a dynamic IP address allocated by the Cato DHCP server
  - Reserved - hosts with a static IP address allocated by the Cato DHCP server
    - Reserved hosts are defined in the Hosts screen for the site (Network > Sites > {site name} > Site Configuration > Static Host Reservations)
  - N/A - Hosts that are sending traffic, but the IP address was not allocated by the Cato DHCP server
- Last Activity - Amount of time that elapsed since this host had network activity (for example, **1 hour ago**).
- Lease Time - Duration for the DHCP lease (either for the specific network range or the entire account).

For hosts with **Reserved** IP Allocation, the Lease Time value is **Permanent**.
- Expires In - Amount of time remaining for the DHCP lease for this host.

For hosts with **Reserved** IP Allocation, the Expires In value is **Never**.
- Identity - For User Awareness, the user identity obtained from the LDAP provider.
- OS - Operating system of the host. For devices such as a network printer, the OS value is **N/A**. Due to a known limitation, iOS devices (behind a socket site) might be misclassified as macOS.

## Sample Known Host Use Cases

This section explains the different types of hosts and expected values for the Known Host screen.

1. Connected hosts with Dynamic IP addresses allocated by the Cato DHCP Server.

![Sample_Known_Host_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247949798813.png)
2. Connected hosts with Reserved IP address allocated by the Cato DHCP Server.

![Sample_Known_Host_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247981858205.png)
3. Connected hosts with IP addresses that were not allocated by the Cato DHCP Server. For example, a host that is configured with a Static IP address, or has received the IP address from a third-party DHCP server.

![Sample_Known_Host_3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247998089245.png)
4. Hosts that are not directly connected to the Socket. For example, hosts behind a router or firewall.

![Sample_Known_Host_4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247950316445.png)

The following information for these hosts is unknown:

- MAC Address
- DHCP Range
- Network Range
- IP Allocation
- Lease Time
- Expires In
