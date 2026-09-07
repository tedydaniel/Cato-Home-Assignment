---
title: "Configuring Exact Data Match Detectors for AI Security (EA)"
slug: "configuring-exact-data-match-detectors-for-ai-security"
tags: ["AI Sec - Users"]
status: "update"
updated: 2026-09-07T07:40:26Z
published: 2026-09-07T07:40:26Z
canonical: "knowledge.catonetworks.com/configuring-exact-data-match-detectors-for-ai-security"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Exact Data Match Detectors for AI Security (EA)

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

## Overview

Exact Data Match (EDM) detectors let you detect sensitive data that is specific to your organization. Predefined AI Security detectors identify sensitive data types, such as Social Security numbers, using Cato's detection engine and semantic analysis to understand when content in a prompt appears to contain sensitive information. EDM detectors add another layer of precision by identifying exact values from a dataset that you provide.

For example, a predefined SSN detector can identify when a prompt contains content that appears to include a Social Security number. An EDM detector can identify when the prompt contains a Social Security number from your organization's uploaded dataset. This helps you enforce AI security controls for customer, employee, or business records that are known to be sensitive to your organization.

After you create an EDM detector, you can add it to an AI Security Engine Profile and use it in runtime policies to monitor, anonymize, or block prompts that contain matching data.

### Use Case - Protecting Customer SSNs in AI Prompts

ABC Company stores sensitive customer records, including customer Social Security numbers. The company uses AI applications to help employees answer customer questions and summarize internal information, but it needs to prevent customer SSNs from being exposed to AI vendors.

ABC Company uses the predefined AI Security SSN detector to monitor when employees include content that appears to contain Social Security numbers in prompts. However, the company wants stricter enforcement for SSNs that belong to its own customers. With an EDM detector, ABC Company can detect exact matches from its uploaded customer SSN dataset and block prompts that contain those values before they reach the AI vendor.

This helps admins apply more precise controls for organization-specific sensitive data, while continuing to use predefined detectors for broader monitoring of general sensitive data types.

## Create an EDM Detector

### Before You Begin

Before you create an EDM detector, prepare the dataset file that contains the values you want the detector to match. The file schema, selected column, data type, and **Key** are used to define the EDM detector and can't be changed after you create it.

After you create an EDM detector, you can only update the dataset. This means you can add or remove values from the file, but you can't change the **Key**, column mapping, or data type for the existing detector. To use a different **Key**, column mapping, or data type, create a new EDM detector.

EDM detectors support the following behavior:

- Currently, EDM detectors support matching values with the SSN data type
- Maximum file size for UI upload is 8 MB
- Supported file types are CSV, TSV, and PSV
- The first row of the file must include column names in plain text
- File content should be hashed
- You must provide the **Key** used to hash the file
- The **Key** can't be changed later for the same EDM detector
- Currently, EDM detectors support matching for SSNs

### Preparing the EDM Dataset File

Before you upload a dataset, create a source file in CSV, TSV, or PSV format. The source file contains the values before hashing, and the first row must include the column names in plain text. Use commas to separate values in a CSV file, tabs in a TSV file, or pipes (`|`) in a PSV file.

For example, the following PSV source file contains three columns and three rows of data. The values are examples to show the file format. For SSN matching, use the SSN values you want the detector to match.

**Source file:**

```
column1|column2|column3
data1a|data2a|data3a
data1b|data2b|data3b
data1c|data2c|data3c
```

Hash each data value using HMAC-SHA256 and the same HMAC key. Replace each value with its hexadecimal hash while preserving the rows, column order, and separators. The column names in the first row must remain in plain text and must not be hashed.

For example, when you use `key123` as the HMAC key, the source file above produces the following hashed file:

**Hashed file:**

```
column1|column2|column3
f4ae0c01b6dc9e180418254a8b64d80256274c43b227b0b7dc2e8fade07503d5|871735dc3870a1fd751fb16b4567f5cf1898a2aa9d3ccb06323493b16196e3c7|b35dd0c42abd532722065ed9908beb964b37e584b9897b312ae93c08a9ba13e8
90ccd6988e7254bb310bb8d3f8ed1ff7e926876ad36c3a43a4f0aebb7fc9b9c1|9a6d2055728933e1d2a5bd9b25efb25b75e52b98a12c6014cfca501ddda37605|66c5715f91c8b089ff8a79f0f42db4bc470dd6436f120e0244175d94609d1527
1e4b69d7cc7f6abfd6707cc6bd3f07ce470ef271322d10091437e5be1b855f52|024cccebb541675d31f14562786c5d777d5ae0303702671ab1c4cb9595ee6390|2ddbc26ad9211a30a682e553289caa422d539cfad56f1a43ada68c741df387c7
```

When you initially create the EDM detector in the CMA, upload the hashed file without gzip compression. Don't upload the plain-text source file. In **Key**, enter the HMAC key used to hash the values. For the example above, enter `key123`.

To update the dataset using the API through S3, compress the hashed file with `gzip` before uploading it. For example, if you save the hashed file as `hashed-file.psv`, run the following command:

```
gzip hashed-file.psv
```

Upload the resulting `hashed-file.psv.gz` file to the pre-signed URL, as described in **Updating an EDM Dataset Using the API**. The updated dataset must use the same HMAC key, schema, and column mapping as the initial dataset.

### Creating an EDM Detector

1. From the navigation menu, click **AI Security** > **Engine Profiles**.
2. Select the **EDM Detectors** tab.
3. Click **New EDM Detector**.
4. In **Detector name & description**, enter a **Name** for the detector.
5. Optional: Enter a **Description**.
6. In **Upload the file to match against**, upload the dataset file that contains the values you want to detect.
7. In **Key**, enter the key used to hash the file content.
8. In **Column Mapping**, select the column that contains the values to match.
9. Select the data type for the column.

Currently, EDM detectors support SSN matching.
10. Save the EDM detector.

### Implementing EDM Detectors in Engine Profiles

After you create an EDM detector, add it to an AI Security Engine Profile so you can use it in runtime policies.

1. From the navigation menu, click **AI Security** > **Engine Profiles**.
2. Create a new Engine Profile or edit an existing profile.
3. Click **Add Detectors** > **Custom Detectors**.
4. Under **Custom Detector Type**, select **EDM**.
5. Select the EDM detector from the list.
6. Click **Save**.

We recommend validating the EDM detector in the Playground after you add it to an Engine Profile. This helps confirm that the detector matches the expected values before you apply the Engine Profile to runtime policies. For more information, see [Testing AI Security Engine Profiles in the Playground](/docs/ADD-LINK).

After you validate the detector, assign the Engine Profile to runtime policy rules for the relevant users, apps, or agents. For more information, see [Assigning AI Security Engine Profiles to Runtime Policy Rules](/docs/ADD-LINK).

## Update an EDM Detector Dataset with the API

You can use the API to keep an EDM detector dataset up to date without manually uploading a new file in the CMA. After you create the EDM detector in the CMA, you can use the API to generate a pre-signed URL and upload the updated dataset to Cato-managed storage. This lets each customer maintain updated datasets for their EDM detectors while preserving the detector configuration.

### Before You Begin

Create an API role with permissions to edit AI Security Engine Profiles. For more information about creating custom admin roles, see [Managing Admin Roles Using RBAC](https://knowledge.catonetworks.com/v1/docs/managing-admin-roles-using-rbac).

Create the API admin as a Service Principal and assign it the API role. Service Principals are intended for API-based workflows and automation processes, and Service API Keys inherit the permissions of the associated Service Principal.

Generate a Service API Key for the Service Principal. For more information, see [Generating API Keys for the Cato API](https://knowledge.catonetworks.com/docs/generating-api-keys-for-the-cato-api).

The API upload supports the following behavior:

- The EDM detector must first be created in the CMA
- The uploaded file must use the same **Key** from the initial EDM detector configuration
- The uploaded file must use the same schema and column mapping as the initial dataset
- The file must be one `gzipped` file per EDM detector
- Don't bundle multiple files in a single ZIP file
- Maximum file size is 5 GB
- The pre-signed URL is valid for 12 hours

### Updating an EDM Detector Dataset with the API

1. Send the following API mutation to generate a pre-signed URL:

```
mutation getPutUrl {
  aiSecurity(accountId: "Account Number") {
    engineProfile {
      generateEdmUploadUrl(
        input: { edm: { by: NAME, input: "EDM detector name" } }
      ) {
        uploadUrl
      }
    }
  }
}
```

1. Include the API key in the request header:

```
{
  "x-api-key": "CATO SECRET"
}
```

The response returns a pre-signed URL that is valid for 12 hours. We recommend copying the URL in quotation marks to avoid automatic escaping.

1. Upload the `gzipped` dataset file to the pre-signed URL:

```
curl --upload-file "SRC (gzip file location)" "DST (pre-signed URL)"
```

After the upload is complete, the EDM detector status is updated with the API source, the corresponding processing status, and the time of the last update.
