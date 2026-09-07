---
title: "Creating a Custom SCIM App for an IdP"
slug: "creating-a-custom-scim-app-for-an-idp"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/creating-a-custom-scim-app-for-an-idp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a Custom SCIM App for an IdP

This article describes how to create a custom SCIM app in your IdP identity provider for user and user group provisioning with your Cato account.

For more information about creating a custom SCIM app with the Cato API, see [Using the Cato SCIM API for Custom SCIM Apps](/v1/docs/using-the-cato-scim-api-for-custom-scim-apps).

## Overview

You can create a custom SCIM app in your IdP tenant (such as a SAML app) to provision users and user groups to your Cato account. You need to:

1. In your IdP, create a custom SCIM app
  - In the app, map the attributes from your IdP to Cato SCIM attributes
2. Create the app in the Cato Management Application (CMA)

## Create a Custom SCIM App in the CMA

To use the SCIM API, you must first create a custom SCIM app in the CMA. This app allows you to integrate your identity provider (IdP) with the Cato platform.

**To create a custom SCIM app in the CMA:**

1. From the navigation menu, select **Identity Awareness > Identity Providers**.
2. Click **New** > **SCIM Custom App**.
3. Enter a name for the app and click **Save**.
4. After the app is created, note the following values:
  - **SCIM Base URL:** Used as the base path for API requests
  - **Bearer Token:** Used for authenticating API requests
5. Use these credentials when calling the SCIM API endpoints described below.

## Cato SCIM Attributes

These are the SCIM attributes for Cato users and user groups that you need to map to the corresponding IdP attributes.

| Cato User Attribute | Description |
| --- | --- |
| userName | User name for authentication |
| user.firstName | First name of user |
| user.lastName | Last name of user |
| user.email | Email address |
| user.displayName | Display name for user |
| phoneNumbers[type eq "work"].value | Work phone number for the user (including prefix) |
| externalId | ID for user (used in events) |

| Cato User Group Attribute | Description |
| --- | --- |
| active | User is assigned and active in the SCIM app |
| displayName | Name of user group |
| members | Users who belong to the user group |
| externalId | ID for user group (used in events) |
