---
title: "Creating Baseline Firewall Rules for Blocking Anonymizers"
slug: "creating-baseline-firewall-rules-for-blocking-anonymizers"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/creating-baseline-firewall-rules-for-blocking-anonymizers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Baseline Firewall Rules for Blocking Anonymizers

## Issue

Anonymization services are often used to bypass various browsing restrictions and internet firewalls. Many respected and popular anonymizers bypass NGFW/traditional firewalls using evasive techniques. These techniques include SNI spoofing, evasive protocols, hiding behind CDNs, and jumping between server IPs. Any anonymization service that can be identified as an application or service by Cato will be categorized under "Anonymizers." For example, ClearVPN, Hola VPN, Mullvad VPN, NordVPN, CyberGhost VPN, TunnelBear VPN, Private Internet Access (PIA), Surfshark VPN, Express VPN, and many more.

This article explains how to create a baseline firewall rule to effectively block anonymization services. However, due to the various evasive techniques employed by anonymizers, successfully blocking all of them can be challenging. If an anonymizer is not blocked despite configuring the baseline rules, please contact [Support](/v1/docs/submitting-a-support-ticket) for assistance.

**NOTE**: TLSi and IPS must also be enabled.

## Solution

To establish baseline protection, two Internet Firewall (IFW) rules need to be created. Additionally, it is best practice to create an Application Control rule, which requires a valid CASB license.

- The first rule blocks the Anonymizer category by using an IFW rule.
- The second rule blocks common protocols and evasive techniques used by anonymizers by using an IFW rule.
- (**Optional**)The third rule blocks the OpenVPN files by using an Application Control Rule. (This requires a valid CASB license)

Cato maintains a curated list of the most commonly used anonymizers. To view this list, go to *Resources > App Catalog* and select "**Anonymizers**" under the "Category."

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20137894678429.png)

For other anonymizers not on this list, we identify them by the protocols and evasion techniques they use. WireGuard, OpenVPN, Evasive DNS, and Evasive TLS are commonly used protocols and techniques by anonymizers to enhance privacy and bypass network restrictions.

### WireGuard

Blocking WireGuard protocol requires blocking WireGuard Protocol in the Internet Firewall rule.

### OpenVPN

OpenVPN is a secure tunnelling protocol used for site-to-site and point-to-point connections. It can communicate via TCP or UDP, and the user can define the port.

Blocking the OpenVPN protocol requires blocking OpenVPN Protocol in the Internet Firewall rule and blocking the OpenVPN Configuration files using the File Control rule.

### Evasive DNS

Many anonymizers use DNS tunneling and other UDP traffic over port 53 (AKA “Evasive DNS”) to evade Firewalls.

### Evasive Traffic over TCP/443

Evasive traffic over port 443 is a technique anonymizers employ to conceal their activities within seemingly legitimate TLS traffic. According to the official RFC, these are not the actual TLS traffic. Many anonymizers use Evasive TLS traffic to bypass the Firewall.

The following are some known anonymizers that can be blocked successfully by blocking the anonymizer category and the respective IFW services.

|  | **Internet Firewall (IFW) Services** |  |  |
| --- | --- | --- | --- |
| **Anonymizers** | **WireGuard Protocol** | **OpenVPN Protocol** | **Evasive DNS** | **Evasive Traffic over TCP/443** | **Configure an IFW rule to block the anonymizer category** | **Remarks** |
| Clear VPN |  |  |  |  | ✔︎ |  |
| Hola VPN |  |  |  |  | ✔︎ | Need to also block the IFW service **HTTP Proxy** |
| Mullvad |  |  |  |  | ✔︎ |  |
| NordVPN | ✔︎ | ✔︎ | ✔︎ | ✔︎ | ✔︎ | “obfuscated servers” mode in Windows will not be blocked |
| CyberGhost VPN | ✔︎ |  |  |  | ✔︎ |  |
| TunnelBear VPN | ✔︎ | ✔︎ |  |  | ✔︎ | Need to also block the IFW services **ISAMP** and **IPsec NAT Traversal**. Need to block IFW Port/Protocol TCP/6418 |
| PIA (Private Internet Access) |  |  |  |  | ✔︎ |  |
| Sufshark VPN | ✔︎ | ✔︎ | ✔︎ |  | ✔︎ |  |
| ExpressVPN |  | ✔︎ |  |  | ✔︎ | Windows Device requires blocking the OpenVPN service in the IFW rule |
| Unlimited VPN | ✔︎ | ✔︎ |  | ✔︎ | ✔︎ | IPS needs to be enabled. Need to also block the IFW services **IPsec NAT Traversal**. |

For anonymizers not listed in the above table, follow the steps below to create the baseline firewall rules for blocking them.

## Rule 1: Block Anonymizer Category

- Navigate to Security > Internet Firewall
- Click on New > New Rule
- Under the App/Category, select Application Category. Then, select Anonymizer from the dropdown list. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20135901495965.png)

## Rule 2: Block Suspicious Services

- Navigate to Security > Internet Firewall
- Click on New > New Rule
- Under Service/Port, configure the following Services ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20135929811229.png)

Once these two rules are configured, they should resemble the example shown below:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20135901500317.png)

**NOTE**: Configuring Rule 2 to Block Suspicious Services may inadvertently block legitimate applications, as these protocols and techniques are not exclusively used by anonymizers. For example, Telegram uses Evasive traffic over TCP/443. As a best practice, we suggest setting the rule to Monitor for a week to identify any false positives. If false positives occur, create an exception in the rule to allow the legitimate application to function properly. After addressing any false positives, change the rule to Block. Refer to [Using Exceptions to Allow Internet Connections](/v1/docs/managing-the-internet-firewall-policy) on how to create an exception rule.

## Rule 3 (Optional): Block OpenVPN Files

- Navigate to Security > Application Control
- Create a new File Control Rule
- Under File Attributes, configure the Content Type Is OpenVPN configuration file. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20625960623901.png)

Once the rule has been configured, it should resemble the example shown below:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20625929803037.png)

**NOTE**:

- A valid CASB license is required.
- TLS inspection needs to be enabled.
