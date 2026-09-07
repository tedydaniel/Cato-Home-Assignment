---
title: "Configuring Private Applications"
slug: "configuring-private-applications"
updated: 2026-08-24T13:25:24Z
published: 2026-08-24T13:25:24Z
canonical: "knowledge.catonetworks.com/configuring-private-applications"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Private Applications

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

A Private App is the CMA object that defines an application in the private environment for access through Private Access. It is associated with an App Connector Group that provides connectivity to the application environment. The Private Access Policy then controls which users and groups can access the application.

For more information, see [Configuring Cato Private Access](/v1/docs/configuring-cato-private-access).

### Browser Access

[Browser-based access](/v1/docs/browser-access) is supported as a method for Private Access users to connect to the application, including: Enterprise Browser, Browser Extension, and Application Portal. When browser access is used, users connect to the published application domain through the Cato PoP, and then the Private Access Policy is enforced before the session is brokered to the application environment.

This lets admins publish applications for user access without requiring direct network reachability to the application environment.

**Note:** Browser Access is supported only for Private Applications that are defined for HTTP(S), RDP, or SSH.

## Internal App Address and Published App Domain

Two settings define different parts of the access flow:

- **Internal App Address:** The internal address of the application in the private environment. Cato uses this address for DNS resolution and to steer traffic to the application.
- **Published App Domain:** The domain name that users use to access the application.

The Published App Domain defines the user-facing application name in the Private Access workflow, while the Internal App Address identifies the application's destination in the private environment.

These values can be the same or different.

- Use the same value when the domain that users use to access the application is also the domain that identifies the application in the private environment.
- Use different values when users access the application with one domain, but the application is identified in the private environment by a different internal domain or address.

This distinction lets admins control the user-facing application domain separately from the application destination in the private environment.

## Create a Private App

When you define the settings for the private application, use the internal IP address and the published application domain.

Select the App Connector Group associated with the application to provide the connectivity path to the application environment.

The **Probing** settings enable monitoring the application availability. It helps identify whether the application is reachable through the configured path and provides visibility into the application status.

![private_apps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809663234205.png)

**To create a Private App:**

1. From the navigation menu, select **Access > Private Apps**.
2. Click **New**. The **Add Private App** panel opens.
3. In **1 - General**, enter the application **Name** and optional **Description**.
4. Configure **2 - App Settings**:
  1. In **Internal App Address**, enter the hostname or IP address of the internal application.

**Note:** If you want to use an FQDN, it needs to be resolvable internally
  2. In **Service / Port**, enter the allowed protocol and port for the application and then click **Add**. For example, **TCP/80-88**.

Repeat for each allowed service and port.
5. Configure **3 - Publish**:

If the App Connector is not yet deployed, the private app is **Disabled**. Continue with step 6.
  1. Set the toggle to **Enabled**.
  2. In **Published App Domain**, enter the public-facing domain for the application, such as **app.example.intranet**

You can use either an FQDN or a domain (e.g. *.example.intranet)
  3. In **Publish via**, select **App Connectors Group**.
  4. Select the **App Connector Group** that provides connectivity to the application environment.
6. Configure **4 - Probing** to monitor the application availability.
  1. Make sure that the toggle is **Enabled**.

**Note:** Disabling probing means that you can't monitor the application connectivity or performance in the CMA.
  2. **(Optional)** Customize the ICMP probe settings:
    - **Interval (Sec)** - select how frequently the probe is sent to the application
    - **Fault Threshold** - select the number of consecutive probe failures before the application status is **Unavailable**
7. Click **Apply**.

### Private App Best Practices

- For the Private App to securely connect to the App Connector:
  - The destination needs to be routable (accept inbound traffic from the App Connector)
  - The destination's **Internal App Address** needs to be resolved using the Internal DNS Server set for the App Connector
- Select the App Connector Group that provides connectivity to the application environment.
- Limit **Service / Port** items to only the protocols and ports required by the application.
- Enable probing to provide application health monitoring
- Deploy the App Connector before configuring the private application

## Monitor Private Apps

After you create a Private App, you can monitor it from the **Private Apps** page in the CMA.

The application status shows whether the application is available through the configured App Connector Group. This helps admins validate that the application path is operational and identify availability issues.

You can also identify Private Apps that are not referenced in the Private Access Policy. These applications are defined in the CMA, but they aren't currently available to users through policy.

When application details change, update the Private App configuration so the internal destination, published domain, services and ports, and App Connector Group remain aligned with the application environment.
