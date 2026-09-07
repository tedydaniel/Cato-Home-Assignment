---
title: "Configuring a Cato vSocket in GCP Using Terraform"
slug: "configuring-a-cato-vsocket-in-gcp-using-terraform"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/configuring-a-cato-vsocket-in-gcp-using-terraform"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a Cato vSocket in GCP Using Terraform

This article explains how to use Terraform to deploy a Cato virtual Socket (vSocket) for a site hosted in Google Cloud Platform (GCP).

## Overview

For sites that are hosted in GCP, you can deploy a vSocket on a GCP virtual machine (VM) and extend the advantages of Cato's secure and optimized network into your GCP environment. This lets you connect to the Cato Cloud while benefiting from GCP’s high-performance global network infrastructure, fast data transfer, and low-latency connections. This article explains how to use Terraform to deploy a GCP vSocket on an n2-standard-4 instance.

> [!NOTE]
> BGP is supported for GCP vSockets.

When you deploy a GCP vSocket, each vSocket interface (MGMT, WAN, LAN) must be assigned a separate Virtual Private Cloud (VPC). The following diagram shows an example topology for deploying a GCP vSocket.

![GCP_vSocket_diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25226767995933.png)

### Prerequisites

- A GCP account with these IAM roles and permissions required for creating and managing GCP resources:
  - Compute Admin
  - Compute Network User
  - Compute Storage Admin
  - Logging Admin
  - Logs Viewer
  - Network Management Admin
  - Service Account User
  - Service Usage Admin
  - Storage Admin
- Make sure the environment meets the requirements listed in [Cato Socket Connection Prerequisites](/v1/docs/cato-socket-connection-prerequisites-and-known-limitations)
- 3 VPCs configured in your GCP environment to be assigned to the vSocket interfaces
- Terraform installed and configured on your system
  - For your convenience, we created a GCP vSocket Terraform module to help configure the vSocket. Download the module from the [Cato Terraform Registry](https://registry.terraform.io/modules/catonetworks/vsocket-gcp/cato/latest)

### Supported Instance Type

- n2-standard-4, including up to 2Gbps throughput

### Known Limitations

- Only a single GCP vSocket is supported per site

### Deploying a GCP vSocket with Terraform

Define the required parameters in the Terraform folder and run Terraform commands to create the site and deploy the vSocket in GCP.

> [!NOTE]
> Each vSocket interface (MGMT, WAN, LAN) must be assigned a separate Virtual Private Cloud (VPC).

**To deploy a GCP vSocket:**

1. In the Terraform folder, define the configuration using the module and the following parameters:
  - **token:** Cato API key, which you can obtain in the Cato Mananagement Application. For more information, see [Generating API Keys for the Cato API](/v1/docs/generating-api-keys-for-the-cato-api). As a best practice, we recommend configuring this as an environment variable.
  - **account_id:** Your Cato account number. For more information, see [Viewing the Account Info](/v1/docs/viewing-the-account-info).
  - **project:** The GCP project ID where the vSocket will be deployed
  - **region:** The GCP region where the vSocket will be deployed (e.g. us-central1)
  - **zone:** The GCP zone within the region for redundancy (e.g. us-central1-a)
  - **mgmt_compute_network_id:** The ID of the VPC for the management interface
  - **wan_compute_network_id:** The ID of the VPC for the WAN interface
  - **lan_compute_network_id:** The ID of the VPC for the LAN interface
  - **mgmt_static_ip_address:** The name of the public IP address for the management interface (optional)
  - **wan_static_ip_address:** The name of the public IP address for the WAN interface (optional)
  - **vm_name:** The name of the virtual machine instance for the vSocket
  - **mgmt_network_ip:** The local IP address for the management interface
  - **wan_network_ip:** The local IP address for the WAN interface
  - **lan_network_ip:** The local IP address for the LAN interface
  - **public_ip_mgmt:** Set to false to not assign a public IP address to the management interface (optional).
  - **create_firewall_rule:** Set to false to skip firewall rule creation
  - **firewall_rule_name:** The name of the firewall rule (only used if create_firewall_rule is set to true)
  - **allowed_ports:** A comma-separated list of ports allowed to access the vSocket in the firewall rule (only used if create_firewall_rule is set to true)
  - **management_source_ranges:** The IP source ranges allowed to access the vSocket in the firewall rule (only used if create_firewall_rule is set to true)
  - **native_network_range:** The IP range configured for the LAN interface (Native Range) as defined in the CMA
  - **lan_subnet_id:** The ID of the subnet where the LAN interface of the socket is located
  - **mgmt_subnet_id:** The ID of the subnet where the MGMT interface of the socket is located
  - **wan_subnet_id:** The ID of the subnet where the WAN interface of the socket located
  - **site_name:** Name of the site shown in the CMA
  - **site_description:** Description of the site in the CMA
  - **site_location:** (city, country_code, state_code, timezone) location of the site shown in the CMA. This field is important for steering
  - **tags:** Tags to add to the vSocket instance in GCP
  - **labels:** Labels to add to the vSocket instance in GCP
2. In Terraform, run the following commands:
  1. Run **terraform init** to initialize the Terraform configuration.
  2. Run **terraform plan** to generate an execution plan to review the resources to be created.
  3. Run **terraform apply** to apply the configuration and deploy the vSocket.

The site is created and the vSocket is deployed. You can view the site and Socket details in the CMA.

![GCP_vSocket_CMA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25226735232925.png)
3. Verify that the vSocket is connected to your account. It may take a few minutes for the connection process to complete.
