---
title: "Users Are Logged Out of Website After Successful Login"
slug: "users-are-logged-out-of-website-after-successful-login"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/users-are-logged-out-of-website-after-successful-login"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Users Are Logged Out of Website After Successful Login

## **Issue**

Frequent session expiry and unexpected timeouts are seen after logging into a website. This leads to disconnections and logouts whilst connected to the Cato Cloud.

## **Environment**

This article applies to customers accessing the internet while connected to the Cato Cloud.

## **Solution**

When Internet traffic is routed via the Cato Cloud, NAT is conducted by the PoP, and a public IP is assigned from its range. The assignment of a public IP is dynamic, and each traffic flow will attempt to use the **same** public IP.

In rare cases, the dynamic public IP from the PoP may change where the IP is unavailable and NAT is not established for this address. Some websites are sensitive to changes in the source IP, and as a result, the user might get "kicked out" of a session while connecting through the Cato Cloud.

As Cato cannot determine what sites might be sensitive to dynamic client egress IP, the workaround is to set static egress NAT IP for the relevant application/website using network rules. Below is an example of static NAT IP via the Amsterdam PoP:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19588601694493.png)

For further information regarding how to configure network rules with static NAT, please view the article [How to Configure an Egress Rule](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic).

## **Troubleshooting**

If you are experiencing this behavior and want to conduct troubleshooting, or wish to gather information before contacting Cato Support, please verify the following steps:

- What network rule is applied to the application that you having issues with?
  - Confirming the rule will rule out any discrepancies and misconfiguration such as unintended Egress.
- What is the source and destination IPs for this connection?
  - Understanding the endpoint addresses can help identify which rules are being applied to the connection.
- Does the relevant rule have static NAT egress defined?
  - The relevant network rule would be expected to **NOT** have static NAT egress defined, as some applications have issues with Cato's dynamic routing.
  - Example applications that have been identified to have this behaviour include UtilPro.
