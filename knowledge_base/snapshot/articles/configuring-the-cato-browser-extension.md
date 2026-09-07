---
title: "Configuring the Cato Browser Extension"
slug: "configuring-the-cato-browser-extension"
updated: 2026-09-07T08:22:02Z
published: 2026-09-07T08:22:02Z
canonical: "knowledge.catonetworks.com/configuring-the-cato-browser-extension"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Cato Browser Extension

This article explains how you configure the Cato Browser Extension. You can read more about the Cato Browser Extension [here](/v1/docs/what-is-the-cato-browser-extension).

## Prerequisites

The Browser Extension has the following prerequisites:

- You must enable [TLS Inspection](/v1/docs/tls-inspection) for the Browser Extension to function properly
  - End users can download the relevant certificate directly from the Browser Extension home page

![BE-home-page.jpeg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30876345562653.jpg)
- A ZTNA (SDP) license is assigned to the user
- To generate events for the Browser Extension, you must have a Client Connectivity policy enabled

## 

## High-Level Overview of Configuring the Browser Extension

This section is a high-level overview of the process to configure the Browser Extension for your account. The first two steps are configured by the CMA admin, and the third step is completed by your users with unmanaged devices.

1. **(Optional)** For SSO authentication, enable SSO for the Cato Browser Extension.
2. Define the rules for the Browser Extension in the Client Connectivity Policy to determine which users are allowed to connect via the extension.
3. Enable the Browser Extension.
4. Install the Browser Extension on the unmanaged devices.

### Step 1 (Optional): Enable SSO for the Cato Browser Extension

If you want to use SSO to manage authentication for the browser extension, you must first enable the option in the CMA.

![SSO-Browser_Extension.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30876335798429(1).png)

**To enable SSO for the Cato Browser Extension:**

1. Navigate to **Access > Single Sign-On**.
2. Under **Browser Extension Users**, select **Allow login with Single Sign-On**.
3. Select the cookie type and for how long it's valid.
4. Click **Save**.
5. Ensure that the following URI is listed in your SSO vendor for traffic redirecting:

`https://sso.proxy.catonetworks.com/auth_results`

For more information, refer to the [SSO documentation](/v1/docs/sso-integrations) for your vendor.

### Step 2: Create a Rule in the Client Connectivity Policy

To ensure that only authorized users connect via the Browser Extension, create a rule in the Client Connectivity Policy. For example, create a User Group for all contractors and apply the rule to the contractor User Group.

![connection_origin-browser_extension.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30876345713309(1).png)

**To create a rule to enable Browser Extension traffic:**

1. Navigate to **Access > Client Connectivity Policy**.
2. Click **New** and follow [these instructions](/v1/docs/configuring-the-client-connectivity-policy).
  - Under **Users/Groups**, select only those users you want to enable to use the Browser Extension
  - Under **Connection Origin**, select **Browser Extension**
  - Under **Action**, select **Allow Internet**
3. Click **Apply** and then **Save**.
4. Below this rule, create an additional rule for all other groups who attempt to connect to the Cato Cloud using the Browser Extension and set the **Action** to **Block**.

### Step 3: Enable the Browser Extension

You must enable the Browser Extension to let your users connect through it.

**Enabling the Browser Extension**

1. Navigate to **Access > Browser Access Control**.
2. Click the **Browser Extension** slider.
3. Click **Save**.

#### Defining the NAT IP Range for the Browser Extension

You can define the range of translated source IP addresses for the users who connect with the Browser Extension. For example, some applications use an Access Control List (ACL) to only allow connections from a specific IP range. We recommend that you define the NAT IP address range, and then enable the source NAT IP range for each of the relevant Browser Access applications.

> [!TIP]
> Note:
> 
> - If a source NAT IP range is configured for the Browser Applications Portal, the Enterprise Browser cannot use the same IP range
> - Set WAN based on the User identity, and not based on the SNAT range

### 

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(51).png)

**To define the NAT IP range for the Browser Extension:**

1. Navigate to **Access > Browser Access Control**.
2. In the **Enterprise Browser and Browser Extension** section, enter the **Source NAT IP Range.**
3. Click **Save.**

### Step 4: Install the Browser Extension

The Browser Extension can be installed on any device running a version of Chrome that supports extensions. For more information, see [Understanding the User Experience](/v1/docs/configuring-the-cato-browser-extension#h_01KFFXH6V3885TD4GR28VJ19P8).

## Understanding the User Experience

When you enable the Browser Extension and define the Client Connectivity Policy, unmanaged devices will only be able to access the designated resources once they install the extension and connect to the network.

Once connected, they will be able to access the internal resources, and the profile used to connect will comply with the policies defined in your organization.

Once the extension is installed, users must connect to pull the initial configuration settings.

**To connect using the Browser Extension**

1. Install the extension either via the Google Store or request it from your admin.
2. Click the Cato icon in Extensions and select **Connect.**
3. The first time users connect, you will need to authenticate.
  1. Enter your corporate email address
  2. (Optional) Enter the sub-domain you're connecting to. This is only relevant for users who are registered on more than one corporate account.
  3. Provide your username and password
  4. Depending on the organizational policy, you might be required to configure MFA

### Browser Extension Statuses

This section shows the different Browser Extension statuses and their descriptions

| Status | Description |
| --- | --- |
| ![browser-extension_Disconnected.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30876331846173(1).png) | The extension is currently disconnected and you can't access company resources |
| ![browser-extension_Authenticating.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30876331898653(1).png) | The extension is currently authenticating and you don't yet have access to company resources |
| ![browser-extension_Connected.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30876336020253(1).png) | The extension is authenticated and you can now access company resources |

## Known Limitations

- Only HTTPS traffic is supported
- WAN routing requires SNAT or the default gateway to be configured to enable routing traffic back to Cato
- Local MFA is not supported
- The Browser Extension is not supported in China
- When the Client Connectivity Policy includes a rule that allows only Internet traffic for the Browser Extension, WAN traffic is also allowed. To block WAN traffic, the rule must also block Internet traffic
- DEM network path analysis is not supported for Browser Extension traffic
- If you receive the following dialog box, it can safely be ignored, and you should click **Cancel** in the dialog box ![Browser-Extension-error.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30876307756573(1).png)
