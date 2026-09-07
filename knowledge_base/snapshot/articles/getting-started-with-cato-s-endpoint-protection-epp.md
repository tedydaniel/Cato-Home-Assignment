---
title: "Getting Started with Cato's Endpoint Protection (EPP)"
slug: "getting-started-with-cato-s-endpoint-protection-epp"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/getting-started-with-cato-s-endpoint-protection-epp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with Cato's Endpoint Protection (EPP)

This article explains how to secure your endpoints with Cato's Endpoint Protection (EPP) solution.

## Overview

To prevent and detect attacks you need to implement security solutions across multiple areas across your attack surface. In addition to network security, Cato's Endpoint Protection (EPP) solution protects your endpoints, centralizing the management of your environment's security.

You can apply a default policy or customize the protection levels by creating your own policies to meet your requirements. These can be added to a profile to apply to endpoints or the same end user entities used in other policies in the Cato Management Application.

With Cato's EPP, potential threats are reported in the Cato Management Application together with events across your network. You can manage and respond to malicious activity from a single platform.

The EEP solution is only available with an additional license. For more information, contact your sales representative

> [!NOTE]
> Note:
> 
> Devices located in China are not able to register their EPP to Cato due to regional restrictions.

### Sample Use Case

Company ABC uses Cato to protect its network and enforce its remote access policy. They are able to create strict Network and Access rules for who can access their network and monitor activity. However, there is a gap in monitoring and responding to possible malicious events that take place on their endpoints. They have a third party EPP solution, but since they can't combine the endpoint and network data, they struggle to manage threats.

The company implements Cato's EPP solution which provides them with the ability to create rules for Access, Network, Security and Endpoint Protection in a single platform. With Cato's EPP solution they can monitor and respond in real time to potential malicious activity with full visibility across their entire attack surface.

## Benefits of Cato's EPP Solution

Cato's EPP provides industry leading protection of your endpoints with a single console for management of threats from across your environment. The key benefits of Cato's EPP are:

- Cato's EPP solution is fully managed through the Cato Management Application. Admins can oversee protected endpoints from a unified console, consolidating user data, network information, and security policies.
- With EPP enabled, Cato protects both network traffic and your endpoints ensuring layered protection against attack. Cato utilizes BitDefender to provide industry leading protection against attacks.
- Using Cato's EPP you can consolidate alerts from all entities into a single pane of glass. For example, from the **Events** page, using preset filters, you can view an alert triggered by a malicious document on an endpoint. Then, from the same page view an Anti-Malware alert from a scan of WAN and Internet traffic for potentially malicious files. This enables you to analyze complex threats that span across your endpoints and network.
- As the same user entity is used across the Cato Management Application, this means that alerts also provide a single source of information. For example, adding a filter for a user displays information from EPP as well as Network or Access alerts. This avoids manually searching for the user in multiple vendor console.

## Deploying Cato's EPP Solution

Before deploying Cato's EPP solution, ensure your endpoints meet the [prerequisites](/v1/docs/installing-the-cato-epp-solution). You can then follow these steps to easily start protecting your endpoints with Cato:

### Step 1: Download and Distribute the Client to your Endpoints

Download EPP from the [Client Rollout](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy) page in the Cato Management Application. The Client is associated to your account using a unique token. You can distribute the Client to your endpoints using an MDM or by manually installing it.

For more information, see [Installing the Cato EPP Solution](/v1/docs/installing-the-cato-epp-solution).

### Step 2: Configure How Cato Protects your Endpoints

Cato's EPP utilizes two engines to provide layered protection to your endpoints. Configure the protection level of each engine, create policies and profiles to meet your security requirements. To avoid false positives and to ensure the EPP solution does not block business processes, you can add objects to the allowlist.

For more information, see [Configuring Endpoint Protection](/v1/docs/configuring-endpoint-protection).

### Step 3: Monitor and Respond to Threats

If EPP identifies malicious activity, an **Event** is created. You can review the details from the same page in the Cato Management Application that is used to monitor Network, Security, and Remote Access events.

For more information, see [Monitoring and Responding to Endpoint Protection Threats](/v1/docs/monitoring-and-responding-to-endpoint-protection-threats).

## Understanding the Difference between EPP, EDR, and XDR

To detect, investigate, and prevent attacks in your network you need to use various security features in parallel. EPP, Endpoint Detection and Response (EDR), and Extended Detection and Response (XDR) each have a unique role in protecting your attack surface.

### EPP

EPP protects your endpoints by using multiple security engines to scan files and processes to identify and prevent attacks. If malicious activity is identified it can be blocked with any malicious processes prevented from executing. EPP provides passive protection, scans run automatically without admins taking any action.

Cato's EPP solution uses signature matching to identify threats using known malware signatures and also behavioral analysis to identify processes that are behaving suspiciously.

### EDR

EDR helps you detect and provide visibility for attacks on endpoints. EDR solutions collect data from your endpoints, analyze the data, and provide analytics on the severity and impact of potential threats. EDR requires active protection to analyze data for threats.

Cato can integrate alert data from [Microsoft Defender for Endpoint](/v1/docs/microsoft-defender-for-endpoint-alerts-configuring-the-xops-integration) to generate stories for endpoint devices in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).

### XDR

XDR integrates data from multiple data sources to provide a holistic view of suspicious activity across your account. Correlation engines analyze data and generate a story if a potential threat is identified. The stories contain common properties that relate to the same threat.

Cato's [XDR solution](/v1/docs/reviewing-site-operations-stories) creates stories based in data sources including endpoints, sources in your network, relevant geo-locations, and more.
