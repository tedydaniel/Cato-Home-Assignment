---
title: "Socket Version 22.0 Release Notes"
slug: "socket-version-22-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-22-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 22.0 Release Notes

## New Features & Updates

Socket version 22.0 includes the following features:

- **Introducing the Layer 7 Socket LAN Firewall:** The new [Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall) policy provides Layer 7 (L7) enforcement and account-level configurations, enabling seamless LAN segmentation. The Socket LAN firewall controls local network traffic without sending the traffic over the last mile to the PoP. This lets you use the Socket to segment the traffic locally while applying application-layer policy controls, without the need for a third-party firewall appliance.
  - **L7 Segmentation**: Implement advanced security rules based on applications, services, and domains. For example:
    - Configure access to on-premise apps dynamically with custom applications as destinations
    - Enforce secure protocols like SMBv3 over vulnerable versions
  - **Account-Level Policy**: Create a single rule that is enforced over multiple sites. This simplifies LAN segmentation at scale with centralized rules using Groups, VLAN IDs, and other flexible criteria
  - Supported for new customers or customers without existing LAN Firewall rules. Migration isn’t currently supported
- **New vSocket for GCP:** For sites hosted in Google Cloud Platform (GCP), you can now deploy a [virtual Socket on a GCP virtual machine](/v1/docs/configuring-a-cato-vsocket-in-gcp-using-terraform) and extend the advantages of Cato's Sockets into your GCP environment.
  - The GCP vSocket supports the n2-standard-4 machine type
  - GCP vSockets are available for deployment with Terraform
  - Previously, vSockets were available only for AWS and Azure environments
- **New Socket Monitoring of CPU Usage:** Use the Cato Management Application to monitor metrics for Socket CPU usage, and identify if the Socket CPU is related to performance issues for a site.
  - Available for all customers in the Site Monitoring > Network Analytics page for a site
  - Customers with a DEM license can also view the Socket CPU metrics as part of the [path analysis](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D4e9537aafe%26e%3Da04538e456&amp;data=05%7C02%7Cjonathan.rabinowitz%40catonetworks.com%7C5cddc5840542447bfb3f08dd4523454c%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638742739996551157%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=gc0vGnuOzcTQDKN4KMSHid4UJZ28inkNETxpcZlj0rk%3D&amp;reserved=0) and more
  - Supported for virtual Sockets from v.22.0, and for physical Sockets from v21.1
- **Important for Azure vSockets - Resuming Automatic Upgrades:** With the release of Socket v22.0, we are resuming automatic upgrades for Azure vSockets. To avoid potential incompatibility issues, we recommend that customers with unsupported VM instances such as Standard_D2s_v4 migrate to supported instances.
  - For more information on changing a vSocket to a different VM instance, see the following articles:
    - [Changing Azure vSockets to a Different VM Size](/v1/docs/changing-azure-vsockets-to-a-different-vm-size)
    - [Migrating Azure vSockets to a 2-NIC Solution](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution)
- Security updates:
  - Supported Open SSL version: 3.3.4
  - Supported OpenSSH version: 9.9

## Known Limitations

Socket version 22.0 has the following known limitations:

| **ID** | **Description** | **Severity** | **Issue Found In** |
| --- | --- | --- | --- |
| 123666 | After upgrading X1700 Sockets in HA configuration with add-on cards, created a split-brain condition. | Critical | v22.0.19219 |
| 124297 | Changing the WAN interface speed/duplex settings in the Socket WebUI from a manual value to **Auto** led to an issue where the Socket was frozen and required a full reset. | Critical | v22.0 |
| 126869 | For Azure vSocket HA configuration, after upgrading to new version, vSocket did not receive floating IP configuration from the Azure API. | Critical | v22.0 |
| 127743 | X1700 Socket site did not reconnect to optimal PoP after scheduled maintenance. | High | v22.0.19344 |
