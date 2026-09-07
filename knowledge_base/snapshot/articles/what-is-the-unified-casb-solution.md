---
title: "What is the Unified CASB Solution?"
slug: "what-is-the-unified-casb-solution"
updated: 2026-07-06T12:44:02Z
published: 2026-07-06T12:44:02Z
canonical: "knowledge.catonetworks.com/what-is-the-unified-casb-solution"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Unified CASB Solution?

This article provides information about the Cato Cloud Access Security Broker (CASB) solution and suggestions for how to implement this solution for your account.

## Overview of Cato's CASB Solution

In today's environment, users need access to a variety of apps which can create challenges for enforcing your organization's security and compliance policies. Cloud apps are now an integral part of the working day and require a different solution beyond firewalls and threat protection. To help users safely access and use cloud apps, Cato's Cloud Access Security Broker (CASB) solution lets you enforce a corporate policy that minimizes security incidents and compliance violations.

Cato's CASB solution is designed to enable your organization to deliver these core functions:

- Visibility for risks related to app usage and shadow IT
- Enforce the app policy to meet compliance requirements and for access control
- Monitor unmanaged and managed users activity in shadow IT and sanctioned apps
- Threat protection from known and unknown cloud threats
- Data protection

The unique architecture of the Cato Cloud is the basis of Cato's robust CASB solution. All Socket and user traffic is connected to cloud apps and servers via the Cato Cloud. Cato can then easily inspect, monitor, and enforce all of this traffic from your account to the different cloud assets. In addition, Cato's Security team analyzes traffic data from billions of flows and is constantly adding new apps and updating and enhancing the existing ones based on actual usage and proprietary data mining technology.

An additional CASB license is required for the Application Control Policy and Cloud Apps Dashboard. For more about purchasing a CASB license, please contact your Cato representative.

## Understanding the Components of the Unified CASB Solution

Unified CASB provides you with a comprehensive solution for monitoring and controlling user activities in SaaS applications across your account. The CMA lets you manage all the components of the CASB solution from a single console. The data and analytics are unified and shared between the CASB components, giving you clarity and control for cloud app usage.

The unified CASB solution combines these features:

- **Enforcing inline app control on sanctioned and shadow IT**

Helps users safely access and use sanctioned and shadow cloud applications and lets you enforce a corporate policy that minimizes security incidents and compliance violations. The inline solution requires users to be connected to the Cato Cloud and TLS inspection to be enabled.
  - Use the [Sanctioned Apps Category](/v1/docs/using-the-applications-dashboard) to define key business apps (requires CASB license)
  - Create an [Application Control Policy](/v1/docs/managing-the-application-control-policy) to define granular app usage (requires CASB license)
- **Out-of-band visibility of SaaS applications**
  - [Visibility](/v1/docs/what-is-application-control-via-api-with-app-activities) of unmanaged users whose traffic is not tunneled through the Cato Cloud
  - Audit of every user activity
  - Configure an integration between your SaaS applications and Cato
- **Visibility, assessing app usage, and risk analysis**
  - [Applications Dashboard](/v1/docs/using-the-applications-dashboard)- overview of the cloud apps usage and risk analysis (requires CASB license)
  - [Application Analytics](/v1/docs/understanding-app-analytics) - helps you to analyze the network and application usage for your entire account, a specific site, or a specific user
  - [Threat Dashboard](/v1/docs/using-the-security-threats-dashboard) - shows threats related to IPS and Anti-Malware and drill-down and analyze the threat types and event data
  - [Apps Catalog](/v1/docs/using-the-app-catalog) - get detailed information, compliance data, and risk analysis for the cloud apps that are used in your account
- **Threat protection for cloud threats**
  - Make sure [IPS protections](/v1/docs/configuring-the-ips-policy) are enabled in block mode
  - Configure [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) for your account
  - Create a custom category of high-risk apps and add them to a block rule in the [Internet firewall](/v1/docs/configuring-tls-inspection-policy-for-the-account)

### Understanding SaaS Posture Checks, CASB, and Interconnected Apps

[SaaS Posture checks](/v1/docs/understanding-the-security-posture-of-your-saas-applications), [CASB](/v1/docs/what-is-the-unified-casb-solution), and [Interconnected Apps](/v1/docs/interconnected-apps) each address different aspects of SaaS security and work together to provide comprehensive visibility into your SaaS environment.

- SaaS Posture checks evaluate the security configuration of your SaaS applications. They identify misconfigurations and settings that don't follow security best practices, such as disabled multi-factor authentication, overly permissive sharing settings, or inactive administrator accounts. These checks help you harden your SaaS applications and reduce the risk of compromise.
- CASB provides visibility into how users interact with SaaS applications. It monitors user activity, detects risky behavior, and helps enforce data security policies. For example, CASB can identify users downloading sensitive files, sharing data externally, or accessing applications from unusual locations.
- Interconnected Apps focus on third-party applications that have been granted access to your SaaS environment through OAuth or similar authorization mechanisms. These applications can introduce additional risk even when the SaaS application itself is securely configured. Interconnected Apps help you identify connected applications, understand the permissions they have been granted, and assess the potential risk they introduce.

Together, these capabilities provide a layered approach to SaaS security.

For example, a Salesforce tenant might pass all SaaS Posture checks because it follows recommended security practices. However, a third-party application with broad permissions could still expose sensitive data if it is compromised. CASB might detect a user downloading an unusually large number of files, indicating potentially risky activity. Together, SaaS Posture checks, Interconnected Apps, and CASB provide visibility into the application's security configuration, the third-party applications that can access it, and how users interact with it.

## Implementing the Cato CASB Solution

This section contains a suggested workflow to implement the CASB solution in your account. The initial stage is to monitor app traffic in your account and identify the different types of app activity. Then define the sanctioned apps and create the Application Control policy. Run the policy in monitor to mode to make sure that you don't accidentally block legitimate and necessary apps. In addition, check to see if there are other risky apps that you need to block. Then enable the policy and continue to monitor and review the traffic. Finally, you can fine-tune the policy and update rules as needed.

> [!NOTE]
> Note:
> 
> The CASB solution, and especially the Application Control policy, relies on the ability to inspect all traffic for your account. We strongly recommend that you enable the TLS Inspection policy for your account as part of implementing CASB. Otherwise, it's not possible to inspect and manage access for apps that use HTTPS traffic.

These are suggested steps to take to implement the CASB solution in your account.

1. Monitoring app activity -
  1. When you activate the CASB license, a rule that monitors **Any Activity** for **Any Cloud Application** is automatically added at the bottom of the Application Control rulebase. Review the events to discover all of the granular apps and activities used on your network.
    - If you already have an existing CASB license and want to monitor your network's app traffic, add a rule near the bottom of the rulebase configured to monitor **Any Activity** for **Any Cloud Application**. If the rule is added with a high priority in the rulebase, it may prevent block rules lower in the rulebase from blocking traffic.
  2. Use the Cloud Apps Dashboard and Application Analytics to further monitor the app activity in your account.

For existing accounts, when you activate the CASB license, no initial configuration is required for the Cloud Apps Dashboard. It is immediately populated with the relevant data history.
2. Identifying types of apps - What are the top apps used in your account? Identify the sanctioned apps, unsanctioned benign apps, and high-risk apps.
  - Sanctioned apps represent approved activity that is totally compliant with your privacy and security policy, such as Office365 and Slack.
  - Unsanctioned benign apps have a minimal security risk and are not key business apps, such as Spotify and YouTube.
  - High-risk apps are potential security risks and are not related to your business. Apps with a Cato risk score of 7 and higher are high-risk apps.
3. Add the applicable apps to the Sanctioned Apps category.
4. In the Internet firewall, block the high-risk apps.

For the initial implementation, monitor traffic (and review the events) for a few weeks to make sure that you don't block legitimate apps. Use the Internet firewall to manage Category based control.
5. Create the Application Control Policy for your account. These are some suggested rules
  1. Allow all sanctioned apps. You can also create granular rules for specific apps, for example block download from Salesforce.
  2. Block traffic that doesn't meet the compliance policy for your organization. For example, block traffic from apps that are NOT SOC-2 compliant.

For the initial implementation, monitor traffic (and review the events) for a few weeks to make sure that you don't block legitimate apps.
6. Review the rules for the cloud apps traffic and fine-tune the CASB rules:
  - Are there additional risky apps that you need to block?
  - Are there additional apps that are key business apps and you need to sanction them?
7. Change the block rules from Monitor to Block.
8. Continue to monitor and review the cloud apps traffic in your account. Fine-tune the CASB policy so that it meets the requirements for your account.

If the data or information for a cloud app needs to be updated, or there are other cloud apps that we need to add to the catalog, please contact Support.
