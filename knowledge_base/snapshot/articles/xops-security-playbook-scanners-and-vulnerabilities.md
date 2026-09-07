---
title: "XOps Security Playbook - Scanners and Vulnerabilities"
slug: "xops-security-playbook-scanners-and-vulnerabilities"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-security-playbook-scanners-and-vulnerabilities"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Security Playbook - Scanners and Vulnerabilities

This playbook describes how to use the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) to investigate stories based on vulnerabilities and scanning activities.

## Overview

This playbook outlines a systematic approach for SOC engineers to investigate potential security incidents related to scanning activities and vulnerabilities. It provides a framework for gathering initial information, analyzing network traffic, and drawing conclusions about the nature of the threat.

The playbook helps you identify the different stages of an attack across the network for attacks based on scanning activity and vulnerability exploitation. These are some of the tactics commonly associated with these attacks:

- Reconnaissance
- Initial access
- Privilege escalation
- Lateral movement
- Exfiltration

### Identifying Scanners and Vulnerability Stories

The XOps engines identify scanner and vulnerability stories mostly based on IPS signatures that match specific threat behaviors. Understanding the behavior that triggered the story gives you a better idea of how to investigate it. The following table shows the formats for different IPS signatures for these types of stories, and describes the potentially malicious behavior that matches the signature.

| IPS Signature | Explanation |
| --- | --- |
| cid_cve_* | Vulnerabilities with CVE identifier |
| cid_vuln_* | Vulnerabilities without CVE identifier |
| cid_scan_* | For network scanners |
| cid_waf_* | For network scanners and vulnerabilities directed to web services |
| feed_cid_cve_* | For specific vulnerability-related threat intelligence sources |
| feed_threat_scanner* | For inbound traffic associated with IPs that were classified as Threat Scanners |

## Investigation Workflow

This section explains the investigation workflow for identifying an attack that originated from a scanning activity or vulnerability exploitation attempt.

### Step 1 - Gathering Initial Information about the Threat

Use the **Details** widget in the story to gather basic information about the potential threat. Review the **Description** of the story. This can help focus the investigation based on the logic that generated the story. In addition, the **Similar Stories** section shows other stories that share similar indicators and observables.

![Playbook.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977992758173.png)

To decide if further investigation is required, review additional data, for example:

- **Direction:** This impacts the investigation process, for more information see [Step 3 - Investigating According to the Direction](/v1/docs/xops-security-playbook-scanners-and-vulnerabilities#step-3-investigating-according-to-the-direction).
- **Source/Target:** This tab displays data about the impacted devices.

**Note:** For inbound stories, the **Target** refers to the affected host, while the **Source** refers to the investigated object located outside of Cato. This can occasionally be caused by devices or sites that are not set up as part of the Cato network, or by configuration errors.
- **Indication Catalog:** This can help understand the logic of the indication.

### Step 2 - Identifying the Type of Threat

In a **Scanner Story** you can identify the type of scanner based on the signature that triggered the story and the application indicated in the signature. These can be associated with a specific type such as Nessus, or Qualys, or based on a generic service/application and amount of traffic.

![image-20240208-152524.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977983928221.png)

In a **Vulnerability Story** the references in the events help you understand the vulnerability and focus the investigation on the relevant IOCs.

![image-20240208-154338.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978020830493.png)

The **Threat Reference** field in the event provides the link to look up the threat in the National Vulnerability Database.

![Playbook_Scanners_and_Vulnerabilities_-_Vul_Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978003309597.png)

### Step 3 - Investigating According to the Direction

The **Direction** of the story impacts the next steps in the investigation:

#### Inbound Scan / Vulnerability Story

The purpose of this stage of the investigation is to identify and verify the possibility of an Information Gathering / Infiltration attempt by an external adversary.

In the **Sources** table, examine the identified sources to ascertain their potential malicious intent:

- **Analysis of Table Parameters for Risk Evaluation**: Evaluate parameters such as the malicious score, popularity, associated categories, and the number of threat intelligence feeds associated with the source to determine the likelihood of the source being malicious.
- **Use Source Links for External Search:** Perform an external search using the source links on reputable third-party search engines and security databases. Look for any historical context, associations, or indicators of malicious behavior linked to the source. Correlate the gathered data to identify connections between the sources and other entities and try to determine if there are any links to known threat actors, campaigns, or techniques.
- **Attack Related Flows/Events:** Use the designated table to inspect the unprocessed data flow samples corresponding to the triggered story. Analyze supplementary data points from the flows, such as URLs, user agents, file names, and additional relevant attributes, and compare these parameters against the findings from the previous investigation steps and gain insights regarding the final verdict of the communicating source.

After understanding the type of threats based on the related events of the story it is important to drill down to the related events to get additional insights regarding the traffic. For example:

- Verifying the traffic and classifying it as a true positive or true negative based on the signature’s reference correlating with the data found in the events.
- Understanding the scope of the threat:
  - Check for additional traffic from the communicating source in to understand if this communication is new, or seen before.
  - Check for additional sources with similar traffic characteristics (application, destination port)

![SourceIP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978014450461.png)
  - Check for additional targets/hosts that were communicated by the investigated source

![Destination.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978003452829.png)
  - Check for differences between the events such as different URLs, destination ports, request method, etc.

![URL.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978021121565.png)
  - Check if the traffic was blocked based on the Action field

![Action.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978021196445.png)

**Conclusion**

For Scanner Investigations, there are multiple classifications of known scanners and scanning methods such as:

- Nessus
- Nmap
- Xmas
- Ping Sweep

For Vulnerability investigations, there are classifications of known vulnerabilities such as:

- SQL Injection
- Cross-Site Scripting Injection (XSS Injection)

If the specific vulnerability in the story does not exist on the classification list, you can add it locally to your account by clicking on **New** and filling in the relevant fields.

In case the story is a true positive and was not blocked, it is highly recommended to add the investigated sources to the RPF policy blocklist. For more information, see [Configuring Remote Port Forwarding for the Account](/v1/docs/configuring-remote-port-forwarding-for-the-account).

In case the story is a false positive, you can classify it as Benign/Informational and also add it to a Mute Stories rule. (If the story results from a legitimate scan/penetration test it is recommended to add to a Mute Stories rule for a specific time range.)

#### Outbound Scan / Vulnerability Story

The purpose of the investigation is to identify and verify possible cases of exfiltration, Command & Control traffic, botnet activity, etc.

In the **Targets** table, examine the identified targets to ascertain their potential malicious intent:

- **Analysis of Table Parameters for Risk Evaluation:** Evaluate parameters such as the malicious score, popularity, associated categories, and the number of threat intelligence feeds associated with the target to determine the likelihood of the target being malicious.
- **Use Target Links for External Search:** In cases of outbound scanning activity, the target investigation can be difficult as most of the communicated targets are not recognized by many if any security engines and lack external data.

However, it is recommended to use external sources to find as much context as possible using any historical context, associations, or indicators of malicious behavior linked to the target. Correlate the gathered data to identify connections between the targets and other entities and try to determine if there are any linkages to known threat actors, campaigns, or techniques.
- **Attack Related Flows/Events:** Use the designated table to inspect the unprocessed data flow samples corresponding to the triggered story. Analyze supplementary data points from the flows, such as destination ports, applications, URLs, user agents, destination countries, and additional relevant attributes, and compare these parameters against the findings from the prior investigation and gain insights regarding the final verdict of the communicating target.

After understanding the type of threats based on the related events of the story it is important to drill down to the related events to get additional insights regarding the traffic. For example:

- Verifying the traffic and classifying it as a true positive or true true negative based on the signature’s reference correlating with the data found on events.
- Understanding the scope of the threat:

**Conclusion**

For scanner Investigations, there are multiple classifications of known scanners and scanning methods such as:

For Vulnerability investigations, there are classifications of known vulnerabilities such as:

In case the specific vulnerability that was found for the story doesn't exist on the classification list, you can add it locally by clicking on **New** and filling in the relevant fields.

In case the story is a true positive and was not blocked, it is highly recommended to add the investigated targets to an Internet firewall block rule. In addition, for cases where the IPS signature is allowlisted, it is recommended to block it using the a firewall rule or editing the IPS allow rule to include only known targets.

In case the story is a false positive, you can classify it as Benign/Informational and also add it to a Mute Stories rule. In case the story results from a legitimate scan/penetration test it is recommended to add to a Mute Stories rule for a specific time range.
  - Check for additional traffic from the communicating target to understand if this communication is new, or seen before.
  - Check for additional targets with similar traffic characteristics (application, destination port)

![Destination2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978000237341.png)
  - Check for additional targets/hosts that were communicated to by the investigated target
  - Check for differences between the events such as different URLs, different destination ports, request method, etc.

![Destination4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978000354077.png)
  - Check if the traffic was blocked based on the Action field
  - ICMP Scan
  - SYN Scan
  - SMTP Scan
  - SQL Injection
  - Cross-Site Scripting Injection (XSS Injection)

#### WANbound Scan / Vulnerability Story

The purpose of the investigation is to identify and verify possible cases of exfiltration, lateral movement, privilege escalation, etc.

The **Targets** table can provide visibility for all communicated targets.

Utilize the table to inspect the unprocessed data flow samples corresponding to the triggered story. Analyze supplementary data points from the flows, such as URLs, user agents, file names, and additional relevant attributes, and compare these parameters against the findings from the previous investigation steps and gain insights regarding the final verdict of the communicating source.

After understanding the type of threats based on the related events of the story it is important to drill down to the related events to get additional insights regarding the traffic. For example:

- Verifying the traffic and classifying it as a true positive or true negative based on the signature’s reference correlating with the data found on events
- Understanding the scope of the threat:

For scanner investigations, there are multiple classifications of known scanners/scanning methods such as:

For Vulnerability investigations, there are classifications of known vulnerabilities such as:

In case the specific vulnerability that was found for the story doesn't exist on the classification list, you can add it locally by clicking on **New** and filling in the relevant fields.

In case the story is a true positive and was not blocked, it is highly recommended to add the investigated targets to a WAN firewall block rule. In addition,for cases where the IPS signature is allowlisted, it is recommended to block it using a firewall rule or by editing the IPS allow rule to include only known targets.

In case the story is a false Positive, you can classify it as Benign/Informational and also add it to a Mute Stories rule. If the story results from a legitimate scan or penetration test it is recommended to add it to a Mute Stories rule for a specific time range.
  - Checking for additional traffic from the communicating source to understand if this communication is new, or seen before
  - Checking for additional sources with similar traffic characteristics (application, destination port)

![Source_IP3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978014957597.png)
  - Checking for additional targets/hosts that were communicated to by the investigated source

![Destination_IP9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978000503325.png)
  - Checking for differences between the events such as different URLs, different destination ports, Request Method, etc.

![URL5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28978003985949.png)
  - Checking if the traffic was blocked based on the Action field
  - Nessus
  - Nmap
  - Xmas
  - Ping Sweep
  - SQL Injection
  - Cross-Site Scripting Injection (XSS Injection)
