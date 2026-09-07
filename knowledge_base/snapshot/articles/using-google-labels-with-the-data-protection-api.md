---
title: "Using Google Labels with the Data Protection API"
slug: "using-google-labels-with-the-data-protection-api"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/using-google-labels-with-the-data-protection-api"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Google Labels with the Data Protection API

This article explains how to add Google Labels as a Data type in a DLP Content Profile that can be used in a with the Data Protection API.

## Overview

Google Labels are metadata that help organize, find, and apply policy to files in Google Drive. To simplify your data control management, you can leverage existing Google Labels as a data type to identify data in with the Data Protection API. This allows you to align DLP enforcement with your existing Google Workspace classification strategy without redefining labels or rules. The DLP engine scans for the defined labels in the file metadata and not in the actual content, which helps reduce false positive results and improves policy evaluation performance.

Google Labels can only be applied to files stored on Google Drive and only supported for out-of-band traffic.

### Prerequisites

- Google Cloud Enterprise License required

## Adding Google Labels to the Data Protection API

To add Google Labels to your Data Protection API, you need to:

1. Configure the integration with Google Drive in the Google Cloud Console and Cato Management Application (CMA)
2. Add the labels to Content Profiles
3. Create DLP rules to manage access to content based on labels

### Step 1: Configure the Integration with Google Drive

To configure the integration with Google Drive, you need to first create a key in the Cloud Console and then add the integration in the Cato Management Application CMA.

#### Configuring the Integration in the Google Cloud Console

In the Google Cloud Console, create a Service account private key to enter into the CMA.

**To configure the Google Drive and Workspace integration:**

1. In your [Google Cloud Console](https://console.cloud.google.com/), click **Select a Project**.
2. Click **New project**.

![Google1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33252182397981.png)
3. Choose a **Name** and **Location** and click **Create**.
4. Navigate to **APIs & Services > Library**.
5. Search for Admin SDK.

![Google_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33252178510749.png)
6. Click on **Admin SDK API** and click **Enable**.

![Google3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33252182603037.png)
7. Navigate to **IAM & Admin > Service Accounts**.

![Labels.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33252171791133.png)
8. Select the project you created in step two, and click **Create service account**.
9. Add a **Service account ID** and click **Create and continue**.
10. In the **Select a role** drop down, choose **Audit Manager Admin** (you can search for this role).

![Google4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33252171883165.png)
11. Click **Done**.
12. Click on the service account you created and navigate to the **Keys** tab,
13. Click **Add key > Create new key**.
14. Choose the JSON key type and click **Create**.

A JSON file containing the private key is downloaded.
15. Copy and save the **Private key** so it can be added to the CMA.
16. In the [Google Admin console](https://admin.google.com/), navigate to **Security > Access and Data Control > API control**.
17. Under **Domain wide delegation**, select **Manage Domain Wide Delegation**.
18. Click **Add new**.
19. Add the **Client ID** of the Service Account. You can find this in the Service Account page.
20. Add these scopes:
  1. `https://www.googleapis.com/auth/drive.labels.readonly`
21. Click **Authorize**.
22. Navigate to [https://console.cloud.google.com/projectselector2/apis/api/drivelabels.googleapis.com/overview](https://console.cloud.google.com/projectselector2/apis/api/drivelabels.googleapis.com/overview)
23. Click **Select a project** and click the Project you created.
24. On the Drive Labels API page, click **Enable.**

#### Configuring the Integration in the Cato Management Application

Once you have created the Private Key, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.

**Note:** Enter the **Private Key** in JSON format.
5. In the **Capability** drop down select Sensitivity Labels.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

### Step 2: Add the Labels to Content Profiles

After you have created the integration, you can add the Labels to a Content Profile. For more information, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).

**To add Labels to Content Profiles:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and select the **Data Types** tab.
2. In **Sensitivity Labels**, click **New**. The **Add Sensitivity Label** panel opens.
3. Select the **Retrieve Labels** option.

![SL.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33252171991453.png)
4. In the **Choose Connector** drop-down, select the Google connector.
5. In the **Imported Label Name** drop-down, choose the label you want to add to a Content Profile.
6. (Optional) Click **Validate Sensitivity Label** to upload and scan a test file to validate the label.
7. Click **Apply**.
8. On the **DLP Profiles** tab, click **New**.

The **Add Content Profile** panel opens.
9. Add a **Name** for the Profile.
10. In the **Data Types** section, click **Add** and choose **Google Labels**.

![SL2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33252182897053.png)
11. Choose the Label to add to the Profile.
12. Click **Apply** then **Apply**.

### Step 3: Create DLP Rules to Manage Access to Content Based on Labels

After you have created Content Profiles with Google Labels, you can add them to Data Protection Rules

**To create DLP Rules:**

1. From the navigation menu, click **Security > App & Data API**.
2. On the **Data Protection** tab, click **New**.

The **New Rule** panel opens.
3. In the **Application Connector** drop-down, choose **Google Drive**.
4. Configure the rule as required. In the **Content Profiles** section, choose the profile you created in step 2.
5. Click **Save**.
