---
title: "Integrating Imperva Cloud WAF/DDoS Services for Internet-Facing RPF Traffic"
slug: "integrating-imperva-cloud-waf-ddos-services-for-internet-facing-rpf-traffic"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/integrating-imperva-cloud-waf-ddos-services-for-internet-facing-rpf-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Imperva Cloud WAF/DDoS Services for Internet-Facing RPF Traffic

This article discusses how to integrate the Imperva WAF/DDoS protection service with an Internet-facing public resource located behind a Cato site.

## Overview

Cato's [Remote Port Forwarding (RPF)](/docs/integrating-imperva-cloud-waf-ddos-services-for-internet-facing-rpf-traffic#UUID-41bcd94b-2c61-4576-dd41-7abe84040d9b) is primarily designed to expose corporate resources to known corporate users with the Allow List approach. This means that you can restrict the corporate resource to the specific IP addresses that are allowed to connect, otherwise, the traffic is blocked.

Sometimes it's necessary to provide access to unknown users and expose an internal server that is behind a site via RPF publicly over the Internet. This creates a potential security risk because you are allowing public access to internal resources. This article explains how to configure the Imperva Cloud service to provide WAF and DDoS protection in front of the site to secure the RPF traffic.

### Diagram of Incapsula Cloud WAF/DDoS with RPF

![Network_Diagram_-_RPF.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24448367794461.png)

## Integrating the Imperva DDoS Solution to Secure RPF Traffic

This section explains how to configure the RPF resource to only allow the Imperva Cloud WAF/DDoS to access it. This adds a significant layer of security to the resource that you are making available over the public Internet.

### Defining the RPF Rule in the CMA

Use the Cato Management Application (CMA) to define an allow list RPF rule to forward the traffic to the Imperva Cloud WAF. The Traffic Sources for the rule are based on the public [Imperva IP ranges](https://docs.imperva.com/bundle/z-kb-articles-km/page/c85245b7.html).

Create a separate rule for each data center and host that are protected by the Imperva Cloud.

The security stack in the Cato Cloud doesn't perform TLS inspection on inbound RPF traffic

![sample_imperva_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24448367861661.png)

**To define an allow list RPF rule that forwards traffic to the Imperva Cloud:**

1. From the navigation menu, click **Security > Remote Port Forwarding**.

The Remote Port Forwarding page opens to your existing unpublished revision, or to the newest published revision.
2. Create a new RPF rule with these settings:
  - **External IP** and **External Port Range** for Cato public IPs (use separate rules for each public IP)
  - **Internal IP** and **Internal Port Range** for the internal host or resource
  - **Traffic Type** is **Allow List**
  - **Traffic Sources** are a range of the public Imperva IP addresses
3. Click **Save** then **Publish**.
4. In the **Publish Revision** confirmation window, click **Publish**. Your revision is applied to the account policy.

### Defining the Imperva Cloud WAF to Protect the RPF Resource

In the Imperva management console, you can use one of these options to automate creating the site records:

- [Imperva Terraform provider](https://registry.terraform.io/providers/imperva/incapsula/latest/docs)
- [Imperva API documentation](https://docs.imperva.com/bundle/api-docs/page/api/api-overview.htm)
- [Imperva CLI](https://github.com/imperva/incapsula-cli)

**To integrate a third-party security service for RPF traffic:**

1. Create a site record in the [Imperva Cloud WAF](https://authentication-management.service.imperva.com/login) management console using the FQDN (www.your-website.com) of the site you are looking to protect.
2. [Configure SSL](https://docs.imperva.com/bundle/cloud-application-security/page/onboarding/cloud-application-security.htm#Step2) for your site leveraging an Imperva provisioned GlobalSign SSL certificate form, or upload a custom SSL certificate.
3. [Get the Imperva provisioned CNAME](https://docs.imperva.com/bundle/cloud-application-security/page/onboarding/cloud-application-security.htm#Step3) for your site record.
4. Add the Cato-allocated public IP addresses used in the RPF rules above as the [origin server entries](https://docs.imperva.com/bundle/cloud-application-security/page/settings/load-balancing-settings.htm) in Imperva Cloud WAF, and select a load balancing option.
5. In the DNS provider, configure the domain to forward traffic to the Incapsula CNAME in step 3.
