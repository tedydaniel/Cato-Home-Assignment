---
title: "Microsoft Changing Default Outbound Access Behavior for New Virtual Networks"
slug: "microsoft-changing-default-outbound-access-behavior-for-new-virtual-networks"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/microsoft-changing-default-outbound-access-behavior-for-new-virtual-networks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Changing Default Outbound Access Behavior for New Virtual Networks

Microsoft has announced that **after March 31, 2026**, newly created virtual networks in Azure will no longer include default outbound Internet access. Instead, new VNets will use private subnets by default, requiring an explicitly defined outbound connectivity method (such as Public IP, NAT Gateway, or Azure Load Balancer) to reach the Internet or Microsoft services.

## Impact on Azure vSocket Deployments

- **No change is required** for existing vSockets using the current default NONE outbound method—this configuration remains supported by [Microsoft](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access?utm_source=chatgpt.com). However, Microsoft recommends transitioning any existing VMs that rely on default outbound access to use an explicit method of connectivity.

- **New vSockets** deployed from the Azure Marketplace will default to using **Public IP** to ensure proper outbound connectivity.

- If your deployment requires a different outbound method, you can configure it during the deployment process using the Azure Marketplace wizard or Terraform module.
  - When deploying resources with an Availability Zone set, the Public IP Set will not work. As a workaround, deploy the Availability Zone using the marketplace deployment wizard and manually configure the Public IP Set after the deployment wizard is complete.

For details on Microsoft’s change and supported outbound access options, see [Default outbound access for VMs in Azure](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access?utm_source=chatgpt.com).

## Update to Terraform Module

Cato has updated its Terraform module to align with this Azure change. The updated module will support explicit outbound access configurations, providing flexibility and ensuring successful vSocket deployments after March 31, 2026. The default setting is now **Public IP**.

We recommend reviewing your deployment workflows to ensure they reflect these changes ahead of time.
