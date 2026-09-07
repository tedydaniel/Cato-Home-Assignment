---
title: "Product Update - Sept. 26th, 2023"
slug: "product-update-sept-26th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-sept-26th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Sept. 26th, 2023

## New Features & Enhancements

- **New Single User Identity to Simplify Policy Enforcement and User Management:** Over the next few weeks, we are unifying users into a [single user identity](/v1/docs/understanding-the-single-user-identity) to enhance policy enforcement and user management.
  - Policies will be enforced whether users are located behind a site or remotely
    - Cato will automatically update all your users to the new single user identity
    - Policies that were enforced for either a User Awareness user or a SDP user, will now be enforced for the new single user identity
  - All users will now be visible from the [Users Directory](/v1/docs/working-with-users) page, providing a single location to manage and view all your users.
- **New Event when Users Proceed after Prompt Page:** The Prompt action shows a page to the users, and then they can choose to proceed to the site. Now, an event is generated when users click **Proceed** on the Prompt page for these policies: [WAN Firewall,](/v1/docs/what-is-the-cato-wan-firewall) [Internet Firewall](/v1/docs/what-is-the-cato-internet-firewall), [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account). These events help admins better understand the users' online behavior, and identify when they visit potentially suspicious website.

## Cato SDP Client Releases

- **Linux Client Version 5.1.0.21:** On Sept. 27th, 2023, we are planning to start the rollout for [Linux Client version 5.1.0.21](/v1/docs/summary-of-cato-linux-client-releases). This version contains bug fixes and enhancements including:
  - Resolved these issues in browserless mode (headless):
    - The Client didn’t automatically recognize a headless device
    - The SMS message for MFA was not sent
    - After the SSO token expired, the Client could not reconnect

## Knowledge Base Updates

[SDP Client Fails To Authenticate When IP Routing is Enabled on Windows](/v1/docs/ip-routing-prevents-windows-client-authentication)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
