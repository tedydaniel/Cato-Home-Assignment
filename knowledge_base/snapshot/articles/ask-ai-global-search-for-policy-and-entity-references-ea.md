---
title: "Ask AI Global Search for Policy and Entity References (EA)"
slug: "ask-ai-global-search-for-policy-and-entity-references-ea"
updated: 2026-08-27T11:29:00Z
published: 2026-08-27T11:29:00Z
canonical: "knowledge.catonetworks.com/ask-ai-global-search-for-policy-and-entity-references-ea"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ask AI Global Search for Policy and Entity References (EA)

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information about enabling the feature, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

## Overview

Ask AI helps you quickly find where a Cato Management Application object or entity is used across different policies. You can use global search to assess the impact of a change, review existing policy usage, and avoid checking each policy separately.

- For more information, see [What is Cato's Ask AI Agent](/docs/ask-ai-global-search-for-policy-and-entity-references-ea#)

## Supported Policies for Global Search

Global search supports cross-policy searches for these policies.

### Security

- Anti-Malware > File Hash Policy
- App & Data Inline Protection
- Application Control Policy
- Tenant Restriction
- Agentic Threat Prevention
- Internet Firewall
- LAN Firewall
- TLS Inspection
- WAN Firewall

### Networking

- DNS Settings
- IP Allocation
- Network Rules
- Site Configuration > Bypass

### Access

- Always-On Policy
- Browser Access Control > Access Policy
- Client Connectivity Policy
- Proxy Configuration Policy
- Split Tunnel Policy

## Supported Entity Types for Global Search

Global search supports searches for these entity types across all supported policies.

### Applications and Categories

- Application
- Application Category
- Custom Application
- Custom Category

### Sites and Network Objects

- Host
- Network Interface
- Site

### Users and Groups

- Directory User
- Group
- System Group
- User
- Users Group

### Device Profiles

- Device Profile

### Services

- Custom Service
- Service

### Geographic Objects

- Country

### IP Ranges and Subnets

- Floating Subnet
- Global IP Range
- Global Range
- Interface Subnet
- Site Network Subnet

### Address and Domain Containers

- Allocated IP
- FQDN Container
- IP Address Range Container

### Notification Targets

- Subscription Group
- Subscription Mailing List
- Subscription Webhook

## Example Questions for Global Search

- In which policies is Japan used?
- In which policies is hq_site used?
- Show all policies that reference example_group
- Where is Salesforce used across policies?
- Which policies reference 192.168.0.0/24
- Which rules apply to example_user?

## Example Questions for Internet Firewall Policy

- Are there rules preventing users from accessing social media sites?
- Who was the last person to update the Internet Firewall rules, and when?
- Show me all Internet Firewall rules that are currently inactive or disabled
- Do we have rules blocking inbound connections from the Internet?

## Example Questions for WAN Firewall Policy

- Show me all WAN Firewall rules between site A and site B
- Which WAN Firewall rules apply to the Finance group?
- Are there any WAN Firewall rules blocking connectivity between specific sites?
- What are the WAN Firewall rules with the most hits?

## Example Questions for LAN Firewall Policy

- Show me traffic that the LAN Firewall blocks at the site HQ
- What LAN Firewall rules are configured for the guest WiFi network?
- Which LAN Firewall rules allow traffic locally without sending to the PoP?

## Example Questions for TLS Inspection Policy

- Which sites or users have TLS Inspection bypassed?
- Show me TLS Inspection rules with the Inspect action
- What is the minimum TLS version and cipher suite configured in the policy?

## Example Questions for Application Control Policy

- Which applications are blocked in the Application Control policy?
- Show me DLP rules for file uploads/downloads
- What SaaS applications have tenant restrictions configured?
- Are there rules restricting access to high-risk applications?

## Example Questions for Client Connectivity Policies

- Which users have Always-on enabled?
- Show me Client Connectivity rules with device posture requirements
- What are the posture requirements for remote users?

## Example Questions for Split Tunnel Policy

- Which applications or domains are excluded from the tunnel?
- Show me Split Tunnel rules for specific user groups
- What is the Split Tunnel configuration for remote users located in Japan?
