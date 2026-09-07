---
title: "Google Drive: Configuring the SaaS Posture Integration"
slug: "google-drive-configuring-the-saas-posture-integration"
updated: 2026-07-01T12:32:24Z
published: 2026-07-01T12:32:24Z
canonical: "knowledge.catonetworks.com/google-drive-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Drive: Configuring the SaaS Posture Integration

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the Google Drive Integration

To configure the Gmail integration, create a new project.

### Prerequisites

- A Google Workspace tenant with Google Drive enabled
- A Google Workspace Super Admin account

### Step 1: Configure the Integration in the Google Cloud Console

In the Google Cloud Console, create a Service account private key to enter into the CMA.

**To configure the Google Workspace integration:**

1. In your [Google Cloud Console](https://console.cloud.google.com/), click **Select a Project**.
2. Click **New project**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(21).png)
3. Choose a **Name, Organization,** and **Parent resource** and click **Create**.
4. Navigate to **APIs & Services > Library**.
5. Search for **Cloud Identity API.**
6. Click on **Cloud Identity API** and click **Enable**.
7. Search for **Google Drive API.**
8. Click on **Google Drive API** and click **Enable**.
9. Navigate to **IAM & Admin > Service Accounts**.
10. Select the project you created in step two, and click **Create service account**.
11. Add a **Service account ID** and click **Create and continue**.
12. Click **Done**.
13. Click on the service account you created, expand **Advanced settings**.
14. Under **Domain-wide delegation**, copy and save the service account's numeric **OAuth 2.0 Client ID** so it can be used later in the procedure.
15. In the service account you created, navigate to the **Keys** tab.
16. Click **Add key > Create new key**.
17. Choose the JSON key type and click **Create**. A JSON file containing the private key is downloaded.
18. Copy and save the **Private key** so it can be added to the CMA.
19. In the [Google Admin console](https://admin.google.com/), navigate to **Security > Access and Data Control > API control**.
20. Under **Domain wide delegation**, select **Manage Domain Wide Delegation**.
21. Click **Add new**.
22. In the **Client ID** field, paste the numeric **OAuth 2.0 Client ID** you saved above.
23. In the **OAuth scopes** field, paste the following as a single comma-separated line:
  - `https://www.googleapis.com/auth/cloud-identity.policies.readonly,https://www.googleapis.com/auth/drive.readonly`
24. Click **Authorize**.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations.**
2. Click the **Configured Integrations** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add. **Note:** Enter the **Private Key** in JSON format.
5. In the **Capability** drop-down select **SaaS Posture**.
6. Add the details created during step one. **Note**: The JSON and admin email address are the details necessary for the connector creation. The admin email field should include the email of a user with the Super Admin role.
7. Click **Save**.
