---
title: "Advanced Configuration for Claude Code"
slug: "advanced-configuration-for-claude-code"
updated: 2026-08-18T06:30:07Z
published: 2026-08-18T06:30:07Z
canonical: "knowledge.catonetworks.com/advanced-configuration-for-claude-code"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced Configuration for Claude Code

This article provides information about deploying Claude Code with advanced settings. For information about deploying Scouts and Agent Controls, see [Understanding Scouts and Agent Controls](/v1/docs/understanding-scouts-and-agent-controls).
## Overview

Advanced Configuration lets security administrators centrally manage how Claude Code behaves for users in your organization. Using a JSON policy file, you can define which AI models users can access, which shell commands Claude can run, which files it can read, and how sandboxed Bash commands interact with the network. This helps enforce consistent security, governance, and cost controls across managed endpoints.

## Before You Begin

Make sure you have:

* Permission to manage Claude Code settings for your organization
* A valid `managed-settings.json` file
* Access to the Claude Admin Console
* A test endpoint with Claude Code installed

## Understand How Managed Settings Are Applied

When Claude Code starts, it checks for managed settings that are configured for your organization. These settings have the highest precedence and cannot be overridden by user-level or project-level settings.

The managed configuration file defines the approved Claude Code behavior for users in your environment. This lets you centrally control model access, permissions, file access, sandboxing, environment variables, and announcements.

## Review Supported Policy Controls

| Control       | Description                                                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Models        | Define which Claude models users can access                                                                                         |
| Permissions   | Control which tools and shell commands Claude Code can run, ask before running, or block                                            |
| File access   | Define which files and directories Claude Code can read or modify                                                                   |
| Sandboxing    | Isolate Bash commands at the OS level, restrict filesystem write paths, and control network domains used by sandboxed Bash commands |
| Environment   | Configure environment variables for Claude Code                                                                                     |
| Announcements | Display organization-wide messages to Claude Code users                                                                             |

The sandbox configuration applies to Bash commands and their child processes. Use permission rules to control other Claude Code tools such as Read, Write, WebFetch, and MCP.

## Upload the Configuration File

Advanced Configuration is managed in the Claude Admin Console under **Advanced Configuration** > **Claude Custom Configuration**.

To upload the managed settings file:

1. Enable the **Claude Custom Configuration** toggle.
2. Paste or upload the contents of your `managed-settings.json` file into the editor.
3. Click **Save**.

The policy applies the next time Claude Code loads the managed settings on user endpoints.
## Advanced Configuration for Individual Endpoints
You can apply advanced configuration settings for individual endpoints by placing the custom configuration file locally on an endpoint. Depending on your operating system, the file should be located in the following location:
* macOS - save the settings.json file to ~/.claude/
* Windows - save the settings.json file to %USERPROFILE%\claude
:::(Info) (Note)
If your organization is using Claude Admin to deploy a custom configuration, the global settings will override local settings.
:::

## Review the Configuration File Format

The configuration file uses JSON format. The following example shows the structure of a managed settings file, but does not represent a real-life configuration for your environment. Review and update the values based on your organization’s security, governance, and operational requirements.

```json id="69mg93"
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "claude-sonnet-4-6",
  "availableModels": [
    "claude-sonnet-4-6"
  ],
  "permissions": {
    "allow": [
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Read(/Users/*/projects/**)"
    ],
    "ask": [
      "Bash(npm install:*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Write(/etc/**)"
    ],
    "disableBypassPermissionsMode": true
  },
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "allowedDomains": [
      "registry.npmjs.org",
      "api.github.com"
    ],
    "allowWrite": [
      "/Users/*/projects/**"
    ]
  }
}
```

In this example:

* Users can access only the example Claude model
* Claude Code can run approved read-only shell commands without prompting
* Claude Code asks before it runs commands such as `npm install`
* Commands such as `rm` and `curl` are blocked
* Users cannot bypass the configured permission mode
* Sandboxed Bash commands can write only to approved project paths
* Sandboxed Bash commands can access only approved domains

## Test the Policy

Before you deploy the policy to all users, validate it on a test machine.

To test the policy:

1. Deploy the managed settings file to a test machine.

2. Run:

   ```bash
   claude doctor
   ```

3. Review any invalid or unrecognized fields.

4. Update the JSON file and test again before deployment.
