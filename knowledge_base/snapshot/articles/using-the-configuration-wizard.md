---
title: "Using the Configuration Wizard"
slug: "using-the-configuration-wizard"
updated: 2026-08-27T13:33:31Z
published: 2026-08-27T13:33:31Z
canonical: "knowledge.catonetworks.com/using-the-configuration-wizard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Configuration Wizard

This article discusses how to use the configuration wizard to set up and customize a policy according to best practices while meeting the specific requirements of your network.

## Overview

To help you maintain a secure and effective policies, Cato provides Posture checks and AI-based insights. For more information, see [Reviewing Posture Checks for Your Account](/v1/docs/reviewing-posture-checks-for-your-account) and [Understanding Cato Autonomous Policies.](/v1/docs/understanding-cato-autonomous-policies)

The Configuration Wizard autonomously reviews a policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management.

This screenshot is taken from the Internet Firewall.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(196).png)

### Supported Policies

The configuration wizard is supported for these policies:

- [Internet Firewall](/v1/docs/what-is-the-cato-internet-firewall)
- [WAN Firewall](/v1/docs/what-is-the-cato-wan-firewall)
- [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account)
- [Application Control](/v1/docs/managing-the-application-control-policy)
- [Private Access](/v1/docs/what-is-cato-private-access)
- [Remote Port Forwarding](/v1/docs/configuring-remote-port-forwarding-for-the-account)

### Use Case

A developer needed to test a new integration with a cloud-based payment gateway initially blocked by the organization's Internet Firewall policy. To enable testing, the IT team created a temporary rule allowing outbound access. Once testing concluded, the rule was intended to be deleted, but that step was inadvertently missed.

A week later, the IT team ran the Configuration Wizard which identified that the temporary rule granting access to the payment gateway was still active.

The IT team deleted the rule from within the Wizard. This ensured their firewall policy remained aligned with security standards and reduced unnecessary exposure.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image-1787837569323.png)

## Running the Configuration Wizard

Run the configuration wizard to review and create the recommended rules. Select which of the recommended rules to include, and the wizard guides you through the configuration. It shows the existing settings for each rule and lets you edit rule parameters to meet your account requirements. After the wizard creates the rules, save them to your account policy. You can run the configuration wizard at any time.

**To run the configuration wizard:**

1. From the navigation menu, select the policy you want to run the wizard for.
2. Click **Posture Recommendations**. The **Review Posture Recommendations** panel opens.
3. Review recommendations and select which ones to include in the wizard.
4. Click **Start Review**.
5. Expand each of the sections and review and configure as required.
6. Apply the updated settings, delete the rule, or skip to the next check.
7. Repeat steps 5-6 for each rule.
