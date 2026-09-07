---
title: "Understanding the Fields in the App Catalog"
slug: "understanding-the-fields-in-the-app-catalog"
status: "update"
updated: 2026-09-06T10:14:54Z
published: 2026-09-06T10:14:54Z
canonical: "knowledge.catonetworks.com/understanding-the-fields-in-the-app-catalog"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the Fields in the App Catalog

## Overview

This article provides a reference for the fields that are available for applications in the [App Catalog](/v1/docs/using-the-app-catalog). Use this reference to understand the metadata that Cato shows for each application and how these fields can help you evaluate apps for your organization.

The App Catalog is continuously updated with new applications and metadata by Cato’s Security Research team, and this data is used across the CMA to help you evaluate apps and use them in policies and rulebases.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/App Catalog - quick view(1).png)

## App Field Descriptions

**Categories** refers to the Cato category for this application.

This table explains the metadata that is available for the applications.

| Field | Description |
| --- | --- |
| **App Quick View** |
| Type | Indicates whether the app is a cloud application, on-premise application, or service |
| Risk | Numerical score that represents the app’s risk level |
| Classification | Shows whether the app is currently sanctioned or unsanctioned, and lets you add the app to Sanctioned Apps |
| **App Overview** |
| Description | Summary of the application’s purpose and functionality |
| Headquarters | Location of the company that owns the application |
| Website | Official vendor website |
| Size | Estimated size of the organization |
| AI Risk | Cato-assigned risk for the AI app. This reflects risks specifically related to an application's use of AI, with a focus on data handling, privacy, and compliance. It is separate from the application's overall Security Risk score, which considers factors such as security threats, vulnerabilities, and reputation. |
| Parent Applications | The applications that contain this application. Policies configured for a parent application can also apply to this application |
| Children Applications | The applications contained within this application. Policies configured for this application can also apply to its child applications. |
| **AI Security** |
| Scope | Indicates how AI functionality is provided by the application. For example, **Native** means the AI functionality is built into the application Possible values: **Native**, **Embedded** |
| Data Usage Type | Indicates whether data submitted to the application can be used to train or improve its AI models. Possible values: **Trains on data**, **General data usage**, **No data usage** |
| Data Usage Policy | Summarizes how the application provider collects and uses data submitted to the AI application, including how the data may be used to improve products or AI models |
| Privacy Policy | Links to the application provider's privacy policy for more information about how data is collected, used, and protected |
| **Domains and FQDNs** |
| A list of the domains and FQDNs associated with each app |
| **IP Ranges and ASNs** |
| A list of static IP ranges, dynamic IP sources, and ASNs associated with each app |
| **Security** |
| MFA Support | Indicates whether multi-factor authentication is supported |
| SSO Support | Indicates whether Single Sign-On is supported |
| RBAC Support | Indicates whether role-based access control is available |
| Encryption in Transit | Indicates whether data is encrypted during transmission |
| TLS Version Support | Supported TLS versions for the application |
| Encryption at Rest | Indicates whether stored data is encrypted |
| Encryption Strength at Rest | Describes the encryption strength for stored data, when available |
| Weak Cipher Support | Indicates whether weak encryption is allowed |
| Trusted Certificates | Indicates whether the application uses trusted certificates |
| HTTP Security Headers | Indicates whether secure HTTP headers are present |
| Physical Data Center Security | Indicates whether physical security controls are disclosed or supported |
| Audit Trail | Indicates whether activity logging is available |
| Disaster Recovery | Indicates whether recovery mechanisms are available |
| Data Segregation by Tenant | Indicates whether tenant data is logically separated |
| Remember Password | Indicates whether persistent login is supported |
| Data Retention Policy | Defines how long customer data is stored |
| Data Deletion Policy | Defines how and when customer data is deleted |
| Data Ownership | Specifies ownership of stored customer data |
| **Compliance - Core Frameworks** |
| ISO 27001 | Information security management certification |
| SOC 1 | SOC 1 reports on controls that can affect customers’ financial reporting |
| SOC 2 | SOC 2 reports on controls for security, availability, processing integrity, confidentiality, and privacy |
| SOC 3 | SOC 3 is a public summary of SOC 2 controls for broad sharing |
| HIPAA | Healthcare data protection compliance |
| PCI-DSS | Payment card industry data security standard |
| GDPR | European data protection regulation |
| SOX | Financial reporting compliance |
| ISAE 3402 | Assurance standard for service organizations |
| FedRAMP | US government cloud security authorization |
| FISMA | Federal information security standard |
| NIST SP 800-53 | NIST framework that defines security and privacy controls for information systems and organizations |
| ISO 27017 | Cloud security standard |
| ISO 27018 | Privacy protection for cloud data |
| ISO 27002 | Information security controls standard |
| CSA STAR | Cloud Security Alliance certification |
| C5 Attestation | German cloud compliance framework |
| Cyber Essentials Plus | UK cybersecurity certification |
| COBIT | IT governance framework |
| FERPA | US education privacy regulation |
| COPPA | US children’s privacy regulation |
| GLBA | Financial services privacy regulation |
| CJIS | Criminal justice information standard |
| FINRA | Financial industry regulation |
| FFIEC | US financial institution guidance |
| GAPP | Privacy framework developed by US and Canadian accounting bodies for managing and assessing an organization’s privacy program |
| EU-US Data Privacy Framework | Cross-border data transfer compliance |
| TrustArc Privacy | A US-based third-party privacy certification program that validates an organization’s privacy practices |
| Japan Privacy Mark | Japan-based third-party certification for organizations that meet privacy protection requirements |
| Jericho Forum Commandments | Security design principles defined by a customer-led industry group for secure architectures in open, networked environments |
| **Identity and Access Management** |
| Access Control Enforcement | Indicates that the application can natively restrict and enforce user access |
| IP-Based Access Restrictions | Shows whether the application supports IP-based access restrictions |
| SAML Authentication | Shows whether the application supports SAML authentication |
| **Activities** |
| Upload | Ability to upload content |
| Download | Ability to download content |
| Send Voice Message | Ability to send voice data |
| Remove/Delete | Ability to delete content |
| Full Path URL Access | Access via a direct URL |
