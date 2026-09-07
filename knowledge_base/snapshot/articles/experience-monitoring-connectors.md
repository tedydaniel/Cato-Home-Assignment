---
title: "Configuring Experience Monitoring UCaaS Connectors"
slug: "configuring-experience-monitoring-ucaas-connectors"
updated: 2026-08-31T19:26:51Z
published: 2026-08-31T19:26:51Z
canonical: "knowledge.catonetworks.com/configuring-experience-monitoring-ucaas-connectors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Experience Monitoring UCaaS Connectors

This article explains how to configure integrations between Cato and your UCaaS applications so that application-specific metrics are displayed on the Experience Monitoring Page.

## Overview

Experience Monitoring provides enhanced context, such as packet loss or tunnel age, to give you the information you need to determine if the issues are related to your ISP, the Cato Cloud, or other sources.

You can also configure a connector with UCaaS applications to display application-specific metrics to monitor the user experience when using the application. Once you have created the connector, add the required information in the CMA.

**Note:** Admins require [edit permissions](/v1/docs/managing-admin-roles-using-rbac) for the relevant CMA pages (such as Resources > Integrations) to add a new DEM connector.

A DEM license is required to display Application-Specific Metrics. For more about purchasing a DEM license, please contact your Cato representative.

## Configuration Application-Specific Metrics

Follow these steps to configure Application-Specific Metrics:

1. Configure the integration within the UCaaS application
2. Create the API connector in the CMA

### Supported Applications

The supported applications are:

- [Microsoft Teams](/v1/docs/microsoft-teams-configuring-the-experience-monitoring-ucaas-connector)
- [Webex](/v1/docs/webex-configuring-the-experience-monitoring-ucaas-connector)
- [Zoom](/v1/docs/zoom-configuring-the-experience-monitoring-ucaas-connectors)

### Prerequisites

- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).
