---
title: "Reviewing Posture Checks for Your Account"
slug: "reviewing-posture-checks-for-your-account"
updated: 2026-07-05T13:40:29Z
published: 2026-07-05T13:40:29Z
canonical: "knowledge.catonetworks.com/reviewing-posture-checks-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reviewing Posture Checks for Your Account

This article explains how to use the Posture page to assess policies and settings in your account and evaluate how they comply with Cato’s recommendations.

## Overview

To ensure your network is optimized, stable, and secure, Cato provides recommended Posture checks and AI-based insights for how to configure policies and features and runs checks to review your account configurations to assess the level of compliance. Posture checks are mapped to leading compliance frameworks, helping you understand how Cato configurations support audit and regulatory requirements. This enables you to easily identify gaps and prioritize improvements based on compliance impact.

The **Posture Check Catalog** lists all available Posture Checks. You can customize the catalog to control which checks are included in the assessment for your account. The **Posture** page provides an overview of your account’s compliance based on the enabled checks.

Some policies have a Posture Recommendation Wizard to simplify the process of creating or updating policies. For more information, see [Understanding Cato Autonomous Policies](/v1/docs/understanding-cato-autonomous-policies) .

Checks are performed automatically every 24 hours. However, some of the checks can be immediately reperformed by clicking the refresh button, and others are reperformed when a policy is updated. To know when the check was last performed, see the the Check Details.

You can view posture-related events, including score changes and new checks from the Events Page. For more information, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

## Customizing Checks for Your Account

If individual checks are not relevant for your environment, you can enable/disable them for your account and exclude them from the **Account Score** (the overall account rating for compliance). The **Posture Check Catalog** lets you enable and disable individual checks as well as categories of checks, for example, disable all checks in the **Application Control** category. This helps you reduce unnecessary noise to focus on relevant items that need your attention, and adjusts the Account Score to only reflect relevant items.

![Best_Practics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34309536016925(1).png)

### 

> [!NOTE]
> Note:
> 
> You must have an Editor role or higher to customize Posture Checks. For more information, see [Managing Admin Roles Using RBAC.](/v1/docs/managing-admin-roles-using-rbac)

**To customize which Posture Checks are run:**

1. From the navigation menu, go to **Resources > Posture Check Catalog**.
2. Use the radio buttons in the **Enable** column to define which categories or individual checks are enabled or disabled. Use the arrows to the left of each category to expand the category and enable/disable individual items.
3. Click **Save**.

## Reviewing the Compliance Level of your Account

The **Posture** pages provides an overview of the compliance posture of your account. It is split into overview widgets and the Posture Check table. You can also view details of each check and mute or dismiss it.

**To view the Posture page:**

- From the navigation menu, select **Home > Posture**.

### Reviewing Your Posture with Ask AI

You can use Ask AI to review your account posture, investigate score changes, and understand how to improve compliance. Ask AI lets you ask natural-language questions about your account data, including current and historical data, helping you analyze posture trends without manually reviewing multiple pages or filters. For more information on Ask AI, see [What is Cato’s Ask AI Agent](/v1/docs/what-is-cato-s-ask-ai-agent).

For example, you can ask Ask AI questions such as:

- Why did my score change recently?
- What changed between April 1 and May 1?
- What should I fix today to improve my posture?
- How do I best fix this check?
- What happened recently to this check, and who made the change?
- Show me all disabled or muted posture checks.

### Understanding the Overview Widgets

The overview widgets provide a high level overview of your level of adherence to the Cato Posture best practices.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144369343005(1).png)

The overview widgets are:

- **Account Score:** The current overall account rating for compliance with Cato posture, as well as how many checks were passed and failed. It reflects the overall health and security posture of your deployment, based on weighted checks that consider both importance and severity. This widget also benchmarks your account against companies in your industry. If industry data is unavailable, your score is compared across all industries. You can also provide feedback, such as recommending a posture check, requesting enhancements, or correcting your industry.
- **Score Breakdown:** A breakdown of the current score by area. Each slice of the pie chart shows the percentage of passed checks and the total number of checks in that area. You can use the dropdown or click an area to drill down and view a more granular view of each area.
- **Score Over Time:** Shows how your score has changed over time. You can view the overall account score or focus on specific areas. Use the checkboxes to select which scores to display and apply the time range filter to refine the view.

### Understanding the Posture Checks Table

The Posture Checks table displays information about every Posture Check. It is split into three tabs:

- **All**: Displays a combined view of your Account Posture Checks and available SaaS Security checks
- **Account Posture:** Displays the posture checks for your Cato Account configurations
- **SaaS Security:** Displays the posture checks for the configurations in connected SaaS applications. For more information, see [Reviewing the Security Posture of Your SaaS Applications (SSPM).](/v1/docs/understanding-the-security-posture-of-your-saas-applications)

You can define how they are grouped, filtered, and sorted to help you focus on the most relevant areas for your environment. You can filter the table by use case or compliance framework.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35646641712029(1).png)

#### Explanation of the Posture Fields

- **Name**: The name of the individual check, category, or CMA area.
- **Area:** The area of the CMA, such as Security or Network.
- **Category:** Each are of the CMA is broken down further into categories to provide a more granular way to group individual checks.
- **Label:** This field displays either a:

**Note**: Cato’s best practices are designed to assist organizations in their compliance efforts. They are provided for general guidance only and should not be relied upon as legal advice
  - Mapping to compliance standards to identify how Cato is playing a role in meeting your compliance assessments. Supported compliance standards are ISO 27001:2022, NIST SP 800-53 Rev. 5, and GDPR
  - Posture Check for specific use cases to enhance your security posture, eliminating the need to design policies from scratch
- **Findings:** Relevant entities related to any check failures. For example, rule names or Site IDs.
- **Status** - Displays if your account complies with an individual check. Possible values are **Passed** and **Failed**.
- **Severity** - The severity of the check, with possible values of **High**, **Medium**, **Low**, and **Informational**. The severity impacts the weight given to the check in calculating the overall Cato Score, with higher severity checks counting more. Checks with Informational severity do not impact the Cato Score at all.

### Viewing the Posture Check Details

You can view additional details of each check by clicking the check to open the **Posture Check Review** panel. This contains the following information about each check:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144369343389(1).png)

- **Details** - The status, description, recommended action, relevant labels, and severity.
- **Industry Comparison** - A comparison of the pass rate of other companies in your industry.
- **Comments** - A history of changes to the status of the check. You can also add a comment.
- **Link to the policy** - A link to the relevant page to update configurations and ensure compliance.
- **Findings tab** - A list of relevant entities related to any check failures. For example, rule names or Site IDs.
- **Guide me** - Uses Ask AI to provide you with step-by-step instructions for implementing the check. For more information, see [Cato's Ask AI Assistant](/v1/docs/what-is-cato-s-ask-ai-agent).
- **Review & Resolve button** - For checks that can be resolved using the Posture Recommendation Wizard, clicking this button navigates directly to the policy page with the Posture Recommendation Wizard open. If a check cannot be resolved with the Posture Recommendation Wizard, this button is disabled.

### Muting / Excluding a Posture Check or Finding

If there is a Posture check or a specific finding, such as a particular site, that you do not want included in your [account score](/docs/reviewing-posture-checks-for-your-account#UUID-7b7c54f9-7423-27fa-d798-affdb139b12f_section-id235376651072351), you can mute, disable, or dismiss it. These actions can be applied either temporarily or permanently.

#### Muting a Posture Check

You can mute a Posture Check for 30 days so that during this period it is not included in the account score.

![Mute.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643825874461(1).png)

**To mute a Posture Check:**

1. From the navigation menu, select **Home > Posture**.
2. Click on the check you want to mute.

The **Posture Check Review** panel opens.
3. Click on the three dots.
4. Click **Mute for 30 days**,

#### Excluding a Posture Check

If a Posture Check is not relevant for your account, for example you do not use Cato DLP, you can disable it so that it is not included in the account score.

**To exclude a Posture Check:**

1. From the navigation menu, select **Home > Posture**.
2. Click on the check you want to exclude.

The **Posture Check Review** panel opens.
3. Click on the three dots.
4. Click **Edit Policy**.

The **Posture Checl Catalog** is displayed.
5. Disable the check you want to exclude.
6. Click **Save**.

#### Muting / Excluding a Specific Finding

If there is a specific finding that you do not want to be included in the account score, you can mute it for 30 days or dismiss it.

**Note**:

- To restore a finding, on the **Posture Catalog**, disable the rule, save the changes and re-enable the rule
- In some checks the embedded remediation wizard suggests multiple findings in one rule (such as block risky categories). If you want to pass the check but exclude one of the findings, remove it from the list in the rule, apply the rule, and then return to the Posture page and dismiss the last finding. This ensures the check is passed.

![Finding.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643818625949(1).png)

**To mute or exclude a specific Finding:**

1. From the navigation menu, select **Home > Posture**.
2. Click on the check with the Findings you want to mute or exclude.

The **Posture Check Review** panel opens.
3. On the **Findings** tab, click on the three dots of the finding you want to mute or exclude.
4. To mute the Finding, click **Mute for 30 days** to exclude it click **Dismiss**.

## Known Limitations

- For TLS Inspection > Inspect Recommended Destination checks, you need to create a separate TLS Inspection rule for each destination
