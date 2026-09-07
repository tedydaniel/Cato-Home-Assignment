---
title: "Configuring Microsoft Foundry"
slug: "configuring-microsoft-foundry"
updated: 2026-09-02T12:15:55Z
published: 2026-09-02T12:15:55Z
canonical: "knowledge.catonetworks.com/configuring-microsoft-foundry"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Microsoft Foundry

## Overview

Cato connects to Microsoft Foundry through a read-only Azure integration that gives CMA admins full visibility into managed agents built in Foundry and their sessions.

### Prerequisites

Before you start, confirm the following:

- You have a Microsoft Entra ID (Azure AD) account with the **Application Administrator**, **Cloud Application Administrator**, or **Global Administrator** role. Cato's application only requests a basic sign-in permission, so Application Administrator or Cloud Application Administrator is the least-privileged option and is sufficient
- You have the **Owner** or **User Access Administrator** role on each Azure subscription that contains the Microsoft Foundry resources you want Cato to monitor. This Azure RBAC role is separate from your Microsoft Entra ID role, and Global Administrator doesn't grant it by default

Setting up this integration is a three-step process, and the steps are often completed by different people. In step 1, an Entra ID admin adds the Cato application to the tenant. In step 2, each subscription owner grants the application access to that subscription. In step 3, a Cato admin finishes the integration in the CMA. Loop in all three roles rather than assuming one admin holds every permission.

## Step 1: Connect Cato to Microsoft Entra ID

Cato registers a multi-tenant application in Microsoft Entra ID. To connect the integration, an Entra ID admin opens the Cato Networks admin consent link, which adds the application to your tenant as an Enterprise Application and grants it consent.

To connect Cato to Microsoft Entra ID:

1. Open the [Cato Networks admin consent link](https://login.microsoftonline.com/organizations/adminconsent?client_id=0f5bb78b-ad8f-454a-a7bc-3c6bb5b1e6c8&state=15021). Sign in with the administrator account described in the prerequisites when prompted. Microsoft displays a consent screen for the **Cato Networks AI Security Integration** application.
2. Click **Accept**.

## Step 2: Grant Cato Access to a Subscription

Cato requires the **Cognitive Services User** role on each Azure subscription that contains Foundry resources. This role provides read-only access and doesn't allow Cato to modify any resource. Assigning the role requires the **Owner** or **User Access Administrator** role on the subscription.

To grant Cato access to a subscription:

1. In the Azure portal, go to **Subscriptions**.
2. Select the subscription you want to connect.
3. Select **Access control (IAM)**, then select **Add** > **Add role assignment**.
4. Search for the **Cognitive Services User** role and click **Next**.
5. Under **Assign access to**, select **User, group, or service principal**.
6. Click **+ Select members**, search for **Cato Networks AI Security Integration**, select it, click **Select**, and click **Next**.
7. Click **Review + assign**, then click **Review + assign** again to confirm.

Cato recommends repeating this procedure for every subscription that contains Foundry resources you want Cato to monitor.

## Step 3: Finish the Integration in the CMA

To finish the integration, a Cato admin enters the Microsoft Entra ID tenant ID where the application was installed.

### Get the Tenant ID

To get your Microsoft Entra ID tenant ID:

1. In the Azure portal, go to **Microsoft Entra ID**.
2. On the **Overview** page, under **Basic Information**, copy the **Tenant ID**.

### Connect the Integration in the CMA

To connect the integration in the CMA:

1. From the navigation menu, select **AI Security** > **Integrations**.
2. On the **Microsoft Foundry** tile, click **Connect**.
3. In the **Azure AD Tenant ID** field, enter the tenant ID you copied.
4. Click **Test Connection**. You can save the integration only after the test succeeds.
5. Click **Save**.

## Data Refresh

After you connect the integration, Cato fetches data from Microsoft Foundry immediately, and then again every hour. Expect updated data in the CMA up to an hour after a change in your environment.

## Review the Requested Permissions

| Role | Access |
| --- | --- |
| Cognitive Services User | Read-only access across Microsoft Cognitive Services, Insights, and Resources. This lets Cato view account details, models, diagnostics, metrics, usage data, and Responsible AI policies, and check availability statuses and list operations. |
