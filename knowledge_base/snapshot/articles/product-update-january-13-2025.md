---
title: "Product Update - January 13, 2025"
slug: "product-update-january-13-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-january-13-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - January 13, 2025

## New Features & Enhancements

- **Introducing Audit Activities via SaaS App APIs:** We are expanding our CASB offering to include in-depth visibility into user activities in SaaS apps [via out-of-band API connectors](/v1/docs/application-control-via-api-with-app-activities). Connecting SaaS apps to Cato lets you understand who is accessing each app and identify suspicious activities or trends even when users are not connected to the Cato Cloud.
  - **New Activity Categories:** User activities are automatically classified into predefined Activity Categories to easily understand the actions of each app
  - **Supported Apps in the Catalog:** Microsoft Exchange, Microsoft SharePoint, Microsoft OneDrive for Business, Salesforce, Atlassian (Jira and Confluence), Egnyte, and Zendesk
  - This feature requires a CASB license
  - Click [here](https://academy.catonetworks.com/casb-via-apis) to watch a video recording of this feature
- **Enhanced Cloud Activity Dashboard**: We rebuilt the Cloud Activity Dashboard to provide centralized and comprehensive visibility of user activities in the SaaS apps used in your ecosystem. This lets you detect any anomalies, ensure compliance, and streamline incident response from a single dashboard. Events are unified from both Application Control (inline via the Cato Cloud) and the new Audit Activities APIs to consolidate all data into a single, easy-to-navigate interface.
  - The dashboard contains data from multiple features to let you monitor:
    - User activity in shadow IT and sanctioned apps
    - Every activity from unmanaged and managed users
    - Logins to sanctioned apps (currently supported for EntraID)
  - This feature requires a CASB license
  - Click [here](https://academy.catonetworks.com/cloud-activities-dashboard) to watch a video recording of this feature
- **DNS Sinkhole for Visibility into Infected Devices:** The DNS Sinkhole feature for DNS Protection intercepts DNS requests attempting to connect to malicious or suspicious domains and returns a designated sinkhole IP address. This protects users and the network while helping admins gain visibility into infected devices.
  - The **Sinkhole** action is available for each protection in the **Security > DNS Protection** page
  - The feature exposes the **Source IP** address in events for the relevant DNS Protection rule
  - Click [here](https://academy.catonetworks.com/dns-sinkhole) to watch a video recording of this feature
- **Mitigate Threats with Cato XDR:** The [XDR Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) lets admins perform mitigation actions for security threats directly from the story drill-down page. The admin can revoke the session of a remote user and force them to reauthenticate to the Client, for example, if a phishing attempt is detected.
  - The **Revoke User Session** option is available in the **Actions** menu in Security stories
  - Click [here](https://academy.catonetworks.com/xdr-mutation-api) to watch a video recording of this feature
- **Customize Machine Learning DLP Classifiers with Private Files:** Over the next few weeks, we are gradually releasing an enhancement to protect your company’s confidential documents and reduce false positives by using your own files to train a custom machine learning Data Classifier. This feature improves the precision and overall efficacy of the DLP engine by tailoring it to your unique needs.
  - Upload samples of document types you want to protect
  - Leveraging an advanced data science model, the classifiers identify similar documents in real time, preventing unauthorized exfiltration of sensitive files
  - Click [here](https://academy.catonetworks.com/custom-dlp-ml-classifiers) to watch a video recording of this feature
- **Device Checks Applied on macOS Devices Behind a Site**: To enforce device compliance requirements behind a site, Device Posture Profiles are applied to macOS devices behind a Socket. This lets you apply the same Device Posture Profiles, regardless of the device's physical location.
  - Supported from macOS Client version 5.8
- **Near-Real-Time DEM Experience Score and Metrics:** We've optimized our infrastructure to deliver near-real-time DEM Experience scores and metrics that should be updated within a few minutes.
- **Last-Mile Bandwidth Supports Kbps:** You can now set bandwidth values that include one decimal point (e.g. 1.5 Mbps) for more granular accuracy. This is useful for low-capacity Internet lines, such as E1 links.
  - You can configure this via the CMA and the following APIs:
    - LastMileBwInput
    - InterfaceInfo
    - SocketInterfaceBandwidthInput
  - Click [here](https://academy.catonetworks.com/last-mile-bandwidth-in-kbps) to watch a video recording of this feature
- **Enhancements to Connectivity Events and Health Alerts:** In the coming weeks, we’re adding improvements to Connectivity events and Link Health alerts. This includes an optimized email layout for better readability and several bug fixes that may result in a change in the frequency of Connectivity events and Link Health alerts.
- **Mutation API Support for XDR:** Save time and automate work processes with a new mutation API for XDR stories. You can set story verdicts, change status, and add comments via API. For more information, see this article. We recommend that you click **Follow** to automatically receive email notifications for updates to this article about changes to the API.

## PoP Announcements

- **New IP Range Owned by Cato 199.27.32.0/19:** A new IP range for Cato PoP locations is now available: 199.27.32.0/19. We recommend that you add this range to the relevant ACLs to allow traffic for upcoming PoP locations and ranges in the Cato Cloud.
- **New York, United States**: A new range (216.205.126.0/24) is now available for the New York PoP location.
- **Los Angeles, United States:** A new range (199.27.32.0/24) will soon be added to the Los Angeles PoP location.
- **New Localized IP Range for Uruguay:** A new localized IP range for Uruguay (serviced through the Sao Paulo PoP location) is now available - 216.205.124.0/27. This replaces the previous localized IP range serviced through Miami - 216.194.96.144/28.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
