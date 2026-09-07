---
title: "Customizing the DNS Protections for IPS"
slug: "customizing-the-dns-protections-for-ips"
updated: 2026-07-09T08:13:47Z
published: 2026-07-09T08:13:47Z
canonical: "knowledge.catonetworks.com/customizing-the-dns-protections-for-ips"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Customizing the DNS Protections for IPS

This article explains how to choose which DNS protections your account enforces as part of the IPS service.

## Overview of DNS Protection

Cato's DNS Protection enhances the IPS service and gives you granular control over the level of security for DNS traffic in your account. DNS Protection applies irrespective of the [DNS server](/v1/docs/what-is-cato-dns) you use, i.e it applies for Cato DNS server, and both trusted and untrusted servers.

Cato continually updates DNS domains and categories and adds new types of protections to the DNS Protection page.

DNS Protection provides robust security by blocking DNS requests before there is a connection between the host and the malicious server (no TCP or UDP handshake). When DNS Protection is disabled, the IPS service still provides some protections for DNS threats, however it doesn't cover all the threats covered by DNS Protection, and they are blocked at a later stage when the destination is accessed. Therefore, we recommend as a best practice to enable both IPS and DNS Protection.

You can use the [Threat Catalog](/v1/docs/using-the-threat-catalog) to see the DNS protections included in the basic IPS service and those included in DNS Protection.

### Understanding DNS Protection Types

You can enable or disable each of these specific DNS protections to meet your security requirements.

- **Malicious Domains**: Detects DNS requests to domains that are known to host or distribute malicious content. Blocking these requests helps prevent users and devices from connecting to destinations used for malware, exploits, or other threats.
- **Newly Registered Domains**: Detects DNS requests to domains that were recently registered and may not yet have an established reputation. Attackers often use newly registered domains for short-lived campaigns, phishing, malware delivery, or command and control activity.
  - To give you more control over how aggressively DNS Protection identifies and blocks risky domains, configure a threshold to block domains registered within the last 7, 14, 21, 30, or 60 days.
- **Crypto Miners**: Detects DNS requests to domains associated with cryptocurrency mining activity. This helps identify and block unauthorized mining software that can consume device resources, degrade performance, and indicate a compromised host.
- **Command and Control (C&C)**: Detects DNS requests to domains used by malware to communicate with attacker-controlled infrastructure. This protection also includes DNS Fast-Flux domains, where attackers rapidly change DNS records to hide malicious servers and make takedown more difficult.
- **Domain Generation Algorithms**: Detects DNS requests to algorithmically generated domains commonly used by malware to locate command and control servers. Blocking these domains helps disrupt malware communication, even when the attacker frequently changes the active domain names.
- **Phishing**: Detects DNS requests to domains that are used to impersonate trusted websites and steal credentials or sensitive information. This protection also includes DNS re-binding attacks, where malicious domains attempt to bypass browser protections and access internal resources.
- **Dynamic DNS**: Detects DNS requests to domains that use dynamic DNS services, where domain records can frequently change to point to different IP addresses. While dynamic DNS can be legitimate, attackers often use it to quickly move malicious infrastructure and avoid detection.
- **DNS Tunneling**: Detects DNS traffic that attempts to tunnel data through DNS queries and responses. This protection also includes ultra-slow DNS tunneling techniques, where data is exfiltrated gradually to avoid triggering volume-based detections.

### DNS Sinkholing

When a DNS request is blocked, it is often not possible to identify the IP address of the original host making the request, due to the request passing from the host through other devices such as private DNS servers or access points. Cato provides a DNS sinkholing option that solves this issue and identifies the IP addresses of infected hosts on the network issuing malicious DNS requests.

#### How Does Sinkholing Work?

When a DNS protection is set to the **Sinkhole** action, the DNS Protection engine returns a forged response to the host querying the malicious domain, resolving the query to the IP address of a designated Cato sinkhole server. Cato pushes an IP in the Cato [system range](/v1/docs/working-with-the-cato-system-range) (such as 10.254.x.x) to the host. The host then attempts to connect directly over the Internet to that IP address, enabling the IPS service to identify the host IP address. The service blocks the traffic and reports the host IP address as the **Source IP** in the event log.

#### Understanding Sinkhole Events

When the **Sinkhole** action is performed, two events are generated. The first event reports the execution of the **Sinkhole** action taken when the host initially queries the malicious destination, and the **Source IP** field may not reflect the address of the client host. The second event reports that the DNS request was blocked when the host attempted to connect to the sinkhole server, and the action for the event is also **Sinkhole**. This second event reports the actual host IP address in the **Source IP** field. This lets you easily identify infected hosts on your network by filtering the [Events](/v1/docs/analyzing-events-in-your-network) page to show events for all traffic connecting to the sinkhole server IP address.

For more about DNS Protection events, see below [Analyzing DNS Protection Events](/v1/docs/customizing-the-dns-protections-for-ips#h_01KV2WBRCC9QNQCGV7XX311M5X).

#### End-user Experience of the Block and Sinkhole Actions

When the IPS engine blocks a DNS request, the connection to the domain is dropped before the end-user receives a DNS response.

When a DNS request is sinkholed, the end-user receives a DNS response, and the connection is dropped when the host attempts to connect to the sinkhole server.

### Prerequisites

- DNS Protection is included in the IPS license. For more about purchasing the IPS license, please contact your Cato representative.

### Sample Workflow for Malicious Domains

This is an example of the workflow for the **Malicious Domains** DNS protection, and when a host tries to access a malicious domain.

1. The host device tries to access a malicious domain from the browser.
2. The IPS engine identifies that there is a DNS request to a malicious domain and blocks the DNS request.
3. The DNS request is blocked before there is a connection between the host and the malicious server (no TCP or UDP handshake).

## Defining the DNS Protections for Your Account

Use the DNS Protection page to select which types of DNS Protections the IPS engine enforces for your account. When you enable DNS Protection for your account, the IPS engine inspects every DNS request sent over the Cato Cloud. DNS requests are inspected also for accounts that don't use Cato as their DNS server, and use a private DNS server instead.

For each DNS protection, you can set one of the following actions:

- **Allow** - The IPS engine does not enforce the protection, however, an event is generated to let you monitor the traffic.
- **Block** - The IPS engine blocks the DNS requests for traffic that matches the protection, and an event is generated.
- **Sinkhole** - The DNS request is first diverted to the sinkhole server, then the traffic attempting to connect to the server is blocked. A separate event is generated for each phase of the **Sinkhole** action. For more information, see above [DNS Sinkholing](/v1/docs/customizing-the-dns-protections-for-ips#h_01KV2WBRCCH3FW8A6PB365SCAX).

**Default Settings for DNS Protections**

The Cato Security team defines the default action for each DNS protection based on the potential to impact legitimate traffic in your organization.

- Default Block action - Protections that are assigned the **Block** action by default, generally have few false positives and will not impact legitimate traffic. We recommend that you leave these DNS protections with the default Block action.
- Default Allow action - Protections that are assigned the **Allow** action by default may generate false positives and it's possible that they could block legitimate traffic in your organization. We recommend that before you change these protections to the **Block** action, first run these DNS protections for a few weeks with the **Allow** action and review the events to monitor the number of false positive matches.

![DNS_Protection_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35722815105565(1).png)

**To define the DNS Protections for your account:**

1. From the navigation pane, select **Security > DNS Protection**.
2. Click the slider to enable (green) or disable (gray) the **DNS Protection** policy for the account.
3. To customize a DNS protection type, click the **Action** or **Track** for that row.

The panel opens for that DNS protection type.
  1. In the **Action** section, select to **Allow**, **Block**, or **SInkhole** the DNS traffic that matches the protection. Note: If you have set an action for Newly Registered Domains, configure the threshold to block domains registered within the last 14, 21, or 30 days.
  2. In the **Track** section, select if you want to [send email notifications](/v1/docs/account-level-alerts-and-system-notifications) for DNS traffic that matches the protection.
4. Click **Apply** and then click **Save**.

## Allowlisting DNS Traffic

You can create an IPS Allowlist rule on the IPS page to define an exception and allow DNS traffic with a specific DNS Protection signature, or you can allowlist a DNS Protection signature from a block event log. For more about creating IPS Allowlist rules, see [Allowlisting IPS Signatures](/v1/docs/allowlisting-ips-signatures).

You can also allowlist specific trusted domain names in the IPS Allow List to exclude them from DNS Protection scans.

**To allowlist specific domain names:**

1. From the navigation menu, click **Security > IPS**.
2. Click **New**. The **New Allow List** panel opens.
3. Enter the **Name** for the rule.
4. Select the **Scope** of the rule as follows:
  - For traffic configured to use the default Cato DNS server or a private DNS server, select **Wan**
  - For traffic configured to use a public DNS server, select **Outbound**
5. Under **Destination**, select Domain, and add the required domain name.
6. Click **Apply**. The IPS allowlist rule is added to the rulebase.
7. Click **Save**.

## Monitoring DNS Protections with the Threats Dashboard

The [Threats Dashboard](/v1/docs/using-the-security-threats-dashboard) includes the following three widgets to help you monitor the status of the DNS protections in your account:

- **Threats Type** - Shows the name of the type of DNS category and the number of events for each type
- **Top Domains** - Shows a list of the top domains that were blocked with the number of DNS protection events for each domain
- **Top Hosts** - Shows a list of the top hosts (source IP address) with the number of DNS protection events for each host

![Threats_Dashboard_-_DNS.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35722837854749(1).png)

## Analyzing DNS Protection Events

The **Home > Events** page shows all the DNS Protection events for your account. The powerful search tools let you drill-down and identify the key events that contain the relevant data that you need.

DNS Protection events can be identified by the following fields:

- Event Type - Security
- Sub-Type - DNS Protection
- DNS Protection Category - Cato’s DNS Protection type that matched the DNS request
- DNS Query - Domain queried in the DNS request

You can learn more about using the Events page [here](/v1/docs/analyzing-events-in-your-network). You can use the **DNS Protection** preset to filter the events.
