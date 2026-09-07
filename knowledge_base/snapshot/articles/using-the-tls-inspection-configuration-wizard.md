---
title: "Using the TLS Inspection Configuration Wizard"
slug: "using-the-tls-inspection-configuration-wizard"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/using-the-tls-inspection-configuration-wizard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the TLS Inspection Configuration Wizard

This article discusses how to use the TLS Inspection configuration wizard to set up and customize the TLS Inspection policy according to best practices while meeting the specific requirements of your network.

## Overview

TLS Inspection decrypts and inspects HTTPS traffic to enhance security. A challenge with TLS inspection is that it can break traffic for legitimate sites and then users can't access important resources. The Cato Research team developed a simplified way to configure your policy to enable TLS Inspection for a large collection of apps and domains that can be safely inspected without causing issues while bypassing traffic that may have issues with TLS Inspection.

Using advanced data analysis methods, Cato Research identified popular apps and domains that can be inspected without issues and grouped them into categories that can easily be configured in a TLS Inspection rule. Cato continually maintains the categories and updates the items when necessary, with relevant rules automatically applying the updated category to inspected traffic. The wizard lets you easily create recommended Inspect rules using these categories while customizing the rule parameters to meet your requirements.

In addition, the wizard helps you create rules to bypass traffic that might have issues when inspected, such as IoT traffic.

## Use Case

Example Corp. recently adopted the use of many different generative AI tools to perform business-critical functions. The Example Corp. security team identified the use of AI tools as a significant data-leak risk requiring the implementation of a Data Control policy to prevent the loss of sensitive data such as PII. Enforcing the Data Control policy requires TLS Inspection of the encrypted AI app traffic, however, the team is concerned that this may impact user experience and overall productivity. Researching and testing all of the relevant apps would require extensive resources.

The security team identifies that the **Popular Cloud Apps** and **Cato-Recommended Domains** categories include the AI apps that can be inspected without issues. This means that the Data Control policy can be applied to these AI apps, and all other AI resources can be blocked because they don’t meet the security policy. The team uses the TLS Inspection configuration wizard to implement the required policy and customize the recommended rule settings for their account.

## Understanding the Recommended Rules

This section describes the recommended rules that the TLS Inspection configuration wizard helps you create. This includes a set of Bypass rules and a set of Inspect rules. The Bypass rules are for operating systems that may cause issues when inspected, and for categories of sensitive information that regulation often requires not to be inspected. The Inspect rules use Cato-defined categories of domains and apps identified as safe to inspect, as well as categories for malicious or suspicious destinations. These are the recommended rules:

- Bypass Rules -
  - **Bypass Embedded Operating Systems** - Operating systems that Cato classifies as **Embedded** are typical for IoT devices and sometimes don’t support installing the Cato certificate for TLS Inspection
  - **Bypass Sensitive Categories** - Categories that are not inspected due to privacy regulations and concerns
- Inspect Rules -

> [!NOTE]
> Note:
> 
> The categories **Popular Cloud Apps** and **Cato-Recommended Domains** are system categories and can't be edited. Category members can be viewed in the **System Categories** tab of the [Categories](/v1/docs/working-with-categories) page.
  - **Inspect Popular Cloud Apps** - High-popularity cloud apps that were analyzed by Cato's security team and confirmed to be safe for inspection. Configure inspection for these apps to enable optimal CASB Application Control and DLP Data Control policy enforcement
  - **Inspect Cato-Recommended Domains** - Top domains found to be broadly TLS-inspected across the Cato cloud. TLS-inspecting these domains is likely to be safe. Create this rule for broader DLP coverage
  - **Inspect Malicious and Suspicious Categories** - Destinations identified as malicious or suspicious. Configure inspection for these destinations to enable Anti-Malware and IPS scanning.

## Running the TLS Inspection Configuration Wizard

Run the configuration wizard to review and create the recommended rules. Select which of the recommended rules to include and the wizard then guides you through the configuration. It shows the default settings for each rule and lets you edit rule parameters to meet your account requirements. After the wizard creates the rules, save them to your account policy. You can run the configuration wizard when first setting up your policy, or at any time afterward.

> [!NOTE]
> Notes:
> 
> - There is a default rule at the bottom of the TLS Inspection rulebase set to inspect any traffic. For customers who configure the recommended rules in this wizard, we recommend changing the default rule to the Bypass action.
> - Cato recommends as a best practice for implementing TLS Inspection to start gradually by first applying it to a test site or a test group of users as part of a controlled rollout

![TLSi_Wizard_Rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23739970649245.png)

**To run the TLS Inspection configuration wizard:**

1. From the navigation menu, click **Security > TLS Inspection**.
2. Click **Start Review**. The Recommended Rule Review and Configuration panel opens.
3. Review the recommended Bypass and Inspect rules and select which ones to include in the wizard.
4. Click **Start Review**. The configuration settings for the first rule open.
5. Expand each of the sections, and review and edit the settings as required.
6. Click **Apply & Continue**. The settings for the next rule open.
7. Repeat steps 5-6 for each rule, and then click **Apply & Complete Review**. The rules are added to the rulebase.
8. Click **Save** to apply the rules to the account policy.
