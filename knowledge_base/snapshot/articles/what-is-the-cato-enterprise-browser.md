---
title: "What is the Cato Enterprise Browser"
slug: "what-is-the-cato-enterprise-browser"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/what-is-the-cato-enterprise-browser"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Cato Enterprise Browser

## Overview

Organizations frequently need to provide access to web-based applications for users on unmanaged devices, such as third-party vendors, contractors, guest users, or personal BYOD endpoints. Because these devices are not governed by your organizational security standards, they can introduce risk when accessing corporate resources.

The Cato Enterprise Browser lets you provide secure, policy-controlled access to public SaaS and private WAN applications from any device, without installing an agent such as the Cato Client. Instead of extending controls into an existing browser, you provide users with a dedicated, managed browser workspace for business activity.

Security enforcement remains consistent across all remote users. Internet Firewall, Application Control (CASB), and Data Protection policies are applied as part of a unified policy framework. The same security policies apply to managed devices using the Cato Client and to unmanaged devices using the Enterprise Browser, which simplifies policy enforcement across different user segments. These controls are fully integrated into the Cato platform and enforced across all Cato backbone PoPs worldwide, so Enterprise Browser traffic benefits from the same single-pass inspection and global enforcement as the rest of your Cato services.

Using a separate Enterprise Browser also makes it easy to distinguish between personal and corporate browsing. Users access business applications only through the Cato Enterprise Browser, while personal activity remains in their standard browser. This clear separation helps users understand when they are operating in a controlled corporate environment.

### Cato Enterprise Browser Architecture

The diagram below shows how traffic from the Enterprise Browser is routed through a Cato PoP using a forward proxy, inspected by the Cato SPACE security engines, and then sent to the relevant SaaS or WAN application.

![Enterprise_browser_diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982625114397.png)

You can also require that access to corporate applications originates from the Cato Cloud. For example, you can configure conditional access policies in your IdP or SaaS providers to allow traffic only from Cato-managed IP addresses. For more information, see [IP Allocation Policy for Remote Users](/v1/docs/ip-allocation-policy-for-remote-users).

When a user launches the Cato Enterprise Browser on an unmanaged device and accesses a corporate application, all browser traffic is automatically routed through a Cato PoP.

The traffic flow includes:

- Routing through a forward proxy in the PoP
- Inspection and enforcement by the Cato SPACE security engines
- Secure access to public SaaS applications or private WAN applications

This architecture ensures that enterprise traffic is inspected and controlled before reaching its destination, while keeping corporate access logically separated from personal browsing activity.

## Enforcing Security Controls at the Browser Level

Because the Enterprise Browser is a dedicated, managed browser environment, you can enforce security controls directly at the browser level.

For example, you can restrict:

- Copy and paste
- File downloads
- Printing
- Installation or use of unauthorized browser extensions

This approach gives you stronger control over how applications are accessed and how data is handled, even on unmanaged or contractor devices. It creates a controlled workspace for business activity and helps reduce the risk of data leakage and malicious browser-based activity, while maintaining a seamless user experience.

## Use Case - Securing Contractor Access to Sensitive SaaS Applications

A financial services organization works with external auditors who require access to internal SaaS applications that contain sensitive customer data. Because the auditors use their own unmanaged devices, the organization needs strong controls to prevent data leakage while enabling full application functionality.

The IT team deploys the Cato Enterprise Browser to the auditors. Within the managed browser workspace, they disable copy and paste, block file downloads, and restrict printing for specific applications. Corporate applications open only within the Enterprise Browser, while the auditors’ personal browsing remains in their standard browser.

As a result, auditors can work productively in a secure, controlled environment, while the organization significantly reduces the risk of data exfiltration and browser-based threats.
