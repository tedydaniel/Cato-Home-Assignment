---
title: "Configuring Endpoint Protection"
slug: "configuring-endpoint-protection"
updated: 2026-06-22T09:27:06Z
published: 2026-06-22T09:27:06Z
canonical: "knowledge.catonetworks.com/configuring-endpoint-protection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Endpoint Protection

This article explains how to configure Cato's Endpoint Protection (EPP) solution to secure your endpoints.

## Overview

Cato's EPP solution includes three types of EPP engines: File Protection, which scans files on the endpoint; Behavioral Analysis, which scans processes running on the endpoint; and Anti-Exploit, which protects software vulnerabilities. Your EPP settings are configured in the Cato Management Application, providing a centralized way to manage security across your attack surface. In the **Endpoint Protection Profile**, you can configure the protection level of each engine to define how it responds to potential threats. Use the **Endpoint Protection Policy** to apply the **Endpoint Protection Profiles** to an end user or endpoint.

You can add a file or process to the **Allow List** to prevent legitimate files or processes from being identified as malicious, and for additional protection, you can run an on-demand scan on a specific endpoint.

> [!NOTE]
> Note:
> 
> Devices located in China are not able to register their EPP to Cato due to regional restrictions.

## EPP Engines

To protect your endpoint from known and unknown malware, Cato's EPP solution provides three layers of protection for a full security solution. Each layer utilizes different detection techniques to identify and prevent different types of attacks.

### Anti-Malware (File Protection)

The File Protection engine supports scanning of more than 300 file types, including archived files, ZIP files, and RAR. A file is scanned once it is downloaded or copied onto an endpoint as well as when an end user attempts to access it. You can also scan all files on an endpoint at any time with an on-demand scan.

### Behavioral Analysis

The Behavioral Analysis engine uses heuristics methods to protect against unknown and zero-day threats. Applications and processes are continuously monitored for indications of malicious activity based on their behavior. Examples of malicious behavior include:

- Executing or injecting code in another process’s space to run with higher privileges
- Accessing or executing illegal operations in registry locations that require elevated privileges
- Copying or moving files in System or Windows folders

### Anti Exploit

> [!NOTE]
> Note:
> 
> Supported from EPP v1.1 and above

The Anti Exploit engine uses machine learning to protect against known and unknown threats that take advantage of software vulnerabilities. System processes, browsers, Microsoft Office, and Adobe Reader are continuously monitored to detect techniques used to exploit software vulnerabilities. Examples of techniques that are detected include:

- Privilege escalation: Processes attempting to gain unauthorized privileges and access to resources
- Process introspection: Attempts to gather detailed information about running processes, system resources, memory usage, and other critical data
- LSASS credential dumping: Attempts to access the memory of the LSASS process and extract sensitive authentication credentials

### Responding to Threats

After an EPP engine identifies potentially malicious activity, the **Protection** settings define the action that EPP takes. In addition, for the Behavioral Analysis engine, you can define how sensitive it is for identifying unknown threats.

The following table describes each **Protection** level and an example use case for it.

| Protection | Description | Sample Use Case |
| --- | --- | --- |
| **Off** | EPP scans do not run, no events are created. | You do not want to use this EPP engine. |
| **Monitor** | An event is created if malicious activity is identified, but no further action is taken. | You want to collect data on malicious files or processes, without preventing their execution. |
| **Block** | A malicious file or process cannot be executed. The file is not modified or moved from its location. This is the default setting for the Behavioral Analysis and Anti Exploit engines. | You want to identify and block malicious files or processes. |
| **Block and Remediate** | The malicious file or process cannot be executed. The file is encrypted and quarantined or if this is not possible, the file is deleted. This is the default setting for the Anti-Malware. | You want to identify, block, and quarantine malicious files or processes. |
| **Kill** | Terminate the infected application process. | You want to kill the malicious process to avoid it continuing to run. |
| **Kill and Remediate** | Terminate the infected process and, if successful, clean malware traces. This may include reverting file changes, removing registry keys, uninstalling services, etc. | You want to kill the process and ensure that you remove any persistence. |
| **Kill Process** | Terminate the exploited application process and any possibly linked processes | Kill processes that injected code into the exploited process. |

#### Behavioral Analysis Heuristic Sensitivity Level

The Behavioral Analysis engine detects potential threats based on a predictive model and learning heuristics. The **Sensitivity Level** of the engine determines the confidence level that identifies the potential threats. For example, the **Aggressive** setting will identify processes with a low level of certainty that the process is malicious. This setting can result in more false-positive matches.

The following options table describes the **Sensitivity Level** and an example use case for it.

| Sensitivity Level | Description | Sample Use Case |
| --- | --- | --- |
| **Permissive** | Only detect processes that are determined to be malicious with a very high level of certainty. This is the setting with the lowest sensitivity. | You only want to detect processes that are certainly malicious. |
| **Balanced** | Detect processes that are determined to be malicious with a high level of certainty. | You want to detect processes that are likely malicious. |
| **Aggressive** | Detect processes that are determined to be malicious with a low level of certainty. This is the setting with the highest sensitivity. | You want to detect processes that are likely but not certainly malicious. |

## Configuring Endpoint Protection Settings

To define how EPP protects endpoints in your account, use the EPP **Profile** to define the level of Protection for each engine. Then use the rules in the EPP Policy to define the scope of endpoints that the **Profile** applies to. A **Profile** can be applied to specific end users, specific endpoints, or both.

EPP policies are an ordered rulebase. The rules in your policy are applied to files and processes sequentially to check if a rule is matched. Rules that are at the top of the rulebase have a higher priority because they are applied before the rules lower down. For example, if rule #1 has a File Protection **Block** response and applies to an endpoint where a malicious file is identified, the file is blocked. No further rules are applied to the file. The final default rule applies the Default Profile to all endpoints and cannot be edited.

### Defining an Endpoint Protection Profile

The EPP **Profile** defines the File Protection and Behavioral Analysis engine **Protection** settings. You can define different profiles based on the requirements for your EPP **Policy**.

![EPP_Profile.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318683919645.png)

**To define an Endpoint Protection Profile:**

1. From the navigation menu, click **Security > Endpoint Protection**.
2. Click the **Profiles** tab.
3. Click **New**.

The **Create New Endpoint Protection Profile** panel opens.
4. Define the settings for the profile.
5. Click **Apply** and then **Save**.

### Creating an Endpoint Protection Policy

Define the rules in the EPP **Policy** with the **Source** and the **Profile**. The Source can be an end user identity or an endpoint device based on the **Endpoint ID**. You can also set the level of protection **(Profile)** that is applied to each end user or endpoint **(Source)** . This lets you customize how each EPP engine is used on each endpoint across your environment.

![image3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318703217053.png)

**To create an Endpoint Protection Policy:**

1. From the navigation menu, click **Security > Endpoint Protection**.
2. Click **New**.

The **Create new Endpoint Protection Policy Rule** panel opens.
3. Define the **Name**, **Description**, **Source**, and **Profile** for this rule.
4. (**Optional**) Configure tracking options to generate **Events** and **Send Notification**

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
5. Click **Apply**.
6. Repeat steps 2-5 for each rule in the EPP Policy.
7. Enable the EPP Policy and click **Save**.

The slider (![slider.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318683954205.png)) is green when the EPP is enabled, and gray when the EPP is disabled.

## Allowing Files and Paths for EPP

Sometimes an EPP engine may consider a legitimate business process to be malicious. To prevent endpoint protection from interrupting legitimate business processes, you can allow an **Object** for an end user or on an endpoint **(Source)**. This means it is not scanned, blocked, or moved. For [On-demand scans](/v1/docs/configuring-endpoint-protection#running-an-ondemand-file-protection-scan) an event may be triggered with the mitigation action Ignore. No event is created for file scans.

The following objects can be allowed to execute for an end user, on an endpoint, or both:

> [!NOTE]
> Note:
> 
> File Paths are allowed by both the Anti-Malware and Behavioral Analysis engines. Other objects are only allowed by the Anti-Malware engine.

- File Path
- Folder Path
- File Type
- SHA256 File Hash

![2023-03-16_18-15-55.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318688120861.png)

**To define an Object for the Allow List:**

1. From the navigation menu, click **Security > Endpoint Protection**.
2. Click the **Allow List** tab.
3. Click **New**.

The **New Allow List** panel opens.
4. Define the **Name**, **Description**, **Object**, and **Source** to be allowed.
5. Click **Apply**.
6. Repeat steps 3-5 for each **Object** that you are allowing.
7. Click **Save**.

## On-demand File Protection Scans

File Protection scans run when a file is downloaded or copied onto an endpoint as well as when an end user attempts to access it. In addition, you can run a File Protection scan on an endpoint on-demand at any time. By running an on-demand File Protection scan, you can identify existing malware on an endpoint before the end user tries to access it.

On-demand scans compare the SHA256 file hash of all files saved on the endpoint with a list of known malware signatures. If a malicious file is detected, EPP follows the action defined by the Policy.

### Running an On-demand File Protection Scan

You can identify malicious files on an endpoint at any time by running an On-demand scan. These scans do not run after the agent is installed, they only run after being trigged from the Cato Management Application.

**To run an on-demand File Protection Scan**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** screen is displayed.
2. Click the three dots (![Three_Dots.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30318703268765.png)) on the endpoint that you want to scan.
3. Click **Scan Endpoint**.

A File Protection scan runs on the endpoint.

## Testing the EPP Solution

After installing the EEP agent on your endpoints, you can test the solution to ensure it prevents malicious activities based on your policy configuration.

**To test the EPP solution:**

1. On an endpoint with the agent installed, download and try to run an [EICAR test file](https://www.eicar.org/download-anti-malware-testfile/).
2. Try to open and run the file.

**Note**: If downloading the file is blocked by your network security solution or browser, copy the text in the EICAR file, paste it into a new .txt file and save.
3. If the EPP solution is installed and enabled correctly, the behavior of the file is in accordance with your configured policies and an event is created.

## Understanding the Frequency of Database Updates

When an EPP engine scans a file or process it is compared to a database of known malicious activity. These databases are regularly updated automatically to ensure the EPP engines protect against the latest threats.

The status of the database update is visible on the **Status** tab of the EPP agent.

The frequency of the database updates are:

- **Malware DB**: Every 1 hour
- **CTC DB:** Every 24 hours (this database is used for Cross-engine corrections)
- **Behavioral DB:** Every 2 hours
- **Exploit DB:** Every 2 hours

A database containing a list of known legitimate files which do not require scanning is updated every 4 hours.
