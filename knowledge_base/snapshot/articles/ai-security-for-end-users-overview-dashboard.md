---
title: "AI Security for End Users Overview Dashboard"
slug: "ai-security-for-end-users-overview-dashboard"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/ai-security-for-end-users-overview-dashboard"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Security for End Users Overview Dashboard

The AI Security for End Users Overview Dashboard provides a centralized view of generative AI usage across your organization. You can quickly understand the scale of AI adoption, identify policy violations, and assess potential risk from AI interactions. This dashboard helps you monitor usage trends, detect risky behavior, and decide where deeper investigation or enforcement is required.

To learn how to refine and analyze dashboard data using filters, see [Configuring Filters to Analyze Dashboard Data](/v1/docs/configuring-filters-to-analyze-dashboard-data).

![AI_Security_Overview.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34140925117469.png)

## Showing the Overview Dashboard

To show the Overview dashboard:

1. From the navigation menu, click **AI Security > Monitoring > Overview**.

## Dashboard Summary Metrics

The top section of the dashboard provides high-level metrics that summarize AI usage:

- Total AI Apps - the total number of AI applications detected in your organization. This metric helps you understand the overall AI application footprint, including sanctioned and shadow AI tools.
- AI Users - the total number of users who interacted with AI applications. This provides visibility into how broadly AI tools are adopted across the organization.
- AI Interactions - the total number of AI interactions detected. This reflects the overall volume of prompts or interactions with AI tools.
- Adoption Rate - the percentage of users adopting AI tools, along with a trend indicator. This metric helps you track how AI usage evolves over time.

## AI Violation Rate

The AI Violation Rate widget shows the percentage of AI interactions that resulted in a policy violation.

This provides a quick indicator of overall risk posture by highlighting how much AI activity violates defined interaction policies.

### Violation Breakdown

The Violation Breakdown widget shows the total number of violations and how they are distributed across different AI interaction policy rules. You can use this widget to:

- Understand which rules are most frequently violated. Prioritize policy tuning or user awareness efforts
- Identify patterns in policy enforcement.
- Prioritize policy tuning or user awareness efforts

Click **View AI Interaction Policy** to review or adjust the relevant policies.

## Latest Application Discovered

The Latest Application Discovered widget lists newly detected AI applications. This helps you:

- Identify shadow AI usage.
- Track newly introduced or emerging AI tools.
- Decide whether new applications require review or governance.

Click **View Shadow AI Inventory** to see the full list of discovered AI applications.

## Topics Popularity

The Topics Popularity widget categorizes AI interactions by topic, such as Code and Computing or Business Management. This widget helps you understand how AI is being used across the organization and identify usage in sensitive or regulated topic areas.

Click **View AI Interactions** to drill down into detailed interaction data.

## Top Interactions Flow

The Top Interactions Flow widget visualizes how AI interactions flow from specific applications to outcomes. This visualization helps you:

- Compare risk levels across AI applications.
- Identify which tools generate the highest number of violations.
- Quickly spot high-risk applications that may require tighter controls.
