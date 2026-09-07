---
title: "Advanced Configurations for a Site"
slug: "advanced-configurations-for-a-site"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/advanced-configurations-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced Configurations for a Site

This article explains how to customize an Advanced Configuration for a specific site.

## Using Advanced Configurations for a Site

The Advanced Configuration section for a site lets you configure advanced features and settings for that site. The available features in the section depend on the Connection Type for the site. For more about using advanced features, see [Working with Advanced Configuration for the Account](/v1/docs/working-with-advanced-configuration-for-the-account).

When an advanced setting is disabled, you are configuring it to use the global setting.

**To configure an advanced feature for a Site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Advanced Configuration**.
3. In the **Status** column, use the toggle to enable or disable the status of each setting (green is enabled, grey is disabled).
4. To configure or edit the value of a setting, click on the name of the setting in the **Name** column.

The **Edit <Setting Name>** panel opens.
5. In the **Edit** panel, you can:
  - Enter or select a **Value**
  - Enter or edit a **Comment** to explain the reason for this advanced setting (Recommended)
6. Click **Apply**. The change for the advanced configuration is added to the screen.
7. Click **Save**. The configuration settings are saved.

### Working with Account and Site Settings

There are some features in the Advanced Configuration section that you can configure either for a specific site or a setting for all the sites in your account. When you configure the advanced feature for a site, it overrides the setting for the account (in **Assets > Advanced Configuration**). Some features are only supported for Socket sites. For example, feature alpha is only supported for Sockets. If you configure feature alpha for the entire account, it is only relevant to Socket sites.

## Configuring WAN Recovery for a Site

To improve resiliency of your network, the WAN Recovery feature provides support if there are connectivity problems in the Cato Cloud, and the Sockets cannot use it to send WAN traffic to the other sites. This feature automatically uses bypass tunnels to maintain connectivity with the other Socket sites. When the Sockets re-establish connectivity to the Cato Cloud, they automatically resume regular operation.

> [!NOTE]
> Note:
> 
> [Off-Cloud traffic](/v1/docs/routing-traffic-to-an-off-cloud-link) must be enabled on the Socket WAN links to support WAN Recovery.

During the temporary WAN recovery, the WAN traffic bypasses the Cato Cloud and these are the changes to the traffic:

- The Cato Management Application does not analyze data for connectivity and does not generate alerts for network health or quality
- The Cato security stack (firewall and Security services) is not applied to the traffic

To configure the **WAN Recovery** setting, see above [Using Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site#using-advanced-configurations-for-a-site) with these values:

- **Disabled** - This site uses the setting that is configured for the account.
- **Enabled** and **On** - This site is configured to provide recovery for WAN traffic to other sites. The functionality is the same as **Disabled**.
- **Enabled** and **Off** - Recovery is NOT enabled for this site, and bypass tunnels are NOT supported or maintained.

For more about configuring the global WAN Recovery setting for all sites, see [Working with Advanced Configuration for the Account](/v1/docs/working-with-advanced-configuration-for-the-account).

## Configuring Recovery via Internet for a Site

To improve resiliency Internet traffic, the **Recovery via Internet** feature provides support if there are problems connecting to the Cato Cloud, and the Cato Socket cannot use it to traffic to the Internet. When enabled, this feature automatically recovers Internet connectivity with the ISP links to send traffic to the Internet.

During the temporary Internet recovery, the Internet traffic bypasses the Cato Cloud and these are the changes to the traffic:

- The Internet firewalls, and URL Filtering rules are not applied to the traffic
- The Threat Protection services are not applied to the traffic
- The Cato Management Application does not analyze data for connectivity and does not generate alerts for Internet traffic

To configure the **Internet Recovery** setting, see above [Using Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site#using-advanced-configurations-for-a-site) with these values:

- **Disabled** - This site uses the setting that is configured for the account.
- **Enabled** and **On** - This site is configured to provide recovery for all traffic to Internet. The functionality is the same as **Disabled**.
- **Enabled** and **Off** - The **Recovery via Internet** feature is DISABLED for this site.

> [!NOTE]
> IMPORTANT!
> 
> We recommend that you always enable the **Recovery via Internet** feature and select the **On** or **Off** option to manage recovery for Internet traffic. When this feature is disabled, there can be issues with settings that are configured using the Socket Web UI.

## Configuring the MTU for DTLS Tunnels to the Cato Cloud

You can configure the maximum MTU for the DTLS tunnels between the Socket and the PoP in the Cato Cloud. For traffic inside these DTLS tunnels, this value overrides the MTU that is configured in the Socket WebUI. This setting is only relevant for physical Sockets, and it doesn't apply to vSockets.

Use the **Socket to PoP max MTU** field to configure the MTU for the DTLS tunnels, see above [Using Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site#using-advanced-configurations-for-a-site).

## Blocking Local Routing when a Site is Disconnected from PoP

By default, traffic within the site (for example, between VLANs) is routed via the Cato PoP, which inspects the traffic. Traffic flows from the VLAN to the PoP in the Cato Cloud and then to the other VLAN.

If a site is temporarily disconnected from the Cato Cloud, the default behavior is fail-open. The traffic flows from the VLAN directly to the other VLAN without being inspected. You can customize this behavior for a specific site, so that the behavior is different than the global default setting for the account. Requires Socket v15.0 or higher.

You can also choose to set the [global account-level behavior](/v1/docs/working-with-advanced-configuration-for-the-account) to fail-closed, so that by default all Socket sites block local routing traffic when they disconnect from the PoP.

> [!NOTE]
> Note:
> 
> For sites that are configured with LAN Firewall or Local Routing rules, these rules take precedence over the **Block Local Routing when disconnected from PoP** setting. Therefore, this setting does NOT apply to traffic that matches the rules.

To configure the **Block Local Routing when disconnected from PoP** setting, see above [Using Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site#using-advanced-configurations-for-a-site) with these values:

- **Disabled** - This site uses the setting that is configured for the account.
- **Enabled** and **On** - The traffic routing within this site is blocked when this site is disconnected from the PoP. This is fail-closed behavior.
- **Enabled** and **Off** - The traffic routing within this site is allowed when this site is disconnected from the PoP. This is fail-open behavior.

The following diagram shows the local routing behavior:

![Block_Local_Routing.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247748257693.png)

## Modifying WAN TCP Proxy Mode

**TCP Proxy** enables you to modify your WAN TCP proxy mode to start on first SYN packets for each connection OR to delay and start the WAN TCP proxy after TCP handshake has been completed. You can read more about the two TCP proxy mode in [Explaining the Cato TCP Acceleration and Best Practices](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices).

**To change the WAN TCP Proxy Mode:**

1. In the **Advanced Configuration** page, Click on the **TCP Proxy** configuration. The **Edit Configuration** pane opens.
2. Enable the configuration and select the mode value:
  1. **On** - Full WAN TCP Proxy.
  2. **Off** - Preserving original WAN TCP negotiation and delaying the TCP proxy.

## Modifying Burstiness Value

Micro-bursts are characterized by a sudden surge of packets or data frames that occur within a very short time frame.

When micro-bursts exceed a site's rate limit in a short time, packet loss may occur due to excessive packet drops by the Last Mile Provider (ISP).

**Burstiness downstream value** and **Burstiness upstream value** allow you to adjust how your sites handle micro-bursts over the network by modifying burstiness level values per the downstream or upstream directions. Modifying the burstiness level values may mitigate packet loss caused by burstiness by applying a more aggressive or more permissive shaping policy for micro-bursts. The default burstiness value depends on the interface bandwidth:

- For interface bandwidth 40 Mbps and above, the default value is 0.2
- For interface bandwidth below 40 Mbps, the default value is 0.1

For more about burstiness and packet loss, see [How to Troubleshoot Socket Site Packet Loss](/v1/docs/troubleshooting-socket-site-packet-loss).

To configure the **Burstiness value** setting for upstream or downstream traffic, see above [Using Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site#using-advanced-configurations-for-a-site).

> [!NOTE]
> Notes:
> 
> - All Sockets must run on version 12.0 and above to support configuring burstiness.
> - The new value is applied only after tunnel reset.

## Modifying IPsec Lifetime Values

IPsec phases have a lifetime, which is the duration for which the Security Association (SA) is valid.

IPsec P1 Lifetime Seconds and IPsec P2 Lifetime Seconds are two advanced configuration parameters that let you change the lifetime of each phase to match remote settings for both IKEv1 and IKEv2, respectively. The default lifetime values depend on the phase:

- For Phase 1, the default values are:

> [!NOTE]
> Note:
> 
> By default, the P1 values are not displayed in the Cato Management Application. If you want to set these values, follow the procedure outlined [above](/v1/docs/advanced-configurations-for-a-site#using-advanced-configurations-for-a-site).
  - For IKEv1: 86400
  - For IKEv2: 19800
- For Phase 2, the default value is 3600 for both IKEv1 and IKEv2.

The configuration is applied after the tunnel restarts, or after the expiration of the current SA lifetime.

For more information, see the [IPsec Sites](/v1/docs/ipsec-sites) articles.

## Entering a Static MAC Address

Some devices do not have ARP enabled for security reasons. To enable discovery of these devices, you can now manually add them to your site by providing a JSON string in the following format:

{ \"ifc_id\": \"LAN1\", \"ip\": \"10.10.10.1\", \"mac\": \"7c:05:1e:11:11:12\" }

Each of the fields presents the following parameters: 'ifc_id' specifies the LAN interface, 'ip' is the device's IP address, and 'mac' is the device's MAC address."

- ifc_id is the LAN interface. In the example above, LAN1
- ip is the device IP address. In the example above, 10.10.10.1
- mac is the device MAC address. In the example above, 7c:05:1e:11:11:12

The configuration is available for all Socket sites version 20 and later.
