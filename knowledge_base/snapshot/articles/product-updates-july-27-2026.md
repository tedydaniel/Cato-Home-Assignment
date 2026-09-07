---
title: "Product Updates - July 27, 2026"
slug: "product-updates-july-27-2026"
updated: 2026-08-02T09:44:30Z
published: 2026-08-02T09:44:30Z
canonical: "knowledge.catonetworks.com/product-updates-july-27-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - July 27, 2026

## New Features & Enhancements

- **Windows Client v6.12:** During the week of July 26, 2026, we plan to begin rolling out Windows Client version 6.12. This version includes:
  - **Additional Installation Parameters**: The Windows MSI supports [installation parameters](https://knowledge.catonetworks.com/docs/deploy-cato-client-with-intune-windows) that previously required setting registry keys, simplifying automated deployments.
  - **Updated OPSWAT OESIS Framework**: We updated the [OPSWAT OESIS framework](https://www.opswat.com/products/endpoint-security-sdk/device-compliance) used by the Client to version 4.3.6344
  - Stability improvements, security updates, and bug fixes
- **New Client Management Page for Endpoint Visibility and Control**: The [**Client Management** page](https://knowledge.catonetworks.com/docs/managing-the-cato-client) provides centralized visibility into Cato Clients installed in your organization. It streamlines troubleshooting and support workflows. (Show me the [Client Management page](https://externallink.cc.catonetworks.com/#/account/me/clientManagement))
  - View the status of each service (Private Access, Internet Access) and troubleshoot issues
  - Perform actions such as **Bypass Always-On** and **Upload Logs** directly from the page
  - Supported for Windows Clients v5.21 and higher
- **Licensing Version Shown in the CMA:** The licensing version for your account determines how you manage and apply licenses in the Cato Management Application (CMA). There are two Cato account licensing versions: Enforcement and Bursting. The License page in the CMA shows the licensing version.
  - Learn more about the two license types [here](https://knowledge.catonetworks.com/docs/identifying-your-license-model)
  - Show me the [License page](https://cc.catonetworks.com/#/account/me/license)
- **Enterprise Browser v1.1.0.52:** During the week of July 26, 2026, Enterprise Browser [version 1.1.0.52](https://knowledge.catonetworks.com/docs/summary-of-enterprise-browser-releases) will be available. This version contains bug fixes and enhancements.
- **AWS IAM Role Authentication for AI Security Proxy Guards:** Authenticate the AI Security Proxy Guard to [Amazon Bedrock](https://knowledge.catonetworks.com/docs/configuring-aws-iam-role-authentication-for-proxy-guards) with an AWS IAM role instead of a static API key. This lets you use short-lived AWS credentials and reduce long-term credential exposure.
  - Supported for Amazon Bedrock Proxy Guards
  - AI Security for Applications license required
- **Investigate AI Security Application Events**: Retrieve detailed prompt and response data from the Cato public API to investigate sensitive AI usage and forward relevant events to your SIEM.
  - API key must include the Cato [**Read Sensitive Content**](https://knowledge.catonetworks.com/docs/managing-admin-roles-using-rbac#understanding-the-predefined-admin-roles) permission
  - Requires an AI Security for Apps license
- **Enhancements to the RPF Policy:** The [Remote Port Forwarding](https://knowledge.catonetworks.com/docs/configuring-remote-port-forwarding-for-the-account) (RPF) Policy now includes:
  - **Configuration Wizard:** To help you maintain a secure and effective policy, [Posture recommendations](https://knowledge.catonetworks.com/docs/using-the-configuration-wizard) and AI-based insights are available for the RPF policy
  - **Export Rules:** Export RPF policy rules to a CSV file
- **Add Connection Origin to the TLS Policy:** To enforce more granular [TLS policies](https://knowledge.catonetworks.com/docs/configuring-tls-inspection-policy-for-the-account), you can define the **Connection Origin** for each rule. This lets you apply different TLS rules based on how users connect to Cato. Supported connection origins are Site, Client, Browser Extension, and Cato Browser.
- **Portkey Support for AI Security Proxy Guards**: Inspect and control AI traffic routed through the Portkey AI Gateway with AI Security Proxy Guards.
  - Requires AI Security for Applications license
- **Improved Usability with Labels for XOps Stories:** Use labels to filter across XOps stories in the [Stories Workbench](https://knowledge.catonetworks.com/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench), making it easy to locate stories for specific security use cases. Labels span multiple security categories, including **Internet Security**, **Asset Security**, **App & Data Security, AISec for End Users/for Applications**, and more, and are available across all Security stories.
  - Requires XOps license
- **Forensic Analysis for DLP - Support for Azure Blob Storage:** To investigate DLP policy violations, forensic evidence helps you effectively understand their context and validate false positives. Evidence is encrypted and can now be stored in [Azure Blob Storage](https://knowledge.catonetworks.com/docs/azure-blob-storage-configuring-the-forensic-storage-connector).
  - Sensitive data is stored only in the customer environment
  - DLP license required
- **Dynamic IP Allocation by Source PoP:** Allocate IP ranges to remote users based on the PoP to which the Cato Client connects.
  - Configure the [source PoP](https://knowledge.catonetworks.com/docs/ip-allocation-policy-for-remote-users#step-3-define-users-or-user-groups-to-be-allocated-ip-addresses-dynamically-or-statically) as a condition in Dynamic IP Allocation rules
