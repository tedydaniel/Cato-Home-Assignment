---
title: "Working with Link Health Rules"
slug: "working-with-link-health-rules"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/working-with-link-health-rules"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Link Health Rules

This article discusses how to configure health rules to send email notifications for connectivity or link quality issues.

## Overview

Use the **Health Rules** page to configure the Cato Management Application (CMA) to send notifications when there are issues related to link connectivity or quality during the configured amount of time. For connectivity rules, you can define the scope for objects that trigger an email notification for connectivity issues. For quality rules, define the objects that are monitored for link quality threshold on one or more interfaces. In addition, you can select which types of quality categories trigger email notifications.

Health Rules is not an ordered policy, and multiple rules can match for a single issue.

## Managing Health Rules

The following sections explain how to create, enable, and manage health rules.

### Configuring a Connectivity Health Rule

> [!NOTE]
> Notes:
> 
> - For accounts that do not currently have users and user groups in Connectivity Health Rules, as of November 3, 2024, they will not be able to define them as the **Source**.
> - From January 2, 2025, users and user groups can no longer be defined as a **Source** in Connectivity Health Rules.
> 
> For more information, see this [article](/v1/docs/users-user-groups-can-no-longer-be-included-as-source-in-connectivity-health-rul).

You can set conditions for the rules (such as only send an alert if the issue persists for a specific duration or if the issue occurs repeatedly), as well as set different rules for one or more connectivity **Condition** issues (such as failover, passive disconnect, disconnect). When you define multiple **Conditions**, there is an OR relationship between them.

For connectivity health rules that include sites, we recommend that you do not use the **Any** option. Sites can generate many notifications because users and groups are regularly disconnecting and connecting.

![ConnectivityHealthRule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28981023256733.png)

**To configure a Connectivity Health Rule:**

1. From the navigation menu, click **Network > Link Health Rules**.
2. From the **Connectivity Health Rules** tab or section, click **New**.

The **New Connectivity Health Rule** panel opens.
3. Configure the **General** settings for the rule:
  1. Enter a **Name** for the rule.
  2. Click the slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28981020764445.png) to make sure that the rule is enabled.
4. Configure the **Source** settings for the rule:
  1. Select the type (for example: site or group).
  2. When needed, select a specific item from the drop-down list for that type.
5. Configure the **Condition** settings (the **On** column) for this rule:
  1. In **On**, select one or more connectivity items that trigger the rule:
    - **Any** - Any type of connectivity issue
    - **Failover** - Failover between primary and secondary links, or vice-versa.
    - **Active WAN Link Disconnect** - Link(s) in active state disconnected.
    - **Passive WAN Link Disconnect** - Link(s) in passive or last resort state are disconnected.
    - **Socket Failover** - Failover between Sockets in HA configuration.
    - **Internet as a Transport** - Disconnection for links transporting data over the Internet (and not the Cato Cloud).
    - **LAN Port Disconnect** - A LAN port is disconnected.
    - **Alt. WAN Disconnect** - Link used for recovery via Alt. WAN is disconnected.
    - **HA Not Ready** - One of the Sockets in an HA configuration is disconnected or both Sockets report as the primary Socket.
  2. In **Alert Upon**, you can define the time duration or number of connectivity issues that trigger the rule:

> [!NOTE]
> Notes:
> 
> - The **Alert Upon** settings are evaluated as an OR relation.
> - By default, the health rule engine checks for a duration of 2.5 minutes to determine if an event matches a rule. If you configure a **Link Down Duration** for the rule of less than 2.5 minutes, this can impact the content of the notification. For example, if a Duration of 1 minute is configured for an Active WAN Link Disconnect rule, then the rule will be matched after the active link is disconnected for 1 minute. But this can result in two different notifications, as follows:
>   - If the active link is disconnected for more than 1 minute and remains disconnected for more than 2.5 minutes - the notification will be for a **Disconnect**
>   - If the active link is disconnected for more than 1 minute, but reconnects before 2.5 minutes - the notification will be for a **Co****nnect** alert (the event related to the alert may also appear as a **PoP Change** or **Reconnect** event)
> - When **Occurrences** are set for a disconnect rule (e.g. **Active WAN Link Disconnect** or **Passive WAN Link Disconnect)**, PoP changes and session reconnects are not counted as occurrences. Only disconnects are counted.
> - When alerts are triggered by **Occurrences** conditions in an **Active WAN Link Disconnect** or **Passive WAN Link Disconnect** rule, a Connected alert will not be sent when the link is back up
> - When the **Condition** is set for **Active WAN Link Disconnect** or **Passive WAN Link Disconnect**, the rule sends a Connected alert after the link is back up for 30 seconds in the following cases:
>   - There are no Alert Upon conditions set
>   - If only a Link Down Duration condition is set
>   - If both Link Down Duration and Event Occurrences conditions are set, as follows:
>     - If the Link Down Duration condition triggers an alert, a Connected alert will be sent when the link is back up for 30 seconds
>     - If the Event Occurrences condition triggers an alert, a Connected alert will not be sent when the link is back up
    - For disconnect conditions, you can define the **Link Down Duration** - the time that the link or connection is disconnected before triggering the rule.
    - In **Event Occurrences**, you can define how often the connectivity issue occurs before triggering the rule.
6. **(Optional)** Configure the **Tracking** options to **Send Notification**.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
7. Click **Apply**. The new rule is added to the rulebase.
8. Click **Save**. The Connectivity Health rules are saved to your account.

### Example Connectivity Health Rules and Behaviors

This section provides examples to illustrate the alert behavior of various types of Connectivity Health Rules.

#### Example 1 - Disconnect Rule with No Alert Upon Conditions Configured

![Connectivity_Health_-_Example_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29150400787869.png)

Rule configuration - **Active WAN Link Disconnect** and **Passive WAN Link Disconnect** conditions, with no Alert Upon conditions configured.

Rule behavior -

- Trigger a Disconnected alert if a link is down for over 2.5 minutes
- Trigger a Reconnected alert if there is a disconnection and reconnection within 2.5 minutes

**Note:** The Reconnect event may be detected with up to a 30-second delay after the connection is restored.
- Trigger a Connected alert after the link is back up for 30 seconds

#### Example 2 - Disconnect Rule with a Link Down Duration Condition Configured

![Connectivity_Health_-_Example_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29150367818909.png)

Rule configuration - **Active WAN Link Disconnect** and **Passive WAN Link Disconnect** conditions, with a Link Down Duration condition configured as **Down Over** 1 minute.

Rule behavior -

- Trigger a Disconnected alert if a link is down for over 1 minute
- No Reconnected alert is triggered if the link reconnects within 2.5 minutes
- Trigger a Connected alert after the link is back up for 30 seconds

#### Example 3 - Disconnect Rule with an Event Occurrences Condition Configured

![Connectivity_Health_-_Example_3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29150387974173.png)

Rule configuration - **Active WAN Link Disconnect** and **Passive WAN Link Disconnect** conditions, with an Event Occurrences condition configured for 4 times in 60 minutes.

Rule behavior -

- Trigger an alert if a link had 4 Disconnected/Reconnected/PoP Changed events in 60 minutes
- An alert is only sent for the 4th occurrence. For example, if the 4 occurrences in order were PoP Changed, Reconnected, PoP Changed, Disconnected - only a Disconnected alert is sent

#### Example 4 - Disconnect Rule with Link Down Duration and Event Occurrences Conditions Configured

![Connectivity_Health_-_Example_4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29150400828317.png)

Rule configuration - **Active WAN Link Disconnect** and **Passive WAN Link Disconnect** conditions, with a Link Down Duration condition configured as **Down Over** 1 minute, and an Event Occurrences condition configured for 1 time in 1 hour.

Rule behavior - Since there is an OR relationship between the Link Down Duration and Event Occurrences conditions, this rule results in two separate behaviors, as follows:

**Behavior for Link Down Duration condition -**

- Trigger a Disconnected alert if a link is down for over 1 minute
- No Reconnected alert is triggered if the link reconnects within 2.5 minutes
- Trigger a Connected alert after the link is back up for 30 seconds

**Behavior for Event Occurrences condition -**

- Trigger an alert if there is at least one Disconnected/Reconnected/PoP Changed event in an hour

## Monitoring Link Quality with Health Rules

Quality Health Rules let you monitor the link quality between the site and the Cato Cloud. When the quality does not meet a threshold during the configured time frame, the CMA sends a notification. A second notification is sent after the link quality returns to comply with the threshold for a specific time period.

You can define the scope of a rule for specific sites or groups. In addition, define which links are monitored for interfaces on sites with Sockets and IPsec connections. You must configure at least one quality threshold to trigger an email alert according to these categories:

| Direction | Traffic that is upstream, downstream, or both |
| --- | --- |
| Packet Loss | Percentage of transmitted packets |
| Distance (msec) | Milliseconds that it takes a packet to travel between the source and the PoP |
| Jitter (msec) | Delay in milliseconds between packets |
| Congestion | The volume of packets exceeds the available link capacity, leading to network congestion Congestion is measured across all bandwidth priorities and is triggered if there are more than 1% of discarded packets for the configured **Duration** for the rule. |

When you select more than one quality threshold, they are evaluated with an OR relationship.

Cato recommends that you have separate link health rules for each link. This ensures that if both the primary and secondary links are disconnected within the same period, you will receive separate notifications for the disconnect and reconnect events.

### Configuring a Link Quality Health Rule

Configure a quality health rule to monitor the quality of the links between sites and objects in your account and the Cato Cloud. When you define multiple **Thresholds**, there is an OR relationship between them.

The **Condition** of a link quality health rule defines the thresholds that are monitored for the link. For example, if the **Threshold** is set to a **Distance** of 100ms, and the **Alert Upon** is set to 50% minutes over a 10-minute time frame, this means that the link is suffering from poor distance quality for a total of 5 minutes during the total 10 minutes. If the issue occurs during the first 2 minutes and then after 1 minute of good link health, the issue occurs for another 3 minutes, then an event is generated, and a notification is sent (according to the rule settings).

![QualityHealthRule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28980987271709.png)

**To configure a Health Rule to monitor the link quality:**

1. From the navigation menu, click **Network > Link Health Rules**.
2. From the **Quality Health Rules** tab or section, click **New**.

The **New Quality Alert** panel opens.
3. Configure the **General** settings for the rule:
  1. Enter a **Name** for the rule.
  2. Select the traffic **Direction** that triggers the rule: **Any**, **Upstream**, or **Downstream**.
  3. Click the slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28981020764445.png) to make sure that the rule is enabled.
4. Configure the **Source** settings for the rule:
  1. Select the type (for example: site or group).
  2. When needed, select a specific item from the drop-down list for that type.
5. In the **Network Interface** section, select one or more interfaces for the rule.

To apply the rule to all the interfaces, select **Any**.
6. In the **Condition** section, define the link quality conditions that trigger the rule:
  1. Select one or more **Thresholds**, and configure the quality value for each threshold.
  2. Define the **Link Down Duration** settings for how long the quality issue for the link continues.
  3. In **Clear Event**, set how long to wait before sending the All Clear email notification.
7. Configure the **Tracking** options to **Send Notification**. **Note:** If the **Send Notification** option is disabled, the rule does not generate notifications or events.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
8. Click **Apply**. The new rule is added to the rulebase.
9. Click **Save**. The Quality Health rules are saved to your account.

## Configuring Alert and Notification Options

The **Track** option lets you create alerts that are triggered by different rules, such as firewall rules, remote port forwarding rules, health alerts and more. For some rules, such as firewall rules, you can choose to generate notifications when the rule is matched.

The **Frequency** defines how often notifications can be generated by the system. Each occurrence only generates a single alert.

**To configure alerts and notifications for a rule:**

1. In the **Tracking** section, select **Send Notification**.
2. In the **Frequency** section, configure how often a notification is sent to the recipients as follows:
  - **Immediate** - Send notification for every occurrence.
  - **Hourly** - Send notification with the first occurrence. Do not send additional notifications if there are more occurrences within an hour.
  - **Daily** - Send notification with the first occurrence. Do not send additional notifications if there are more occurrences within a day.
  - **Weekly** -Send notification with the first occurrence. Do not send additional notifications if there are more occurrences within a week.
3. In **Send notification to**, select the **Subscription Group** , **Mailing List** or **Integration** and select the relevant item.
4. Click **Apply**, and then click **Save**.
