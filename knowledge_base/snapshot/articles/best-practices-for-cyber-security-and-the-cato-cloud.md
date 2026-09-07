---
title: "Best Practices for Cyber Security and the Cato Cloud"
slug: "best-practices-for-cyber-security-and-the-cato-cloud"
tags: ["Best Practices", "Internet Security"]
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/best-practices-for-cyber-security-and-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices for Cyber Security and the Cato Cloud

This article contains best practices for security policies and settings to provide the maximum protection for your account.

## Security Best Practices

These are recommended best practices to make sure that you are providing the best level of defense against cyber threats and malware. We strongly recommend that you review the security policies and settings in your account based on the recommendations below.

1. Restrict security policies to actual business policies:
  1. Review WAN and Internet firewall rules and make sure that they are specific as possible.
    - Replace the **Any** settings in rules with items that are the actual source, destination, application, service, and so on.
  2. Block Cato's predefined System Categories that contain common security risks, such as: Anonymizers, Botnets, Cheating, Compromised, Criminal Activity, Cults, Gambling, Hacking, Keyloggers, Malware, Nudity, P2P, Parked domains, Phishing, Porn, Questionable, Spam, Tasteless, Weapons, Sex Education, Spyware, Violence and Hate.
    - Tip - you can create a new Custom Category that contains all the items that are security risks and add it to the firewall rule.

![Category_BestPractice.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/4457047005469.png)
  3. Block the category **Uncategorized**, this category can contain domains and websites that are potential security risks.
  4. For more information, see [Internet and WAN Firewall Policies – Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies). (Security > Internet Firewall and Security > WAN Firewall)
2. Refine the Remote Port Forwarding (RPF) and Local Port Forwarding settings for inbound traffic:
  1. Avoid RPF rules with **Traffic Sources** that use **Any** (0.0.0.0) as much as possible. Instead configure specific IP ranges for the rules.
    - For more information, see [Controlling Inbound Traffic with Remote Port Forwarding](/v1/docs/security-and-qos-recommendations-for-rpf). (Security > Remote Port Forwarding)
  2. Avoid configuring a site with Local Port Forwarding rules. Instead, replace them with RPF rules. (Network > Sites > (site name) > Local Port Forwarding)
3. Implement network segmentation for your sites.
  1. Provides extra security, especially against ransomware.
  2. For more information, see [Network Segmentation - Best Practices](/v1/docs/network-segmentation-best-practices).
4. Use IPS **Geo Restriction** rules to block inbound and outbound traffic from countries where you have no business dealings and are known sources of malicious traffic.
  1. Please be aware that geo restriction rules for IPS impact all traffic in your account.
  2. For more information, see [(New) Configuring the IPS Policy.](/v1/docs/configuring-the-ips-policy) (Security > IPS > Geo Restriction)
5. TLS Inspection allows Cato's security services to inspect encrypted Internet traffic.
  1. Use the granular TLS Inspection policy to only inspect specific traffic types.
  2. Exclude applications and destinations which don't work with TLS Inspection.
  3. For more information, see [Best Practices for TLS Inspection](/v1/docs/best-practices-for-tls-inspection). (Security > TLS Inspection)
6. Refine settings for custom applications and define all the applicable items for the rule for the custom application.
  1. For example, configure the custom application with defined **Destination IP**, **Domains**, and **Ports** instead of only defining the **Ports**.
  2. For more information, see [(New) Working with Custom Applications](/v1/docs/working-with-custom-apps). (Resources > Custom Apps)
