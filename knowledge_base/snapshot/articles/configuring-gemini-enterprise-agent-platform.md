---
title: "Configuring Gemini Enterprise Agent Platform"
slug: "configuring-gemini-enterprise-agent-platform"
status: "new"
updated: 2026-09-06T13:04:01Z
published: 2026-09-06T13:04:01Z
canonical: "knowledge.catonetworks.com/configuring-gemini-enterprise-agent-platform"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Gemini Enterprise Agent Platform

## Overview

Cato lets you monitor Gemini Enterprise Agent Platform session activity from the CMA, helping admins review agent activity across the connected Google Cloud project. You configure the integration by running a setup script in Google Cloud Shell.

Cato can view sessions and session events, but does not collect or display the tools, integrations, or external services an agent uses during a session.

The connection uses Google Cloud Workload Identity Federation. Cato accesses the project by impersonating a dedicated service account, and no service-account key is created or shared.

### Prerequisites

Before you start, confirm the following:

- You have access to the Google Cloud project that contains the Gemini Enterprise Agent Platform resources you want Cato to monitor.
- You have permission to enable required Google Cloud APIs and create or update IAM resources in the project.
- You can create Workload Identity Federation resources, service accounts, custom IAM roles, and IAM policy bindings.
- You can access Google Cloud Shell.

## Connect Gemini Enterprise Agent Platform

Cato uses a Google Cloud setup script to configure the connection. The script creates the required federation configuration and grants Cato read-only access to the selected project.

To connect Gemini Enterprise Agent Platform:

1. From the navigation menu, select **AI Security** > **Integrations**.
2. Locate **Gemini Enterprise Agent Platform** and click **Connect**.
3. Click **Connect Google Cloud**.
4. Click the link to open Google Cloud Shell and display the generated setup command.
5. Review the command, then run it in Google Cloud Shell.
6. When prompted, review the Google Cloud project, Cato identity, and requested permissions, then confirm the installation.

The script configures the connection and verifies it automatically. The integration shows as connected in the CMA when verification succeeds.

## Review the Requested Permissions

The setup script creates a dedicated service account and grants it the read-only permissions Cato needs to access Gemini Enterprise Agent Platform session activity.

The permissions allow Cato to:

- List available Google Cloud locations
- List managed agent resources
- List agent sessions
- List events within agent sessions

The script does not create a service-account key and does not grant write permissions.

Before you run the script, verify that the displayed Google Cloud project, Cato AWS identity, Cato tenant, and requested permissions match your organization's requirements.

## How the Connection Works

Cato uses Workload Identity Federation to connect its AWS workload identity to your Google Cloud project. The setup script creates a workload identity pool, an AWS identity provider, and a dedicated Google Cloud service account.

Cato can impersonate the service account only when its AWS identity matches the configured Cato role and tenant. This lets Cato access the granted Google Cloud resources without storing long-lived Google Cloud credentials.

## Troubleshooting

### The setup script cannot find a Google Cloud project

In Google Cloud Shell, select the project you want to connect, then run the setup command again.

```bash
gcloud config set project PROJECT_ID
```

### The setup script fails with a permission error

Confirm that your Google Cloud identity can enable APIs and create or update the required IAM resources in the selected project. Contact a Google Cloud administrator if you do not have the required permissions.

### Cato cannot verify the connection

Google Cloud IAM changes can take several minutes to propagate. Wait a few minutes, then restart the connection from the CMA and run the newly generated setup script.

### The onboarding token is invalid or expired

Start the connection again from the CMA. Cato generates a new setup script with a new onboarding token.

## Disconnect and Cleanup

Disconnecting the integration in the CMA stops Cato from using the connection.

To fully remove Cato's access from Google Cloud, remove the federation configuration, service account, custom role, and related IAM policy bindings that the setup script created. Coordinate with your Google Cloud administrator before removing these resources if they are used by another Cato integration.
