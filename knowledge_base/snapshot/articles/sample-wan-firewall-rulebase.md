---
title: "Sample WAN Firewall Rulebase"
slug: "sample-wan-firewall-rulebase"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/sample-wan-firewall-rulebase"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sample WAN Firewall Rulebase

This article shows an example of a WAN firewall rulebase.

## Details for Sample WAN Firewall Rulebase

This section shows and explains the settings for a sample rulebase for the WAN firewall. The **Time**, **Track**, and **Enabled** settings are not shown. All of these rules allow traffic in both directions.

| # (rule number) | Name | Source | Destination | App/Category | Service/Port | Action |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Allow IT remote access | IT group | All Sites system group | Any | Any | Allow |
| 2 | Remote access to AWS Transit | All VPN Users system group | AWS Transit Gateway site | Any | Any | Allow |
| 2 exception | Exception: Remote access to AWS Transit | Finance Temps group | AWS Transit Gateway site | Any | Any | N/A |
| 3 | Corporate WAN | All Sites system group | HQ site | Backup Services, Voip Video | Any | Allow |
| 4 | Finance access | Finance group | Finance Server host | Any | HTTP, HTTPS, SMTP | Allow |
| 5 | Marketing access | Marketing group | HQ\LAN\Marketing Segment subnet | Any | HTTP, HTTPS, SMTP, FTP, TFTP | Allow |

- Rule 1 - Allows traffic from the members of the **IT** group to the **All Sites** system group (includes all sites in the account).
- Rule 2 - Allows traffic from the **All VPN Users** system group (includes all SDP users in the account) to the **AWS Transit Gateway** site.
- Rule 2 exception - Ignores the Allow action for the users in the **Finance Temps** group to the **AWS Transit Gateway** site. These users are blocked and cannot access this site.
- Rule 3 - Allows traffic from the **All Sites** system group to the **HQ** site. The allowed traffic includes the **Backup Services** custom application, and the default **Voip Video** category.
- Rule 4 - Allows and logs traffic from the custom **Finance** group to the **Finance Server** host in the HQ site. Only HTTP, HTTPS, and SMTP services are allowed for these connections. The **Track** action is set to **Event**, and each connection generates an event.
- Rule 5 - Allows traffic from the custom **Marketing** group to the **Marketing Segment** subnet for the network in the HQ site. Only HTTP, HTTPS, SMTP, FTP, and TFTP services are allowed for these connections.
