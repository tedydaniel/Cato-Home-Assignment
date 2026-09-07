---
title: "How to Solve \"Secure Connection Failed\" Error"
slug: "how-to-solve-secure-connection-failed-error"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-solve-secure-connection-failed-error"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Solve "Secure Connection Failed" Error

Problem Example:

*Secure Connection Failed*

*The connection to website.domain.com was interrupted while the page was loading.*

*The page you are trying to view cannot be shown because the authenticity of the received data could not be verified.*

*Please contact the website owners to inform them of this problem.*

Within the above example, the customer has TLS inspection disabled, yet they are unable to complete/create a secure connection to the HTTPS/TLS based web server. Although this could also occur if/when TLS inspection is enabled, this specific issue is not related to the inspection of TLS. In "normal" circumstances, customer's are used to traffic from their office being sent from a single egress point (firewall). Because of this, traffic always has the same source IP address. SD-WAN, on the other hand, provides benefits that include increased network performance and reduced latency while using multiple points of egress (among other things). In the above example, the TLS handshake is failing because the egress/source IP is changing.

Solution:

Create a Network Rule to route the specific traffic out a single IP address. See [How to Configure an Egress Rule.](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic) All traffic will now be "forced" via that single IP address and should resolve the TLS handshake issue listed above.
