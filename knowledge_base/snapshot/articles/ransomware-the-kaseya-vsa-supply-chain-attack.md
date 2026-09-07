---
title: "Ransomware: The Kaseya VSA Supply Chain Attack"
slug: "ransomware-the-kaseya-vsa-supply-chain-attack"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/ransomware-the-kaseya-vsa-supply-chain-attack"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ransomware: The Kaseya VSA Supply Chain Attack

## Overview

This article will discuss information pertaining to the Kaseya VSA Supply-Chain Ransomware attack, and steps that Cato have taken to ensure that our customers stay protected.

As of July 7th 2021, all known IOCs relating to the Kaseya VSA Ransomware attack have been implemented within the Cato Threat Intelligence Platform. Any traffic which matches this profile (or similar) will be actively blocked by our IPS.

## Background

As of July 3rd 2021, Multiple organizations and Managed Service Providers (MSPs) have been targeted by the REvil (aka Sodinokibi) ransomware. This has been conducted in a supply chain attack focusing on the Kaseya VSA software. This attack has led to Kaseya urging customers to [users to shut down their VSA servers](https://www.kaseya.com/potential-attack-on-kaseya-vsa/) to prevent them from being compromised.

REvil (frequently detected by threat protection systems as Ransom.Sodinokibi) is a family of ransomware used in targeted attacks. Attackers will attempt to encrypt all computers on the victim’s network, preventing access to files or data unless a large sum of money is paid.

## Impact

Once the target computer has been infected with the Sodinokibi ransomware, administrative access is disabled and the malicious code will begin to encrypt data. This is the initial step prior to the 'ransom' being demanded.

Once the encryption process is complete, the system’s desktop wallpaper is set to an image stating that "All of your files are encrypted", with a link to a readme file detailing how to restore access to the machine. Each infected machine is encrypted with a Private Key unique to that host, which is used in the ransomware decryption process. This tactic ensures that data retrieval using traditional means incurs an element of private key corruption and permanent data loss.

In the event that a machine becomes infected with this ransomware, data will not be accessible (or extractable) from the device unless a ransom has been paid.

## What is Cato doing?

The Security Analysts at Cato Networks are working tirelessly to identify, pinpoint and mitigate any potential vulnerability or exposure that our customers may have to this threat.

- After using a forensic analysis of Cato Customer traffic profiles, we have identified several customers who currently use Kaseya products.
- Our preliminary analysis shows no evidence for infection in our customer base. This is based on the Indicators of Compromise (IOC) published in the wild that are related to the attack).
- Cato Networks has added all IOCs related to this attack to our Threat Intelligence Platform. This will ensure that any traffic of this type will be blocked by our IPS.
- It is recommended that any customer using Kaseya products should follow Kaseya’s [continued advisory.](https://helpdesk.kaseya.com/hc/en-gb/articles/4403440684689-Important-Notice-July-2nd-2021)

This situation is currently evolving within the IT landscape, and Cato Networks is actively monitoring and investigating the situation to ensure our customers remain protected.
