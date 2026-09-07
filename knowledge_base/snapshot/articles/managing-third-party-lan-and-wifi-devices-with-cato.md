---
title: "Managing Third-Party LAN and WiFi Devices with Cato"
slug: "managing-third-party-lan-and-wifi-devices-with-cato"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/managing-third-party-lan-and-wifi-devices-with-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Third-Party LAN and WiFi Devices with Cato

## Overview

Cato's SASE platform provides turnkey integrations with Juniper Mist and Cisco Meraki for unified LAN switching and WiFi management built directly into the Cato Management Application (CMA) with no additional licenses or separate consoles required.

These integrations bring third-party device inventory, telemetry, and digital experience monitoring into the same management and orchestration plane used to run your entire Cato SASE environment. For teams running infrastructure-as-code, Cato extends this further through the Cato API, Terraform provider, and CLI, giving network engineers full programmatic control.

## Turnkey Vendor Integrations

Cato's integrations with Juniper Mist and Cisco Meraki are built into the CMA and activated without middleware, separate licensing, or manual pre-configuration in third-party portals. Once connected, the device LAN and WiFi data flows natively into Cato's management plane.

The following is included out of the box:

- **Device Inventory** - LAN switching and WiFi devices surfaced directly in the CMA
- **Cato Experience Monitoring (DEM)** - end-to-end visibility across wired and wireless segments, included as part of the Cato platform
- **LAN and WiFi Telemetry** - real-time performance and event data from Juniper Mist and Cisco Meraki environments
- **Single pane of glass** - no cross-launching to third-party portals or managing separate dashboards

## Programmatic Orchestration

Beyond the native CMA interface, Cato supports full management and orchestration through open, documented interfaces, letting network teams automate configuration as part of existing workflows.

You can use the Cato API, Terraform provider, and CLI for:

- **BGP peer configuration** - managing BGP peering between Cato Sockets and on-premises LAN switching and routing infrastructure
- **Network routing automation** - adding, updating, and removing network ranges across distributed sites at scale
- **Site provisioning** - onboarding new Socket sites and configuring interfaces programmatically, and quick IPsec deployment
- **Policy management** - automating firewall and access policies as part of change management or CI/CD pipelines

## Related Articles

- [Juniper Mist: Creating the Device Management Integration](/v1/docs/juniper-mist-creating-the-device-management-integration)
- [Juniper Mist: Creating the Experience Monitoring Connector](/v1/docs/juniper-mist-creating-the-experience-monitoring-connector)
- [Cisco Meraki: Creating the Experience Monitoring Connectors](/v1/docs/cisco-meraki-creating-the-experience-monitoring-connector)
- [What is the Cato API](/v1/docs/what-is-the-cato-api)
- [Using Terraform with the Cato Cloud](/v1/docs/using-terraform-with-the-cato-cloud)
- [Generating Custom Analytics Using Cato CLI for API Queries](/v1/docs/generating-custom-analytics-using-cato-cli-for-api-queries)
