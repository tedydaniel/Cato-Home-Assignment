---
title: "How Cato Protects Sensitive Data with DLP"
slug: "how-cato-protects-sensitive-data-with-dlp"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/how-cato-protects-sensitive-data-with-dlp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How Cato Protects Sensitive Data with DLP

## Overview

Cato Data Loss Prevention (DLP) inspects traffic to identify and control sensitive information as users access SaaS, private applications, and web resources. The service uses two complementary methods of inspection for full visibility and governance. Data Protection Inline and Data Protection API operate independently in different scenarios but rely on the same underlying classification engines to ensure consistent detection across all user types.

![image__64_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32622825420957.png)

- **Data Protection Inline** applies DLP inspection to real-time traffic routed through Cato PoPs. Inline protection covers managed users and site traffic, enforcing DLP rules on SaaS, private applications, and web destinations. TLS Inspection is required to analyze encrypted sessions.

The inline traffic flow is shown on the left side of the example above.
- **Data Protection API** extends DLP coverage to sanctioned SaaS apps even when traffic is not routed through the Cato Cloud. It monitors user-driven actions such as file uploads, shares, and modifications directly through API integrations, providing visibility for unmanaged devices, split‑tunnel connections, or users who access the apps without the Cato Client. The API inspects data in motion within the SaaS platform but does not scan stored files at rest.

The API out-of-band traffic flow is shown on the right side of the example above.

The Cato XOps service provides the operational context for DLP events by correlating Inline and API detections into unified stories. Each story aggregates related activity, such as the user, app, action sequence, and destination, to show how sensitive data moved through the environment. This correlation helps administrators quickly identify unintended sharing, policy violations, or abnormal data handling across different access paths.

## Data Classification and Detection Methods

Cato’s DLP engine provides a consistent classification framework used by both Data Protection Inline and Data Protection API. Each enforcement method uses separate policies to ensure accurate detection of sensitive information across all access paths.

Although Data Protection Inline and Data Protection API use different policies, they share the same data classification framework and detection methods to ensure accurate detection of sensitive information.

You can also ensure seamless data governance by integrating with Microsoft Purview and Google Sensitivity Labels. Customers who already use these solutions for data classification and labeling can leverage them for inline protection and data leak prevention.

For more information, see [Using MIP Sensitivity Labels in your Cato DLP Policy](/v1/docs/using-mip-sensitivity-labels-in-your-cato-dlp-policy) and [Using Google Labels with the Data Protection API](/v1/docs/using-google-labels-with-the-data-protection-api).

### Cato Data Classification

Cato’s classification framework is centered on **DLP Profiles**, which define the data identifiers that represent sensitive content within an organization.

- **Predefined Data Types:** [Built-in identifiers](/v1/docs/creating-dlp-content-profiles) for common regulated and sensitive information, such as global PII formats, financial data, healthcare data, HR documents, and compliance-driven categories.
- **Custom Data Types:** User-defined data identifiers that extend classification to organization-specific requirements.

### Data Detection Methods

Cato applies several detection techniques to accurately identify sensitive data:

- Machine learning and LLM-based models, accelerated by GPU hardware in the Cato PoP, classify full documents by analyzing semantic meaning and similarity to known sensitive categories. Administrators can upload and test custom LLM classifiers directly within the CMA.
- Image ML classifiers are machine learning models that analyze pixels in an image to determine what the image contains. They are part of the broader field of computer vision.
- LLM topic classifiers use LLM-based models to understand the meaning and context of text. They classify a document based on its topic, theme, structure, or writing style.
- Exact Data Match (EDM) validates sensitive values against approved datasets, reducing false positives for structured, organization-specific content.
- Optical Character Recognition (OCR) extracts text from images, scanned documents, and screenshots to prevent attempts to bypass text-based inspection.
- Regex and keyword matching detect patterns associated with regulated data fields or internal identifiers.

For more information, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles), [Working with Custom Data Types for DLP](/v1/docs/working-with-custom-data-types-for-dlp), and [Working with Exact Data Matching (EDM) for DLP](/v1/docs/working-with-exact-data-matching-edm-for-dlp).

## Data Protection Inline

Data Protection Inline applies DLP inspection to data in motion as traffic is routed through Cato PoPs. Because it operates at the network layer, inline inspection provides deterministic, real-time enforcement for traffic fully routed through the Cato Cloud.

Inline enforcement applies to:

- Office users connected through a Cato-enabled site
- Remote users connected through the Cato Client
- Site-to-cloud and site-to-Internet flows are inspected in real time

Inline DLP has specific operational requirements and behaviors that impact how the data polices are applied to traffic over the Cato Cloud:

- TLS Inspection is required to analyze encrypted content, such as HTTPS sessions, so that sensitive content within SaaS, private applications, or web traffic can be inspected.
- Enforcement actions, including block, alert, and redact, are applied immediately as traffic is evaluated.

For more information, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service).

## Data Protection API

Data Protection API extends DLP inspection to sanctioned SaaS applications when traffic does not traverse the Cato Cloud. It uses application-specific connectors to send SaaS activity to a Cato DLP engine hosted in AWS for inspection.

The API connector uses OAuth-based integrations defined in App & Data API Protection (Security > App & Data API Protection). Supported apps include Microsoft 365, Google Workspace, Salesforce, and others. For a full list of supported apps, see [Data Protection API](/v1/docs/data-protection-api).

Data Protection API provides DLP visibility for:

- Unmanaged devices
- Split-tunnel or locally routed SaaS traffic
- Users without the Cato Client or a ZTNA license

The API engine applies the same classification logic used for inline DLP, enabling consistent detection of sensitive content for SaaS actions such as:

- File uploads
- External or public sharing
- Permission changes
- Modifications involving regulated data

Admins can use the **Data Protection API Dashboard** in the CMA to monitor SaaS activity and drill down into violations to view the associated data and context.

For more information, see [What is the Data Protection API?](/v1/docs/what-is-the-data-protection-api).

## Managed and Unmanaged Device Coverage

Cato’s Data Protection architecture provides unified coverage for both managed and unmanaged devices, regardless of how users connect or where data is accessed. Inline and API protection work together to eliminate common visibility and control gaps. This ensures that sensitive data remains protected across every usage scenario, from corporate devices on trusted networks to unmanaged devices accessing SaaS directly.

### Managed Devices

Managed devices either sit behind a Cato-connected site or use the Cato Client to send traffic through the Cato Cloud. In these cases, inline DLP based in the PoP inspects data in motion as users access SaaS, private applications, or web resources.

Admins can apply app-level restrictions to control which applications are inspected, how sensitive data is handled, and enforce login to SaaS apps only when users are connected to the Cato cloud.

Selective on-ramp configurations allow only chosen traffic to be routed through the Cato Cloud, ensuring that inline DLP enforcement is applied specifically to the flows that require inspection.

### Unmanaged Devices

Unmanaged devices access SaaS applications directly over the Internet. Data Protection API gives admins visibility into sensitive data use in sanctioned SaaS applications.

- No requirement to install the Cato Client as additional software for contractors
- For Split Tunnel policy, traffic that bypasses the Cato Cloud is still inspected for sensitive data
- No additional ZTNA licenses required for Data Protection API

## Policy Configuration and Visibility

Cato separates Inline and API-based Data Protection into dedicated rulebases, allowing administrators to tailor controls to how users access applications and where inspection is required. This structure ensures that each enforcement path can be refined for maximum relevance and visibility.

### Configuring DLP Policies

Admins configure Inline and API DLP policies separately to ensure that controls align with how users access applications and where inspection is required.

- Inline DLP policy rules are configured in **Security > App & Data Inline**, where admins define which applications, users, and destinations are subject to inline inspection.
- API-based DLP policy rules are configured in **Security > App & Data API Protection**, where SaaS connectors and event-driven rules are managed.
- The same DLP Profiles and Data Types can be used in both policies.

### Enforcement Actions

Enforcement actions determine how detected sensitive data is handled and provide administrators with immediate control over both inline and SaaS‑based violations.

- **Block** prevents sensitive data from leaving the organization through inspected inline flows.
- **Alert** logs the event without blocking the action, allowing visibility into usage patterns.
- **Quarantine** is available for supported SaaS applications via API-based protection, moving sensitive files to a restricted location for admin review.

### Visibility and Monitoring

The CMA includes dedicated dashboards for each policy type so administrators can quickly identify violations, investigate activity, and understand how sensitive data moves across the environment.

- Inline DLP events appear in the **App & Data Inline Dashboard**, where admins can filter, sort, and investigate violations. For more information, see [Using the Data Protection Inline Dashboard](/v1/docs/using-the-data-protection-inline-dashboard).
  - You can view forensic evidence directly from the event to quickly understand the context of an incident, assess potential data exposure, and validate false positives. For more information, see [Investigating DLP Violations with Forensic Evidence](/v1/docs/investigating-dlp-violations-with-forensic-evidence).
- The Data Protection API Dashboard provides visibility into SaaS-specific activity, such as file uploads, shares, or permission changes. For more information, see [Using the Data Protection API Dashboard](/v1/docs/using-the-data-protection-api-dashboard).

The Cato XOps service correlates inline and API detections into unified stories, allowing administrators to investigate cross-channel patterns of sensitive data movement.

## XOps and Data Protection

Cato XOps strengthens DLP investigations by correlating detections from both Data Protection Inline and Data Protection API into unified stories. This correlation provides a single view of sensitive data movement across network traffic inspected in-line in Cato PoPs and out-of-band SaaS activity inspected through API connectors. Integrating with your DSPM also provides visibility of data at rest, for example, in a data center.

Each XOps story includes the user, application, action, and destination involved in the activity. This consolidated context helps administrators understand how sensitive data was accessed or shared, regardless of whether it moved through the network or within a SaaS platform. For example, the XOps UEBA anomaly engines analyze deviations from typical user or device behavior to surface risks such as unexpected SMB uploads or SSH file transfers. These behaviors may indicate attempts to bypass normal data handling processes.

Related Articles:

- [Welcome to the Cato XOps Service](/v1/docs/welcome-to-the-cato-xops-service)
- [Analyzing XOps UEBA Stories for Usage and Events Anomalies](/v1/docs/analyzing-xops-ueba-stories-for-usage-and-events-anomalies)

### Example Use Case: Responding to Coordinated Threats

XOps also correlates DLP events with detections from other Cato security services, enabling administrators to identify multi‑vector attacks. For example, IPS may detect malware activity on a device, indicating potential compromise. Shortly afterward, the inline or API DLP engine flags an attempted exfiltration of customer data from the same device to an external server. XOps links these detections into a single story that shows both the malware indicators and the attempted data transfer. This story gives SOC teams full visibility into the scope of the threat progression and helps them respond more quickly and accurately.
