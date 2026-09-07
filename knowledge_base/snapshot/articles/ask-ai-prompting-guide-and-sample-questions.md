---
title: "Ask AI - Prompting Guide and Sample Questions"
slug: "ask-ai-prompting-guide-and-sample-questions"
updated: 2026-06-30T15:06:15Z
published: 2026-06-30T15:06:15Z
canonical: "knowledge.catonetworks.com/ask-ai-prompting-guide-and-sample-questions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ask AI - Prompting Guide and Sample Questions

For more information, see [What is Cato's Ask AI Agent](/v1/docs/what-is-cato-s-ask-ai-agent)

## How to Write Better Prompts

The more specific your prompt is, the better the result is likely to be. Include the details you already know, such as the site, user group, user, application, policy, action, and time range. If you want the answer in a specific format, ask for it directly, such as a table, trend, timeline, distribution, or executive summary.

If no results are found, remove filters to widen the scope or review **Query Details** to confirm that Ask AI understood the entities, filters, and time range correctly.

## Example prompts

### Sites, Users, and Topology

#### Account Snapshot and Connectivity Status

- `Which country/PoP location currently has the most connected remote users?`
- `Which country/PoP/ISP combination has the most degraded sites right now?`
- `Which sites are currently in degraded state?`
- `Provide a list of connected sites grouped by site type (Socket/IPsec/vSocket)`
- `Which sites currently have only one WAN link up?`

#### Remote Users and Client Health

- `How many users are currently connected to Cato on my account?`
- `List all remote users that are currently online and the PoP they are connected through`
- `Which remote users are running older Cato Client versions?`
- `Group connected remote users by operating system and Cato Client version`
- `Which users have poor Wi-Fi signal and degraded connectivity quality right now?`

#### Site Infrastructure Operations

- `Were there any HA role changes or PoP connection changes for site {site_name} in the last {duration_value} {duration_unit}?`
- `Show infrastructure stability events, including tunnel reconnects, role changes, and PoP changes, from the last {duration_value} {duration_unit}`
- `Which sites had repeated disconnect and reconnect events in the last {duration_value} {duration_unit}?`

### Network Analytics and Application Performance

#### Connectivity Metrics and Quality

- `Which sites had average packet loss above {packet_loss_threshold}% in the last {duration_value} {duration_unit}?`
- `Show RTT and packet loss trends for all sites over the last {duration_value} {duration_unit}`
- `List the top {num_count} site links with the worst upstream packet loss in the last {duration_value} {duration_unit}`
- `Which interface on site {site_name_or_id} had the highest downstream packet loss in the last {duration_value} {duration_unit}?`
- `Show ISP-side latency and packet loss for all sites in the last {duration_value} {duration_unit}`
- `Show me traffic trends over the past 48 hours`
- `Which sites had high packet loss last week?`
- `What are the worst-performing ISPs in this account? Please include their IPs and average packet loss`

#### Application Experience and Usage

- `Show performance metrics for {application_name} over the last {duration_value} {duration_unit}, including latency, throughput, and experience score`
- `Which applications consumed the most bandwidth across my sites in the last {duration_value} {duration_unit}?`
- `What are the top {num_count} applications with the lowest average experience score in the last {duration_value} {duration_unit}?`
- `Show hourly traffic volume trends for all applications over the last {duration_value} {duration_unit}`
- `Which users had poor Zoom or Microsoft Teams experience in the last {duration_value} {duration_unit}?`
- `Which apps in use are considered high risk?`
- `Who used the most bandwidth last week?`
- `Which sites used the most bandwidth yesterday?`

#### Visualization and Chart Requests

Ask AI can help with visual answers for measurable data. To get the best outcome, ask it to **Visualize**, **Show trends**, or **Show distribution** when your prompt already includes measurable data, grouping, or a time range.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(29).png)

- `Create a pie chart of sites by country`
- `Show a time-series chart of packet loss for top degraded sites over the last {duration_value} {duration_unit}`
- `Create a pie chart of connected remote users by operating system`
- `Show a daily time-series chart of total bandwidth for all sites over the past {duration_value} {duration_unit}`

### Security Investigation and Firewall Analysis

#### Security Events and Threat Hunting

- `Show all high-risk blocked IPS events from the last {duration_value} {duration_unit}`
- `Find Anti-Malware events where verdict is not clean in the last {duration_value} {duration_unit}`
- `Show me security events with destination IP between {start_ip} and {end_ip}`
- `Which users and sites are most impacted by critical security events in the last {duration_value} {duration_unit}?`
- `Summarize top security threat subtypes and their trend over the last {duration_value} {duration_unit}`

#### XOps Stories Investigation

- `Summarize XOps Story ID {xops_story_id} in no more than 10 sentences`
- `Show the full XOps Story timeline for incident ID {incident_id} and identify impacted users and sites`
- `Get the latest critical XOps Story and explain what happened and recommended response steps`

#### Firewall Events

- `Show WAN Firewall block events from the last {duration_value} {duration_unit}`
- `Find LAN Firewall events for traffic from {source_site} to {destination_site} in the last {duration_value} {duration_unit}`
- `Show Internet Firewall block events for {application_name} in the last {duration_value} {duration_unit}`
- `Which firewall policy rules generated the highest blocked counts in the last {duration_value} {duration_unit}?`
- `What are the top 5 enabled blocking Internet Firewall rules with the most hits?`

### Policy, Identity, and Admin Operations

#### **Policy Management**

- `[Action prompt - requires user approval] Create a new Internet Firewall rule to {action} {application_name_or_category} for {user_or_group_scope}, place it in the recommended position, and confirm the proposed change before applying it`
- `Review my current Internet Firewall policy and propose a new rule to {action} {application_name_or_category} for {user_or_group_scope}`
- `Before creating the rule, analyze existing Internet Firewall rules and recommend the best position, including above or below which rule, to preserve intent`
- `Check for overlapping or conflicting rules, then suggest the safest insertion point for a new rule targeting {target_scope}`
- `Propose the exact Internet Firewall rule definition, including sources, destinations, applications or services, and action, and explain why this position is optimal`
- `Show if there are existing objects or groups I should reuse before creating a new Internet Firewall rule`

#### **Policy Change Validation Checklist**

- `Give me a validation checklist to run after adding this Internet Firewall rule, including expected allow and block patterns`
- `Create a pre-change and post-change verification checklist for this policy update`
- `Which events, metrics, and logs should I monitor in the first {duration_value} {duration_unit} after rollout?`
- `Provide a rollback checklist in case this rule causes unexpected blocking`
- `Build a short acceptance checklist for Security and IT Ops sign-off on this rule change`

#### **Internet Firewall Policy Information and Operations**

- `Show Internet Firewall rules that apply to {application_name_or_object}`
- `Look at Internet Firewall policy and show the top {num_count} rules by hit count for group {group_name}`
- `When was the Internet Firewall rule that applies to {ip_address_or_object} last updated?`
- `Show overlapping Internet Firewall rules that may conflict with a new rule for {target_scope}`
- `Are there any Internet Firewall rules currently inactive or disabled?`
- `Are there rules preventing users from accessing social media sites?`
- `Who was the last person to update the Internet Firewall rules, and when?`
- `Show me all Internet Firewall rules that are currently inactive or disabled`
- `Do we have rules blocking inbound connections from the Internet?`
- `Are there Internet Firewall rules that restrict access to SaaS applications?`
- `How many allow and block rules are there in the Internet Firewall policy?`

#### Questions for TLS Inspection Policy

- `Which sites or users have TLS Inspection bypassed?`
- `Show me TLS Inspection rules with the Inspect action`
- `What is the minimum TLS version and cipher suite configured in the policy?`

#### Application Control Policy

- `Which applications are blocked in the Application Control policy?`
- `Show me DLP rules for file uploads/downloads`
- `What SaaS applications have tenant restrictions configured?`
- `Are there rules restricting access to high-risk applications?`

#### **Policy and Where-Used**

- `Where is network object {object_name} used across policies?`
- `In which firewall rules is application {application_name} referenced?`
- `Show all policies that reference user group {group_name}`
- `Show revision history for policy type {policy_type}`
- `In which policies is Japan used?`
- `In which policies is hq_site used?`
- `Show all policies that reference example_group`
- `Where is Salesforce used across policies?`
- `Which policies reference 192.168.0.0/24`

For more ideas about using Ask AI to assess the impact of a change or review existing policy usage, see the [Ask AI Global Search feature](/v1/docs/ask-ai-global-search-for-policy-and-entity-references-ea).

  

#### **Identity, Audit, and Admin Changes**

- `What user groups does user {user_email} belong to?`
- `Show the admin audit log for the last {duration_value} {duration_unit} and who made configuration changes`
- `List all policy changes made by admin {admin_email} in the last {duration_value} {duration_unit}`
- `Which administrators made the most configuration changes in the last {duration_value} {duration_unit}?`

#### **Remote User Session Management**

- `[Action prompt - requires user approval] Revoke all active sessions for user {user_email} and confirm completion`
- `[Action prompt - requires user approval] Revoke all active sessions for users in group {group_name}`
- `[Action prompt - requires user approval] For user {user_email}, show active sessions first, then revoke the current active sessions`
- `[Action prompt - requires user approval] Reset the risk score for user {user_email} and show the updated user risk state`
- `Which users currently have elevated risk score, and for which users should I reset risk score now?`

### Posture, Compliance, and Data Protection

#### AI Security

- `Show AI Security security events where sensitive data was detected in the last {duration_value} {duration_unit}`
- `Which users triggered the most AI Security policy violations in the last {duration_value} {duration_unit}?`
- `Show blocked AI app interactions, including suspected prompt-injection related detections, in the last {duration_value} {duration_unit}`
- `Which unsanctioned AI applications are being used in my account in the last {duration_value} {duration_unit}?`

#### Posture

- `What should I fix today to improve my security posture?`
- `Which posture checks are currently failing for our account?`
- `Show all posture checks that passed in the last posture assessment`
- `Which posture checks have the highest risk impact if left unresolved?`
- `Are there any best practice checks that are disabled?`
- `What is the best practices score for network security?`

#### Compliance Frameworks

- `Which compliance frameworks are currently enabled on my account?`
- `Show active compliance frameworks, for example NIST, CIS, or ISO 27001, and current status`
- `Which failed posture checks map to framework {framework_name} controls?`

#### Data Protection and DLP

- `Show all DLP events from the last {duration_value} {duration_unit}`
- `Find Data Protection violations where sensitive files were uploaded to cloud storage in the last {duration_value} {duration_unit}`
- `Show DLP events where credit card data was detected in outbound traffic`
- `Which users and applications triggered the highest number of high-severity DLP events in the last {duration_value} {duration_unit}?`

### Hardware, Sockets, and Device Health

#### Socket Inventory and Lifecycle

- `How many Sockets do I have by operational status, including ORDERED, SHIPPED, DELIVERED, INSTALLED, and CONNECTED?`
- `How many Sockets are currently in CONNECTED status?`
- `Which Sockets are not yet connected, and to which sites are they assigned?`
- `Can I assign Socket {socket_id} to site {site_name_or_id}?`
- `When is Socket &lt;serial number&gt; scheduled to arrive?`
- `How many Sockets are pending shipping?`

#### Hardware Utilization and Root Cause Analysis

- `Show CPU utilization time-series for all Sockets at site {site_name} over the last {duration_value} {duration_unit}`
- `Show memory utilization trends for all Sockets over the last {duration_value} {duration_unit}`
- `Which devices have average memory utilization above {memory_threshold}% in the last {duration_value} {duration_unit}?`
- `I am investigating a Socket CPU spike at site {site_name}. Show likely root-cause traffic patterns over the last {duration_value} {duration_unit}`

#### Multi-Domain Correlation Prompts

- `Show all sites with high packet loss that also had security events in the last {duration_value} {duration_unit}, including threat subtype and event count`
- `Which sites in {region} have high bandwidth consumption and poor health score, and what PoP are they connected to?`
- `Find users with poor hardware experience score who are also using high-risk unsanctioned apps`
- `Show remote users with poor Wi-Fi signal and high application latency for Zoom or Microsoft Teams, including their PoP and device metrics`

#### Automation and GraphQL Scripting

Use these prompts when you want Ask AI to help you build automation with Cato APIs and ready-to-run scripts.

- `Using Cato GraphQL, show me the exact query to pull connected sites, PoP location, and WAN health for account {account_id}`
- `Generate a Python script that authenticates to Cato GraphQL and exports top degraded sites to CSV for the last {duration_value} {duration_unit}`
- `Generate a Bash script with curl to call Cato GraphQL and list currently connected SDP users with their PoP`
- `Create a reusable automation script that runs daily, fetches posture check failures, and writes a summary report file`
- `Provide a GraphQL mutation example and script flow to update Internet Firewall rule order safely, including validation steps`
- `Build a script that correlates high packet loss sites with security event counts and outputs a ranked remediation list`

## Review Your Prompt Before You Send It

Use this checklist before sending a prompt:

- Did I include the specific site, group, user, application, policy, or CMA task I care about
- Did I set a clear time range, if relevant
- Did I ask for the format I want
- If this is a comparison, did I clearly define both sides
- If I want a visual answer, did I include measurable data, grouping, or a time trend
- If I am excluding a maintenance window, did I define the exact time range

## FAQ

### Are Ask AI capabilities limited by CMA permissions?

Yes. Ask AI only provides access to data that aligns with the user’s existing CMA RBAC permissions.

### The first answer is too narrow, or no results were found. What should I do?

First, review **Query Details** to confirm that Ask AI understood the entities, filters, and time range correctly. If the prompt was interpreted correctly and still returns no results, remove some filters or widen the scope.

In this example, you can expand **Query Details** to see how Ask AI interpreted “recent”:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(31).png)

### Can Ask AI perform actions?

Ask AI can automate troubleshooting and provide actionable insights, but it always requires human interaction and confirmation and is not allowed to make changes independently.
