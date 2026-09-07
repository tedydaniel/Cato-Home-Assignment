---
title: "Provisioning Users from Google Workspace"
slug: "provisioning-users-from-google-workspace-ea"
updated: 2026-08-31T08:57:37Z
published: 2026-08-31T08:57:37Z
canonical: "knowledge.catonetworks.com/provisioning-users-from-google-workspace-ea"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Provisioning Users from Google Workspace

## Overview

The Google Workspace integration lets you provision users and groups from Google Workspace to your Cato account.

User information is securely and continuously synced from Google Workspace to Cato to create and update users and groups. This helps keep your Cato user directory aligned with your Google Workspace directory.

When user details change in Google Workspace, the changes are synced to Cato. For example, when an employee leaves the company and their Google Workspace account is suspended or removed, this change is reflected in Cato.

After users are provisioned from Google Workspace, the user can be identified by user awareness. For more information, see [Using Cato Identity Agents for User Awareness.](/v1/docs/using-cato-identity-agents-for-user-awareness)

### Supported Capabilities

The capabilities supported by this integration are:

- **Full user directory sync:** Every user with profile details, status, department, and org unit
- **Full group directory** **sync**: Every group with description and member list, including nested groups
- **Real-time user lifecycle events:** Updates for users created, modified, or deleted
- **Real-time group membership changes:** Updates for members added or removed from groups
- **Admin audit trail:** The creation and deletion of the connector are recorded in the audit trail

### Viewing Users Provisioned from Google Workspace

You can identify users provisioned from Google Workspace on the **Access > Users** page. On the **User Directory** tab, the **Source** column displays **Integration** for a user provisioned from Google Workspace.

If a user has been deleted in Google Workspace, they are still visible on the **Access > Users** page, with a **Disabled** status. If required, they can be deleted from the Cato Management Application. For more information, see [Working with Users](/v1/docs/working-with-users).

If a manually created user matches the email address of a user provisioned from Google, the user is associated to the Google integration directory and is on longer considered a manual user.

## Configuring the Google Workspace Integration for User Provisioning

To configure the Google Workspace integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

### Prerequisites

- Google Workspace Business Standard, Business Plus, Enterprise, or Education license
- A Super Admin account is required to configure domain-wide delegation

### Known Limitations

- Up to 50,000 users and 50,000 groups can be synced
- Provisioning from Google Workspace cannot coexist with provisioning from another IdP with SCIM or LDAP
- Multiple Google Workspace connectors for user provisioning are not supported

### Step 1: Configure the Integration in the Google Cloud Console

In the Google Cloud Console, create a Service account private key to enter into the CMA.

**To configure Google Workspace Integration:**

1. In your [Google Cloud Console](https://console.cloud.google.com/), click **Select a Project**.
2. Click **New project**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(9).png)
3. Choose a **Name, Organization** and **Parent resource** and click **Create**.
4. Navigate to **APIs & Services > Library**.
5. Search for Admin SDK.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(12).png)
6. Click on **Admin SDK API** and click **Enable**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(11).png)
7. Navigate to **IAM & Admin > Service Accounts**.
8. Select the project you created in step two, and click **Create service account**.
9. Click **Create and close**.
10. Click on the service account you created and navigate to the **Keys** tab,
11. Click **Add key > Create new key**.
12. Choose the JSON key type and click **Create**.

A JSON file containing the private key is downloaded.
13. Copy and save the **Private key** so it can be added to the CMA.
14. In the [Google Admin console](https://admin.google.com/), navigate to **Security > Access and Data Control > API control**.
15. Under **Domain wide delegation**, select **Manage Domain Wide Delegation**.
16. Click **Add new**.
17. Add the **Client ID** of the Service Account. You can find this in the Service Account page.
18. Add these scopes:
  1. [https://www.googleapis.com/auth/admin.directory.user.readonly](https://www.googleapis.com/auth/admin.directory.user.readonly)
  2. [https://www.googleapis.com/auth/admin.directory.group.readonly](https://www.googleapis.com/auth/admin.directory.group.readonly)
  3. [https://www.googleapis.com/auth/admin.reports.audit.readonly](https://www.googleapis.com/auth/admin.reports.audit.readonly)
19. Click **Send Request.**

If multi-party approval is enabled, the admin who manages requests must provide authorization before progressing to step 2. To view submitted requests navigate to **Security > Authentication > Multi-party approval requests.**
20. Click **Authorize**.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. In the **Integration** drop-down, select **Google Workspace**.

**Note:** Enter the **Private Key** in JSON format.
5. In the **Capability** drop-down, select **User Provisioning**.
6. In the **Auth** drop-down, select **Service Account**.
7. In the **Admin email** field, add the email address of a user with the Super Admin role.
8. Add the JSON private key file you created in step 1.
9. Click **Save**.
10. The app is visible on the **Integrated Apps** table with a **Connected** status.

## Deleting the Google Workspace Integration

If you delete the integration, synced users and groups are still visible in the CMA, and changes made in Google Workspace to users and groups are no longer synced.

**To delete the Google Workspace integration:**

1. Navigate to the **Integrations** page.
2. On the **Configured Integrations** tab, click the three dots on the Google Workspace User Provisioning row.
3. Click **Delete**.

## Understanding Events from Provisioning Users

The CMA generates events with every record update. You can identify these events by the:

- **Type:** System
- **Sub-type:** Integration

For more information, see [Analyzing Events in Your Network.](/v1/docs/analyzing-events-in-your-network)
