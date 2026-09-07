---
title: "Selecting the Connection Type for a Site"
slug: "selecting-the-connection-type-for-a-site"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/selecting-the-connection-type-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Selecting the Connection Type for a Site

The Connection Type for each physical or cloud-based site defines how that site connects to the Cato Cloud. The following table lists the Connection Types and the supported features:

| Connection Type | Multiple WAN | Bypass | Local Port Forwarding | Networks |
| --- | --- | --- | --- | --- |
| Socket X1500, X1600, X1700 | Yes | Yes | Yes | Full |
| AWS/Azure/ESX vSocket | Yes | Yes | Yes | Full |
| Cato-initiated IPsec IKEv1 | - | - | - | Partial |
| IPSec IKEv2 | - | - | - | Partial |

### Which IPsec Connection Type Do I Use?

Using the correct IPsec Connection Type depends on the environment and firewall that is involved in connecting the site to the Cato Cloud. In general, IPsec IKEv2 is the more robust and we recommend that you use it whenever possible for the Connection Type. However, it is not always supported - for example Azure only supports IKEv1 for policy-based VPN gateways.

For sites that use IPsec IKEv1, the option is Cato-initiated Connection Type. This means that the Cato Cloud initiates the connection with the site and easily handles failovers to another link.

For Cisco ASA appliances, there is a known incompatibility with Cato IKEv2 sites, [read more](/docs/selecting-the-connection-type-for-a-site#UUID-ea6a83c8-e0f7-2d7d-7799-8a52c294a61d).
