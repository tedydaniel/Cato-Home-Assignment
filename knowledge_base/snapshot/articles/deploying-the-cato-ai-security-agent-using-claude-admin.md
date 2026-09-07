---
title: "Deploying the Cato AI Security Agent using Claude Admin"
slug: "deploying-the-cato-ai-security-agent-using-claude-admin"
updated: 2026-08-18T06:30:24Z
published: 2026-08-18T06:30:24Z
canonical: "knowledge.catonetworks.com/deploying-the-cato-ai-security-agent-using-claude-admin"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying the Cato AI Security Agent using Claude Admin

## Overview

The Cato AI Security Agent lets you connect Claude to Cato AI Security so admins can monitor and govern AI usage in your organization. Deploy the agent from Claude Admin by adding the Cato marketplace source, enabling the Cato agent plugin, and providing the Cato AI Security API key.

After the configuration is applied, Claude users in your organization can use the Cato AI Security Agent according to the access controls configured in Claude Admin.

## Prerequisites

Before you deploy the agent, make sure you have:

- A Claude for Work account with permissions to manage integrations or extensions
- A Cato AI Security license
- A Cato AI Security API key
- Access to Claude Admin

## Configure the Cato AI Security Agent

Use the following JSON configuration to deploy the Cato AI Security Agent in Claude Admin. Replace `[SECRET_1]` with the API key provided for your Cato AI Security tenant.

To configure the Cato AI Security Agent:

1. In Claude Admin, navigate to Admin Settings > Claude Code > Managed Settings.
2. Add a custom JSON configuration.
3. Paste the following JSON:

```json
{
    "extraKnownMarketplaces": {
        "cato-networks": {
            "source": {
                "source": "github",
                "repo": "catonetworks/agent-plugins"
            },
            "autoUpdate": true
        }
    },
    "enabledPlugins": {
        "scout@cato-networks": true
    },
    "env": {
        "SCOUT_PLUGIN_API_KEY": "[SECRET_1]",
        "SCOUT_PLUGIN_BASE_URL": "https://api.aisec.catonetworks.com"
    }
}
```

4. Save the configuration.

## Understanding the JSON Configuration

The JSON configuration includes the following settings:

| Setting | Description |
| --- | --- |
| `extraKnownMarketplaces` | Adds the Cato Networks marketplace source to Claude |
| `source` | Defines GitHub as the source for the Cato agent plugins |
| `repo` | Defines the GitHub repository that hosts the plugin |
| `autoUpdate` | Allows Claude to automatically update the plugin when a new version is available |
| `enabledPlugins` | Enables the Cato AI Security Agent plugin |
| `SCOUT_PLUGIN_API_KEY` | Authenticates the agent to Cato AI Security |
| `SCOUT_PLUGIN_BASE_URL` | Defines the Cato AI Security API endpoint |
