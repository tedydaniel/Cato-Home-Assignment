---
title: "Monitoring Suspicious Activity with IPS (SAM)"
slug: "monitoring-suspicious-activity-with-ips-sam"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/monitoring-suspicious-activity-with-ips-sam"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Suspicious Activity with IPS (SAM)

This article explains how to use the Suspicious Activity Monitoring (SAM) feature with the IPS service to increase awareness of potential threats on your network.

## Overview of the SAM Service

Cato's SAM feature expands the IPS service to provide visibility for suspicious activities on your network that aren't monitored by standard IPS signatures. This type of traffic represents actions taken over the network that warrant attention, and depending on context could point to a compromise or breach. However, since the traffic is not definitely malicious, SAM only monitors the traffic without blocking it. The broader view of potential threats that SAM provides can help you identify all phases of an attack, and be better prepared for detection and defense against future similar attack vectors.

You can view and analyze suspicious activity data in the [Threats Dashboard](/v1/docs/using-the-security-threats-dashboard), [MITRE ATT&CK® Dashboard](/v1/docs/using-the-mitre-att-ck-dashboard), and [XDR Stories Dashboard](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench), and review SAM events in the [Events](/v1/docs/analyzing-events-in-your-network) page.

### What is SAM?

The Cato Security Research team creates specific signatures for unusual behavior patterns that look suspicious. The SAM service detects traffic that matches these signatures, and generates events and data that SOC teams can analyze to track and investigate threats. SAM events are labeled with the **Suspicious Activity** Sub-Type, to differentiate between malicious IPS events and possibly legitimate unusual traffic.

SAM monitors all WAN, inbound, and outbound traffic for your account, IPS **Protection Scope** settings do not affect SAM.

These are examples of scenarios that generate SAM events:

- Outbound HTTP traffic exfiltrating system information
- HTTP requests to low popularity destinations using non-standard HTTP ports
- A programmatic HTTP client downloading a binary or executable file
- Transfer of an executable to a sensitive folder over the WAN

### Understanding SAM Risk Levels

The SAM feature classifies events into different risk levels: **High**, **Medium**, and **Low**. Cato calculates the risk level based on analysis of a number of factors, for example:

- The prevalence of the activity in all traffic across the Cato Cloud. The lower the prevalence, the more likely the activity is malicious
- The MITRE ATT&CK® techniques associated with the activity

The risk level helps you assess the traffic and focus your analysis on the events most likely to be part of an attack. Additionally, high risk SAM events automatically generate an XDR story, which can be investigated in the Stories Workbench.

### Prerequisites

- SAM is included in the IPS license. For more about purchasing the IPS license, please contact your Cato representative.
- The IPS policy must be enabled before you can enable SAM.

> [!NOTE]
> **Note:**
> 
> We recommend that you enable TLS inspection so that the IPS service and SAM enhancement provide the maximum protection for your network.

## Understanding the Use Cases for SAM

To derive the maximum benefit from SAM, we recommend incorporating a review of SAM events as part of the regular security procedures for your network. For example, you can implement the review of SAM events in the following use cases:

- Routine review of the high risk SAM events to detect and prevent potential attacks
- Analyze SAM events after a confirmed attack to provide broader context as part of the forensic investigation

## Reviewing Suspicious Activities with SAM

Cato provides a number of ways to discover and investigate the suspicious activities detected by SAM. These different resources can be used together to gain thorough visibility and build context for the suspicious activities on your network. These resources include:

- XDR Stories Workbench - SAM events serve as a basis for XDR stories in the Stories Workbench. Reviewing the stories in the workbench can alert you to suspicious activities that might be part of an attack. For more about using the Stories Workbench, see [Reviewing Detection & Response (XDR) Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).

![SAM_Stories_Dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303182150941.png)
- Threats Dashboard - Review SAM event data by filtering the dashboard to focus on SAM events. See below [Viewing SAM Data in the Threats Dashboard](/v1/docs/monitoring-suspicious-activity-with-ips-sam#viewing-sam-data-in-the-threats-dashboard)

![SAM_Threat_Dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303143521181.png)
- MITRE ATT&CK Dashboard - You can set the dashboard to show data for IPS Monitor events including SAM events. See below [Analyzing SAM Data in the MITRE ATT&CK® Dashboard](/v1/docs/monitoring-suspicious-activity-with-ips-sam#analyzing-sam-data-in-the-mitre-attck®-dashboard)

![SAM_MITRE_Dashboard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303182318877.png)
- Events page - Filter the page to show SAM events (subtype: **Suspicious Activity**). When you select the **Suspicious Activity** preset filter, by default the page shows only high risk SAM events. You can add filters to focus on specific SAM events such as events with a source or destination of interest. For more about SAM events, see below [Reviewing SAM Events](/v1/docs/monitoring-suspicious-activity-with-ips-sam#reviewing-sam-events).

The Threats Dashboard, MITRE ATT&CK Dashboard, and Stories Workbench all let you drill-down and review details in the Events page.

## Working with SAM

This section explains how to configure the SAM service.

![Suspicous_Activity_Tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303182402589.png)

### Enabling and Disabling SAM

By default, SAM is enabled for your account. The **Suspicious Activity** tab on the IPS page lets you change this setting.

**To enable or disable SAM for your account:**

1. From the navigation menu, click **Security > IPS**.
2. Select the **Suspicious Activity** tab.
3. Click to enable or disable **Suspicious Activity Monitoring** for the account.
4. Click **Save**.

### Viewing SAM Data in the Threats Dashboard

The Threats Dashboard page lets you analyze suspicious activities in your network. You can set the widgets in the **IPS** section to show suspicious activity, and then filter the dashboard to show the data for specific SAM threat types, and relevant hosts and users. You can also view SAM events on the Events page, pre-filtered for threat type, host, and user.

For more about how to filter the dashboard and view events from the Threats Dashboard widgets, see [Using the Security Threats Dashboard](/v1/docs/using-the-security-threats-dashboard).

**To view Suspicious Activity Data in the Threats Dashboard:**

1. From the navigation menu, select **Security > Security Threats**.
2. Under the **IPS** section, in the **Event Type** drop-down menu, select **Suspicious Activity**.

The widgets now show SAM data.

### Analyzing SAM Data in the MITRE ATT&CK® Dashboard

The MITRE ATT&CK® Dashboard helps you analyze suspicious activities using the MITRE ATT&CK® framework of tactics and techniques. You can set the dashboard to show data for IPS Monitor events including SAM events. For more about using the MITRE ATT&CK® Dashboard, see [Working with the MITRE ATT&CK® Dashboard](/v1/docs/using-the-mitre-att-ck-dashboard).

### Allowlisting Suspicious Activity Traffic

If you want to stop logging events for specific traffic, you can allowlist that traffic in the **IPS Allow List** page. To allowlist suspicious activity traffic, create an IPS Allow List rule using the **Signature ID** of the traffic you want to stop monitoring. You can also allowlist suspicious traffic by clicking the Signature ID of an event on the Events page. For more information, see [Allowlisting IPS Signatures](/v1/docs/allowlisting-ips-signatures).

### Reviewing SAM Events

You can review Security events in **Home > Events** and find the unusual behaviors and potential threats detected by SAM. These events are labeled with the Sub-Type **Suspicious Activity**, which lets you distinguish them from the higher risk events generated with the **IPS** Sub-Type.

You can select the **Suspicious Activity** preset filter from the **Select Presets** drop-down menu to show the relevant events. By default, when you select this preset the page is filtered to show the high risk SAM events. To view all SAM events, remove the **Risk Level is High** filter.

The **Suspicious Activity** Sub-Type is limited to 2,500,000 events per hour. See [Cato Cloud Thresholds and Limits](/v1/docs/cato-cloud-thresholds-and-limits).

This is an example analysis of a high risk SAM event:

![SAM_Event_update.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303182477469.png)

- The **Threat Name** provides a basic explanation of what occurred in this event - an executable was moved laterally using PsExec
- The **Mitre Attack Tactics** and **Mitre Attack Subtechniques** fields show an execution using a remote service and lateral movement over SMB to an ADMIN$ shared folder
- The fields detailing the source and destination help you pinpoint the network hosts involved. With this information you can:
  - Confirm that the source host for the event has the required privileges to use PsExec
  - Confirm that the end-user associated with the event is likely to perform the detected actions
