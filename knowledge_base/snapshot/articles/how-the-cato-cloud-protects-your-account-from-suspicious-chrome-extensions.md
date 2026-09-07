---
title: "How the Cato Cloud Protects your Account from Suspicious Chrome Extensions"
slug: "how-the-cato-cloud-protects-your-account-from-suspicious-chrome-extensions"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/how-the-cato-cloud-protects-your-account-from-suspicious-chrome-extensions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How the Cato Cloud Protects your Account from Suspicious Chrome Extensions

This article explains how the IPS security service protects your network from suspicious and malicious extensions for the Chrome browser.

## How the Cato IPS Service Identifies Suspicious Chrome Extensions

Chrome extensions give users lots of features and functionality, however, organizations then face the challenge of protecting against attackers who exploit typically trusted Chrome extensions through a variety of attack vectors. The Anti-Malware service can't distinguish between benign and malicious extensions, and leaves organizations vulnerable to attacks. Cato's IPS service provides coverage for these network vulnerabilities through advanced techniques that identify potentially malicious extensions, and offer unique and valuable protection for your organization.

### Prerequisites

- Protections for Chrome extensions are included in the IPS license. For more about purchasing the IPS license, please contact your Cato representative
- The IPS service must be enabled and set to the **Block** action for Chrome extension protections functionality

### Fine-Tuning Threat Intelligence Feeds

Malicious Chrome extensions may abuse their permission level on the infected host to drop malware and compromise the host. This exposes the entire network to threats such as ransomware, data leaks, resource exhaustion, and so on. The IPS service leverages innovative techniques for maintaining, developing, and fine-tuning threat intelligence feeds to make it possible to identify suspicious activity associated with Chrome extensions.

### Blocking Chrome Extension Threats

Once the IPS service detects that a host is connected to the Cato Cloud and is using a suspicious Chrome extension, the service blocks the HTTP/S connection on that network flow. This stops the host from using the suspicious extension, and blocks connectivity to the extension to prevent it from getting updates, sending data, and so on.

> [!NOTE]
> Note:
> 
> Suspicious and malicious extensions are only blocked according to the IPS **Protection Scope** settings. For example, if the **WAN Traffic** scope is set to **Monitor** or **Allow**, then that scope will not be protected from malicious Chrome extensions.

## Reviewing Events for Blocked Chrome Extensions

You can review Security events in **Home > Events** and find the IPS block events related to Chrome extensions.

This is an example of an event for a blocked Chrome extension:

![Chrome_Extension_Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303168145309.png)

These are the IPS event fields for a suspicious Chrome extension event:

- Event Type - Security
- Event Sub-Type - IPS
- [MITRE ATT&CK](/v1/docs/using-the-mitre-att-ck-dashboard)® Techniques - Command and Scripting Interpreter (T1059)
- Threat Type - PuP
- Threat Name - Low credibility Chrome extension

These are examples of Signature ID for a Chrome extension event:

- feed_suspicous_chrome_ext_low_popu
- feed_suspicous_chrome_ext_high_popu
- feed_risky_chrome_ext_in_webstore
- feed_risky_chrome_ext_in_webstore_no_intersect

For more information about event logs, see [Analyzing Events in Your Network](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings).

## Cato Blocked a Chrome Extension - Now What?

After Cato blocks a Chrome extension, we recommend that the IT manager inspect all Chrome extensions in use and remove any that are unfamiliar. Further, because malicious Chrome extensions can infect legitimate extensions to exploit their permissions, the best practice is to remove all existing browser extensions and reset Chrome to default settings.
