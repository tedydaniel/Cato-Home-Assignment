---
title: "Reviewing the Security Posture of Your SaaS Applications"
slug: "reviewing-the-security-posture-of-your-saas-applications"
updated: 2026-07-30T11:53:56Z
published: 2026-07-30T11:53:56Z
canonical: "knowledge.catonetworks.com/reviewing-the-security-posture-of-your-saas-applications"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reviewing the Security Posture of Your SaaS Applications

## Overview

SaaS Posture checks continuously evaluate the configuration and security settings of your SaaS applications. Each of the numerous applications used by your organization introduces its own configuration risks, for example, authentication settings, third-party integrations, and data-sharing controls. Misconfigurations can expose risk, even when access to the application itself is tightly controlled. SaaS Posture checks address this by providing visibility into how SaaS applications are configured and identifying where those configurations do not follow security best practices.

SaaS Posture checks are configured by creating a connector between Cato and the SaaS application. After creating the connector, the current posture of the connected SaaS application is compared with the recommended posture defined by Cato’s research team. This helps identify vulnerabilities in the configuration of the application. For a full list of supported applications, see [SaaS Posture Connectors](https://knowledge.catonetworks.com/docs/saas-posture-connectors).

Posture data for each application is available in the Applications dashboard. This provides a summary of posture scores and highlights the highest-severity findings across connected applications. You can review each posture check from the Posture page. Each check includes details about the issue, its status, and the remediation action required to pass the check.

SaaS Posture checks require a CASB license.

### Understanding SaaS Posture Checks, CASB, and Interconnected Apps

[SaaS Posture checks](/v1/docs/understanding-the-security-posture-of-your-saas-applications), [CASB](/v1/docs/what-is-the-unified-casb-solution), and [Interconnected Apps](/v1/docs/interconnected-apps) each address different aspects of SaaS security and work together to provide comprehensive visibility into your SaaS environment.

- SaaS Posture checks evaluate the security configuration of your SaaS applications. They identify misconfigurations and settings that don't follow security best practices, such as disabled multi-factor authentication, overly permissive sharing settings, or inactive administrator accounts. These checks help you harden your SaaS applications and reduce the risk of compromise.
- CASB provides visibility into how users interact with SaaS applications. It monitors user activity, detects risky behavior, and helps enforce data security policies. For example, CASB can identify users downloading sensitive files, sharing data externally, or accessing applications from unusual locations.
- Interconnected Apps focus on third-party applications that have been granted access to your SaaS environment through OAuth or similar authorization mechanisms. These applications can introduce additional risk even when the SaaS application itself is securely configured. Interconnected Apps help you identify connected applications, understand the permissions they have been granted, and assess the potential risk they introduce.

Together, these capabilities provide a layered approach to SaaS security.

For example, a Salesforce tenant might pass all SaaS Posture checks because it follows recommended security practices. However, a third-party application with broad permissions could still expose sensitive data if it is compromised. CASB might detect a user downloading an unusually large number of files, indicating potentially risky activity. Together, SaaS Posture checks, Interconnected Apps, and CASB provide visibility into the application's security configuration, the third-party applications that can access it, and how users interact with it.

### Use Case

A Salesforce administrator manages a Salesforce tenant that contains sensitive customer information, sales opportunities, and business data. While the security team uses CASB controls to monitor user activity and enforce access policies, they also need to ensure that Salesforce is configured according to security best practices.

After creating a Salesforce connector, the security team reviews the Salesforce posture in the Cato Management Application. They identify several failed checks, such as users who are not required to use multi-factor authentication, overly permissive administrator roles, and security settings that do not align with recommended configurations. From the Posture page, they review each failed check and follow the remediation guidance.

This helps reduce risk in the Salesforce environment without manually auditing every security setting.

## Viewing Posture Checks

A summary of SaaS Posture checks can be viewed from the Application dashboard. This provides a high-level view of SaaS posture findings across connected applications. For more information, see [Using the Applications Dashboard.](/v1/docs/using-the-applications-dashboard)

On the **Posture** page, the **SaaS Security** tab displays each posture check. Each check includes its status, severity, related findings, and remediation guidance. This helps security teams understand what failed and how to resolve it.

For more information on reviewing Posture checks, see [Reviewing Posture Checks for Your Account.](/v1/docs/reviewing-posture-checks-for-your-account)

**Note:** SaaS Security checks do not contribute to the **Account Score**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(15).png)

The posture checks are divided into these security domains:

- **Authentication:** Help verify that strong authentication methods are configured. For example, they can identify gaps in MFA enforcement or other login security settings.
- **Data Protection:** Checks related to protecting sensitive data in SaaS applications. These checks help identify settings that may expose data or allow unnecessary access.
- **Application Access:** Checks related to how users and services access SaaS applications. These checks help identify risky access paths, broad permissions, or access that is not aligned with security policy.
- **Identity Access:** Help identify users, roles, or permissions that may increase account or application risk.
- **Configuration Governance:** Checks related to the overall configuration of the SaaS application. These checks help identify settings that do not follow recommended security practices.
- **Identity and Access:** Checks related to the relationship between identities, privileges, and access rights. These checks help identify excessive permissions, stale access, or privileged access concerns.
