---
title: "What is the Cato API"
slug: "what-is-the-cato-api"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/what-is-the-cato-api"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Cato API

This article helps you get started with the Cato API to monitor and configure settings and items in your account.

## Overview

Cato API is the primary automation interface for seamless integration with the Cato Cloud. Use the Cato APIs to set up efficient operational workflows such as deployment and configuration, as well as comprehensive status monitoring, statistics and data collection, and analytics to streamline your network and security management.

### Cato API Endpoint and Schema

The URL for the API endpoint and schema is specific to the location where the Cato Management Application (CMA) instance is hosted. There can be a <prefix> value that is appended to the URL for your CMA account and to the API endpoint and schema.

The URL for the API endpoint is in the format, `https://api.&lt;prefix&gt;.catonetworks.com/api/v1/graphql2`.

The URL for the API schema is in the format, `https://api.&lt;prefix&gt;.catonetworks.com/api/schema`.

**URLs for API Endpoint**

- If there is no prefix (`cc.catonetworks.com`), then use the following URL: `https://api.catonetworks.com/api/v1/graphql2`
- If there is a prefix (such as `cc.us1.catonetworks.com`), then you would use the following URL (modify the prefix for different locations): `https://api.us1.catonetworks.com/api/v1/graphql2`

**URLs for API Schema**

- If there is no prefix (`cc.catonetworks.com`), then use the following URL: `https://api.catonetworks.com/api/schema`
- If there is a prefix (such as `cc.us1.catonetworks.com`), then you would use the following URL (modify the prefix for different locations): `https://api.us1.catonetworks.com/api/schema`

## API Schema Documentation

Cato APIs are built on GraphQL, offering an intuitive interface that's fully compatible with RESTful API tools and clients. GraphQL also provides the added flexibility to query exactly the data you need, reducing over-fetching and improving efficiency.

Cato API documentation is available at [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/), which contains:

- Schema definition and documentation
- Example API calls and corresponding sample responses
- GraphQL API endpoint with an interactive Playground for exploring and testing the API

## API Lifecycle

This section describes the different lifecycle stages based on the maturity level and availability of a specific API.

Every new API is initially released in the Beta stage. The transition from Beta to GA is subject to internal review and consideration to verify that the API is stable and production-ready. Typically, the transition from Beta to GA takes about one year.

> [!NOTE]
> Note:
> 
> The lifecycle described below refers only to the formal Cato API as defined in the [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/). It does not cover any additional tools and examples that may be provided as references.
> 
> For example, it does not cover the open-source examples and utilities available at the [Cato GitHub account](https://github.com/catonetworks). These resources are provided “as is” with no warranty or obligation for further development, maintenance, or support.

### API Maturity Levels

These are the API maturity levels as part of the lifecycle stage:

- **Beta:** APIs in the Beta stage are feature-complete and considered fully operational, making them suitable for use in production environments. However, they may undergo changes based on user feedback or additional considerations. These changes, including breaking changes to the API schema, may occur with short notice and require updates to client code.
- **GA (General Availability):** APIs in GA are stable, production-ready, and come with long-term support and commitments to backward compatibility. Breaking changes to the API schema are rare and are announced well in advance to provide sufficient time for client code adjustments.

APIs that aren't explicitly labeled as Beta are considered GA. In some cases, within a GA API, individual fields, types, and inputs may be marked as Betas.

### API Availability Levels

These are the availability levels for APIs as part of the lifecycle stage:

- **EA (Early Availability):** APIs in EA are available to a limited group of users for testing and feedback before broader release. Access may require special approval or conditions.
- **Gradual Rollout:** Following standard industry best practices for cloud-based services, Cato APIs are gradually rolled-out to ensure stability and monitor performance, with availability expanding to all accounts over time.

APIs not marked as EA or Gradual Rollout are considered fully deployed and accessible to all users.

### Summary of API Labels

This section summarizes the labels used for APIs in the documentation based on the maturity and availability levels.

APIs with no label are fully available to all accounts and there are rarely breaking schema changes. Any such changes will be announced several months in advance. For more about these changes, see below [Potentially Breaking Schema Changes](/v1/docs/what-is-the-cato-api#potentially-breaking-schema-changes).

- **EA**
  - Only available to customers that join Cato's EA program, to join, please contact us at [ea@catonetworks.com](mailto:ea@catonetworks.com)
- **Beta**
  - There may be changes to the schema
  - Limited notice for breaking changes, possibly as short as two weeks
  - Beta APIs support full functionality
- **Rollout**
  - These GA APIs are being gradually rolled out to all accounts over a period of a few weeks
  - Calling an API in the Rollout status may result in an error message because that API is not yet available for your account

## Potentially Breaking Schema Changes

This section discusses when Cato makes changes to the GraphQL API schema that can impact behavior and results for API calls.

### What is a Potentially Breaking Change in GraphQL?

A potentially breaking change in GraphQL occurs when modifications to the API require client applications to update their queries or logic to maintain functionality. Examples include:

- Removing a field, type, or argument.
- Renaming fields, types, or arguments.
- Modifying default values for arguments in a way that changes the expected results of queries or mutations.
- Altering the type or behavior of a field in a way that impacts compatibility. For example, changing a field's type (e.g., from Int to String) or modifying an argument's nullability (e.g., from nullable to non-nullable).

### Announcing and Managing Potentially Breaking Changes

We work as hard as possible to avoid [potentially breaking changes](/v1/docs/cato-api-potentially-breaking-changes-and-eol). However, in the rare case that there is such a change, it will be communicated to customers as explained below in [Notifying about EoL APIs](/v1/docs/what-is-the-cato-api#notifying-about-eol-apis).

These changes may occur more frequently for Beta APIs but are rare for GA APIs.

#### Deprecated APIs

An API or a field marked as **Deprecated** indicates that its usage is no longer recommended, and a better alternative exists. We recommend that you update scripts and processes to no longer use deprecated APIs and fields to maintain expected behavior and functionality.

#### Notifying about EoL APIs

If an API or a field is planned for removal or replacement, it will go through an End-of-Life (EoL) process. This process includes the following steps:

1. Marking the API or Field as Deprecated
  1. The API or field planned for removal is marked as **Deprecated** in the [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/).
  2. This label is accompanied by a message, specifying an alternative API or field if applicable, and the planned EoL date.
2. EoL Notifications
  1. The [Cato API Potentially Breaking Changes and EoL](/v1/docs/cato-api-potentially-breaking-changes-and-eol) article is updated with the specific date that the schema will be updated with the change.
  2. The time period between the notification and the schema changes is as follows:
    - GA API: At least 3 months in advance and generally 6 months in advance
    - Beta API: Typically 2 weeks in advance
  3. During the time period between the EoL notification and the EoL date, customers are expected to update the client code to accommodate the changes to the GraphQL schema.

## Non-Breaking Schema Changes

Changes to the GraphQL that are non-breaking and still significant, such as new APIs or new fields, are announced in the [Cato API Changelog](/v1/docs/cato-api-changelog) article.

The [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/) always includes the complete supported up-to-date GraphQL schema.
