---
title: "Troubleshooting Scenarios for Issues with the Cato Client"
slug: "troubleshooting-scenarios-for-issues-with-the-cato-client"
updated: 2026-08-18T07:15:32Z
published: 2026-08-18T07:15:32Z
canonical: "knowledge.catonetworks.com/troubleshooting-scenarios-for-issues-with-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Scenarios for Issues with the Cato Client

This article contains some suggestions for troubleshooting common issues with the Cato Client.

> [!NOTE]
> Note:
> 
> If the Cato Client presents an error while connecting to the Cato Cloud, refer to the following article: [Cato Client Login Errors](/v1/docs/cato-client-login-errors)

## Cato Client Conflicts with Third-Party VPN Clients

**Challenge**

When third-party VPN clients are installed on the same computer as the Cato Client, their drivers and settings can conflict with the Cato Client and override its settings. For example, Cisco AnyConnect can override the Cato Client's DNS and split-tunnel settings.

**Solution**

Cato Networks provides recommendations per Cato Client OS, as outlined below:

**Windows:** Please refer to the following KB article: [Working with the DNS Relay Service](/v1/docs/working-with-the-dns-relay-service) **macOS:** Cato Client on macOS cannot run alongside another connected VPN Profile. **iOS:** Please refer to the following KB article [Deploy a Per APP VPN with Intune for iOS](/v1/docs/deploy-a-per-app-vpn-with-intune-for-ios) **Android:** Not supported. **Linux:** Please disconnect the Cato Client while running a third-party VPN.

Please note: Running the Cato Client in full-tunnel mode alongside a third-party VPN is not recommended. [Managed Networks](https://support.catonetworks.com/hc/en-us/articles/12952058150045-Working-with-Managed-Networks) settings may be implemented to prevent third-party split-tunnel conflicts based on the network the user is connected to.

## Antivirus Blocks the Cato Client

**Challenge**

Antivirus software can identify the Cato VPN Client traffic as malicious and, by mistake, block the VPN traffic.

**Solution**

If you determine that the antivirus software on the laptop or device blocks the Cato Client, these are your options to allow the VPN connection:

- Configure the antivirus settings and create an exception for the Cato Client.
- Contact Cato Networks Support to coordinate with the antivirus vendor to whitelist our client; this may take time, so an exception is recommended if possible.

**Tip:** You can temporarily disable the antivirus software to check if this software is blocking the Cato Client traffic.

## Firewall Blocks the Cato Client

**Challenge**

It's possible that a firewall blocks the specific port that the Client uses to connect to the Cato Cloud.

**Solution**

Several types of firewalls can block the Cato Client from connecting to the Cato Cloud. The following sections describe solutions for each firewall type; use the solution that is applicable to your network.

### Network Firewall

Check the network firewall settings and see if it blocks UDP traffic over ports 53 and 443. If it does, add a rule that allows UDP traffic over ports 53 and 443 and the URLs and IP addresses described in [Prerequisites for Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

### Endpoint Firewall

For endpoint computers, you have to make sure that the endpoint firewall agent isn’t blocking the connection. If an endpoint firewall agent is installed on your computer, check the agent settings and see if it’s configured to block UDP traffic over port 53 or 443. We recommend that you contact the agent vendor and ask them to whitelist the Cato Client and the URLs and IP addresses described in [Prerequisites for Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

For Windows OS, check the Windows firewall settings and see if they’re configured to block UDP traffic over port 53 or 443. You can also change the Cato Client's default port from 443 to 1337. For more information about changing the default port, see [Configuring a Different UDP Port for Cato Client](/v1/docs/configuring-a-different-udp-port-for-the-cato-client).

## The DTLS Connection Fails with the Cato Cloud

**Challenge**

The Cato Client cannot authenticate with the Cato Cloud when the user's PC does not use the required DTLS ciphers during the DTLS handshake.

**Solution**

Confirm that the DTLS ciphers described in [Cipher Suites Used by the Cato Socket and SDP Client](https://support.catonetworks.com/hc/en-us/articles/115005910469-Cipher-Suites-Used-by-the-Cato-Socket-and-SDP-Client) are included on the PC's cryptography configuration. For windows devices, this can be checked under the following registry key:

- Cipher Suites: Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Cryptography\Configuration\Local\SSL\00010002
- Signature Algorithms: Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Cryptography\Configuration\Local\SSL\00010003

## Cato Client IP Range Conflicts with Local Network

**Challenge**

If your local network uses the same subnet as the Cato VPN IP range, overlapping networks can cause IP conflicts and routing issues. For example, the Cato Clients cannot connect to the Cato Cloud.

**Solution**

By default, Cato Networks uses the 10.41.0.0/16 subnet as the VPN range. You can change the local network IP range to avoid conflict with the Cato VPN IP range. You can also change the default VPN range in the Cato Management Application (**Resources** > **IP Ranges**).

The following screenshot shows an example of a custom IP range of 10.43.0.0/16 subnet for VPN users:

![range.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20824945984413.png)

## Unable to Access WAN or Internet Resources

**Challenge**

The Cato Client successfully connects to the Cato Cloud, but users cannot access WAN or Internet resources over the VPN connection.

**Solution**

In this situation, the Cato Client has connectivity to the Cato Cloud, but something else is blocking WAN or Internet access. You can check that the following settings are configured correctly in the Cato Management Application:

For more information about WAN and Internet access troubleshooting, see [Internet Service Reachability Troubleshooting](/v1/docs/internet-service-reachability-troubleshooting) and [Access to Internal Resources Troubleshooting](/v1/docs/access-to-internal-resources-troubleshooting).

### The Cato WAN or Internet firewall blocks VPN access

The Cato WAN or Internet firewall can block access for Cato Clients to the WAN or Internet resource. Check the firewall rule bases in the Cato Management Application (**Security** > **WAN Firewall** or **Internet Firewall**) and make sure that the firewall allows VPN access. For example, does the WAN firewall have a rule that allows VPN users to access the site?

For more information on the Cato firewall and best practices, see [Internet and WAN Firewall Policies – Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies) .

## Unable to resolve DNS

When the DNS settings are misconfigured, then users can’t connect to the network resources. The Cato Management Applications lets you configure DNS settings for the entire account in **Network > DNS Settings**. You can also configure DNS settings for each site, group, and SDP user.

By default, Cato Networks uses the following DNS servers: primary DNS – 10.254.254.1 and secondary DNS – 8.8.8.8.

If you want to reach an internal resource (WAN) with a local DNS server, make sure that your account's DNS is configured to use the local DNS. For example, users can only access the internal domain **images.mycompany.com** if your account is configured with your local DNS server or with DNS Forwarding. Otherwise, the DNS for that address will not be resolved.

For VPN users to connect to an Internet resource, such as www.catonetworks.com, the DNS settings for your account must contain at least one public DNS server. This server allows DNS resolution for the public Internet.

For more information on how to configure the DNS settings for your account, see [Configuring DNS Settings](/v1/docs/configuring-dns-settings).

### Geo-location restrictions block connectivity

Some Internet content is restricted based on the geographic location of the Cato Client. If you are physically located in a country with limited Internet access, then you can’t access the blocked content from that country.

For more information, see [Website Inaccessible due to Cato IP Blacklisting or Geo-Blocking](/v1/docs/website-inaccessible-due-to-cato-ip-blacklisting-or-geo-blocking).

## Slow Network Performance Due to DNS Resolution Outside Intended Path

**Challenge**

In Windows environments, users may experience slow application performance, DNS resolution failures, or VPN tunnel instability. These issues are commonly traced back to a feature called **Smart Multi-Homed Name Resolution**.

This feature sends DNS queries in parallel over all available network interfaces (e.g., Ethernet, Wi-Fi, VPN). The first DNS response is used, regardless of the source. While designed for speed, this can cause:

- DNS queries to bypass the VPN and resolve via public/local DNS
- VPN-based internal domain resolution to fail
- Unexpected delays or misrouted traffic

**Solution**

Disable Smart Multi-Homed Name Resolution to Enforce Interface-Based DNS Resolution : To ensure DNS queries are routed only through the intended adapter (typically the VPN tunnel), disable this Windows feature. This allows Windows to use DNS servers based on interface metrics and routing priority - a behavior that's critical for split tunneling and private/internal domain lookups.

**To disable:** Group Policy**:** Computer Configuration > Administrative Templates > Network > DNS Client > Turn off smart multi-homed name resolution → Enabled Or Via Registry: `[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\DNSClient]` `"DisableSmartNameResolution"=dword:00000001`

## GPO Rule Blocks Cato Adapter Installation

**Challenge**

A restrictive GPO policy may block the installation of the Cato Adapter during the installation or upgrade process of the Cato Client. GPO rules such as “Restricted installation of devices not described by policy” may block the adapter installation.

**Solution**

Allow the GPO policy to permit the installation of the Cato Adapter.
