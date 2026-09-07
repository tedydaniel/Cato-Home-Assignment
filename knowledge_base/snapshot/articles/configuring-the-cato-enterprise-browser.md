---
title: "Configuring the Cato Enterprise Browser"
slug: "configuring-the-cato-enterprise-browser"
updated: 2026-08-12T10:06:36Z
published: 2026-08-12T10:06:36Z
canonical: "knowledge.catonetworks.com/configuring-the-cato-enterprise-browser"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Cato Enterprise Browser

## Overview

The Cato Enterprise Browser lets you provide secure, policy-controlled access to public SaaS and private WAN applications from any device, without installing an agent such as the Cato Client. Instead of extending controls into an existing browser, you provide users with a dedicated, managed browser workspace for business activity.

For more information, see [What is the Cato Enterprise Browser](/v1/docs/what-is-the-cato-enterprise-browser).

### Prerequisites

- A ZTNA (SDP) license is assigned to the user
- Only HTTPS traffic is supported, and access to these apps is based on the [WAN firewall](/v1/docs/managing-the-wan-firewall-policy) policy
- To generate events for the Enterprise Browser, you must have a Client Connectivity policy enabled
- For a list of supported IdPs for SSO authentication, see [Supported Identity Providers for SSO Authentication](/v1/docs/supported-idps-for-sso-authentication)

## Configuring the Enterprise Browser

To configure the Enterprise Browser, request the package, apply the required settings and install it on devices.

### Summary of Configuring the Enterprise Browser

The first four steps are completed by the Cato Management Application (CMA) admin. The fifth step is completed by users with devices.

1. Download the Enterprise Browser package and choose your upgrade policy.
2. **(Optional)** For SSO authentication, enable SSO for the Enterprise Browser.
3. **(Optional)** If Client Connectivity Policy is enabled, define the rules for the Enterprise Browser to determine which users are allowed to connect.
4. Enable the Enterprise Browser.
5. Install the Enterprise Browser on the devices.

### Step 1: Download the Enterprise Browser Package and Choose Your Upgrade Policy

You can download the Enterprise Browser package from the Client Rollout page in the CMA. Users can download the Enterprise Browser package from the [Client Download portal](https://clientdownload.catonetworks.com/).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36501151038237.png)

**To download the Enterprise Browser package and choose your upgrade policy:**

1. Navigate to **Access > Client Rollout**.
2. Under the operating system you want to download the package for, click **Download Browser**. The package is downloaded to your device.
3. On the **Upgrade Policy** tab, configure your upgrade policy. For more information, see [Managing the Rollout of Client Versions (Client Upgrade Policy)](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy).

### Step 2: Enable SSO for the Enterprise Browser

If you want to use SSO to manage authentication for the Enterprise Browser, you must first enable the option in the CMA.

This step is optional.

![SSO-Browser_Extension.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34694462938013(1).png)

**To enable SSO for the Enterprise Browser:**

1. Navigate to **Access > Single Sign-On**.
2. Under **Browser Extension Users**, select **Allow login with Single Sign-On**.

**Note**: This enables SSO for Enterprise Browser and the Browser Extension.
3. Select the cookie type and for how long it's valid.
4. Click **Save**.
5. Ensure that the following URI is listed in your SSO vendor for traffic redirecting:

`https://sso.proxy.catonetworks.com/auth_results`

For more information, refer to the [SSO documentation](https://support.catonetworks.com/hc/en-us/sections/4963959594141-Single-Sign-On) for your vendor.

### Step 3: Create a Rule in the Client Connectivity Policy

To ensure that only authorized users connect via the Enterprise Browser, create a rule in the Client Connectivity Policy. For example, create a User Group for all contractors and apply the rule to the contractor User Group.

This step is optional.

![connection_origin-browser_extension.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34694434001437(1).png)

**To create a rule to enable Enterprise Browser traffic:**

1. Navigate to **Access > Client Connectivity Policy**.
2. Click **New** and follow [these instructions](/v1/docs/configuring-the-client-connectivity-policy).
  - Under **Users/Groups**, select only those users you want to enable to use the Enterprise Browser
  - Under **Connection Origin**, select **Browser Extension**

**Note**: This applies to the Enterprise Browser and the Browser Extension.
  - Under **Action**, select **Allow Internet**
3. Click **Apply** and then **Save**.
4. Below this rule, create an additional rule for all other groups who attempt to connect to the Cato Cloud using the Enterprise Browser and set the **Action** to **Block**.

### Step 4: Enable the Enterprise Browser

You must enable the Enterprise Browser to let your users connect through it.

**To enable the Enterprise Browser:**

1. Navigate to **Access > Browser Access Control**.
2. Click the **Browser Extension** slider.

**Note:** This enables the Enterprise Browser and the Browser Extension.
3. Click **Save**.

#### Defining the NAT IP Range for the Enterprise Browser

You can define the range of translated source IP addresses for the users who connect with the Enterprise Browser. For example, some applications use an Access Control List (ACL) to only allow connections from a specific IP range. We recommend that you define the NAT IP address range, and then enable the source NAT IP range for each of the relevant Browser Access applications.

> [!NOTE]
> Note:
> 
> - If a source NAT IP range is configured for the Browser Applications Portal, the Enterprise Browser cannot use the same IP range
> - Set WAN based on the User identity, and not based on the SNAT range

### 

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(51).png)

**To define the NAT IP range for the Enterprise Browser:**

1. Navigate to **Access > Browser Access Control**.
2. In the **Enterprise Browser and Browser Extension** section, enter the **Source NAT IP Range.**
3. Click **Save.**

### Step 5: Distributing Enterprise Browser to Users

After configuring the required settings, you can distribute the Enterprise Browser to your users.

**To distribute the Enterprise Browser to users:**

1. Distribute the Enterprise Browser and certificate to end users.

To use the Enterprise Browser, users must sign in and authenticate.

## Understanding the User Experience

After you deploy the Enterprise Browser to your end users, the browser will automatically update when a new version is available.

Once connected, they will be able to access the internal resources, and the profile used to connect will comply with the policies defined in your organization.

**To connect using the Enterprise Browser:**

1. The first time users connect, they will need to authenticate.
  1. Enter your corporate email address
  2. (Optional) Enter the sub-domain you're connecting to. This is only relevant for users who are registered on more than one corporate account.
  3. Provide the username and password

## Known Limitations

- WAN routing requires SNAT or the default gateway to be configured to enable routing traffic back to Cato
- MFA using Cato as the IdP is not supported
- Coexistence with the Cato Socket or Cato Client is supported only when the browser is associated with the same Cato account.
- Multiple IdPs for the same account are not supported
- The Enterprise Browser is not supported in China
- When the Client Connectivity Policy includes a rule that allows only Internet traffic for the Enterprise Browser, WAN traffic is also allowed. To block WAN traffic, the rule must also block Internet traffic.
- DEM network path analysis is not supported
- Public networks that block non-standard ports are not supported
