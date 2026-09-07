---
title: "Understanding the Sandbox Analysis Report"
slug: "understanding-the-sandbox-analysis-report"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/understanding-the-sandbox-analysis-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the Sandbox Analysis Report

The Sandbox Analysis Report is automatically generated after a file is scanned in the Sandbox. This article explains how to access and understand the analysis in the Report.

## Overview

The Sandbox is an isolated, secure, and virtual, environment where potentially malicious files are executed and analyzed without risk to your network. This provides in-depth forensic analysis for comprehensive malware investigation. Files are scanned in the Sandbox because they have been either identified as Suspicious or Malicious by the Anti-Malware scan or manually uploaded to the Sandbox.

For more information about the Sandbox see [What is the Sandbox?](/v1/docs/scanning-files-in-the-sandbox)

Once a file is executed and analyzed in the Sandbox, a comprehensive report is generated within 10 minutes and made available for download in the CMA for one month. The report summarizes the results of the static and dynamic analysis scans, enabling you to confidently assess the file’s potential risk.

## Access the Sandbox Analysis Report

After a file scan, the results are available for download as a PDF within a few minutes in the Sandbox Analysis Report.

![sandbox_report.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24708659515933.png)

You can access the Sandbox Analysis Report from the **Security > Sandbox Reports** page.

The Sandbox Reports table can be filtered and sorted and contains these columns:

| Column | Description |
| --- | --- |
| File Name | The name of the file that was scanned in the Sandbox. |
| Sandbox Verdict | The overall verdict based on all of the file scans. Options are: - Benign - Suspicious - Malicious |
| File Hash | The SHA-256 file hash of the file that was scanned in the Sandbox. |
| Report | A link to download the Sandbox Analysis Report. |
| Status | The stats of the report. Options are: - **In Progress**: The report is being generated - **Ready**: The report can be downloaded |
| Generated On | The date the report was created. |
| Expires on | The last date the report is available for download. |

## Understanding the Sandbox Analysis Report

The Sandbox Analysis Report has four key sections to provide you with a comprehensive overview of the file's risk.

### Report Summary

This section has three subsections:

- **File Metadata**: The metadata of the file, for example the file name and type
- **Summary**: The high level summary of the report including the:
  - Overall verdict based on all the scans run in the Sandbox
  - Verdict of the static and dynamic analysis independently
  - Number of VirusTotal detections identified in the file
- **MITRE ATT&CK**: MITRE ATT&CK tactics associated with the file's malicious activity

### Static Analysis

This section provides an overall verdict of the static analysis scans and the verdict of each of static analysis scan independently. The static analysis scans are:

- **Machine Learning - Overall**: Based on multiple deep learning models, analyzing file attributes against millions of benign and known malware samples to provide an overall verdict of the file.
- **Machine Learning - Feature Analysis**: Analyzes each file feature individually, comparing them to millions of benign and known malware samples.
- **Machine Learning - Similar Files**: Analyzes a few file features and compares them to benign and known malware samples. It then gradually adds more features to calculate the probability of the file being malicious based on their combination.
- **Machine Learning - Structure Similarity**: Identifies 32 key structural genes in the file, then scans the database to find the closest matching files. It analyzes the correlation between the genes and the file's maliciousness.
- **Reputation**: Engine that analyzes the file's prevalence across the network, enabling rapid blocking of emerging threats while reducing false positives.

### Dynamic Analysis

This section provides the overall verdict of the dynamic analysis scans and a summary of:

- Detailed analysis of all malicious activities, including MITRE ATT&CK tactics, detected during file execution
- Identified processes
- File system activities
- Network activity and interactions
- Screenshots of the file execution
