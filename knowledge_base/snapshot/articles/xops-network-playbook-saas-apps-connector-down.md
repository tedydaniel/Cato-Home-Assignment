---
title: "XOps Network Playbook - SaaS Apps Connector Down"
slug: "xops-network-playbook-saas-apps-connector-down"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-saas-apps-connector-down"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - SaaS Apps Connector Down

This playbook describes steps to resolve issues when a Saas Apps Connector Down Indication is detected.

## Overview

This playbook guides you through resolving the SaaS Apps Connector Down alert, which can occur due to an issue with the connector responsible for integrating a SaaS application with Cato has lost connectivity or failed a health check.

## Step 1 - Identifying the Relevant Connector

**First, you need to identify the connector causing the alert.**

**Check the Connector Status:** On the **Resources > Integrations > Integrated Apps** page in the Cato Management Application (CMA) to view the status of the connector.

- Statuses can be: Connected, Warning, or Failure.
- “Warning” typically means a connectivity or permissions issue, or possibly rate limiting from the SaaS vendor (e.g., Microsoft).

## Step 2 - Immediate Steps to Take

**Once you have identified the connector, take steps to find the cause of the issue.**

- **Review Error Details:** Use the action menus in the connectors dashboard to access error logs for the connector. This will help you identify the root cause (e.g., expired credentials, permission changes, vendor-side issues).
- **Check for Vendor-Specific Issues:**
  - For Microsoft connectors, rate limiting or permission changes are common causes.
  - For Box, Slack, and others, check for known limitations (e.g., only one connector per tenant, delays in event generation).

## Step 3 - Troubleshooting Steps

- **Validate Credentials and Permissions:** Ensure that the connector’s credentials are valid and have not expired. Confirm that the required permissions are still granted in the SaaS application.
- **Check for Configuration Changes:** If there were recent changes to the SaaS app (e.g., user permissions, API access), these might have broken the connector.
- **Attempt to Reconnect:** If the connector is in a failed state, try to re-establish the connection. This may involve re-authenticating or re-creating the connector.

## Raising a Ticket with Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
