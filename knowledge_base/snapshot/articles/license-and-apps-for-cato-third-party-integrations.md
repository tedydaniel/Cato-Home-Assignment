---
title: "License and Apps for Cato Third-Party Integrations"
slug: "license-and-apps-for-cato-third-party-integrations"
updated: 2026-07-16T09:48:41Z
published: 2026-07-16T09:48:41Z
canonical: "knowledge.catonetworks.com/license-and-apps-for-cato-third-party-integrations"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# License and Apps for Cato Third-Party Integrations

This article lists the different [third-party integrations](/v1/docs/using-the-integrations-page) that you can connect to your Cato account and which license is required for the integration. Some integrations are included with the default account license.

**Included** means that the integration type is part of the default Cato account and doesn't require an additional license.

> [!NOTE]
> Note:
> 
> Cato account licenses use one of two models: [Bursting Model](/v1/docs/jan-2027-license-bursting-model) (starting in January 2027) and Enforcement Model. The licenses listed in this table refer to both license models unless stated. Not sure which license your account uses? See [Identifying your License Model](/v1/docs/identifying-your-license-model).

| Integration Type | Integration Description | Supported Apps & Vendors | License |
| --- | --- | --- | --- |
| vSocket Connectivity | Create a virtual Socket site to connect your cloud tenant to the Cato Cloud For more information about vSockets, see the relevant articles in [vSocket Sites](/v1/docs/vsocket-sites). | - AWS Cloud - Azure Cloud - GCP - VMware ESXi | Enforcement Model: Included Bursting Model: Bandwidth Pool |
| Cloud Interconnect | Connect directly to another network using a data center cloud exchange via a service provider partner (such as Equinix’s Cloud Exchange Fabric or Megaport SDCI) For more information about Cloud Interconnect, see the relevant articles in [Cloud Interconnect Sites](/v1/docs/cloud-interconnect-sites). | - AWS Cloud - Azure Cloud - GCP - Oracle | Enforcement Model: Included Bursting Model: Bandwidth Pool |
| Directory Service | Retrieve and synchronize user information from a user directory into your Cato account for efficient user-aware access control For more information about Directory Services, see the relevant articles in [Directory Services](/v1/docs/directory-services). | - JumpCloud - Microsoft Entra ID - Okta - OneLogin | Included |
| User Authentication | Configure SSO for unified secured user access and authentication across enterprise apps and services For more information about authentication, see the relevant articles in [Single Sign-On](/v1/docs/single-sign-on). | - CyberArk - ForgeRock - Google - Hennge One - JumpCloud - Microsoft Entra ID - Okta - OneLogin - OneWelcome - Ping Federate IDP - SafeNet | Enforcement Model: Included Bursting Model: ZTNA User |
| CMA Admin Authentication | Configure SSO for Cato Management Application admins, providing unified, secure access and authentication For more information about CMA admin authentication, see [Authenticating Admins](/v1/docs/authenticating-admins). | - Google - KeyCloak - Microsoft Entra ID - Okta - OneLogin - Ping Federate IDP | Included |
| Sensitivity Labels | Import sensitivity labels for DLP engine For more information, see [Using MIP Sensitivity Labels in your Cato DLP Policy](/v1/docs/using-mip-sensitivity-labels-in-your-cato-dlp-policy). | - Microsoft AIP | DLP |
| App Activities | Monitor app activities from unmanaged and managed users by connecting apps via APIs For more information, see the relevant articles in [Application Control via API with Audit Activities](/v1/docs/application-control-via-api-with-app-activities). | - Confluence - Egnyte - ChatGPT - Atlassian (Jira and Confluence) - GitHub - Box - Jira - Make - Microsoft - Copilot - Exchange - OneDrive Business - SharePoint Business - Teams - Viva - Salesforce - Zendesk - Google Drive and Workspace - Dropbox - Slack - Make - ServiceNow - Workday | CASB |
| Data Protection | Deliver App & Data security with data protection and threat detection for key SaaS apps using API-based integration For more information, see the relevant articles in [Data Protection API](/v1/docs/data-protection-api). | - Box - Dropbox - GitHub - Google Workspace - Meta Workplace - Microsoft Office 365 - Salesforce - Service Now - Slack | Enforcement Model: CASB Bursting Model: DLP |
| Interconnected Apps | Comprehensive visibility and risk insights into third-party plugins connected to sanctioned business-critical applications For more information, see the relevant articles in [Interconnected Apps](/v1/docs/interconnected-apps). | - Microsoft Entra ID - Salesforce - Slack | CASB |
| Device Inventory | Discover, monitor, and manage devices connected to your network. For more information, see [What is Device Inventory?](/v1/docs/what-is-device-inventory) and [Device Management Connectors](/v1/docs/device-management-connectors) | - Armis - Claroty - CrowdStrike - Microsoft Intune - Juniper Mist - Zoom | Enforcement Model: IoT/OT Bursting Model: Asset Security |
| Sign In Activities | Integrate your IdP app and collect sign-in audit activities For more information, see [Configuring the Microsoft Entra ID (Azure AD) Connector](/v1/docs/configuring-the-microsoft-entra-id-azure-ad-connector). | - Microsoft Entra ID | Included |
| EDR | Integrate with data from your EDR to collect endpoint alerts and incidents For more information, see [Microsoft Defender for Endpoint Alerts: Configuring the XOps Integration](/v1/docs/microsoft-defender-for-endpoint-alerts-configuring-the-xops-integration), [SentinelOne EDR: Configuring the XOps Integration](/v1/docs/sentinelone-edr-configuring-the-xops-integration), [CrowdStrike: Configuring the XOps Integration](/v1/docs/crowdstrike-configuring-the-xops-integration) | - Defender for Endpoint - SentinelOne - CrowdStrike | Events - Included Stories - XOps |
| AI Security | Secure and govern AI usage across your organization with full visibility, policy enforcement, and data protection For more information, see the articles in [AI Security](/v1/docs/ai-security) (you must be logged in to view the articles). | - Anthropic Compliance API - Azure Blob Prompts Storage - ChatGPT Compliance API - M365 Copilot API - AWS Prompts Storage | AI for End Users AI for Applications |
| XOps | Integrates data from Wiz into your XOps platform For more information, see [Wiz: Configuring the XOps Integration](/v1/docs/wiz-configuring-the-xops-integration) | - Wiz | XOps |
| Sign In Anomalies | Monitor IDP sign-in anomalies For more information, see [Configuring the Microsoft Entra ID Protection Connector for Sign-In Anomaly Data](/v1/docs/configuring-the-microsoft-entra-id-protection-connector-for-sign-in-anomaly-data) | - Microsoft Entra ID | Included |
| Security Checks | Monitor security checks for SaaS applications (SSPM) For more information, see the relevant articles in [Data Protection API](/v1/docs/data-protection-api). | - Google Drive - Microsoft 365 | Included |
| Experience Monitoring | Integrate Cato Cloud's Experience Monitoring with call metrics for Zoom, Teams, and Webex For more information, see the relevant articles in [Experience Monitoring Connectors](/v1/docs/experience-monitoring-connectors). For Webex see [this article](/v1/docs/webex-configuring-the-experience-monitoring-ucaas-connector). For the Juniper Mist integration, see [this article](/v1/docs/juniper-mist-creating-the-device-management-integration). For the Cisco Meraki integration, see [this article](/v1/docs/cisco-meraki-creating-the-experience-monitoring-connector). | - Teams - Zoom - Webex - Juniper Mist - Cisco Meraki | DEM |
| Cloud Storage | Generate an events feed directly from the Cato Data Lake to Azure and AWS storage For more information, see the relevant articles in [Event Integration](/v1/docs/event-integration). | - Azure Blob - AWS S3 | Included |
| Alerts | Receive notifications based on CMA alerts For more information, see the relevant articles in [Alerts](/v1/docs/notifications). | - Jira - Service Now - Slack | Included |
| SaaS Posture | Continuously evaluate the configuration and security settings of your SaaS applications. For more information, see the relevant articles in [SaaS Posture Management](https://knowledge.catonetworks.com/docs/saas-security-posture-management). | - Microsoft 365 - ChatGPT - Cursor - Dropbox - GutHub - Google Drive - Google Workspace - Salesforce - Slack - Zendesk | CASB |
| SIEM | Data integrations - SIEM, asset management, log and security analytics For more information, see [Cato Data: Third-Party Supported Integrations](/v1/docs/cato-data-third-party-supported-integrations). | - Arctic Wolf - Axonius - Data Bee - Devo - Google Chronicle - Hunters - LogicMonitor - Lumu - Microsoft Sentinel - Rapid7 - SecureWorks Taegis XDR - Sekoia - Sophos - Splunk - Stellar Cyber - Sumo Logic - Zenoss | Included |
| Integration Tools | Terraform provider for Infrastructure as Code (IaC) and DevOps automation For more information, see [Using Terraform with the Cato Cloud](/v1/docs/using-terraform-with-the-cato-cloud). | - Terraform | Included |
