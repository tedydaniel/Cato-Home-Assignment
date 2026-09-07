---
title: "Configuring Copilot Studio"
slug: "configuring-copilot-studio"
updated: 2026-07-27T15:06:42Z
published: 2026-07-27T17:46:45Z
canonical: "knowledge.catonetworks.com/configuring-copilot-studio"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Copilot Studio

## Overview

Cato connects to Copilot Studio environments through API access, giving admins visibility into the Agents created in Copilot Studio across the organization and their activity.

## Prerequisites

Before you start, confirm the following:

- You have a Microsoft Entra ID (Azure AD) account with the **Application Administrator**, **Cloud Application Administrator**, or **Global Administrator** role. This role lets you grant tenant-wide consent to the Cato application in step 1. Cato's application only requests a basic sign-in permission, so Application Administrator or Cloud Application Administrator is the least-privileged option and is sufficient
- You have **Power Platform Administrator** or **Global Administrator** access at the tenant level. This is a separate, Power Platform-specific permission rather than an Entra ID app registration, and it lets you register the Cato application as a management application in step 2 and enable Agent Sessions in step 3
- You have access to the Azure subscription associated with Copilot Studio, to open a Cloud Shell session in step 2
- You can run PowerShell commands in Azure Cloud Shell, to run the registration script in step 2

Setting up this integration is a four-step process, and the steps are often completed by different people. In step 1, an Entra ID admin adds the Cato application to the tenant. In steps 2 and 3, a Power Platform admin registers the Cato application as a management application and enables Agent Sessions. In step 4, a Cato admin finishes the integration in the CMA.

## Step 1: Connect Cato to Microsoft Entra ID

Cato registers a multi-tenant application in Microsoft Entra ID. To connect the integration, an Entra ID admin opens the Cato Networks admin consent link, which adds the application to your tenant as an Enterprise Application and grants it consent.

To connect Cato to Microsoft Entra ID:

1. Open the [Cato Networks admin consent link](https://login.microsoftonline.com/organizations/adminconsent?client_id=0f5bb78b-ad8f-454a-a7bc-3c6bb5b1e6c8&state=15021). Sign in with the administrator account described in the prerequisites when prompted. Microsoft displays a consent screen for the **Cato Networks AI Security Integration** application.
2. Click **Accept**.

## Step 2: Register Cato as a Management Application in Power Platform

This step registers the same Cato application from step 1 as a management application with Power Platform. Normally, an application needs a Dataverse application user added to every environment before it can read data there. Registering it as a management application grants it read access to Power Platform environments and Dataverse across the whole tenant instead, which lets Cato read Agent configurations and Agent Sessions without that per-environment setup. You register the application using PowerShell in Azure Cloud Shell, and the registration script requires your Microsoft Entra ID tenant ID.

### Get the Tenant ID

To get your Microsoft Entra ID tenant ID:

1. In the Azure portal, go to **Microsoft Entra ID**.
2. On the **Overview** page, under **Basic Information**, copy the **Tenant ID**. You use this value in the registration script and later to finish the integration in Cato.

### Run the Registration Script

To register the management application:

1. In the Azure portal, open **Cloud Shell**.
2. Select **PowerShell**.
3. Select the subscription associated with Copilot Studio and click **Apply**.
4. Run the following commands, and replace `<YOUR-TENANT-ID>` with the tenant ID you copied earlier:

```powershell
$tenantId = "<YOUR-TENANT-ID>"

az login --scope "https://api.bap.microsoft.com/.default"
# Complete the sign in process by following the link and inputting the code, and select the relevant subscription

$token = az account get-access-token `
  --scope "https://api.bap.microsoft.com/.default" `
  --tenant $tenantId `
  --query accessToken -o tsv

$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

$body = "{}"

$uri =
      "https://api.bap.microsoft.com/providers/" +
      "Microsoft.BusinessAppPlatform/adminApplications/" +
      "0f5bb78b-ad8f-454a-a7bc-3c6bb5b1e6c8?api-version=2020-10-01"

Invoke-RestMethod -Method Put -Uri $uri -Headers $headers -Body $body
```

The `Invoke-RestMethod` command returns the registered `applicationId`, which confirms the management application registered successfully:

```text
applicationId
-------------
0f5bb78b-ad8f-454a-a7bc-3c6bb5b1e6c8
```

## Step 3: Enable Agent Sessions

Enabling this setting lets Cato view Agent Sessions for Copilot Studio agents in an environment. Enable it for every relevant environment in the tenant. The environment can't be a developer environment. Enabling this setting requires **Power Platform Administrator** access, or the **System Administrator** security role in that environment.

To enable Agent Sessions for an environment:

1. In the **Power Platform admin center**, go to **Manage** > **Environments** and select the environment.
2. Select **Settings**.
3. Expand **Product** and select **Features**.
4. Under **Copilot Studio agents**, enable **Allow conversation transcripts and their associated metadata to be saved in Dataverse (required for enhanced reporting)**.

## Step 4: Finish the Integration in the CMA

To finish the integration, a Cato admin enters the Microsoft Entra ID tenant ID you copied earlier.

To finish the integration in the CMA:

1. From the navigation menu, select **AI Security** > **Integrations**.
2. On the **Copilot Studio** tile, click **Connect**.
3. In the **Azure AD Tenant ID** field, enter the tenant ID you copied.
4. Click **Test Connection**. You can save the integration only after the test succeeds.
5. Click **Save**.

## Data Refresh

After you connect the integration, Cato fetches data from Copilot Studio immediately, and then again every hour. Expect updated data in the CMA up to an hour after a change in your environment.

## Review the Requested Permissions

| Permission | Access |
| --- | --- |
| Management application | Enables Cato to read Power Platform environments and access Dataverse, and thus read Agent configurations and Agent Sessions. |
