---
title: "Azure M365 Copilot Integration with AI Security"
slug: "integrating-azure-m365-copilot-with-ai-security"
updated: 2026-07-06T08:14:17Z
published: 2026-07-06T08:14:17Z
canonical: "knowledge.catonetworks.com/integrating-azure-m365-copilot-with-ai-security"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure M365 Copilot Integration with AI Security

AI Security integrates with your M365 Copilot through read-only API access. This integration lets Cato AI Security provide you with comprehensive insights into M365 Copilot AI usage.

## Setting UP Azure AD

AI Security is a multi-tenant Azure application, and is deployed in Azure AD by adding the Cato Enterprise Application to the organization from an admin user who has the correct privileges.

The admin who adds the connection must be assigned to the Global Administrator role. You may also create a new admin account dedicated to the AI Security integration. In this case, make sure that the role is directly assigned to the account, like so:
![01_Azure_M365.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_Azure_M365.png){height="" width=""}

To enable the integration, you must connect the AI Security application and grant it the correct
permissions.

**Note:** If there are no users who are licensed for Microsoft 365 Copilot, no data will be available.

## Connecting AI Security to M365 Copilot

1. Click this [link](https://login.microsoftonline.com/organizations/adminconsent%20?client_id=0dce36c5-bbd6-495c-9e82-eda1b38d58c4%20&state=15021) to give permissions for AI Security to connect to your Copilot tenant.
![02_Azure_M365.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_Azure_M365.png){height="" width=""}


    For the login details, sign in with the administrator account from the previous section.

2. Click **Accept**.

    After the integration is installed, you can see it in the Enterprise applications > All applications
section of the Azure portal.
![03_Azure_M365.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_Azure_M365.png){height="" width=""}
3. {{variable.AI Sec - Integrations}}
3. In **Add M365 Copilot API**, click **Connect**.
![m365_copilot_cma.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/m365_copilot_cma.png){height="" width=""}

4. In the **M365 Copilot API** panel, add the following details:

   - Tenant ID

5. Click **Test Connection** to verify the integration.
6. Click **Connect**.
