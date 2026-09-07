---
title: "Securing AI App Traffic"
slug: "securing-ai-app-traffic"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/securing-ai-app-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Securing AI App Traffic

This article explains how to maintain secure access to AI apps in your organization.

## Overview

Using AI-based tools increases productivity but also presents new security challenges and risks to your organization. For example, users can enter proprietary data into the free tier version of an AI app, resulting in the app vendor having the right to use this information. Bad actors could query the AI app's LLM to extract the proprietary data. As the number of AI apps rapidly expands, security teams face the challenge of knowing which applications are in use and where is sensitive data being shared.

To protect your organization and its sensitive data while enabling secure AI application usage, Cato recommends a three-part strategy:

1. **Gain Visibility**: Understand which AI applications are in use, who is using them, and how they are utilized
2. **Control Access**: Implement policies to regulate access to AI applications and enforce security measures
3. **Protect Data**: Safeguard sensitive information by preventing unauthorized access or sharing within AI applications

Leveraging a combination of features enable you to implement this strategy and monitor and secure AI app traffic. You can define Internet Firewall rules to control access to a category of AI apps and set rules for specific AI apps. In addition, define the Application Control policy to ensure users only access your enterprise tenant for an AI app or block granular actions, keeping your proprietary information safe. As a further layer of protection, you can configure the Data Control policy to prevent the transfer of sensitive data to AI apps.

## Gaining Visibility of AI Apps in your Environment

Knowing and understanding the risks associated with the AI apps used within your organization can prevent data leakage risks, compliance violations, and potential security vulnerabilities. Understanding which AI apps are in use, who is using them, and how they interact with sensitive data enables you to enforce policies, mitigate threats, and ensure responsible AI adoption. Visibility also helps assessing the potential risks of AI apps, maintaining governance, and aligning AI usage with your organization’s security framework.

The GenAI Apps Dashboard and the Apps Catalog provide you with visibility and understanding of the AI apps used in your environment.

### The GenAI Dashboard

The GenAI Apps Dashboard provides centralized, comprehensive visibility into inline GenAI app usage, including shadow AI. The dashboard details what AI applications are being used across your organization, and by who, and tracks all user interactions and sensitive data sharing. With the visibility provided by the GenAI Apps dashboard, you can proactively prevent data breaches by identifying risks. For more information, see [Using the GenAI Apps Dashboard](/v1/docs/using-the-genai-apps-dashboard).

### The App Catalog

The App Catalog contains a broad range of security data, compliance, and general information for hundreds of AI apps and services. This includes providing all the insights for conducting TPRM (third-party risk management) to evaluate the risk of using this app. You can use the catalog to learn more about an app and decide how to use it in your organization. For more information, see [Using the App Catalog](/v1/docs/using-the-app-catalog).

### Audit Activities Support GenAI Apps

Audit Activities provides you with out-of-band visibility of all activity made by any user in a connected SaaS application even if a user is not connected to the Cato Cloud. Microsoft Copilot and ChatGPT can be integrated with Cato to provide you with visibility of the chats and data that is being shared with these apps. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

### Use Case - Identifying Shadow AI

Company ABC reviews the GenAI Apps Dashboard and identifies an unknown AI-driven code analysis tool. They search for the app in the App Catalog and find that the app has a risk score of 6. To avoid the risk of sensitive information being disclosed, they create an Application Control role to block access to the app.

## Controlling Access to AI Apps

Without proper access controls, users may inadvertently input confidential information into AI models, leading to data leakage or regulatory violations. Additionally, unvetted AI applications could introduce security vulnerabilities, expose proprietary code, or generate misleading or harmful content. By enforcing strict access policies, you can ensure that only authorized users engage with authorized AI tools, minimizing risk while enabling AI adoption.

### Controlling Access to App Categories

Cato maintains 8 system categories for AI apps in addition to the general **Generative AI Tools** category. These can be used in the Internet Firewall to control access to a category of AI apps, for example, code assistants apps, or for the most popular AI apps, including ChatGPT, AgentGPT, Google Bard, Elicit AI, MagicPen AI, Poe AI, OpenAI, and more.

You can also define rules for specific AI apps or app categories. For example, after creating a rule that blocks traffic to the **Generative AI Tools** category, you can create a rule with higher priority that allows traffic to **ChatGPT** for a specific group of users that need access. For more information, see [What is the Cato Internet Firewall?](/v1/docs/what-is-the-cato-internet-firewall).

The following example Internet Firewall rules allow the **User Group** Research Team to access **ChatGPT**, while blocking all other access to the **Generative AI Tools** category:

![AI_Tools_FW_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28862955832349.png)

The Application Control Policy lets you granularly control app access based on specific criteria, such as an app's risk score or its level of compliance. For more about configuring Application Control rules, see [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy).

### Controlling Tenant Access

To prevent the exposure of proprietary information in the free tier of an app, you can create rules in the Application Control policy that block users from accessing private accounts, and allow access to only your enterprise tenant. For example, you can define rules for the **OpenAI** app that only allow login activity to your organization's tenant, and block all other logins (for example, logging in with a private email address).

Below is a sample rulebase where the first rule allows login to **OpenAI** for user names that include the company domain, then the next rules block all login to OpenAI through direct and third-party authentication.

![AI_Tools_CASB_Rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28862943269277.png)

### Controlling Granular Activities

For increased granularity, for some apps you can balance security with productivity by allowing users access to a necessary application while blocking risky activities within it. To do this, you can create rules in the Application Control policy, that include granular activities. For example, you can allow access to Wordtune, but block users from uploading files.

![Gran_actv.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28862946018461.png)

### Enforcing Temporary Chats (ChatGPT)

ChatGPT offers a temporary chat feature designed to enhance user privacy. According to OpenAI, these chats don’t appear in the user’s history, aren’t stored in memory, and aren’t used to train models. However, this privacy safeguard is disabled by default. Unless users manually enable it, all interactions are saved, posing a potential risk for work-related use.

The Application Control policy can detect whether users are in a temporary chat and can block traffic when they’re not. This lets organizations give users access to ChatGPT, while ensuring sensitive data isn’t inadvertently exposed.

![ChatGPT.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28862926094877.png)

## Protecting Sensitive Data

GenAI apps often process user inputs in ways that could lead to data leakage, such as users unintentionally sharing proprietary code, personally identifiable information (PII), or confidential business data. The Cato DLP service scans content and enforces policies in an AI app to help you prevent users from compromising sensitive data when using the app. By creating DLP rules for GenAI apps, you can enforce policies that detect and block sensitive data from being entered into AI models.

### Pre-Defined Data Profiles

Cato's DLP service uses dozens of models capable of detecting sensitive data in the traffic flow using advanced techniques. This includes categories such as Finance, Legal, HR, Immigration, and Medical. In addition, DLP also includes Data Types for use with GenAI apps. For example, the PII Data Profile includes Data Types such as credit card information and Drives licenses. This lets you create a granular policy that only applies to the relevant sensitive data and prevents it from being used in an AI app.

If the pre-defined data profiles can provide your own files/data to train a custom ML model. Advanced AI engines learn from this input, deduce context, and later detect sensitive data within the same domain.

For more information, see [Working with Custom Data Types for DLP](/v1/docs/working-with-custom-data-types-for-dlp).

### Pre-Defined Data Violation Monitoring

> [!NOTE]
> Note:
> 
> This feature is available by default for accounts created after March 25, 2025. For accounts created before this date, you can manually create the Data Types. For more information, see [Recommended DLP Configuration to Monitor AI Apps](/v1/docs/recommended-dlp-configuration-to-monitor-ai-apps).

The Application Control and DLP policy includes pre-defined Cato-recommended rules. Included in these are rules to protect your AI apps. By default, DLP monitors and creates events for the following Data Types being uploaded to GenAI tools:

- PII
- Financial data
- Access keys & tokens
- Legal data

### Use Case - Identify Data Policy Violations

Company ABC is signing a deal to subscribe to a new SaaS application. They are sent the contract to sign and a user uploads it to the free tier of a high-risk GenAI app to review and summarize the contract. The Pre-Defined DLP rule creates an Event to alert the security team of this policy violation.
