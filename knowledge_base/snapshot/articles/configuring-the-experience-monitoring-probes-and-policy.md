---
title: "Configuring the Experience Monitoring Probes and Policy (EA-Socket Probes Follow Policies)"
slug: "configuring-the-experience-monitoring-probes-and-policy"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/configuring-the-experience-monitoring-probes-and-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Experience Monitoring Probes and Policy (EA-Socket Probes Follow Policies)

This article provides an overview of the Experience Monitoring Probes and Policy for sites and users to help you monitor your LAN and WAN traffic over the Cato Cloud.

## Overview

Experience Monitoring enables you to configure probes to business-critical applications and use the policy to determine how to implement those probes to best monitor your sites and users. By default, [Experience Monitoring](/v1/docs/what-is-cato-experience-monitoring) gives you insight into all of the sanctioned [applications](/v1/docs/using-the-app-catalog) that traverse the Cato Cloud. In addition, you can configure customized probes and send them to destinations over your links. The probes can be configured to use different protocols to help you identify trends in different segments of your network.

Once you configure the probes, the Experience Monitoring policy lets you define the sites and users that you want to monitor and the domains or applications that the metrics or the experience monitoring is based on. For example, you can create a rule to monitor the performance of Salesforce for a specific group of SDP users.

The policy gives you granularity with your monitoring – letting you apply probes only to the sites or users that are relevant for an application.

> [!NOTE]
> Note:
> 
> To provide an accurate simulation of user-generated traffic, Experience Monitoring probes operate in compliance with the Network and Security policies configured for your account.
> 
> - Probe traffic that hits policy rules will generate events (if the rule is configured for events)
> - Probe traffic can be blocked by policy rules
> - For Socket site probes, supported for Socket version 24 and higher

### Experience Monitoring Probe Policy

The Experience Monitoring Probe policy lets you create a rule-based policy for your Sockets, sites, and users.

The policy lets you create ordered rules to implement the probes in different situations. For example, you can create a rule to use an ICMP probe for www.sampleprobe.com for all Socket sites around the world, and another rule for www.sampleprobe.ca using a TCP probe for Socket sites in Canada.

In addition, you can create rules in the policy for specific users or user groups. For example, if you want to monitor the application performance of your business applications for all of your Cato Client users and see how their experience is different from the users in the office for the same business application.

### Probes

Cato supports sending different probes to various URLs or IP addresses to monitor different segments of your network. Each probe measures latency and packet loss.

The following probe types are supported and more than one probe type can be configured per destination:

- ICMP - used to ping a site or device to see that it is up and functioning (supported from Socket v20).
- The following probe types are supported from Socket v21:
  - TCP - used to make sure that a 3-step handshake can be established with the target site
  - HTTP and HTTP/s - used to see if a request is received and what response is sent back. A response code of 200 indicates that the site responded with a successful connection.
  - DNS - used to send a DNS request to the target, usually your DNS server, and make sure the target name is resolved successfully.

Once you configure your probes, you can apply them to your sites or users to start monitoring their experience using the Synthetic Probe policy.

### Use Case – Increased Latency over Time

The IT department at Company ABC is receiving tickets for an internal application that users are accessing through the WAN. The IT department configures HTTP probes to monitor trends in the performance to this app.

When they look at the Experience Monitoring graphs for this application, they see that due to high traffic volume, there is increased latency to this site.

Using this information, they create a QoS rule increasing bandwidth to this application.

### Use Case - Gradual Rollout

The IT department at Company ABC wants to start monitoring user experience for all users. However, they don’t know what affect this might have on network performance, and also want to be able to start receiving data on one group of users before continuing with additional users in the organization.

In the Experience Monitoring policy, they create a rule for all users in the R&D department that have the Cato Client installed to start sending probes to their relevant applications, such as their database and repository.

The IT department, using the **User** and **Applications** tabs in the Experience Monitoring page is able to start seeing data for the R&D department, such as which applications are working well, which have a bottleneck at certain times, and more. This enables them to make changes to QoS rules to improve performance and gives them the confidence to start rolling out the User Experience policy to additional departments.

## Enabling the Experience Monitoring Policy

The Experience Monitoring policy lets you control which probes and probe types are sent to which destinations. In addition, you can also enable collecting specific monitoring data for users even when they are behind a Socket.

**To enable or disable the Experience Monitoring policy:**

1. From the navigation menu, select **Network > Experience Monitoring Probes**.
2. Toggle the **Experience Monitoring Policy** slider above the rule base to enable or disable the policy

**To enable or disable collecting monitoring data for users behind a Socket:**

1. From the navigation menu, select **Network > Experience Monitoring Probes**.
2. Toggle the **Use Probes in Office Mode** slider above the rule base to enable or disable collecting data behind a Socket

**Note:** This setting affects all users regardless of whether they match a specific rule.

## Configuring the Experience Monitoring Probe Policy

The Experience Monitoring policy is comprised of two stages:

- Defining probes
- Creating rules for when the different probes are used

### Define a Probe

By default, you have predefined probes to several destinations, some in China and others globally. You can define additional probes for use in your policy

![DEM_probes.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28912640193053.png)

**To define a probe:**

1. From the navigation menu, select **Network > Experience Monitoring Probes**.
2. On the **Probes** page, click **New**.
3. Enter a descriptive **Name** for the probe and complete the following information:
  - Probe Type - select any of the supported probes, e.g. DNS
  - Destination Type - Select either **Internet** or **WAN**
  - Destination - the URL or IP address to send the probe to
  - Probe Interval - for sites, the default is 60 seconds, and for users, the default is 300 seconds
4. Configure if you want to **Send on last resort** links. Take into account that last resort links are often more expensive
5. Click **Apply**

### Configure an Experience Monitoring Policy Rule

By default, you have 2 predefined rules - one for all sites and another for all users. You can configure additional rules in the policy. You must assign at least one probe to each rule, and no more than 20 probes.

The rules are order-based, meaning, once a rule is matched, it is applied to the site or user and all following rules are ignored.

![DEM_policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28912629033373.png)

**To configure a rule:**

1. From the navigation menu, select **Network > Experience Monitoring Probes**.
2. On the **Policy** page, click **New**.
3. Enter a descriptive **Name** for the rule and complete the following information:
  - Type
    - Site - Socket site
    - User - Cato Client
  - Rule Order
4. Select the **Source** as a site or user.
  - For **Sites**, the source is at least one of the following:
    - Site - a specific site or sites
    - Country - all sites whose origin is the selected country or countries
    - System Group - Select the All Sites system group
  - For **Users**, the source is at least one of the following:
    - User Group - a specific User Group or User Groups
    - User - a specific user or users
    - System Group - select the All Users system group
5. If necessary, click **Add Exceptions** to exclude any items from the rule.
6. If the rule **Type** is **User**, configure the following for the device:
  - The **Platforms** on which this rule applies
  - The **Countries** in which this rule applies
  - The **Device Posture Profiles** to which the rule applies
7. Under **Configuration**, select the probes to which to apply this rule.
8. Click **Apply**

It will take several minutes for you to start seeing the data in the [Experience Monitoring](/v1/docs/using-the-experience-monitoring-page) pages of the Cato Management Application. The results are available in the Synthetic Probes graphs.
