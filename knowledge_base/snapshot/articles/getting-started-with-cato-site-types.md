---
title: "Getting Started with Cato Site Types"
slug: "getting-started-with-cato-site-types"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/getting-started-with-cato-site-types"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with Cato Site Types

## Overview

In the Cato platform, a site represents a branch, data center, or cloud environment that connects to the Cato Cloud. Cato provides several site types to support different connectivity and deployment requirements. Each site type supports different deployment needs, from physical appliances to virtual and cloud native options. This article discusses the four primary Cato site types and explains when each is typically used.

## Understanding Cato Site Types

This section introduces the three primary methods for connecting locations and workloads to the Cato SASE Cloud. Cato sites provide full access to Cato’s security stack, including Next-Generation firewall, Threat prevention, secure web filtering, and continuous traffic inspection, all centrally managed through the cloud for consistent policy enforcement across every site.

### Cato Socket Sites

Cato Sockets, whether deployed as physical appliances or virtual vSockets, are the primary way to connect branches, data centers, and cloud environments to the Cato SASE Cloud. Physical Sockets run on-premise, while vSockets provide the same experience in virtualized or cloud environments.

The physical and virtual Sockets deliver the same core capabilities, including optimized WAN connectivity, built-in security, and seamless integration with the Cato backbone. Sockets deliver full SD-WAN capabilities, combining multiple WAN connections into a resilient, application-aware transport layer. This functionality lets enterprises leverage broadband, MPLS, cellular, and other access links while maintaining secure, optimized connectivity to the Cato Cloud.

![Site_Types__1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35397986279581(1).png)

The Socket acts as the connection point between the Cato Cloud and the LAN, enabling bidirectional traffic flow. The routing options are fully scalable and include both static routes and BGP dynamic routing.

The Sockets apply the Network Rules policy in the CMA to classify and route traffic based on application, source, destination, or other attributes, ensuring consistent enforcement of business intent across all links.

Sockets are fully managed by Cato and automatically updated to the latest software version, ensuring consistent performance and security without customer maintenance.

#### Available Physical Sockets and vSockets

Physical Sockets:

- [X1500](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35397986200605(1).pdf) - Designed for small branches
- [X1600](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398010004765(1).pdf) / [X1600 Cellular](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398010006429(1).pdf) / X1600 Wi-Fi - Designed for medium-sized branches. The Cellular model provides resiliency and out-of-band connectivity
- [X1700](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Socket_X1700_Deployment_Guide%20(3).pdf) - High-performance appliance for large sites and on-premises data centers

Virtual Sockets (vSockets):

- [ESXi](/v1/docs/configuring-an-esxi-vsocket-site) - Virtual appliances for deployment in private virtualized environments
- [Azure](/v1/docs/deploying-azure-vsockets-from-the-marketplace) - Cloud‑native virtual socket optimized for Microsoft Azure environments
- [AWS](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace) - Virtual socket tailored for Amazon Web Services deployments
- [GCP](/v1/docs/deploying-a-gcp-vsocket-from-the-marketplace) - Virtual socket built for Google Cloud Platform environments

### IPsec Sites

IPsec sites allow you to connect existing firewalls, routers, and virtual platforms to the Cato SASE Cloud using standard IKEv1 or IKEv2 IPsec tunnels. This option is useful when deploying a Cato Socket isn’t feasible or when you want to incorporate Cato into an existing network setup. IPsec sites offer secure, encrypted connections to the nearest Cato PoP, enabling locations to access the Cato backbone and its security services.

IPsec sites provide a versatile way to onboard third-party devices or support transitional and SSE-only deployments, but they don’t provide the full optimization and visibility that come with Sockets.

![Site Types 2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398465643293(1).png)

To configure an IPsec site, please see the articles in the [IPsec sites](/v1/docs/ipsec-sites) section.

### Cloud Interconnect Sites

Cloud Interconnect sites provide high-performance, direct connectivity between the Cato SASE Cloud and major public cloud providers. Instead of routing traffic over the public Internet, these connections use dedicated cloud on-ramps to deliver more predictable performance, lower latency, and improved reliability. Cloud Interconnect is ideal for organizations with significant workloads in AWS, Azure, Oracle, or Google Cloud, ensuring those environments benefit from the same optimized backbone and security services as any other Cato-connected site.

| ![image1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35397986401821(1).png) |
| --- |

To configure a Cloud Interconnect site, please see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).
