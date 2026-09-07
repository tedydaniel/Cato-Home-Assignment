---
title: "Configuring DNS Settings"
slug: "configuring-dns-settings"
updated: 2026-07-20T07:20:03Z
published: 2026-07-20T07:20:03Z
canonical: "knowledge.catonetworks.com/configuring-dns-settings"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring DNS Settings

This article explains how to configure the Cato Management Application to work with private DNS servers and customized DNS suffixes for the entire account, and for specific sites, groups, and users.

## Overview of the Cato DNS Server

Cato can provide DNS services for your account and act as the DNS server. When a DNS query is sent from behind a Socket, IPsec site, or the Cato Client, the PoP intercepts, inspects, and tries to resolve the query using its own DNS cache. If there is no DNS cache entry for the query, the PoP forwards the query to one of its global trusted DNS servers.

You can define DNS settings and suffixes, and DNS forwarding configurations for your entire account. If required, you can also define custom DNS settings and suffixes for specific Sites, Groups, and User groups.

For more information about how DNS works with the Cato Cloud, see [What is Cato DNS?](/v1/docs/what-is-cato-dns).

## Defining DNS Server Settings and Suffixes for an Account

The DNS Settings page lets you configure private DNS servers for your account. You can also add DNS suffixes to the queries for LAN hosts and Cato Clients that are connected to Cato Cloud.

The DNS suffixes are configured via DHCP (where used), and Clients configure the device operating system's DNS suffixes. For example: two DNS suffixes myorganization.local and myorganization.com are configured in this order. When a user attempts to access a server named **storage**, the device operating system initially sends a DNS query for the name storage.myorganization.local.

If this name represents an existing server, a connection is made to that server. Otherwise, the operating system proceeds to query for storage.myorganization.com, and then tries storage.

**To define private DNS servers and DNS suffixes for your account:**

1. From the navigation menu, click **Network > DNS Settings**.

The **Settings & Suffix** tab is displayed.
2. Enter the IP addresses for the **Primary DNS** (required) and **Secondary DNS** (optional) servers.
3. **Optional:** In the **DNS Suffix** section, enter the suffix to append.
4. Click **Save**.

### Accepting DNS Requests Sent to Socket LAN (Native Range) Interface

For LAN hosts that have static IP settings, and the DNS server IP address is similar to the default gateway IP address (IP for the Socket LAN/Native Range interface), you can enable the Socket sites to accept DNS requests sent to the Socket LAN interface IP address. This is a global setting for the account, and you can choose to disable this setting for specific Socket sites.

When this setting is enabled, the Socket relays the DNS request packets to the connected PoP for further processing. All DNS requests are processed according to the DNS settings configuration (for example, DNS forwarding) defined for the account or site.

> [!NOTE]
> Note:
> 
> Accepting DNS requests sent to the Socket LAN interface is supported from Socket v16.0 and higher.

**To enable accepting DNS requests sent to the Socket LAN (Native Range) interface for the account:**

1. From the navigation menu, click **Network > DNS Settings**.

The **Settings & Suffix** tab is displayed.
2. Select **Accept DNS requests sent to Socket LAN interface IP**.
3. Click **Save**.

#### Disabling Accepting DNS Requests for a Specific Site

When the account is enabled to accept DNS requests sent to the Socket LAN interface, you can disable this setting for specific sites.

**To disable accepting DNS requests sent to the Socket LAN (Native Range) interface for a specific site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Advanced Configuration**.
3. Click the row for **Disable site DNS relay**.

The **Edit - Disable site DNS relay** panel opens.
4. Use the **Enabled** toggle to enable this setting. The toggle is green ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34730122493597.png) when enabled.
5. In **Value**, select **On**.
6. Click **Apply**.

## Customizing DNS Servers and Suffixes for CMA Entities

You can customize private DNS servers and set DNS suffixes for Cato Management Application (CMA) entities such as groups, specific sites, and hosts or users.

![dns-sitelevel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34730112988317.png)

### Hierarchy for Custom DNS Servers

You can configure the settings for DNS servers on different objects in the Cato Management Application, for example, settings for the entire account and for specific groups. If you are using DHCP options, these take precedence over and override the DNS settings for the account, group, site, or user.

When there is a conflict between these objects, the precedence is for the most specific object:

1. DCHP options for groups (highest precedence)
2. DHCP options for the account
3. DNS user-specific settings
4. DNS site-specific settings
5. DNS group settings
6. DNS account-level settings (lowest precedence)

### Customizing DNS Servers and Suffixes for Sites

You can improve network performance for sites based in different locations by configuring different internal DNS servers based on location. The Cato Cloud provides your hosts with fast and global DNS resolution that can significantly reduce DNS latency. Customizing the site's DNS servers to retrieve the DNS responses from the closest PoP can significantly improve efficiency and response time.

**To customize DNS settings for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > DNS**.

### Customizing DNS Servers and Suffixes for Groups

You can configure internal DNS servers for a group of objects. For example, all devices in the Finance_Servers group resolve DNS queries using internal DNS servers instead of the default system DNS.

**To customize DNS settings for a group:**

1. From the navigation menu, click **Resources > Groups** and select the group.
2. From the navigation menu, click **DNS**.

### Customizing DNS Server and Suffixes for Users and User Groups

One way to protect your corporate assets is to limit access and only use internal DNS servers. For example, you might want to use the default DNS servers for employees while having guests connect to a public network by configuring the DNS settings for the public group or User Group to only resolve from the public DNS servers.

Some users, for example, mobile or remote users, may need to connect directly to the Cato Cloud rather than through the account’s servers. In these cases, users might encounter connectivity problems or are unable to access internal resources. In addition, if you configure DNS settings for the site rather than for the individual users, users can’t access these internal resources in your domain. This is because the DNS server can’t resolve DNS queries for the Cato Client since they aren't connected to the site. You can easily resolve this issue by configuring the DNS settings for specific users.

For more information on customizing DNS settings for specific users or User groups, see [Centralized Management of SDP User DNS Settings](/v1/docs/centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy).
