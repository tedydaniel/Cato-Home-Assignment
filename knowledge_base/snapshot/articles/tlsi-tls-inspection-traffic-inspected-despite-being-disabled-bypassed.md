---
title: "TLSi (TLS Inspection) - Traffic Inspected despite being Disabled/Bypassed"
slug: "tlsi-tls-inspection-traffic-inspected-despite-being-disabled-bypassed"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/tlsi-tls-inspection-traffic-inspected-despite-being-disabled-bypassed"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TLSi (TLS Inspection) - Traffic Inspected despite being Disabled/Bypassed

## Issue

You may observe events where **TLSi appears enabled** even though:

- Global TLS Inspection is disabled, or
- The traffic matches a TLS bypass rule, or
- The source OS is one of the default bypassed OS types (for example: **Android, Linux, Unknown OS**).

This behavior is typically identified in **Security / Internet Events**, where the event details show **TLS inspection = 1** and, in some cases, a TLS-related **Block**, **Prompt**, or **Captive Portal** page is presented.

## Environment

One or more of the following conditions may apply:

- TLS Inspection disabled globally or bypassed by OS (for example: Android, Linux, Unknown OS)
- Firewall rules with **Block** or **Prompt** actions
- Captive Portal authentication in use
- Clientless Access (Browser Access)
- Traffic classified as high-risk or prohibited by system security controls
- TLS Inspection–enforcing Global Parameters for specific applications

> [!NOTE]
> Note:
> 
> TLS Inspection in events can reflect system-required inspection for control, enforcement, or security, not necessarily only configured policy inspection.

## Understanding the Behavior

TLS Inspection settings define **policy-based inspection**, but certain traffic flows require **system-level inspection performed by Cato’s security stack** to function correctly. In these cases, TLS Inspection may occur even when it is disabled or bypassed at the tenant policy level.

Per [Cato’s Master Service Agreement (MSA)](https://www.catonetworks.com/msa/) and global security and compliance requirements, access to certain malicious, dangerous, or prohibited destinations is **blocked** by default. To enforce these baseline protections and meet regulatory obligations, Cato may intercept and evaluate traffic using its security stack. As a result, TLS Inspection functions can be reported as active on some block events, even when customer-configured TLS Inspection is disabled.

This behavior is **expected and by design**. It does not indicate that TLS Inspection has been enabled by customer policy or that bypass rules were ignored. Instead, it reflects mandatory system-enforced security controls required to accurately classify and block high-risk traffic while maintaining platform security and compliance. The above behavior will be reflected in the event with the **TLS inspection = 1** [![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32602464544157.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32602464544157.png)

## Scenarios where TLS Inspection is enforced

### Scenario 1: Captive Portal traffic is always inspected

Traffic used for Captive Portal detection and authentication is handled by system rules.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32602464544413.png)

The PoP must:

- Detect authentication requirements
- Inject the Captive Portal page
- Temporarily manage access behavior (for example, Always-On handling)

To support this, the traffic is always passed through the TLS inspection engine, even when:

- The source OS is normally bypassed, or
- Tenant TLS Inspection is disabled or bypassed

This behavior is expected and does not indicate that tenant TLSi policy was ignored.

### Scenario 2: Clientless Access (Browser Access Portal) traffic is always inspected

Traffic for **Clientless Access (Browser Access Portal)** originates from the public Internet and enters the Cato Cloud as untrusted inbound traffic.

For security reasons:

- This traffic is always inspected by system rules, including TLS Inspection
- Tenant TLS Inspection configuration does not apply to these flows

As a result, Events related to Browser Access may show **TLS inspection = 1** even when:

- Global TLS Inspection is disabled, or
- The same destination would normally be bypassed for user traffic via the SDP client ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32602493970077.png)

### Scenario 3: Firewall rules with Block or Prompt actions

For HTTPS traffic, Firewall rules configured with **Block** or **Prompt** actions require TLS Inspection to:

- Accurately classify encrypted traffic
- Inject block or prompt pages back to the user

This TLS termination is performed by **system rules**, not by tenant TLS Inspection policy.

Therefore, Events for flows matching Block or Prompt rules may show **TLS inspection = 1** even when:

- TLS Inspection is globally disabled, or
- A TLS bypass rule applies to the destination

This behavior is required to correctly enforce block/prompt actions for HTTPS traffic.

(See also: [*Accessing an Untrusted Website Is Blocked Even Though TLS Inspection Is Disabled*](/v1/docs/accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled).)

### Scenario 4: Global TLS Inspection policies for specific applications

In addition to tenant-defined TLS Inspection rules, Cato applies **global TLS Inspection policies** for certain applications, such as **Dropbox** and **WhatsApp**.

These policies are used to:

- Ensure consistent security and CASB enforcement
- Handle certificate pinning and application-specific behavior

As a result, traffic to certain applications may be inspected even when:

- TLS Inspection is disabled in the tenant policy, or
- The source OS would normally be bypassed

In Events, this appears as **TLS inspection = 1**, even though no matching tenant-defined TLSi rule is visible.

This behavior is expected and driven by Cato’s global security policies.

## When to Investigate Further

If performance issues are observed (for example, slow application load times) and bypassing cato provides better performance, additional data may be required for support to investigate so please make sure to provide the following :

- What is the performance impact? Is it data loading time or issues with loading content itself ?
- HAR file from the client browser
- Provide an [SSS](/v1/docs/support-self-service-supportme-portal) for support to validate
