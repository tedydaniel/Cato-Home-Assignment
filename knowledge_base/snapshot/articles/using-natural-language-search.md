---
title: "Using Natural Language Search"
slug: "using-natural-language-search"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/using-natural-language-search"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Natural Language Search

This article explains how to easily search using everyday language to drill-down and identify relevant data on a page. You can also use [preset or custom filters](/v1/docs/filtering-data-on-a-page) to filter content on a page.

## Overview

Natural language search lets users find relevant data using everyday language instead of complex queries, commands, or filters. This is important for network and security monitoring because it simplifies the process of querying vast amounts of data, and lets admins more easily focus on the most relevant information while requiring less technical expertise. Searching with everyday language improves response times and enhances the overall effectiveness of admin teams by making access to data more intuitive.

The Cato Management Application (CMA) integrates generative AI with the filter bar to enable natural language search as part of the powerful search tools that let you drill down and identify the items that contain the relevant data you need.

When you enter a natural language query, an advanced AI engine translates your query into filters that refine the data shown on the page to match what you're looking for. Then you can manually adjust the filters to further refine the results.

Currently, the natural language search is supported in the following pages:

- Events
- Audit Trail

## Filtering Data with Natural Language Queries

The natural language search lets you use common words and phrases to request the data that you’re looking for. Enter the keywords or phrases for the query in the search bar and the AI search engine translates the query to the relevant filters and fields. Review the filters created by the AI engine and If the query isn’t quite right, you can enter a manually edit the filters or enter a new query.

The AI engine also formats the table of results to show the columns relevant to the query.

These are examples of queries you can enter and the resulting filters:

- **Show me Internet firewall security events from phishing category URLs**

![NLS_Example_phishing.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896512263837.png)
- **Show recent security incidents and alerts related to application vulnerabilities and threats**

![NLS_Example_app_threats.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896516497053.png)
- **Show me a security alert where data was sent from computer 10.0.0.1 to computer 10.0.0.2 over the Internet**

![NLS_Example_IP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896531985181.png)

> [!NOTE]
> Note:
> 
> Personal identifiable information is not shared outside of Cato unless you include it in a query. Avoid entering sensitive information in the search bar to prevent it from being submitted to an AI search engine.

**To filter data with a natural language query:**

1. Navigate to the Events or Audit Trail page.
2. Click ![Events_Filter_Create_New_Query_Button.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896532011421.png) to open the natural language search bar.
3. Type a query in everyday language in the search bar and press Enter.

The AI engine translates the query into the filters shown in the dropdown window, and the page is updated to show the items according to the filters.
4. If necessary, refine the filters manually:
  1. Click ![Events_Add_New_Filter_Button.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896539343005.png) to open the filter bar.
  2. Add new filters to refine the results. For more about adding filters, see [Filtering Data on a Page](/v1/docs/filtering-data-on-a-page).

## Frequently Asked Questions

---

### FAQ

#### What is Cato's AI safety policy?

Cato, along with our subcontractors, will not use any content, sensitive data, or personally identifiable information (PII) you provide for training AI models. For more details about Cato's AI policy, see [Cato Networks AI Safety](https://support.catonetworks.com/hc/en-us/articles/24202000386077#UUID-49cb9020-edb9-f98a-bc27-94499e70bf37)

#### How does the natural language search feature work?

When you type a query in everyday language, it's sent to an AI engine (provided by Amazon Bedrock) that translates it into specific filters and fields relevant to the Events page. These filters are then applied to refine the event data displayed. The AI engine only processes the query you enter and doesn’t have access to your event data.

#### What data is sent to the AI engine when I use this feature?

Only the natural language query that you type into the search bar is sent to the AI engine. No customer data, event logs, or any other account information is shared with the AI service. The AI engine processes your query in isolation, without any context of your specific data.

#### How is my company's data protected when using this feature?

Your company's data remains within the CMA environment and is not exposed to the AI engine. The engine only receives and processes the text of your query. It then returns instructions on how to create filters that match your query, which are applied within your secure CMA environment. This approach ensures that your sensitive information never leaves your protected infrastructure.

#### Does Cato use my queries or data to train the AI engine?

No, Cato does not use your queries or any of your data to train the AI engine. The AI engine we use from Amazon Bedrock is pre-trained. For each query, we send specific instructions to the AI along with your input to guide its interpretation, but this is done in real time and is neither used for training nor stored for future use.

#### Can I choose not to use the natural language search feature?

Yes, the natural language search is an optional feature. You can continue to use the traditional preset and manual filters for event searching and analysis if you prefer. The system allows you to switch between natural language search and traditional filtering methods based on your preference and security requirements.

## Known Limitations

Natural language search supports a limited set of event fields. Support for the other fields will be gradually added. The attached files detail which event fields are currently supported and which ones will be added.

[Supported Event Fields.txt](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Supported%20Event%20Fields.txt)[Fields to be Added.txt](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Fields%20to%20be%20Added.txt)
