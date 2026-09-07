---
title: "XOps Security Playbook - Events Anomalies"
slug: "xops-security-playbook-events-anomalies"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-security-playbook-events-anomalies"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Security Playbook - Events Anomalies

This playbook describes how to use the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) to investigate stories related to anomalous behavior detected by the Events Anomaly producer.

For more about using the Stories Workbench to analyze Events Anomalies, see [Analyzing XOps UEBA Stories for Usage and Events Anomalies](/v1/docs/analyzing-xops-ueba-stories-for-usage-and-events-anomalies).

## Overview

This playbook outlines a systematic approach for SOC engineers to investigate potential security incidents related to anomalous behaviors that result in unusual numbers of events. It provides a framework for gathering initial information, analyzing network traffic, and drawing conclusions about the nature of the threat.

It is applicable to situations where the engine surfaces either a volume spike (many events in a short window) or a first‑seen behaviour (an event or application that has never been observed before). Both indications arise from the same underlying behavioral analytics model; the workflow below covers them jointly and points out where additional context gathering may be required.

### What to Look For

Events anomaly stories can help identify threats that produce abnormal traffic patterns as well as network misconfigurations that could pose security threats. The following are examples of these types of potential threats:

**Threat activity associated with anomalous traffic patterns:**

- Data exfiltration attempts
- Lateral movement within the network
- Malicious infection attempts

**Network misconfigurations that could pose security risks**

- Policy violations - For example: Unauthorized access attempts, unexpected data transfers, or connections that bypass established security controls
- Open ports and protocol misuse - Anomalous traffic spikes related to specific ports or protocols often indicate that these settings are not aligned with best practices and may indicate misconfiguration
- Network segmentation failures - Misconfigured network segmentation may allow unauthorized access or movement between segments, which can be detected as anomalies

## Step 1 - Gathering Initial Information about the Threat

Use the **Details** widgets in the story to gather basic information about the potential threat and make an initial assessment whether further investigation is required. Review these key fields:

- **Description** - Understand the type of anomaly (including the specific application, engine, or behavior), and whether the focus is on a specific site or user
- **Train Period** - Shows how long the engine has been collecting baseline data for the anomaly. A longer train period may indicate a well-established baseline, while a shorter one could indicate the data is limited
- **Source Tab** -Lists the site or user that generated the traffic. When the scope is an entire site, expect several hosts to be involved.

> [!NOTE]
> Tip:
> 
> If the anomaly affects a site, identifying a single source host may be challenging, and the anomaly could span multiple hosts.

![source.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424531262621.png)

## Step 2 - Analyzing the Origin of the Anomalous Events

### Anomaly Distribution

The **Anomaly Distribution** graph can help identify which firewall rule, IPS signature, or Anti-Malware rule generated the events that triggered the anomaly story. If multiple rules are involved, prioritize the ones that caused the largest spikes in events.

Event-based anomaly stories can originate from any Cato log source, Firewall, IPS, DNS Protection, CASB, DLP, Application Security, NGAM, and others, so the likely attack vector and your investigative approach should be adjusted to fit the specific event type.

Note the exact timestamp of the anomaly. This is critical for analyzing related events in later steps of the investigation.

![Scanner_Playbook_-_Anomaly_Distribution.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424506315037.png)

## Step 3 - Review Additional Widgets

Review these widgets for additional context. The widgets show top applications, servers, hosts, and targets involved in the anomaly. The data is aggregated over a 14-day period leading up to the anomaly story.

- **Top Applications** - Shows the applications with the highest event counts.

![Events_Anomaly_Playbook_-_Top_Apps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424531443357.png)
- **Top Servers/Destinations** - Shows the most accessed servers or networks.

![Events_Anomaly_Playbook_-_Top_Servers.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424539774493.png)
- **Top Hosts** - Shows the top source IP addresses generating the traffic.
- **Targets** - Shows the target destinations for the anomalous traffic.

> [!NOTE]
> Note:
> 
> These widgets provide a high-level overview and are not always indicative of the exact cause of the anomaly. For example, the widgets indicate that the anomaly involves TOR traffic, but without a specific destination IP. This may indicate broader TOR activity rather than a single malicious target.

## Step 4 - Analyze Related Stories

This step offers valuable context by identifying additional detections associated with the same behavior or the host/site where it was observed. Reviewing similar stories can help determine whether other hosts in the network triggered the same detection, potentially revealing a broader phenomenon affecting the environment.

![image-20250710-122158.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424569902109.png)

## Step 5 - Investigate Application Analytics and Events

Analyzing individual events is the most critical step in the investigation. It lets you drill down deeper into the anomaly to understand the root cause.

Review the relevant events to correlate data related to the story. Look for recurring elements such as specific source IPs, domains, and applications to focus your investigation. For example, if the anomaly is caused by TOR traffic, and a specific source IP or domain shows repeated activity, investigate that entity further.

The following are example steps for analyzing events related to an Events Anomaly story. For more about filtering and working with the Events page, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

1. Show the Events page pre-filtered for events related to the story by clicking View All on the story page.

![Events_Anomaly_Playbook_-_View_All.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424569971997.png)
2. On the Events page, configure the time range filter or use the mouse to select the time range that clearly shows an anomalous number of events.

![Events_Anomaly_Playbook_-_time_range.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424570047005.png)
3. Add relevant fields to the Events page. This provides a better perspective of the events involved in the anomaly. In the below example, these event fields were added to the page: **Signature ID**, **Application**, **Domain Name**, **Source IP**.

Check the added fields and attempt to identify the anomaly cause. In this example, the added event fields clearly show that the cause of the anomaly is a specific domain.

![Events_Anomaly_Playbook_-_Add_Fields.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424570146845.png)
4. Check the added fields and attempt to identify the anomaly cause. Look for recurring elements:

Compare traffic to organizational traffic:
  - Repeating source IPs / users
  - The same domain or destination across multiple events
  - Sudden appearance of an unfamiliar application or country.
  - Do other users have similar traffic patterns?
  - In case this is a first occurrence of suspicious behavior, is it something common within the organization? Was this behavior triggered for other hosts within the organization?
5. In the next step in this example, after identifying based on widgets and events that Tor Networks is the top used application, and that there are two main IPS threats that had a spike of events, filters are added for the specific Application and Threat Names.

![Events_Anomaly_Playbook_-_More_filters.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29424506859037.png)

The added filters reveal that this anomalous traffic relates to one specific source IP address.
6. Now further investigation steps can be taken:
  1. Check the Device Name or User Name correlated with this activity.
  2. Investigate the target and see if it is related to the malicious activity.
  3. Inspect traffic with the same characteristics for other users in the same site or network for broader context.

### File‑Sharing vs SMB Anomalies

The XOps engine groups file‑transfer events under a single umbrella, but cloud file‑sharing apps (e.g., Dropbox, SharePoint, S3) and SMB‑based file access expose different investigative data:

- **Cloud applications** – events show the application and volume only; object‑level details reside on the cloud platform itself
- **SMB traffic** – events include granular metadata, such as file name and path, enabling deeper forensic review.

### Investigation Tips and Use Cases

- In site-based anomalies there may be cases where there isn’t a specific host or destination and the anomaly is a broad phenomenon across the site.
- There may be cases where the application that caused the anomaly is not one of the top 5 applications generating anomalous events.
- There are cases when the anomaly is based on threat intelligence (Reputation) IPS events. In such a case, the investigation should be more target-focused, so you should use the following playbook: [XOps Security Playbook - Suspicious Target Communication](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings).
- In case you are not sure if a specific anomaly poses a security threat, try to observe if that traffic occurred in the same site or different sites in the past. This can help identify if the anomaly is simply caused by a new device.

## Conclusions from the Investigation

These are some examples of relevant conclusions for Events Anomaly stories:

- Anomalous Traffic
- Blocked Files Anomaly
- Blocked IPS Traffic Anomaly
- Exfiltration Attempt using {app name} Application
- Malicious Target Traffic Anomaly

## Recommended Actions

1. Perform a full endpoint protection scan (including Anti-Virus, EPP, EDR, etc.) and remove any unknown programs and browser extensions from the infected machine.
  - Make sure the removal process is thorough and all related components are identified and deleted.
2. If you identify a specific host or user as the source of the anomaly, isolate them from the network immediately to prevent further potential damage or data exfiltration.
3. If necessary, update or create rules for a more restrictive security policy, especially if the anomaly was caused by an application or traffic that should not have been allowed.
4. In case the story is a false Positive, you can classify it as Benign/Informational and also add it to a Mute Stories rule. If the story results from a legitimate scan or penetration test, it is recommended to add it to a Mute Stories rule for a specific time range.
