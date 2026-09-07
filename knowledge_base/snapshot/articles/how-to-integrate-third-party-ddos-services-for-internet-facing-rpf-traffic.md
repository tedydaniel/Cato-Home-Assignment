---
title: "How to Integrate Third-Party DDoS Services for Internet-Facing RPF Traffic"
slug: "how-to-integrate-third-party-ddos-services-for-internet-facing-rpf-traffic"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/how-to-integrate-third-party-ddos-services-for-internet-facing-rpf-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Integrate Third-Party DDoS Services for Internet-Facing RPF Traffic

This article discusses how to integrate third-party DDoS protection solutions with an Internet facing public resource located behind a Cato site.

## Overview

Cato's [Remote Port Forwarding (RPF)](/docs/how-to-integrate-third-party-ddos-services-for-internet-facing-rpf-traffic#UUID-41bcd94b-2c61-4576-dd41-7abe84040d9b) is primarily designed to expose corporate resources to known corporate users with the Allow List approach. This means that you can restrict the corporate resource to the specific IP addresses that are allowed to connect, otherwise the traffic is blocked.

Sometimes it's necessary to provide access to unknown users, and expose an internal server via RPF publicly over the Internet. This creates a potential security risk, because you are allowing public access to internal resources. In this situation, we recommend that you secure the RPF traffic with a third-party DDoS cloud service in front of the site. For example, integrating a WAF to protect inbound HTTP traffic.

### Diagram of Sample Third-Party Security Solution with RPF

![Network_Diagram_-_RPF.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24448358577181.png)

## Integrating the Third-Party Solution to Secure RPF Traffic

This section explains how to configure the RPF resource to only allow the security service (such as DDoS) to access it. This adds a significant layer of security to the resource making available over the public Internet.

These are the configurations that you need to make:

- In the third-party cloud service define:
  - Public IPs that the service uses
  - DNS name for the resource mapped to the public IP address that Cato allocated to your account (**Network > IP Allocation)**
- In the Cato Management Application define an RPF rule to forward the traffic to the cloud service
  - The security stack in the Cato Cloud doesn't perform TLS inspection on inbound RPF traffic

**To integrate a third-party security service for RPF traffic:**

1. In the third-party security service, define these settings:
  1. Allocate a public IP address for the server.
  2. Configure the IP/CNAME for the IP address for the external RPF rule.
2. In the DNS provider, configure the domain to forward traffic to the IP/CNAME in the previous step.
3. Configure the policy for the third-party security service (WAF, inbound TLS inspection, and so on).
4. In the Cato Management Application define an RPF rule with these settings (**Security > Remote Port Forwarding**):
  - **External IP** and **External Port Range** for Cato public IPs (separate rule for each IP)
  - **Internal IP** and **Internal Port Range** for the internal resource
  - **Traffic Type** is **Allow List**
  - **Traffic Sources** are the public IP addresses for the cloud service (publicly advertised by the third-party security service)
