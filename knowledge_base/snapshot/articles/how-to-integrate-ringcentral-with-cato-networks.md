---
title: "How to Integrate RingCentral with Cato Networks"
slug: "how-to-integrate-ringcentral-with-cato-networks"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-integrate-ringcentral-with-cato-networks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Integrate RingCentral with Cato Networks

Cato Networks is a certified connectivity partner of RingCentral, a leading provider of unified communications as a service (UCaaS). RingCentral has performed extensive testing that demonstrates Cato’s ability to provide excellent call quality even during poor network conditions with up to 15% packet loss.

If you’re a current or prospective RingCentral customer, this article will guide you through the Cato configuration necessary to get the best performance out of your RingCentral product.

## High-Level Overview

1. Verify that SIP ALG is disabled for the account or specific sites.
2. Enabled Preferred IP for SIP traffic for the account or specific site.
3. Verify that the security policies do not block RingCentral traffic.
4. Configuring the BW Management to give the correct priority for RingCentral traffic.
5. Configure a network rule for RingCentral traffic.

## Verify that SIP ALG is Disabled

SIP ALG is disabled by default. Verify that it is still disabled.

**To verify that SIP ALG is disabled:**

1. Go to the **Advanced Configuration** section for the entire account or the site:
  - For the account: **Resources > Advanced Configuration**
  - For the site: In **Network > Sites** click the site and go to **Site Configuration > Advanced Configuration**
2. Click the **SIP ALG** line and verify that it is disabled. If it is not disabled, click the toggle to disable it. (The toggle is green when enabled).
3. The value of the Value field should be **OFF**.
4. Click **Apply**.

SIP ALG is disabled for the account or site.

## Enable Preferred IP for SIP Traffic

If you have an egress network rule for VoIP or SIP traffic, sometimes RingCentral has problems if the IP address changes. When the Preferred IP for SIP Traffic feature is enabled, VoIP and SIP traffic always uses the same egress IP address.

**To enable Preferred IP for SIP Traffic:**

1. Go to the **Advanced Configuration** section for the entire account or the site:
  - For the account: **Resources > Advanced Configuration**
  - For the site: In **Network > Sites** click the site and go to **Site Configuration > Advanced Configuration**
2. Locate the **Preferred IP for SIP Traffic** line and enable the setting (The toggle is green when enabled).
3. The value of the **Value** field should be **On**.
4. Click **Apply**.

## Verifying the Security Policies

Make sure that the Internet Firewall and URL Filtering policy do not block RingCentral traffic.

### Configuring the Internet Firewall

By default, the Internet Firewall will not block any RingCentral traffic. However, if you have created a more restrictive Internet Firewall policy, you may need to create a rule to allow RingCentral traffic.

**To create an Internet firewall rule to allow RingCentral traffic:**

1. In the navigation menu, go to **Security > Internet Firewall**.
2. Click **New > New Rule**.
3. In the **general** section, give your rule a name and description, and select the appropriate **Position** of the rule. The rule should be placed before any rules that might block RingCentral traffic.
4. In the **App/Category** section, select **Application** and enter **RingCentral**.
5. In the **Actions** section, select the action **Allow**.
6. Click **Save**.

The Rule is created allowing RingCentral traffic.

### Allowing Traffic from RingCentral Domains

By default, the Internet Firewall policy will not block traffic to any RingCentral domains. However, if you have configured a more restrictive policy, such as blocking all URL categories and allowing only certain domains, you will need to create a rule to allow RingCentral domains.

First you will create a Custom App containing the domains, then you will create an Internet Firewall rule using the Custom App.

**To create a Custom App for RingCentral Domains:**

1. In the Cato Management Application, go to **Resources > Custom Apps** and click **New**.
2. Enter a **Name** and a **Description** for the **Application**.
3. In the **Rules** section, click **New**.
4. In the **Domains** section, select **Domains** and enter the required RingCentral domains one at a time. You can view the RingCentral domains on the [RingCentral support site](https://support.ringcentral.com/article-v2/Network-requirements.html?brand=RingCentral&amp;product=RingEX&amp;language=en_US).
5. Click **Apply** on the Rule page, and then **Apply** on the Custom App page.
6. Click **Save** on the Custom Apps window to save the policy.

**To create an Internet Firewall Rule to allow RingCentral Domains:**

1. In the Cato Management Application, go to **Security > Internet Firewall**.
2. Click **New > New Rule**.
3. In the **general** section, give your rule a name and description, and select **First** as the **Position** of the rule.
4. In the **App/Category** section, select **Custom Application** and enter the name of the Custom Application you just created.
5. In the **Actions** section, select the action **Allow**.
6. Click **Save**.

The Rule is created allowing RingCentral domains.

## Configuring Bandwidth (BW) Management

RingCentral should be assigned the lowest BW Management priority to ensure optimal voice quality even during link congestion. By default, all voice and video traffic over the Internet is assigned the lowest predefined priority, P10, by the “Internet Voice & Video - Predefined” policy under **Network > Network Rules** in the Cato Management Application. Therefore, without any rule modification, RingCentral traffic will be given the same precedence as other voice traffic.

If you’d like to prioritize RingCentral traffic over all other voice traffic, create a lower priority under **Network > Bandwidth Management**. You’ll use this priority when setting up a Network Rule in the next step.

**To configure a BW Management Priority for RingCentral:**

1. From the navigation pane, go to **Network > BW Management**.
2. Click **New**.
3. Define the **Priority** as any number less than 10.
4. Click **Apply**.
5. Click **Save**.

## Configuring a Network Rule

Create a network rule for RingCentral traffic to assign a custom BW priority, set the NAT IP, and enable Packet Loss Mitigation. The NAT IP address is also the egress IP address for a specific Cato PoP. We recommend that you select the Cato PoP that is physically closest to a RingCentral PoP, and lets you take advantage of the RingCentral tier 1 backbone.

Setting the NAT IP in the network rule ensures that both SIP (used for call setup) and RTP streams (voice data) share the same NAT IP. Phone calls will not work if the RTP stream uses a different NAT IP than the SIP stream.

Enabling Packet Loss Mitigation will prevent call quality from degrading with up to 15% packet loss on the WAN link.

**Prerequisites**

You will need at least one allocated IP to complete the configuration for the network rule. If you do not have any allocated IPs, you can create one under **Network > IP Allocation** in the Cato Management Application. See this [article](/v1/docs/allocating-ip-addresses-for-the-account) for more information.

**To configure a network rule:**

1. In the Cato Management Application, go to **Network > Network Rules**.
2. Click **New > New Rule**.
3. Enter the **Name** and specify the type as **Internet**.
4. Select a low **Rule Order** to make sure this rule is checked before any other potentially conflicting rules.
5. In the **App/Category** section, add the **ApplicationRingCentral** and the **Custom Application** you created.
6. In the **Configuration** section, under **Bandwidth Management**, select the **Bandwidth Priority** you defined above and enable **Packet Loss Mitigation**.
7. In the **Configuration > Routing Method > Route/NAT** field, select **NAT** and enter a single or multiple egress IPs. We recommend that you select the Cato PoP that is physically closest to a RingCentral server.
8. Click **Apply** and then **Save** the rule.
