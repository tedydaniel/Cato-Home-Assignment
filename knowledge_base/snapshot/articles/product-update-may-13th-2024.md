---
title: "Product Update - May 13th, 2024"
slug: "product-update-may-13th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-may-13th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 13th, 2024

## New Features & Enhancements

- **Network XDR Indication for LAN Socket Port Status**: You can now use [Network XDR](/v1/docs/reviewing-site-operations-stories) to monitor changes to the status of the Socket LAN port with the new LAN Port Down indication.
- **Additional X1700 WAN Interfaces:** Starting with Socket v20, the X1700 and X1700B Sockets support four WAN interfaces.
  - Previously up to three WAN interfaces were supported
- **Comments for XDR Stories:** You can now [add comments to XDR stories](/v1/docs/managing-xops-story-investigations) to document the investigation process and enhance collaboration between team members.
  - Add comments to both Security and Network stories
  - Available for XDR Core and XDR Pro customers
  - Managed XDR customers cannot perform actions or post comments
- **New Device Posture Checks Supported on Linux Client**: You can now include a check for Patch Management and DLP on Linux devices within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and security policies.
  - Supported from Linux Client v5.2 and higher
- **Enhanced Deployment for ESXi vSocket:** The [ESXi vSocket](/v1/docs/configuring-an-esxi-vsocket-site) OVF template now lets you configure static **Network Settings** during the deployment process. This update provides a streamlined setup by eliminating the need to configure static IP settings through the Socket Web UI after deployment.
  - Previously, only DHCP was supported during deployment
  - This feature requires Socket version 19.0 or higher
- **Support for Additional Diffie-Hellman Groups for IPSec IKEv2 Sites:** We now support two new key length groups, 19 and 20, that you can select when configuring the **Diffie-Hellman Group** for an [IPsec IKEv2 site](/v1/docs/configuring-ipsec-ikev2-sites).
- **Cato Cross Connect is Now Cloud Interconnect:** We are renaming our Cross Connect offering to Cloud Interconnect.
  - No impact on existing deployments, we are changing the name in the Cato Management Application
- **Enhanced Visibility of Protected Endpoints**: To enhance the visibility of the endpoints protected by Cato’s Endpoint Protection, we have updated the [Protected Endpoints page](/v1/docs/installing-the-cato-epp-solution) to include:
  - High-level summary of protected endpoints and their status
  - New filter
  - Improved search
  - Refresh button

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
