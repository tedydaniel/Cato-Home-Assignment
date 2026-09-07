---
title: "Configuring the Cato Captive Portal"
slug: "configuring-the-cato-captive-portal"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/configuring-the-cato-captive-portal"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Cato Captive Portal

This article provides information about configuring the Cato Captive Portal, customizing the branding, and more.

## Overview

A captive portal is a web page that users are automatically directed to when they attempt to access the Internet. This page typically requires users to accept terms of service or perform other actions before they can access the internet. Captive portals are commonly used to provide secure network access to a network by controlling who can connect and by monitoring usage.

Cato lets you configure a captive portal as part of your environment to ensure that users on a public network who are trying to access the Internet are complying with your terms and conditions, that their usage is monitored, and that they adhere to the rules that your organization sets out. In addition, you can brand your captive portal so that visitors get the look and feel of your company brand to provide them with a sense of familiarity when they log on.

### Prerequisites

If you are using a private DNS server, you must add this entry to your DNS listing:

- 10.254.254.167 captiveportal.catonetworks.com

If you change the Cato default system range, the last octet for the Captive Portal IP will be x.x.x.13.

### Limitations

Branding settings for the Cato Captive Portal are not available in Reseller accounts.

### Use Case - Guest Wi-Fi

ABC company has a guest Wi-Fi network that visitors can use when they are at the organization's offices. Before they are granted access to the Internet, they are directed to a captive portal page with the company's branding and terms of agreement. Once a user enters their email address and accepts the terms, they are forwarded to your company's home page and can start to use the network.

### Use Case - Session Duration

ABC company has set the duration of their captive portal connections to 3 hours. A user connects under those conditions and expects to have access for those 3 hours.

An admin for ABC company determines that 3 hours is too long for a session duration and decreases it to 90 minutes. However, users who are already connected under the previous session duration will still stay connected for the amount of time previously allocated.

The configuration for the session duration is updated after approximately 2.5 hours and all sessions from that point adhere to the new settings.

## Configure the Captive Portal

There are two main steps to configuring the captive portal:

- Create a rule in the Internet Firewall to redirect traffic on the guest network to the captive portal
- Configure branding and captive portal settings

### Create a Rule for the Captive Portal

To ensure that traffic on the guest network is directed to the captive portal, you must first create a rule in the Internet Firewall. You should place this rule at the top of your rulebase to make sure that the rule is applied to users on the guest network. While the Internet Firewall is ordered, meaning, once traffic matches a rule, the other rules are ignored, the Captive Portal rule is an exception.

Even after the traffic for the guest network matches the Captive Portal firewall rule, once the user accepts the terms and is granted access to the network, traffic continues to be inspected for the sequential rules to see if there are any matches.

For example, your first rule is the captive portal rule, followed by a rule prohibiting access to any sites in the gambling category. Users will first hit the captive portal rule, sending them to agree to the terms and conditions. Once they are granted Internet access, if they try to navigate to a gambling site on your guest network, that traffic will be blocked.

![captive-portal_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26068620178205(1).png)

**To define a captive portal rule:**

1. From the navigation menu, click **Security > Internet Firewall**.
2. Click **New > New Rule**.
  - Set the IP address of the Guest network as the **Source** of the traffic
  - Set the **Criteria, App/Category, and Service/Port** to **Any**
  - Set the **Action** to **Captive Portal**
  - (Optional) Determine whether you want to generate an **Event** when this rule is triggered
3. Click **Add**.

### Configure Branding and Settings

To give your users the look and feel that they are used to, you can configure the branding that is applied to the captive portal page. In addition, you can customize the terms and conditions, whether an email address is required, and more.

![captive-portal_branding.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26068595332637(1).png)

**To configure the captive portal branding:**

1. From the navigation menu, click **Account > Captive Portal**.
2. Configure the following settings:
  - Upload your company logo
  - Set the colors for the background and determine the text and colors for the confirmation button
  - Customize the terms and conditions, and determine whether an email address is required
3. Under **Settings**, enter how long the user is granted access for, once the session is authorized.
4. **(Optional)** Enter the URL to which the user is redirected after authorization is granted. For example, your company homepage.
5. Click **Save**.
