---
title: "Working with Custom Apps"
slug: "working-with-custom-apps"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/working-with-custom-apps"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Custom Apps

## Overview

Cato provides full layer 7 application and service awareness that can be used across the Cato Management Application (such as in analytics, security rules, networking rules).

Custom apps enable you to define a proprietary or unique app/service used by your organization that isn't predefined in the Cato Management Application (CMA). Once defined, you can use the custom app in Security or Network Rules and analytics like any other global object.

Custom apps are descendants of matching predefined applications. The first matching firewall or network rule is applied to the custom or predefined application. If you want to apply the rule action for a specific application, make sure that this rule is placed above any other rule that contains matching predefined applications.

> [!NOTE]
> Note:
> 
> Although Cato Networks continuously updates its predefined application and service list, in some cases, you may not find a commonly-used application/service for which you are searching. If this occurs, please open a support ticket so that Cato adds the application/service to the predefined list. While you are waiting for the predefined application, you can create the specific application/service as a custom application as a workaround until it is available in the CMA.

### Best Practices for Creating Custom Applications

When the Cato Cloud processes traffic flows, the real-time classification of custom applications matches one application per flow. However, if the applications are not defined according to best practices, then they can overlap which can cause unpredictable behavior regarding which custom application matches a traffic flow.

To help make sure that the applications function correctly in your account, we strongly recommend that you define the custom applications as specifically as possible. This means that you define all the applicable items for the rule for the custom application. For example, configure the custom application with defined **Destination IP**, **Domains**, and **Ports** instead of only defining the **Ports**.

The following example shows a custom application configured according to Cato's best practices:

![CustomApplication_Items.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447627871901.png)

## Adding Custom Apps

When defining a new custom app, you can assign one or more categories that the app belongs to as well as create rules that define the app.

- When specifying multiple categories (for example: Advertisements, Gambling, or News), to define the custom application, the categories have an **OR** relationship. This means that the custom app belongs to all of the categories.

The **Member of category** setting does not impact the traffic that matches the custom app.
- When adding a rule to the custom application, the settings for **Protocol**, **Ports**, **Destination IPs**, and **Domains** have an **AND** relationship. This means that the custom app is recognized only if traffic matches the all the criteria defined in the rule.

![customapps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447616929309.png)

**To add a custom app:**

1. From the navigation menu, click **Resources > Custom Apps**.
2. Click **New**. The **New Custom Application** panel opens.
3. Enter a **Name** and **Description** (optional) for the application.
4. In the **Member of categories** section, search for an existing application category from the drop-down menu.

You can add multiple categories.
5. In the **Rules** section, click **New** to add a rule for the custom app.

The **Add Rule** panel opens.
  1. In the **Protocol** section, select the appropriate protocol for the rule.
  2. In the **Ports** section, from the drop-down menu select **Port** or **Port Range**, and then enter the value.

Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447587007005.png) (Add) to add the ports to the application rule.
  3. In the **Destination IP** section, enter the IP address or IP Range.

You can also paste a comma separated list with multiple IP addresses and ranges, for example: 10.1.1.1, 10.2.1.1-10.2.1.105

Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447587007005.png) (Add) to add the destination IPs to the application rule.
  4. In the **Domains** section, from the drop-down menu select if the rule should include matching traffic based on **Domain** or **FQDN** and then enter the domains or FQDNs.

Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447587007005.png) (Add) to add the domains to the application rule.
  5. Click **Apply**. The rule is added to the custom application.
6. Click **Apply**. The custom app is added to the page.
7. Click **Save**. The custom app is saved to your account.
