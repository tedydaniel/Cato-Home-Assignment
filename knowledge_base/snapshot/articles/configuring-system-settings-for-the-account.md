---
title: "Configuring System Settings for the Account"
slug: "configuring-system-settings-for-the-account"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/configuring-system-settings-for-the-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring System Settings for the Account

The **System Settings** window lets you configure these settings:

- Default TCP acceleration
- Static range translation
- Configuration validation

![SystemSettings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247964518941.png)

## Configuring Default TCP Acceleration for Network Rules

You can define if TCP acceleration should be enabled by default for network rules.

- For a description of acceleration in the Cato Cloud, see [Accelerating and Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic).
- For information on overriding the acceleration default setting in network rules, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

You always have the option to change the default acceleration settings for network rules.

> [!NOTE]
> Note:
> 
> TCP acceleration does not affect non-TCP traffic (UDP-based traffic) that is part of a network rule).

**To enable TCP acceleration by default in network rules:**

1. From the navigation menu, click **Resources > System Settings**.
2. In the **Default Acceleration Settings** section, select from these options:
  - **TCP Proxy for Internet** - Enables acceleration by default for new Internet network rules
  - **TCP Proxy for WAN** - Enable acceleration by default when WAN network rules are created.
3. Click **Save**.

## Configuring Static Range Translation

In general, we recommend that all sites in your account use unique network ranges for optimal troubleshooting and avoiding route loops. However, sometimes there are two or more sites that use identical IP address ranges. For example, this is common in hub-and-spoke topologies where multiple branches need to access a shared data center but do not need to communicate with each other.

Since Cato "flattens" the network and eliminates inter-LAN NAT commonly used by older solutions, IP range duplication is, in principle, prohibited. However, you can keep duplicate IP ranges when needed by activating **Static Range Translation**. This performs a many-to-many translation for specific networks.

> [!NOTE]
> Note:
> 
> To enable overlapping networks to communicate with each other, they must be translated by activating and configuring **Static Range Translation** on all relevant networks.

### Using Static Range Translation with the Cato Cloud

In a translated network, the translation occurs at the Cato PoP to which the site is connected. This means that hosts within the network keep using their real IPs, but traffic between them and hosts outside this network uses their translated IPs.

If you define static hosts in this network, the Cato Management Application automatically displays the translated IP for these hosts, in case it needs to be reached from outside the local network.

> [!NOTE]
> Note:
> 
> All other configuration options in the Cato Management Application that are not specific to this network (such as groups, firewalls, network rules, and so on) are only aware of the translated IPs. All references (such as analytics and event logs) to this network and its hosts always use the translated IPs.

First enable static range translation for your account, and then configure the translated IPs for the relevant network ranges.

### Enabling Static Range Translation

> [!NOTE]
> Important:
> 
> - Do not use static range translation on network ranges that include AD or DNS servers, or where FTP or SIP protocols are used
> - After enabling static range translation for your account, Alt. WAN recovery, Alt. WAN and off-cloud transport, and WAN recovery are automatically disabled for sites that define a static NAT for the native range
> - BGP isn't supported for accounts that use static range translation

**To enable static range translation:**

1. From the navigation menu, click **Resources > System Settings**.
2. In the **Static Ranges Translation** section, select **Enable static range translation**.
3. Click **Save**.

### Defining Static Range Translation

After you enable static range translation for the account, configure the translated IP range for the network rules. The default translated IP range is the same as the real IP range.

- The real and translated ranges must have the same CIDR notation
- The translated range must be unique and you cannot use it in other places in the account![Static_NAT.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247978826525.png)

**To define static range translation:**

1. From the navigation menu, click **Network > Sites**.
2. From the list of sites, select the site you are defining the static range translation settings.
3. From the navigation menu, click **Site Configuration > Networks**.
4. Click the IP range **Type** to edit it. The **Edit IP range** panel opens.
5. In **Static NAT**, enter the translated IP address range for this network IP range.
6. Click **Apply**. The **Edit IP Range** panel closes.
7. Click **Save**.

## Enabling Public IP Addresses in Your Site (Configuration Validation)

If your organization uses public IP ranges inside your organization LAN, you need to disable the **Prevent use of public IP addresses and ranges in sites** option so that the IP address validation mechanism allows this.

**To allow the use of public IP addresses in your site:**

1. From the navigation menu, click **Resources > System Settings**.
2. In the **Configuration Validation** section, clear the **Prevent use of public IP addresses and ranges in sites** option.
3. Click **Save**.

## Disabling Site Degraded Status

Degraded connectivity status indicates when a Socket or port are experiencing some issues. You can also choose to display the Degraded status only for sites with issues that occurred within the past 30 days. Sites whose issues are older than 30 days will then appear as Connected.

When disabled, Degraded status is not shown on relevant pages.

**To toggle the site Degraded status:**

1. From the navigation menu, click **Resources > System Settings**.
2. In the **Site Degraded Status** section, use the toggle to enable or disable the Degraded status (green is enabled, grey is disabled).
3. **(Optional)** To make sure that Degraded status is only shown for recent issues, select **Don't trigger a Degraded Status for failures that were detected more than 30 days ago**.
4. Click **Save**.

## Sharing Advanced Device Analytics

You can choose whether to share advanced device analytics with Cato to help improve product quality and support. This setting lets you control the sharing of enhanced device usage analytics without impacting traffic processing or consuming additional SKU resources. Data includes, for example, CPU usage percentage and Wi-Fi signal strength.

**To toggle the Share Advanced Device Analytics setting:**

1. From the navigation menu, click **Resources > System Settings** and select the **System** tab.
2. In the **Share Advanced Device Analytics** section, use the toggle to enable or disable sharing (green is enabled, grey is disabled).
