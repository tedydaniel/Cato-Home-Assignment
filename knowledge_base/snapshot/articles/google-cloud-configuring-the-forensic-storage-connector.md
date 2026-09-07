---
title: "Google Cloud: Configuring the Forensic Storage Connector"
slug: "google-cloud-configuring-the-forensic-storage-connector"
updated: 2026-07-26T11:07:02Z
published: 2026-07-26T11:07:02Z
canonical: "knowledge.catonetworks.com/google-cloud-configuring-the-forensic-storage-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Cloud: Configuring the Forensic Storage Connector

This article explains how to configure the connector for Google Cloud, so that data generated from Cato can be securely stored.

## Overview

To minimize data exposure and ensure compliance with regulatory requirements, you can create an integration with a third party for the storage of the evidence files.

This is supported for storing data from DLP policy violations. For more information, see [Investigating DLP Violations with Forensic Evidence](/v1/docs/investigating-dlp-violations-with-forensic-evidence).

To configure the integration, you need to:

1. Configure the integration storage application
2. Create the API connector in the CMA

## Configuring the Google Cloud Integration

To configure the Google Cloud integration, create the required configurations in your Google Cloud account, then configure the connector within the CMA.

### Step 1: Configure the Integration in Google Cloud Storage

To configure the Google Cloud integration, create a bucket, create a service account, grant permissions, and create and add permission to a Workload Identity Federation.

**To create a bucket:**

1. In the Google Cloud console, navigate to **Buckets**.
2. Click **Create**.
3. Choose a name for the bucket and click **Create**.
4. Check the **Enforce public access prevention on this bucket** check box and click **Confirm**.

![GCP1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34695200416029.png)

**To create a service account:**

1. Open Google Cloud IAM & Admin and navigate to **Service Accounts**
2. Click **Create service account**.
3. Choose a name for the service account and copy and save the **Service account ID** for a future step.
4. Click **Done**.

**To grant storage object creator permission:**

1. In the Google Cloud console, navigate to **Buckets**.
2. Click on the bucket you created in step 1.
3. In the **Permissions** section, click **Grant Access**.

![GCP2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34695184128157.png)
4. In the **Add Principal** field, enter `&lt;Service account ID&gt;@gcp-datastorage.iam.gserviceaccount.com`

**Note:** The service account ID was created above.
5. In the **Assign Roles** dropdown, choose **Storage Object Creator**.
6. Click **Add another role** and choose **Storage Object Viewer**.
7. Click **Save**.

**To create a workload identity federation:**

1. Open Google Cloud IAM & Admin and navigate to **Workload Identity Federation**.
2. Click **Create pool**.
3. Choose a name for the pool and click **Continue**.
4. Select **AWS** as the provider.
5. Choose a name for the provider, add **428465470022** in the **AWS Account ID** field.
6. Click **Continue**.
7. In **Attribute conditions**, add `assertion.arn.startsWith("arn:aws:sts::428465470022:assumed-role/cato-forensics-integration/")`
8. Click **Save**.
9. Click on the pool that was just created.
10. Copy and save the IAM Principle to be used at a future step.

**To grant workload identity user permission:**

1. Open Google Cloud IAM & Admin and navigate to **Service Accounts**.
2. Click on the service account you created above.
3. On the **Principals with access** tab, click **Grant access**.
4. In the **Add principals** field, paste the IAM Principle created above, and replace:
  - `subject/SUBJECT_ATTRIBUTE_VALUE`

with

`attribute.aws_role/arn:aws:sts::428465470022:assumed-role/cato-forensics-integration`
  - `principal://`

with

`principalSet://`
5. In the **Assign roles** dropdown, choose **Workload Identity User**.
6. Click **Save**.

**To download the access config file:**

1. Open Google Cloud IAM & Admin and navigate to **Workload Identity Federation**.
2. Click on the name of the pool you created above.
3. Click **Grant access**.
4. Choose **Grant access using service account impersonation**.
5. Choose the service account you created above.
6. In the **Principal** field, choose **AWS_role**.
7. In the **Attribute** value, add `assertion.arn.startsWith("arn:aws:sts::428465470022:assumed-role/cato-forensics-integration/")`.
8. Click **Save**.
9. In the Popup window choose the provider you created above.
10. Click **Download config**.

A json file is downloaded - save this file to be added to the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. In the **SaaS Application** dropdown, select GCP GCS.
5. Add these configurations:
  - **Auth** - Service Account
  - **Name** - Choose a name for the integration
  - **Service Account Key** - Upload the config file
  - **Storage** - The bucket name created above
  - **Folder Path** - Choose a folder name
6. Click **Save**.
7. The app is visible on the **Integrated Apps** table with a **Connected** status.
