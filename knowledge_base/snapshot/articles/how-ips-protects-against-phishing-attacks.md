---
title: "How IPS Protects Against Phishing Attacks"
slug: "how-ips-protects-against-phishing-attacks"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/how-ips-protects-against-phishing-attacks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How IPS Protects Against Phishing Attacks

This article explains how the IPS security service and Internet firewall in the Cato Cloud security stack protects your network from phishing attacks.

## How the Cato Security Stack Identifies Phishing Attacks

Phishing continues to be one of the most dangerous threats to organizations, and phishing attacks can be an initial vector to infiltrate the corporate network or to steal credentials and other private data. The Cato IPS service and Internet firewall in the security stack has different techniques to identify traffic as a phishing attack and block the attack before it enters your network.

### IOCs Based on Threat Intelligence Feeds

Cato's Security team creates IPS and firewall protections for phishing attacks based on Indicators of Compromise (IOCs). The IOCs are accumulated from a variety of private and open source threat intelligence feeds that contain domains, URLs, and other data about known phishing campaigns. Any traffic that matches the IOC of a known phishing campaign is automatically blocked by the IPS engine.

### Heuristics and Algorithms Based on Traffic Analysis

Another level of protections in the security stack utilizes heuristics and algorithms that are based on the characteristics of phishing websites. The Security team analyzes all this network data and then creates protections that can identify websites which are sources of phishing attacks. For example, a phishing campaign can use a fake Office365 URL to trick users into believing that this link is legitimate. If a user accidentally clicks the malicious Office365 link, IPS or the firewall can block the traffic and prevent the phishing attack.

Additionally, IPS includes protections that use advanced machine learning algorithms and image processing models to protect against the latest phishing attack techniques. For example:

- IPS machine learning algorithms can detect and block attacks that use new domains created through techniques such as DGA and cybersquatting
- IPS image processing models can identify malicious sites that use fake icons, as well as sites that use icons, graphics, and other elements identical to those of legitimate sites

The Security team is constantly analyzing network traffic in the Cato Cloud to improve the heuristics and algorithms and improve the ability to detect new phishing attacks.

### Detection and Mitigation Strategies

The IPS phishing protections use various strategies to detect and mitigate attacks, which helps maximize protection with the ability to block phishing attacks at different stages. These are the types of protection strategies:

- **Blocking Access** - These protections identify the browsing destination as a phishing site and block access to the site. Examples using this strategy include protections based on:
  - Threat intelligence feeds
  - Machine learning models that identify potential phishing sites
  - Identification of newly registered domains
  - Heuristics that identify suspicious top-level domains
  - Heuristics that detect legitimate HTML title tags rendering in an unknown resource
- **​Blocking Credentials Submission — Advanced Phishing Page Element Detection​****​** - These protections can block a phishing attack even after the user has already accessed the malicious site and the webpage has fully rendered in the browser. The engine uses advanced heuristics to detect legitimate Office 365 visual and functional elements that appear on pages not owned or operated by Microsoft. Attackers increasingly clone authentic assets, when such inconsistencies between trusted brand assets and untrusted domains are detected, the IPS service intervenes at the critical moment by blocking the credential submission. Importantly, the user does not see a block page. Instead, the system silently prevents the credentials from leaving the device or browser session. A corresponding security event is generated in the CMA with the threat name: Attempt to insert sensitive information into a phishing site.
- **Post-Compromise Detection — Identifying Credential Submission in High-Risk Web Forms** - n some situations, users may access suspicious domains that cannot be definitively categorized as malicious and therefore are not immediately blocked. In these cases, the [Suspicious Activity Monitoring (SAM)](/v1/docs/monitoring-suspicious-activity-with-ips-sam) service provides a crucial secondary layer of protection. SAM continuously monitors user interactions with high-risk or untrusted web forms, detecting behaviors indicative of credential harvesting. If a user enters or submits corporate credentials on such a site, SAM generates detailed events that alert administrators to the potential compromise so they can take immediate action. To enable these detections, TLS Inspection must be enabled, allowing inspection of encrypted traffic to identify misuse of legitimate Microsoft assets within malicious pages.TLS Inspection must also be enabled for the following Microsoft domains:
  - windows.net​
  - windows.com
  - ​msauthimages.net
  - msauth.net
  - msftauthimages.net

## Reviewing Events for Blocked Phishing Attacks

You can review Security events in **Home > Events** and find any phishing attacks in your account that were blocked. There are different event sub types for phishing attacks blocked by IPS and by the firewall. For IPS events, the threat type can be classified as **Reputation**, or as **Phishing**.

This is an example of an event for a phishing attack blocked by IPS:

![PhishingEvent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303152034077.png)

- IPS event fields for a phishing attack:
  - Event type - Security
  - Event sub type - IPS
  - Threat type - Reputation
    - Threat name - Domain reputation based signature – Phishing
  - Threat type - Phishing
    - Threat name - Name that the Security team gives for this phishing attack
  - Internet firewall event fields for a phishing attack:
    - Event type - Security
    - Event sub type – Internet Firewall
    - Categories - Phishing
- The IPS [mitigation strategy](/v1/docs/how-ips-protects-against-phishing-attacks#detection-and-mitigation-strategies) for a phishing attack can be identified by the format of the **signature id** in the event, as follows:
  - Signatures that block access have the prefix: **cid_heur_ba_phishing_detection_**
  - Signatures that block credentials submission have the prefix: **cid_heur_bs_phishing_detection_**
  - Signatures that detect credential submissions to risky web forms have the prefix: **cid_sam_cs_phishing_detection_** or **cid_sam_suspected_phishing_submission_to_risky_web_form**

For more information, see [Analyzing Security Events According to Threat Reputation](/v1/docs/analyzing-security-events-according-to-threat-reputation).

## Reviewing XDR Stories for Phishing Attacks

The XDR [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) generates stories for potential malware attacks including phishing, and provides tools for investigating the attack. The following is an example of a story for a phishing attack blocked by IPS. The story helps investigate the attack by providing information such as a description of the attack, the domain and URL related to the attack, and more.

![XDR_Phishing_Story.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303168026013.png)

## Cato Blocked a Phishing Attack - Now What?

This section contains suggested next steps if you discover that IPS or the Internet firewall blocked phishing attacks for your account.

1. Identify which endusers in your organization were the target of the phishing attack.
2. Talk to the endusers, and identify what type of information they were sharing with this website.
3. Tell the endusers to take the following actions:
  - Change their passwords for the website
  - Initiate a hard log off from all services that are related to the website
4. Check if any data that was shared (or potentially shared) represents any risk.
