---
title: "What is the Cato DLP Service?"
slug: "what-is-the-cato-dlp-service"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/what-is-the-cato-dlp-service"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Cato DLP Service?

This article provides an overview and background information about Cato's Data Loss Prevention (DLP) service to provide content inspection and protect sensitive data. Cato's DLP solution extends the abilities of [Cloud Access Security Broker (CASB)](/v1/docs/application-control-casb) that manage how cloud-based apps are used, and adds the capabilities for data and content inspection.

The Application Control policy is included in the CASB license. Enabling Data Control rules in the Application Control policy also requires the DLP license.

## Overview of Cato DLP

With the proliferation of SaaS and web-based apps, it is increasingly difficult for admins to easily monitor and control how sensitive information is accessed, used, and shared. Cato's DLP service provides a data-aware solution to enhance the CASB Application Control rules and provides:

- The ability to prevent or detect data exfiltration, and minimize risks for data breaches or accidental data loss
- Granular rules let you comply with industry regulations and standards for only the relevant traffic segments
- Monitor sensitive content and file uploads and downloads across the organization

The DLP content scans are inline proxy-based using HTTP inspection. The DLP engine uses the advanced Cato Cloud architecture which implements content inspection and at the same time ensures privacy with minimal latency or impact for the end-user.

### Understanding DLP Fail Mode

The DLP fail mode determines how the DLP policy handles cases when the DLP scan for a file can't be completed, for example, if a file is [too large to scan](/v1/docs/what-is-the-cato-dlp-service#dlp-service-file-requirements) (see below) or if the scan times out. By default, the Data Control policy fails open and allows the traffic for uncompleted scans. However, you can configure a fail closed mode that blocks the traffic if Cato’s DLP can't complete the scan. This setting applies for all DLP scans for the account. For more about DLP fail mode, see [Creating the Data Control Policy](/v1/docs/creating-the-data-control-policy).

> [!NOTE]
> Note:
> 
> When fail closed is enabled, it is applied to all traffic flows, not only the traffic that matches a Data Control rule.

## Using the Cato Management Application to Create the DLP Policy

The Cato Management Application lets you add Data Control rules to the Application Control Policy (Security > Application Control) to define the content and apps that are inspected. The Data Control rules support these DLP features:

- File attribute content inspection - specify the file types and size which are monitored and controlled. These are configured as the **File Attributes** for a rule.
- Predefined Data Types - recognize a wide range of sensitive data (such as credit card numbers, and identity numbers). These are configured as the **Data Types & Profiles** for a rule.

The DLP Profiles page (Security > DLP Profiles) lets you combine related Data Types into a single Content Profile which you can add to a Data Control rule.

> [!NOTE]
> Note:
> 
> If you create a Data Control rule that uses both **File Attributes** and **Data Types & Profiles**, then there is an AND relationship between those settings. That means that the rule only matches content that meets all the file requirements and the Data Types. In general, we recommend that you configure either **File Attributes** or **Data Types & Profiles** within a single rule.

### Implementing DLP Policy in Your Account

This is a high-level overview of the steps to implement the DLP policy.

1. Create (or review) the DLP Content Profile that defines the Data Types that you are including in the DLP policy (see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles)).
2. Create the Data Control rules for the File Attributes and DLP Profiles (see [Creating the Data Control Policy](/v1/docs/creating-the-data-control-policy)).
3. Set the DLP fail mode to define whether the DLP policy enforces a default Block action when a file scan can't be completed (see [Creating the Data Control Policy](/v1/docs/creating-the-data-control-policy)

## Sample DLP Use Cases

- Challenge - Prevent users from uploading Autocad source files to an external destination
  - Cato solution - Create a Data Control rule for the **Design** file type in the upstream direction
- Challenge - Enforce Personally Identifiable Information (PII) for a specific country
  - Cato solution - Create a DLP Content Profile that contains all the relevant PII Data Types

## DLP Service File Requirements

For more information on the DLP file requirements, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).
