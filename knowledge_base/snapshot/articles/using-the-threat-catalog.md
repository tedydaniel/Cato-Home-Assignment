---
title: "Using the Threat Catalog"
slug: "using-the-threat-catalog"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/using-the-threat-catalog"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Threat Catalog

This article discusses how to use the Threat Catalog to get more information about threats and vulnerabilities covered by Cato security services.

## Overview of the Threat Catalog

The Threat Catalog contains security data and general information for the thousands of cyber threats in the Cato security database. You can easily search and filter the catalog to see details of threats detected by Cato's security services, or show the newest threats. You can also drill-down to detailed information about the threats and view relevant event logs.

The Threat Catalog includes information for threats detected by the following security services:

- IPS
- Anti-Malware
- Suspicious Activity Monitoring
- DNS Protection

### Understanding Threat Updates in the Cato Cloud and Threat Catalog

Cato deploys weekly threat updates for its security services, and the new threats also appear in the Threat Catalog. Cato uses a gradual roll-out process for these updates, in line with industry best practices for Cloud services. Due to this graduality, a new threat that appears in the catalog might take up to a week to be deployed for the security services in your account. However, for urgent new threats deployment times are shortened to up to one day.

The Anti-Malware service receives updates approximately every 20 minutes, while the catalog updates Anti-Malware signatures on a daily basis. Therefore it may take up to a day until you can see new Anti-Malware protections in the catalog.

### Known Limitations

- For Anti-Malware, the catalog only includes threats detected by the Anti-Malware service, not the NG Anti-Malware service. Since NG Anti-Malware is designed to detect unknown threats, these protections can't be listed in the catalog
- Information for Anti-Malware threats is available only for the **Name** and **Engine** columns of the catalog, and no drill-down links are available for these threats

## Getting Started with the Threat Catalog

![Threat_Catalog.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24198369452701.png)

**To show the Threat Catalog:**

- From the navigation menu, click **Resources > Threat Catalog**.

The Threat Catalog has these columns:

- **Name** of the threat.
  - Click the name to read more about the threat in third-party resources
- A **Description** of the threat.

Note: The information in the **Description** column is AI-generated and might contain inaccuracies. Cato does not assume responsibility for this information.
- Cato **Threat Name** or **Signature ID** as it appears in event logs shown in the Events screen.
  - Click the **Threat Name** or **Signature ID** to open the Events screen pre-filtered for that threat
- **MITRE Reference** - Shows the threat technique used by the threat according to the MITRE ATT&CK® framework. For more about the MITRE ATT&CK® framework, see [Working with the MITRE ATT&CK® Dashboard](/v1/docs/using-the-mitre-att-ck-dashboard) .
  - Click the reference to open the Events screen pre-filtered for the MITRE ATT&CK® technique
- **Engine** - Shows the Cato security service that detects the threat

## Configuring Filters to Find Relevant Threats

You can search the **Name** or **Threat Name/Signature ID** columns for specific threats, and set the following filters to easily find relevant threats:

- **Engine** - Select a Cato security service to filter the catalog to show the threats that the service detects.
- **MITRE Technique** - Select an attack technique as defined in the MITRE ATT&CK® framework to show threats that use the technique.
- You can use the **Status** drop-down menu to filter the catalog to show only new threats.

Threats are considered new if they were added to the catalog within the last two weeks, and appear with the label **New**,
