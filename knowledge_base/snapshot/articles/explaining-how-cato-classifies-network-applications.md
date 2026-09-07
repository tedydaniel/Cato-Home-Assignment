---
title: "Explaining How Cato Classifies Network Applications"
slug: "explaining-how-cato-classifies-network-applications"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/explaining-how-cato-classifies-network-applications"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Explaining How Cato Classifies Network Applications

This article explains how Cato classifies applications and discusses the resources and the traffic information that is used for analysis of the proprietary DPI engine.

## Overview of Classifying Applications

Application awareness is necessary for network security and traffic monitoring. It provides visibility and application control of the applications that are running on your network. Cato Networks’ deep packet inspection (DPI) engine examines the network traffic in the application-level and provides the application traffic control based on the application layer and not only on port and protocol.

Cato classifies applications into categories that are used in different policies in the Cato Management Application. For example, managing and controlling the traffic in the bandwidth management and the network rules sections. It also allows you to control the security in the firewall rules section. And, it helps to identify the application name in the Events Discovery window for better visibility and monitoring capabilities.

For more about Cato’s application classification using machine-learning technique, see [Cato develops groundbreaking method for automatic application identification](https://www.catonetworks.com/blog/cato-develops-groundbreaking-method-for-automatic-application-identification/).

## Classifying Application Traffic

Cato’s DPI engine classifies applications according to the traffic analysis of Cato’s security team and based on feeds from external sources

The following sections describe

- Inspecting the traffic
- Using SaaS applications vendors feeds

### Inspecting the Traffic

Cato’s DPI engine runs on every PoP in the Cato Cloud and inspects the traffic content. It uses the packets flow metadata and the data payload for classification.

#### Explaining the Flow Metadata Analysis

The DPI engine inspects various types of data contained in the application flow and then classifies it into application and each application assigned to a category. It uses the following correlated items for the flow metadata analysis.

#### Using the Destination IP Address and Network Port

The DPI engine uses the destination IP address and port number to classify traffic. It easily classifies the applications traffic into categories when the traffic uses well-known ports.

#### Domains Pattern Matching

Cato uses pattern matching techniques on the domain names to classify applications. The DPI engine uses a rich variety of wildcards and logical expressions to search for a matching pattern and identify the application. When it finds a pattern that matches the domain name, it then classifies the application into the fitting category. The following examples show a wildcard and a logical expression pattern matching technique:

1. *Wildcard: ***.google.com.*** Traffic with a domain name that matches this wildcard is classified as a Google application.
2. *Logical expression: "**google.com**"* or *"**googleadservices.com**".* Traffic with a domain name that match this expression is classified as a Google AdWords application.

#### Destination IP Address Member of an IP Range

Cato checks if the traffic destination IP address belongs to a specific IP range that is allocated for an application. It then classifies this application traffic into a category. If the destination IP address is part of an ASN, CIDR, subnet or IP-Set, the engine classifies it based on this information. To correctly classify the application, Cato regularly updates the IP addresses and ASN lists.

For example, if the destination IP address belongs to subnets in these Amazon IP ranges: **52.23.61.0/24 OR 54.244.46.0/24**, Cato classifies the traffic as Amazon application.

Another example is if the destination IP address belongs to the autonomous system (AS): **AS == 62041**(Telegram ASN), Cato classifies it as a Telegram application.

#### Analyzing the Traffic Data Payload

The packet payload contains information about the application that helps the DPI engine to classify it. Here are some examples of payload data that Cato uses for application classification:

- For HTTP traffic, Cato uses the data in the User-Agent HTTP header
- For TLS Traffic, Cato uses the TLS attributes

Cato’s NGFW also uses the payload to identify most services such as HTTP, SSH, TLS and more. We identify services and protocols signatures that are based on their RFC’s. For example, Cato uses patterns such as **"ssh-1" OR "SSH-1"** to identify an SSH application.

### Using SaaS Applications Vendors Feeds

Some SaaS vendors publish feeds and web content with their IP address ranges for applications. Cato uses an intelligence system that routinely follows these vendors to update the specific application IP ranges (e.g. Office365, Google Apps, etc.), and the ASN database. These feeds and web content dynamically update the Cato Cloud and help to classify applications. When providers change and update the properties for an application, Cato also changes the definitions to always use the correct data. The following example shows a feeds source for O365 application: [Office365 URLs and IP Address Ranges](https://docs.microsoft.com/en-us/office365/enterprise/urls-and-ip-address-ranges).

## Introducing the Applications Classification Process

This section introduces new applications classification process.

### Adding New Applications

When does Cato Networks add new applications? The following items describes when Cato adds a new application:

1. Per customer request – Cato’s security team can easily add applications based on requests from customers. If you want Cato to add a new application, please contact the Cato Networks Support team.
2. Tracking unclassified traffic – Cato’s Security team regularly tracks for unclassified traffic using a machine-learning clustering model that analyzes the application behavior, which is then marked for further analysis.

## Cato’s Security Team

Cato Networks’ has a dedicated Security team that constantly analyzes network traffic to protect your data. The Security team contains security experts and analysts that monitor traffic to identify unclassified applications and any applications that aren’t classified correctly. The team monitors the traffic 24/7 using intelligence and monitoring systems
