---
title: "How the Cato Cloud Protects your Account from Ransomware Encryption Actions"
slug: "how-the-cato-cloud-protects-your-account-from-ransomware-encryption-actions"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/how-the-cato-cloud-protects-your-account-from-ransomware-encryption-actions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How the Cato Cloud Protects your Account from Ransomware Encryption Actions

This article explains how the IPS security service in the Cato Cloud security stack protects your network from ransomware attempts to maliciously encrypt resources in your network.

When you enable [IPS to block WAN traffic](/v1/docs/configuring-the-ips-policy), this helps protect against attempts by ransomware to move laterally and spread over the WAN.

## How the Cato Security Stack Identifies Ransomware Attacks

Ransomware continues to be one of the most dangerous threats to organizations, these attacks can lock and encrypt the victim's data. Then there is a demand for payment to unlock and decrypt the data. Cato leverages the security stack engines to kill the attack chain as quickly as possible.

- IPS – Cato's IPS includes data from numerous threat intelligence sources and can block potential ransomware, including:
  - Access to suspected websites that are likely to be associated with different threats (such as malware C&C, ransomware, phishing, and so on)
  - Suspected malicious host that is attempting to spread ransomware
  - Lateral traffic over the WAN that would leverage the threat actor for the ransomware
- Internet Firewall – protects users from accessing malicious websites (such as the Malware category) where they can accidentally download a malicious payload that could contain ransomware.
- Anti-Malware and NG Anti-Malware – provides an additional layer of protection and contributes to the Cato ZTNA (Zero Trust Network Access). These engines prevent any malicious downloads attempts and block the related ransomware before they are executed on the user's device.

> [!NOTE]
> **Note:**
> 
> These Cato protections work when the action is set to Block.

### Blocking SMB Ransomware Traffic

The Cato Security team continuously develops and updates traffic algorithms and heuristics to detect SMB traffic that is associated with ransomware attacks. These are supplemented with malware data from a variety of private and open source threat intelligence feeds regarding known ransomware campaigns.

Cato uses these techniques to block malware attacks that are trying to spread over the WAN:

- Block traffic from a single host that is infected with ransomware and then tries to spread the ransomware to other hosts (in the WAN)
- Block traffic with file extensions that have low credibility and therefore are potential ransomware

In addition, once IPS identifies a ransomware attack, it blocks all traffic from the infected host over TCP port 445. This prevents the attack from infecting and impacting other network assets.

## Reviewing Events for Blocked Ransomware Attacks

You can review Security events in **Home > Events** and find events for suspected ransomware attacks in your account that were blocked. There are different event sub types for these attacks blocked by IPS and by the firewall. For IPS events, the threat type can be classified as **Ransomware**.

This is an example of an event for a suspected ransomware attack blocked by IPS:

![Ransomware_Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303151958429.png)

The logic for this IPS protection is counter based, and it counts the SMB activity over a short time frame (a few hours) to identify the ransomware attack. During this time frame, if the IPS engine determines that a host is the possible source of the ransomware, it then blocks any SMB WAN traffic (port 445) from this host.

When IPS identifies a ransomware attack, it can be based on traffic that matches a behavioral pattern which was identified as ransomware. It is possible that the event is a false positive, and is actually legitimate traffic.

## Cato Blocked a Ransomware Attack - Now What?

If you discover that IPS blocked a ransomware attack, most likely some of your internal resources have already been hit by ransomware. Cato's IPS protections work to prevent the ransomware from spreading over the WAN, and your EPP solution minimizes the damage in the LAN for the relevant sites.

This list contains suggested next steps for the internal resources that were hit by ransomware attacks:

1. Isolate the infected hosts from the network (in both the WAN and Internet firewalls).
2. Identify which assets in your organization were the target of the ransomware attack.
3. You can view the CISA recommendations for ransomware incidents [here](https://www.cisa.gov/stopransomware/ive-been-hit-ransomware). For example:
  - Identify which files that attack damaged or impacted.
  - Confirm the identity of the malware family or author.
  - Make sure that all corporate devices are installed with endpoint protection software and it is updated with signatures that can identify the malware responsible for this attack.
