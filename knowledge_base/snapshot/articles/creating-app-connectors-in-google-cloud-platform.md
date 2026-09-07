---
title: "Creating App Connectors in Google Cloud Platform"
slug: "creating-app-connectors-in-google-cloud-platform"
updated: 2026-08-23T13:52:18Z
published: 2026-08-23T13:52:18Z
canonical: "knowledge.catonetworks.com/creating-app-connectors-in-google-cloud-platform"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating App Connectors in Google Cloud Platform

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

You can deploy an app connector in Google Cloud Platform (GCP) to provide secure access to private applications in your cloud environment. The app connector establishes a connection between your cloud environment and Cato, and once connected, you assign it in the CMA and associate it to the relevant app connector group.

## Understanding the App Connector in GCP Workflow

The following is a high-level workflow for deploying an app connector in GCP:

- You create the App Connector object in the CMA
- Deploy the Cato App Connector from Google Marketplace
- Assign apps to the connector

## Create an App Connector

When you create an App Connector, you can choose the behavior for connecting to a preferred PoP in the Cato Cloud:

- Disabled - the App Connector automatically connects to the best available PoP (default)
- Enabled - Select the PoPs to which the connector attempts to connect to

When Preferred PoP is enabled, you can restrict an App Connector to only connect to the Preferred PoP Locations that you configure. In this case, the connector doesn't connect to a non-preferred PoP location despite any connectivity or performance issues that it is experiencing. When you use this option, you must define a primary and secondary PoP location for the App Connector.

Once the App Connector is created in the CMA, copy the serial number, as you will need to provide it when deploying the App Connector in your cloud environment.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/new app connector.png)

**To create an App Connector in the CMA:**

1. From the navigation menu, click **Access > App Connector**, and then click **New**.
2. Enter the information in the **General** section, such as **Connector** **Name** and **Country**.
3. Under **Type**, click **Virtual**.
4. In the **Connector Group** section, select an existing App Connector group from the list or enter a name to create a new group.
5. Under **Preferred PoPs**, select the behavior
  1. **Disabled** - the App Connector tries to connect to the best available PoP
  2. **Enabled** - Select the **Primary** and **Secondary** PoP locations that the connector tries to connect to
  3. **Enabled** and **Only connect to the preferred PoPs** - Only connect to the **Primary** or **Secondary** PoP location
6. Click **Apply**.

## Deploy the App Connector in Google Cloud Platform

Use the automated Cato wizard in the Google Marketplace to create the virtual resources for the app connector and deploy it to GCP. The GCP app connector image is publicly available in the Marketplace.

**To deploy an app connector in GCP**

1. From the Google Cloud Marketplace, search for Cato Networks App Connector, and click **Launch**.
2. Under **Deployment Service Account**, determine if you want to deploy the App Connector in a new or existing account.
  1. If you select an existing account, in the **Select a Service Account** dropdown, click on the relevant account.
3. Enter the following settings for the resources and costs:
  - **Zone** - resource group that the app connector resources are associated to
  - **Region** - region for the app connector resource
  - **App Connector VM Name** - a descriptive name that will help you identify the purpose for the connector
  - **Cato Serial ID** - paste the value you copied when creating the connector in the CMA.
4. Select the subnets for the following interfaces (minimum subnet address space of /28):
  - MGMT subnet – Management communication between the app connector and the GCP API
  - WAN subnet - External WAN traffic for the app connector (Internet and Cato Cloud)
  - LAN subnet - Internal GCP resources and traffic that are connected to the app connector
5. Click **Deploy**.

After the app connector resources are deployed, it automatically connects to the Cato Cloud and checks if it's necessary to upgrade to the newest version. The Cato Management Application notification area shows messages regarding the status of connecting the app connector.

You can see your app connectors in the Access > App Connectors page.

## Assign Apps to the Connector

You assign apps to your connectors either from the Private Apps page or from App Connectors page, using the **Assign App** link.
