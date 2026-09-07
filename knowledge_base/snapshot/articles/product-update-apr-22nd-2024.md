---
title: "Product Update - Apr. 22nd, 2024"
slug: "product-update-apr-22nd-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-apr-22nd-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Apr. 22nd, 2024

## New Features & Enhancements

- **New SaaS Security API Connector for Workplace from Meta:** Over the next few weeks, we’re adding a [connector for Workplace from Meta](https://support.catonetworks.com/hc/en-us/articles/17904249251101-Configuring-the-SaaS-Security-API-Connector-for-Workplace-from-Meta) that lets you monitor for sensitive data in user posts, comments, and chats in your Workplace tenant. For example, detect when a user posts a message containing credit card details or API tokens.
  - Scans can include attachments
  - Events provide a link to the relevant message
- **Improved Supportability for SaaS Security API Connector Issues:** The [Integrations](/v1/docs/using-the-integrations-page) page now shows detailed information for the connectivity **Status** of SaaS Security API connectors, based on the errors reported by the SaaS vendor.
  - The new information is available for these connectors: Box, Sharepoint, OneDrive, Exchange
- **Client Connectivity Policy is the Central Location to Manage Device Posture Requirements:** For customers who didn’t configure settings on the Device Authentication page, this page is no longer available in the Cato Management Application. You can manage all posture requirements using the [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy).
  - Device certificates can still be managed from the Access > Client Access page. For more information, see [Controlling Certified Corporate Devices](https://support.catonetworks.com/hc/en-us/articles/4413280521361-Controlling-Certified-Corporate-Devices-Device-Authentication)
  - We are sending dedicated customer communications for impacted customers to explain how to transition to the Client Connectivity Policy
- **AWS vSocket IMDSv2 Support:** To align with AWS best practices, we are introducing support for the IMDSv2 security option for [AWS vSocket sites](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace), which employs session-oriented authentication mechanisms.
  - Supported for Socket v20.0.18221 and higher
  - Enabling IMDSv2 support on the EC2 instance doesn't impact the site functionality
- Go to the [Cato Product Roadmap](https://support.catonetworks.com/hc/en-us/articles/14517158733853-Cato-Product-Roadmap) in the Knowledge Base to follow the status of upcoming features and enhancements.

## PoP Announcements

- **Tokyo PoP Location IP Range Optimization:** We are improving the PoP infrastructure for the IP range 123.253.152.0/24 that belongs to the Tokyo PoP locations.
- A new geo-localized IP range is available for Paraguay, serviced through the Santiago PoP location: 150.195.192.0/28.
