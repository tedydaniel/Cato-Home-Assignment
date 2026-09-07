---
title: "Monitoring and Responding to Endpoint Protection Threats"
slug: "monitoring-and-responding-to-endpoint-protection-threats"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/monitoring-and-responding-to-endpoint-protection-threats"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring and Responding to Endpoint Protection Threats

This article explains how to monitor and respond to threats identified by Cato's Endpoint Protection (EPP) engines.

## Overview

To increase your awareness of potential threats for your endpoints and endusers, you can view and analyze details of potential threats to determine how to respond. If potentially malicious activity is identified by an EPP engine, an **Event** is created containing the relevant information. The EPP events provides key information about the identified threat for example, the endpoint the threat occurred on, the time and date of the threat, and the name of the file that triggered the event. For more information about analyzing events, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network)

You can also view and overview of threats detected by EPP in your network from the [Endpoint Protection Dashboard.](/v1/docs/using-the-endpoint-protection-dashboard)

Files that are identified a malicious can be encrypted and quarantined, depending on your protection settings. You can view quarantined files and if considered safe, restore them to their original location.

## Identifying Endpoint Protection Threats

You can view all the events triggered by endpoint protection within a defined timeframe. The **Engine Type** field provides information about which engine triggered the event.

> [!NOTE]
> Note:
> 
> An event can take 6 minutes to be created after a file is blocked.

**To identify threats on your endpoints:**

1. From the navigation menu, click **Home > Events**.
2. In the events filter bar, click the **Presets** icon.
3. From the **Predefined Presets** list, select **Endpoint Protection**.

The threats identified by EPP are displayed.

### Understanding Event Fields

The following table lists the event fields in a EEP Malware event.

| Field Name | Description |
| --- | --- |
| Action | Action that is relevant to the event type that EPP tried to take. |
| Mitigation Actions Taken | Action taken by EPP. Mitigation actions are: - **Deny:** The SDP user is denied access to the file - **Disinfect Only:** The malicious content identified in the file is removed. If this fails, the file remains in its current location - **Disinfect delete:** The malicious content identified in the file is removed. If this fails, the file is deleted - **Delete:** The file is deleted - **Move to quarantine:** The file is moved to quarantine - **Ignore:** No action is taken Mitigation actions are defined by the EEP Profile. For more information, see [Configuring Endpoint Protection](/v1/docs/configuring-endpoint-protection). |
| Actions Taken | List of all actions taken. For example, the EPP tried to quarantine a file, the action failed, then the EPP tried to delete the file. Actions taken are: `[Quarantine, Delete]` |
| Client Version | Version number of EPP. |
| Device Name | Computer name of the endpoint. |
| Endpoint ID | Unique ID of the EEP agent. |
| Engine Type | Engine that detected the threat. |
| Endpoint Protection Profile | EEP profile on the endpoint. |
| Event Count | Count for events that are repeated multiple times during one minute. |
| Sub-Type | Sub-Type category of the event. |
| Event Type | Category of the event. |
| File Hash | File hash of the suspicious file. |
| File Name | File path and name of suspicious file. |
| File Operation | Action the enduser took to trigger the event. |
| Final Object Status | The final status of a file after all actions are taken (or attempted to be taken) SCAN_FAILED means the EPP was unable to scan the file |
| ISP Name | ISP the endpoint is connected to. |
| Logged In User | Enduser logged in at the time of the event. |
| Object Name | File path and name of suspicious file. |
| OS Type | Endpoint operating system. |
| OS Version | Endpoint operating system version. |
| User SID | SID of the endpoint. |

## Quarantining Files

If your **Protection** setting is set to **Block and Remediate**, EPP encrypts and quarantines malicious files. This prevents the enduser from accessing the file and prevents harmful processes from running on the endpoint. Quarantining potential threats ensures your endpoints remain secure and reduces the risk of infection across your environment.

You can monitor quarantined files and restore them to their original location if they are safe.

### Monitoring Quarantined Files

You can monitor the files that have been quarantined on each endpoint.

**To review quarantined files:**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** table is displayed.
2. In the **Quarantine Files** column, click the number of the endpoint that want to view the quarantined files of.

The quarantined files on the endpoint are displayed.

> [!NOTE]
> If the **Quarantine Files** column is blank, no quarantined files have been found on the endpoint

### Restoring Quarantined Files

If a file has been mistakenly quarantined error or if you consider the file to be safe, you can restore it to the original location on the endpoint. The enduser can then access the file. After a file is restored from quarantine, it is added to the Allow List.

**To restore quarantined files:**

1. From the navigation menu, click **Access > Protected Endpoints**.

The **Protected Endpoints** table is displayed.
2. In the **Quarantine Files** column, click the number of the row of the endpoint you want to restore a quarantined file from.

The **Quarantine** table is displayed.
3. On the file you want to restore, click on the three dots at the end of the table.
4. Click **Restore**.

The file is restored to its original location.
