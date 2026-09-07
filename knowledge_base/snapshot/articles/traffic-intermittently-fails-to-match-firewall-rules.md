---
title: "Traffic Intermittently Fails to Match Firewall Rules"
slug: "traffic-intermittently-fails-to-match-firewall-rules"
updated: 2026-08-13T00:51:43Z
published: 2026-08-13T00:51:43Z
canonical: "knowledge.catonetworks.com/traffic-intermittently-fails-to-match-firewall-rules"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Traffic Intermittently Fails to Match Firewall Rules

## Issue

This article describes the reason why, despite going to the same destination, certain connections are blocked by Cato while others are allowed.

For example, the event discovery below illustrates instances where the same source attempted to connect to the same destination IP on the same protocol. However, while one connection was blocked, the other was allowed.

![eventdiscoverycat.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12014582980381.jpeg)

## Troubleshooting

In this section, we will explore several common scenarios that may cause the connection to be treated differently by Cato. Understanding these scenarios is essential for optimizing and troubleshooting the connection effectively. Let's delve into each of them below.

### 1. Asymmetric Routing

When Cato doesn't have visibility into the complete flow, it might lack sufficient information to accurately categorize the data into the appropriate application. Consequently, even if there is a firewall rule permitting a specific protocol like HTTPS, asymmetric routing could lead to the flow being mistakenly categorized as TCP. Unfortunately, this misclassification can result in the connection being blocked since it doesn't align with the allowed firewall rule. To investigate further, it's recommended to perform a traceroute from both the source to the destination and vice versa when the issue is occurring. By comparing the forward and reverse paths, we can validate if this indeed is the cause of the problem.

### 2. Overlapping Custom Application

When dealing with an affected connection that involves a custom application, it is crucial to conduct a thorough examination of its definition. An overly simplified definition of a custom application could cause Cato to inconsistently identify the application. If there is a Firewall Rule permitting connections to the custom app, but due to how the custom app was defined, its identification becomes inconsistent, resulting in intermittent blocking of the connection. Therefore, when dealing with connections destined for custom applications, we recommend following the best practices outlined in [Working-with-Custom-Applications](/v1/docs/working-with-custom-apps) to ensure consistent behavior.

### 3. User Awareness Delay

When a user initially connects to the Cato network, both [AD-based](/v1/docs/using-ad-query-for-user-awareness) and [Identity-Agent](/v1/docs/using-cato-identity-agents-for-user-awareness)-based user awareness mechanisms require a few seconds to map the source IP address to the corresponding username. During this brief period, initial user traffic may be processed under an unexpected firewall rule. However, once user awareness successfully identifies the username, the appropriate firewall rule will be enforced.

### 4. App Identification Timeout (HTTP/1.1)

Modern browsers open **multiple TCP connections** simultaneously over **HTTP/1.1** to improve page load performance. Some of these connections remain idle briefly after being established — no HTTP request is sent right away, meaning the destination hostname is not yet visible. When Cato processes traffic through a Socket site, it evaluates each connection as it arrives. If the destination hostname is not present at the time of evaluation, the traffic will not match any firewall rule that uses an FQDN or Domain as a match condition, even if such a rule is correctly configured.

This is expected behavior and is specific to HTTP/1.1 traffic processed through a Socket site (Office Mode). It does not occur with the SDP Client, which provides destination context before the traffic is forwarded. Below are the conditions that would lead to this issue:

1. HTTP-only website
2. Browser opens a spare TCP connection (HTTP/1.1 behavior — Chrome opens up to 6 parallel connections)
3. No HTTP GET is sent on that spare connection within 1 second

#### Suggestion Solution

- If you are using Firefox, you can set the `network.http.max-persistent-connections-per-server` to **1** under `about:config`
- Update the firewall rule to use the destination IP address instead of FQDN/Domain.
- Alternatively, if the destination server supports it, HTTP/2 eliminates this behavior as it uses a single multiplexed connection and does not open idle parallel TCP connections.

### 5. FQDN in the Rule

Another common scenario where seemingly similar connections are treated differently by Cato (blocked or allowed) is when Fully Qualified Domain Names (FQDN) are used in the Firewall Rules or in a custom category/app. Before we delve into the details, let's examine two events, both are sourcing from the same source IP address and destined to the same IP address and port, but with different outcomes—one allowed and the other blocked.

![event-review.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12461220381725.jpeg)

#### Review the Firewall Rules

In the given example, the connection is either blocked or allowed based on the WAN Firewall rule.

To investigate further, follow these steps:

- Navigate to the WAN Firewall section within CMA and search for the relevant rules.
- It becomes evident that rule 1 corresponds to the Monitor (Allow) event. This rule specifically permits connections categorized under "Internal Web Servers". Clicking into the rule reveals that the "Internal Web Servers" is from the Custom Category.
- In contrast, rule 5 aligns with the Block event. It is designed to block HTTP(s) traffic alongside other services.![wanFWrule.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12015556095901.jpeg)

#### Review the App/Category

Now that we have determined from the Firewall Rule that the connection was allowed based on a match to the "Internal Web Servers" custom category, let's investigate further to understand the condition for this match.

- Navigate to Resources > Categories > Custom Categories
- In the list of custom categories, locate and select the "Internal Web Servers" category.
- Within the category details, it is observed that the member of the "Internal Web Servers" category matches the Fully Qualified Domain Name (FQDN) to webserver.dyow-homelab.com.
- This indicates that connection matching to the FQDN will be allowed. (In order for Cato to correctly identify the hostname, we need to see the DNS query/response) ![customercat.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12016455008413.jpeg)
- Any connection that does not correspond to the exact FQDN will be denied. For example, if the visited website includes "www", that is www.webserver.dyow-homelab.com (as per the DNS query), it won't match with the defined FQDN in CMA. To solve this issue, a Domain object can be defined instead. This will allow matches to all subdomains that include the defined Domain. See [Cato WAN Firewall](/v1/docs/what-is-the-cato-wan-firewall). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16558701039773.png)
- In the above-blocked connection example, the user attempted to access the server using its destination IP address instead of the FQDN. In this case, since there isn't any DNS query/response, Cato wasn't able to identify the hostname, and the rule wasn't matched.
- In situations where direct IP access occurs without a preceding DNS request, Cato utilizes its DNS cache to attempt to match a domain to the given IP. If the cache does not contain any domains, Cato will be **unable** to associate it with a hostname or FQDN. As a result, the connection in the aforementioned example will be blocked.
- Therefore, when an allow firewall rule is configured to match based on the FQDN, the customer must access the server using its domain name to ensure uninterrupted connectivity.

> [!NOTE]
> NOTE:
> 
> If you are using an internal DNS server, make sure that all its DNS queries are routed through the Cato Cloud, regardless of the destination DNS server configured. For DNS best practices, refer to [Best-Practices-for-DNS-and-Your-Cato-Account](/v1/docs/best-practices-for-dns-and-your-cato-account)

## Alternative Solutions

In case of firewall rule mismatches continue to occur, even after accessing the site using its domain name and DNS queries/responses are indeed going through Cato, the following solutions can be implemented:

- The DNS cache on the user's PC may be different than the DNS cache on the PoP which will lead to Cato not associating the server IP with the FQDN. In cases where an internal DNS server is used, the DNS TTL (time-to-live) can be shortened and therefore force the PC to generate DNS queries more frequently.
- Use an IP/port combination in the custom app/category used in the firewall rule that matches the server. In the example above, set the custom app to IP address 192.168.2.25 and port 8080. This will force rule matching even if there are DNS cache mismatches or missing DNS queries over the Cato Cloud.
