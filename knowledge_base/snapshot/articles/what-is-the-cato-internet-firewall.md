---
title: "What is the Cato Internet Firewall?"
slug: "what-is-the-cato-internet-firewall"
updated: 2026-08-18T06:41:17Z
published: 2026-08-18T06:41:17Z
canonical: "knowledge.catonetworks.com/what-is-the-cato-internet-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Cato Internet Firewall?

This article provides background information about the Internet firewall for your account.

For more information about configuring the Internet firewall, see [Managing the Internet Firewall Policy](/v1/docs/managing-the-internet-firewall-policy).

## Overview

The Internet firewall inspects traffic between the WAN and the Internet and lets you create rules to control this traffic. Similar to the WAN firewall, the Internet firewall uses an ordered rulebase, starting from the first rule, connections are inspected according to each rule. The Internet firewall uses a blacklist approach. This means that there is an implicit ANY - ANY rule to allow any traffic and connections that are not explicitly blocked in the rulebase. The Internet firewall also includes full layer 7 functionality with User Awareness, and you can create rules for specific applications. For example, you can use the Internet firewall to:

- Block specific websites, such as Facebook or LinkedIn
- Block categories of inappropriate websites, such as Guns, Alcohol, and Gambling
- Allow only the IT department to use remote administration applications (SaaS and IaaS)

### Understanding Autonomous Firewall Insights

![Auto_FW.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26957301991709(1).png)

The Autonomous Firewall Insights are a list of [best practice posture checks](/v1/docs/reviewing-posture-checks-for-your-account) that evaluate your Internet Firewall policy and show how they comply with Cato’s recommendations. Following these recommendations optimizes your firewall configurations and improves security posture.

There are two types of insights:

- Star icon (powered by AI): Enabled rules in your Internet Firewall policy are automatically analyzed by Artificial Intelligence (AI) to detect issues, for example, rules that can be discarded or modified, such as:
  - **Expired Rule** or **Rule with Future Expiration Date:** Rules created to address a specific need and have a desirable cutoff date that has already passed or that has not yet been reached or cannot be proven/evaluated.
  - **Temporary Rule:** Introduced as a short-term solution to address an immediate need. These rules are mostly created to function temporarily while a proper or permanent solution is being deployed or developed.
  - **Testing Rule:** Rules explicitly created for validating, debugging, or experimenting with a specific feature or scenario.
  - **Unused Rule:** Identifies firewall rules with an Allow action that have not generated any events in the past 60 days
  - **Contradicting Rules Check**: Identifies firewall rules with identical predicates but different actions, which can create conflicts that prevent lower-priority rules from being applied
- **Configuration-based:** The configurations and settings in your Internet Firewall policy are checked to ensure they follow best practices.

### Working with the Internet Firewall Configuration Wizard

The Internet Firewall Configuration Wizard autonomously reviews your policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management. For more information, see [Using the Configuration Wizard](/v1/docs/using-the-configuration-wizard).

### Anti-Spoofing Protections in the Cato Firewall

One of the basic functionalities of an NGFW is to protect against anti-spoofing attacks. The security engines in the Cato Cloud implicitly drop any connection where the source IP is outside the scope of the configured entity (such as site, network range, device, or user). This blocks anti-spoofing attacks and prevents violations of the configured logical topology.

### Working with Ordered Rules

The Internet firewall inspects connections sequentially and checks to see if the connection matches a rule. The final rule in the rulebase is an implicit ANY - ANY allow rule - so if a connection does not match a rule, then it is allowed by the final implicit rule.

Rules that are at the top of the rulebase have a higher priority because they are applied to connections before the rules lower down in the rulebase. If a connection matches on rule #3, the action is applied to the connection, and the firewall stops inspecting it. The firewall does not continue to apply rules #4 and below to the connection.

### Working with Multiple Objects in a Single Rule

When there is a rule with objects in multiple columns, such as an **application** and a **service**, then there is an AND relationship between them. For example, if there is a rule that blocks the Netflix application for port 443, then the traffic is blocked when it matches both the application and the port.

For rules that use multiple objects in a single column, such as more than one **application**, there is an OR relationship between them. For example, if there is a rule that blocks access to the Netflix, iTunes, and YouTube applications, then the traffic is blocked when it matches any of the applications.

> [!NOTE]
> Note:
> 
> Each rule can have a maximum of 64 conditions with an AND relationship between them, and a rule's exceptions are included in the rule limit. For example, if there is a rule with two AND conditions (such as a **source** and a **service**), and the rule has 25 exceptions with 3 AND conditions each (such as a **source**, an **app**, and a **service**), then the rule has 77 conditions. This exceeds the supported limit of 64 conditions and the rule might not function properly. However, you can assign more than 64 objects within the same column of a rule, since there is an OR relationship between them. For example, you can assign more than 64 apps in one rule.

### Understanding the Hit Count

The hit count helps you identify unused rules that can be removed from a policy and optimize rule configuration to better match the required traffic scope. The hit count for a rule is based on the number of events generated by the rule. If a rule does not generate events, the hit count is zero.

The hit count contains two numbers:

- The approximate number of events generated by each rule in the policy
- How often the rule is hit relative to other rules (ranked by percentile)

These values are updated once every 24 hours and are based on the past 14 days of traffic.

You can quickly identify the rules with the highest and lowest hit count, based on the color of the status bar. This color reflects how often the rule is hit relative to other rules:

- Blue: 0 - 24th percentile
- Green: 25th - 49th percentile
- Orange: 50th - 74th percentile
- Red: 75th -100th percentile

#### Resetting and Refreshing the Hit Counter

![Reset.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33141045582493(1).png)

The hit count values are updated automatically every 24 hours and are based on the past 14 days of traffic. From the three dots at the end of each rule, you can reset or refresh the hit count for up-to-date visibility. This lets you accurately measure rule effectiveness and immediately validate rule activity.

- Resetting the hit counter for a specific firewall rule returns the hit count to 0
- Refreshing the hit counter updates the hit count on demand for all firewall rules

### Policy Revisions and Concurrent Editing by Multiple Admins

The Internet Firewall lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Configuring the Time Settings for a Rule

You can configure the time settings for a rule so that it is enabled or disabled at a defined date and time. In the **Time** drop-down menu, you can configure the **Daily Schedule** and/or the **Active Period**.

You can configure both of these options so that, for example, the rule is active on weekdays during the month of May 2025. Alternatively, you can configure each option independently to meet your requirements.

![Time.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28648007298589(1).png)

#### Understanding the Daily Schedule

The **Daily Schedule** defines the schedule for when the rule is active. If a schedule is configured for a rule, a clock symbol is displayed in the **Action** column.

The options for the **Daily Schedule** are:

- **No time constraint:** There is no schedule for the rule. This is the default behavior of the rules.
- **Limit to working hours:** The rule is active only during the working hours configured in the Cato Management Application. For more about working hours, see [Defining Default Working Hours for the Account](/v1/docs/defining-default-working-hours-for-the-account).
- **Custom:** Select the time of the day and the days of the week when the rule is active. Uncheck the **Recurring** option, and select the **Date** and time setting for the rule.
  - **Recurring:** The time setting will be applied more than once, for example, every Tuesday from 9:00 am to 5:00 pm.

#### Understanding the Active Period

The **Active Period** defines the date and time period the rule is active in UTC. If the **Effective From** field is not selected, the rule is active immediately after the rule is saved and published.

On the rule table, if an **Active Period** is defined, an hourglass symbol is displayed in the **Action** column. The color of the symbol reflects the status:

- **Black**: The rule is not active and will become active in the future
- **Green**: The rule is active
- **Red**: The rule has expired

### Traffic Blocked Related to the MSA

The Cato Networks Master Service Agreement (MSA) defines traffic that is potentially illegal or malicious that is automatically blocked. There is a hidden implicit rule at the top of the Internet firewall rulebase that blocks these connections.

For more about the MSA, see [Cato Networks MSA](https://www.catonetworks.com/msa/).

## Understanding the Settings for Internet Firewall Rules

This section explains the fields and settings for the rules in the Internet firewall rule base. A thorough understanding of the Internet firewall helps to successfully manage access control for the corporate network.

### Rule Actions

The following table describes the actions that each firewall rule can apply to the network traffic. For actions that generate events, you can show event logs in **Home > Events**.

| Item | Description |
| --- | --- |
| Allow | Firewall allows matching traffic. |
| Block | Firewall blocks matching traffic. |
| Prompt | Firewall redirects matching traffic to a web page with a message. The user is prompted to decide whether or not to continue. You can customize the prompt web page, see [Customizing the Warning / Block Page](/v1/docs/customizing-the-warning-block-page-branding). The Cato prompt page is an HTML page that uses JavaScript and session cookies to manage user consent. These cookies are domain-specific, temporary, and typically deleted when the browser is closed. Cato currently uses three cookie name prefixes, (`tls_cert_err`, `fw_wan`, and `fw_inet`). Cookie handling and session persistence depend on user settings and behaviour, the browser, and operating system. To review events for when a user chooses to proceed after a prompt page, filter the [Events](/v1/docs/analyzing-events-in-your-network) page to show events with the **Prompt Action** field set to the value **Proceed**. |
| Remote Browsing (RBI) | Matching traffic is delivered by [RBI](/v1/docs/securing-browsing-sessions-through-rbi). |
| Captive Portal | Matching traffic is directed to the [captive portal](/v1/docs/configuring-the-cato-captive-portal). |

### Internet Firewall Rulebase Columns

For a description of the different rulebase columns and Source, App, and Category items for rules, see [What is the Cato WAN Firewall?](/v1/docs/what-is-the-cato-wan-firewall) and [Reference for Rule Objects](/v1/docs/reference-for-rule-objects). Unlike the WAN firewall, the **Destination** for the Internet firewall is always the Internet. When there are multiple columns configured for a rule, then there is an AND relationship between them.

### Setting the Rule Order

Rule order is defined by setting a rule’s position relative to other rules. For example, set a rule to follow a specific rule, or to be first in a section.

These are the options for defining the rule order:

- **Before Rule** - The rule is positioned immediately before the selected rule
- **After Rule** - The rule is positioned immediately after the selected rule
- **First in Section** - The rule is positioned first in the selected section
- **Last in Section** - The rule is positioned last in the selected section
- **First** - The rule is positioned at the top of the rulebase
- **Last** - The rule is positioned at the bottom of the rulebase
