---
title: "Recommendations for Internet and WAN Firewall Policies"
slug: "recommendations-for-internet-and-wan-firewall-policies"
tags: ["Best Practices", "Internet Security"]
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/recommendations-for-internet-and-wan-firewall-policies"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recommendations for Internet and WAN Firewall Policies

## Overview

Firewalls play a key role in securing your corporate networks and protecting internal resources. This article contains recommendations and best practices to help you create the strongest security policy for your organization. We also explain how to keep your firewall policies clean and manageable.

The Internet firewall helps you manage access for users and devices in your network to a wide variety of web services, applications, and content. The WAN firewall lets you manage the WAN traffic for internal resources and between users and sites. This guide helps you configure and fine-tune the rules in each firewall to maximize the effectiveness of the security policy.

For more information about specific rule settings, see [Reference for Rule Objects](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings).

The Best Practices page in the Cato Management Application (CMA) shows a number of firewall checks, and if your account complies with them, for more information, see [Reviewing Best Practices for Your Account in the CMA](/v1/docs/reviewing-posture-checks-for-your-account).

### Planning the Firewall Security Policy

There are two approaches to firewall rulebases: allowlist and blocklist. Allowlisting the firewall rulebase means that the rules define which traffic the firewall allows. All other traffic is blocked by the firewall. Blocklisting the firewall rulebase is the opposite, the rules define the traffic that is blocked. All other traffic is allowed by the firewall. Organizations choose the approach that is the best fit for their specific needs and situations.

- An allowlist security policy has an ANY ANY Block rule as the final rule to block all traffic that doesn't match an allow rule
- A blocklist security policy has an ANY ANY Allow rule as the final rule to allow all traffic that doesn't match a block rule

The recommendations for each approach are discussed below in the respective sections for the Internet and WAN firewalls.

### Traditional vs. NG Firewall Rules

Cato's Internet and WAN firewalls use two different types of firewall rules:

- Traditional firewall rules (also known as simple rules)
- Next-Generation (NG) firewall rules (also known as complex rules)

This section describes the differences between these rule types and the logic that the firewall uses to apply them to network traffic.

#### Traditional Firewall Rules - Inspecting the First Packet

Cato lets you define a network security policy and configure traditional firewall rules to control incoming and outgoing traffic in your network. Cato’s traditional firewall rules only have one or more of the following settings:

- IP Range
- ASN
- Countries
- Site
- Host
- Protocol/Port
  - Available protocols: TCP, UDP, TCP/UDP, and ICMP

The traditional firewall engine evaluates the traffic on the first packet. For example, network administrators can configure firewall rules that are based on protocols and ports. For this kind of rule, the firewall decides to allow or block the traffic based on the first packet.

The following screenshot shows an example of a traditional WAN firewall rule that blocks TCP traffic on port 80:

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209968127133.png)

The following figure shows an example of a TCP connection from Host A to Host B and the point for the traditional firewall engine to evaluate a Block rule:

![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209927584669.png)

> [!NOTE]
> Note:
> 
> The traditional firewall engine doesn’t drop the packets. The PoP completes the TCP handshake without sending any packets to the destination (Host B). The reason for that is to display the Internet redirect page for block or prompt actions. For more about the redirect page, see [Customizing the Warning / Block Page](/v1/docs/customizing-the-warning-block-page-branding).

#### NG Firewall Rules - Deep Packet Inspection

Cato’s NG firewall engine is stateful and uses application-layer data inspection for full awareness and control of applications and services. It applies deep packet inspection (DPI) and multiple security engines to inspect the traffic. The key element of the NG firewall engine is application awareness, which lets you define rules that allow or block traffic based on applications and services. The NG firewall engine inspects the packet content based on applications, custom applications, categories, custom categories, services, FQDN, domain, and more. For example, you can define a rule to block uTorrent application traffic in your network. To inspect the data content of the communication flow, the firewall evaluates multiple packets in the flow, including packets that can help identify the application and other attributes of the content payload.

The following figure shows an example of a TCP connection from Host A to Host B and the point for the NG firewall to evaluate a Block rule:

![mceclip3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209910765853.png)

## Best Practices for Internet and WAN Traffic

This section contains best practices for a strong security policy that are relevant to the Internet and WAN firewalls.

### Ordering the Firewall Rules

The WAN and Internet firewalls in Cato Networks are ordered firewalls. The firewall inspects connections sequentially and checks to see if the connection matches a rule. For example, if a connection matches rule #3, the action is applied to the connection, and the firewall stops inspecting it. The firewall does not continue to apply rules #4 and below to the connection.

When the firewall rules are in the wrong order, you can accidentally block or allow traffic. This can lead to a bad user experience or create security risks. For more about ordering the firewall rules, see the [firewall Knowledge Base articles](/v1/docs/cato-firewalls).

This is the recommended rulebase order for most cases:

- Specific block rules
- General allow rules
- Specific allow rules
- ANY ANY rule
  - Allowlist (default WAN firewall) uses a final block rule
  - Blocklist (default Internet firewall) users with a final allow rule

#### Prioritizing Traditional Firewall Rules

Since the Cato firewall follows an ordered rulebase, if you configure the NG firewall rules before the traditional firewall rules, the DPI engine inspects the traffic to identify the application or service before it applies the action. This means that the first packet can pass through and reach the destination. Therefore, for traditional rules to properly protect your network and apply the action on the first packet, they need to have a high priority and be located at the top of the rulebase (before any NG firewall rules). We recommend that you place all the traditional firewall rules at the top of the rulebase before the NG firewall rules.

For more information, see above [Traditional vs. NG Firewall Rules](/v1/docs/recommendations-for-internet-and-wan-firewall-policies#traditional-vs-ng-firewall-rules).

### DNS Security for WAN and Internet Firewall

Cato also recommends these configurations for the WAN and Internet firewall to further mitigate risks related to DNS traffic:

- Block evasive uses of DNS by restricting the **DNS over HTTPS - DoH** service in the firewall policies
- In the Internet firewall, block the **Parked domain Application** category for DNS traffic

![block_parked.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209955927965.png)
- Correctly define WAN segmentations to block DNS rebinding attacks

### Maximum Number of Predicates per Firewall Rule

The WAN and Internet Firewall policies support up to 128 predicates per rule each.

Predicates are the types of settings defined for a rule, and elements are the total number of items. For example, a rule with 100 users and 10 sites has 110 elements and 2 predicates (user and site).

Groups and advanced groups each count as a single predicate.

### Monitoring Traffic

The **Track** option for firewall rules lets you monitor and analyze the firewall traffic events and notifications. We recommend that you configure rules to generate events for the **Block** action to easily monitor the sources that are trying to reach restricted content. You can also configure events and notifications for rules that handle traffic with significant security risks.

As a best practice, we recommend using monitoring to log all internet traffic. To implement this, add an explicit ANY-ANY Allow rule as the final Internet Firewall rule and configure it to generate events. This provides visibility for all Internet traffic on your network so you can understand how to better protect the network and users while maintaining usability.

For more information about email notifications and events, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).

### Scheduling Time Constraints for Rules

The **Time** setting lets you define a specific time range for the firewall rule. Outside of the time range, the firewall ignores this rule. This feature lets you limit Internet access and improve access control in your network. For example, you can define a rule in the Internet firewall that only blocks access to the Social category during regular work hours. Or you can create a rule in the WAN firewall that only allows access to a cloud data center during work hours. The **Actions** section for a rule provides a preset option to **Limit to working hours**.

You can also schedule **Custom** time constraints and limit the rule to the specified hours. Make sure that the **From** time is set earlier than the **To** time, otherwise, the rule will not function properly. If you want to create a constraint spanning the end of one day and the beginning of the next, create two rules and define a constraint for the relevant hours for each day. For example, one rule with a constraint defined from 23:00-23:59 on Monday, and a second rule with a constraint defined from 00:00 to 01:00 on Tuesday.

> [!NOTE]
> Note:
> 
> Time-Constrained Firewall rules have different classifications based on the user type:
> 
> - For sites, the configured time-zone will be used to enforce time-constrained firewall rules
> - For ZTNA users, the time-constrained firewall rules will be based on the geo-location of their public IP address. If this is not available, the geo-location of the account's timezone is used.

### Simplifying Firewall Management

A simple and clean firewall rulebase helps implement a strong security policy because it’s easier to manage and reduces confusion. The recommendations in this section help you create a clear and consistent security policy and avoid mistakes.

#### Avoid Confusing Rule Names

When you create a rule, give it a specific and unique name. Self-explanatory rule names let other administrators on the team easily understand the purpose of the rule. Poorly named rules can cause mistakes and create confusion.

For example, name an Internet firewall rule that blocks gambling websites **Block Gambling** instead of the unclear **Blocked Websites**.

#### Don’t Disable, Delete

Each individual firewall rule can be disabled or enabled. However, we recommend that you only disable rules for a short period of time. For rules that are obsolete and no longer in use, delete them from the rulebase instead of disabling them. Disabled rules make the rulebase more complex and harder to manage.

#### Use Groups

When you create a firewall rule, use a Group of users or sites and restrict network access for the members of this group. For example, you can create a group of users (**Resources > Groups**) and block the internet access for this group only.

#### Name Rules with Exceptions Clearly

Exceptions are powerful tools for firewall rules, but they can make the rulebase difficult to read. In the cases that you use exceptions in rules, name the rules so that it's obvious they contain exceptions. For example, **Block Social (with except)**.

#### Avoid Having a Very High Number of Rules

While there is no limitation on the number of rules that can be added to a firewall policy, an extremely high number may result in performance issues and make the policy difficult to manage. We recommend designing the rulebase to avoid needing a very high number of rules.

## Securing Internet Traffic

The Cato Internet firewall inspects the Internet traffic and lets you create rules to control Internet access. The Internet firewall is based on a set of security rules that let you allow or block access from sites and users to websites, categories, applications, and so on. The default approach of the Internet firewall is blocklist (ANY ANY Allow).

The following screenshot shows a sample Internet firewall policy in the CMA (**Security > Internet Firewall**):

![DefaultInternetFirewall.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209910926109.png)

### 

**​​Note:​​** A system rule at the top of the Internet firewall rulebase. This rule automatically blocks potentially illegal or malicious traffic as defined by the Cato Networks Master Service Agreement (MSA).

### Best Practices for Cato Internet Firewall Policy

The section contains best practices to help you secure Internet access for your account.

#### Managing QUIC Traffic in Cato

QUIC is a new multiplexed transport built on top of UDP. HTTP/3 is designed to take advantage of QUIC's features, including the lack of Head-Of-Line blocking between streams. The QUIC project started as an alternative to TCP+TLS+HTTP/2, with the goal of improving user experience, particularly page load times. Cato can identify and block QUIC traffic as well as GQUIC (Google QUIC) traffic.

To manage QUIC traffic in a firewall or network rule, use the service **QUIC** and application **GQUIC** in the relevant rules. These are examples of Internet firewall rules blocking QUIC traffic for an account:

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209927897757.png)

Since the QUIC protocol works over UDP 443, encapsulated HTTP traffic is not parsed. This means that the Application Analytics screen shows only entries for the QUIC traffic instead of the application itself.

We therefore recommend creating specific rules to block QUIC and GQUIC traffic, so that the browser uses the default HTTP version instead of HTTP 3.0 and QUIC. This provides detailed analytics for the applications used, instead of just reporting on the usage of the QUIC service or GQUIC application.

#### Avoiding ANY as a Source in Internet Rules

For rules that allow Internet access, we recommend that you select a specific site, host or user in the **Source** column, instead of using the option **Any**. Rules that allow any traffic to the Internet are a potential security risk because you are allowing traffic from unexpected sources.

The following screenshot shows a rule where the **Source** column is set to the groups **All Sites** and **All SDP Users** instead of **Any**:

![group_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209911039005.png)

> [!NOTE]
> Note:
> 
> If you add new sites to your account, remember to also add them to the relevant Internet firewall rules.

#### Improving Event Data with Granular Rules

Internet Firewall rules that use **Any** in some settings can generate events that don't include important and useful information. For example, a rule configured with **Any** application might generate events that don't identify the app in the traffic flow. This happens because the firewall triggers the rule before it completes the app identification, since any application matches the rule. Then, when the Cato security stack completes the app identification process, this application usage data is included in the [Application Analytics](/v1/docs/understanding-app-analytics) screen. However, the events don't include all the same information, and then it may be difficult to continue to further investigate the application usage.

To help improve analysis of app usage, we recommend that you minimize **Any** for rule conditions and instead use granular rules with specific apps, services, ports, and so on.

#### Limiting Outbound Internet Traffic

When it is necessary to configure firewall rules that allow any Internet outbound traffic for a specific service or port, we recommend that you block categories or applications that are potential security risks.

For example, if you have a rule that allows all HTTP traffic, add an exception to the rule for categories such as: Cheating, Gambling, Violence and Hate, Parked Domains, Nudity, Weapons, Sex Education, Cults, and Anonymizers. These are examples of categories that can contain malicious content, and the exception blocks Internet access for these categories.

#### Using Secure Protocols

In general, we recommend that for rules that allow Internet traffic, use secure, encrypted protocols instead of regular plain text protocols. For example, use FTPS instead of FTP, or SSH instead of Telnet or SNMP. Internet traffic that is allowed with secure protocols is encrypted and very difficult for hackers to intercept and decrypt.

#### Prompting Users for Access to Risky Websites

If you have a rule that allows access to websites with a minor security risk, we recommend that you use the **Prompt** action instead of **Allow**. When users try to access one of these websites, the **Prompt** action redirects the users to a web page where they decide whether to continue or not. Because these websites add a security risk for your network, we recommend that you track events for traffic that matches this rule.

For the **Prompt** action to function properly, we recommend that you install the Cato certificate on all supported devices.

#### Simplifying Rule Management by Using Custom Categories

When you include many categories in a rule, it makes the rulebase harder to manage. You can instead define a Custom Category that contains all of the relevant categories, and then add this single Custom Category to the rule. Defining simple rules that use one Custom Category makes the rulebase easy to read and search.

For example, you can create a Custom Category named **Internet Profile** that contains all the categories, apps, and services you want to allow access to, and then add the Custom Category to the relevant Internet firewall rule. To keep the rule up to date, you can simply edit the Custom Category and remove or add the necessary updates.

These are additional suggestions for rules that implement best practices using Custom Categories:

- Create a rule for all traffic you want to define with the **Prompt** action. Then create a Custom Category named **Prompt Sites** that contains all relevant URLs and categories, and add it to the rule. Recommended categories for the **Prompt** action include: Cheating, Gambling, Violence and Hate, Tasteless, Parked Domains, Weapons, Sex Education, Cults, and Anonymizers. Configure tracking for the rule to generate events for matching traffic.
- Create a rule for all traffic you want to define with the **Block** action. Then create a Custom Category named **Block Sites** that contains all relevant URLs and categories, and add it to the rule. Recommended categories for the **Block** action include: Botnets, Compromised, Porn, Keyloggers, Malware, Phishing, Spyware, Illegal Drugs, Hacking, SPAM, Questionable. Configure tracking for the rule to generate events for matching traffic.

The final rule in the Internet firewall is an implicit Any - Any - Allow rule, nevertheless we recommend that you add an explicit Any - Any - Allow rule as the final rule. This way, you can easily log ALL Internet traffic, just select Track Events for all the rules.

### Blocking Top-Level Domains (TLDs)

The Internet Firewall in Cato makes it simple and effective to block entire top-level domains (TLDs), such as `.shop`, `.info`, or country-code TLDs like `.cg` (Congo). This capability enhances security by enabling organizations to proactively prevent access to high-risk or undesired TLDs across their networks.

To block a TLD, define the **Domain** for the **App/Category** of an Internet Firewall rule. There is no need to use a wildcard (e.g., ***.info**); subdomains are automatically included. This means that adding **info** will block **example.info**, **subdomain.example.info**, and any other domain under the **.info** TLD.

The Internet Firewall blocks outbound traffic to domains under the specified TLD. It does not block inbound traffic. Blocking a country by the domain relies on the domain name itself rather than IP-based filtering.

![FW_TLD.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209928028189.png)

The example above shows domains that can be added to a block rule with this behavior:

- **info** blocks all **.info** domains
- **shop** blocks all **.shop** domains
- **cg** blocks all **.cg** (Congo) domains

### Allowlisting Internet Traffic

Implementing an Internet firewall with allowlist behavior means that by default, the firewall blocks all Internet traffic. Add rules to the firewall that specifically allow Internet traffic according to the needs of the corporate security policy.

To implement an allowlist Internet firewall in the CMA, the final rule at the bottom of the rulebase must be an explicit rule that blocks any traffic from any source to any destination. See the following example:

![any_any_block_int.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209956229789.png)

We also recommend that you enable tracking for the final rule to generate events that help you monitor and analyze Internet traffic on your network.

### Recommended Rules for an Allowlist Internet Firewall

This section discusses rules that we recommend that you include in rulebases for the Internet firewall that use the allowlist approach.

#### Restricting Websites and Apps

When allowing HTTP and HTTPS traffic, we recommend that you block websites that contain risky and inappropriate content. These websites are typically blocked by businesses and can also be potential sources of malware. Each category (**Resources > Categories**) contains a variety of websites and applications that you can easily add to rules. Categories include, for example, Botnets, Compromised, Porn, Keyloggers, Malware, Phishing, Spyware, Illegal Drugs, Hacking, SPAM, and Questionable.

#### Allowing DNS Traffic

At the top of the rulebase, make sure that there’s a rule to allow all DNS services as part of the Internet traffic.

The following screenshot shows an example rule allowing DNS traffic:

![DNS_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209956300189.png)

#### Allowing Services

Create a rule to allow the services that are used by your account and require access to the Internet. In addition, if there are services that are only used for specific sites, then you can create a separate rule that only allows access for those sites.

#### Allowing Applications

Add the applications that are used by your organization to the Internet firewall rules from the predefined applications list. Cato continuously updates this list with new applications. If you need an application that doesn’t appear in the list, you can define a custom application. For more information about configuring custom apps, see [Working with Custom Apps](/v1/docs/working-with-custom-apps).

### Blocklisting Internet Traffic

Implementing an Internet firewall with blocklist behavior means that, by default, the firewall allows all Internet traffic. Add rules to the firewall that specifically block Internet traffic according to the needs of your corporate security policy. Blocklisting is the default structure for the Internet firewall, it allows any traffic that isn’t blocked by a rule.

In addition, we recommend that you use a learning period to identify unwanted Internet traffic. During this learning period, temporarily add a rule at the bottom of the rulebase that allows any traffic from any source to any destination with tracking enabled. This rule generates an event for every connection that is allowed to access the Internet. When you review the Internet traffic for your account, if you identify unwanted traffic, you can then add a rule to block it.

For more information about firewall events, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

### Recommended Rules for Blocklist Internet Firewall

This section describes rules that we recommend you include in rulebases for the Internet firewall that use the blocklist approach.

#### Blocking Services with Known Vulnerabilities

Services such as Telnet and SNMP v1 & v2 are potential security risks, and they can be blocked in Internet rulebases. If your organization requires access to these services, we recommend that you add an exception to the block rule for those specific users or groups.

The following screenshot shows a sample rule blocking Telnet and SNMP traffic, with an exception that allows access for the IT Department:

![Block_Telnet.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209968804253.png)

#### Blocking Uncategorized Web Content

The category **Uncategorized** contains websites that are not assigned to an existing category from the list of categories. These websites can be a potential security risk for your network. Create a rule that blocks the category **Uncategorized** for all Internet traffic.

You can also use Cato's RBI service to enable safe access to **Uncategorized** sites. For more information about RBI, see [Securing Browsing Sessions Through Remote Browser Isolation (RBI)](/v1/docs/securing-browsing-sessions-through-rbi).

#### Using Geo-Location to Block Countries

There are several countries that are known to generate malicious traffic. If your organization doesn’t have business with these countries, we recommend that you block Internet access to them and reduce potential malicious traffic. You can create a rule that uses the **Country** setting in the **App / Category** section to block Internet traffic to the specified countries.

If you want to block traffic from a specific country, but allow access to a specific FQDN, create an rule with the required FQDN with an Allow action. Then create a lower priority rule that blocks the country.

![countries.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209911366813.png)

> [!NOTE]
> Note:
> 
> To block all Internet access to a country, make sure that the geo-location rule is higher in the rulebase than rules with an allow or prompt action.

## Securing WAN Traffic

Cato’s WAN firewall is responsible for controlling the traffic between the different network elements that are connected to the Cato Cloud. With the WAN firewall, you can control the WAN traffic over your network and achieve optimal network security.

The WAN firewall uses the ANY ANY Block (allowlist) approach by default. This means that any connectivity between sites and users is blocked unless you define specific WAN firewall rules that allow the connections.

The following screenshot shows an example WAN firewall policy in the CMA (**Security > WAN Firewall**)

![wan_fw.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209968928157.png)

### Best Practices for Cato WAN Firewall Policy

This section contains best practices to help you secure the WAN connectivity for your account.

#### Allowing Specific Traffic Between Sites and Users

The golden rule for the WAN firewall is to allow only the desired traffic. For these allow rules, add specific services and ports that are used and provide enhanced secured connectivity for the WAN firewall.

The following screenshot shows a sample WAN firewall rule that allows all ZTNA users to access the datacenter site. This rule improves security because it only allows RDP traffic for ZTNA users.

![mobile_rule_wan.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209928500765.png)

#### Avoiding Any for Source and Destination

WAN firewall rules that give access to ANY **Source** or **Destination** are less secure than specific sites and users. The more specific settings give you increased control for the WAN connectivity for the account.

The following screenshot shows an example of a WAN firewall rule that uses specific sites in the **Source** and **Destination** settings:

![src_and_dest.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29209928582045.png)

#### Improving Event Data with Granular Rules

When you configure WAN Firewall rules using **Any** in some settings, the events related to the rule don't necessarily include all the relevant data, and can make it more difficult to analyze app usage. For more information on events for rules using **Any** settings, see above [Improving Event Data with Granular Rules](/v1/docs/recommendations-for-internet-and-wan-firewall-policies#improving-event-data-with-granular-rules) . To help improve analysis of app usage, we recommend that you minimize the use of **Any** for rule conditions and instead use granular rules with specific apps, services, ports, and so on.

### Allowlisting WAN Traffic

Implementing a WAN firewall with allowlist behavior means that by default, the firewall blocks all WAN connectivity between sites, servers, users, and so on. Add rules to the firewall that specifically allow WAN traffic connectivity in your network. Allowlisting is the default structure for the Cato WAN firewall, the implicit final rule of the WAN rulebase is ANY ANY Block.

We strongly recommend that you don’t add a rule that allows connectivity from any source to any destination in the WAN. This type of ANY ANY Allow rule exposes your network to significant security risks.

#### Limiting Traffic with Services and Applications

A strong security policy for an allowlist WAN firewall includes rules that only allow the specific services and applications that are used by your organization. Instead of using rules that allow ANY service for traffic between sites, add the services or applications to this rule. Since services are more specific than ports, we recommend defining rules using Services instead of ports where possible.

Examples of services often used by organizations include: DNS, DHCP, SMB, Databases, Citrix, RDP, DCE/RPC, SMTP, FTP, ICMP, NetBIOS, NTP, SNMP, and so on.

Examples of applications often used by organizations include: SharePoint, Slack, Citrix ShareFile, and so on.

You can also create a custom category that contains all the applications and services for the WAN firewall, and then add this custom category to the relevant rules. Use the Custom Applications for applications or services that are not predefined in the firewall. This also allows the Events to contain the application name for better analysis.

### Blocklisting WAN Traffic

Implementing a WAN firewall with blocklist behavior means that, by default, the firewall allows all WAN connectivity between sites, servers, users, and so on. Add rules to the firewall that specifically block WAN traffic according to the needs of the corporate security policy. We don’t recommend using this approach for a WAN security policy. However, if your organization does use it, then make sure that you block undesired WAN traffic.

To implement a blocklist WAN firewall in the CMA, the rulebase contains an ANY ANY Allow rule at the bottom.

#### Blocking WAN Traffic for a Blocklist Firewall

For blocklist WAN firewalls, we recommend that you add the following rules above the final ANY ANY Allow rule to help create a strong security policy:

- Rules to block services that are security risks and have known vulnerabilities, such as SMBv1
- Rules that block connectivity between sites that don’t need to communicate
