---
title: "Integrating Cato Events with Microsoft Sentinel"
slug: "integrating-cato-events-with-microsoft-sentinel"
updated: 2026-08-16T11:41:05Z
published: 2026-08-16T11:41:05Z
canonical: "knowledge.catonetworks.com/integrating-cato-events-with-microsoft-sentinel"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato Events with Microsoft Sentinel

## Overview

Use this Microsoft Sentinel integration to include Cato event data in your existing monitoring, correlation, and investigation workflows.

Cato offers two types of integration with Microsoft Sentinel. Each approach offers distinct advantages depending on your goals and environment:

- **Native turnkey integration** - Cato sends events directly to Sentinel, automatically mapped to Sentinel’s data model
- **Custom GitHub integration** - For advanced or non-standard schema needs, available from the [Cato GitHub repo](/v1/docs/introduction-to-the-cato-github-account)

This document covers the native turnkey integration. [A comparison with the custom GitHub integration is included below](/v1/docs/integrating-cato-events-with-microsoft-sentinel#choosing-between-the-native-turnkey-and-custom-github-integration-methods).

### Process and Owners

| **Step** | **What happens** | **Owner** |
| --- | --- | --- |
| 1. [Entra ID admin consent](/v1/docs/integrating-cato-events-with-microsoft-sentinel#step-0-—-entra-id-admin-consent-before-the-master-connector) | One-time OAuth consent granting Cato's app the ability to create app registrations in your tenant. | Customer (Entra ID admin) |
| 1. [Tenant connector approval](/v1/docs/integrating-cato-events-with-microsoft-sentinel#step-1-master-connector-onetime-prerequisite) | Approve Cato's tenant connector in the CMA (no data access granted yet). | Customer |
| 1. [Sentinel Connector Setup](/v1/docs/integrating-cato-events-with-microsoft-sentinel#step-3-sentinel-connector-setup) | (a) [App creation](/v1/docs/integrating-cato-events-with-microsoft-sentinel#app-creation) - Cato creates a per-customer app registration (the 0–100% loader in the CMA). | Cato (automatic) |
| (b) [ARM deployment](/v1/docs/integrating-cato-events-with-microsoft-sentinel#arm-template-deployment-deploy-to-azure) - You deploy the pre-populated ARM template in you Azure environment; this is where permissions are actually granted and Sentinel resources are provisioned. | Customer |
| 1. [Ongoing schema updates](/v1/docs/integrating-cato-events-with-microsoft-sentinel#step-3-ongoing-schema-management) | Cato updates the DCR mapping and table columns as new event fields ship, only while its Service Principal retains the roles granted at deployment | Cato (automatic, conditional) |

### Prerequisites

- A Microsoft tenant integration already configured in the CMA, under **Resources > Integrations > Configured Integrations**. This is the parent connector for Microsoft

applications. Configure it once and reuse it across all Microsoft integrations.
- **Editor** permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).
- An existing Log Analytics workspace in Sentinel to receive Cato events.
- An Azure account with permission to deploy ARM templates and grant role assignments in the target subscription and resource group.
- Review the prerequisites for all Cato event integrations in [Getting Started with Event Integrations](/v1/docs/getting-started-with-event-integrations).

## Understanding the Integration’s Architecture

Understanding the underlying model helps explain why certain steps exist, and what to check if events aren't flowing as expected.

This is a high-level architecture diagram:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/cato_sentinel_integration_fixed_v4.png)

### Step 1: Entra ID admin consent (before the tenant connector)

Approving the tenant connector triggers an OAuth consent prompt against your Microsoft Entra tenant. Before your Entra ID admin approves this, they should know exactly what is being granted:

- The only Microsoft Graph permission requested is `Application.ReadWrite.OwnedBy`. It grants Cato's multi-tenant application two capabilities, and only for applications the tenant connector itself creates:
  - The ability to create new app registrations in your tenant.
  - Read/write access, at any time, to the applications it created, **not** to any other application in your tenant.
- It does not grant blanket tenant access. Newly created applications start with zero permissions: no Graph API scopes and no Azure RBAC roles. They cannot do anything until you consent to specific permissions for that connector (for example, through the Sentinel ARM template below, or an OAuth consent screen for other connector types).
- Each application created this way is dedicated to your tenant alone. It is never shared with, or joint across, any other Cato customer.

Tenant-wide admin consent in Microsoft Entra requires one of the following roles:

- **Privileged Role Administrator**, which can consent to any permission for any API
- **Cloud Application Administrator** or **Application Administrator**, which can consent to most permissions but with some exceptions for Microsoft Graph application permissions
- **Global Administrator**, which can also grant consent

**To grant admin consent:**

1. Go to the Entra admin center and navigate to **Identity > Applications > Enterprise applications**.
2. Locate the application
3. Go to **Security > Permissions** and select **Grant admin consent**.

For the full prerequisites and step-by-step instructions, [see the Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent).

### Step 2: Tenant connector (one-time, prerequisite)

Before any Sentinel-specific setup, you approve Cato's tenant connector, shown in the CMA as "Microsoft 365 (New Tenant)". This is backed by Cato's own multi-tenant application, which resides in Cato's tenant, not yours. You can revoke this approval at any time.

Approving it grants Cato only one capability: the permission to create new app registrations inside your tenant. It does not grant those apps any access on its own. Every permission a created app receives still requires your explicit approval, either via OAuth consent or via the ARM template deployment below.

This connector is shared across all Microsoft-family integrations, not just Sentinel. The tenant connector is used by every Cato connector that integrates with a Microsoft product: Sentinel, Intune, CASB/DLP, Defender, and others. You approve the tenant connector once; after that, each time you create a new Microsoft-family connector in the CMA, a separate, dedicated app registration is created in your tenant for that connector specifically. Creating a Sentinel connector does not grant any access related to Intune or other Microsoft products. Each connector gets its own app with its own permissions.

Apps created by the tenant connector authenticate using a certificate (not a client secret). Cato manages certificate rotation and lifecycle automatically. When you delete a connector in the CMA, Cato deletes the corresponding app registration it created for that connector; app registrations don't outlive the connector that created them.

Benefits of the tenant connector model:

- **One-time consent, not one per connector.** You approve the tenant connector once, then adding any future Microsoft-family connector (Sentinel, Intune, CASB/DLP, Defender, etc.) doesn't require a new app registration and consent flow each time: it's created automatically under the existing approval.
- **Automatic cleanup (no orphaned app registrations).** Deleting a connector in the CMA removes the app registration Cato created for it in the same action. There's nothing left behind in your tenant to track down and clean up manually.
- **Certificate-based auth with automatic rotation.** Because Cato creates and manages these app registrations, it also owns certificate rotation for their lifetime. Registering the app yourself would mean taking on that rotation as an ongoing operational task.
- **Zero permissions by default.** Every app the tenant connector creates starts with no API scopes and no Azure RBAC roles. Access is only added in a later, explicit step (an ARM deployment or OAuth consent screen).
- **Per-connector isolation.** Each Microsoft-family connector gets its own dedicated app registration. A Sentinel connector's app has no bearing on an Intune or CASB connector's access, and vice versa.

### Step 3: Sentinel Connector Setup

#### App Creation

When you start a new Sentinel connector in the CMA, the parent connector uses its capability to create a new per-customer app registration in your tenant. This is what the progress loader (0–100%) in the CMA represents. At this point, the app exists but has no permissions and no resources yet.

#### ARM Template Deployment ("Deploy to Azure")

Clicking through takes you to a pre-populated ARM template that you deploy in your own Azure portal, under your own credentials. This is the step where:

- You approve the app's scoped permissions
- Sentinel resources are actually provisioned
- Cato's Service Principal receives its role assignments

Cato never deploys directly into your tenant. Deployment is always customer-initiated and customer-executed. The template provisions:

| Resource | Location | Purpose |
| --- | --- | --- |
| Custom log table | Existing Log Analytics workspace | Target table for Cato event ingestion (suffixed `_CL`). |
| Data Collection Rule (DCR) | Provisioned by the template (the direct kind; no separate DCE resource) | KQL transform and field mapping from raw events to the table schema; ingests directly through the Logs Ingestion API. |
| RBAC role assignments | DCR and Log Analytics workspace | Grants Cato's Service Principal the built-in Monitoring Metrics Publisher role (on the DCR), plus two custom least-privilege roles: one on the DCR, one on the workspace (exact names, scopes, and actions in the Reference section). |

> [!NOTE]
> Note:
> 
> Azure Data Collection Rules now expose their own ingestion endpoint directly, so a separate Data Collection Endpoint (DCE) is no longer required. This is what keeps the template's resource count and permission scope minimal.

### Step 4: Ongoing Schema Management

As Cato's event schema evolves, the DCR and table schema need updating so new fields are ingested.

- This is not automatic on the customer side. New fields do not apply themselves to your DCR or table.
- Cato can already push DCR mapping and table column updates to match the current schema, using the roles granted during ARM deployment.
- This only works while those roles remain active on Cato's Service Principal.

The three role assignments serve two distinct purposes, and removing them has different consequences:

- Removing Monitoring Metrics Publisher (on the DCR) stops data ingestion entirely. This is a full outage, not a degraded mode. No new events reach Sentinel.
- Removing either custom role (DCR Manager / Table Manager) does not stop existing ingestion; it only prevents Cato from applying future schema updates, so new event fields won't appear in your table until the roles are restored.

Recommendation: if your organization runs periodic access reviews, flag Cato's Service Principal for renewal rather than removal.

## Setting Up the Integration

### Creating the Microsoft Tenant Integration (one-time)

> [!NOTE]
> Note:
> 
> As explained in the [prerequisites](/v1/docs/integrating-cato-events-with-microsoft-sentinel#h_01KRV32916QF0ZN4T9DCFEZ72V), the MS tenant connector is a parent connector for other Microsoft Apps. If you have already created this for a different Microsoft integration, you don’t need to repeat it for your Sentinel integration.

**To create the MS Tenant integration:**

1. From the CMA’s navigation menu, select **Resources > Integrations**, and then click the **Configured Integrations** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the Microsoft account and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.

A success page shows that the permissions were applied.
  4. You can close the browser tab and return to the CMA.
7. The Microsoft 365 app now appears under the **Integrated Apps** tab.

### Creating the Sentinel Integration

**To create the Sentinel integration:**

1. From the navigation menu, select **Resources > Integrations**.
2. On the **Configured Integrations** tab, click **New**. The **New Integration** panel opens.
3. Select **Microsoft Sentinel** and configure the following fields:
  - Enter a **Name** for this integration
  - Select the name of the MS tenant integration in the **Connector Tenant** field
  - Enter your existing **Log Analytics Workspace Name** that receives the data in Microsoft Log Analytics
  - Enter a new **Log Analytics Table Name** to hold the data in the Log Analytics Workspace with this name (Cato appends `_CL`)
  - Define how many days you want Microsoft to retain Cato data in the **Table Retention Days** field
  - Optional: Add filters to control which Cato events are sent to Microsoft Sentinel, [as described below](/v1/docs/integrating-cato-events-with-microsoft-sentinel#configure-your-filters)
4. Click **Save** to deploy the integration to Microsoft. **Note:** You now have 10 minutes to complete the setup in Microsoft.
5. A browser tab opens and directs you to **authorize** the creation of the integration in Microsoft. **Note**: You must authorize the integration with the same tenant used to create the MS tenant integration. The signed-in user must have permission to create resources in that tenant.
6. In the Microsoft portal, select the resource group and region that contain the target Log Analytics workspace, and click **Review + Create**.
7. Click **Create** to start the deployment.
8. When the deployment is complete, you can close the Microsoft tab.
9. In the CMA, refresh the **Integrations** page. The integration status appears in the **Integrated Apps** tab.

### Verifying the integration is working

After setup, confirm:

- The new table (with the `_CL` suffix) appears in your Log Analytics workspace under Tables.
- The connector status in the CMA's Integrated Apps tab shows as connected / healthy.
- Sample events appear in the table within a few minutes of traffic. Query with `&lt;YourTableName&gt;_CL | take 10` in Log Analytics.
- In Azure, Cato's Service Principal still holds its granted roles on the DCR and table resources.

### Configure Filters

Use filters to control which Cato events are exported to Microsoft Sentinel. This helps reduce ingestion costs, minimize noise, and focus investigations on the events that are most relevant to specific sites, users, or regions. You can also use filters to route different subsets of events to different SIEM environments.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36659121973661.png)

Use filter groups to define filters based on any [Event Field](/v1/docs/understanding-event-fields) or combination of fields. Conditions within each group use AND logic. OR logic is applied between groups. The filters in the screenshot configure the integration to export:

- Events that **originate** from Paris or Madrid, are of **sub-type** Internet Firewall, and resulted in **actions** other than Monitor or Prompt
- **Username** contains Test

## Choosing Between the Native Turnkey and Custom GitHub Integration Methods

| Consideration | Native Turnkey | Custom GitHub |
| --- | --- | --- |
| Maintenance | Fully maintained and supported by Cato | Self-maintained |
| Schema mapping | Automatic, Cato ↔ Sentinel | Customizable |
| Scale | No API-based limitations; handles high volume | Subject to API limits |
| Filtering | Built-in filter groups | Custom logic required |
| Architecture | **Push**-based: Cato pushes events directly to your DCR's ingestion endpoint | **Pull**-based: an Azure FunctionApp deployed in your tenant polls the Cato API on a schedule and loads the results into Log Analytics, which is why it is subject to API limits |
| Best for | Standard event types, minimal configuration | Custom data sources or non-standard processing logic |

## Known Limitations

- **Large event limitation:** Some XOps events can include extensive story information in the raw_data field, which may cause the event to exceed Microsoft Sentinel ingestion size limits (approximately 1 MB). When this occurs, Cato still forwards the event to Sentinel, but omits the raw_data field to maintain compatibility with Sentinel ingestion requirements.
- **Schema update dependency:** ongoing schema updates depend on Cato's Service Principal retaining its granted roles. If your organization runs periodic

access reviews, flag this Service Principal to avoid unintentional role removal breaking future ingestion.

### 

### 

---

### FAQ

#### What's the difference between the tenant connector and the Sentinel connector?

The “Microsoft 365 (New Tenant)” connector is a one-time, tenant-wide consent that lets Cato create app registrations in your tenant. It grants no data access by itself. Each Sentinel connector you create afterward is a separate app registration under that umbrella, and its actual permissions are granted only when you deploy its ARM template.

#### Can I revoke the tenant connector after setting up Sentinel integrations?

Yes, but doing so removes Cato's ability to create new app registrations going forward. Existing Sentinel connectors and their already-granted role assignments are not automatically revoked by this action. Check the relevant app registrations in Azure directly if you want to fully remove access.

#### What happens if I accidentally remove Cato's Service Principal roles after deployment?

It depends which role. Removing the Monitoring Metrics Publisher role (on the DCR) stops data ingestion entirely, resulting in a full outage. Removing either custom role (DCR Manager / Table Manager) doesn't stop existing ingestion; it only blocks future schema updates, so the failure isn't immediate or obvious. It surfaces later, when a new event field ships and doesn't appear in your table. Re-grant the roles listed in the Reference section to restore it.

#### What happens if I miss the 10-minute ARM deployment window?

The CMA-side integration record is left in an incomplete state and can't be resumed. Delete it and perform the Sentinel integration creation again.

#### Does deleting the integration in the CMA remove the resources in Azure?

No. Deleting the integration in the CMA does not remove the table, DCR, or role assignments created in Microsoft. Clean those up directly in Azure if needed.

#### Can I have multiple Sentinel integrations from one Cato account?

Yes. Each is set up independently through its own app registration and ARM deployment, all under the same tenant connector consent.

#### Why did an event arrive without its raw data field?

Some XOps events carry large story payloads in `raw_data` that can exceed Sentinel's ingestion size limit (approximately 1 MB). When that happens, Cato still forwards the event but omits `raw_data` to stay within Sentinel's limits. See [Known Limitations](/v1/docs/integrating-cato-events-with-microsoft-sentinel#h_01KRV32917F00J1ZW7ZM5X9FMV).

#### Does approving the tenant connector only affect the Sentinel connector?

No. The tenant connector is shared across every Microsoft-family Cato connector (Sentinel, Intune, CASB/DLP, Defender, and others). Approving it once means each new Microsoft-family connector you create afterward gets its own dedicated app registration and permissions.

#### What happens to the app registration if I delete the connector?

Cato deletes the app registration it created for that connector at the same time. App registrations created by the tenant connector never outlive the connector they were created for.

#### Does Cato use client secrets to authenticate these apps?

No. Apps created by the tenant connector authenticate using a certificate, not a client secret. Cato manages certificate rotation automatically.

#### Can we register the app ourselves instead of using the tenant connector?

In principle, yes, you could create the app registration yourself and provide Cato with a client ID and secret. This path is not currently supported in the CMA UI. It would also mean taking on certificate and secret rotation yourselves, rather than having Cato manage it automatically.
