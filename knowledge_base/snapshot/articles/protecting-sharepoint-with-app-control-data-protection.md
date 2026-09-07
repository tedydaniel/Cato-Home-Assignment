---
title: "Protecting SharePoint with App Control & Data Protection"
slug: "protecting-sharepoint-with-app-control-data-protection"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/protecting-sharepoint-with-app-control-data-protection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Protecting SharePoint with App Control & Data Protection

This article explains how you can use App Control and Data Protection features to secure your Microsoft SharePoint tenant.

## Overview

As organizations increasingly rely on SharePoint for collaboration and document management, securing sensitive data and ensuring compliance becomes a critical challenge. App Control and Data Protection features strengthen SharePoint security by providing visibility, threat protection, data loss prevention (DLP), and compliance enforcement. Ensure your data and intellectual property are always secure by leveraging both inline and out-of-band App Control and Data Protection features. This proactive approach enforces rules irrespective of how users are connected and provides you with visibility of unmanaged and managed users.

This article provides example use cases for how to use these features to protect your SharePoint tenant. These examples are not exhaustive, there are likely to be other use cases that are specific to your environment.

## Restrict Access with Application Control with Inline Inspection

![AC_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25713759256989.png)

App control lets you define activities and required criteria to manage access to applications or specific app tenants. For SharePoint, this includes blocking access to unauthorized tenants and restricting access to sensitive data to authorized users. For more information about adding rules to your Application Control Policy, see [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy).

### Block Access to Unauthorized Tenants

The application control policy contains a [predefined rule](/v1/docs/using-the-default-recommended-casb-dlp-policy) allowing access to your corporate SharePoint tenant only. Access to other SharePoint tenants is blocked. This prevents data exposure or compliance violation if users inadvertently or intentionally upload sensitive company data to an external or unauthorized tenant. This App Control rule also lets you enforce data policies like retention, encryption, or access controls.

### Reduce Access to Sensitive Data

App control can Allow or Block access for specific users or groups to folder paths or files. For example, if a file containing employee salaries is saved on SharePoint, you can restrict access to this file to the finance team only. This ensures you are compliant with data protection laws and can mitigate insider threats.

## Monitor Actions with App Activities

![Sign_in_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25713784623005.png)

App Activities provides out-of-band visibility of all user activities including unmanaged users (contractors) that access corporate SaaS applications. Events generated from App Activities are visible from the [**Cloud Activity Dashboard**](/v1/docs/using-the-cloud-activity-dashboard). This lets you monitor the activities of all users accessing your SharePoint tenant even if they are not connected to the Cato Cloud. This gives you granular insights into user activity and identifies unauthorized access. For more information about creating an App Activities integration, see [What is Application Control via API with App Activities?](/v1/docs/what-is-application-control-via-api-with-app-activities) .

### Analyze Sign-In Activity

The Cloud Activity Dashboard contains an **SSO Sign In** section, which lets you view details of the users accessing your SharePoint tenant. With the **Top Sign-in Anomalies** widget, you can monitor sign in activity that may indicate malicious activity. For example, Anomalous token, Suspicious browser, Unfamiliar sign-in properties, or Malicious IP address. Performing this analysis from the Cloud Activity Dashbord, provides you with the ability to detect unauthorized access.

## Prevent Data Breaches or Data Loss with DLP

DLP inspects how data and content are transferred and moved within and outside of your organization. This can prevent data exfiltration and minimize breach risks. Granular rules ensure compliance with industry regulations for relevant traffic segments. It also monitors sensitive content and file transfers across the organization. By combining DLP inline and the Data Protection API, you can enforce the same rules irrespective of whether a user is connected to the Cato Cloud. For more information, see [Data Loss Prevention (DLP)](/v1/docs/data-loss-prevention-dlp).

### Quarantine Private Data

When you create a Data Protection rule, you can define different actions to monitor or remediate the policy violations when the rule is matched. SharePoint supports the quarantine action. This moves a file containing predefined data types into a quarantine folder so that it can no longer be accessed. For example, if customer credit card information was uploaded to SharePoint, you can create a DLP rule that quarantines the file and prevents any other users from accessing it.
