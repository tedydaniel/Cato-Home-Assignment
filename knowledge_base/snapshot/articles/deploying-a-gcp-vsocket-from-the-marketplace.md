---
title: "Deploying a GCP vSocket from the Marketplace"
slug: "deploying-a-gcp-vsocket-from-the-marketplace"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/deploying-a-gcp-vsocket-from-the-marketplace"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying a GCP vSocket from the Marketplace

This article explains how to use the Google Cloud Marketplace to automatically deploy a virtual Cato Socket (vSocket) for a site hosted in GCP.

For deploying a GCP vSocket using Terraform, see [Configuring a Cato vSocket in GCP Using Terraform](/v1/docs/configuring-a-cato-vsocket-in-gcp-using-terraform).

## Overview

For sites that are hosted in GCP, you can deploy a vSocket on a GCP virtual machine (VM) directly from the Google Cloud Marketplace and extend the advantages of Cato’s secure and optimized network into your GCP environment. This lets you connect to the Cato Cloud while benefiting from GCP’s global infrastructure and high-performance connectivity. This article explains how to use the Google Cloud Marketplace to deploy a GCP vSocket on an n2-standard-4 instance.

When you deploy a GCP vSocket, each interface (MGMT, WAN, LAN) is assigned to a separate Virtual Private Cloud (VPC). The following diagram shows an example topology for deploying a GCP vSocket.

![GCP_vSocket_diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34144279529117(1).png)

### Prerequisites

- Permissions to deploy solutions from the Google Cloud Marketplace
- A GCP project with billing enabled
- A service account with the following roles:
  - `roles/config.agent`
  - `roles/compute.networkAdmin`
  - `roles/compute.admin`
  - `roles/iam.serviceAccountUser`
  - `roles/config.admin`
- The vSocket deployment creates three separate VPC networks. Make sure your organization policies allow creating VPC networks and subnets.

### Supported Instance Type

- n2-standard-4, including up to 2Gbps throughput

## High-Level Workflow

To deploy a GCP vSocket:

1. Create a new GCP vSocket site in the Cato Management Application (CMA).
2. Copy the vSocket serial number (S/N). You need to enter this number when deploying the vSocket from the Marketplace.
3. Deploy the vSocket from the Google Cloud Marketplace.
4. Verify that the vSocket connects to the Cato Cloud.

## Creating the GCP vSocket Site in the CMA

Create the site in the CMA before deploying the vSocket in GCP. The serial number generated for the site is required during the Marketplace deployment. The Local IP for the vSocket must match the LAN Network IP defined during deployment in GCP.

**To create the site for the GCP vSocket:**

1. In the Cato Management Application, from the navigation menu select **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![GCP_Add_Site.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34144305903133(1).png)
3. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Under **Conncetion Type** select **vSocket GCP**.
  4. Configure the **Country**, **State**, **City**, and **Time Zone** to set the time frame for the Maintenance Window.
4. Configure the **WAN Interface Settings**, including the **Downstream** and **Upstream** bandwidth according to your ISP bandwidth.
5. Configure the **LAN Interface Settings**, including the **Native Range** for the GCP site.
  - The Native Range must match the LAN Subnet CIDR that you define in GCP.
  - The Local IP must match the LAN Network IP configured in GCP.
6. Click **Apply**. The site is added to the **Sites** list.

## Copying the vSocket Serial Number

The CMA automatically generates a unique serial number for the new vSocket. You need to enter this serial number when deploying the vSocket from the Marketplace.

**To copy the serial number:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Copy the **S/N** for the vSocket.

## Deploying the GCP vSocket from the Marketplace

Use the Google Cloud Marketplace solution to automatically create the required Compute Engine instance, VPC networks, subnets, and optional public IP addresses for the vSocket deployment.

**To deploy the GCP vSocket from the Marketplace:**

1. In Google Cloud Console, go to Marketplace.
2. Search for **Cato Networks Virtual Socket** and select the product.
3. Click **Launch**.
4. Configure the deployment settings:

![GCP_Market_Settings_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34144305935389(1).png)
  - **Deployment name**
  - **Deployment Service Account** - Select an existing service account with the required roles or create a new one. For more about the required roles, see above [Prerequisites](/v1/docs/deploying-a-gcp-vsocket-from-the-marketplace#prerequisites).
  - **Deployment Type**2025
  - **Region** and **Zone**.
  - **Network Tier** - Select the network tier for external traffic associated with the vSocket’s public IP addresses.
5. Configure the VPC and subnet settings. Each interface (MGMT, WAN, LAN) is deployed in a separate VPC network.
  - **Management VPC Name**
  - **WAN VPC Name**
  - **LAN VPC Name**
  - **Management Subnet Name**
  - **WAN Subnet Name**
  - **LAN Subnet Name**
  - **Management Subnet CIDR**
  - **WAN Subnet CIDR**
  - **LAN Subnet CIDR** - This subnet must match the Native Range you configured in CMA.
6. Configure IP and VM settings:
  - **Management Public IP Name**
  - **WAN Public IP Name**
  - **VM Instance Name**
  - **Management Network IP**
  - **WAN Network IP**
  - **LAN Network IP** - This IP must match the Local IP configured for the site in the CMA.
7. Under **Primary Socket Serial ID** enter the serial number you copied in the CMA. For more information, see above [Copying the vSocket Serial Number](/v1/docs/deploying-a-gcp-vsocket-from-the-marketplace#copying-the-vsocket-serial-number).
8. (Optional) Configure settings for public IP options and LAN default route:

![GCP_Market_Settings_optional.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34144328310173(1).png)
  - **Assign Public IP to Management Interface**
  - **Assign Public IP to WAN Interface**
  - Select **Create LAN Default Route** to automatically create a default route in the LAN VPC.
9. Click **Deploy**.

The deployment process creates:

The deployment can take several minutes to complete.
  - Three VPC networks
  - Three subnets
  - A Compute Engine VM for the vSocket
  - Optional public IP addresses

## Verifying the vSocket Connection

After the deployment completes, the vSocket automatically connects to the Cato Cloud. Check the connection status in CMA.

**Note:** It may take several minutes for the connection process to complete.

**To verify the vSocket Connection**

1. In the Cato Management Application, from the navigation menu select **Network > Sites**.
2. Select the GCP vSocket site.
3. Verify that the Socket status shows as **Connected**.
