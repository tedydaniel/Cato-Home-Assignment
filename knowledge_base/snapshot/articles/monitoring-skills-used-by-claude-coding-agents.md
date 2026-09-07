---
title: "Monitoring Skills Used by Claude Coding Agents"
slug: "monitoring-skills-used-by-claude-coding-agents"
updated: 2026-08-04T14:15:52Z
published: 2026-08-04T14:15:52Z
canonical: "knowledge.catonetworks.com/monitoring-skills-used-by-claude-coding-agents"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Skills Used by Claude Coding Agents

## Overview

Claude coding agents can use skills to extend what they can do beyond the user’s original prompt. A skill can include instructions, files, scripts, commands, and tool guidance that the agent uses to complete a task. This can create potential risks when skills come from untrusted sources or include malicious instructions. For example, a skill can influence how the agent accesses files, runs commands, or uses connected tools.

Cato AI Security helps you monitor skills used in your organization so you can review their source, inspect their content, identify risky capabilities, and investigate related activity in Agent Sessions. 

### Prerequisites

- AI Security for Users license
- [Scout](/v1/docs/understanding-scouts-and-agent-controls-1) deployed on user endpoints
- Agent Controls enabled for supported Claude coding agents

## Review Skills in the Agent Inventory

The **Skills** tab in the Agent Inventory page shows skills identified from activity analyzed by Scout and Agent Controls.

Use the page to:

- Review Skills available to users
- Identify frequently used Skills
- Review the source of a Skill
- Find Skills with security findings
- See when a Skill was last detected
![local_agents_skills.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/local_agents_skills.png){height="" width=""}

**To show Skill usage:**

1. From the navigation menu, select **AI Security > Agent Inventory**.
2. Select the **Skills** tab.


### Discovering skills

Use the filters to narrow the Skills inventory to the activity you want to review.

For example, to find potentially risky Skills from a specific source:

1. In **Source**, select the repository or publisher.
2. In **Findings**, select one or more findings, such as:
   - **Unrestricted Filesystem Write**
   - **Unrestricted Shell Access**
3. Review the matching Skills in the table.

## Investigate a Skill

Click a skill to open the Skill Quick View panel that helps you understand: where the Skill came from, what it is designed to do, and whether it contains potentially risky capabilities.

### Skill Details
![findings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/findings.png){height="" width=""}

The Skill Quick View begins with a summary that shows how widely the skill is used in your organization.

- **Installed On Users** - Number of users detected with the skill 
- **Usage** - Total number of skill invocations 
- **Usage by User** - Number of unique users who invoked the Skill

The **Skill Details** section provides information about the skill and helps you determine whether it originates from a trusted source.

- **Skill Description** explains the purpose of the skill and the task it is designed to perform
- **Source Type** shows how the skill was distributed, such as a plugin or Git repository
- **Plugin Name**, **Marketplace**, and **Marketplace URL** identify where the Skill originated and provide a link to the published source so you can validate its origin and review the published content

### Findings

The **Findings** section shows potentially risky capabilities detected in the Skill definition.

Each finding includes:

- **ID** - Unique Cato identifier for the finding
- **Finding** - Name of the detected capability
- **Description** - Explanation of the behavior and its potential risk
- **Risk Category** - Type of risk associated with the finding

For example, findings can indicate that a Skill allows unrestricted shell access or unrestricted filesystem write access.

### Skill MD
![skill_md.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/skill_md.png){height="" width=""}

The **Skill MD** section shows the collected skill definition and the versions identified by Cato. Use this information to review how the skill is configured and whether its declared capabilities match its intended purpose.

- **Version** - Shows when the Skill definition was collected or updated
- **Metadata** - Shows configuration details defined for the Skill
- **Allowed Tools** - Identifies the tools the Skill is permitted to use
- **Invocation Settings** - Shows how the Skill can be triggered or invoked



### Skill Content

The **Skill Content** section shows the complete instructions defined in the skill. Use the Skill content together with the findings and metadata to assess if this is an approved skill for the company, or if it's risky and you don't want to allow it. 

Review the content to understand:

- The task the Skill is designed to perform
- The workflow the agent is instructed to follow
- The commands the Skill can run
- The tools the Skill can use
- The actions the Skill can perform on files or external systems


## Known Limitations

- Skills visibility is currently supported for Claude coding agents
- Matching skills to users is based on best-effort user identification
- Usage data depends on activity analyzed by Scout and Agent Controls
