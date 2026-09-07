---
title: "Cryptocurrency and the Cato Cloud"
slug: "cryptocurrency-and-the-cato-cloud"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/cryptocurrency-and-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cryptocurrency and the Cato Cloud

## The Problem with Crypto

If you have spent any amount of time browsing the Internet, you are likely to have encountered the idea of cryptocurrency at least once. This is an exciting step in the establishment of the world's digital economy and poses both significant opportunities and risks.

The rise in popularity of cryptocurrencies such as Bitcoin, Monero, Ripple, Shib, and so on has led to a dramatic increase in the number of people who are actively looking to trade these currencies. When this is coupled with lower barriers to entry for trading platforms, then many people see dabbling with cryptocurrency is seen as a lucrative proposition. Especially cyber-criminals.

Cyber-criminals often use fraud attacks in order to trick the user to send cryptocurrency to the attacker’s cryptocurrency wallet, or they may use other techniques such as malware, or drive-by attacks to use the victim’s processing resources for crypto-mining purposes. In the eyes of cyber-criminals, an unsecured machine is exactly the same as a wallet left unattended at a nightclub.

Luckily, if you're a Cato customer, we automatically have mitigation strategies in place to help keep you secure.

## Cato's Crypto Solution

There are a variety of vectors for cryptocurrency attacks, for example stealing crypto coins just like stealing someone's physical wallet. However, it's also possible to mine crypto coins using local hardware. This means that it's possible that for cyber-criminals to compromise hosts and servers in your account and use them to mine crypto coins. This causes a significant impact on performance for these resources, and increased profits for the cyber-criminals.

The Cato Cloud uses several different approaches to protect your account from crypto attacks, let's start to explore the options.

### IPS Signatures

Whenever a crypto-miner attempts to utilize system resources to generate a coin, the software must contact a pool, or validate the work effort against the blockchain. Once the proof of completion has been submitted, a coin (or most likely a fragment of), is issued to the associated wallet. This leads to machines running at nearly 100% CPU and GPU almost constantly, impacting your users' digital experience and increasing operational costs for your business.

The Cato IPS service automatically mitigates and blocks the transmission and communication of this type of traffic, using advanced threat analysis which is continuously updated. The Cato Security team creates dedicated IPS signatures to detect mining protocols such as Stratum and also for known miners such as XMRig and XMR-Stak. In addition, there are also dedicated IPS signature and heuristics for known cryptocurrency malware, to help mitigate any potential impact there may be on your business operations.

Cato is constantly maintaining, monitoring and evolving the IPS engine, so you can relax knowing that the Cato Cloud is always up-to-date with the latest protections.

### Threat Intelligence Feeds

As part of the Cato IPS service, we use dedicated threat intelligence feeds for cryptocurrency, which help to detect mining pools and malicious domains associated with known cryptocurrency attacks and malware. In addition, we created our own threat intelligence feed to detect and block cryptocurrency activity (regardless of the protocol type).

Cato also leverages our global backbone, monitoring trillions of network flows for mining activities across all of our customer networks. If we observe and block a potential threat for one of our customers, the same protection is applied to all customers.

### Anti-Malware Protections

Imagine a world where you've updated the IPS engine databases on your network, patched all your firewalls and scoured every directory on your servers. Still - your users are still reporting that the network is 'slow', and tickets are piling up in your helpdesk queue. What do you do? Naturally, you start with packet captures, you look at the application throughput metrics. Then you run a traceroute over the network, and everything looks great. Slowly it dawns on you, and panic sets in. It's not a network issue, it's a host problem.

Your endpoint devices are the widest attack surface to corporations, and it's farily simple to infect a device with malware, especially if they leverage technology like WebAssembly. This is often used by attackers to perform cryptocurrency mining using the victim’s processing resources. But unlike 'traditional' malware, it's possible to execute the attack without downloading a file.

Imagine your user opens their browser and establishes a legitimate session to a website. They are browsing as normal, but their machine is slowing down (and the laptop fans are spinning at 100%). What happened? Well, this user may have accessed a website that loads crypto-mining code. Oops, your network is now exposed and potentially infected.

Cato handles such threats by scanning WebAssembly files (and all other file types) with the Anti-Malware engines, and detects malicious files before they actually reach your endpoint devices. By using a combination of our threat intelligence feeds and heuristic analysis, we can block these types of attacks.

The Cato global backbone provides coverage for north/south and east/west distribution of potentially malicious code. It ensures that every user, site, branch and cloud presence is equally protected and doesn't require you to deploy any patches or upgrades.

### Cato's MDR Service

Cato's Managed Threat Detection and Response (MDR) service monitors security incidents and vulnerabilities across your network. MDR uses all of the above techniques to detect cryptocurrency attacks (as well as every other security incident which may arise on your network.) If an issue is detected, then you're protected and will be informed on the impact to resources in your network.

Here are some example scenarios where MDR helps you to track cryptocurrency issues:

- Periodic communication identified towards cryptocurrency domains with unknown clients
- Periodic JSON-RPC traffic observed which is associated with crypto-mining activities
- Suspicious WebAssembly download attempts from low popularity domains.

## What Does a Cryptocurrency Event Look Like?

If cryptocurrency events are ever identified on your network, you can easily review the events in **Home > Events** including:

- Time of event
- A descriptor of Threat Name
- Signature ID
- Threat Type
- Action
- Source/Destination IP
- Source Site Name
- Traffic Direction

Using this information, you can easily pinpoint who, what, where and when your cryptocurrency incident occurred. This provides a clear line of sight to identify which machines are attempting to perform crypto actions within your corporate environment.

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303168264093.png)

Expand the event to show more information about the incident. Below is an example of a crypto-mining event:

![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303152405277.png)
