---
title: "Cato Event to Splunk CIM Field Mapping"
slug: "cato-event-to-splunk-cim-field-mapping"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/cato-event-to-splunk-cim-field-mapping"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Event to Splunk CIM Field Mapping

## Overview

This article lists example mappings between Cato fields and Splunk Common Information Model (CIM) fields for the supported data models. Use this reference to understand how Cato data is normalized for Splunk searches, dashboards, and detections.

For more information, see [Configuring the Cato Technology Add-on for Splunk Integration](/v1/docs/configuring-the-cato-technology-add-on-for-splunk-integration)

## Network Traffic

| Cato Field | CIM Field | Source | Splunk CIM Description |
| --- | --- | --- | --- |
| action | action | Events / Flows | The action taken by the network device |
| application_name | app | Events / Flows | The application protocol of the traffic |
| dest_ip | dest | Events / Flows | The IP address of the destination |
| dest_port | dest_port | Events / Flows | The destination port of the network traffic |
| direction | direction | Events / Flows | The direction of the network traffic, such as inbound or outbound |
| downstream | bytes_in | Flows | The number of bytes received (inbound) |
| duration | duration | Flows | The amount of time in seconds for the completion of the network event |
| ip_protocol | transport | Flows | The OSI layer 4 (Transport) protocol, such as TCP or UDP |
| Ipv4 | protocol | Events / Flows | The OSI layer 3 (Network) protocol, such as IPv4 or IPv6 |
| pop_name | dvc | Events / Flows | The device that reported the traffic event |
| src_ip | src | Events / Flows | The IP address of the device that originated the network event |
| src_port | src_port | Events / Flows | The source port of the network traffic |
| traffic_direction | direction | Flows | The direction of the network traffic, such as inbound or outbound |
| upstream | bytes_out | Flows | The number of bytes sent (outbound) |
| user_name | user | Events / Flows | The user that requested the traffic flow |
| Static: “Cato Networks” | vendor | Events / Flows | The vendor of the product generating the network event |
| Static: “Cato SASE” | vendor_product | Events / Flows | The product name of the vendor’s network device |
| downstream + upstream | bytes | Flows | The total number of bytes transferred (in and out) |

## Intrusion Detection

| Cato Field | CIM Field | Source | Splunk CIM Description |
| --- | --- | --- | --- |
| action | action | Events | The action taken by the intrusion prevention system |
| application_name | app | Events | The application protocol of the traffic |
| dest_country | dest_country | Events | The country associated with the destination IP address |
| dest_ip | dest | Events | The IP address of the destination |
| dest_port | dest_port | Events | The destination port of the network traffic |
| dest_site_name | dest_zone | Events | The name of the destination zone |
| pop_name | dvc | Events | The device that detected the intrusion event |
| src_country | src_country | Events | The country associated with the source IP address |
| src_ip | src | Events | The IP address of the device that originated the intrusion event |
| src_port | src_port | Events | The source port of the network traffic |
| src_site_name | src_zone | Events | The name of the source zone |
| threat_name | signature | Events | The name of the intrusion detected on the client (the src), such as PlugAndPlay_BO and the traffic was denied |
| threat_type | category | Events | The category of the intrusion detected on the client (the src), such as extrusion policy violation |
| url | url | Events | The URL associated with the intrusion event |
| user_name | user | Events | The user involved with the intrusion detection event |
| signature_id | signature_id | Events | The ID or version of the signature |
| Conditional: “network” for all events mapped here | ids_type | Events | The type of IDS that generated the event, such as network-based or host-based |
| Ipv4 | protocol | Events | The OSI layer 3 (Network) protocol |
| Static: “Cato Networks” | vendor | Events | The vendor of the product generating the intrusion detection event |
| Static: “Cato SASE” | vendor_product | Events | The product name of the vendor’s intrusion detection software |

## Network Resolution (DNS)

| Cato Field | CIM Field | Source | Splunk CIM Description |
| --- | --- | --- | --- |
| action | action | Events | The action taken by the DNS server or security device |
| application_name | app | Events | The application that initiated the DNS query |
| dest_ip | dest | Events | The IP address of the DNS server |
| dns_query | query | Events | The domain name that was queried |
| dns_record_type | record_type | Events | The DNS resource record type, such as A, AAAA, CNAME, PTR |
| pop_name | dvc | Events | The device that processed the DNS query |
| src_ip | src | Events | The IP address of the device that originated the DNS query |
| user_name | user | Events | The user that initiated the DNS query |
| Ipv4 | protocol | Events | The OSI layer 3 (Network) protocol |
| Static: “Cato Networks” | vendor | Events | The vendor of the product generating the DNS event |
| Static: “Cato SASE” | vendor_product | Events | The product name of the vendor’s DNS security software |

## Web

| Cato Field | CIM Field | Source | Splunk CIM Description |
| --- | --- | --- | --- |
| action | action | Events | The action taken by the web proxy or security device |
| application_name | app | Events | The application that generated the web traffic |
| categories | category | Events | The category of the web request, such as search engines, news, or shopping |
| dest_ip | dest | Events | The IP address of the web server |
| dest_port | dest_port | Events | The destination port of the network traffic |
| http_request_method | http_method | Events | The HTTP method used in the web request |
| http_response_code | status | Events | The HTTP response status code |
| ip_protocol | transport | Events | The OSI layer 4 (Transport) protocol |
| pop_name | dvc | Events | The device that processed the web request |
| referer_url | http_referrer | Events | The HTTP referrer used in the web request |
| request_size | bytes_in | Events | The number of bytes received by the web server |
| response_size | bytes_out | Events | The number of bytes sent by the web server |
| src_ip | src | Events | The IP address of the client that accessed the web server |
| src_port | src_port | Events | The source port of the network traffic |
| transaction_size | bytes | Events | The total number of bytes transferred |
| url | url | Events | The URL of the web request |
| user_agent | http_user_agent | Events | The user agent string of the client |
| user_name | user | Events | The user that accessed the web server |
| Ipv4 | protocol | Events | The OSI layer 3 (Network) protocol |
| N/A | cookie | Events | The cookie file recorded in the event |
| Static: “Cato Networks” | vendor | Events | The vendor of the product generating the web event |
| Static: “Cato SASE” | vendor_product | Events | The product name of the vendor’s web security software |

## Authentication

| Cato Field | CIM Field | Source | Splunk CIM Description |
| --- | --- | --- | --- |
| action | action | Events | The action taken by the authentication system |
| application_name | app | Events | The application that was accessed |
| auth_method | authentication_method | Events | The authentication method used, such as LDAP, RADIUS, or local |
| dest_ip | dest | Events | The IP address of the authentication server |
| failure_reason | reason_id | Events | The reason for the authentication failure |
| pop_name | dvc | Events | The device that processed the authentication request |
| src_ip | src | Events | The IP address of the device that initiated the authentication attempt |
| user_agent | user_agent | Events | The user agent string of the client |
| user_name | src_user | Events | The user that initiated the authentication attempt |
| user_name | user | Events | The user that attempted to authenticate |
| Static: “Cato Networks” | vendor | Events | The vendor of the product generating the authentication event |
| Static: “Cato SASE” | vendor_product | Events | The product name of the vendor’s authentication system |

## Malware

| Cato Field | CIM Field | Source | Splunk CIM Description |
| --- | --- | --- | --- |
| action | action | Events | The action taken by the malware detection system |
| application_name | app | Events | The application involved in the malware event |
| dest_ip | dest | Events | The IP address of the destination |
| file_hash | file_hash | Events | The hash of the file involved in the malware event |
| file_name | file_name | Events | The name of the file involved in the malware event |
| file_size | file_size | Events | The size of the file involved in the malware event |
| full_path_url | file_path | Events | The path of the file involved in the malware event |
| pop_name | dvc | Events | The device that detected the malware |
| src_ip | src | Events | The IP address of the device where the malware was detected |
| threat_name | signature | Events | The name of the malware infection detected on the client (the src) |
| threat_type | category | Events | The category of the malware detected on the client (the src) |
| user_name | user | Events | The user involved with the malware event |
| Static: “Cato Networks” | vendor | Events | The vendor of the product generating the malware event |
| Static: “Cato SASE” | vendor_product | Events | The product name of the vendor’s malware detection software |

## Change (Account Management)

| Cato Field | CIM Field | Source | Splunk CIM Description |
| --- | --- | --- | --- |
| action | action | Events | The action performed on the resource |
| admin_email | src_user_email | Events | The email address of the user that initiated the change |
| event_sub_type | command | Events | The command that initiated the change |
| pop_name | dvc | Events | The device where the change was observed |
| user_id | object_id | Events | The ID of the object that was changed |
| user_name | object | Events | The object that was changed |
| user_name | src_user | Events | The user that initiated the change |
| user_name | user | Events | The user that performed the change |
| Conditional: “user” or “admin” | object_category | Events | The category of the object that was changed |
| Static: “AAA” | change_type | Events | The type of change, such as filesystem or AAA (authentication, authorization, and accounting). |
| Static: “Cato Management Application” | dest | Events | The destination of the change |
| Static: “Cato Networks” | vendor | Events | The vendor of the product generating the change event |
| Static: “Cato SASE” | vendor_product | Events | The product name of the vendor’s change management system |
| Static: “success” | status | Events | The status of the change |
