---
title: "Reference for Rule Objects"
slug: "reference-for-rule-objects"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/reference-for-rule-objects"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference for Rule Objects

This article describes the objects that can be configured in the **Source**, **Destination**, and **App/Category** fields in rules for policies.

## Source and Destination Objects

The following table describes the objects that you can use in the **Source** and **Destination** fields.

| Item | Description | Screen Where Defined |
| --- | --- | --- |
| Site | Sites defined for the account | Network > Sites |
| Host | Hosts and servers defined in the sites | Network > Sites > Site Settings > Hosts |
| Interface Subnet | Subnets and network ranges defined for the LAN interfaces of a site | Network > Sites > Site Settings > Networks |
| Global Range | Native range for the LAN interface of a site | Network > Sites > Site Settings > Networks |
| Network Interface | Networks defined in the sites | Network > Sites > Site Settings > Networks |
| Floating Subnet | Global IP ranges that are not connected to a specific site, but can be learned from any site with a BGP neighbor | Resources > Floating Ranges |
| SDP User | Individual users defined for the account | Access > Users |
| Group | Groups in the account | Resources > Groups |
| System Group | Predefined groups | N/A |
| User | Users that are imported with Directory Services | Access > Directory Services |
| IP | Enter the IP address with the CIDR that is applied to this rule | N/A |
| IP Range | For the **Source** of a rule, enter the multiple separate IP addresses or IP range that is applied to this rule (in one of the following formats): - 192.168.0.26, 192.168.0.58, 192.168.0.200 - 192.168.0.1-192.168.0.100 - 192.168.0.0/24 | N/A |
| Any | Any source or destination | N/A |

## App/Category Objects

The following table describes the objects that you can use in the **App/Category** field.

| Item | Description | Where Configured |
| --- | --- | --- |
| Application | Default applications defined by Cato | Default values, cannot be configured |
| Custom Application | Custom applications defined for the account | Resources > Custom Apps |
| Application Category | Default categories defined by Cato | Default values, cannot be configured |
| Custom Category | Custom categories defined for the account | Resources > Categories |
| Custom Service | A user-defined service including a protocol and port. Used in Network Rule policies. | Setting for this rule |
| Custom Service IP | A user-defined service, including the service name and IP address or range. Used in Network Rule policies. | Setting for this rule |
| FQDN | FQDN is an exact match of the fully qualified domain (for example, the FQDN **example.com** only matches **example.com**) Specifying ​**sub1.example.com**​ only includes that exact subdomain. Subdomains such as ​**sub2.sub1.example.com**​​ are not included and are treated separately. Wildcards are not supported. | Setting for this rule |
| Domain | A Domain is a Registered Domain and matches all subdomains. For example, the Domain **example.com** matches **example.com**, **host.example.com**, and **subhost.host.example.com** | Setting for this rule |
| IP Range | Enter the IP addresses with the CIDR for the apps that are applied to this rule | Setting for this rule |
| Any | Any web content, application, or category | Default values, cannot be configured |
