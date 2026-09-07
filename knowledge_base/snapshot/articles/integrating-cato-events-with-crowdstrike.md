---
title: "Integrating Cato Events with CrowdStrike"
slug: "integrating-cato-events-with-crowdstrike"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/integrating-cato-events-with-crowdstrike"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato Events with CrowdStrike

This article explains how to configure the CrowdStrike integration to forward Cato events.

> [!NOTE]
> Note:
> 
> Enabling the connector in the Cato Management Application lets you use the HEC/HTTP generic connector with CrowdStrike, but vendor-specific fields (Vendor, Vendor Product) and CrowdStrike schema parsing are not supported. The vendor-specific fields and the optional CrowdStrike parser are currently in Beta. For more information and to enable these features, contact your CrowdStrike representative.

## Overview

The CrowdStrike Next-Gen SIEM integration enables Cato to forward events directly to CrowdStrike using a native connector. You can stream normalised Cato events, complete with rich context on network activity, threats, users, devices and all other aspects of traffic traversing the Cato platform directly into Falcon Next Gen. This allows analysts to investigate and hunt with full network context without leaving Falcon.

To configure the CrowdStrike integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the Cato Management Application (CMA)

### Use Case

A company is using CrowdStrike for centralized security monitoring and response. As Cato customers, they have useful data from key features such as network activity, threats, user data, devices, and all other aspects of traffic traversing the Cato platform. They can use this integration to send this data directly to CrowdStrike, where they can easily integrate it into existing workflows for the SOC and NOC teams.

### Prerequisites

- Falcon Next-Gen SIEM or Falcon Next-Gen SIEM 10GB subscription.
- For vendor-specific fields and the optional CrowdStrike parser, the Beta feature needs to be enabled in CrowdStrike. For more information and to enable these features, contact your CrowdStrike representative.
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).
- Please review the prerequisites for all Cato event integrations in [Getting Started with Event Integrations](/v1/docs/getting-started-with-event-integrations)

## Configuring the CrowdStrike Integration

To configure the CrowdStrike integration, create a Data connection.

### Step 1: Configure the Integration in the Falcon console

In the Falcon console, create a data connection.

**To configure the CrowdStrike integration:**

1. In your Falcon CrowdStrike console, navigate to **Data connectors > Data connections**.
2. Click **Add connection**.
3. In the **Product** filter, apply a filter for HEC and in the **Connector type** filter, apply a filter for Push.
4. Click on the **HEC/HTTP Event Connector** and click **Configure**.
5. Add a name for the connection and add the following details (only supported if enabled in CrowdStrike, for more information see the [Prerequisites](/v1/docs/integrating-cato-events-with-crowdstrike#prerequisites)):
  - Vendor: CatoNetworks
  - VendorProduct: CatoNetworksSASECloud
  - (Optional) Parsers: cato-sase
6. Affirm the Terms and Conditions and click **Create connection**.
7. Once the connection is created, click on the three dots and select **Generate API key** followed by **Regenerate API key**.
8. Copy and save the **API key** and **API URL** so they can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **CrowdStrike Falcon NG-SIEM**.
5. Add the details created during step one.
6. Click **Save**.
7. The app is visible on the **Configured Integrations** table with a **Connected** status.
