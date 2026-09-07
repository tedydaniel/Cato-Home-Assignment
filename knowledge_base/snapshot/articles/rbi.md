---
title: "Securing Browsing Sessions Through RBI"
slug: "securing-browsing-sessions-through-rbi"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/securing-browsing-sessions-through-rbi"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Securing Browsing Sessions Through RBI

## Overview

Remote Browser Isolation (RBI) protects users from web and browser-based threats without blocking Internet access. It prevents attacks such as ransomware, malware, phishing, malicious ads, and cross-site scripting (XSS) by isolating browsing activity from the user’s device. Instead of rendering web pages locally, RBI streams a safe visual representation from a remote environment, keeping harmful code from reaching the endpoint.

This lets users safely access potentially risky or unknown websites while reducing the risk of attack. Cato routes traffic to Uncategorized, Undefined, and Custom Categories destinations through RBI sessions, ensuring no direct browser connection or file system access occurs.

### Understanding How RBI Works

RBI is invoked through the Internet Firewall using the Remote Browsing action. When a rule matches destinations classified as Undefined, Uncategorized, or part of a Custom Category, the traffic is redirected to an isolated browser running in the Cato Cloud. All active web content—HTML, JavaScript, and other dynamic code—executes remotely, and only a safe, visual stream is delivered to the user’s browser. This ensures consistent protection across all users and devices, without requiring endpoint agents or plugins by:

- Executing all code from the website in the isolated browser, and never reaching the user’s device
- Containing malware and exploit attempts within the remote session
- Protecting sensitive data and cookies from theft and injection attacks

### Understanding How RBI Operates with Other Security Protections

Cato’s multi-layered security architecture combines RBI, Intrusion Prevention System (IPS), and Anti-Malware protections to deliver complete threat prevention across the network and web. RBI adds a crucial browser-level defense layer. While IPS and Anti-Malware stop network and file-based threats, RBI isolates and neutralizes attacks that originate through user browsing. Each technology addresses different aspects of the threat landscape:

| Protection Type | Primary Focus | How It Works | Threats Mitigated |
| --- | --- | --- | --- |
| RBI | Web-based and browser threats | Executes web content in a remote environment and streams a safe visual output to the user | Phishing, drive-by downloads, XSS, cookie theft, malicious ads |
| IPS | Network-level threats | Inspects traffic patterns and payloads to detect and block suspicious or exploitative behavior | Exploits, command-and-control (C2) traffic, network intrusions |
| Anti-Malware / Next-Gen Anti-Malware | File-based and payload threats | Uses signature matching, heuristics, and behavior analysis to detect and block malicious files | Viruses, trojans, ransomware, zero-day malware |

### Optimizing RBI Usage for Security and Performance

Cato’s architecture enables selective use of RBI, applying it only where it delivers the greatest security benefit. As using RBI results in higher latency and complexity, Cato leverages its multi-layered protection to isolate only the traffic categories that require it while protecting all other traffic through complementary defenses. RBI can be applied only to Uncategorized, Undefined, and Custom Category destinations. Known and categorized sites continue to be protected by other Cato security layers, including IPS, Next-Gen Anti-Malware, CASB, and DLP.

## Understanding the RBI Solution

Here's an overview of how the RBI process works:

![RBI_Diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31524638765341.png)

| Step | Description |
| --- | --- |
| 1 | The user opens a website in their local browser |
| 2 | The request is forwarded to the RBI service in the cloud |
| 3 | The RBI browser initiates a session with the remote destination |
| 4 | The site’s code executes in the RBI browser (HTML, JS, CSS, etc.) |
| 5 | A safe visual stream is sent to the user’s local browser. The user interacts with the web pages through their device, but their device is not directly interacting with the web pages themselves. |

## Common RBI Use Cases

### Protecting Against Ransomware

Sarah Lee is browsing the internet and visits a website that is categorized as undefined by Cato. The Cato admin configured undefined sites to be delivered by RBI. As she browses the website, exploit kits are silently downloaded onto the remote browser. The kit scans the remote browser and device for vulnerabilities, and after finding a vulnerability, delivers ransomware by exploiting the vulnerability.

The website is rendered in the RBI service via the remote browser and remote device, and only pixels are streamed from the RBI service to Sarah Lee’s local browser and device. The ransomware is isolated and contained in the remote browser and device and doesn’t reach Sarah Lee’s device or her network. She continues to safely interact with the website, as all the website code is executed on the isolated remote browser and device.

### Protecting Against Phishing

John Smith is the CFO and accesses his email that contains a link to a website that looks legitimate, and he clicks the link. He doesn’t realize, but he is the target of a spear-phishing attack.

This link directs him to a website that is defined as uncategorized by Cato. The Cato administrator has configured uncategorized sites to be delivered by RBI. This compromised website redirects his browser session to another malicious website that attempts to steal cookies to impersonate him. Cato’s RBI runs the website’s active code, including HTML, CSS, and JavaScript, in a remote isolated browser and device, while streaming website content to the local browser and device. The attacker has no access to the CFO’s local device or browser or the local network and cannot steal cookies that can be used to impersonate the CFO.

### Restricting Access to Private Apps

A retail company has created a private app to track its inventory, manage logistics, and process orders. The app contains personal information about their customers and is accessed by employees and third-party contractors.

To protect their customer information, the security team creates a rule to ensure the app is only accessed through RBI. They configure RBI to block copy/paste, download, or printing. This ensures private customer data cannot be exfiltrated.

## RBI Supported Browsers

- Cato RBI is supported for browsers only
- Cato RBI supports all modern browser releases of any major desktop browsers (e.g. Chrome, Edge, Firefox, IE, Safari, etc.). Mobile browsers are not supported
- Some old browsers may not comply with the minimum set of requirements for RBI to work properly
- Internet Explorer mode in Microsoft Edge is not supported

## Supported Security Engines in an RBI Session

The following security engines are applied to downloaded content during an RBI session:

- Anti-Malware
- NG Anti-Malware
- Sandbox
