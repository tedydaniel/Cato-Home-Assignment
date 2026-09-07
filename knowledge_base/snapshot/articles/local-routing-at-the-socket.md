---
title: "Local Routing at the Socket"
slug: "local-routing-at-the-socket"
updated: 2026-08-27T07:22:40Z
published: 2026-08-27T07:22:40Z
canonical: "knowledge.catonetworks.com/local-routing-at-the-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Local Routing at the Socket

> [!TIP]
> **Note:**
> 
> For many customers, the Local Routing feature is replaced by the LAN Firewall. The LAN Firewall policy enhances the existing Local Routing capabilities that control the LAN communication between hosts and networks behind a Socket site.

For Socket sites, you can configure traffic between local network ranges and/or local host to be routed locally by the Socket and prevent it from going to the Cato Cloud and back. Traffic routed locally is NOT inspected and WAN Firewall rules are not applied to it.

The direction of a rule indicates to which direction the rule applies. For example, an allow rule in one direction from Host A to Host B, locally routes communication initiated by Host A only. An allow rule in both directions from Host A to Host B, routes communication locally initiated by either host.

![localrouting.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247937868701.png)

**To define a local routing rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Local Routing**.
3. Click **New**. The **Add Rule** panel opens.
4. In the **General** section:
  - Enter a **Name** for the new rule.
  - By default, the rule is **Enabled**. You can disable the rule using the slider.
  - Under **Direction**, select **To** to enable traffic in one direction only, or **Both** to enable traffic in both directions
5. In the **Source** and **Destination** sections, define the traffic source and destination entities for this rule.

For more information, see [Source and Destination Objects](/v1/docs/reference-for-rule-objects).
6. In the **Protocols** section, select the protocols that this rule applies to (TCP, UDP, or ICMP).
7. In the **Ports** section, enter the port or port range for this rule.
8. Click **Apply**, and then click **Save**.

## Configuring NAT for a Local Routing Rule

There are scenarios that require using NAT between the LAN networks within a site, this can be between two (or more) directly connected networks, or between routed networks (static routes or BGP routes).

Configure a Local Routing rule with Dynamic NAT overload (Port Address Translation - PAT), so that the Socket translates the source IP address of a packet to the egress network range interface IP address and a random port number. The egress interface must belong to a network range (native range, routed range, or VLAN range).

**Requirements for Local Routing Rules with NAT:**

- Supported for sites with Sockets version 13.0 and higher
- You can only configure the rule in the **To**![To_arrow.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247954213789.png) direction
- For SNAT configuration, you must use one of the following predicates as the **Destination** of the rule: Global Range, Interface Subnet, or a Host
- After you save the configuration for the rule, the Cato Management Application automatically calculates the **Outbound Network** and **Outbound IP** for the rule
- Known limitation: For local routing rules with NAT for FTP traffic, you must configure the **Ports** to **Any**

![Local_PAT_Routing.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247906491933.png)

These are the fields in the **NAT** column:

- **Outbound Network** - name of the network range in this site
- **Outbound IP** - translated egress IP address for this rule

**To configure NAT for a local routing rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Local Routing**.
3. Click **New**. The **Add Rule** panel opens.
4. Configure the settings for the rule as explained in the section above.
5. Configure the NAT settings for the rule:
  1. Expand the **NAT** section.
  2. Click **Enable NAT**.
  3. For **NAT Type**, select **Dynamic NAT (PAT)**.
6. Click **Apply**.

The local routing rule shows the **Outbound IP** (translated IP address) for the rule.

## Disabling a Local Routing Rule

You can disable a rule to temporarily disable local routing for that traffic and resume sending it to the Cato Cloud. Cato recommends that you delete rules that you are no longer planning to use.

**To disable a local routing rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Local Routing**.
3. Click the More icon ( ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247913394461.png) ) on the rule line to disable and select **Disable**.
4. Click **Save**. The rule is disabled.

## Deleting a Local Routing Rule

**To delete a rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Local Routing**.
3. Click the More icon ( ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247913394461.png) ) on the rule line to delete and select **Delete Rule**.
4. Click **Save**. The rule is deleted.
