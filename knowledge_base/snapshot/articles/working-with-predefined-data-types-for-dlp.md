---
title: "Working with Predefined Data Types for DLP"
slug: "working-with-predefined-data-types-for-dlp"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/working-with-predefined-data-types-for-dlp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Predefined Data Types for DLP

This article explains how to use predefined data types to identify sensitive data to prevent data exfiltration.

## Overview

Cato’s DLP service uses predefined Data Types to identify sensitive data within a traffic flow. You can add the Data Types to an existing [DLP content profile](/v1/docs/creating-dlp-content-profiles) or create a new one.

The predefined Data Types are:

- **The Data Catalog**: This contains hundreds of different static data points tailored to specific countries
- **Machine Learning (ML) Classifiers**: These adapt to changing data patterns and accurately identify a wide range of sensitive data or images without requiring ongoing manual updates.

In addition to predefined Data Types, you can also create custom Data Types. For more information, see [Working with Custom Data Types for DLP](/v1/docs/working-with-custom-data-types-for-dlp).

## Understanding the Data Catalog

The Data Catalog contains country-specific data types that are categorized into the following data categories:

- Document classification
- Financial data
- HIPAA - only relevant to the USA
- Health care
- Item identifiers - such as postal codes and license keys -
- Payment Card Industry Data Security Standard (PCI DSS) - credit card data
- Personally Identifiable Information - PII
- UK National Health Service

## Understanding Machine Learning Classifiers

ML Classifiers are trained to identify sensitive documents or images. Using an advanced data science similarity model, the **ML Classifiers** offer better adaptability and accuracy in detecting sensitive data, as they can dynamically learn and evolve with changing data patterns. For example, instead of needing to update a custom data type whenever a medical form is updated, you can use the **Records** ML Classifier to detect all medical records. The **ML Classifiers** provide comprehensive detection for categories such as medical records, tax forms, patent documents, resumes, immigration forms, and more.

There are two ML Classifiers:

- **Predefined ML Classifiers**: Identifies sensitive data, for example, a resume, in over a hundred languages
- **Image ML Classifiers**: Identifies sensitive images, for example, engineering diagrams or screenshots

### Known Limitations

- OCR image scanning is not supported for ML Classifier data types

## Validating Data Types

To ensure data within your environment matches a predefined data type, you can validate your data and ensure it is correctly identified by exporting the extracted text.

**To validate data types:**

1. From the navigation menu, select **Security > Data Types & Profiles,**, and click the **Data Types** tab.
2. Click on the three dots at the end of the row of the data type you wish to validate, and click **Validate**.
3. Upload the test file or image.

## Viewing the Data Types

The **Data Types** page shows all the Data Types that you can add to a profile. This lets you research and understand more about specific Data Types that you are using in your organization. The catalog also shows the **Threshold** for each data type, indicating the minimum number of occurrences to activate the data type. For more about data type thresholds, see [Working with Custom Data Types for DLP](/v1/docs/working-with-custom-data-types-for-dlp).

![Image_class.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32901522791837.png)

**To show the Data Types:**

- From the navigation menu, select **Security > Data Types & Profiles,**, and click the **Data Types** tab.
