---
title: "Action Required: Update Policies to Include ChromeOS"
slug: "action-required-update-policies-to-include-chromeos"
updated: 2026-07-27T13:10:31Z
published: 2026-07-27T13:10:31Z
canonical: "knowledge.catonetworks.com/action-required-update-policies-to-include-chromeos"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Required: Update Policies to Include ChromeOS

For configuration of some policies in the Cato Management Application, Chromebook devices running ChromeOS are currently included within:

- Linux - when connecting behind a site
- Android - when connecting with the Client

To simplify configuration, starting the week of August 9, 2026, ChromeOS will be available as a dedicated operating system. This lets you easily and consistently configure policy behavior for ChromeOS devices separately from other operating systems.

This change will be made gradually:

- Starting August 9, 2026, ChromeOS will operate side by side with Linux and there is no impact on Android Client versions lower than v5.7. During this period:
  - There is no change to policy behavior
  - ChromeOS devices will continue to match the existing policy configuration for either Linux or Android Client versions lower then 5.7
  - ChromeOS can be configured as a distinct operating system for more granular control
    - Available on any Linux Client version and Android Client version 5.7 and higher
- Starting September 13, 2026 ChromeOS will behave as a distinct operating system and will no longer be included within Linux or Android policy configurations. This change is supported from Android Client v5.7 or higher and any Linux Client. After September 13:
  - ChromeOS can be configured as a distinct operating system for more granular control
  - ChromeOS devices will only match rules that explicitly include a setting for Chrome OS

### Which Policies Does This Apply To?

This change applies to these policies:

- Network Rules
- Internet Firewall
- WAN Firewall
- TLS Inspection
- Client Connectivity
- Dynamic IP Allocation
- Split Tunnel

### What is the Impact to the Account?

Between August 9, 2026, and September 13, 2026, there is no impact on your account, ChromeOS devices will continue to have the existing behavior.

After September 13, 2026, policies that currently block/allow these devices will not apply to Chrome OS devices:

- Linux Client with any version
- Android Client v5.7 or higher

### What Action Do I Need to Take?

Between August 9, 2026, and September 13, 2026, review your policies that include Linux or Android as an operating system.

- If you want ChromeOS devices to continue matching those policies, update the relevant rules to include **ChromeOS**.
  - For example, if you have an Internet Firewall rule that blocks access to gambling sites on Linux devices, add **ChromeOS** as an operating system for this rule.
- If you want different behavior for ChromeOS and Linux or Android, upgrade the Android Client to v5.7 or higher and create separate policy rules for each operating system.
  - For example, if you have a Client Connectivity Policy rule that blocks Android devices from connecting to your network remotely and you want to allow ChromeOS devices, then create a new rule in the Client Connectivity Policy to allow **ChromeOS**.

### Who Do I Talk to If I Have Questions?

Please use the [Cato Knowledge AI assistant](/v1/docs/what-is-cato-s-ask-ai-agent) in the CMA to answer questions about configuring policies for ChromeOS.

Show me the [Ask AI Workspace in the CMA](https://externallink.cc.catonetworks.com/#/account/me/aiWorkspace).
