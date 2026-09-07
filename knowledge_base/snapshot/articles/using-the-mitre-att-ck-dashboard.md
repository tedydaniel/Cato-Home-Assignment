---
title: "Using the MITRE ATT&CK® Dashboard"
slug: "using-the-mitre-att-ck-dashboard"
updated: 2026-06-29T06:50:46Z
published: 2026-06-29T06:50:46Z
canonical: "knowledge.catonetworks.com/using-the-mitre-att-ck-dashboard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the MITRE ATT&CK® Dashboard

This article discusses how to use the MITRE ATT&CK® Dashboard to get an overview of the threat tactics and techniques in your network.

## Overview of the MITRE ATT&CK® Dashboard

The MITRE ATT&CK® Dashboard maps the threats identified by the Cato IPS service to tactics and techniques that are presented in the MITRE ATT&CK® Matrix. This provides a powerful framework for analyzing threats and identifying the various phases of attacks. MITRE ATT&CK® tactics are the high-level goals in an attack vector, while techniques are specific methods used to accomplish these goals.

The dashboard contains a number of widgets that provide visibility and analytics including:

- Summary of tactics identified in your network, with the number of events for each tactic
- Breakdown of techniques for each tactic
- Most common techniques identified in your network
- Device distribution for each technique
- Time distribution of identified tactics
- Sources in your network that generated the most security events

### Getting Started with the MITRE ATT&CK® Dashboard

The MITRE ATT&CK® Dashboard widgets present a summary of the attack tactics and techniques identified in your network. You can also drill-down to see granular details and analysis for each technique, or view the Events screen pre-filtered for a tactic or technique.

By default, the dashboard shows data for IPS [Monitor](/v1/docs/configuring-the-ips-policy) events (including [Suspicious Activity](/v1/docs/monitoring-suspicious-activity-with-ips-sam) events) and Block events. For a more focused analysis, you can filter the dashboard to only show data for **Monitor** events, or **Block** events.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/mitre.png)

**To show the MITRE ATT&CK® Dashboard:**

- From the navigation menu, click **Security > Threats Dashboard** and select the **MITRE ATT&CK** tab.

For more information about using the dashboard, see [Configuring Filters to Analyze Dashboard Data](/v1/docs/configuring-filters-to-analyze-dashboard-data) and [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter). The maximum date range for the dashboard is 90 days.

## Working with MITRE ATT&CK® Dashboard Widgets

This section explains the widgets that are available in the MITRE ATT&CK® Dashboard. The data shown in the dashboard is based on the configured time range.

These are the widgets:

- Tactics summary - The top row of the dashboard shows the tactics identified in your network, with the number of events generated for each tactic. Tactics are shown according to phases in the attack lifecycle, following the left-to-right arrangement in the MITRE ATT&CK® Matrix.
- Technique breakdown - The left-hand pane shows the techniques used for each tactic, with the number of events for each technique. Click the row of a technique to open the **Details** panel containing the following information and widgets:

![MITRE_Details.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275718862749.png)
  - Basic description of the tactic and technique according to the MITRE ATT&CK® definitions
  - Attacks Over Time - Time distribution of attacks using this technique. Click and drag to zoom-in on:
    - Time of events
    - Number of events
  - Top Sources - Shows a list of the top sources for the technique, with the number of MITRE ATT&CK® events for each source. Click the source row to open the Events screen pre-filtered for the technique and source.
  - Device distribution - The bottom row shows OS icons with the number of events generated for the technique on each OS
- Top Techniques - Shows a list of the top MITRE ATT&CK® techniques with the number of events for each one. Click a technique name to open the Events screen pre-filtered for that technique.
- Tactics Distribution Over Time - Graphs the events for each tactic on a timeline.

![MITRE_Tactics_Time_Widget.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275702126365.png)
  - Hover the mouse on the graph to show a summary of events for a point on the timeline
  - Click the toggle button of a tactic to turn its graph on or off
  - Click a tactic name to open the Events screen pre-filtered for the tactic
  - Click and drag to zoom-in on:
    - Time of events
    - Number of events
- Top Security Events - Sources that generated the most overall security events, including MITRE ATT&CK® and other event types. The MITRE Techniques column shows the top technique identified for a source.
  - Hover the mouse on a number in the MITRE Techniques column to show additional techniques for the source.
  - Click in the row of a source to open the Events screen pre-filtered for the source.

## Sample Threat Analysis with the MITRE ATT&CK® Dashboard

After the IPS service blocks an attack, you can analyze it with the MITRE ATT&CK® Dashboard and take actions to stop similar future attacks at an earlier stage. This is an example of a threat analysis and possible actions:

1. The left-hand pane shows 80 Phishing events under the Initial Access tactic.
2. In the Details panel for the Phishing technique, the Top Hosts widget shows that one user generated 25 of the events, and a second user generated 20.
3. The bottom row of the Details panel shows that 60 of the events were generated by Windows devices, and 20 by Android devices.
4. Investigate the two problematic users to find out why they are vulnerable to these attacks.
5. Educate and train the users to avoid phishing attacks in the future.
6. Verify that all Windows and Android devices on your network have the required security updates.

## License Information

### MITRE License

The MITRE Corporation (MITRE) hereby grants you a non-exclusive, royalty-free license to use ATT&CK® for research, development, and commercial purposes. Any copy you make for such purposes is authorized provided that you reproduce MITRE’s copyright designation and this license in any such copy.

© 2022 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.

### Disclaimer

The information on this application is for general informational purposes only. Your use of the application is solely at your own risk. This application may contain links to third party content, which we do not warrant, endorse, or assume liability for. Cato Networks make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the application or the information, services, or related graphics contained on the application for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

In no event will Cato Networks be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this application.
