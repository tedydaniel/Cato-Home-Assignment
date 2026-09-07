---
title: "Product Updates - Aug. 24, 2026"
slug: "product-updates-aug-24-2026"
updated: 2026-08-24T04:39:13Z
published: 2026-08-24T04:39:13Z
canonical: "knowledge.catonetworks.com/product-updates-aug-24-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - Aug. 24, 2026

## New Features & Enhancements

- **Cato Schema Explorer for Event Fields and Traffic Flow Data:** A new [interactive tool](https://knowledge.catonetworks.com/docs/cato-event-schema) in the Knowledge Base maps the Cato API schema to its fields, including event types, subtypes, and flows. You can find all fields and their possible values and build integrations and agents more easily.
  - Helps SIEM parsers and other integrations use precise field-level mapping
- **Support for SecureAuth SSO:** We added SecureAuth as an [SSO provider](https://knowledge.catonetworks.com/docs/configuring-secureauth-sso-for-your-account) for authenticating remote users (supported in the Client, Browser Extension, and Enterprise Browser).
- **Enhanced AI Security Safety & Security Detectors**: Reduce false positives by approximately 10x while maintaining strong protection against Jailbreak and Prompt Injection, Obfuscation Attacks, and Harmful or Unsafe Content.
  - Applies when **Confidence Level** is set to **High** in the Engine Profile
  - Outpost support is planned by the end of the year
  - AI Security for Users or AI Security for Apps license required
- **AI Security Coding Agent Policy Enforcement Includes Claude Cowork:** We extended AI Security to include visibility and enforcement for Claude Cowork for [Coding Agent Policy rules](https://knowledge.catonetworks.com/docs/ai-security-for-agents-configuring-the-coding-agents-policy).
  - AI Security for Users license required (show me the [Coding Agent Policy page](https://externallink.cc.catonetworks.com/#/account/me/agentsAgentPolicies))
- **Skill Enforcement for Claude Code**: Control Claude Code agent activity by enforcing AI Security policy rules based on the skills used in each session.
  - Apply rules for specific detected skills
  - Investigate detected skills from the **Local Agents** page
  - AI Security for Users license required
- **AI Risk Details in the App Catalog**: Assess how applications use AI and handle data separately from the overall Security Risk score.
  - [View AI Risk](https://knowledge.catonetworks.com/docs/understanding-the-fields-in-the-app-catalog?highlight=app%20cat) information for applications with AI capabilities, including policy type, description, and reference links
  - Review AI scope and data usage details in the new **AI Security** section (show me the [App Catalog page](https://externallink.cc.catonetworks.com/#/account/me/appsCatalog))
- **Delegate TLS Inspection Policy Management with Granular RBAC:** [Delegate ownership](https://knowledge.catonetworks.com/docs/configuring-rbac-for-policy-management) of specific [TLS Inpsection policy](https://knowledge.catonetworks.com/docs/configuring-tls-inspection-policy-for-the-account) sections to dedicated teams while maintaining centralized governance of the overall policy.
  - Assign view or edit permissions for specific sub-policies
  - Distribute operational ownership across regional or functional teams
- **Enhanced Admin Experience for Proxy Configuration Policies:** Easily manage complex rulebases with more speed and flexibility for the [Proxy Configuration](https://support.catonetworks.com/hc/en-us/articles/16231563119901-Centralized-Management-of-Proxy-Configuration-Proxy-Configuration-Policy) policy. Enhancements include:
  - **Concurrent editing** – Multiple admins can [modify policies](https://support.catonetworks.com/hc/en-us/articles/21583885497245-Working-with-Policy-Revisions) in parallel without conflicts
  - **Improved performance** – Policy pages are more responsive, especially for rulebases with a large number of rules
  - **GraphQL API support** – Public API support will be available soon
- **Updated Cato Terraform to v0.0.96:** We uploaded [version 0.0.96](https://registry.terraform.io/providers/catonetworks/cato/latest/docs) of the Terraform module with these enhancements:
  - Extended the Internet, WAN, LAN Firewall, and Network Rule policies to manage sub-policies and rule order
  - Added `cato_lf_sub_policy` and `cato_bulk_lf_move_rule` resources

### PoP Announcements

- New ranges are now available for these PoP locations:
  - **Shanghai, CN:**
    - 116.238.242.0/26
    - 211.95.36.128/26
  - **Shenzhen, CN:**
    - 112.95.31.0/26
    - 183.36.38.64/26

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://knowledge.catonetworks.com/docs/understanding-rollout-to-the-cato-cloud). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
