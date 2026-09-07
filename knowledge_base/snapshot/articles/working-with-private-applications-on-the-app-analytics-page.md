---
title: "Working with Private Applications on the App Analytics Page"
slug: "working-with-private-applications-on-the-app-analytics-page"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/working-with-private-applications-on-the-app-analytics-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Private Applications on the App Analytics Page

This article explains how to identify private applications and configure them as custom applications on the [App Analytics](/v1/docs/understanding-app-analytics) page.

## Overview

When deploying ZTNA solutions, it can be challenging to identify and enforce policies for all of your organization's private applications, and all the destinations your users require. The Cato Cloud detects the applications that are unidentified and not included in predefined or custom-defined applications in the Cato Management Application, and shows them on the App Analytics page. This page lets you easily configure the unidentified application destinations as custom applications that can be included in policies.

You can also add custom applications from the Custom Apps page. For more about custom applications, see [Working with Custom Apps](/v1/docs/working-with-custom-apps).

## Showing Unidentified Applications on the App Analytics Page

Filter the **Destinations** on the App Analytics page to show the unidentified applications for your network.

![App_Analytics_-_Unidentified_Apps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275665175709.png)

**To show the unidentified applications:**

1. From the navigation menu, click **Home > App Analytics**. The **App Analytics** page for the account is displayed.
2. Select the **Destinations** tab.
3. In the **Traffic Type** dropdown menu, select **Unidentified Apps**. The page shows the data filtered for application destinations not included in predefined or custom applications.

## Generating Custom Applications on the App Analytics Page

The App Analytics page streamlines the process for defining unidentified applications as custom applications, which you can then create polices for. First, show the unidentified applications and expand an application to see the component protocols and services. Then select the ones you want to include in the custom application and generate the custom application. When you generate an application, settings are automatically configured based on the selected components. You can also manually configure settings for the application.

![App_Analytics_-_Generate_App.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275672075165.png)

**To generate a custom application from the App Analytics page:**

1. From the navigation menu, click **Home > App Analytics**. The **App Analytics** page for the account is displayed.
2. Select the **Destinations** tab.
3. In the **Traffic Type** dropdown menu, select **Unidentified Apps**. The page shows the data filtered for application destinations not included in predefined or custom applications.
4. Expand a destination. The protocols and services detected for the application are shown.
5. Select the protocols and services to include in the custom application.
6. Click **Generate Custom App**. The **New Custom Application** panel opens with data preconfigured for the destination.

![App_Analytics_-_New_Custom_App_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275672160029.png)
7. Enter a **Name** and **Description** (optional) for the application.
8. In the **Member of categories** section, search for an existing application category from the drop-down menu.

You can add multiple categories.
9. In the **Rules** section, click **New** to add a rule for the custom app.

The **Add Rule** panel opens.
  1. In the **Protocol** section, select the appropriate protocol for the rule.
  2. In the **Ports** section, from the drop-down menu select **Port** or **Port Range**, and then enter the value.

Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275648743581.png) (Add) to add the ports to the application rule.
  3. In the **Destination IP** section, enter the IP address or IP Range.

You can also paste a comma separated list with multiple IP addresses and ranges, for example: 10.1.1.1, 10.2.1.1-10.2.1.105

Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275648743581.png) (Add) to add the destination IPs to the application rule.
  4. In the **Domains** section, from the drop-down menu select if the rule should include matching traffic based on **Domain** or **FQDN** and then enter the domains or FQDNs.

Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275648743581.png) (Add) to add the domains to the application rule.
10. Click **Apply & Save**. The custom application is configured. You can see and edit the settings for the application on the [Custom Apps](/v1/docs/working-with-custom-apps) page.

> [!NOTE]
> Note:
> 
> Only new traffic detected for the app appears in App Analytics under the name of the custom application, previous traffic will continue to appear as it originally did as an unidentified app.
