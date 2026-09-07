---
title: "Working with Advanced Configuration for the Account"
slug: "working-with-advanced-configuration-for-the-account"
updated: 2026-06-29T06:21:50Z
published: 2026-06-29T06:21:50Z
canonical: "knowledge.catonetworks.com/working-with-advanced-configuration-for-the-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Advanced Configuration for the Account

This article explains how to customize an Advanced Configuration feature for the entire account.

## Overview of Advanced Configuration for the Account

The options in the **Advanced Configuration** page give you increased granular control over different settings in your account. The screen also shows the default value for each of the disabled settings.

When you disable an advanced setting, it returns to the default value. However, the custom value is saved and if you enable the setting later, the custom value can be used.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33047343262749.png)

**To configure advanced configuration features for an account:**

1. From the navigation menu, click **Resources > Advanced Configuration**.
2. In the **Status** column, use the toggle to enable or disable the status of each setting (green is enabled, grey is disabled).
3. To configure or edit the value of a setting, click on the name of the setting in the **Name** column.

The **Edit <Setting Name>** panel opens.
4. In the **Edit** panel, you can:
  - Enter or select a **Value**
  - Enter or edit a **Comment** to explain the reason for this advanced setting (Recommended)
5. Click **Apply**. The change for the advanced configuration is added to the screen.
6. Click **Save**. The configuration settings are saved.

### Precedence for Advanced Configuration with Sites and VPN User Settings

When you configure the advanced feature for a site or SDP user, it overrides the setting for the account in the **Advanced Configuration** page. The following table shows each advanced feature and if it applies to a site or a SDP user.

| Feature Name | Applies to |
| --- | --- |
| Block Local Routing when Disconnected from PoP | Sites (only for Sockets) |
| Burstiness Downstream Value | Sites (only for Sockets) |
| Burstiness Upstream Value | Sites (only for Sockets) |
| IKEv2 Send Single TS per Payload | Sites (only IPsec IKEv2) |
| Preferred IP for SIP Traffic | Sites |
| Recovery via Internet | Sites (only for Sockets) |
| Revoke Certificates by Serial Number | All SDP users |
| SIP ALG | Sites |
| TCP Acceleration on SYN for WAN traffic | Sites and SDP Users |
| TCP Congestion Algorithm | Global only |
| Verify OID in Device Certificate | All SDP users |
| VPN Office Mode | All SDP users |
| WAN Keep-alive Frequency | Sites (only for Sockets) |
| WAN Recovery | Sites (only for Sockets) |

You can configure the following settings only for individual sites (not as a global setting for the account):

- Socket to PoP Max MTU (only applies to physical Sockets)

For more about Advanced Configuration for sites, see [Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site).

## Enabling SDP Users to Configure VPN Office Mode

When a SDP user is working in an office that is behind a Cato Socket, the Cato Client automatically connects to that site. This behavior is called VPN office mode and it is enabled by default for all accounts. Without office mode, when the Cato Client connects to the VPN behind a Cato Socket, the Client connects with a VPN tunnel-in-tunnel which often has a negative impact on performance.

With office mode, the Cato Client connects to the Cato Cloud using the Socket tunnel and is treated as a regular host for that site. The Client receives the networking and security settings from the site and prevents using a VPN tunnel-in-tunnel.

Sometimes office mode can prevent someone who is visiting a branch office from connecting to resources in a different office, such as the corporate headquarters. You can choose to enable SDP users to configure the Cato Client behavior for office mode.

For more about how to enable SDP users to configure Office Mode for their clients, see [Configuring Office Mode](/v1/docs/configuring-office-mode).

## Configuring WAN Recovery for the Account

To improve resiliency of your network, the WAN Recovery feature provides support if there are connectivity problems in the Cato Cloud, and the Cato Sockets cannot use it to send WAN traffic to the other sites. This feature automatically uses bypass tunnels to maintain connectivity with the other Socket sites. When the Sockets re-establish connectivity to the Cato Cloud, they automatically resume regular operation.

> [!NOTE]
> Note:
> 
> [Off-Cloud traffic](/v1/docs/routing-traffic-to-an-off-cloud-link) must be enabled on the Socket WAN links to support WAN Recovery.

During network recovery, the WAN traffic bypasses the Cato Cloud and these are the changes to the traffic:

- The Cato Management Application does not analyze data for connectivity and does not generate alerts for network health or quality
- The WAN and Internet firewalls are not applied to the traffic
- The Threat Protection services are not applied to the traffic

To configure the **WAN Recovery** setting, see above Configuring Advanced Features the Account with these values:

- **Disabled** - Default global setting. Sockets establish tunnels with other Socket sites and use keep-alive messages to maintain the tunnels. Recovery IS enabled by default for all Socket sites in the account.
- **Enabled** and **On** - The account is configured to provide recovery for WAN traffic to other sites. The functionality is the same as **Disabled**.
- **Enabled** and **Off** - Recovery is NOT enabled for this account, and bypass tunnels are NOT supported or maintained.

### Note

**Note:** Events generated by the WAN Recovery feature are described as **Off-Cloud Recovery**.

For more about configuring the global WAN Recovery setting for specific sites, see [Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site).

## Configuring Recovery via Internet for the Account

To improve resiliency Internet traffic, the **Recovery via Internet** feature provides support if there are problems connecting to the Cato Cloud, and the Cato Socket cannot use it to traffic to the Internet. When enabled, this feature automatically recovers Internet connectivity with the ISP links to send traffic to the Internet.

During the temporary Internet recovery, the Internet traffic bypasses the Cato Cloud and these are the changes to the traffic:

- The Internet firewalls rules are not applied to the traffic
- The Threat Protection services are not applied to the traffic
- The Cato Management Application does not analyze data for connectivity and does not generate alerts for Internet traffic

To configure the **Internet Recovery** setting, see above, Configuring Advanced Features the Account with these values:

- **Disabled** - Default global setting. Recovery IS enabled by default for all Socket sites in the account. We recommend that you use this setting.
- **Enabled** and **On** - The account is configured to provide recovery for all traffic to Internet. The functionality is the same as **Disabled**.
- **Enabled** and **Off** - The **Recovery via Internet** feature is DISABLED for this the account.

### Note

**IMPORTANT!** We recommend that you always enable the **Recovery via Internet** feature and select the **On** or **Off** option to manage recovery for Internet traffic. When this feature is disabled, if the Socket can't connect to the Cato Cloud, then it doesn't route traffic to the Internet.

For more about configuring the global Internet Recovery setting for a specific site, see [Advanced Configurations for a Site](/v1/docs/advanced-configurations-for-a-site).

## Using the Same (Preferred) Egress IP Address for VoIP and SIP Traffic

If you work with a UCaaS and have an egress network rule for VoIP or SIP traffic, sometimes the UCaaS (such as RingCentral) has problems if the IP address changes. When the **Preferred IP for SIP Traffic** feature is enabled, VoIP and SIP traffic always uses the same egress IP address.

### Note

**Note:** You must have an egress network rule for VoIP or SIP traffic to use this feature.

## IKEv2 Sites Sending a Single TS per Payload

When creating a child SA, Cato sends multiple traffic selectors (TS) in the same TS payload in accordance with RFC 7295. Some third-party solutions, such as Cisco ASAs, only support a single TS in each child SA. A Cisco ASA will send a **TS_UNACCEPTABLE** message in response to a Cato proposal to create a child SA with multiple TS.

When **IKEv2 Send Single TS per Payload** is enabled and set to **On** , only a single TS is sent in each child SA. It is disabled by default.

## Blocking Local Routing when Sites are Disconnected from a PoP

By default, traffic within a site (for example, between VLANs) is routed via the Cato PoP, which inspects the traffic. Traffic flows from the VLAN to the PoP in the Cato Cloud and then to the other VLAN.

If a site is temporarily disconnected from the Cato Cloud, the default behavior is fail-open. The traffic flows from the VLAN directly to the other VLAN without being inspected. You can change the default global account-level behavior to fail-closed, so that by default all Socket sites block local routing traffic when they disconnect from the PoP. Requires Socket v15.0 or higher.

### Note

**Note:** For sites that are configured with LAN Firewall or Local Routing rules, these rules take precedence over the **Block Local Routing when disconnected from PoP** setting. Therefore, this setting does NOT apply to traffic that matches the rules.

To configure the **Block Local Routing when disconnected from PoP** setting, see above [Overview of Advanced Configuration for the Account](/docs/working-with-advanced-configuration-for-the-account#UUID-80c11ba6-65c4-a267-aa30-e51b9ac63fd1_id_top) with these values:

- **Disabled** - Default global setting. The traffic routing within a supported site is allowed when the site is disconnected from the PoP. This is fail-open behavior.
- **Enabled** and **On** - The traffic routing within a supported site is blocked when the site is disconnected from the PoP. This is fail-closed behavior.
- **Enabled** and **Off** - The traffic routing within supported site is allowed when the site is disconnected from the PoP. This is fail-open behavior. The functionality is the same as **Disabled**.

The following diagram shows the local routing behavior:

![Block_Local_Routing.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24198311116445.png)

## Verifying OID in Device Certificates

**Verify OID in Device Certificate** enhances Device Certificate checks. When enabled, you can define a list of device certificate OIDs that can connect to your network. Only devices authenticating with a certificate that matches a defined OID are able to connect. Separate multiple OIDs with a semicolon, and in the following format:

- cert_ext_obj(cert, "<extension_key>") == "<OID_value1>;<OID_value2>"

The extension key and OID values can be found using the certutil or openssl x509 certificate tools.

This feature is disabled by default. SDP users may not be able to connect to your network if you activate this setting without correctly configuring your device’s certificates.

## Revoking Certificates by Serial Number

**Revoke Certificates by Serial Number** enhances Device Certificate checks. When enabled, you can define a list of blocked certificate serial numbers. Devices authenticating with a certificate that matches a defined serial number are blocked.

- Each serial number must be in a format with a delimiter (1a:2b:3c:4d ...)
- Separate multiple serial numbers with a comma

There is no limit to the amount of serial numbers that you revoke

This feature is disabled by default. SDP users may not be able to connect to your network if you activate this setting without correctly configuring your device’s certificates.

## Modifying WAN TCP Proxy Mode

TCP Proxy enables you to modify your WAN TCP proxy mode to start on first SYN packets for each connection OR to delay and start the WAN TCP proxy after TCP handshake has been completed. For more about TCP proxy mod, see [Explaining the Cato TCP Acceleration and Best Practices](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices).

To configure the **TCP Acceleration on SYN for WAN traffic** setting, see above [Overview of Advanced Configuration for the Account](/docs/working-with-advanced-configuration-for-the-account#UUID-80c11ba6-65c4-a267-aa30-e51b9ac63fd1_id_top) with these values:

- **On** - Full WAN TCP Proxy.
- **Off** - Preserving original WAN TCP negotiation and delaying the TCP proxy.

## Modifying Burstiness Value

Micro-bursts are characterized by a sudden surge of packets or data frames that occur within a very short time frame.

When micro-bursts exceed a site's rate limit in a short time, packet loss may occur due to excessive packet drops by the Last Mile Provider (ISP).

**Burstiness downstream value** and **Burstiness upstream value** allow you to adjust how your sites handle micro-bursts over the network by modifying burstiness level values per the downstream or upstream directions. Modifying the burstiness level values may mitigate packet loss caused by burstiness by applying a more aggressive or more permissive shaping policy for micro-bursts. The default burstiness value depends on the interface bandwidth:

- For interface bandwidth 40 Mbps and above, the default value is 0.2
- For interface bandwidth below 40 Mbps, the default value is 0.1

For more about burstiness and packet loss, see [How to Troubleshoot Socket Site Packet Loss](https://support.catonetworks.com/hc/en-us/articles/360002598617-How-to-Troubleshoot-Socket-Site-Packet-Loss).

### Note

**Notes:**

- All Sockets must run on version 12.0 and above to support configuring burstiness.
- The new value is applied only after tunnel reset.
