---
title: "Configuring Cato Private Access"
slug: "configuring-cato-private-access"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/configuring-cato-private-access"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Cato Private Access

## Overview

Private Access lets you provide user-to-application access to private applications without onramping the application environment to your network. Access is brokered through the Cato Cloud and enforced at the PoP based on authenticated user identity and policy. Private applications are not reachable unless they are explicitly defined and authorized.

This article explains the complete admin end-to-end workflow for configuring Cato Private Access. Starting with deploying App Connectors in the application environment, then configuring the Private App, and defining the Private Access Policy to manage access to the application.

For more information, see [What Is Cato Private Access?](/v1/docs/what-is-cato-private-access)

### Prerequisites

Before you configure Private Access, make sure that your account uses an identity provider (IdP) for user authentication. Private Access requires authenticated user identity, and unauthenticated users can't access private applications.

For more information, see the articles in [Identity Providers and Authentication](/v1/docs/identity-providers-and-authentication).

## Private Access Configuration Workflow

For the Cato Private Access service, the App Connector provides connectivity to the application environment, the Private App defines what is published, and the Private Access Policy defines who can access it.

This is a high-level workflow for configuring Private Access:

1. Deploy the App Connector and assign it to an App Connector Group.
2. Configure the settings for the Private App.
3. Define access rules in the Private Access Policy.

## Deploy App Connectors

App Connectors provide secure connectivity between the Cato Cloud and the environment that hosts the private application. Each App Connector establishes an outbound-only DTLS tunnel to the Cato Cloud and forwards only sessions that were authorized by the PoP.

The Private App is attached to an App Connector Group, and the PoP brokers authorized sessions to the best available connector in that group.

**Best Practice:** Deploy the App Connector before you publish the application.

For more information, see [Working with App Connectors](/v1/docs/working-with-app-connectors)

![App_Connectors.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809671183005.png)

### Configure the App Connector

Deploy the App Connector in the same network environment as the protected application. Depending on where the application is hosted, the connector can be deployed in a physical data center or in a public cloud environment.

These are the supported App Connector types:

- [Creating Physical App Connectors](/v1/docs/creating-physical-app-connectors)
- [Creating App Connectors in Azure](/v1/docs/creating-app-connectors-in-azure)

### Assign the App Connector to a Group

An App Connector is the Cato component that provides connectivity between the Cato Cloud and the private application environment. Assign the connector to an App Connector Group so Private Apps can use the group as the connectivity path instead of depending on a single connector.

This design improves resiliency and operational flexibility because multiple connectors in the same group can provide access to the application. If one connector becomes unavailable, the application can use another available connector in the same group.

### Verify Connector Status

Confirm that the App Connector Group includes the connectors that provide connectivity to the application environment. The App Connectors page in the Cato Management Application shows the overall connector status, in addition to the connectivity status of individual ports.

## Private Applications

A Private App is the CMA object that defines the internal application, the published application domain, and the App Connector Group associated with the application.

![private_apps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809658693917.png)

For more information, see [Configuring Private Applications](/v1/docs/configuring-private-applications).

### Key Components of Private Apps

The **App Settings** define the internal application address and the service/port items for the application. The internal application address identifies the application in the private environment, and the service/port items define the protocols and ports that are allowed for the application.

The **Publish** settings define the published application domain and the App Connector Group associated with the application. The published application domain is the domain that users use to access the application, and the App Connector Group provides the connectivity path to the application environment.

**Probing** monitors application availability. It helps identify whether the application is reachable through the configured path and provides visibility into the application status.

### Internal App Address and Published App Domain

Two settings define different parts of the access flow:

- **Internal App Address:** The internal address of the application in the private environment. Cato uses this address for DNS resolution and to steer traffic to the application.
- **Published App Domain:** The domain name that users use to access the application.

## Private Access Policy

The Private Access Policy controls which users or groups can access the published private applications. The policy is evaluated at the PoP before a session is brokered to the application environment. It is an ordered rulebase, and only the highest priority matching rule is applied to allow or block access.

Each rule evaluates the relevant users or groups, optional criteria, and the selected Private Apps to determine whether access is allowed or blocked.

![private_access_policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809680804637.png)

For more information, see [Configuring the Private Access Policy](/v1/docs/configuring-the-private-access-policy).

### Key Components of the Private Access Policy

**Users / Groups** defines which users and groups are allowed to access the application

The **Criteria** setting defines the optional conditions for user access to the application. This lets admins add context-based controls, such as only devices with a valid anti-virus solution can connect.

The **Private Apps** setting defines the range of private applications that are available to the users.

### Private Access Policy Best Practices

- Scope **Users / User Group** to the required identities
- Select only the required **Private Apps** for users to access
