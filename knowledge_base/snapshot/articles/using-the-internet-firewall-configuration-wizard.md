---
title: "Using the Internet Firewall Configuration Wizard"
slug: "using-the-internet-firewall-configuration-wizard"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/using-the-internet-firewall-configuration-wizard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Internet Firewall Configuration Wizard

This article discusses how to use the Internet Firewall configuration wizard to set up and customize the Internet Firewall policy according to best practices while meeting the specific requirements of your network.

## Overview

The Internet Firewall controls traffic between your WAN and the Internet using policy rules that you define. Misconfigured rules can block legitimate traffic or allow unwanted access, reducing network security and performance. To help you maintain a secure and effective policy, Cato provides best practice checks and AI-based insights.

The Internet Firewall Configuration Wizard autonomously reviews your policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management.

![Wizard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27286747868445.png)

### Use Case

A developer needed to test a new integration with a cloud-based payment gateway initially blocked by the organization's Internet Firewall policy. To enable testing, the IT team created a temporary rule allowing outbound access. Once testing concluded, the rule was intended to be deleted, but that step was inadvertently missed.

A week later, the IT team ran the Configuration Wizard which identified that the temporary rule granting access to the payment gateway was still active.

The IT team deleted the rule from within the Wizard. This ensured their firewall policy remained aligned with security standards and reduced unnecessary exposure.

![Wizard_UC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27286747926301.png)

## Running the Internet Firewall Configuration Wizard

Run the configuration wizard to review and create the recommended rules. Select which of the recommended rules to include and the wizard guides you through the configuration. It shows the existing settings for each rule and lets you edit rule parameters to meet your account requirements. After the wizard creates the rules, save them to your account policy. You can run the configuration wizard when first setting up your policy, or at any time afterward.

**To run the Internet Firewall configuration wizard:**

1. From the navigation menu, select **Security > Internet Firewall**.
2. Click **Start Review**. The **Review Recommended Best Practices** panel opens.
3. Review the best practices checks and select which ones to include in the wizard.
4. Click **Start Review**.
5. Expand each of the sections, and review and edit the settings as required.
6. Apply the updated settings, delete the rule or skip to the next check.
7. Repeat steps 5-6 for each rule.
