---
title: "Creating App Connectors in AWS"
slug: "creating-app-connectors-in-aws"
updated: 2026-08-23T13:48:53Z
published: 2026-08-23T13:48:53Z
canonical: "knowledge.catonetworks.com/creating-app-connectors-in-aws"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating App Connectors in AWS

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

You can deploy an app connector in Amazon Web Services (AWS) to provide secure access to private applications in your cloud environment. The app connector establishes a connection between your cloud environment and Cato, and once connected, you assign it in the CMA and associate it with the relevant app connector group.

## Understanding the App Connector in AWS Workflow

The following is a high-level workflow for deploying an app connector in AWS:

- You create the App Connector object in the CMA
- Deploy the Cato App Connector from AWS Marketplace
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

## Deploy the App Connector in Amazon Web Services

Use the automated Cato wizard in the Amazon Marketplace to create the virtual resources for the app connector and deploy it to AWS. The app connector image is publicly available in the Marketplace.

**To deploy an app connector in AWS**

1. From the AWS Marketplace, search for Cato Networks App Connector, and click **Launch**.
2. Under **Network Configuration**, determine if you want to deploy the App Connector in a new or existing VPC.
  1. If you select an existing account, in the **Existing VPC** dropdown, click on the relevant virtual network.
3. Select the subnets for the following interfaces (minimum subnet address space of /28):
  - MGMT subnet – Management communication between the app connector and the AWS API
  - WAN subnet - External WAN traffic for the app connector (Internet and Cato Cloud)
  - LAN subnet - Internal AWS resources and traffic that are connected to the app connector
4. Under **Security Configuration**:
  1. In the **Existing External Security Group** field, define the security group that controls inbound traffic over ports 443 and 22. To maintain good security posture, this should be limited to the smallest possible group of IP addresses
  2. In the **Existing Internal Security Group** field, define the security group that controls traffic from your internal network
5. Under **Instance Configuration**:
  1. Select the Instance Type on which the app connector should run
  2. In the **MyKeyPair** field, select the key pair that you created to encrypt this connection
  3. In the **Serial Number** field, paste the value that you copied earlier from the CMA.
6. Click **Submit**.

You can see your app connectors in the Access > App Connectors page.

## Assign Apps to the Connector

You assign apps to your connectors either from the Private Apps page or from App Connectors page, using the **Assign App** link.
