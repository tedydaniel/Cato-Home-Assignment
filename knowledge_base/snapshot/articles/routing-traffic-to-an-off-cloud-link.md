---
title: "Routing Traffic to an Off-Cloud Link"
slug: "routing-traffic-to-an-off-cloud-link"
updated: 2026-07-26T12:03:12Z
published: 2026-07-26T12:03:12Z
canonical: "knowledge.catonetworks.com/routing-traffic-to-an-off-cloud-link"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Routing Traffic to an Off-Cloud Link

## Overview of Off-Cloud Transport

Traffic that is sent over the Cato Cloud benefits from the Cato network and security enhancements. However, there are specific scenarios where companies may need to use Socket to Socket direct VPN connectivity over the Internet. The off-cloud transport feature lets you configure Sockets to send off-cloud traffic over the Internet instead of the Cato Cloud. For example, when there are regular backups between different sites in the same region, you can designate these backups as off-cloud transport.

The Sockets create a full mesh topology with each other for the off-cloud traffic. The traffic is encrypted and sent over the Internet using DTLS tunnels.

For Sockets with multiple links, you can enable or disable each link for sending off-cloud traffic. Off-Cloud can be configured in these deployments:

- Active/Active - the off-cloud traffic is load balanced and distributed between the active links in a weighted manner according to the available bandwidth for each link
- Active/Passive (and Active/Active/Passive) - the passive link provides redundancy in case the active link goes down, or the link quality declines significantly

**Note:** Off-Cloud traffic is excluded from the bandwidth license for the site.​ The maximum Socket throughput of a WAN link is for all traffic combined (WAN, Off-cloud, bypass). So if an X1500 Socket (500 Mbps max throughput) is sending 400Mbps of WAN traffic, then 100Mbps is available for off-cloud and bypass traffic.

### Known Limitations

- Off-Cloud traffic is not inspected by the Cato Threat Protection engines.
- Sockets support a maximum of three links for off-cloud traffic.
- You can't route FTP passive mode with Off-Cloud traffic, you can only route it over the Cato Cloud.
- Off-Cloud (site-to-site) tunnels can't be established between sites that are connected to the same ISP router. Each site needs to have a unique public IP address.
- Alt-WAN isn’t supported for Off-Cloud as a secondary transport. You can’t configure a network rule with Alt-WAN as the primary transport that fails over to Off-Cloud.

### Working with Off-Cloud Traffic

Cato Sockets support two types of off-cloud traffic, transport and WAN recovery. WAN recovery provides resiliency if there are connectivity problems in the Cato Cloud, and automatically uses bypass VPN tunnels to maintain connectivity with the other Socket sites. When you configure a link to send off-cloud traffic, that link is enabled to send both transport and recovery traffic. You can't designate one link for off-cloud transport and another link for recovery in a Socket.

> [!NOTE]
> Notes:
> 
> - Off-Cloud transport is officially supported for simple network rules only. If you configure a complex rule using Off-Cloud as the transport, the traffic is still sent to the PoP for analysis. A complex network rule is a network rule that the Socket itself cannot evaluate. Therefore, the Socket needs to send the traffic to the PoP to choose the correct network rule which in turn enables TCP Proxy. A complex rule may contain Applications, Applications Categories, Services, Custom Applications or Domain/FQDN objects.
> 
> Sometimes, this traffic will trigger TCP acceleration mode, in which case the traffic will be sent through the PoP and not Off-Cloud, as intended. In other instances, even when the traffic is sent Off-Cloud, it might appear as going through the PoP because of the previously mentioned analysis.
> - Cato recommends that you configure all Off-Cloud simple rules at the top of the Network Rulebase.

For more about WAN recovery, see [Working with Advanced Configuration for the Account](/v1/docs/working-with-advanced-configuration-for-the-account).

## Configuring Off-Cloud Transport

This section explains how to configure sites and network rules for off-cloud transport.

### Enabling the Sites for Off-Cloud Transport

Enable off-cloud transport on each site that is sending and receiving off-cloud traffic. For Socket deployments with multiple links, configure the links to support off-cloud traffic.

By default, off-cloud transport is enabled for the WAN links on Socket sites. However, when you define the **WAN Precedence** for a link as **3 (Last-Resort)**, then off-cloud transport is automatically disabled for that link.

![off-cloud.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31225816806557.png)

The example above, shows a site with the WAN1 and WAN2 links are configured to send off-cloud traffic. You can also choose to configure a site where one of the WAN links only sends traffic over the Cato Cloud.

For more about sites with multiple links, see below [Configuring a Site for Off-Cloud with Multiple Links](/v1/docs/routing-traffic-to-an-off-cloud-link#configuring-a-site-for-offcloud-with-multiple-links).

**Configuring the Public IP and Static Port**

In general, the **Public IP** and **Static Port** settings for links that send off-cloud traffic are automatically configured by the Socket, and aren't configured in the Cato Management Application. The Socket chooses a random source port and uses the public IP address of the Internet router to initiate the connection.

You can also use the Cato Management Application to manually configure a static public IP address and port number for each link that sends off-cloud traffic. When doing this, make sure that the site's Internet router is assigned a fixed public IP address and configured with a matching Port Forwarding Rule. Otherwise, don't manually configure the **Public IP** and **Static Port** settings.

However, in some situations you need to configure these settings. For example, when you are using port-forwarding rules as a solution to NAT related issues with the local router.

**To enable off-cloud transport for a site:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Configure the active link that will be enabled for off-cloud traffic:
  1. Click the link.

The **Edit Socket Interface** pane opens.
  2. Expand the **Off-Cloud** section.
  3. In the **Traffic Status** drop-down menu, select **Enabled**.
  4. **(Optional)** Enter the **Public IP** and **Static Port** number for the off-cloud link.
4. Click **Apply**.
5. Repeat the previous steps for each site that sends and receives off-cloud traffic.

## Configuring Network Rules for Off-Cloud Transport

Create a network rule that defines the type of WAN traffic that is sent using the off-cloud transport. Then configure this rule to route the traffic over the off-cloud transport.

You can't configure the Interface Role options for off-cloud transport. Also, disable TCP acceleration for network rules that use off-cloud as the primary transport.

The Socket applies QoS and **Bandwidth Priority** to off-cloud traffic. For more information, see this [article](/v1/docs/configuring-bandwidth-management-profiles).

For more about network rules, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

**To configure a network rule for off-cloud transport:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click **New**. The **Add Network Rule** panel opens.
3. Create a new WAN networking rule:
  1. In the **General** section, enter the **Name** for the rule.
  2. In the **Rule Type** drop-down menu, select **WAN**.
  3. Configure the **Rule Order** which defines where the rule appears in the network rule base.
4. Expand the **Source** section and select one or more objects for the traffic source for this rule (or you can enter an IP address).
5. Expand the **Destination** section and enter a string or select one or more objects for the traffic destination for this rule.
6. Expand the **App/Category** section and select one or more applications for the rule.
7. Expand the Configuration section and configure the transport settings for the network rule: ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/off-cloud-qos.png)
  1. Select the **Bandwidth Priority** for the off-cloud traffic.
  2. Make sure that **Active TCP Acceleration** is disabled.
  3. In **Primary Transport**, configure **Off Cloud** as the primary **Transport**.
  4. In **Secondary Transport**, configure the secondary **Transport**:
    - **Automatic** - The Socket automatically chooses the secondary transport option
    - **None** - Only send traffic over the primary transport (the off cloud transports)
    - **Cato** - The Socket uses the Cato Cloud as the secondary transport option
8. Click **Apply**.
9. Click **Save**.

The changes are saved to your unpublished revision and are available for editing until they are published or discarded.

## Working with Multiple Links for Off-Cloud Traffic

For Sockets with multiple links, you can configure active/active and active/passive deployments for off-cloud traffic. If you choose to only enable one link for off-cloud traffic, if that link can't send traffic, then the off-cloud connections follow the **Secondary Transport** option in the Transport settings for the Network Rule.

For in-depth technical background about Sockets with multiple links, see [Part 1: The Socket Interfaces and Precedence](/v1/docs/part-1-the-socket-interfaces-and-precedence).

## Off-Cloud Traffic and Active/Passive Deployments

In active/passive deployments, the Socket links are set to different precedences and provide high availability for the site. Every few seconds, the Socket evaluates the link quality of the active link - if the health of the active link degrades, then the Socket gradually moves the traffic to the passive link. When the link quality is restored, the Socket resumes sending traffic over the active link. Similarly, if the active link goes down, then the traffic flows are transferred to the passive link until the active link is restored. These are the minimal link quality metrics:

- Packet loss - 3%
- Jitter - 30 ms
- Latency - 600 ms

If a link can't meet one of the above metrics, then the traffic is gradually moved to the other link. Every 10 seconds, the Socket evaluates the links and chooses the best link for the traffic. So, if the Socket fails over to the passive link, then it waits at least 10 seconds before it can fall back to the active link.

In some situations, failover to the passive link can create asymmetric traffic between two sites. For example, site1 and site2 are both configured for active/passive deployments. If site1 fails over to the passive link, site1 sends traffic over WAN2, and site2 sends traffic over WAN1. Another situation is when one site is configured in an active/active deployment, and the other side is active/passive. The single active link on one site sends traffic to both active links on the other site.

### Off-Cloud Traffic and Active/Active Deployments

In active/active deployments, both Socket links are set to the same precedence and provide high availability and load balancing for the site. For each traffic flow, the Socket continuously monitors each link and chooses the best option.

### Configuring a Site for Off-Cloud with Multiple Links

Define the **Socket** settings to configure the links to send off-cloud traffic as an active/active or active/passive deployment.

**To configure a site for active/active or active/passive off-cloud traffic:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Enable **Off Cloud** traffic for this site.

The slider is gray when this option is disabled.
4. Configure the settings for the WAN 1 link:
  1. Click the link.

The **Edit Socket Interface** pane opens.
  2. In the **General** section, set the **Precedence** to **1 (Active)**.
  3. Expand the **Off-Cloud** section.
  4. In the **Traffic Status** drop-down menu, select **Enabled**.
  5. **(Optional)** Enter the **Public IP** and **Static Port** number for the off-cloud link.
  6. Click **Apply**. The off-cloud settings for the WAN1 link are updated.
5. Repeat step 4, and configure the settings for the WAN 2 link:
  - For active/passive, set the **Precedence** to **2 (Passive)**.
  - For active/active, set the **Precedence** to **1 (Active)**.
6. Click **Save**. The off-cloud settings for the site are configured.

## Off-Cloud Analytics

You can show analytics and status for the off-cloud traffic and tunnels, in the **Off-Cloud** screen.

**To show the Off-Cloud analytics for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Monitoring > Off-Cloud**.

### Off-Cloud Transport Events

The **Events** screen shows all the off-cloud transport events for your account. The powerful search tools let you drill-down and identify the few events that contain the relevant data that you need.

You can learn more about using the Events screen [here](/v1/docs/analyzing-events-in-your-network). You can use the **SaaS Security API Data Protection** preset to filter the events.

| Event Sub-Type | Description |
| --- | --- |
| Off-Cloud Transport Connect | Site connects to the off-cloud tunnel (usually the initial connection) |
| Off-Cloud Transport Disconnect | Off-cloud transport for the site disconnects |
