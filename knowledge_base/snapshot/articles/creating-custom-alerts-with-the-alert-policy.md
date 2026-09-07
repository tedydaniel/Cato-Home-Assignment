---
title: "Creating Custom Alerts with the Alerts Policy (EA)"
slug: "creating-custom-alerts-with-the-alert-policy"
updated: 2026-08-04T08:27:52Z
published: 2026-08-04T08:27:52Z
canonical: "knowledge.catonetworks.com/creating-custom-alerts-with-the-alert-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Custom Alerts with the Alerts Policy (EA)

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

## Overview

The Alerts Policy lets you create custom, threshold-based rules that determine when an Alert is generated. This helps you identify potential indicators of attack, investigate abnormal activity, and respond before network performance, security, or user experience is impacted. Based on your network or security requirements, you define the conditions that matter most to your organization and receive an alert if they are met.

You can build Alerts around a wide range of occurrences across SD-WAN, Security, Digital Experience Monitoring (DEM), and other areas of your network. For each rule, you define the scope that the Alert applies to, the trigger that generates it, and the time window over which the condition is evaluated. You then choose what happens if the occurrence takes place. The Alert can generate an Event, a Notification, or both.

As Cato collects data from many domains across your network, there are a vast number of possible configurations for a rule. To help you configure rules for your organization, the Alerts Policy includes:

- **Predefined Rules:** Suggested alert rules that you can enable or disable
- **Templates:** Include only the metrics relevant to a specific monitoring scenario. Select a template that matches your use case to configure alert conditions and thresholds without searching through all available data sources. For example, the Device Posture template only displays Device ID, User ID, and Site ID as the scope for a rule.

### Use Case - Preventing Performance Degradation

Company ABC’s London site regularly runs bandwidth-intensive operations, and the network team has noticed that unusually high volumes of concurrent flows from this site often precede performance degradation for business-critical applications.

To be informed before users are impacted, the network administrator creates an Alerts Policy rule for the London site with the Site Connectivity template and sets a threshold based on the Site’s typical traffic volume. The rule is configured to send a notification.

When the number of concurrent flows at the London Site exceeds the threshold, a notification is sent alerting the network team so they can investigate or take action before application performance is affected. This helps Company ABC focus on conditions that are relevant to its environment while reducing unnecessary Events and Notifications.

### Understanding Alerts, Events, and Notifications

The Cato Management Application (CMA) generates Alerts and Events and sends Notifications. Although related, they are different notification mechanisms.

- **Alert:** A rule-based condition defined in the Alerts Policy. When the criteria are met, the alert generates an event, sends a notification, or both
- **Event:** Visible in the CMA, Events record detailed information about an occurrence in your network for investigation and analysis. For more information, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network)
- **Notification:** A proactive message sent outside the CMA to inform you about something that occurred in your environment. For more information, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications)

## Enabling the Alerts Policy

Create Alerts Policy rules to define the monitored scope, trigger conditions, evaluation window, and tracking actions for alerts.

### Understanding the Sections in an Alerts Policy Rule

Rules in the Alerts Policy contain these sections:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(63).png)

****General****

Configure general details about the rule, such as the Rule name, Description, and severity of the Alert.

In the General section, you can choose a template to help you configure the Rule.

****Scope****

This section defines where the rule applies and which data is evaluated. If a template is selected, you can apply the rule to all relevant entities or limit it to specific objects in your environment. Only the data within the defined scope is evaluated by the rule.

The scope is defined by selecting the **Data Source**, **Scope**, and applying **filters**.

****Triggers****

The **Trigger** defines the condition that must be met for an Alert to be generated. The trigger is evaluated against the data in the defined scope, and when the conditions are met an Alert is generated. For example you can trigger an alert when:

- Socket CPU is greater than 90% and the Experience Score is Low
- A user failed to authenticate 10 times within 10 minutes
- 1000 users were disconnected in 5 minutes

****Time Window****

The **time window** defines the period of time evaluated to determine whether the trigger conditions are met before an Alert is generated. It helps ensure that an Alert is generated based on activity over a meaningful period, rather than a brief or isolated change.

There are two **Window Types**:

- **Sliding:** Continuously evaluates the trigger condition over a rolling period of a fixed length. As new data becomes available, the window moves forward and the trigger is reevaluated. For example, a five-minute sliding window always evaluates activity from the previous five minutes.
- **Periodic:** Evaluates data in fixed, consecutive time periods. The trigger is evaluated after each completed period. For example, a one-hour periodic window evaluates activity from 10:00–11:00, then 11:00–12:00.

Both Window Types have the option to **Generate Clear.** This determines whether a second Alert is generated when the trigger conditions are no longer met. This indicates that the monitored metric no longer meets the alert condition. For example, if an Alert is generated when concurrent flows exceed a configured threshold, a Clear Alert is generated when the number of flows falls below that threshold according to the selected time window.

****Tracking****

This defines what happens when the Alert conditions are met. Configure the rule to generate an **Event**, send a **Notification**, or perform both actions.

Notifications can be sent to a Subscription group, mailing list, or webhook integration. For more information, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).

### Configuring the Alerts Policy

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(62).png)

**To configure Alerts Policy rules:**

1. From the navigation menu, select **Account > Alerts**.
2. Click **New** then **New Rule**.
3. Configure the **General**, **Scope**, **Triggers**, **Time Window**, and **Tracking** sections to meet your requirements.
4. Click **Save** and then **Publish**.
5. Set the **Alerts** toggle to Enabled.
