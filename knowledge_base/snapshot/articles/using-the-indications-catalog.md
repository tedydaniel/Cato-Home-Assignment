---
title: "Using the Indications Catalog"
slug: "using-the-indications-catalog"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/using-the-indications-catalog"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Indications Catalog

This article discusses how to use the Indications Catalog to get more information about potentially malicious activity identified by the Cato Detection & Response security layer.

For more about Detection & Response, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).

## Overview of the Indications Catalog

The Indications Catalog contains explanations and reference information for the hundreds of indications (indicators of attack) that are identified by the Detection & Response security engines. An indication is a set of actions and behaviors that can indicate intent to carry out an attack, even if no actual security breach has been identified yet. For example, a host generating traffic that exhibits C&C characteristics may indicate a malware attack. When the engines analyze traffic data and identify a match for an indication, they create a security story that is shown in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) page, including the indication for the story and other data to help investigate the threat. The Indications Catalog provides a full description for all the indications.

You can easily search and filter the catalog to find indications, and check to see which indications relate to a specific attack tactic. The catalog also lets you look up a specific indication to see if it is covered by the Detection & Response engines, show the newest indications, and view event logs relevant to an indication.

### Understanding the Indication Types

The Indications Catalog includes information for a number of **Types** of threat indications, detected by the different Detection & Response engines. These are brief descriptions of some of the different engines and the types of indications they identify, for a full list see, [Welcome to the Cato XOps Service](/v1/docs/welcome-to-the-cato-xops-service).

- **Threat Prevention** - Detects a specific set of attack behaviors in IPS events
- **Site Operations** - Identifies network issues such as degraded connectivity
- **Threat Hunting** - Identifies an expansive set of attack behaviors in events and richer traffic data
- **Usage Anomaly** - Identifies indications that relate to applications showing unusual usage. For example, an application using more upstream bandwidth than usual
- **Events Anomaly** - Detects indications that involve an entity on the network triggering an unusual number of security events
- **Experience Anomaly** - Detects significant changes to the experience of an application or network performance to an application

#### Indication Types and Licensing

Your Detection & Response license determines the indication **Types** enabled for your account. The Indications Catalog shows your current license, and whether a specific indication is available for that license. When an indication is unavailable for your license, stories based on that indication won't be created and shown in the Stories Workbench. For more information of the XOps License Tiers, see [Welcome to the Cato XOps Service](/v1/docs/welcome-to-the-cato-xops-service).

### Known Limitations

- Indications recently added to the Detection & Response engines may not immediately appear in the catalog.

## Getting Started with the Indications Catalog

![Indications_Catalog.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30223484873757.png)

**To show the Indications Catalog:**

- From the navigation menu, click **Resources > Indications Catalog**.

The Indications Catalog has these columns:

- **ID** - The identifier for the indication used by the Detection & Response engines
- **Indication** - The name of the indication category. A category can include multiple different indications with similar behaviors
- A **Description** of the indication's suspicious actions and behaviors
- **Available in Account** - Whether the indication is enabled for the account, based on the Detection & Response license level.

For more information about indication availability, see [Indication Types and Licensing](/v1/docs/using-the-indications-catalog#indication-types-and-licensing).
- **MITRE Reference** - Shows the related MITRE ATT&CK® framework threat techniques for the indication. For more about the MITRE ATT&CK® framework, see [Using the MITRE ATT&CK® Dashboard](/v1/docs/using-the-mitre-att-ck-dashboard)
  - Click the reference to open the Events page pre-filtered for the MITRE ATT&CK® technique
- **Type** - Shows the Detection & Response engine that detects the indication

## Configuring Filters to Find Relevant Indications

Set the following filters to easily find relevant indications:

- **ID** - Select an indication **ID** to show the indication
- You can use the **Status** drop-down menu to filter the catalog to show only **New** indications.

Indications are considered new if they were recently added to the catalog, and appear with the label **New**. The label doesn't indicate a specific time frame
- **Indication** - Select an indication category to filter the catalog to show the indications in that category
- Search the **Description** field for relevant indications.
- **Available in Account** - Filter the catalog to show only the indications that are **Available** or **Not Available** for the account.

For more information about indication availability, see [Indication Types and Licensing](/v1/docs/using-the-indications-catalog#indication-types-and-licensing).
- **MITRE Technique** - Select an attack technique as defined in the MITRE ATT&CK® framework to show indications related to the technique
- **Type** - Select a Detection & Response engine to filter the catalog to show the indications that the engine detects
