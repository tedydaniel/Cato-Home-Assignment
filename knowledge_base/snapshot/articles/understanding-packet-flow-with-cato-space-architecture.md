---
title: "Understanding Packet Flow with Cato SPACE Architecture"
slug: "understanding-packet-flow-with-cato-space-architecture"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/understanding-packet-flow-with-cato-space-architecture"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Packet Flow with Cato SPACE Architecture

This article explains the packet flow for the security engines in the PoP based on Cato's Single Pass Cloud Engine architecture (SPACE).

## Overview

Cato's SPACE architecture examines and processes traffic flows with a single service. This service includes multiple networking and security engines that simultaneously analyze and process traffic flows. This architecture avoids the limitations of combining multiple point solutions with service chaining. The single pass for a flow minimizes latency and improves overall network performance. Each PoP can perform these networking and security decisions using all of Cato's SPACE services and engines.

The security and networking engines have full access to the data for the traffic flow and simultaneously evaluate and share data with each other with a shared context. The engines operate in parallel, there is no priority for one engine to evaluate traffic over another. The engines are located in each PoP and can share data without waiting for information from an engine in a different physical location.

For example, a firewall rule blocks macOS devices, however the firewall engine can’t get this data from the first packet and waits for more data. When a different engine identifies the device as macOS, then the firewall blocks the flow according to the rule action.

### Summary of SPACE Network and Security Services

This section lists the network and security services and engines in the PoP that are applied to the different phases of the packet flow.

- Cato policies and engines
  - Firewall - Firewall policy for Internet and WAN firewalls
  - Network - Network Rules policy for routing and QoS priority
  - IPS/SAM - IPS protections and Suspicious Activity Monitoring (SAM)
  - App Control - App identification for the Application Control policy
    - App Control gen2 - Rules for apps based on access: allow or block
    - App Control gen3 - Rules for apps based on granular actions: upload, download, and so on
  - TLSi - TLS Inspection for HTTPS and encrypted traffic
  - DLP - Content inspection for the Data Loss Protection (DLP) policy
  - AM/NGAM - Anti-Malware and Next-Gen Anti-Malware scanning attached files for malware
- Traffic flow data and protocols
  - App identification - Various criteria are used to identify the specific application for security or networking policies
  - OS - Operating system (OS) for the device, for example with Device Posture or the Client Connectivity policy
  - Client Class - Type of client applications that run on the operating system that created this network flow (for example, Chrome)
  - URLF - URL Filtering for Cato categories based on the website URL
  - File_type - For CASB and DLP, file attachment in the upload or download direction

## TCP Packet Flow with SPACE

This is an example of a typical HTTP flow with the following items:

- Timeline - Different phases of the traffic flow
- Available fields - Data that is available for the specific timeline phase
- Cato Engine - SPACE engine that is able to analyze the flow and then take the appropriate action (block or allow)
- Traffic flow data - For each phase, data that is used to evaluate the traffic flow

![SPACE_Flow.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275618710173.png)

You can see a list of the details below, [Details of Sample TCP Flow](/v1/docs/understanding-packet-flow-with-cato-space-architecture#details-of-sample-tcp-flow).

### Sample App Identification from a Traffic Flow

This is an example of a traffic flow for a rule that includes the Slack application, and shows which information is available at each stage.

1. First packet - TCP

```plaintext
Source - 10.10.2.107
Source port - 55477
Dest IP - 3.68.124.168
Dest port - 443
Protocol - TCP
DNS response - 3.68.124.168 - slack.com  (optional response)
```

This is the traffic flow information available based on this sample first packet:

The engine waits for additional information from the TLS handshake before it can complete the identification of the Slack app.
  - 5 tuple - can't identify the traffic is connected to the Slack application
  - DNS response - Based on previous flows, the engines already know that the dname for this destination IP is slack.com
  - ASN - based on the destination IP, the Security engine can identify the ASN
  - App identification includes: tcp
2. tls_handshake

```plaintext
"TLS Header"
"sni_host": "slack.com"
"predefined inspection bypass reason": "none"
"ja3_formatted_str": "771,4865-4866-4867-49195-49199-49196-4920…"
```

This is the traffic flow information available based on this sample tls_handshake:
  - TLS header and server port 443 - matches the TLS protocol
  - SNI is slack.com - matches the Cato Slack app identification

SNI is also sent to the URLF, and matches categories Business Information, Computers and Technology, Social
  - Client Class is JA3 - classifies the client as a browser based on TLS fingerprinting
  - TLS inspection or bypass action - based on the Client Class and the app identification
  - App identification includes: tcp, tls, slack
3. HTTP

```plaintext
"url" : "upload.slack.com:
"host_name" : "slack.com"
"Content-Type" : "application/pdf"
"Content-Disposition" : form-data; name="file"; filename="sample-data.pdf"
"Content-Length" : "52765"
```

In this sample flow, the following information is available based on the HTTP data:
  - App identification includes: tcp, tls, http, slack
  - TLS Inspection decrypts the flow and identifies that the Slack server host_name is slack.com
  - HTTP header - matches the HTTP protocol

This is a common example where HTTP_host matches the SNI, and there's no change for the App identification
  - URL - the upload prefix provides more granularity, and can match the upload action in the Application Control policy
  - Content-Type, Content-Disposition, Content-Length - provides information about the file name, size, and type
  - Application Control policy actions:
    - Enforce a policy that only uses the corporate Slack tenant
    - File control based on the file type

Anti-Malware and NG Anti-Malware only scan files in the download direction.
4. HTTP Body

```plaintext
"HTTP Body payload" : "The File itself"
```

For example, DLP policy enforces no credit card data can be used in Slack messages.
  - The app identification is completed for the Slack application. It is identified as traffic that belongs to the **social** Category.
  - When the file content is ready, these engines analyze the file content:
    - DLP engine scans content based on the Data Control policy
    - Anti-Malware and NG Anti-Malware scan files in the download direction

## Cato Policies and Engines

This section explains the Cato security policy and engines that analyze and act on the traffic flow.

### Firewall and Network Policies

The WAN Firewall, Internet Firewall, and Network Rules policies are often able to evaluate a traffic flow on the first packet. For example, rules that are based on data from the 5-tuple. However, for rules that match specific applications, such as Azure or Slack, then additional data from the traffic flow is required for the engine to evaluate the flow. This means that the phase which the engine evaluates the flow depends on the settings for the specific rule.

For more information about the types of firewall rules, see [Internet and WAN Firewall Policies – Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies).

#### Example of First Packet for Simple Network Rule and Complex Firewall Rule

This example shows how the PoP engines evaluate a traffic flow differently for a simple network rule that uses IP addresses and ports, and a complex firewall rule for Azure apps. The network engine is able to evaluate the flow based on the first packet, but the PoP waits for the additional data for the firewall engine to finalize its analysis.

**Sample Network Rule**

The following network rule is for traffic for the **Source** as an IP range with the port range 8000 - 8010, and the traffic is egressed via the London PoP location.

![Simple_network.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275609657373.png)

The networking engine is able to evaluate the routing decision for the traffic flow based on the 5-tuple.

**Sample WAN Firewall Rule**

The following WAN firewall rule allows traffic that is the same **Source** as the IP range for the network rule above, and for users that are members of the RnD user group. In addition, the rule is for Azure applications for HTTP(S), TLS, FTP, and TFTP services.

![Azure_FW.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275625515677.png)

The firewall engine can't evaluate the traffic on the first packet, because it needs to confirm the user identity, Azure applications, and services for the flow. After the engine finishes the evaluation and the flow meets all the criteria, then the engine allows the flow. The PoP also applies the routing decision based on the first packet.

### URL Filtering and Cato Categories

The URL filtering service works by analyzing the URL of a website and comparing it against a database of known or suspected malicious or inappropriate websites. This service may also analyze the content of the website itself to determine its categories, such as adult content, gambling, social networking, or streaming media.

For more about categories, see [Working with Categories](/v1/docs/working-with-categories).

### TLS Inspection

The TLS Inspection engine is involved during the tls_handshake phase of the packet flow. The decision whether or not to inspect the flow is irreversible and takes place in two stages:

1. Stage 1 - The first payload of the client_hello packet gives an initial indication if the TLS Inspection engine will inspect this traffic flow
2. Stage 2 - The client_hello is fully parsed, and the TLS Inspection policy action is applied (inspect or bypass the flow)

For HTTPS flows, it's possible that there is a decision to block the packet based on stage 1. However, the engine continues to communicate and establish a TLS connection to present the correct firewall or IPS block page to the end user.

### IPS

The IPS engine continues to run during the lifetime of the traffic flow. It inspects specific items that are available at different stages, and acts on content that positively matches an IPS protection. You can think of IPS as acting like a magnifying glass, constantly waiting for updates from traffic and continuously providing information to the engine that was seen on the flow.

The following example shows different information that is available at different stages of the flow:

- The protocol for the flow is HTTP
- Based on the payload, there is TLS
- There is a client_hello that uses TLS 1.3 cipher suite TLS_AES_256_GCM_SHA384

Different IPS protections could match any of the above items and then take action on the traffic flow at that phase.

### DNS Protection

DNS Protection is part of the IPS engine and runs on the DNS flow for the request and response (without any connection to the transport, for example TCP or UDP).

During the DNS request, the domain name is analyzed and evaluated for domain reputation and static feeds. Then during the DNS response, the resolved IP and the content are analyzed for potentially malicious content. The DNS Protection policy is applied to any matching content (block or allow the traffic flow).

### App Control

The App Control engine inspects traffic and applies the actions for the Application Control policy, and it is evaluated on each new HTTP transaction (request and response).

For gen2 apps, TLS and HTTP proxy are required to complete the app identification.

For rules that include security and compliance requirements:

- Based on contextual data from other networking and security engines, the App Control engine can evaluate these requirements during the tls_inspection phase
- It's also possible that the engine can get this information from the SNI, and doesn't require TLS or full App identification (layer 7 DPI) to evaluate the app

### DLP

The DLP engine inspects the content of the traffic flow and is an extension of the App Control engine. When the policy specifies a file type or file size, then the engine needs to inspect the app metadata and payload for these file characteristics:

1. The engine evaluates the file type and checks to see if it matches the supported list of files for content inspection.
2. Then the gen3 app identification is finalized to identify the specific content signatures for the fields that store the content and data that is inspected.
3. The content is inspected and checked to see if it matches the defined content profile.

### Anti-Malware and NG Anti-Malware

The Anti-Malware and SentinelOne NG Anti-Malware engines scan file attachments on inbound traffic (downloading files) for known and unknown malware. The file_type is based on the HTTP response, or the request for FTP traffic.

Only HTTP, HTTPS, and FTP applications and services are scanned.

1. The engine checks to see if the application matches a rule in the Anti-Malware policy.
2. The file is matched against these lists of files:
  1. The **Allowlist** configured in the Cato Management Application - these files are allowed to download.
  2. The blocklist managed by the Cato Security team - these files are blocked.
3. The files are scanned by the Anti-Malware and NG Anti-Malware engines, and the verdict is returned: malicious, suspicious, or benign.
4. The appropriate action for the Anti-Malware policy is applied to the file.

## FAQ for Cato Policies and Engines

**Does URL Filtering apply to WAN traffic?**

No, URL Filtering is only for Internet traffic and is not applied to account traffic over the WAN.

**What is the difference between Geo-Restriction settings for firewall vs IPS policies?**

The **Device** setting in the [WAN and Internet firewalls](/v1/docs/adding-device-conditions-to-firewall-rules) lets you define the source country for the granular rules. However, there is no control over the destination country.

The **Geo Restriction** tab in the [IPS policy](/v1/docs/configuring-the-ips-policy) defines restricted traffic that is either the source or the destination. However, IPS is a global policy for the entire account, and you can't apply the geo-restriction settings for specific sites or objects.

## Details of Sample TCP Flow

1. Timeline - First packet
  1. Available fields - 5-tuple, hostname (dname)
  2. Cato engine - Firewall, Network, IPS/SAM
  3. Traffic flow data - App identification, Client Class, OS
2. Timeline - tls_handshake
  1. Available fields - cipher_suite, hostname (SNI)
  2. Cato engine - IPS/SAM, App Control gen2, TLSi, Firewall, Network
  3. Traffic flow data - App identification, Client Class, URLF
3. Timeline - HTTP_headers
  1. Available fields - headers, URL, hostname (host header)
  2. Cato engine - App Control gen3, IPS/SAM
  3. Traffic flow data - File_type (upload), OS
4. Timeline - HTTP_body
  1. Available fields - HTTP_request, HTTP_body
  2. Cato engine - App Control gen3, DLP, IPS/SAM
  3. Traffic flow data - File_type (upload), App identification
5. Timeline - HTTP_response
  1. Available fields - HTTP_response_headers, HTTP_response_body
  2. Cato engine - AM/NGAM, App Control gen3, DLP, IPS/SAM
  3. Traffic flow data - File_type (download), App identification
