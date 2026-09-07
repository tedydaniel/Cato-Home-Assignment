---
title: "Product Update - Nov. 20th, 2023"
slug: "product-update-nov-20th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-nov-20th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Nov. 20th, 2023

## New Features & Enhancements

- **Enhanced Visibility for Socket Connectivity Status:** We made the following enhancements for showing the status of Socket ports and links:
  - We combined the Socket physical port and connectivity status into a single **Status** field in these pages:
    - [Topology](/v1/docs/using-the-topology-page) - Socket preview panel
    - [Socket](/v1/docs/managing-sockets) - **Port Status** columns
  - In the Socket page we added a new **Port Status** column for the secondary Socket links
- **Improved Socket Reconnected Event Messages**: We added more details to the event to describe the reason that the Socket reconnected. For example, when the Socket reconnects because the WAN cable is disconnected and reconnected, the event message says: Reconnected after WAN port was physically disconnected.
  - You can also see the improved reconnect reason in the [site Snapshot page](/v1/docs/monitoring-a-site-with-a-snapshot), and the [AccountSnapshot API query](https://api.catonetworks.com/documentation/#definition-AccountSnapshot) in the **tunnelConnectionReason** field

## Cato SDP Client Releases

- **Windows Client Version 5.9:** From November 20th, 2023, we are starting the roll out of Windows Client version 5.9. This version contains:
  - **New Experience for Secured Remote Internet Access (Early Availability)**: We are introducing new features that transform the user experience for secured Internet access. Users can benefit from Internet security based on a one time authentication and Always-On can be used while ensuring business continuity:
    - **Remote Internet Security with One Time Authentication:** For secured Internet access, remote users only need to [authenticate once](/v1/docs/remote-internet-security-with-one-time-authentication).
      - Cato Security policies are always enforced for Internet traffic with this mode, users continuous access without needing to re-authenticate.
    - **New Bypass Mode for Always-On**: Users can temporarily access the Internet without waiting for admin approval. Users provide a reason in the Client and they can temporarily bypass Always-On and disconnect the Client.
      - The duration of the bypass can be configured by administrators
    - **Always-On Recovery Mode:** Users can access the Internet if a connection to the Cato Cloud is unavailable. For example, if a Captive Portal prevents the Client connecting to the Cato Cloud, users can still access the Internet. However, Cato security is bypassed.
  - **Device Posture Check Improves Security Posture**: You can now include a check for DLP within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and security policies.
  - **Client UI Improvements:** We have updated the Client UI, to display:
    - A message if the Client experiences issues establishing a connection to the Cato Cloud
    - The indication if Always-On is enforced is moved to the **Statistics** page
  - **Updated Vendors and Versions for Device Posture Checks:** We updated the [OPSWAT framework](https://www.opswat.com/products/endpoint-security-sdk/device-compliance) used by the Client to version 4.4.3.3714
- **Android Client Version 5.0.1.115:** From November, 20th 2023, the new version of the Android Client will be available in the Google Play store. This version includes:
  - **Device Posture Check Improves Security Posture**: You can now include a check for Device Certificate within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and security policies.
  - **Bug Fixes and Enhancements:** This version contains a number of security enhancements and bug fixes including:
    - Resolved an issue for users with Always-On enabled, the Client could't connect to the Cato Cloud until Airplane mode was enabled and disabled
- **Device Posture Check Improves Security Posture**: You can now include a check for DLP within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and security policies.
  - Supported from macOS version 5.4.3

## PoP Announcements

- The following IP ranges are now available in these PoP locations:
  - **Boston, MA:** 216.205.119.0/24
  - **Minneapolis, MN:** 216.205.117.0/24
  - **Detroit, MI:** 216.205.116.0/24

## Knowledge Base Updates

[Handling Stolen or Compromised Sockets](/v1/docs/handling-stolen-or-compromised-sockets)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
