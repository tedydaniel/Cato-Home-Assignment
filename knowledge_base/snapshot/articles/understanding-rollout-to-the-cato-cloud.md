---
title: "Understanding Rollout to the Cato Cloud"
slug: "understanding-rollout-to-the-cato-cloud"
updated: 2026-07-08T10:42:15Z
published: 2026-07-08T10:42:15Z
canonical: "knowledge.catonetworks.com/understanding-rollout-to-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Rollout to the Cato Cloud

This article explains the process for new content that is gradually rolled out and implemented for the Cato service.

## Overview

Cato follows standard industry best practices for cloud-based services, and gradually rolls out new features, security updates and improvements for the Cato service that includes different products: Cato Cloud, Sockets, and Clients. Cato's process to gradually update the Cato service ensures minimal impact on customers and end-users. For the Cato Cloud, in the rare case that an issue is detected, rollback and recovery features help to maintain the stability and resiliency of the network.

The descriptions in this article are based on sites and SDP users that follow Cato's recommended settings and configurations. For more information, see below [Cato's Best Practices for Updates to the Cato Service](/v1/docs/understanding-rollout-to-the-cato-cloud-1#catos-best-practices-for-updates-to-the-cato-service).

## Updating the Cato Cloud

The Cato Cloud service includes two main components: PoPs and the Cato Management Application (the console to manage your account settings). Cato regularly deploys gradual updates to the PoPs in the Cato Cloud with new content, including: new features, updates, security patches and protections, infrastructure enhancements, and more.

The Cato PoP is a location that is constructed of many compute nodes. Each can serve any remote user or site. The update is gradually rolled out to the compute nodes in the PoP.

This is the cadence for gradually updating the components in the Cato service:

- **PoPs in the Cato Cloud** - Cato PoPs are updated with new content on a bi-weekly schedule.
  - Starting from Sunday, the content is gradually rolled out to the PoPs over two weeks.
  - During the Sunday maintenance window for PoP updates, the relevant sites and SDP users automatically reconnect to the same PoP. The update process can take up to 10 seconds to complete with minimal impact. During the update, other PoPs in the Cato Cloud continue to process the traffic and flows for the sites and SDP users using Cato's resiliency features.
  - If an issue is detected during the two week rollout, the Cato Cloud has self-healing tools that automatically roll back to the previous version. After Cato resolves the issue, then the fixed version is gradually deployed during a future maintenance window.
- **Cato Management Application** - The maintenance window to update the Cato Management Application with new content is every week on Sunday. There is no impact to our customers' networks during the update for the Cato Management Application.
  - New features are gradually activated for customer accounts in the Cato Management Application over the same two-week rollout period as the PoPs. This means that a feature that is announced in the weekly Release Notes can take up to two weeks to be available in a specific account.

You can use this [webpage](https://status.catonetworks.com/) to view the current maintenance status and upcoming maintenance windows for specific PoPs in the Cato Cloud and for the Cato Management Application.

### Rollout Stages

Cato uses automated continuous integration and continuous deployment (CI/CD) processes to evaluate and approve the code for each deployment.

These are the stages that Cato follows to roll out new content:

- **Automation and CI/CD** - Content is tested and validated for upcoming deployment
- **Early Availability (EA)** - Customers can choose to test new features as part of Cato's EA program

For more information about EA features, see these [EA Documentation](/v1/docs/ea-documentation-1) articles
- **General Availability (GA)** - Content is gradually rolled out to all customers during Cato's scheduled maintenance window (as explained in the previous section)

### Security Updates

Cato's Security team is constantly working to create patches and protections to keep the Cato Cloud safe from malware. This means that sometimes we are gradually deploying security updates with new signatures and protections to the PoPs as required, and not during the scheduled maintenance windows. Deploying these security updates doesn't impact sites and SDP users.

## Cato's Best Practices for Updates to the Cato Service

- For IPsec and Cloud Interconnect sites, we strongly recommend that you configure a secondary tunnel that connects to a different PoP than the primary tunnel. For sites that only connect to one PoP with a primary tunnel, it's possible that the regular Cato service updates can impact them for a few minutes.
- For Socket version upgrades, Cato manages the Socket firmware upgrades and version control for Socket sites to make sure that they are running up-to-date versions. For more information, see [Understanding Cato's Managed Socket Upgrade Service](/v1/docs/understanding-cato-s-managed-socket-upgrade-service).
- For Cato Client version upgrades, we recommend that you use Cato's managed upgrade service to make sure that the Clients are using the most up-to-date versions. For more information, see [Best Practices for Cato Client Upgrades](/v1/docs/recommendations-for-cato-client-upgrades).
