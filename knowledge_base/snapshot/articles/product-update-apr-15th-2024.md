---
title: "Product Update - Apr. 15th, 2024"
slug: "product-update-apr-15th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-apr-15th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Apr. 15th, 2024

## New Features & Enhancements

- **Mutation API Supports Optimized PoP Selection for Socket Sites:** We updated the [addSocketSite mutation API](https://api.catonetworks.com/documentation/#mutation-addSocketSite) to include the optional City field, which improves the accuracy of Cato’s automatic PoP selection mechanism.
  - In the siteLocation argument, define the city for the Socket site
  - Use the entityLookup query to search for a list of cities
  - The City field is already available in the Cato Management Application
- **User Awareness Identifies SCIM-Provisioned Users in Azure AD Hybrid Join:** The Cato [Identity Agent](/v1/docs/using-cato-identity-agents-for-user-awareness) can now identify SCIM-provisioned users behind a site when using Microsoft Azure AD hybrid join. No SDP license is required for the Identity Agent.
  - Previously, SCIM-provisioned users using Azure AD hybrid join required an SDP license and one-time authentication
  - No action is required for users to be identified by the Identity Agent
  - Supported from Windows Client v5.9 and higher
- Go to the [Cato Product Roadmap](https://support.catonetworks.com/hc/en-us/articles/14517158733853-Cato-Product-Roadmap) in the Knowledge Base to follow the status of upcoming features and enhancements

## Cato SDP Client Releases

- **macOS Client v5.6:** From April 14th, 2024, we are starting to roll out macOS Client version 5.6. This version contains:
  - **Device Posture Check** **for Disk Encryption:** You can now include a check for Disk Encryption within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and Security policies
    - This feature will be gradually enabled over the next few weeks
  - **Updated Client Tray Icon:** We improved how the Client’s tray icon indicates a connected or disconnected status
  - **New Indication of System Notification Status:** On the **Settings** page, we added the status of System Notifications and improved the messaging to highlight their importance
    - System level notifications must be enabled on the device to authenticate using the browser within the Client ([Embedded browser](/v1/docs/configuring-the-authentication-policy-for-cato-clients)).
  - Bug fixes and stability improvements

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
