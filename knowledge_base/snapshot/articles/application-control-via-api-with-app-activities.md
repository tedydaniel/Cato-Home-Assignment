---
title: "What is Application Control via API with App Activities"
slug: "what-is-application-control-via-api-with-app-activities"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/what-is-application-control-via-api-with-app-activities"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Application Control via API with App Activities

App Activities enables out-of-band visibility into actions taken in SaaS applications via direct API connections. This article provides an overview and background information about API-based CASB to monitor traffic to sanctioned SaaS cloud applications.

## Overview

Users have become increasingly dependent on a wide range of SaaS applications to complete their daily tasks. Siloed departments may use these applications without them being vetted. This creates a risk as security teams are unaware of what applications are being used, what data they are processing, and have no single location to monitor application usage.

The API-Based solution provides you with out-of-band visibility of all activity made by any user in a connected SaaS application. You still have visibility even if a user is not connected to the Cato Cloud, or TLS inspection is disabled.

For example, you can view a user changing their permissions. To ensure you understand the nuances of each application, activities are automatically categorized into predefined Activity Categories. An event is created after an activity is performed which is summarized in the **Cloud Activities Dashboard**. This provides you with complete visibility of activities on applications in one place.

A CASB license is required for Application Control via API with App Activities. This license also includes [app and data control](/v1/docs/what-is-the-unified-casb-solution). For more about purchasing a CASB license, please contact your Cato representative.

### Use cases

These are two use cases of how Application Control via API with App Activities can provide visibility of suspicious activity in a SaaS application.

#### Suspicious Downloads

A contractor on an unmanaged device downloads 10MB of Salesforce reports with customer personal data each week. In one day the contractor downloads 5GB of customer personal data. From reviewing the **Cloud Activities Dashboard**, the security team can identify this behavioral anomaly and analyze if it is suspicious.

#### Employee Offboarding

A developer that uses their own device is leaving company ABC. They have access to a SharePoint with presentations containing sensitive intellectual property. On the **Events** page, the security team can filter for the SharePoint activities taken by the developer to ensure they did not download the intellectual property before leaving the company.

### Supported Applications

For a full list of supported applications, see: [Application Control via API with App Activities](/v1/docs/application-control-via-api-with-app-activities)

### Prerequisites

- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section) and **App & Data API Protection** (in the **App & Data Control** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

### Understanding Unified CASB

Application Control via API with App Activities is part of the Cato Unified CASB solution. Unified CASB provides you with a comprehensive solution for monitoring and controlling user activities in SaaS applications across your account.

The [inline solution](/v1/docs/what-is-the-unified-casb-solution) help users safely access and use sanctioned and shadow cloud applications and lets you enforce a corporate policy that minimizes security incidents and compliance violations. The inline solution requires users to be connected to the Cato Cloud and TLS inspection to be enabled.

App Activities provides out-of-band visibility of all users activities in including unmanaged users (contractors) that access corporate SaaS applications. This functionality does not require users to be connected to the Cato Cloud or TLS inspection.

For total visibility of sanctioned and unsanctioned applications and managed and unmanaged users, we recommend using the inline and API solutions together.

Events generated from the inline and out-of-band solutions are visible from the **Cloud Activity Dashboard** and the **Events** page. This enables you to monitor all application activities in one location, without needing to switch between different consoles.

### Understanding Activity Categories

Different SaaS applications use different terms to describe the same action. For example, accessing a report could be called Exporting, Downloading, or Fetching. This creates a challenge when trying to understand what actions users are taking.

With Activity Categories, Cato maps activities in a SaaS application into a general category. This lets you track, filter, and visualize SaaS application activity, without needing to understand detailed processes in each application.

Activity Categories are applied to activities monitored by your Application Control policy and apps integrated with App Activities. They are used as a field in the Application Security API Events and can be in the Cloud Activities Dashboard to filter activities.

This ensures a unified solution across both API-based and inline modes.

The Activity Categories are:

| Activity Category | Example Actions |
| --- | --- |
| Admin Settings | User creation, Quarantine, Change permissions |
| API and Integration Execution | Automation, scripts via API |
| Communication & Collaboration | Chat, Video, Voice |
| Content Operations other | Upload, Download, Move |
| Delete | Deleting data |
| Download | Downloading a report |
| Execution | Automation, scripts |
| Failed Login | Failed login |
| Login other | Login, Logout |
| Move | Moving the location of a report |
| Search and View | View report |
| Share | Sharing via link |
| Upload | Uploading data |
