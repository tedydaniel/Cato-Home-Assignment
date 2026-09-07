---
title: "Viewing and Analyzing Interconnected Apps"
slug: "viewing-and-analyzing-interconnected-apps"
updated: 2026-07-06T12:41:36Z
published: 2026-07-06T12:41:36Z
canonical: "knowledge.catonetworks.com/viewing-and-analyzing-interconnected-apps"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Viewing and Analyzing Interconnected Apps

This article explains how to view and analyze third-party interconnected apps used in your environment to quickly assess their security posture.

## Overview

Third-party applications, extensions, and plugins can introduce significant risk to corporate SaaS environments. These integrations often request broad permissions and are frequently installed without security oversight, creating visibility gaps and expanding the attack surface.

Using integrations with SaaS provider APIs, the **Plugin** page, in the **Applications** dashboard, provides comprehensive visibility and risk insights into third-party plugins connected to sanctioned business-critical applications. With this visibility, you can maintain an up-to-date inventory of interconnected apps and plugins, the users who have used them, assess associated risks, and identify unauthorized integrations or integrations with overly permissive permissions. This enables effective governance and control of your SaaS attack surface.

To provide visibility into the third-party apps interconnected with a business-critical app, a connector is required. For a list of supported SaaS apps and an explanation of how to configure the connector, see [Interconnected Apps](/v1/docs/interconnected-apps).

A CASB license is required for the Plugin page. For more information about purchasing a CASB license, please contact your Cato representative.

### Understanding SaaS Posture Checks, CASB, and Interconnected Apps

[SaaS Posture checks](/v1/docs/understanding-the-security-posture-of-your-saas-applications), [CASB](/v1/docs/what-is-the-unified-casb-solution), and [Interconnected Apps](/v1/docs/interconnected-apps) each address different aspects of SaaS security and work together to provide comprehensive visibility into your SaaS environment.

- SaaS Posture checks evaluate the security configuration of your SaaS applications. They identify misconfigurations and settings that don't follow security best practices, such as disabled multi-factor authentication, overly permissive sharing settings, or inactive administrator accounts. These checks help you harden your SaaS applications and reduce the risk of compromise.
- CASB provides visibility into how users interact with SaaS applications. It monitors user activity, detects risky behavior, and helps enforce data security policies. For example, CASB can identify users downloading sensitive files, sharing data externally, or accessing applications from unusual locations.
- Interconnected Apps focus on third-party applications that have been granted access to your SaaS environment through OAuth or similar authorization mechanisms. These applications can introduce additional risk even when the SaaS application itself is securely configured. Interconnected Apps help you identify connected applications, understand the permissions they have been granted, and assess the potential risk they introduce.

Together, these capabilities provide a layered approach to SaaS security.

For example, a Salesforce tenant might pass all SaaS Posture checks because it follows recommended security practices. However, a third-party application with broad permissions could still expose sensitive data if it is compromised. CASB might detect a user downloading an unusually large number of files, indicating potentially risky activity. Together, SaaS Posture checks, Interconnected Apps, and CASB provide visibility into the application's security configuration, the third-party applications that can access it, and how users interact with it.

### Use Case: Identifying High-Risk or Unauthorized Plugins

A security analyst needs to ensure that only approved third-party plugins are connected to corporate Slack. End users may install plugins without a security review, potentially granting excessive permissions or introducing security risks. Using the Plugin Inventory, the analyst identified 30 users using an unsanctioned plugin with a high risk level and overly permissive permissions. The analyst contacts the users and requests that they remove the risky plugin to reduce the attack surface.

## Getting Started with the Plugin Page

The **Plugin** page is part of the **Applications Dashboard** and displays a list of apps integrated with SaaS applications.

![Plugging.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33644450128669.png)

### Accessing the Plugin Page

To access the **Plugin** page, navigate to **Security > Applications**. On the **Inventory** page, click **Plugins**.

### Understanding the Summary Section

This table explains the widgets in the Summary section.

![Summary1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33644500502813.png)

| Name | Description |
| --- | --- |
| Plugins | Number of plugins integrated with SaaS applications |
| Risky Plugins | Number of risky plugins integrated with SaaS applications |
| Plugin Users | Number of users using plugins |
| Integrations | Number of integrations created with SaaS applications to monitor plugins |

### Understanding the Plugins Table

The Plugins table displays information about each plugin.

For detailed information about a plugin, including its granted permissions and the users who have installed or used it, click the plugin name to open the **Plugin Quick View** panel.

![Pluginquickview.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33644433151645.png)
