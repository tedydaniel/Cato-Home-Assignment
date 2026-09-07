---
title: "Using MIP Sensitivity Labels in your Cato DLP Policy"
slug: "using-mip-sensitivity-labels-in-your-cato-dlp-policy"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/using-mip-sensitivity-labels-in-your-cato-dlp-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using MIP Sensitivity Labels in your Cato DLP Policy

This article explains how to use Microsoft Sensitivity Labels from the Microsoft Information Protection (MIP) framework in your Cato DLP policy.

## Overview of Using MIP Labels with Cato DLP

You can simplify your data control management by leveraging your existing Microsoft Information Protection policy for use with Cato DLP. By using MIP labels as data types, you can design a clear and manageable DLP policy consistent with your MIP policy. This lets you use MIP labels to secure your sensitive information beyond the Azure ecosystem in all traffic handled by Cato.

### High Level Overview of Working with MIP Labels

This is a high level description of the workflow for using MIP labels with DLP:

1. Create **Sensitivity Labels** in the Cato Management Application.
2. Add the labels to **Content Profiles**.
3. Create DLP rules to manage access to content for different users and groups according to **Sensitivity Labels**.

For example, if you have files with the MIP label Classified, create the label in your Cato DLP policy and add it to the **Content Profile** Restricted Documents. Then define a DLP rule that blocks access for groups of users without sufficient security clearance.

### Adding MIP Labels to the DLP Policy

There are two ways you can add MIP labels to the DLP policy in the Cato Management Application:

- Automated import with an API connector that retrieves the labels from your Microsoft 365 account
- Manual configuration by entering the required label data

### Scanning Files with Sensitivity Labels

The DLP engine scans for the defined labels in the file metadata and not in the actual content, which helps reduce false positive results. The engine enforces the **Sensitivity Label** according to the **Label ID** you configure, not according to the **Name**. When you manually configure a label, make sure that the **Label ID** of the **Sensitivity Label** exactly matches the MIP label ID.

For more information about finding the MIP label IDs for your organization's account, see the [Microsoft documentation](https://learn.microsoft.com/en-us/powershell/module/exchange/get-label?view=exchange-ps).

### Known Limitations

- DLP scanning for sensitivity labels is not supported for encrypted DOCX files.
- For information on the file requirements, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service)

## Automatically Importing MIP Labels

You can configure an API connector in the Cato Management Application to automatically retrieve your existing Microsoft sensitivity labels to use as custom DLP data types. The connector fetches all the necessary MIP label data at the same time, and makes the labels available for easy configuration as custom data types. If you make changes to the sensitivity label policy in your Microsoft 365 account, you can use the connector to retrieve your latest sensitivity label configuration, and then update your Cato DLP data types to match.

### Overview of the Microsoft Connectors

To configure Cato's MIP labels connector to fetch your organization's sensitivity labels, first you need to configure the Microsoft 365 connector as the parent app to give read permissions for the MIP label connector. The parent app only has permissions to manage the Microsoft connectors. After configuring the Microsoft 365 connector, you can configure a MIP labels connector to retrieve the sensitivity labels.

If you want to import sensitivity labels from the MIP policies of different sub-organizations within your organization, create a separate Microsoft 365 connector for each relevant Azure tenant, and then configure a MIP labels connector for each tenant.

#### Prerequisites

- The Microsoft 365 connector requires an admin with the global admin role to give permissions to Cato's MIP labels connector.

#### Required Permissions for the MIP Labels Connector

To let the MIP labels connector retrieve the sensitivity labels from your Microsoft 365 account, the connector gives Cato the following permissions and actions with Microsoft 365:

- Connect to the Microsoft APIs and read all published sensitivity labels and label policies for an organization
- Sign in and read user profile

### Configuring the Microsoft Connectors

Configure a parent Microsoft 365 connector and then define a MIP labels connector for the Microsoft 365 account with the sensitivity labels you want to use.

If your organization configured a [Saas Security API](/v1/docs/what-is-the-data-protection-api) policy for Microsoft apps, the relevant parent Microsoft 365 connector may already be configured and appear in the Data Types & Profiles page. In this case, you only need to configure a MIP labels connector.

#### Configuring the Microsoft 365 Connector

Use the Cato Management Application to create the Microsoft 365 SaaS application connector for the Azure tenant with the MIP sensitivity labels you want to use. You must have the correct credentials to authenticate to Microsoft 365 to add the connector to your Cato account.

![MIP_DLP_Connectors_Settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002079914141.png)

**To configure the Microsoft 365 parent connector:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and in the **Settings** tab select **DLP Connectors**.
2. Click **New**. The **New Connector** panel opens.
3. From the **SaaS Application** drop-down menu, select the **Microsoft 365** app.

![MIP_New_Connector_MS365.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002107592733.png)
4. Enter a unique **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.

![MIP_Labels_Parent_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002079957405.png)
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002107642525.png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **DLP Connectors Settings** screen.

It can take Microsoft Azure several seconds to process the request, so if the **Status** shows **Pending user consent**, refresh the browser.

#### Configuring the MIP Labels Connector

Use the Cato Management Application to create the MIP Labels SaaS application connector for the Azure tenant with the MIP sensitivity labels you want to use. You must have the correct credentials to authenticate to Microsoft 365 to add the connector to your Cato account.

> [!NOTE]
> Note:
> 
> When you create an API connector for a Microsoft 365 app, the connector creates an authentication certificate that is valid for 3 months, and renews the certificate 7 days before expiration.

**To configure the MIP Labels connector:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and in the **Settings** tab select **DLP Connectors**.
2. Click **New**. The **New Connector** panel opens.
3. From the **Saas Application** drop-down menu, select the **MIP Labels** app.

![MIP_New_Connector_MIP_Con.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002080003997.png)
4. From the **Connector Tenant** drop-down menu, select the parent Microsoft 365 connector for the tenant with the labels you want to use.
5. Enter a unique **Connector Name** for the MIP Labels connector.
6. Click **Save**.

Wait at least 30 seconds for Microsoft to create the Cato connector app in Azure.
7. After the connector is successfully created, click **Authorize**.

![MIP_Labels_SuccessCreate_Authorize.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002068326685.png)

A new browser tab opens to the Microsoft 365 app.
8. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Wait at least 30 seconds for Microsoft to create the Cato connector app in Azure before you select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.

![MIP_Labels_MIP_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002080050589.png)
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002107642525.png)

You can close the browser tab and return to the Cato Management Application.
9. The MIP Labels SaaS application is added to the **DLP Connectors Settings** screen.

It can take Microsoft Azure several seconds to process the request, so if the **Status** shows **Pending user consent**, refresh the browser.

#### Understanding the Connector Status

The **Status** column on the DLP Connectors Settings screen shows the status of the connection between the Microsoft app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and it is working correctly
- **Pending user consent** - Permissions have not been granted to let Cato access the Microsoft 365 app. To resolve this issue, refresh the browser. If **Status** changes to **Connected**, the issue is resolved, if **Status** doesn't change, delete and recreate the connector.
- **Error** - There is a connectivity, permissions, or other issue with the Microsoft connector. Delete and recreate the connector.

### Importing MIP Labels to the DLP Policy

Retrieve the MIP sensitivity labels from your Microsoft 365 account and select the labels you want to use as data types in your Cato DLP policy.

![DLP_Sensitivity_Labels.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002107734557.png)

**To import MIP labels to the DLP policy:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and select the **Data Types** tab.
2. In **Sensitivity Labels**, click **New**. The **Add Sensitivity Label** panel opens.

![MIP_Add_Sensitivity_Label_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002080104221.png)
3. Select the **Retrieve Labels** option.
4. In the **Choose Connector** drop-down menu, select the MIP Labels connector for the Microsoft 365 tenant you want to retrieve labels from.

The **Imported Label Name** drop-down menu is populated with the retrieved labels.
5. From the **Imported Label Name** drop-down menu, select the label to import. The required fields are automatically filled with the label details.
6. Click **Apply**.

The label is added to the Sensitivity Labels list and can be added to a Content Profile as a custom DLP data type.

## Manually Configuring MIP Labels in Cato DLP

You can also choose to manually configure MIP labels in the Cato Management Application. This method could be convenient if, for example, you only need a few MIP labels in your Cato DLP policy. Configure the labels under **Sensitivity Labels** in the **Data Types** tab of the Data Types & Profiles page. To configure a new label, enter the details for the label including a **Name**, **Description**, and **Label ID**. Make sure that the **Label ID** you enter exactly matches the MIP label ID.

![DLP_Sensitivity_Labels.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002107734557.png)

**To manually configure a Sensitivity Label:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and select the **Data Types** tab.
2. In **Sensitivity Labels**, click **New**. The **Add Sensitivity Label** panel opens.
3. Select the **Custom Labels** option.
4. Enter the **Name** and **Description** for the label.
5. Enter the same **Label ID** as the MIP label ID.
6. Click **Apply**.

The label is added to the Sensitivity Labels list and can be added to a Content Profile as a custom DLP data type.
