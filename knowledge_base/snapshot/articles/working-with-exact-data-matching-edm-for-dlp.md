---
title: "Working with Exact Data Matching (EDM) for DLP"
slug: "working-with-exact-data-matching-edm-for-dlp"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/working-with-exact-data-matching-edm-for-dlp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Exact Data Matching (EDM) for DLP

This article explains how to create Exact Data Matching (EDM) custom data types to identify specific sensitive data for the DLP policy.

For more about custom data types for DLP, see [Working with Custom Data Types for DLP](/v1/docs/working-with-custom-data-types-for-dlp).

## Overview

Exact Data Matching (EDM) for DLP finds specific sensitive data values that are important to the organization, rather than matching general data patterns. For example, instead of blocking the transfer of all credit card data, you can block a specific set of data containing your customers' credit card information. By using EDM to tailor your DLP policies, you can significantly reduce false positives and increase admin productivity.

To implement Exact Data Matching in your DLP policy, import a structured data set of the specific sensitive data, and use it to create an EDM profile. Then you can configure a DLP rule for the profile and block only that specific data. This is an example workflow for blocking a specific set of data using an EDM profile:

1. Create a CSV or similar file type (such as TSV or PSV) containing the required data set.
2. In the Cato Management Application, import the CSV file and create an EDM profile based on the data in the file.
3. Configure a [Data Control](/v1/docs/creating-the-data-control-policy) rule for the EDM profile.

### Defining the Data for Matching

When you create an EDM profile, you can select up to two columns of the imported data file to include in the profile. When you select two columns, there is an AND relationship between them, and the DLP engine returns a match only when both data values are detected. For example, if you select the Employee Name column and the Salary column in a data set, the DLP engine will only return a match for content containing both a matching name value and its relevant salary value.

#### Understanding Primary and Secondary Data

For EDM profiles that include two data columns, you configure one column as **Primary** and the other as **Secondary**. This defines the order in which the DLP engine searches for the data. Only if the **Primary** data is matched, the DLP engine continues and looks for the **Secondary** data.

Since EDM is designed for identifying specific data, **Primary** data can't contain many occurrences of the same value. A data column that contains a value that occurs more than 3 times can't be defined as **Primary**.

#### Understanding Data Types for EDM Profiles

For each data column you include in the EDM profile, you define an existing general DLP data type that matches the data in the column. When the DLP engine scans content to match the EDM profile data, it first tries to match the content with the existing data type, and only if there's a match it continues to check for the specific data in the profile. For example, the engine first matches for a general credit card data pattern, and then looks for specific credit card numbers. This ensures greater efficiency for EDM data scans.

### Understanding Data Security for EDM Profiles

When you import data sets for EDM profiles, all data is hashed by the user's browser before it is uploaded to the Cato Cloud. When the DLP engine compares the hashed data with content and looks for a match, it first hashes the content using the same algorithm. This method lets the DLP engine identify matches with EDM profiles without uploading or storing any clear-text data.

### Requirements for Imported Data Set Files

EDM for DLP supports imported data set files that meet the following requirements:

- Files must be one of the following formats: CSV, TSV, PSV, SSV, HSV, TXT
- Supported delimiters include the following characters:
  - Comma (,)
  - Pipe (|)
  - Tab
  - Semicolon (;)
  - Colon (:)
  - Hyphen (-)
  - Number sign (#)
  - Caret (^)
  - Exclamation point (!)
  - At sign (@)
  - Dollar sign ($)
  - Percent sign (%)
  - Ampersand (&)
  - Forward slash (/)
- Supported file size is up to 8 MB

This is an example of a data set CSV file that can be used for an EDM profile:

![DLP_-_EDM_Sample_CSV.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33998047016221.png)

## Creating an EDM Profile

Create a new EDM profile and upload a data set file containing the specific data for content matching. Select up to two columns of data and define the **Primary** column. For each selected column, define an existing data type that matches the data in the column. This can be a predefined or user-defined data type.

![DLP_-_EDM_Page.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33998063124125.png)

**To create an EDM profile:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and in the **DLP Profiles** tab select **EDM Profile**.
2. Click **New**. The **Add Exact Data Match Profile** panel opens.

![DLP_-_EDM_New_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33998047150493.png)
3. Enter the **Profile Name** and **Description**.

The **Profile Name** must be a unique name not used for other EDM profiles or any other custom data types.
4. Drag and drop or browse to upload a file containing a schema and exact data for the profile. A **File Loaded** message appears when the upload is complete, containing the following information:
  - Number of data rows detected in the file
  - The detected delimiter
5. Select the file columns to include in the profile, you can select up to two columns.
6. For each selected column, configure the following:
  1. Data **Type** of the data in the column. You can select one predefined or user-defined data type for each column.
  2. Whether the column is **Primary**. You can define only one column as **Primary**, the other column is automatically configured as **Secondary**.
7. Click **Save**.

## Best Practices for User-Defined Data Types

- When you implement the policy, or add a new application with the Block action:
  - Use the Monitor action for the rule.
  - Review the events that the rule generates and make sure that there are no events for traffic that you want to allow (false positive traffic).
  - If there is false positive traffic, you can make these changes:
    - Refine the scope of the rule to exclude the false positive traffic
    - Create a new allow rule before the block rule, and the scope of the new rule is only for the false positive traffic
- Remember that the Application Control policy is an ordered policy, and the final implicit rule is ANY ANY Accept. Add rules to the policy to block the relevant application traffic, activities and criteria.

### Known Limitations

- You can create up to 15 EDM profiles for your account
- OCR scanning is not supported for DLP content matching for EDM profiles
- For information on the file requirements, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service)
- Base64 encoded files are not supported, and the DLP engine can't inspect the content in these files.
