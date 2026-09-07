---
title: "Using Terraform with the Cato Cloud"
slug: "using-terraform-with-the-cato-cloud"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/using-terraform-with-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Terraform with the Cato Cloud

The [Cato Networks Terraform provider](https://registry.terraform.io/namespaces/catonetworks) lets you manage your account with Infrastructure as Code (IaC)-based automation. You can declaratively configure and maintain resources such as Socket sites, IPsec sites, WAN firewall rules, routing policies, and identity integrations directly in Terraform.

- Integrate Cato’s global cloud network into CI/CD pipelines
- Enforce consistent network and security policies across environments
- Streamline provisioning of secure connectivity for cloud, data center, and branch locations

The provider supports both standalone usage and integration with Cato-certified Terraform modules for cloud deployments. For more information, see [https://registry.terraform.io/providers/catonetworks/cato/latest](https://registry.terraform.io/providers/catonetworks/cato/latest)

The Cato Terraform provider uses the API, which requires an [API key](/v1/docs/generating-api-keys-for-the-cato-api).

The Terraform provider implementation, modules, and examples are available in the corresponding repositories at: [https://github.com/catonetworks](https://github.com/catonetworks).

This is a summary of the available modules:

| Feature | Description | Link |
| --- | --- | --- |
| Socket Site Module | Facilitates the creation and bulk configuration of physical Socket sites in the CMA. | [https://registry.terraform.io/modules/catonetworks/socket](https://registry.terraform.io/modules/catonetworks/socket) |
| IPsec Site Module for AWS | Creates AWS resources and sets up IPsec tunnels from AWS to Cato’s platform for secure connectivity. | [https://registry.terraform.io/modules/catonetworks/ipsec-aws](https://registry.terraform.io/modules/catonetworks/ipsec-aws) |
| IPsec Site Module for Azure | Creates Azure resources and sets up IPsec tunnels from Azure to Cato’s platform for secure connectivity. | [https://registry.terraform.io/modules/catonetworks/ipsec-azure](https://registry.terraform.io/modules/catonetworks/ipsec-azure) |
| Azure Virtual WAN IPsec Module | Provisions primary and secondary IPsec tunnels between Cato Cloud and Azure Virtual WAN for high availability. | [https://registry.terraform.io/modules/catonetworks/azure-vwan](https://registry.terraform.io/modules/catonetworks/azure-vwan) |
| Site Location Validator Module | Validates site location data from CSV files against geographical standards in the Cato system. | [https://registry.terraform.io/modules/catonetworks/sitelocation](https://registry.terraform.io/modules/catonetworks/sitelocation) |
| vSocket AWS Module | Deploys a virtual socket (3-NIC vSocket) EC2 instance in AWS and registers it as a Socket site. | [https://registry.terraform.io/modules/catonetworks/vsocket-aws](https://registry.terraform.io/modules/catonetworks/vsocket-aws) |
| vSocket AWS with VPC Module | Creates an AWS VPC and deploys a virtual Socket EC2 instance, registering it with the CMA. | [https://registry.terraform.io/modules/catonetworks/vsocket-aws-vpc](https://registry.terraform.io/modules/catonetworks/vsocket-aws-vpc) |
| vSocket AWS Transit Gateway Module | Creates an AWS VPC and deploys a virtual Socket EC2 instance, registering it with the CMA. Attaches the deployment to a transit gateway and specifies a default route to the EC2 instance. | [https://registry.terraform.io/modules/catonetworks/vsocket-aws-tgw/cato/latest](https://registry.terraform.io/modules/catonetworks/vsocket-aws-tgw/cato/latest) |
| vSocket AWS HA Module | Provisions primary and secondary virtual Socket instances in AWS for high availability. | [https://registry.terraform.io/modules/catonetworks/vsocket-aws-ha](https://registry.terraform.io/modules/catonetworks/vsocket-aws-ha) |
| vSocket AWS HA with VPC Module | Deploys HA virtual Sockets in an existing AWS VPC with all required networking setup. | [https://registry.terraform.io/modules/catonetworks/vsocket-aws-ha-vpc](https://registry.terraform.io/modules/catonetworks/vsocket-aws-ha-vpc) |
| vSocket AWS HA Transit Gateway Module | Deploys HA virtual Sockets in an existing AWS VPC with all required networking setup. Attaches the deployment to a transit gateway and specifies a default route to the EC2 instance. | [https://registry.terraform.io/modules/catonetworks/vsocket-aws-tgw-ha](https://registry.terraform.io/modules/catonetworks/vsocket-aws-tgw-ha) |
| vSocket Azure 3-NIC Module | Deploys a virtual Socket (3-NIC vSocket) in Azure and registers it as a Socket site. | [https://registry.terraform.io/modules/catonetworks/vsocket-azure](https://registry.terraform.io/modules/catonetworks/vsocket-azure) |
| vSocket Azure 2-NIC Module | Deploys a virtual Socket (2-NIC vSocket) in Azure and registers it as a Socket site. | [https://registry.terraform.io/modules/catonetworks/vsocket-azure-vnet-2nic/cato/latest](https://registry.terraform.io/modules/catonetworks/vsocket-azure-vnet-2nic/cato/latest) |
| vSocket Azure with VNet Module | Creates an Azure VNet and deploys a virtual Socket instance registered in the CMA. | [https://registry.terraform.io/modules/catonetworks/vsocket-azure-vnet](https://registry.terraform.io/modules/catonetworks/vsocket-azure-vnet) |
| vSocket Azure HA Module | Deploys high-availability virtual Sockets in Azure and registers them as a Socket site. | [https://registry.terraform.io/modules/catonetworks/vsocket-azure-ha](https://registry.terraform.io/modules/catonetworks/vsocket-azure-ha) |
| vSocket Azure 2-NIC HA Module | Deploys high-availability virtual Sockets in Azure (2-NICs) and registers them as a Socket site. | [https://registry.terraform.io/modules/catonetworks/vsocket-azure-ha-2nic/cato/latest](https://registry.terraform.io/modules/catonetworks/vsocket-azure-ha-2nic/cato/latest) |
| vSocket Azure HA with VNet Module | Creates an Azure VNet and deploys HA virtual Sockets integrated with the CMA. | [https://registry.terraform.io/modules/catonetworks/vsocket-azure-ha-vnet](https://registry.terraform.io/modules/catonetworks/vsocket-azure-ha-vnet) |
| vSocket GCP Module | Deploys a single virtual Socket instance in GCP and registers it as a Socket Site. | [https://registry.terraform.io/modules/catonetworks/vsocket-gcp](https://registry.terraform.io/modules/catonetworks/vsocket-gcp) |
| vSocket GCP with VPC Module | Creates a VPC in GCP and deploys a virtual Socket, integrating it with the CMA. | [https://registry.terraform.io/modules/catonetworks/vsocket-gcp-vpc](https://registry.terraform.io/modules/catonetworks/vsocket-gcp-vpc) |
| Bulk Internet Firewall Rules Module | Imports Internet Firewall (FW) rules and sections from a JSON configuration file, and defines the order of those rules and sections within the Cato Internet FW policy. | [https://registry.terraform.io/modules/catonetworks/bulk-if-rules/cato/latest](https://registry.terraform.io/modules/catonetworks/bulk-if-rules/cato/latest) |
| Bulk WAN Firewall Rules Module | Imports WAN Firewall (FW) rules and sections from a JSON configuration file, and defines the order of those rules and sections within the Cato WAN FW policy. | [https://registry.terraform.io/modules/catonetworks/bulk-wf-rules/cato/latest](https://registry.terraform.io/modules/catonetworks/bulk-wf-rules/cato/latest) |
| Bulk Network Range Module | Imports multiple site network ranges with their associated DHCP settings by accepting either CSV-decoded data or JSON arrays and automatically transforming them into the required nested structure. | [https://registry.terraform.io/modules/catonetworks/network-ranges-bulk/cato/latest](https://registry.terraform.io/modules/catonetworks/network-ranges-bulk/cato/latest) |
| Bulk TLS Rules Module | Import TLS Inspection rules and sections from a JSON configuration file, and define the order of those rules and sections within the Cato policy. | [https://registry.terraform.io/modules/catonetworks/bulk-tls-rules/cato/latest](https://registry.terraform.io/modules/catonetworks/bulk-tls-rules/cato/latest) |
| WAN Network Rules Module | Import WAN Network rules and sections from a JSON configuration file, and define the order of those rules and sections within the Cato policy. | [https://registry.terraform.io/modules/catonetworks/bulk-wnw-rules/cato/latest](https://registry.terraform.io/modules/catonetworks/bulk-wnw-rules/cato/latest) |
