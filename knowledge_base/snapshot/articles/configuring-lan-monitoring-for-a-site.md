---
title: "Configuring LAN Monitoring for a Site"
slug: "configuring-lan-monitoring-for-a-site"
updated: 2026-07-13T12:09:15Z
published: 2026-07-13T12:09:15Z
canonical: "knowledge.catonetworks.com/configuring-lan-monitoring-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring LAN Monitoring for a Site

## Monitoring Internal Servers and Hosts in the LAN

The **LAN Monitoring** screen lets you send ICMP packets to monitor if specific hosts in the LAN for a site are running. If the server or host fails to respond to the specified number of ICMP tests, it is considered down and an event is generated that the host is unreachable. When the host recovers and responds to an ICMP test, a second event is generated that the host is now reachable. You can also choose to send an email notification when a host is unreachable, or recovers.

You can limit the time that a LAN monitoring rule actively monitors the server and generates events or sends email notifications. For example, the rule is only active during the working hours configured for the account.

> [!NOTE]
> Notes:
> 
> - The source IP address of the ICMP test is 10.254.254.1. You cannot change this IP address.
> 
> If your account is using a [custom System Range](/v1/docs/working-with-the-cato-system-range), the source IP address is the first IP in the range. For example, if the custom range is 198.51.100.0/24, then the source IP address is 195.51.100.1
> - For each site, you can monitor a maximum of 50 hosts.
> - If a site is offline, the hosts behind the site aren't monitored. There are no events or email notifications until the site is re-connected.
> - No Host Reachable alerts or events are generated if the site connects to a different PoP.
> - LAN Monitoring doesn’t support monitoring the Socket LAN interface.

![LAN_Monitoring.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247798792093.png)

**To monitor a server or host in the LAN:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > LAN Monitoring**.
3. Click **New**. The **New** panel opens.
4. In the **General** section, configure these settings for the LAN host that you're monitoring:
  - **Name** of the LAN monitoring rule
  - IP address of the host that you're monitoring
  - Time **Interval** in seconds between each test packet
  - In **Fault Threshold**, select the maximum number of consecutive failed ICMP tests.

When this value is met, the Cato Management Application considers this server or host as unreachable.
5. In the **Actions** section, you can choose to configure the Time Limit and Tracking settings for the LAN monitoring rule.

These are optional settings.
  1. In the **Time Limit** section, choose a time range option for the rule: **No time constraint**, **Limit to working hours**, **Custom**.
  2. In the **Track** section, define the events and notifications for this rule:
    1. Select **Event** to generate events when the LAN host is defined as unreachable.
    2. Select **Email Notification**, to also send email alerts when the event is generated.
    3. Define the settings for the **Email Notifications**.
6. Click **Apply**. The **Add LAN Monitoring** panel closes and the rule is added to the screen.
7. Click **Save**. The rule is added to the site.

### Deleting a LAN Monitoring Rule

When you no longer need to monitor a LAN host, you can delete the rule in the **LAN Monitoring** screen.

**To delete a LAN Monitoring rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > LAN Monitoring**.
3. From the rule, click the Delete icon ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/1677d0c9526c9f.svg).

The rule is removed from the screen.
4. Click **Save**. The LAN Monitoring rule is deleted.
