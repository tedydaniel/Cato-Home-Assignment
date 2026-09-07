---
title: "Data Obfuscation in the CMA"
slug: "data-obfuscation-in-the-cma"
updated: 2026-07-13T07:54:29Z
published: 2026-07-13T07:54:29Z
canonical: "knowledge.catonetworks.com/data-obfuscation-in-the-cma"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Obfuscation in the CMA

## Overview

Many admins need access to the same CMA pages to monitor events and manage the account, but not all of them need to see personal and sensitive data. Data Obfuscation helps you limit exposure to personally identifiable information (PII) in the CMA while still allowing admins to work with the data they need.

When Data Obfuscation is enabled, the CMA hides the selected PII fields by default and shows aliases instead of the original values. You can also create exceptions for admins to continue to see the original PII data, while other admins only see obfuscated data.

## Configuring Data Obfuscation

Enable Data Obfuscation for the account and select which PII fields are obfuscated. For example, the user name **Jane Smith** will show as *******.

**Note:** Before you enable Data Obfuscation, review any Service Principal accounts that are used for API integrations such as [events](https://api.catonetworks.com/documentation/#query-events), [appStats](https://api.catonetworks.com/documentation/#query-appStats), and [appStatsTimeSeries](https://api.catonetworks.com/documentation/#query-appStatsTimeSeries). If you want to only obfuscate data in the CMA pages and show PII for the data returned by these integrations:

1. Enable Data Obfuscation.
2. Configure the relevant Service Principals with **Allow Viewing Original Data**.

![Data_Anon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35813198150685.png)

**To enable data obfuscation for the account:**

1. From the navigation menu, click **Account > Roles & Permissions**.
2. Click the **Settings** tab.
3. Select **Enable Data Obfuscation**.
4. Under **Select the PII fields to obfuscation**, select the data that is obfuscated for the account.
5. Click **Save**.

## Allowing Admins to View Original Data

Some admins may need to view original data for operational or investigation workflows. You can configure exceptions so specific admins can view the original values even when Data Obfuscation is enabled for the account.

For Service Principal accounts, you can control which data is obfuscated for the relevant APIs.

![Allow_Data_Anon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35813223009693.png)

### Manually Created Admins

For admins that are managed directly in the CMA, you can configure the **View Original Data** permission for those admins.

**To allow a manually created CMA admin to view PII:**

1. From the navigation menu, click **Account > Administrators**.
2. Click the admin to edit the settings in the **General** page.
3. In the **Data Obfuscation Visibility (PII)** section, select **Allow viewing original data**.
4. Click **Save**.

### IdP Synced Admins

For admins that are synced from your Identity Provider (IdP), create a user group that the IdP syncs to the CMA, and then assign a dedicated admin role to that group. In the role assignment, select the synced user group, define the required RBAC settings, and enable **Allow viewing original data**.

**To configure IdP-synced admins to view PII:**

1. Select or create a new user group for CMA admins that can view PII.
2. Sync the admins from your IdP to the CMA, see [Manage Admins with your Identity Provider (IdP)](https://support.catonetworks.com/document/preview/215688#UUID-ef4fedce-213b-e8e1-2d89-ecd3d4c62006).
3. Create a role assignment for the relevant admins.
  1. From the navigation menu, click **Account > Administrators** and select the **Role Assignments** tab.
  2. Click **New**.
  3. Select the user group from step 1.
  4. Define the RBAC settings
  5. In the **Data Obfuscation Visibility (PII)** section, select **Allow viewing original data**.
  6. Click **Apply**.
