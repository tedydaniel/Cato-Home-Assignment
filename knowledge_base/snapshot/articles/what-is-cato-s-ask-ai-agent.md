---
title: "What is Cato's Ask AI Agent"
slug: "what-is-cato-s-ask-ai-agent"
updated: 2026-08-27T11:25:54Z
published: 2026-08-27T11:25:54Z
canonical: "knowledge.catonetworks.com/what-is-cato-s-ask-ai-agent"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Cato's Ask AI Agent

## Overview

Cato's Ask AI is a generative AI agent that lets you explore your Cato account using natural language. Ask AI dynamically selects from a range of tools to answer your query, based on each tool’s capabilities. This helps you troubleshoot, analyze, and monitor your network, including performing root cause analysis based on your account data. It understands follow-up questions within the same session and provides links to relevant KB articles when available. Ask AI can also access data about your account when providing answers to queries. This unlocks hundreds of new use-cases to help you view information about your users, sites, applications, and bandwidth usage. For the most accurate results, ask questions in English.

For more information about queries, see [Ask AI - Sample Questions](/v1/docs/ask-ai-sample-questions).

### Sources of Information

Ask AI autonomously determines which sources to use on its own to answer your question. This makes it easier than ever to troubleshoot, analyze performance, and explore usage trends directly through natural-language questions.

Ask AI can draw information from the following sources of information:

- **Your Account Data** - Ask AI accesses both current and historical data about your account. This includes queries about sites, users, applications, bandwidth usage, and more.
- **The Cato API** - Ask AI can answer questions about some of the [Cato API](https://api.catonetworks.com/documentation/) queries and mutations, and can generate GraphQL queries that illustrate how to use the API from natural language prompts.
- **Cato's Knowledge Base** - All articles and information from the Cato Knowledge Base

## Asking Questions Related to Your Account Data

Ask AI can query data from your account in response to natural-language prompts. This lets you investigate account data without manually navigating to multiple pages, applying filters, or constructing the query yourself.

You can ask about account entities and telemetry, including sites, users, applications, policies, events, bandwidth usage, and network health. Ask AI can return both current and historical data, depending on the scope of the request.

## Ask AI for Global Search

Ask AI helps you quickly find where a Cato Management Application object or entity is used across different policies. You can use global search to assess the impact of a change, review existing policy usage, and avoid checking each policy separately.

### Supported Policies for Global Search

Global search supports cross-policy searches for these policies.

#### Security

- Anti-Malware > File Hash Policy
- App & Data Inline Protection
- Application Control Policy
- Tenant Restriction
- Agentic Threat Prevention
- Internet Firewall
- LAN Firewall
- TLS Inspection
- WAN Firewall

#### Networking

- DNS Settings
- IP Allocation
- Network Rules
- Site Configuration > Bypass

#### Access

- Always-On Policy
- Browser Access Control > Access Policy
- Client Connectivity Policy
- Proxy Configuration Policy
- Split Tunnel Policy

### Supported Entity Types for Global Search

Global search supports searches for these entity types across all supported policies.

#### Applications and Categories

- Application
- Application Category
- Custom Application
- Custom Category

#### Sites and Network Objects

- Host
- Network Interface
- Site

#### Users and Groups

- Directory User
- Group
- System Group
- User
- Users Group

#### Device Profiles

- Device Profile

#### Services

- Custom Service
- Service

#### Geographic Objects

- Country

#### IP Ranges and Subnets

- Floating Subnet
- Global IP Range
- Global Range
- Interface Subnet
- Site Network Subnet

#### Address and Domain Containers

- Allocated IP
- FQDN Container
- IP Address Range Container

#### Notification Targets

- Subscription Group
- Subscription Mailing List
- Subscription Webhook

## Asking Questions Related to the Cato API

The Ask AI can answer questions about the Cato API queries and mutations and can generate GraphQL queries that illustrate how to use the API from natural language prompts. It provides information, including:

- Sample GraphQL script for the API query or mutation
- Variables for the script
- Required and optional fields
- Links to the [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/) for relevant queries, mutations, and types

**Note:** The results of Ask AI may be inaccurate or incomplete. Always validate the syntax, parameters, and logic against the [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/) before using the query in a production environment.

## Ask AI in the CMA

Ask AI supports two complementary ways to work with AI in the Cato Management Application (CMA), letting you choose the right experience for the task.

For deeper analysis, use the AI Workspace, a dedicated full-page experience for exploring your Cato account. The AI Workspace lets you ask natural-language questions to understand account state, usage, policies, and best practices from a single, focused page.

You can also work with Ask AI while navigating the CMA, keeping the AI panel open as you review sites, Events, and policies. This approach supports fast, in-context investigation without interrupting your workflow.

There is the option to provide feedback on Ask AI responses to help improve the accuracy, relevance, and usefulness of future answers.

### Opening the AI Workspace

Use the AI Workspace page to enter free-text questions and select from guided question areas that help you quickly start common investigations. These guided options are intended as starting points and do not limit the types of questions you can ask.

![AI_workspace.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33870273255325(1).png)

**To open the AI Workspace:**

- From the navigation menu, click **Home > AI Workspace**.

To open the Ask AI chat, navigate to a different CMA page.

### Ask AI in the CMA Panel

The Ask AI panel is most effective when used as part of an investigation workflow, where AI-generated insight helps you decide which CMA pages to review next.

#### Ask AI Side-by-Side with the CMA

The Ask AI panel opens alongside the CMA and remains available as you navigate between pages. This side-by-side experience reduces context switching and lets you ask follow-up questions while reviewing live data in the CMA.

You can also click the microphone icon to use speech-to-text to enter queries in Ask AI.

![Ask_AI_chat.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35487207962269(1).png)

### Analyzing Ask AI Responses

Ask AI can help you investigate account data, but for complex or unexpected results, you may need to understand how it interpreted your request. Use the data in **Query Details** to analyze the response and confirm that Ask AI generated the correct query for your prompt.

Expand the **Query Details** to show the JSON query that Ask AI used to retrieve the data. You can review the time frame, dimensions, filters, measures, sorting logic, and result limits. This helps you verify that Ask AI understood your intent, identify why the response returned specific results, and troubleshoot prompts that need to be refined.

![query_details.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35487238298653(1).png)

### Visualize Data from a Query

Visualizing data helps you identify trends, compare values, and detect outliers more quickly than reviewing raw results.

Ask AI can present query results as a chart or graph for queries with measurable data, such as traffic over time, top applications by usage, or comparisons between sites, users, or policies. By default, Ask AI returns this data in tabular form. You can then prompt Ask AI to visualize the results as a chart or graph.

### Reopen Previous Chats

If you close the Ask AI panel and reopen it, a new conversation begins. Previous chats are available in the **Chat History** tab. Go there to continue previous conversations, revisit useful answers, and build on prompts that worked well.

### Contact Support

If you have additional questions after chatting with Ask AI, click **Contact Support** in the chat window to open a ticket. The chat transcript is automatically included, so our support team has the full context needed to assist you efficiently.

![ask_ai_contact_support.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32850028416797(1).png)

## Ask AI Architecture

Ask AI evaluates each question you enter and works with a Large Language Model (LLM) hosted in AWS for responses based on Knowledge Base articles, the Cato API, or account data queries. All access to account data is enforced by the same RBAC permissions that apply throughout the CMA.

The architecture includes these components:

- **LLM (Large Language Model)** - An AI model hosted on AWS Bedrock that understands natural-language questions and helps determine what information is needed to answer them. Ask AI uses the LLM to interpret your question and generate a clear, human-readable response.

The LLM doesn't have direct access to the account data and can't execute API calls. It receives the account data after the query is executed.
- **Internal MCP Server** - An internal Cato service that securely retrieves account data from the CMA.
- **Account Data** - A database containing data for your Cato account, such as sites, users, applications, traffic statistics, events, and usage metrics. Access to account data is always governed by your admin role and permissions.

The following diagram shows the decision flow for a typical request for account data:

![Account_info_Ask_AI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image-1785067911886.png)

**How It Works**

1. **Enter a question about the account** - The CMA admin asks a question in Ask AI using natural language, such as asking about site usage, user activity, or network performance.
2. **Ask AI interprets the request** - Ask AI sends the question to the LLM to understand what information is needed and which CMA data should be retrieved to answer it.
3. **Permissions are enforced** - Before any data is accessed, RBAC is applied to the query. This ensures that the response only includes data the admin is allowed to view, based on the admin role and account permissions.
4. **Account data is retrieved** - The internal MCP server queries the CMA database and retrieves the relevant account data, such as sites, users, applications, or usage metrics.
5. **Answer is generated** - Ask AI combines the retrieved data with the original question and returns a clear, natural-language answer. When applicable, the response includes links to relevant Knowledge Base articles.

## 

---

### FAQ

#### Q: Do RBAC permissions apply to the account data that admins can view?

A: Yes, Ask AI only provides admins with information that is aligned with their existing view and edit permissions.

#### Q: How is PII protected and treated in Ask AI?

A: Ask AI may process PII in compliance with applicable data protection laws. Cato may process PII through [third-party services](/v1/docs/cato-networks-sub-processors) with relevant agreements and controls in place.

#### Q: Will the ability to ask questions about account data require an additional license in the future?

A: Possibly. License requirements are still under evaluation and may depend on future roadmap and commercial decisions.

#### Q: Does Cato use its own LLM instance?

A: Cato uses its own AWS account to access Amazon Bedrock.

#### Q: How is customer data handled and segregated in Bedrock?

- Each Amazon Bedrock model call runs under Cato's invoking account's security context, ensuring strict data and execution isolation.
- Bedrock does not use any Cato or customer queries for model training.
- Cato uses an AWS Bedrock instance in the same region that the CMA is hosted in.

#### Q: Is data stored within Amazon Bedrock?

- No. Data is not stored within Amazon Bedrock, and Bedrock does not use Cato customer data to train its foundation models.
- Certain history and logs are retained in Amazon S3 for debugging, research, and improvement, in line with [Data Processing Agreements (DPA) and retention policies](/v1/docs/guide-to-cato-data-lake).

#### Q: What data does Cato retain, and for how long?

- Ask AI retains data for three months in accordance with Cato’s published Data Retention Policy. For details about what data is retained and the applicable retention periods, see the [Data Retention Policy](https://www.catonetworks.com/cato-networks-data-processing-and-privacy-agreement/).
- Certain history and logs are retained in Amazon S3 for debugging, research, and improvement, in line with [Data Processing Agreements (DPA) and retention policies](/v1/docs/guide-to-cato-data-lake).

#### Q: Is Cato AI Security involved in Ask AI?

A: Yes, AI Security monitors the prompts and queries entered into Ask AI.
