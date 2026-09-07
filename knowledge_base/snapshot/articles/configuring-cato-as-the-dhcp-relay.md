---
title: "Configuring Cato as the DHCP Relay"
slug: "configuring-cato-as-the-dhcp-relay"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/configuring-cato-as-the-dhcp-relay"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Cato as the DHCP Relay

This article explains how to configure Cato as a DHCP relay for your account.

## Overview of Using Cato as a DHCP Relay

If your organization uses centralized DHCP servers (for example Microsoft DHCP servers), then you can configure Cato to relay DHCP messages to these servers. The DHCP relay configuration can be applied to the entire account, or to individual network ranges within a site.

Cato lets you define different groups of DHCP servers and then assign the appropriate DHCP server group to a network range.

## Defining the DHCP Relay Groups

Use the **Network > DHCP > DHCP Relay Settings** section to define destination DHCP servers. You can create multiple DHCP relay groups based on the requirements for your environment. For example, one group for a production environment and another one for a guest WiFi.

The same DHCP server can belong to multiple groups. You can define up to three separate servers for each DHCP relay group.

For groups with multiple DHCP servers, the Cato Socket relays the DHCP request to all the configured servers within the group. All the DHCP responses from the servers are sent back to the originating client.

**To define DHCP relay groups:**

1. From the navigation menu, click **Network > DHCP**.
2. Select the **DHCP Relay Settings** tab.
3. Click **New**. The **New DHCP Relay Group** panel opens.
4. Enter a **Name** for the new DHCP relay group.
5. Enter the IP address for the **DHCP Relay Servers**.
6. Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247989610141.png) (Add) to add the IP address for the server.
7. Repeat steps 5 and 6 for each DHCP relay server in this group.
8. Click **Apply**. The group is added.
9. Click **Save**. The group is saved.

## Configuring the DHCP Servers for Network Segments

You can define one of the following DHCP server settings for each Native Range and VLAN Range within a site:

- Account Default - the network uses the settings for the account that are configured in the **DHCP Relay** section (see below, [Configuring the DHCP Relay Settings for the Account](/v1/docs/configuring-cato-as-the-dhcp-relay#configuring-the-dhcp-relay-settings-for-the-account)).
- DHCP Range - enter an IP range that is assigned by the Cato DHCP server. Use this option when you want to use Cato as the DHCP server.
- DHCP Relay - select the DHCP relay group that you previously defined.

The DHCP Relay option is only available for X1500, X1600, and X1700 Sockets, and ESX vSockets that meet the minimum Socket version.

> [!NOTE]
> Note:
> 
> When you select the DHCP Range or Relay settings for a network segment, this overrides the DHCP Relay settings for the account.

The following screenshot is an example of a network configured to use the DHCP relay group, **DHCP-Group1**.

![DHCP_Relay_Group.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247989786269.png)

### Assigning the Account Default DHCP Settings to a Network Range

When you enable the **Account Default** option for the DHCP Setting for the network range in a site, then it uses the account level DHCP Relay settings.

- When you enable DHCP Relay for the account, the default DHCP Relay group settings are applied to the network range
- When DHCP relay is disabled for the account:
  - A network range configured for DHCP relay, receives no DHCP settings
  - A network range configured with a DHCP range, receives the DHCP settings

For more about configuring the account level DHCP settings, see below, [Configuring the DHCP Relay Settings for the Account](/v1/docs/configuring-cato-as-the-dhcp-relay#configuring-the-dhcp-relay-settings-for-the-account).

**To assign the Account Default DHCP settings to a network segment:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Networks**.
3. Select a network. The **Edit IP range** panel opens.
4. In **DHCP Range Type**, from the drop-down menu select **Account Default**.
5. Click **Apply**. The changes are updated.
6. Click **Save**.

### Assigning a DHCP Relay Group for a Network Range

When you select a **DHCP Relay** option for the DHCP Setting for the network segment in a site, select the DHCP Relay group for this network range. Cato relays the DHCP requests to servers within the configured group. For groups with multiple DHCP servers, the Cato Socket relays the DHCP request to all the configured servers within the group. All the DHCP responses from the servers are sent back to the originating client.

![Edit_IP_DHCP_Relay.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247966871709.png)

**To assign a DHCP Relay group to a network segment:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Networks**.
3. Select a network. The **Edit IP range** panel opens.
4. In **DHCP Type**, from the drop-down menu, select **DHCP Relay**.
5. In **DHCP Relay Group**, from the drop-down menu, select the DHCP Relay group for this network.
6. Click **Apply**. The changes are updated.
7. Click **Save**.

### Using Cato as the DHCP Server for a Network Range

When you select a DHCP Range for the DHCP Setting, the Cato DHCP server assigns DHCP settings to this network based on the IP range that you enter. The DHCP Relay settings aren't relevant for this option.

For more about using the Cato DHCP server, see [Configuring DHCP Settings](/v1/docs/configuring-dhcp-settings).

**To assign a DHCP range to a network segment:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Networks**.
3. Select a network. The **Edit IP range** panel opens.
4. In **DHCP Range Type**, from the drop-down menu, select **DHCP Range**.
5. Enter the range of IP addresses that the Cato DHCP server can assign.

You can use a single IP address, CIDR, or the first and last IP address of the range with a dash. For example, 10.11.1.0/28 or 10.11.1.5-10.11.1.10

> [!NOTE]
> Note:
> 
> You cannot use /32 CIDR blocks.
6. Click **Apply**. The changes are updated.
7. Click **Save**.

## Configuring the DHCP Relay Settings for the Account

You can use the **Account Default Setting** to configure the global DHCP Relay settings for the account. Select the DHCP Relay group that is used for the Account Default option. You can also configure the Relay Wait Time, which is how long Cato waits before relaying the DHCP requests to the servers in the group.

When you disable the DHCP Relay for the account, network ranges that are configured with the Account Default option don't receive DHCP services.

> [!NOTE]
> Note:
> 
> When you select the DHCP Range or Relay settings for a network segment, this overrides the DHCP Relay settings for the account.

**To assign the Account Default DHCP settings to a network segment:**

1. From the navigation menu, click **Network > DHCP**.
2. In the **Global DHCP Relay** section, click **Enabled**.
3. In **DHCP Relay Group**, select a DHCP relay group.
4. In **Relay Delay**, set the relay timeout for this DHCP relay group. The default value is 0 seconds.
  - To immediately send the DHCP requests enter **0**.
  - To configure the number of seconds that Cato waits to send the DHCP requests, enter between **1-90** seconds.
5. In the **DHCP Settings** column, from the drop-down menu select **Account Default**.
6. Click **Save**.
