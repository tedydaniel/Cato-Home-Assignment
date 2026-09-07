---
title: "Network Rule Evaluation Troubleshooting"
slug: "network-rule-evaluation-troubleshooting"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/network-rule-evaluation-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Rule Evaluation Troubleshooting

## Overview

Ensuring accurate network rule evaluation is crucial for making informed routing decisions. This troubleshooting guide aims to comprehensively address various common symptoms, explore potential causes, and offer systematic steps to resolve issues related to network rule evaluation.

## Symptoms

A failure to evaluate traffic against network rules can manifest in several ways. An administrator may note the following symptoms:

- Incorrect Public Source IP
- Network Rule Mismatch
- Incorrect WAN Interface Selected
- TCP Acceleration Is Being Enforced or Skipped
- QoS Priority Mismatch
- Off-Cloud or Alt-WAN Break Traffic Connections

## Possible Causes

- Custom or Built-in Application mismatch
- Mismatching domain
- Incorrect chosen Egress PoP
- Unhealthy WAN connections
- Blocked or unidentified app leads to fixed QoS priority
- Incorrect Network Rule Ordering

## Initial Assessment

> [!NOTE]
> Note:
> 
> Make sure you have a Firewall Rule (even temporarily created for troubleshooting purposes) with **event tracking enabled** that will include the traffic expected to match the configured Network Rule.

Review Firewall Events by selecting the **Internet Firewall** or **WAN Firewall** presets in CMA. Set filters to narrow down the interesting traffic. Analyze relevant fields such as **Related Apps**, **Application**, **Cato App**, **Egress PoP Name, Public Source IP, Destination IP**, **Domain Name**, **Network Rule, and TCP Acceleration** that will help you identify the possible root cause of the issue.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18216056658973.png)![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18216076632733.png)

Make sure to review the appropriate troubleshooting section by identifying the symptoms reported by the users:

- Web applications may report a public source IP address different from the one configured in the network rule. If the **Egress PoP Name**, and **Public Source IP** fields in the Firewall Event are not the expected ones, see [Troubleshooting Incorrect Public Source IP](/v1/docs/network-rule-evaluation-troubleshooting#troubleshooting-incorrect-public-source-ip)
- Check if the **Network Rule** field in the firewall event is the expected one. If not, continue with [Troubleshooting Network Rule Mismatch](/v1/docs/network-rule-evaluation-troubleshooting#troubleshooting-network-rule-mismatch)
- If traffic flows do not use the configured primary WAN link or they are not balanced as configured in the Network Rule's primary transport section, see [Troubleshooting Incorrect WAN Interface Selected](/v1/docs/network-rule-evaluation-troubleshooting#troubleshooting-incorrect-wan-interface-selected)
- If the **TCP acceleration** field from the firewall event is not the expected configured value in the network rule, see [Troubleshooting TCP Acceleration Being Enforced or Skipped](/v1/docs/network-rule-evaluation-troubleshooting#troubleshooting-tcp-acceleration-being-enforced-or-skipped)
- If traffic is assigned the wrong **QoS Priority** of 255 as per the firewall event, see [Troubleshooting QoS Priority Mismatch](/v1/docs/network-rule-evaluation-troubleshooting#troubleshooting-qos-priority-mismatch)
- If **TLS connections** are failing when off-cloud or Alternative WAN is selected as the transport in the network rule, see [Troubleshooting Off-Cloud or Alt-WAN Breaking Traffic Connections](/v1/docs/network-rule-evaluation-troubleshooting#troubleshooting-offcloud-or-altwan-breaking-traffic-connections)

## Troubleshooting the Issue

### Troubleshooting Incorrect Public Source IP

There are cases where it's necessary to define a specific source public IP to access restricted internet service as explained in [How to Configure an Egress Rule](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic). If the service reports an unexpected source public IP, follow the steps below.

#### Reviewing Multiple Egress IPs

For network rules with multiple egress IP addresses, the Cato Cloud uses the egress IP address for the PoP that is geographically closest to the source. If the first egress IP address is unavailable, the Cato Cloud automatically moves to the second egress IP address. The following screenshot shows an example of a network rule with two egress IP addresses.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17001204168733.png)

In this example, a network rule can egress the traffic from the New York PoP or the Chicago PoP. If the source is physically closer to the New York PoP, Cato will try to egress the specific traffic from the PoP in New York. If the destination isn’t reachable from the New York PoP, then Cato egresses the traffic from the Chicago PoP.

To change this behavior see [Egress PoP Selection Change](/v1/docs/network-rule-evaluation-troubleshooting#egress-pop-selection-change).

#### Unavailable Egress IPs

It may be possible that a network rule containing a single egress IP will egress traffic using a Cato public IP different than what is configured. This may be possible when the PoP associated with the egress IP is temporarily unavailable during a maintenance window. This situation may be critical, especially for VoIP applications.

To change this behavior see [Egress PoP Selection Change](/v1/docs/network-rule-evaluation-troubleshooting#egress-pop-selection-change).

#### Checking Network Rule Changes

If the network rule was recently edited with an egress IP address. Keep in mind that only newly generated traffic flows will use the new egress IP. Existing traffic flows will keep the egress IP associated at the time when the flow was created.

The above behavior is usually common with VoIP traffic where the SIP flow remains active for a long time. To resolve this issue, the VoIP phone can be rebooted which will trigger the creation of a new SIP flow that will be routed as per the updated network rule's egress IP.

### Troubleshooting Network Rule Mismatch

When configuring a network rule, it may be possible that the traffic is evaluated against the wrong network rule. This section covers all the possible mismatching scenarios and how to troubleshoot this issue.

#### Firewall Event Analysis

Identify relevant fields like **Related Apps**, **Application**, **Cato App**, **Destination IP**, **Domain Name**, and **Network Rule** from the Firewall Event. This information will help you troubleshoot the reason for the network rule mismatch.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16968276860189.png)

#### Checking Network Rule Exceptions

Identify any exceptions added to the network rule. If the traffic flow matches the added exception, the network rule will be ignored and the rule lookup will continue with the remaining of the rule base until a match is found.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17201282391197.png)

#### Verifying Custom Application

If the interesting traffic is expected to match a custom application and the **Application** field found in the FW event does not match it, confirm that the custom app is correctly configured. Keep in mind that when overlapping custom apps exist, Cato **only** identifies traffic as **one of the custom apps**.

To prevent this issue, please view the [Resolving Overlapping Custom Application](/v1/docs/network-rule-evaluation-troubleshooting#resolving-overlapping-custom-application) section.

#### Verifying Built-in Application

If the interesting traffic is expected to match a built-in Application and traffic is matching the wrong network rule, check the following:

- What applications are configured in the 'wrong' matching network rule.
- Whether any of these applications are listed in the **Related Apps** field from the FW event.

App identification is a multi-step process that starts with identifying the protocol and then all the possible matchable Applications that are included in the **Related Apps** field. Any 'related app' application identified in a flow regardless of the final app (**Application** field) decision will match a network rule.

In the example below, access to *portal.azure.com* matches Rule #7 instead of Rule #8. This is because Rule #7 includes the *Microsoft Azure* application (included in **Related Apps**) even though the final app (**Application** field) is *Azure Front Door*.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16996731261725.png)![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16996324879133.png)

To resolve this expected behavior see [Network Rule Ordering](/v1/docs/network-rule-evaluation-troubleshooting#network-rule-ordering)

#### Verifying the Domain Name

If a Network Rule contains a Domain or FQDN object, check what the **Domain Name** field is in the FW event. The Domain/FQDN object in the network rule must be the same as this field.

Bear in mind that an **FQDN** is an exact match of the fully qualified domain. For example, the FQDN *example.com* only matches *example.com.*

On the other hand, a **Domain** is a top-level (TLD) or second-level domain (SLD) that matches all subdomains. For example, the Domain *example.com* matches www.*example.com* and *host.example.com*.

There could be cases where Cato cannot determine the correct Domain Name from HTTP, TLS, or DNS flows. To resolve these types of issues see [Resolving Domain Name Issues](/v1/docs/network-rule-evaluation-troubleshooting#resolving-domain-name-issues)

### Troubleshooting Incorrect WAN Interface Selected

This section addresses the scenario where Cato is selected as the transport with both WAN interfaces configured in an Active/Active deployment. For more information about policy-based routing, see [How does Cato Select the Best Transport or Link](/v1/docs/part-2-pbr-and-network-rules-within-the-socket)

> [!NOTE]
> Note:
> 
> The **ISP Name** and **Source ISP IP** fields in the FW rule may not be a good indication to determine which WAN link is used by the traffic. This is because the traffic flow can change tunnels multiple times during its lifetime.

#### Reviewing Network Rule Transport Configuration

If Active/Active deployment is to be achieved, the primary interface role must be set to **Automatic** or both primary and secondary interface roles must be configured as shown in the screenshot below. Setting the secondary interface role as **None** will lead to no traffic failover when the primary interface becomes unavailable. See [Routing Traffic over the Socket Interfaces](/v1/docs/part-2-pbr-and-network-rules-within-the-socket)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17220226170781.png)

#### Reviewing Network Analytics

The **Avg Throughput** widget will show the average BW utilization for each WAN link. This may serve as an indicator to confirm that the Network Rule is selecting the right WAN connection or balancing traffic properly. In the screenshot below, the Network Rule was modified to select WAN2 as the primary transport.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17009865461789.png)

It's important to monitor the WAN link performance, in particular for packet loss, jitter, and distance. As explained in [Active/Active Traffic Distribution](/v1/docs/active-active-traffic-distribution), if one link does not meet the minimal link quality thresholds, it will be considered unhealthy and won't be selected for traffic distribution, even if the WAN link is selected as the primary transport.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17009865472925.png)

#### Reviewing the Socket WebUI

One easy way to find whether the Socket is considering a link unhealthy is the Monitoring page in the Socket WebUI. If latency, jitter, or packet loss metrics do not meet the minimum requirements, the unhealthy value will be marked in red.

In the example below, WAN1 has fairly high latency which leads to the Socket considering the link unhealthy. This issue must be raised with your ISP.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17009881093917.png)

#### Checking the WAN Link Configuration

If all active/active links are healthy, check the bandwidth configuration for each WAN link in CMA. In the example below, the WAN1 link is configured with a bandwidth of 100 Mbps down/up, and the WAN2 link is configured with 20 Mbps down/up. This will result in sending more traffic to WAN1 in a 100:20 or 5:1 ratio for both upstream and downstream directions.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17009865495965.png)

### Troubleshooting TCP Acceleration Being Enforced or Skipped

As discussed in [Explaining the Cato TCP Acceleration](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices), TCP Acceleration can be enabled in a Network Rule to accelerate TCP connections over the WAN. This feature is usually enforced in certain scenarios and the admin may not be able to disable it even if the **Active TCP Acceleration** option in the rule is unchecked. This section addresses those scenarios and how to disable the feature when it's needed.

#### When TCP Acceleration is Enforced

TCP Acceleration will be enforced when the network rule uses an egress IP or an egress location. This forces the PoP to act as a proxy which in turn enforces TCP acceleration to all traffic flows matching the rule. The checkbox in the network rule will be greyed out.

Disabling TCP Acceleration in a network rule will not disable the feature when:

- TLS inspection is enabled for the account, which will activate TCP acceleration to all TLS traffic even if it's TLS bypassed. This is because the PoP needs to act as a proxy to inspect the traffic for malicious files and threats.
- A complex network rule exists above the matching network rule with TCP Acceleration disabled
- The network rule that has TCP Acceleration disabled is itself complex.

A complex network rule (also known as NG rule) is a network rule that the Socket itself cannot evaluate. Therefore, the Socket needs to send the traffic to the PoP to choose the correct network rule which in turn enables TCP acceleration. It may contain: Applications, Applications Categories, Services, Custom Applications, or Domain/FQDN objects.

On the other hand, a simple rule may contain the following entities which can be evaluated by the Socket and do not need involvement from the PoP:

- In the **Source/Destination** field: Sites, IP addresses, Network interfaces, IP Range, or Any.
- In the **App/Category** field: Port Range or a Custom Service.

#### When TCP Acceleration is Skipped

TCP Acceleration will be applied only to TCP traffic. In case TCP Acceleration is enabled in the network rule or enforced as explained in the previous section, but the **TCP Acceleration** field in the CMA event is **0**, it is possible that asymmetric routing over the Cato Cloud is causing the traffic flow to be detected as **Open Mode.**

As explained in [Asymmetric Routing over Cato](/v1/docs/asymmetric-routing-over-cato-and-mpls), **Open Mode** is a connection mode in which the Cato Cloud is not aware of the beginning of the TCP flow (3-way handshake), preventing TCP Acceleration from being applied. We recommend working with Cato Support to determine the root cause for the creation of Open Mode flows.

#### Disabling TCP Acceleration

To disable TCP Acceleration, a simple rule with no Egress IP or location can be placed on top of the network rule base as described in [Network Rule Ordering](/v1/docs/network-rule-evaluation-troubleshooting#network-rule-ordering). As mentioned above, if the traffic is TLS, TLS inspection must be disabled for the whole account.

### Troubleshooting QoS Priority Mismatch

As explained in [When is a Flow Assigned QoS Priority 255](/v1/docs/when-is-a-flow-assigned-qos-priority-255), there could be cases, where the QoS priority configured in the network rule, is different than the priority shown in the FW event.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17201082768797.png)

QoS priority 255 is referred to as the default priority for BW Management. There are several reasons why a flow can be assigned QoS priority 255 regardless of the Network Rule's bw priority configuration:

- Cato evaluates the network profile for each flow, and the QoS priority of 255 is assigned when the specific application hasn't yet been identified.
- The first packets (before the flow is identified) are assigned QoS priority 255.
- Blocked flows are assigned QoS priority 255.

### Troubleshooting Off-Cloud or Alt-WAN Breaking Traffic Connections

This section addresses the scenario where TLS connections fail to get established between sites when the WAN Network Rule is configured with Off-Cloud or Alt-WAN as the primary transport. To troubleshoot this issue follow the steps below.

#### Flow Analysis

When traffic is correctly routed via Off-cloud or Alt-WAN, traffic flows will not generate FW events in CMA because this traffic does not go through the PoP.

One way to confirm that the traffic is successfully being routed via Off-Cloud or Alt-WAN is from the SDWAN tab in the [Socket WebUI](/v1/docs/accessing-the-socket-webui). Identify the active traffic flow and under **Chosen NIC** you will see the selected transport for the interesting traffic. If the expected transport is not selected, confirm that [Off-Cloud](/v1/docs/routing-traffic-to-an-off-cloud-link) or [Alt-WAN](/v1/docs/integrating-cato-with-an-alt-wan-network) are configured correctly.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17140100662173.png)

#### Verifying Network Rule Ordering

As explained in [TLS Connection Failure Over Off-Cloud or Alt-WAN Links](/v1/docs/tls-connection-failure-over-off-cloud-or-alt-wan-links), when traffic is TLS and TLS inspection is enabled, network rule ordering is an important factor in ensuring traffic flow over Off-Cloud or Alt-WAN links.

Sockets can not evaluate network rules and route packets over Off Cloud or Alt-WAN when the network rule that the traffic hits is below a complex rule. To resolve this expected behavior see [Network Rule Ordering](/v1/docs/network-rule-evaluation-troubleshooting#network-rule-ordering)

## Resolving Discovered Issues

### Resolving Overlapping Custom Application

Make sure that the custom application includes the correct IP addresses, Domain, Port, and Protocol. There is no logic to what custom app is chosen for identification, so the custom app must be uniquely defined to avoid overlapping with another custom app. For more information, see [Working with Custom Applications](/v1/docs/working-with-custom-apps)

### Network Rule Ordering

Keep in mind that Network Rules are evaluated according to their order, so it's important to define more specific rules above more general rules. For example, Network Rules that define a custom application, built-in application, domain, FQDN, or custom service should be placed above Network Rules containing categories, custom categories, or services.

In the screenshot below, Rule #1 contains a custom service that includes IP ranges for twitter.com and is placed above Rule #2 which contains Application Categories. Rule #1 is more specific than Rule #2 and will be a better match for traffic destined to *twitter.com.* This will additionally disable TCP acceleration and solve any Off-Cloud or Alt-WAN routing issues given that Rule #1 is a simple rule.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16997600002845.png)

### Resolving Domain Name Issues

Network Rule matching issues based on Domain/FQDN can be resolved as follows:

- For protocols like HTTP/S, Cato can determine the destination domain using the following sources:
  - **HTTP Hostname header** (when TLS inspection is enabled)
  - **SNI** field during the TLS handshake
  - **DNS resolution**, where the domain name is learned from DNS queries and responses
- It is important to ensure that the domain specified in the Network Rule is consistent across all of these sources. Note that only the best-matched domain name (evaluated from top to bottom) is displayed as **Domain Name** in Firewall events.
- For other protocols, such as SSH or SMB, that don't send a domain in plain text, Cato relies exclusively on **DNS interception** to associate traffic with a domain or FQDN. This is particularly critical when using a private DNS, as we need to ensure that DNS queries/responses go through Cato. See [Best Practices for DNS and Your Cato Account](/v1/docs/best-practices-for-dns-and-your-cato-account)

### Egress PoP Selection Change

If you want to route all egress rules for the account via the PoP that is closest to the destination, instead of closest to the source (default behavior), please contact Cato Networks Support by [Raising a case to Cato Support](/v1/docs/network-rule-evaluation-troubleshooting#raising-a-case-to-cato-support).

For VoIP applications using the SIP protocol that require always using the same Egress IP, enable the [Preferred IP for SIP Traffic](/v1/docs/working-with-advanced-configuration-for-the-account) option in advance settings.

If a different VoIP protocol or any other Application requires always using the same Egress IP, please contact Cato Networks Support by [Raising a case to Cato Support](/v1/docs/network-rule-evaluation-troubleshooting#raising-a-case-to-cato-support).

## Raising a case to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the experienced issue and overall impact on users.
- Related Firewall events and Network Rule configuration.
- Reproduce the issue and run the [Support Self Service](/v1/docs/support-self-service-supportme-portal). Include the ticket number generated by the Tool.
