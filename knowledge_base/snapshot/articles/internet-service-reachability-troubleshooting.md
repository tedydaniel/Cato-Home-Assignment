---
title: "Internet Service Reachability Troubleshooting"
slug: "internet-service-reachability-troubleshooting"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/internet-service-reachability-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Internet Service Reachability Troubleshooting

## Overview

Accessing cloud-based applications over the internet is a large part of business traffic that a site or user facilitates. If critical services reached over the internet are unreachable, this can have material impact on business performance. This playbook aims to assist in scenarios like this.

## Symptoms

- Website doesn't load
  - This could manifest in a few ways, typically though the browser requests will time out when attempting to access a site.
- Firewall rule mismatch
- Certificate error
  - A certificate error appears when attempting to browse to a site or application over HTTPS
- Block page
  - When trying to access a site or application, a splash page identifying that the traffic is blocked appears.

## Possible Causes

- Internet Firewall rule blocked traffic
- Service reachability, including geo-blocked IPs
- Incompatibility with TLS Inspection
- TLS error
- TLSI pre-requisites not met - ie certificate installation
- Mis-categorised URL
- False positive security engine results
- RBI service failing

## Initial Assessment

> [!NOTE]
> Note:
> 
> Make sure you have Internet Firewall Rules (even temporarily created for troubleshooting purposes) configured with **event tracking enabled**.

Review Internet firewall, IPS, and Anti-malware events by selecting the respective preset in CMA. Set filters to narrow down the interesting traffic and check whether the flow was blocked by the firewall or the IPS/AM engines. The **rule** field will show the respective rule that matches the traffic.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17340528352157.png)

Make sure to review the appropriate troubleshooting section by following these initial assessment steps:

- If you can find FW events relevant to the attempts to reach the application, go to [Troubleshooting Website Not Loading Using Events](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-website-not-loading-using-events)
- If no events seem to have been generated for the tested flow, go to [Troubleshooting Website Not Loading - No Events](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-website-not-loading-no-events)
- If IPS or Anti-malware events show that any of these engines are blocking access to the internal server, or replication shows splash pages related to IPS or Anti-Malware, go to [Resolving False Positive IPS/Anti-Malware Block](/v1/docs/internet-service-reachability-troubleshooting#resolving-false-positive-ipsantimalware-block)
- If a splash page related to corporate internet policy is reported or reproduced, visit [Troubleshooting Erroneous Block Page](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-erroneous-block-page)
- If the application reports untrusted certificate, navigate to [Troubleshooting Untrusted Certificate for All Traffic](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-untrusted-certificate-for-all-traffic)
- If TLS errors are reported on splash pages when attempting to reach the internet application, see [Troubleshooting Certificate Errors](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-certificate-errors)
- For website rendering issues specifically within China, go to [Troubleshooting Rendering Issues Within China](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-rendering-issues-within-china)

## Troubleshooting the Issue

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

#### Checking Audit Trail Logs

Check [Audit Trail](/v1/docs/using-the-audit-trail) for any **modified** logs that may have impacted access to the internal resources. This includes Internet firewall rules, AM/IPS settings, and TLS inspection.

### Troubleshooting Website Not Loading Using Events

#### Finding Relevant Flows in Events

Using the Home > Events page in CMA, an administrator can quickly get a history of connectivity events for sites within an account. Events can be filtered down into relevant events by selecting the 'Internet firewall' preset, or else by filtering for Event type 'Security' and Sub-type 'Internet firewall'. You can further filter for the name of the site in question with the 'Source site' field.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17168211477789.png)

For a failing application or site that is not loading, try and filter down into the flow in question. To do this you can further add filter fields in the search. For example you might want to filter based on 'Domain' or 'Destination IP'. You may otherwise want to filter based on the 'Source IP' or any flow in which 'Action' was Block.

Once you've identified the events that are relevant for the flow being troubleshot, we can continue to analyse the information seen here.

#### Analysing Event Fields

The event fields will offer a lot of information on individual flows and help an administrator to ensure that the CMA policy and configuration for a given flow is correct, or else identify mismatches or issues in the flow.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17237356410781.png)

Fields that can indicate causes of application unreachability are as follows:

- **Action** If the flow was blocked, this indicates that the flow is being intercepted based on the security policies configured in **Security** > **Internet Firewall.** The rule that blocked this traffic will also be listed as a field in the event. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17169545744157.png)If this firewall rule is not the one that you would expect this traffic to be actioned on, please visit the [Resolving Flow Matching Wrong Rule](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-internet-firewall-rule-mismatch) section. If the action shows 'RBI', view [Troubleshooting RBI flows](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-rbi-flows)
- **PoP Name/ Public Source IP** It may be important to know in what form the traffic is reaching the internet based application. Particularly in regards to the source IP. These fields help an administrator determine what source IP and region the packets are leaving the PoP at, and are impacted by [egress configuration](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic) within the network rule base. ![Monosnap Cato|Liam-lab - Events 🔊 2024-03-01 09-26-37.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17236196262557.png)Ensure that the application does not [blacklist or geo-block Cato IPs](/v1/docs/website-inaccessible-due-to-cato-ip-blacklisting-or-geo-blocking). If the outgoing PoP or source IP does not match your expectations based on your network rules, follow the [rule mismatch troubleshooting flow](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-internet-firewall-rule-mismatch) for the network rule in question.
- **TLS Inspection** The TLS inspection field identifies whether the flow in question was intercepted for [inspection of data via TLSI](/v1/docs/best-practices-for-tls-inspection). A value of 1 suggests the flow was inspected. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17236608440477.png)Some applications do not handle being inspected well, especially those which use security techniques such as certificate pinning. For flows which appear to be impacted due to the interception of TLS inspection, view [Resolving Applications Failing Due to TLSI](/v1/docs/internet-service-reachability-troubleshooting#resolving-applications-failing-due-to-tlsi).
- **TCP Acceleration** TCP acceleration is a method of optimising TCP traffic as it traverses the Cato cloud. The ways in which TCP acceleration function and how it can impact traffic for internet applications are described [here](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices).

### Troubleshooting Website Not Loading - No Events

If there were no events able to be found for a flow, and all relevant rules in Security > Internet Firewall are set to block or monitor, then it is likely that the flow is not reaching the stage at which the flow would be registered. This can be due to a configuration error or an issue with protocol success preceding the flow, such as DNS.

The first step for troubleshooting issues is to confirm that this issue is specific to traffic traversing Cato. This can be done by bypassing Cato by connecting a host directly to the internet connection or utilising [Socket Bypass](/v1/docs/bypassing-the-cato-cloud-site-level-policy) or [Split tunnel](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) for socket sites and SDP users respectively. If the website still does not load when bypassing Cato, this is not a Cato issue and should be taken with either an ISP or the providers of the application. If the issue does not present when Cato is bypassed, continue this troubleshooting flow.

#### Troubleshooting DNS resolution

If a flow is not reaching the stage at which an event can be generated, a likely cause is that the inability to complete DNS is preventing the flow to the internet application to be initiated from the client.

For the host that this application is failing for, test DNS resolution for the hostname of the application in question to determine if DNS is successfully returning a response.

For instances where DNS is failing:

If your DNS servers are external internet based DNS servers consider changing DNS servers as per [Cato best practice for DNS](/v1/docs/best-practices-for-dns-and-your-cato-account).

If DNS servers in use are Cato's recommended servers (10.254.254.1 and 8.8.8.8), ensure that these DNS flows are not blocked using the troubleshooting flow described in [Finding Relevant Flows in Events.](/v1/docs/internet-service-reachability-troubleshooting#finding-relevant-flows-in-events)

If private DNS servers are being used, ensure the DNS requests are reaching those servers and verify that the response matches expectations.

#### Check Bypass configuration for Socket Sites

Flows that are [bypassed](/v1/docs/bypassing-the-cato-cloud-site-level-policy) on sockets sites will not appear in the Events page and will not be subject to Cato's traffic optimisation or security engines. This may lead to reachability issues particularly in cases where specific known IP addresses need to source the traffic towards the internet application.

Ensure that the flow in question is not included in a bypass rule if not necessary:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17194838801437.png)

#### Check Split Tunnel for SDP Clients

Flows that are within scope of a split tunnel policy for SDP clients will not appear in the Events page and will not be subject to Cato's traffic optimisation or security engines. This may lead to reachability issues particularly in cases where specific known IP addresses need to source the traffic towards the internet application.

Ensure that the flow in question is not in scope of a split tunnel policy rule if not necessary:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17194838829341.png)

#### Check confidence level Configuration for SDP Clients

[Remote Internet Security Confidence Levels](/v1/docs/remote-internet-security-with-one-time-authentication) can impact traffic to the internet to SDP users in instances where the authentication to Cato has expired. The failover behaviour for user sessions that have expired tokens can cause traffic to the internet to not be routed to Cato. This may lead to reachability issues particularly in cases where specific known IP addresses need to source the traffic towards the internet application.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17195130645533.png)

For a user that has an expired session, either ensure that the user can access the internet even at low confidence, or else ensure they renew their authentication.

### Troubleshooting Internet Firewall Rule Mismatch

When configuring a firewall rule, it may be possible that the traffic is evaluated against the wrong rule. This section covers all the possible mismatching scenarios and how to troubleshoot this issue.

#### Verifying Custom Application

If the interesting traffic is expected to match a custom application and the **Application** field found in the FW event does not match it, confirm that the custom app is correctly configured. Keep in mind that when overlapping custom apps exist, Cato **only** identifies traffic as **one of the custom apps**.

To prevent this issue, please view the [Resolving Overlapping Custom Application](/v1/docs/network-rule-evaluation-troubleshooting) section.

#### Verifying Built-in Application/Service

If the interesting traffic is expected to match a built-in Application or Service and traffic is matching the wrong firewall rule, check the following:

- What applications or services are configured in the 'wrong' matching firewall rule.
- Whether any of these applications/services are listed in the **Related Apps** field from the FW event.

App/Service identification is a multi-step process that starts with identifying the protocol and then all the possible matchable Applications that are included in the **Related Apps** field. Any 'related app' application identified in a flow regardless of the final app (**Application** field) decision will match a firewall rule.

In the example below, youtube traffic matches Rule #3 instead of Rule #4. This is because Rule #3 includes the *TCP* service (included in **Related Apps**) even though the final app (**Application** field) is *youtube*.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17345364866333.png)![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17345364874013.png)

To resolve this expected behavior, see [Firewall Rule Ordering](/v1/docs/internet-service-reachability-troubleshooting#firewall-rule-ordering). A built-in application mismatch can also be solved by adding the relevant application domain name to the firewall rule, as seen in the CMA event, or reporting the mismatch [to Support](/v1/docs/internet-service-reachability-troubleshooting#raising-cases-to-cato-support).

#### Verifying the Domain Name

If a Firewall Rule contains a Domain or FQDN object, check what the **Domain Name** field is in the FW event. The Domain/FQDN object in the firewall rule must be the same as this field.

Bear in mind that an **FQDN** is an exact match of the fully qualified domain. For example, the FQDN *example.com* only matches *example.com.*

On the other hand, a **Domain** is a top-level (TLD) or second-level domain (SLD) that matches all subdomains. For example, the Domain *example.com* matches www.*example.com* and *host.example.com*.

There could be cases where Cato cannot determine the correct Domain Name from HTTP, TLS, or DNS flows. To resolve these types of issues see [Resolving Domain Name Issues](/v1/docs/internet-service-reachability-troubleshooting#resolving-domain-name-issues)

### Troubleshooting Certificate Errors

Certificate errors are another common symptom when met with internet application reachability problems. TLS related splash pages are common and help administrators to determine the cause of application reachability failure.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17239677462941.png)

If the block page suggests a TLS error as above, the relevant flow can be found in events. The filter sub-type is TLS can be used to zoom into specific events related to TLS errors.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17239661858717.png) Here the block reason can be identified for any flow that was blocked due to TLS error.

If the following error is shown, despite the website's certificate being valid, and the site being accessible outside of Cato, please raise a case with Cato Support.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17345806754461.png)

### Troubleshooting Untrusted Certificate for All Traffic

If all internet bound traffic for particular users or hosts is receiving privacy or trust errors and TLSI is enabled for the traffic in question, it is likely that the certificate required for TLSI to function is not present on the device.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17238981144861.png)

#### Checking if Custom Certificate is in Use

When investigating how to ensure traffic can be successfully intercepted for TLSI without breaking flows, first it needs to be determined if any custom certificate is in use. Looking at the certificate presented via the browser we can identify if either Cato's default certificate, or a custom one is acting as the certificate authority.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17239013022365.png)

In the above screenshot we can see that CA for the injected certificate is not the standard Cato cert. We can check our custom certificates in Cato via Security > Certificate Management to identify if this matches with our configured active certificate:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17238981163677.png)

This helps an administrator to identify which certificate requires distribution to end clients.

#### Check if Relevant certs are installed

Once we have identified which certificate needs to be installed on hosts in order for these flows to function, we can follow [this guide](/v1/docs/how-to-verify-if-cato-or-custom-root-certificate-is-installed) to ensure those certificates are installed on devices.

### Troubleshooting Erroneous Block Page

When presented with a block page, it is important to determine from the block page the type of block that has taken place and how troubleshooting should move forward.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17195977143837.png)

The above splash page indicates that this block was generated by the internet firewall. If the rule which blocked this flow is set to Events tracking, this flow will show in the [events page](/v1/docs/internet-service-reachability-troubleshooting#finding-relevant-flows-in-events) and can be further analysed:

- If this rule was activated erroneously, and you expected this flow to match a different rule, view the [Troubleshooting Internet Firewall Rule Mismatch](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-internet-firewall-rule-mismatch) section.
- If this rule was activated based on the URL Category, and you believe this category to be applied to this URL in error, view the [Resolving URL Miscategorisations](/v1/docs/internet-service-reachability-troubleshooting#resolving-url-miscategorisations) section.
- If the action that matches the relevant event is 'RBI' navigate to [Troubleshooting RBI flows](/v1/docs/internet-service-reachability-troubleshooting#troubleshooting-rbi-flows)

### Troubleshooting RBI flows

If a URL is triggering an RBI rule against expectations, ensure that the URL is being classified correctly, as in [Resolving URL Miscategorisations](/v1/docs/internet-service-reachability-troubleshooting#resolving-url-miscategorisations).

If a user experiences an issue browsing a certain URL, you can generate a test RBI emulation session for the URL with the Admin RBI Utility . Enter the valid HTTP or HTTPS URL and then follow the resulting link to view the site in an RBI session. The utility sends this traffic directly to the RBI service without passing through the Cato Cloud. This can help determine if a user's issue relates to the RBI service itself, or is caused by other issues such as account configuration or Cato infrastructure connectivity. For example, a user connected to Cato can't browse to an Uncategorized website configured for RBI, but the admin is able to reach the site using the utility. This may indicate that the RBI service is functioning properly and the issue is related to connectivity between a PoP and the service.

After running an RBI session from the utility, you can report the results to Support to help them resolve the issue.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17237816976285.png) To troubleshoot with the Admin RBI Utility:

1. From the navigation panel, select Security > RBI.
2. Under Admin RBI Utility, enter a valid HTTP or HTTPS URL. For example: https://maps.google.com
3. Click Generate. A URL is created for the RBI session.
4. Click the link next to the URL. The RBI session opens in your default browser.

### Troubleshooting Rendering Issues Within China

For this specific use case, please view our relevant KB on this topic, [China | Webpage Having Rendering Issues](/v1/docs/china-webpage-having-rendering-issues)

## Resolving Discovered Issues

### Resolving Overlapping Custom Application

Make sure that the custom application includes the correct IP addresses, Domain, Port, and Protocol. There is no logic to what custom app is chosen for identification, so the custom app must be uniquely defined to avoid overlapping with another custom app. For more information, see [Working with Custom Applications](/v1/docs/working-with-custom-apps)

### Firewall Rule Ordering

Keep in mind that Firewall Rules are evaluated according to their order, so it's important to define more specific rules above more general rules. For example, Firewall Rules that define a custom application, built-in application, domain, FQDN, or custom service should be placed above Firewall Rules containing categories, custom categories, or services.

In the screenshot below, Rule #1 contains a custom service that includes IP ranges for twitter.com and is placed above Rule #2 which contains Application Categories. Rule #1 is more specific than Rule #2 and will be a better match for traffic destined to *twitter.com.* This will additionally disable TCP acceleration and solve any Off-Cloud or Alt-WAN routing issues given that Rule #1 is a simple rule.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17195492514973.png)

### Resolving Domain Name Issues

Firewall Rule matching issues based on Domain/FQDN can be resolved as follows:

- For protocols like HTTP/S, Cato can determine the destination domain using the following sources:
  - **HTTP Hostname header** (when TLS inspection is enabled)
  - **SNI** field during the TLS handshake
  - **DNS resolution**, where the domain name is learned from DNS queries and responses
- It is important to ensure that the domain specified in the Firewall Rule is consistent across all of these sources. Note that only the best-matched domain name (evaluated from top to bottom) is displayed as **Domain Name** in Firewall events.
- For other protocols, such as SSH or SMB, that don't send a domain in plain text, Cato relies exclusively on **DNS interception** to associate traffic with a domain or FQDN. This is particularly critical when using a private DNS as we need to ensure that DNS queries/responses go through Cato. See [Best Practices for DNS and Your Cato Account](/v1/docs/best-practices-for-dns-and-your-cato-account).
- DoH (DNS over HTTPS) and DNS over TLS aren't supported for Domain Name/Application matching, hence, they must be blocked in the Firewall rules to force moving DNS queries to UDP/53.

### Resolving Applications Failing Due to TLSI

For TLS inspected flows that are erroneously inspected, ensure that the ordered TLSI rule base is configured correctly, taking into account the application match of the flow and the ordered nature of the rules, as described [here](/v1/docs/configuring-tls-inspection-policy-for-the-account).

If a flow is inspected by intention, and this is causing the internet application to break, consider configuring a bypass rule for the application in question.

### Resolving URL Miscategorisations

To re-categorise domains, please view our documentation on [Identifying the Category for a Domain](/v1/docs/identifying-the-category-for-a-domain).

### Resolving False Positive IPS/Anti-Malware Block

Review IPS/Anti-malware events by selecting the **IPS** and **Anti-malware** presets in CMA. Set filters to narrow down the interesting traffic and check whether the flow was blocked by the IPS or AM engines.

If the interesting traffic is blocked by IPS/AM, you can add allow lists with scope **Internet** to both IPS and Antimalware settings.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17194160630173.png)

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the experienced issue and overall impact on users.
- Related Firewall events and Firewall Rule configuration.
- Reproduce the issue and run the [Support Self Service](/v1/docs/support-self-service-supportme-portal). Include the ticket number generated by the Tool.
