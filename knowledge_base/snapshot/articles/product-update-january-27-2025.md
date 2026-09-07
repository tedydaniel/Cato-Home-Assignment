---
title: "Product Update - January 27, 2025"
slug: "product-update-january-27-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-january-27-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - January 27, 2025

- **Introducing the Layer 7 Socket LAN Firewall:** The new Socket LAN Firewall policy provides Layer 7 (L7) enforcement and account-level configurations, enabling seamless LAN segmentation. The Socket LAN firewall controls local network traffic without sending the traffic over the last mile to the PoP. This helps you reduce latency and offload bandwidth from the cloud by keeping internal traffic onsite, while still applying application-layer policy controls.
  - **L7 Segmentation**: Implement advanced security rules based on applications, services, and domains. For example:
    - Configure access to on-premise apps dynamically with custom applications as destinations
    - Enforce secure protocols like SMBv3 over vulnerable versions
  - **Account-Level Policy**: Create a single rule that is enforced over multiple sites. This simplifies LAN segmentation at scale with centralized rules using Groups, VLAN IDs, and other flexible criteria
  - Supported from Socket v.22
  - Supported for new customers or customers without existing LAN Firewall rules. Migration isn’t currently supported
  - Available from January 31, 2025

- **New Sandbox Service for Advanced Forensic Malware Analysis:** The new [Sandbox service](/v1/docs/scanning-files-in-the-sandbox) delivers in-depth forensic analysis for comprehensive malware investigation. After a file is scanned in the Sandbox, a [report](/v1/docs/understanding-the-sandbox-analysis-report) provides detailed insights into the file’s risk level. The report includes processes, network and disk activity, and other critical indicators of compromise, empowering teams with actionable intelligence. Key features include:
  - **Secure Isolated Environment:** Suspicious files are safely triggered within an isolated, secured environment, ensuring no impact on endpoints or network security
  - **Comprehensive Analysis:** Files undergo both static and dynamic analysis, generating a detailed report that provides a complete view of potential risks and exposure
  - **Automation and Flexibility:**
    - Blocked malicious and suspicious files are automatically forwarded to the Sandbox for analysis
    - Files can also be manually uploaded for scanning
  - The Sandbox service is included in the Advanced Threat Prevention license
  - Click [here](https://academy.catonetworks.com/cloud-sandbox) to watch a video recording of this feature

- **Data-Driven Safe TLS Inspection for Improved User Experience:** We’ve simplified the process for implementing the TLS Inspection policy to significantly reduce the setup time and potential issues. This [new setup experience](/v1/docs/using-the-tls-inspection-configuration-wizard) includes:
  - **TLS Inspection Setup Wizard:** The new wizard guides you through the rule configuration process and helps ensure that your policy follows best practices for what traffic to inspect and what to bypass. The wizard also lets you customize the rules to meet your organization’s needs.
    - You can also review your compliance with best practices in a new section on the TLS Inspection page
  - **Category for Safe-to-Inspect Apps**: The Cato research team used advanced data analysis methods to identify many apps and domains that don’t cause issues during TLS Inspection. All of these items are included in a single category you can add to an inspect rule.
  - Click [here](https://academy.catonetworks.com/safe-tls-inspection) to watch a video recording of this feature

- **New Experience Monitoring Metrics for Zoom and Microsoft Teams:** Experience Monitoring includes application-specific metrics for Unified Communication as a Service (UCaaS) traffic, such as Zoom and Microsoft Teams sessions. The new metrics provide insights into the experience of video, audio, and screen sharing during calls.
  - Requires Cato connectors for Microsoft Teams and Zoom
  - For customers with a DEM license
  - Available from January 31, 2025

- **Browser Access Application Portal now supports RDP and SSH:** The [Browser Access Application Portal](/v1/docs/browser-application-portal-overview-securing-remote-access-to-applications) now supports Remote Desktop Protocol (RDP) and Secure Shell (SSH) for [remote connections to hosts](/v1/docs/defining-browser-access-to-remote-hosts) residing on your WAN. This lets remote users securely access and utilize hosts supporting these protocols without establishing a direct connection between the user's device and the remote host.
  - All connections are brokered by our Cato secure PoPs based on the administrator Access Policy
  - This capability provides internal or external Users the experience of a native desktop or terminal via their browser
  - Available from January 31, 2025
  - Click [here](https://academy.catonetworks.com/rdp-ssh-clientless-capabilities) to watch a video recording of this feature

- **Native Integration for Azure vWAN:** Cato now supports a native integration for customers who want to connect their Azure vWAN environment to their account and benefit from the Cato networking and security services. The integration is configured using Terraform and connects to the Cato Cloud via IPsec connections
  - For customers with an existing vWAN and vHub setup
  - Requires two IPsec connections (primary and secondary)
  - Available from January 31, 2025

- **New vSocket for GCP:** For sites hosted in Google Cloud Platform (GCP), you can now deploy a virtual Socket on a GCP virtual machine and extend the advantages of Cato's Sockets into your GCP environment.
  - The GCP vSocket supports the n2-standard-4 machine type
  - Previously, vSockets were available only for AWS and Azure environments
  - Available from January 31, 2025

- **New Indications for XDR UEBA Stories**: Cato's XDR detects anomalous activities that may indicate a security threat based on User and Entity Behavior Analytics (UEBA). We are adding additional indications related to anomalies for cloud applications. For example, bulk failed logins, or insider threats such as user activity that could cause data loss.
  - Available for XDR Pro and MXDR customers
  - Click [here](https://academy.catonetworks.com/ueba-xdr-stories) to watch a video recording of this feature

- **Seamless Cloud Interconnect Sites Provisioning with Megaport:** You can now provision your Cloud Interconnect sites with Megaport fabric-based locations through the Cato Management Application. This lets you quickly connect using our turnkey solution.
  - Adds 6 new PoP locations
  - Supported cloud providers: AWS, Azure, GCP, and Oracle
  - View the complete list of Cloud Interconnect Availability locations [here](/v1/docs/cloud-interconnect-availability)
  - Available from January 31, 2025

- **DLP Support for Google Drive:** Data Loss Prevention (DLP) now supports files stored in Google Drive. This ensures that you can protect sensitive information stored in Google Drive according to your data protection policies.

- **Microsegmentation for Inner L2 Zero Trust:** We are introducing microsegmentation for your VLANs, forcing traffic between hosts within the same VLAN/broadcast domain to be routed to Cato for thorough inspection and security enforcement. Use the WAN or LAN Firewall policies to define how the traffic is managed.
  - Supported for Native, and VLAN static network ranges where Cato is the DHCP server
  - Available for Socket sites starting from v22 and higher
  - Available from January 31, 2025

- **EPP - Export Protected Endpoints to CSV:** Cato Endpoint Protection (EPP) now supports exporting the list of [Protected Endpoints](/v1/docs/managing-the-endpoint-protection-solution) to a CSV file. This can be useful for ensuring that the information in the CMA and your third-party MDM software is aligned.
  - Click [here](https://academy.catonetworks.com/epp-export-protected-endpoints-to-csv) to watch a video recording of this feature

- **CMA Enhancement:**
  - **XDR Network Stories Sync with ILMM Onboarding Data:** For accounts with the ILMM and NOCaaS services, [XDR Network stories](/v1/docs/reviewing-site-operations-stories) now automatically include ILMM onboarding data required to respond to network issues.
    - The new story data includes the site contact person and ISP details
    - Stories related to a link that isn’t fully onboarded are muted by default

- **Translated Knowledge Base Articles:** We are starting to introduce AI-based translations for the Knowledge Base for all the [languages supported in the CMA](/v1/docs/setting-the-cma-user-interface-preferences).
  - Select the language from a drop-down menu in the Knowledge Base header
  - It’s possible that the AI translations contain expressions that may be incorrect. Please contact us at [article-translations@catonetworks.com](mailto:article-translations@catonetworks.com) with any comments or feedback
