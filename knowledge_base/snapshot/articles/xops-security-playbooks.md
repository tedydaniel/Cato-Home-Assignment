---
title: "XOps Security Playbook - Phishing Website Attack"
slug: "xops-security-playbook-phishing-website-attack"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-security-playbook-phishing-website-attack"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Security Playbook - Phishing Website Attack

This playbook describes how to use the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) to investigate stories for attacks that use phishing websites.

## Overview

This playbook outlines a systematic approach for SOC engineers to investigate potential security incidents related to websites used for phishing attacks. It provides a framework for gathering initial information, analyzing network traffic, and drawing conclusions about the nature of the threat.

## Gathering Initial Information about the Threat

Use the **Details** widget in the story to gather basic information about the potential threat. Review the **Description** of the story and other data to decide if further investigation is required. In addition, the **Similar Stories** section shows other stories that share similar indicators and observables.

![gathering-info.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977991575837.png)

Click **Generate AI Summary** for a natural language story description that provides rich context and helps you quickly assess the story.

![XDR_Phishing_Playbook_-_AI_Summary.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978013234205.png)

Use the **Source** widget to review data about the device that is impacted by this attack.

![source.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977998717981.png)

You can also use the [Indications Catalog](/v1/docs/using-the-indications-catalog) for more information (such as the **Indication ID**), and focus the investigation based on your query.

## Understanding Attack Distribution for a Phishing Attack

The **Attack Distribution** graph can help to understand the nature of the traffic, periodic attacks which resembles bot behavior, a one-time occurrence, or other characteristics.

For phishing attacks, the traffic distribution will usually consist of a low amount of flows, or a one-time occurrence, with a graph that looks similar to this:

![XDR_Phishing_Playbook_-_attack_distribution.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977991814045.png)

## Determining the Stage of the Phishing Attack

To properly investigate a potential phishing attack, it's important to first identify at what stage the attack was detected. Cato's Security services detect phishing attacks at the following different stages:

- Block Access - Cato identifies the browsing destination as a phishing site and blocks access to the site
- Block Credentials Submission - When a user accesses a phishing site and the site is rendered in the browser, Cato can block the user from entering credentials
- Post-Compromise Detection - The Suspicious Activity Monitoring (SAM) service can identify when a user submits credentials in risky sites, and creates events that alert the admin to the potential breach

Use the **Target Actions** widget to see the events that relate to the story and find information to determine at what stage the phishing attempt was detected, and if it was blocked. The **Threat Name** field can indicate at what point the attack was detected.

This is an example of an event showing an IPS block of credential submission on a phishing site:

![XDR_Phishing_Playbook_-_credential_submission.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978019873821.png)

## Investigating Phishing Attacks at Different Stages

After determining the stage at which the potential attack was detected, follow the investigation steps described below for detection at that stage.

### When Access to the Site was Blocked

This section describes an approach for verifying that the blocked website is a phishing site. This part of the investigation focuses mainly on the target.

#### Targets

The **Targets** section lets you examine the identified targets to learn more about their potential intent and the likelihood that the target is malicious:

- Assess Cato's malicious score
- Examine Cato's popularity
- Consider associated Cato categories
- Review the number of threat intelligence feeds linked to the target

An especially important indicator for phishing attacks is the **Creation Date** of the domain. If the date is recent, it is more likely that the site is malicious.

![XDR_Phishing_Playbook_-_target_creation_date.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978002439837.png)

**Using Target Links to Search External Sources**

By now, you should have a solid grasp of the activity captured in this story, the **Target Links** help you conduct an external search on reputable sources for historical context and signs of malicious behavior. Correlate this data to identify connections with other entities and possible links to known threat actors, campaigns, or techniques.

#### Attack Related Flows

Use the **Attack Related Flows** section to examine unprocessed data flows related to the story.

Analyze supplementary data points from these flows, including URLs, user-agents, file names, and other relevant attributes, and compare them to the findings from the previous investigation step to reveal potential correlations.

#### Conclusion

For most cases of blocked access to a phishing site, the correct classification for the story is **Browsing to a Phishing Site**.

#### Recommended Actions

1. Verify with the victim whether the attack was a spear phishing attempt and was specifically targeted at them (using a private name, private information, etc.).

If not, ensure that no other employees were victims of the same phishing campaign.
2. If the source of the phishing attempt is email-based and known to the user, mitigate the attack by using your organizational email platform to report and block the source address.
3. If the source of the phishing attempt is unknown, perform a full Endpoint Protection scan (Anti-Virus, EPP, EDR, etc.) and remove any unknown programs and browser extensions from the infected machine.

### When Credentials Submission was Blocked

This section describes an approach for verifying there was an attempt to submit credentials to a phishing website. This part of the investigation focuses mainly on the detected target and URL.

#### Targets

The **Targets** section lets you examine the identified targets to learn more about their potential intent and the likelihood that the target is malicious:

- Assess Cato's malicious score
- Examine Cato's popularity
- Consider associated Cato categories
- Review the number of threat intelligence feeds linked to the target

An especially important indicator for phishing attacks is the **Creation Date** of the domain. If the date is recent, it is more likely that the site is malicious.

![XDR_Phishing_Playbook_-_target_creation_date.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978002439837.png)

**Using Target Links to Search External Sources**

By now, you should have a solid grasp of the activity captured in this story, the **Target Links** help you conduct an external search on reputable sources for historical context and signs of malicious behavior. Correlate this data to identify connections with other entities and possible links to known threat actors, campaigns, or techniques.

**Identifying the Referrer**

In phishing attacks, the target first communicated with is often not the malicious site itself, but a referrer site, meaning a site that contains the link to the malicious site. The referrer site appears in the **Attack Related Flows** section in the **Referrer** column.

![XDR_Phishing_Playbook_-_referrer.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977999077405.png)

**Checking the Referrer with Domain Lookup**

After identifying a referrer, you can use [Domain Lookup](/v1/docs/identifying-the-category-for-a-domain) to research the domain. Low **Popularity** and a high **Malicious Score** indicate a malicious domain.

![XDR_Phishing_Playbook_-_domain_lookup.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978013691549.png)

#### Attack Related Flows

Use the **Attack Related Flows** section to examine unprocessed data flows related to the story.

Analyze supplementary data points from these flows, including URLs, user-agents, file names, and other relevant attributes, and compare them to the findings from the previous investigation step to reveal potential correlations.

When investigating a URL, it is important to check whether it contains any sensitive data (note that in many cases the URLs are encoded and need to be decoded to access all the data it contains). We also recommend checking external tools for similar URL patterns to gain further insight into the detected traffic.

**Note:** When performing an investigation, we recommend that you don't access suspicious phishing related sites.

#### Conclusion

For most cases of blocked credentials submission to a phishing site, the correct classification for the story is **Credentials Submission Attempt**.

#### Recommended Actions

1. If sensitive data is leaked, change the password to the relevant services and consider initiating a hard log-off from all services.
2. Make sure that no malicious files are downloaded and executed.
3. Verify with the victim whether the attack was a spear phishing attempt and was specifically targeted at them (using a private name, private information, etc.).

If not, ensure that no other employees were victims of the same phishing campaign.
4. If the source of the phishing attempt is email-based and known to the user, mitigate the attack by using your organizational email platform to report and block the source address.
5. If the source of the phishing attempt is unknown, perform a full Endpoint Protection scan (Anti-Virus, EPP, EDR, etc.) and remove any unknown programs and browser extensions from the infected machine.

### When the Attack was Detected Post-Compromise

This section describes an approach for verifying there was submission of credentials to a phishing website. This part of the investigation focuses mainly on the detected target and referrer (a site that contains the link to the malicious site).

#### Targets

The **Targets** section lets you examine the identified targets to learn more about their potential intent and the likelihood that the target is malicious:

- Assess Cato's malicious score
- Examine Cato's popularity
- Consider associated Cato categories
- Review the number of threat intelligence feeds linked to the target

An especially important indicator for phishing attacks is the **Creation Date** of the domain. If the date is recent, it is more likely that the site is malicious.

![XDR_Phishing_Playbook_-_target_creation_date.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978002439837.png)

**Using Target Links to Search External Sources**

By now, you should have a solid grasp of the activity captured in this story, the **Target Links** help you conduct an external search on reputable sources for historical context and signs of malicious behavior. Correlate this data to identify connections with other entities and possible links to known threat actors, campaigns, or techniques.

**Identifying the Referrer**

In phishing attacks, the target first communicated with is often not the malicious site itself, but a referrer site, meaning a site that contains the link to the malicious site. The referrer site appears in the **Attack Related Flows** section in the **Referrer** column.

![XDR_Phishing_Playbook_-_referrer.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977999077405.png)

**Checking the Referrer with Domain Lookup**

After identifying a referrer, you can use [Domain Lookup](/v1/docs/identifying-the-category-for-a-domain) to research the domain. Low **Popularity** and a high **Malicious Score** indicate a malicious domain.

![XDR_Phishing_Playbook_-_domain_lookup.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978013691549.png)

#### Attack Related Flows

Use the **Attack Related Flows** section to examine unprocessed data flows related to the story.

Analyze supplementary data points from these flows, including URLs, user-agents, file names, and other relevant attributes, and compare them to the findings from the previous investigation step to reveal potential correlations.

When investigating a URL, it is important to check whether it contains any sensitive data (note that in many cases the URLs are encoded and need to be decoded to access all the data it contains). We also recommend checking external tools for similar URL patterns to gain further insight into the detected traffic.

**Note:** When performing an investigation, we recommend that you don't access suspicious phishing related sites.

#### Conclusion

For most cases of post-compromise detection of credentials submission to a phishing site, the correct classification for the story is **Credentials Submission**.

#### Recommended Actions

1. If sensitive data is leaked, change the password to the relevant services and consider initiating a hard log-off from all services.
2. Make sure that no malicious files are downloaded and executed.
3. Verify with the victim whether the attack was a spear phishing attempt and was specifically targeted at them (using a private name, private information, etc.).

If not, ensure that no other employees were victims of the same phishing campaign.
4. If the source of the phishing attempt is email-based and known to the user, mitigate the attack by using your organizational email platform to report and block the source address.
5. If the source of the phishing attempt is unknown, perform a full Endpoint Protection scan (Anti-Virus, EPP, EDR, etc.) and remove any unknown programs and browser extensions from the infected machine.
6. If the identified traffic wasn't blocked, create an [Internet Firewall](/v1/docs/managing-the-internet-firewall-policy) rule to block the target.
