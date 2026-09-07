---
title: "Managing the Socket Next Gen LAN Firewall Policy"
slug: "managing-the-socket-next-gen-lan-firewall-policy"
updated: 2026-07-27T12:47:50Z
published: 2026-07-27T12:47:50Z
canonical: "knowledge.catonetworks.com/managing-the-socket-next-gen-lan-firewall-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing the Socket Next Gen LAN Firewall Policy

This article explains how to configure Socket Next Gen LAN Firewall rules to route and control site traffic locally in the Socket. For more about the Socket Next Gen LAN Firewall, see [What is the Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall).

## Overview

Configure LAN Network rules to define the traffic to be routed locally with LAN transport, then create related LAN Firewall rules to enforce the security policy for the traffic.

This is an example high-level workflow for configuring the policy:

1. Determine which sites require Layer 7 enforcement capabilities and configure them in the policy.

This enables Layer 7 enforcement for LAN Firewall rules, as well as events with Layer 7 data for the site.
2. Monitor Socket CPU performance and events for the sites to assess the impact of enabling Layer 7.
3. Create LAN Network rules to define which site traffic is routed locally through the Socket instead of through the WAN.
4. (Optional) Partition the policy into sub-policies to delegate management of specific rules to different admins.
5. For each LAN Network rule, create LAN Firewall rules to enforce the security policy for the traffic.

## Enabling Layer 7 Capability for a Site

Enable Layer 7 inspection capabilities for traffic for a site. After enabling, the Socket performs deep packet inspection on traffic whether or not a LAN Firewall rule is configured, as long as there is traffic defined to use LAN transport (see [What is the Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall)). This means that Layer 7 data appears in events for the site traffic, including fields such as Application, App Risk, and Custom App. This also impacts the Socket CPU usage.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(83).png)

**To enable Layer 7 capability for a site:**

1. From the navigation menu, click **Security > LAN Firewall**.

The LAN Firewall page opens to your existing unpublished revision, or to the newest published revision.
2. Select the **Layer 7 Sites** tab.
3. Click **New**. The **Add Site** panel opens.
4. Under **Site**, select one or more sites from the drop-down list of Socket sites.
5. Click **Apply**. The site is added to the list of Layer 7 sites.
6. Click **Save**. Layer 7 functionality is configured for the site.

## Creating LAN Network Rules

Create a new LAN Network rule and configure the settings to define the transport for the traffic. For rules defined with LAN transport, you can add LAN Firewall rules to manage access control for the traffic. For more information, see below [Creating LAN Firewall Rules](/v1/docs/managing-the-socket-next-gen-lan-firewall-policy#h_01KTVD8DEY2Y9NVY2A8QPH7YKB).

![LAN_Firewall.png](https://support.catonetworks.com/hc/article_attachments/26784695484957)

**To create a LAN Network rule:**

1. From the navigation menu, click **Security > LAN Firewall**.

The LAN Firewall page opens to your existing unpublished revision, or to the newest published revision.
2. Click **New** and from the drop-down menu select **New LAN Network Rule**. The **New Network Rule** panel opens.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider (green is enabled, grey is disabled).
5. Configure the **Position** and **Direction** for the new rule.

  - By default, the rule is applied in one direction, from the source **To** the destination. Click the **Direction** drop-down menu to set the rule to operate in **Both** directions.
6. Expand the **Site** section and select one or more sites or site groups that the rule applies to. The default value is **Any**.
7. Expand the **Source** section and select one or more objects for the traffic source for this rule.
  1. Select the type (for example: Host, Network Interface, IP, User, User Group, Any). The default value is **Any**.
  2. When needed, select a specific object from the drop-down list for that type.
8. Expand the **Destination** section and select one or more destination objects for this rule.
  1. Select the type (for example: Host, Network Interface, IP, User, User Group, Any). The default value is **Any**.
  2. When needed, select a specific object from the drop-down list for that type.
9. Expand the **Criteria** section and add the device conditions to the rule. For more information, see [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules). The default values are **Any**. **Note:** Criteria for LAN Firewall are supported from Socket version 26 and higher.
10. Expand the **Service/Port** section, and select the protocols that the rule applies to with one of the following options:

  - **Simple Service** - Select the relevant Layer 4 services from the list.

The predefined services list is based on the RFC definition of each service.
  - **Custom Service** - Enter the relevant port and protocol in the "Protocol/Port" format (e.g. TCP/80-88, UDP/53, ICMP)

The default value is **Any**.
11. **(Optional)** Expand the **NAT** section to enable NAT on the outgoing interface. This translates all originating IPs to one NAT IP.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/img-fb0d2b0869a62683969be81adc74de3a.png)
12. Select the **Transport** for traffic matching the rule. The options are:

  - **LAN** - The traffic is routed locally by the Socket and not sent to the PoP
  - **WAN** - The traffic is sent over the WAN to the PoP for inspection
13. Click **Save**.

The changes are saved to your unpublished revision and are available for editing until they are published or discarded.

## Creating LAN Firewall Rules

Create a new LAN Firewall rule and configure it to manage traffic access control. A LAN Firewall rule can only be configured with objects within the scope of its parent LAN Network rule.

Rules for sites enabled with Layer 7 capabilities can include conditions with application layer objects such as **Application** and **Domain**. If rules for sites without Layer 7 capabilities include these objects, the rules won't function properly.

**Note:** Traffic within the same site that doesn't match a LAN Firewall rule is considered WAN traffic, even if it travels to the PoP and back to the same site.

> [!NOTE]
> Note:
> 
> For guidance about how to use **User** and **User Group** objects in the **Source** and **Destination** fields, or for using device criteria in a rule, contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com).

**To create a LAN Firewall rule:**

1. From the navigation menu, click **Security > LAN Firewall**.

The LAN Firewall page opens to your existing unpublished revision, or to the newest published revision.
2. Click **New** and from the drop-down menu select **New LAN Firewall Rule**. The **New Firewall Rule** panel opens.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider (green is enabled, grey is disabled).
5. Configure the **Position** for the rule, and from the **Rules** drop-down select the relevant reference rule, as follows:

  - For the **Before Rule** and **After Rule** options, select from the **Rules** drop-down a LAN Firewall rule under the relevant LAN Network rule.
  - For the **First in Rule** and **Last in Rule** options, select from the **Rules** drop-down the parent LAN Network rule for this rule.
6. Configure the **Direction** for the rule.

  - By default, the rule is applied in one direction, from the source **To** the destination. Click the **Direction** drop-down menu to set the rule to operate in **Both** directions.
7. Expand the **Source** section and select one or more objects for the traffic source for this rule.
  1. Select the type (for example: Host, Network Interface, IP, User, User Group, Any). The default value is **Any**.
  2. When needed, select a specific object from the drop-down list for that type.
8. Expand the **Destination** section and select one or more destination objects for this rule.
  1. Select the type (for example: Host, Network Interface, IP, User, User Group, Any). The default value is **Any**.
  2. When needed, select a specific object from the drop-down list for that type.
9. Expand the **App/Category** section and select one or more applications for the rule.

When there is more than one App/Category object in a rule, there is an OR relationship between them. The default value is **Any**.

**Note:** Only configure App/Category objects for rules for sites with Layer 7 capabilities enabled. Otherwise, the rule won't function properly.
10. Expand the **Service/Port** section, and select the protocols that the rule applies with one of the following options:

  - **Simple Service** - Select the relevant Layer 4 services from the list

The predefined services list is based on the RFC definition of each service.
  - **Service** - Select the relevant Layer 7 services from the list
  - **Custom Service** - Enter the relevant port and protocol in the "Protocol/Port" format (e.g. TCP/80-88, UDP/53, ICMP)

The default value is **Any**.
11. Select the **Action** for this rule. The options are **Allow** and **Block**.
12. **(Optional)** Configure tracking options to generate **Events** and **Send Notification**. The frequency starts counting after the first notification is sent.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
13. Click **Save**.

The changes are saved to your unpublished revision and are available for editing until they are published or discarded.

### Using Sub-Policies and RBAC for the LAN Firewall Policy

The LAN Firewall policy supports sub-policies so that you can delegate management of a defined set of rules to specific admins, while keeping centralized control and security boundaries for the rest of the policy. Create sub-policies for specific rules, and define which admins have view or edit access to those sub-policies.

A LAN Firewall policy is made up of a main policy and any number of sub-policies. Any rules that are not inside a sub-policy belong to the main policy when you define admin permissions.

#### Creating a Sub-Policy

Configure the sub-policy and its permissions before you enable the scoping rule, so that the rules and access are in place before enforcement starts. Note: Make sure you define rules and permissions before you enable the sub-policy.

**To create a sub-policy:**

1. In the LAN Firewall policy, click **New > Sub-Policy**.
2. Define the **Name**, **Position**, and conditions (the scoping rule) for the sub-policy.
3. Click **Save**. Leave the scoping rule disabled until the rules and permissions for the sub-policy are configured.

#### Defining Admin Permissions for Sub-Policies

By default, admins have permissions to view and edit all sub-policies on every page that they have permissions for. To restrict an admin to a specific sub-policy, remove the permission for all LAN Firewall sub-policies and add it back for the individual sub-policy.

**To define admin permissions on a sub-policy:**

1. From the navigation menu, select **Administration > Admins**.
2. Select an admin, and go to the **Access Permissions for Entities** area.
3. In the table, locate the line for **All LAN Firewall Policies** and remove the view and edit permissions.
4. In the drop-down, select **LAN Firewall Sub-Policies**.
5. In the second drop-down, select the target sub-policy. The sub-policy is added to the table.
6. In the table, give the admin **Edit** or **View Only** permissions for the sub-policy.
7. Repeat this process for every admin.

After the admin permissions are defined, the assigned admins can configure rules for the sub-policy.

#### Configuring Rules in the Sub-Policy

Add the LAN Network rules and LAN Firewall rules for the sub-policy in the same way as for the main policy (see [Creating LAN Network Rules](/docs/managing-the-socket-next-gen-lan-firewall-policy#h_01KTVD8DEYFZ3KWHQSVAPX7F5D) and [Creating LAN Firewall Rules](/docs/managing-the-socket-next-gen-lan-firewall-policy#h_01KTVD8DEY2Y9NVY2A8QPH7YKB)). Learn about the rule behavior that is specific to sub-policies [here](/v1/docs/what-is-the-socket-next-gen-lan-firewall#lan-firewall-rules).

#### Enabling the Sub-Policy

After the rules and permissions are defined, enable the sub-policy.

To enable a sub-policy:

1. In the LAN Firewall policy, select the sub-policy.
2. Expand the **General** section and use the toggle to enable it.
3. Publish your changes.

## Monitoring and Events

You can optionally enable event tracking for each defined rule in the Next Gen LAN Firewall policy.

> [!NOTE]
> Note:
> 
> LAN firewall traffic will not be visible in app and network analytics dashboards.

The events appear under **Site Monitoring > Events**.

- **Event Type** - Security
- **Sub-Type** - LAN Firewall

**To filter for LAN Firewall events:**

1. Go to **Home** > **Events**.
2. Click on **Filter** and select the relevant field, operator and value.

  1. **Field** - Multiple fields can be selected as a filter. For example we may opt to filter for "Source site" or "Sub-Type" (LAN Firewall)
  2. **Operator** - Choose to include or exclude specific values (**Is**, **Is not**) or multiple values (**In**, **Not in**), for example "Source site" with operator "**In**" allows to select multiple source sites as values.
  3. **Value** - The value for the field.
3. Click **Add filter**.

![image.png](https://support.catonetworks.com/hc/article_attachments/26784695552541)

![image.png](https://support.catonetworks.com/hc/article_attachments/26784661319581)

In the following example, you can see the details for a LAN Firewall event.

- **Action** - Block or Monitor. (Traffic was blocked or allowed locally by the LAN Firewall)
- **Configured Host Name** - Additional host information on the source IP, if available.
- **Sub-Type** - LAN Firewall. All events generated by the LAN Firewall will have this sub-type.
- **Network Rule** - The parent LAN Network rule for the LAN Firewall rule that generated the event.
- **Rule Name** - The name of the LAN Firewall rule that generated the event.

![LAN_FW_L7_Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image-1785061816823.png)

Unlike the WAN or Internet Firewall, where events are generated by the Cato PoP, LAN Firewall events are generated on the Socket itself. These events are sent over the site tunnel to be stored in the Cato Management Application.

All flow traffic over the tunnel is prioritized before LAN Firewall events, which have a default QoS priority of 255 and may generate additional overhead.

Cato recommends tracking only high-priority LAN Firewall rules to avoid additional overhead over the tunnel.
