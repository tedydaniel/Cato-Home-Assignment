---
title: "Understanding Event Fields"
slug: "understanding-event-fields"
updated: 2026-07-14T13:44:07Z
published: 2026-07-14T13:44:07Z
canonical: "knowledge.catonetworks.com/understanding-event-fields"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Event Fields

## Explaining the Available Fields

These are descriptions of event fields for the Cato Management Application (CMA). Event fields are frequently updated, for the full list of event fields, please refer to the Cato GraphQL API Reference for [EventFieldName](https://api.catonetworks.com/documentation/#definition-EventFieldName).

For customers that use the Cato API for event data, see [Cato API Potentially Breaking Changes and EoL](/v1/docs/cato-api-potentially-breaking-changes-and-eol) for notifications on potentially breaking changes and end-of-life (EoL) announcements for the Cato GraphQL API schema. We recommend that you follow the article to automatically receive email notifications for updates and changes.

| Name | Description |
| --- | --- |
| Action | Action that is relevant to the event type, for example: - BGP - BGP route ignore, see **Event Message** below for more information. - Firewall - the rule action taken for this event, only rules with the **Track** setting enabled to generate **Events**. - Allow - the traffic is allowed and an event isn't generated (default behavior) - Monitor - the traffic is allowed and an event is generated - IPS - for customers using [SAM](/v1/docs/monitoring-suspicious-activity-with-ips-sam), generated events have the Monitor action - Last-Mile Quality sub-type - [Link Health Rules](/v1/docs/working-with-link-health-rules) generate events with the Alert action - QoS - Alert or Clear Alert - TLS Inspection - Alert action is generated for cases such as an unknown certificate or untrusted CA |
| Active Directory name | Active Directory User Awareness name associated with the device behind a socket |
| API Key Name | Name defined for the public API Key in the Cato Management Application |
| Application | Applications that are used in the different policies, for example: Facebook, CNN |
| Authentication type | Authentication method that is connected to this event, for example: MFA or password |
| BGP Cato ASN | The BGP ASN for the Cato BGP peer (local connection) |
| BGP Cato IP | The BGP IP address for the Cato BGP peer (local connection) |
| BGP error code | Error message for the BGP disconnect event |
| BGP peer ASN | The BGP ASN for the BGP peer (remote connection) |
| BGP peer description | For BGP events, description of the BGP neighbor from the Cato Management Application |
| BGP peer IP | The BGP IP address for the BGP peer (remote connection) |
| BGP route CIDR | The CIDR for the BGP route |
| BGP suberror code | Error message that is connected to the BGP disconnect event |
| Category | Default system Cato categories |
| Cato App | App data related to this traffic flow |
| Certificate Expiration Date | Expiration date for Client certificate |
| Client Class | Type of process generating this traffic |
| Client Version | Version number for the Socket or Cato Client |
| Collaborators | For SaaS Security API, email addresses of the users that received the file |
| Configured Host Name | Name configured in the Cato Management Application for a host with a static IP address |
| Congestion Algorithm | The TCP congestion control algorithm for the traffic in the event. Possible values: CUBIC, NewReno, BBR |
| Connector Name | For SaaS Security API, name of the connector |
| Connector Type | For SaaS Security API, SaaS app for the connector |
| Criticality | For XDR events, 0 (no risk/impact) to 10 (very high risk/impact) |
| Custom categories | The Custom Categories for your account (**Resources > Categories**) |
| Destination Country | For Internet traffic, IP address based location of the destination server |
| Destination Country Code | For Internet traffic, the two letter country code where the destination host is located (based on ISO 3166-1 alpha-2) |
| Destination IP | For Internet traffic, IP address of the destination server |
| Destination is Site or SDP User | For WAN traffic, destination type: site or SDP user |
| Destination Port | For Internet traffic, port number for the destination server |
| Destination Site | For WAN traffic, the name of the destination site or SDP user |
| Device Name | Name of the host connected to the event |
| Device Posture Profiles | Profiles that matched this event |
| Directory Host Name | For LDAP events, the host name |
| Directory IP | For LDAP events, IP address of the Domain Controller |
| Directory Sync Result | For LDAP events, result of sync with the Domain Controller |
| Directory Sync Type | LDAP event generated because there was a sync with the Domain Controller |
| Display Name | The name of the user |
| DLP Profiles | DLP profiles related to the event |
| DNS Protection Category | Cato’s DNS Protection type that matched the DNS request |
| DNS Query | Domain queried in the DNS request |
| Domain Name | SSL SNI, HTTP host name, DNS name |
| Duration Ms | Duration in milliseconds between the start and end of a transaction or operation. For example, in DNS or HTTP events, this reflects the time between the request and the corresponding response. For DNS event sub-types |
| Egress PoP Name | Name of the PoP the traffic egresses from, as defined in a Network Rule using a **NAT** or **Route via** configuration The field is shown only when traffic egresses from a PoP other than the one the site is connected to |
| Egress Site | Name of the egress site for backhauling traffic |
| Event Count | Count for events that are repeated multiple times during one minute |
| Event Message | Cato's description of the event For BGP route ignore action: - Too Many Routes - Exceeded the maximum number of allowed BGP routes. Any routes after route number 1024 are ignored. - Route Collision - The BGP route is ignored because it collided with a BGP range that Cato blocks. - Zero Length Route -The default route (0.0.0.0/0) was ignored. |
| Event Type | Type of event: Connectivity, Security, Routing, System, Sockets Management, or Detection and Response |
| File Hash | For anti-malware events, hash of the relevant file |
| File Name | Name of the relevant file **Note:** If the PoP can't capture the actual file name at the time of detection, then it uses the last part of the URL for the file name, such as **download** |
| File Size | Size (in bytes) of the relevant file |
| File Type | File content type (such as Archive or Microsoft Office) For File Control rules, form_data is a generic representation of data submitted through a web form, commonly used in HTTP requests (e.g., multipart form submissions). It doesn't indicate a distinct file type. |
| Flows Cardinality | Number of flows for a given incident |
| Full Path URL | Full path URL for app activity. [Application Control](/v1/docs/managing-the-application-control-policy) must be enabled for this field to appear in Apps Security events. |
| Host IP | IP address of host related to the event |
| Host MAC Address | MAC address of the host for this event |
| HTTP Response Code | HTTP status code returned (ie. for DNS request, DNS-over-HTTPS (DoH) server when DoH is used) For DNS and App Security event sub-types |
| IP Protocol | Network protocol for this event |
| ISP Name | The ISP used for this event When the IP address isn't provided by the ISP, then the event message is **IP Addresses are assigned statically** **Note:** For sites with multiple active WAN interfaces that use different ISPs, the ISP Name value might not be accurate because the interfaces can change over the lifetime of the traffic flow |
| Link Health is Congested | Data that measures the congestion for a specific link |
| Link Health Jitter | Data that measures the jitter for a specific link |
| Link Health Latency | Data that measures the latency for a specific link |
| Link Health Packet Loss | Data that measures the packet loss for a specific link |
| Link Type | Link type for this connection, for example: Cato, or Alt. WAN |
| Login Type | Login action, values are: **Admin Login** or **VPN client** (remote access or site traffic) |
| Matched Data Types | Matched DLP data types related to the event |
| Mitre Attack fields | For relevant IPS events, shows data based on the comprehensive [Mitre Att&ck knowledge base](https://attack.mitre.org/) of cyber adversaries - mitre attack subtechniques - mitre attack tactics - mitre attack techniques |
| NAT Error | Indicates the reason for connectivity issues related to NAT |
| Network Rule | Name of the Network Rule matched by the traffic in this event A value of 0 indicates that the flow experienced packet corruption issues, or was a system flow such as accessing the Socket WebUI |
| Office Mode | Indicates if [office mode](/v1/docs/configuring-office-mode) is enabled for this user |
| OnPrem SID | Unique identifier assigned to a user object in Microsoft's Azure Active Directory (Azure AD), used to distinctly identify and manage the user across various Azure services |
| OS Type | Type of host operating system, or tunnel device |
| OS Version | Version number of host operating system, or tunnel device |
| PoP Name | Name of PoP location that is connected to this event |
| Public Source IP | The public IP address assigned by the PoP that traffic egressed from. For sites that are using [Internet Traffic Backauling](/v1/docs/internet-traffic-backhauling) as the routing method, this field shows the Local IP address of the Native Range for the site. The field is not shown for traffic that doesn't egress from the PoP to the Internet, such as internal DNS requests and FTP traffic. |
| QoS Priority | The QoS priority value defined in the Network Rule matched by the traffic |
| QoS Reported time | For QoS, the time at which this QoS event started. The event is generated when the QoS event finishes. |
| Record Types | Type of query (ie. DNS query: A, AAAA, MX, or PTR) For DNS and App Security event sub-types |
| Registration Code | Registration code used the first time that a ZTNA user authenticates (the code is partially obfuscated) |
| Related Apps | A list of applications identified in the traffic flow for this event, as part of the application identification process. This process analyzes the traffic at different stages of the flow, gathering information on all the protocols, services, and applications to make an accurate final determination of the application. This field provides context for the app identification by showing the apps identified throughout the stages of the process. |
| Request Method | HTTP request method (ie. GET, POST) |
| Request Size | Request packet size in bytes (ie. DNS request packet) For DNS and App Security event sub-types |
| Response Size | Response packet size in bytes (ie. DNS response packet) For DNS and App Security event sub-types |
| Risk Level | IPS event indicating the overall impact of a threat for the host or network: Risk level low – minimal risk for network, such as adware Risk level medium – medium risk for the network, such as network scans Risk level high – significant risk for the network, such as spyware or worms |
| Rule | Name of the Firewall Rule matched by the traffic in this event |
| Rule ID | Unique Cato ID for the security rule related to the event |
| SAM Account Name | Logon name used to on versions of Windows prior to Windows 2000, used within a Windows Active Directory |
| Severity | Severity defined for the security rule |
| Sharing Scope | Sharing Options for the file (such as SharePoint) |
| Signature ID | For IPS and SAM, ID of the IPS signature |
| Socket Interface ID | Unique Cato ID for the Socket interface |
| Socket Interface Name | Name in Cato Management Application for the Socket port (interface) |
| Socket New Version | For Socket upgrade events, the version number for the new version |
| Socket Old Version | For Socket upgrade events, version number for the previous version |
| Socket Reset | For Socket reset events, indicates a hardware or software reset |
| Socket Role | For Socket high availability events, indicates if the Socket is primary or secondary |
| Source Country | For Clients and sites, the physical location for the public IP address that is outside the tunnel (detected via public IP address) |
| Source Country Code | Country Code of the country in which the source host is located (detected via public IP address) |
| Source IP | The IP address that Cato assigns to the host or Client |
| Source ISP IP | The ISP IP address that is outside the tunnel that connects the Cato Cloud |
| Source is Site or SDP User | For WAN traffic, source type: site or SDP user |
| Source | For all traffic, the name of the source site or SDP user |
| Source Port | The internal port number for the Client, site, or host for the network connection |
| Source Site | For all traffic, the name of the source site or SDP user |
| Subnet name | Name of the subnet that is defined in the Cato Management Application |
| Sub-Type | Subtype for an Event Type, such as Internet Firewall, SDP Activity, Apps Security |
| Targets Cardinality | Number of targets (servers) associated with this event |
| TCP Acceleration | Shows if traffic in the event was TCP accelerated. Values are 1 (accelerated) and 0 (not accelerated) The field appears only for TCP-based traffic flows |
| Threat Name | For anti-malware events, malware name For IPS events, explains the reason why the traffic was blocked |
| Threat Reference | Link to the anti-malware threat database for the suspicious file |
| Threat Type | Type of malware event |
| Threat Verdict | Result of the anti-malware scan - Bypass by Size - Can't scan file because it is too big - Bypass by Min Size - Can't scan file because it is too small - Clean - File was scanned and no threat was detected - Encrypted - Can't scan file because it is encrypted - Match - Matched the anti-malware rule - No scan - Can't scan file because there is no content in the file to scan - Not Scanned for Content Match - File not scanned for a match to a Data Protection rule (DLP) - Suspicious - File was scanned, and based on the analysis, it was flagged as suspicious - virus_found - File was scanned, and the verdict is malicious |
| Time | Time stamp for this event (Linux epoch format) |
| TLS Error Description | Explanation of the TLS error in this event, values are: close notify, unexpected message, bad record mac, decompression failure, handshake failure, no certificate, bad certificate, unsupported certificate, certificate revoked, certificate expired, certificate unknown, illegal parameter, decryption failed, record overflow, unknown CA, access denied, decode error, decrypt error, export restriction, protocol version, insufficient security, internal error, user canceled, no renegotiation, unknown PSK identity, unknown For explanations of these errors, see [this document](https://www.openssl.org/docs/manmaster/man3/SSL_alert_type_string.html) |
| TLS Error Type | The type of TLS error for this event, values are: - warning - Generally, the connection can continue normally, however the receiving party could choose to close the connection. - fatal - Generally closes the TLS connection. For example, the network is busy, or a packet drop - unknown - The connection can continue normally. A part of the TLS connection is unknown, such as certificate_uknown |
| TLS Inspection | Shows if traffic in the event was TLS. Values are 1 (inspected) and 0 (not inspected) The field appears only for TLS traffic flows |
| TLS Rule Name | When traffic in the event was TLS inspected, this field shows the name of the rule matched by the traffic (only when the traffic matches a rule other than default rules) |
| TLS Version | TLS protocol version number for this event |
| Traffic Direction | Direction of network traffic for this event, values are inbound or outbound |
| Transaction Size | Total transaction size in bytes, including both the request and response For DNS and App Security event sub-types |
| Tunnel Protocol | Protocol for the tunnel connection |
| Upgrade End Time | Socket upgrade end time (Linux epoch format) |
| Upgrade Initiated By | Indicates if the Socket upgrade occurred during the maintenance window or was initiated by Support (value is Cato Admin) |
| Upgrade Start Time | Socket upgrade start time (Linux epoch format) |
| URL | For Internet traffic, URL for the event |
| User Agent | The user agent used in the sign-in as it appears in the User Agent field in the HTTP header for the traffic. This field is only populated when the pop extracts its value from HTTP requests, which currently occurs in the following cases: - IPS events when TLS inspection occurs - Application Control events - Events related to security stories in XDR These are examples of user agent values: - Chrome/90.0.4430.212 - Safari/537.36 - Mozilla/5.0 (Windows NT 10.0; Win64; x64) |
| User Awareness Method | Method used to get identity with User Awareness (such as Identity Agent) |
| User email | Email address for the user |
| User Name | User that generated the event |
| User Object ID | Unique identifier assigned to a user object within Azure Active Directory, used to distinctly identify and manage user accounts |
| User Principal Name | Login name for a user in a Microsoft Active Directory environment, formatted as an email address (e.g., user@domain.com), and used for sign-in purposes |
| User Reference ID | For Block/Prompt page, reference ID to report the incorrect category |
| User SID | Unique identifier assigned to each user on a Windows device system to manage permissions and access rights |
| Windows Domain Name | For LDAP sync events, the name of the AD domain |
| XFF | XFF HTTP header indicates the original IP address for the connections |

## Event Sub-Types

This is a list of the event sub-types:

- Connectivity
  - API Key
  - Cato Management Application
  - Changed PoP
  - Client Connectivity Policy
  - Connected
  - DHCP Lease
  - Disconnected
  - LAN Monitoring
  - Last-Mile Quality
  - Link-Aggregation
  - Off-Cloud Transport Connect
  - Off-Cloud Transport Disconnect
  - Passive Connect
  - Passive Disconnect
  - Reconnected
  - Recovery via Alt. WAN
  - Registration Code
  - SDP Portal
  - Socket Fail-Over
- Detection and Response
  - XDR Endpoint
  - XDR Network
  - XDR Threat
- Routing
  - BGP Routing
  - BGP Session
  - VPN Never-Off Bypass
- Security
  - Application Sign in
  - Apps Security
  - DNS Protection
  - Endpoint Protection
  - Identity Alert
  - Internet Firewall
  - IPS
  - LAN Firewall
  - MAC Address Authentication
  - Misclassification
  - NG Anti Malware
  - RPF
  - Saas Security API Anti Malware
  - Saas Security API Data Protection
  - SDP Activity
  - Suspicious Activity
  - TLS
  - WAN Firewall
- Sockets Management
  - Socket Password Reset
  - Socket Upgrade
  - Socket WebUI Access
- System
  - DC Connectivity Failure
  - Directory Services
  - Multiple Users Detected
  - QUOTA LIMIT
  - SCIM Provisioning
  - SDP License

## Understanding the Types of Fields

These are the types of each field and how to use them for manual filters.

- Date and Time - Values for dates in this format `&lt;year&gt;-&lt;month&gt;-&lt;day&gt;T&lt;hour&gt;:&lt;minute&gt;:&lt;second&gt;.&lt;millisecond&gt;Z`, for example `2021-01-01T12:10:30.591Z`
- IP - Filter for IP addresses using the CIDR notation: `[ip_address]/[prefix_length]`
- Keyword - Enter text strings, you can only search for Keyword fields with the exact value
- Link - Link to an external reference
- Number - Enter numbers as integers
- Text - Event description, can't include in a filter

## Explaining Fields for MDR Customers

MDR (Managed Detection and Response) customers of Cato Networks can view the events for security incidents in the Events page. The following table explains the event fields for these incidents in the event subtype **MDR**.

| Name | Type | Description |
| --- | --- | --- |
| Client Class | keyword | Type of client applications that run on the operating system that created this network flow (for example, Chrome) |
| Flows Cardinality | number | Number of network flows that were included in this security incident |
| Incident Aggregation | number | A true/false value that indicates if this event is: - A summary that aggregates many events (true) - Raw network flows for a single event (false) |
| Incident ID | keyword | ID that identifies this security incident. You can use this ID to follow up for more information with the MDR team. |
| Targets Cardinality | number | Number of servers that were included in this security incident |

## Explaining Fields for IoT/OT Security Customers

The IoT/OT Security service discovers and monitors devices connected to your network. The following table explains the event fields containing data related to this service.

| Name | Description |
| --- | --- |
| Device Categories | General categories that the device related to the event belongs to |
| Device ID | Unique Cato identifier for the device related to the event |
| Device Manufacturer | Company that manufactured the device related to the event |
| Device Model | Name of the model of the device related to the event |
| Device OS Type | The operating system on the device related to the event |
| Device Type | Specific type of device related to the event. It is possible that the Device Type includes multiple different models |

## Explaining Fields for the Browser Access Portal

For more about the SDP events and fields, see [Browser Access Portal Overview - Securing Remote Access to Applications](/v1/docs/browser-application-portal-overview-securing-remote-access-to-applications).
