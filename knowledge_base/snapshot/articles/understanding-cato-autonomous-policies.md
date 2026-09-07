---
title: "Understanding Cato Autonomous Policies"
slug: "understanding-cato-autonomous-policies"
updated: 2026-08-27T15:08:43Z
published: 2026-08-27T15:08:43Z
canonical: "knowledge.catonetworks.com/understanding-cato-autonomous-policies"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Cato Autonomous Policies

## Overview

Autonomous Policies use an AI agent to help you optimize your policies and simplify day-to-day policy management. The agent continuously analyzes real network behavior and highlights where policies can be tightened, cleaned up, or refined to better match actual usage. This helps you strengthen your account posture and reduce the manual effort required to maintain policies. For example, the agent can identify an unused rule with an Allow action and recommend deleting it.

## Why Use AI in Policies?

As networks become more dynamic with cloud adoption, remote access, and constantly changing applications, manual policy maintenance becomes inefficient and prone to errors. An AI agent helps keep policies accurate, streamlined, and aligned with real usage without requiring continuous manual review. By learning from traffic flows across the Cato Cloud, the agent provides insights based on broad behavioral baselines and not only on account-specific data. ​ With Cato Autonomous Policy, the AI agent analyzes rule behavior at scale and provides recommendations based on best practices and actual traffic patterns. This delivers several key benefits:

- **Stronger Account Posture**: Rules become more precise and less permissive, reducing exposure to unnecessary risk
- **Fewer Configuration Errors**: Automated analysis highlights misconfigurations early, preventing them from propagating into production
- **Continuous Policy Hygiene**: Unused or outdated rules are automatically identified, keeping the rulebase clean and efficient
- **Faster and Easier Updates**: Admins can act on AI-driven insights instead of manually reviewing large rule sets
- **Reduced Operational Overhead**: Enabling the policy and ongoing optimization requires minimal effort, freeing teams to focus on higher-value tasks

## Understanding Autonomous Policies

Autonomous Policies consist of the AI-Driven Posture agent and the Posture Recommendation Wizard, both of which are included in the core license. Together, these features ensure your policies remain accurate, optimized, and aligned with Cato best practices.

### AI-Driven Insights

AI-Driven Insights evaluate the effectiveness and relevance of your configurations, identifying areas that may require attention. Recommendations are automatically generated for specific rules in your policy to help align it with Cato’s posture checks for optimal and performance.

AI-Driven Posture agent is supported for the Internet Firewall, WAN Firewall, LAN Firewall, and Remote Port Forwarding Policies.

![Auto.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27344444940957(1).png)

#### Related Articles

- [What is the Cato Internet Firewall?](/v1/docs/what-is-the-cato-internet-firewall)
- [What is the Cato WAN Firewall?](/v1/docs/what-is-the-cato-wan-firewall)
- [Configuring Remote Port Forwarding for the Account](/v1/docs/configuring-remote-port-forwarding-for-the-account)
- [What is the Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall)

### Posture Recommendation Wizard

The Posture Recommendation Wizard simplifies the process of creating or updating policies by:

- Recommending rules to enable
- Suggesting improvements to your existing rules

After generating a list of recommended rules, you can select which ones to apply. The Wizard then guides you through the configuration process, ensuring that each update is applied accurately and efficiently.

The Posture Recommendation Wizard is supported for the Internet and WAN Firewalls, TLS Inspection Policy, Private Access and Application Control Policy.

![TLSi_Wizard_Rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27344490685085(1).png)

### Related Articles

- [Using the Configuration Wizard](/v1/docs/using-the-configuration-wizard)

## Autonomous Policies Use Cases

The following use cases provide examples for how autonomous polices can be used with each feature.

#### Internet Firewall Policy: Deleting a Rule Providing Temporary Access

A developer needed to test a new integration with a cloud-based payment gateway initially blocked by the organization's Internet Firewall policy. To enable testing, the IT team created a temporary rule allowing outbound access. Once testing concluded, the rule was intended to be deleted, but that step was inadvertently missed.

A week later, the IT team saw that the **Review Temporary Rule** Posture check flagged the rule with a **Failed** status. Upon investigation, they discovered that the temporary rule granting access to the payment gateway was still active.

The IT team quickly identified and remediated the oversight by deleting the rule.

The IT team quickly identified and remediated the oversight by deleting the rule. This ensured their firewall policy remained aligned with security standards and reduced the attack surface, and prevented unnecessary exposure.

![IFW_eg.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27344445163549(1).png)

#### WAN Firewall Policy: Identifying Overly Permissive Rules

To enable quick access to a newly deployed internal collaboration tool, the IT team created a WAN Firewall rule allowing access from all Site locations. The rule permitted traffic to the application server from the entire corporate network segment. This covered more users than necessary as a temporary measure until more granular access controls could be implemented. However, the rule remained unchanged well after deployment.

The AI-based **Overly Permissive Rule** Posture check flagged this rule for review. The AI engine analyzed traffic and user access patterns, identifying that only two specific departments were actively using the application. It also noted that the current rule applied to all users across the WAN, including those with no business need for access. This enabled the IT team to refine the rule to apply only to the relevant departments

The AI-driven alert ensured the IT team reduced the attack surface and enforced a ZTNA strategy by ensuring only approved, authenticated users could access the tool while blocking access for all other users.

![WAN_Firewall1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27344490899357(1).png)

#### TLS Inspection: Securing AI Tool Usage with the Posture Recommendation Wizard

As part of a broader digital transformation initiative, the IT team enabled access to several generative AI tools to improve employee productivity. While valuable, these tools raised concerns around potential data leakage, particularly involving sensitive corporate and customer information.

To address this, the security team needed the ability to inspect TLS-encrypted traffic for these apps. However, there was a significant operational challenge to manually identify which domains were safe to decrypt and which might break under inspection.

The team used the TLS Inspection Wizard to simplify and accelerate the deployment. The wizard recommended a balanced and secure configuration:

- Inspect Rules were automatically created for vetted categories like Popular Cloud Apps and Cato-Recommended Domains, including commonly used AI tools
- Bypass Rules were suggested for incompatible traffic, such as Categories that are not inspected due to privacy regulations and concerns
- The wizard clearly indicated which existing rules were safe to enable immediately and which might require further review

As a result, the IT team implemented TLS inspection efficiently, gaining visibility into encrypted traffic without disrupting business-critical applications or user productivity.

![TLSi_Wizard_Rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27344490685085(1).png)

#### Remote Port Forwarding: Identifying Forgotten Test Rules

As part of a troubleshooting effort, an engineer temporarily enabled Remote Port Forwarding to allow external access to a staging server hosted at a branch location. The rule forwarded traffic from a specific external port to the internal server over SSH, intending to disable the rule once the issue was resolved.

Although the rule was labeled for testing, it was unintentionally left active after troubleshooting was completed.

A few days later, the AI-based **Review Testing Rule** best practice had a **Failed** status. The AI engine identified a rule that included a broad exposure to the Internet and included "test" in the rule name. This indicated a temporary configuration that may have been forgotten.

The IT team was able to quickly locate and remove the rule, restoring a more secure Remote Port Forwarding posture and minimizing unnecessary external access.

![RPF1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27344411379741(1).png)
