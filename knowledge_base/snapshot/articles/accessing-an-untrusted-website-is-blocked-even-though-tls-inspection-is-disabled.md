---
title: "Accessing An Untrusted Website Is Blocked Even Though TLS Inspection Is Disabled"
slug: "accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Accessing An Untrusted Website Is Blocked Even Though TLS Inspection Is Disabled

## Issue

Accessing a website with an untrusted CA or self-signed certificate is blocked by Cato even though TLS inspection is disabled

## Environment

- TLS inspection disabled
- Firewall rule with prompt or block action

## Troubleshooting

- The blockage should generate a TLS sub-type event which may mislead users into thinking that TLS inspection is blocking the traffic even though it's disabled.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12481895282205.png)
- Rightfully by design, when TLS inspection is not enabled, HTTPS requests will not be inspected even when the website in question is using an untrusted certificate, no actions will be performed.
- However, when the traffic matches a Firewall rule that has **Prompt or Block** as the **Action**, this will invoke or trigger TLSi, even though the latter wasn’t enabled. This is because to inject the prompt/block page into the payload, TLSi needs to occur. If it detects the untrusted or self-signed certificate, our algorithm is to block this page even though TLSi wasn't enabled in the first place, because this is a potential security risk.
- The above behavior will be reflected in the event with the **TLS inspection = 1** ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17299956465053.png)
- If the Cato certificate is installed on the client's PC, the user gets the prompt page but after that, they will get an 'Invalid SSL/TLS certificate' error which proves the previous point.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12482000538269.png)![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12481929672861.png)

## Solution

Change the firewall rule action from **prompt/block** to **allow** or create a new rule that contains the target site as App/Category and set the action to **allow**. You can define the site's IP address or Domain in a Custom Application.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12465240043165.png)
